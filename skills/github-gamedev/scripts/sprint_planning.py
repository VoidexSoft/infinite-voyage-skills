#!/usr/bin/env python3
"""
Sprint Planning Utility - Plans sprints from GitHub backlog issues.

Queries a GitHub repository's backlog via gh CLI, sorts by priority labels,
calculates team capacity, and suggests sprint scope based on story points.
Outputs a sprint plan as markdown or JSON.
"""

import subprocess
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime
from dataclasses import dataclass, asdict, field
from collections import defaultdict


# ---------------------------------------------------------------------------
# Priority configuration
# ---------------------------------------------------------------------------

PRIORITY_ORDER: Dict[str, int] = {
    'priority-critical': 0,
    'priority-high': 1,
    'priority-medium': 2,
    'priority-low': 3,
}

DEFAULT_POINTS_PER_DEV_PER_DAY = 1.0


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class BacklogIssue:
    """Represents a single backlog issue from GitHub."""
    number: int
    title: str
    state: str
    labels: List[str]
    assignees: List[str]
    story_points: int
    priority: str
    priority_rank: int
    url: str = ""
    body: str = ""


@dataclass
class SprintPlan:
    """Complete sprint plan with capacity and issue assignments."""
    repo: str
    milestone: Optional[str]
    sprint_duration_days: int
    team_size: int
    capacity_points: float
    included_issues: List[BacklogIssue]
    overflow_issues: List[BacklogIssue]
    total_points_included: int
    total_points_overflow: int
    utilisation_pct: float
    generated_at: str
    priority_breakdown: Dict[str, int] = field(default_factory=dict)
    assignee_breakdown: Dict[str, int] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# GitHub interaction
# ---------------------------------------------------------------------------

def verify_gh_cli() -> None:
    """Verify that the gh CLI is installed and authenticated."""
    try:
        subprocess.run(
            ['gh', '--version'],
            capture_output=True,
            check=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        raise RuntimeError(
            "gh CLI not found or not authenticated. "
            "Install: https://cli.github.com/"
        )


def fetch_backlog_issues(
    repo: str,
    milestone: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """
    Fetch open backlog issues from a GitHub repository.

    Args:
        repo: GitHub repository in owner/repo format.
        milestone: Optional milestone name to filter by.

    Returns:
        List of issue dictionaries from the gh CLI.
    """
    cmd = (
        f'gh issue list --repo {repo} --state open --limit 500 '
        f'--json "number,title,state,labels,assignees,createdAt,body,url"'
    )

    if milestone:
        cmd += f" --milestone '{milestone}'"

    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            check=True,
        )
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to fetch issues: {e.stderr}")


# ---------------------------------------------------------------------------
# Issue parsing helpers
# ---------------------------------------------------------------------------

def extract_story_points(labels: List[Dict[str, str]]) -> int:
    """
    Extract story points from issue labels.

    Looks for labels in the format ``points-N`` (e.g. ``points-3``).
    Returns 1 as the default when no points label is found.
    """
    for label in labels:
        name = label.get('name', '')
        if name.startswith('points-'):
            try:
                return int(name.split('-', 1)[1])
            except (IndexError, ValueError):
                pass
    return 1


def extract_priority(labels: List[Dict[str, str]]) -> tuple:
    """
    Extract the highest-priority label from an issue's label set.

    Returns:
        Tuple of (priority_label, priority_rank).
        Issues without a recognised priority label default to medium (rank 2).
    """
    best_label = 'priority-medium'
    best_rank = PRIORITY_ORDER.get('priority-medium', 2)

    for label in labels:
        name = label.get('name', '')
        if name in PRIORITY_ORDER:
            rank = PRIORITY_ORDER[name]
            if rank < best_rank:
                best_label = name
                best_rank = rank

    return best_label, best_rank


def parse_issues(raw_issues: List[Dict[str, Any]]) -> List[BacklogIssue]:
    """
    Convert raw GitHub issue dicts into typed BacklogIssue objects.

    Args:
        raw_issues: Issue list as returned by the gh CLI.

    Returns:
        Sorted list of BacklogIssue (highest priority first, then by points
        descending within the same priority tier).
    """
    parsed: List[BacklogIssue] = []

    for issue in raw_issues:
        labels_raw = issue.get('labels', [])
        label_names = [l.get('name', '') for l in labels_raw]
        assignees = [a.get('login', '') for a in issue.get('assignees', [])]
        points = extract_story_points(labels_raw)
        priority_label, priority_rank = extract_priority(labels_raw)

        parsed.append(BacklogIssue(
            number=issue.get('number', 0),
            title=issue.get('title', ''),
            state=issue.get('state', 'OPEN'),
            labels=label_names,
            assignees=assignees,
            story_points=points,
            priority=priority_label,
            priority_rank=priority_rank,
            url=issue.get('url', ''),
            body=issue.get('body', ''),
        ))

    # Sort: priority rank ascending, then story points descending (big items first)
    parsed.sort(key=lambda i: (i.priority_rank, -i.story_points))
    return parsed


# ---------------------------------------------------------------------------
# Capacity & planning
# ---------------------------------------------------------------------------

def calculate_capacity(
    team_size: int,
    sprint_days: int,
    velocity: float = DEFAULT_POINTS_PER_DEV_PER_DAY,
) -> float:
    """
    Calculate sprint capacity in story points.

    Args:
        team_size: Number of developers.
        sprint_days: Duration of the sprint in working days.
        velocity: Expected story points per developer per day.

    Returns:
        Total story point capacity for the sprint.
    """
    return team_size * sprint_days * velocity


def build_sprint_plan(
    repo: str,
    issues: List[BacklogIssue],
    capacity: float,
    milestone: Optional[str],
    sprint_days: int,
    team_size: int,
) -> SprintPlan:
    """
    Select issues that fit within the sprint capacity.

    Issues are consumed in priority order. An issue is included only if its
    story points fit within the remaining capacity.

    Args:
        repo: Repository identifier.
        issues: Priority-sorted backlog issues.
        capacity: Total available story points.
        milestone: Milestone name (may be None).
        sprint_days: Sprint duration in days.
        team_size: Number of developers.

    Returns:
        A fully populated SprintPlan.
    """
    included: List[BacklogIssue] = []
    overflow: List[BacklogIssue] = []
    remaining = capacity

    for issue in issues:
        if issue.story_points <= remaining:
            included.append(issue)
            remaining -= issue.story_points
        else:
            overflow.append(issue)

    total_included = sum(i.story_points for i in included)
    total_overflow = sum(i.story_points for i in overflow)

    # Priority breakdown for included issues
    priority_breakdown: Dict[str, int] = defaultdict(int)
    for issue in included:
        priority_breakdown[issue.priority] += 1

    # Assignee breakdown for included issues
    assignee_breakdown: Dict[str, int] = defaultdict(int)
    for issue in included:
        if issue.assignees:
            for assignee in issue.assignees:
                assignee_breakdown[assignee] += 1
        else:
            assignee_breakdown['unassigned'] += 1

    utilisation = (total_included / capacity * 100) if capacity > 0 else 0.0

    return SprintPlan(
        repo=repo,
        milestone=milestone,
        sprint_duration_days=sprint_days,
        team_size=team_size,
        capacity_points=capacity,
        included_issues=included,
        overflow_issues=overflow,
        total_points_included=total_included,
        total_points_overflow=total_overflow,
        utilisation_pct=round(utilisation, 1),
        generated_at=datetime.now().isoformat(),
        priority_breakdown=dict(priority_breakdown),
        assignee_breakdown=dict(assignee_breakdown),
    )


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def format_markdown(plan: SprintPlan) -> str:
    """
    Render the sprint plan as a Markdown document.

    Args:
        plan: The computed SprintPlan.

    Returns:
        Markdown string.
    """
    lines: List[str] = []

    lines.append("# Sprint Plan")
    lines.append("")
    lines.append(f"Generated: {plan.generated_at}")
    lines.append(f"Repository: `{plan.repo}`")
    if plan.milestone:
        lines.append(f"Milestone: **{plan.milestone}**")
    lines.append("")

    # Capacity overview
    lines.append("## Capacity")
    lines.append("")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Team size | {plan.team_size} |")
    lines.append(f"| Sprint duration | {plan.sprint_duration_days} days |")
    lines.append(f"| Capacity | {plan.capacity_points:.0f} points |")
    lines.append(f"| Planned | {plan.total_points_included} points |")
    lines.append(f"| Utilisation | {plan.utilisation_pct}% |")
    lines.append("")

    # Priority breakdown
    if plan.priority_breakdown:
        lines.append("## Priority Breakdown")
        lines.append("")
        lines.append("| Priority | Count |")
        lines.append("|----------|-------|")
        for priority in ['priority-critical', 'priority-high', 'priority-medium', 'priority-low']:
            count = plan.priority_breakdown.get(priority, 0)
            if count > 0:
                display = priority.replace('priority-', '').capitalize()
                lines.append(f"| {display} | {count} |")
        lines.append("")

    # Assignee breakdown
    if plan.assignee_breakdown:
        lines.append("## Assignee Breakdown")
        lines.append("")
        lines.append("| Assignee | Issues |")
        lines.append("|----------|--------|")
        for assignee, count in sorted(plan.assignee_breakdown.items()):
            lines.append(f"| {assignee} | {count} |")
        lines.append("")

    # Included issues table
    lines.append("## Sprint Scope")
    lines.append("")
    if plan.included_issues:
        lines.append("| # | Title | Points | Priority | Assignees |")
        lines.append("|---|-------|--------|----------|-----------|")
        for issue in plan.included_issues:
            assignees = ', '.join(issue.assignees) if issue.assignees else 'unassigned'
            display_priority = issue.priority.replace('priority-', '').capitalize()
            lines.append(
                f"| #{issue.number} | {issue.title} | {issue.story_points} "
                f"| {display_priority} | {assignees} |"
            )
    else:
        lines.append("_No issues fit within the sprint capacity._")
    lines.append("")

    # Overflow / deferred
    if plan.overflow_issues:
        lines.append("## Overflow (Deferred)")
        lines.append("")
        lines.append(f"Total deferred points: **{plan.total_points_overflow}**")
        lines.append("")
        lines.append("| # | Title | Points | Priority |")
        lines.append("|---|-------|--------|----------|")
        for issue in plan.overflow_issues:
            display_priority = issue.priority.replace('priority-', '').capitalize()
            lines.append(
                f"| #{issue.number} | {issue.title} | {issue.story_points} "
                f"| {display_priority} |"
            )
        lines.append("")

    return '\n'.join(lines)


def format_json(plan: SprintPlan) -> str:
    """
    Render the sprint plan as a JSON string.

    Args:
        plan: The computed SprintPlan.

    Returns:
        Pretty-printed JSON string.
    """
    data = asdict(plan)
    return json.dumps(data, indent=2, default=str)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Sprint planning utility - suggest sprint scope from GitHub backlog'
    )
    parser.add_argument(
        '-r', '--repo',
        required=True,
        help='GitHub repository (owner/repo)',
    )
    parser.add_argument(
        '-m', '--milestone',
        default=None,
        help='Filter backlog by milestone name',
    )
    parser.add_argument(
        '-d', '--duration',
        type=int,
        default=14,
        help='Sprint duration in working days (default: 14)',
    )
    parser.add_argument(
        '-t', '--team-size',
        type=int,
        default=4,
        help='Number of developers on the team (default: 4)',
    )
    parser.add_argument(
        '-v', '--velocity',
        type=float,
        default=DEFAULT_POINTS_PER_DEV_PER_DAY,
        help=f'Story points per developer per day (default: {DEFAULT_POINTS_PER_DEV_PER_DAY})',
    )
    parser.add_argument(
        '-f', '--format',
        choices=['markdown', 'json'],
        default='markdown',
        help='Output format (default: markdown)',
    )
    parser.add_argument(
        '-o', '--output',
        default=None,
        help='Output file path (default: stdout)',
    )

    args = parser.parse_args()

    # Verify gh CLI availability
    verify_gh_cli()

    # Fetch and parse backlog
    print(f"Fetching backlog from {args.repo}...")
    raw_issues = fetch_backlog_issues(args.repo, milestone=args.milestone)
    print(f"  Found {len(raw_issues)} open issue(s)")

    if not raw_issues:
        print("No open issues found. Nothing to plan.")
        return

    issues = parse_issues(raw_issues)

    # Calculate capacity
    capacity = calculate_capacity(
        team_size=args.team_size,
        sprint_days=args.duration,
        velocity=args.velocity,
    )
    print(f"  Team capacity: {capacity:.0f} points "
          f"({args.team_size} devs x {args.duration} days x {args.velocity} pts/day)")

    # Build plan
    plan = build_sprint_plan(
        repo=args.repo,
        issues=issues,
        capacity=capacity,
        milestone=args.milestone,
        sprint_days=args.duration,
        team_size=args.team_size,
    )

    # Format output
    if args.format == 'json':
        output = format_json(plan)
    else:
        output = format_markdown(plan)

    # Write or print
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"\nSprint plan saved to {args.output}")
    else:
        print("")
        print(output)

    # Summary to stderr-style console line
    print(f"\nSummary: {len(plan.included_issues)} issues planned "
          f"({plan.total_points_included} pts), "
          f"{len(plan.overflow_issues)} deferred "
          f"({plan.total_points_overflow} pts), "
          f"{plan.utilisation_pct}% utilisation")


if __name__ == '__main__':
    main()
