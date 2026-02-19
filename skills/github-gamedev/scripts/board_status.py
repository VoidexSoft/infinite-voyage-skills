#!/usr/bin/env python3
"""
GitHub Project Board Status Reporter.

Queries a GitHub project board via the gh CLI, groups issues by board column
(To Do, In Progress, Review, Done), reports counts per column and per assignee,
checks WIP (Work-In-Progress) limit violations, and outputs a markdown summary
or JSON report.
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict, field
from datetime import datetime
from collections import defaultdict


# Default WIP limits per column
DEFAULT_WIP_LIMITS: Dict[str, int] = {
    'In Progress': 5,
    'Review': 3,
}

# Canonical column ordering
COLUMN_ORDER = ['To Do', 'In Progress', 'Review', 'Done']


@dataclass
class ColumnStatus:
    """Status of a single board column."""
    name: str
    issue_count: int
    wip_limit: int
    wip_exceeded: bool
    issues: List[Dict[str, Any]] = field(default_factory=list)
    assignee_counts: Dict[str, int] = field(default_factory=dict)


@dataclass
class BoardReport:
    """Full board status report."""
    repo: str
    project: str
    generated_at: str
    total_issues: int
    columns: List[ColumnStatus] = field(default_factory=list)
    wip_violations: List[Dict[str, Any]] = field(default_factory=list)
    assignee_summary: Dict[str, Dict[str, int]] = field(default_factory=dict)


class BoardStatusReporter:
    """Queries GitHub project board and generates status reports."""

    def __init__(
        self,
        repo: str,
        project: str,
        wip_limits: Optional[Dict[str, int]] = None,
    ):
        """
        Initialize reporter.

        Args:
            repo: GitHub repository in owner/repo format
            project: Project board number or name
            wip_limits: Custom WIP limits per column name
        """
        self.repo = repo
        self.project = project
        self.wip_limits = wip_limits or dict(DEFAULT_WIP_LIMITS)
        self._verify_gh_cli()

    def _verify_gh_cli(self) -> None:
        """Verify gh CLI is installed and authenticated."""
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

    def _run_gh(self, args: List[str]) -> str:
        """Execute a gh CLI command and return stdout."""
        try:
            result = subprocess.run(
                ['gh'] + args,
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"gh command failed: {e.stderr.strip()}")

    # ------------------------------------------------------------------
    # Data fetching
    # ------------------------------------------------------------------

    def _fetch_project_items(self) -> List[Dict[str, Any]]:
        """
        Fetch project items using gh CLI.

        Tries the modern `gh project item-list` command first, then
        falls back to the GraphQL API for classic project boards.
        """
        # Strategy 1: gh project item-list (ProjectV2)
        try:
            output = self._run_gh([
                'project', 'item-list', str(self.project),
                '--owner', self.repo.split('/')[0],
                '--format', 'json',
            ])
            data = json.loads(output)
            items = data.get('items', data) if isinstance(data, dict) else data
            if isinstance(items, list):
                return items
        except (RuntimeError, json.JSONDecodeError, KeyError, IndexError):
            pass

        # Strategy 2: gh api for classic project columns
        try:
            owner, repo_name = self.repo.split('/')
            columns_output = self._run_gh([
                'api',
                f'repos/{owner}/{repo_name}/projects/{self.project}/columns',
                '--jq', '.',
            ])
            columns = json.loads(columns_output)
            items: List[Dict[str, Any]] = []
            for col in columns:
                col_name = col.get('name', 'Unknown')
                cards_url = col.get('cards_url', '')
                if not cards_url:
                    continue
                try:
                    cards_output = self._run_gh([
                        'api', cards_url, '--jq', '.',
                    ])
                    cards = json.loads(cards_output)
                    for card in cards:
                        items.append({
                            'status': col_name,
                            'title': card.get('note') or '',
                            'content': card.get('content_url', ''),
                            'assignees': [],
                            'labels': [],
                            'number': None,
                        })
                except (RuntimeError, json.JSONDecodeError):
                    pass
            return items
        except (RuntimeError, json.JSONDecodeError, ValueError):
            pass

        # Strategy 3: Fallback -- list repo issues and infer status from labels
        try:
            output = self._run_gh([
                'issue', 'list',
                '--repo', self.repo,
                '--state', 'all',
                '--json', 'number,title,state,labels,assignees',
                '--limit', '200',
            ])
            issues = json.loads(output)
            items = []
            for issue in issues:
                status = self._infer_column_from_issue(issue)
                assignees = [
                    a.get('login', '') for a in issue.get('assignees', [])
                ]
                label_names = [
                    l.get('name', '') for l in issue.get('labels', [])
                ]
                items.append({
                    'status': status,
                    'title': issue.get('title', ''),
                    'number': issue.get('number'),
                    'assignees': assignees,
                    'labels': label_names,
                })
            return items
        except (RuntimeError, json.JSONDecodeError):
            pass

        return []

    @staticmethod
    def _infer_column_from_issue(issue: Dict[str, Any]) -> str:
        """Infer board column from issue state and labels."""
        state = issue.get('state', '').upper()
        labels = [
            l.get('name', '').lower()
            for l in issue.get('labels', [])
        ]

        if state == 'CLOSED':
            return 'Done'

        for label in labels:
            if 'review' in label or 'pr' in label:
                return 'Review'
            if 'progress' in label or 'wip' in label or 'doing' in label:
                return 'In Progress'

        return 'To Do'

    def _normalize_column(self, raw_status: str) -> str:
        """Normalize column/status name to canonical form."""
        status_lower = raw_status.strip().lower()

        mapping = {
            'todo': 'To Do',
            'to do': 'To Do',
            'to-do': 'To Do',
            'backlog': 'To Do',
            'new': 'To Do',
            'open': 'To Do',
            'in progress': 'In Progress',
            'in-progress': 'In Progress',
            'doing': 'In Progress',
            'active': 'In Progress',
            'started': 'In Progress',
            'review': 'Review',
            'in review': 'Review',
            'in-review': 'Review',
            'pr': 'Review',
            'testing': 'Review',
            'done': 'Done',
            'closed': 'Done',
            'completed': 'Done',
            'merged': 'Done',
        }

        return mapping.get(status_lower, raw_status.strip())

    # ------------------------------------------------------------------
    # Analysis
    # ------------------------------------------------------------------

    def analyze(self) -> BoardReport:
        """Fetch board data and generate analysis report."""
        items = self._fetch_project_items()

        # Group items by column
        column_items: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
        for item in items:
            raw_status = item.get('status', '') or item.get('Status', '') or 'To Do'
            column = self._normalize_column(str(raw_status))
            column_items[column].append(item)

        # Build column statuses
        columns: List[ColumnStatus] = []
        wip_violations: List[Dict[str, Any]] = []
        assignee_totals: Dict[str, Dict[str, int]] = defaultdict(
            lambda: defaultdict(int)
        )

        # Ensure canonical columns exist
        all_columns = set(COLUMN_ORDER) | set(column_items.keys())

        for col_name in COLUMN_ORDER:
            if col_name not in all_columns:
                continue
            col_issues = column_items.get(col_name, [])
            wip_limit = self.wip_limits.get(col_name, 0)
            wip_exceeded = (
                wip_limit > 0 and len(col_issues) > wip_limit
            )

            # Count per assignee
            assignee_counts: Dict[str, int] = defaultdict(int)
            for issue in col_issues:
                assignees = issue.get('assignees', [])
                if isinstance(assignees, list):
                    for a in assignees:
                        name = a if isinstance(a, str) else a.get('login', 'unknown')
                        assignee_counts[name] += 1
                        assignee_totals[name][col_name] += 1
                if not assignees:
                    assignee_counts['unassigned'] += 1
                    assignee_totals['unassigned'][col_name] += 1

            col_status = ColumnStatus(
                name=col_name,
                issue_count=len(col_issues),
                wip_limit=wip_limit,
                wip_exceeded=wip_exceeded,
                issues=col_issues,
                assignee_counts=dict(assignee_counts),
            )
            columns.append(col_status)

            if wip_exceeded:
                wip_violations.append({
                    'column': col_name,
                    'limit': wip_limit,
                    'actual': len(col_issues),
                    'over_by': len(col_issues) - wip_limit,
                })

        # Add any non-canonical columns
        for col_name in sorted(all_columns):
            if col_name in COLUMN_ORDER:
                continue
            col_issues = column_items.get(col_name, [])
            wip_limit = self.wip_limits.get(col_name, 0)
            wip_exceeded = wip_limit > 0 and len(col_issues) > wip_limit

            assignee_counts = defaultdict(int)
            for issue in col_issues:
                assignees = issue.get('assignees', [])
                if isinstance(assignees, list):
                    for a in assignees:
                        name = a if isinstance(a, str) else a.get('login', 'unknown')
                        assignee_counts[name] += 1
                        assignee_totals[name][col_name] += 1
                if not assignees:
                    assignee_counts['unassigned'] += 1

            columns.append(ColumnStatus(
                name=col_name,
                issue_count=len(col_issues),
                wip_limit=wip_limit,
                wip_exceeded=wip_exceeded,
                issues=col_issues,
                assignee_counts=dict(assignee_counts),
            ))

            if wip_exceeded:
                wip_violations.append({
                    'column': col_name,
                    'limit': wip_limit,
                    'actual': len(col_issues),
                    'over_by': len(col_issues) - wip_limit,
                })

        total_issues = sum(c.issue_count for c in columns)

        return BoardReport(
            repo=self.repo,
            project=str(self.project),
            generated_at=datetime.now().isoformat(),
            total_issues=total_issues,
            columns=columns,
            wip_violations=wip_violations,
            assignee_summary={
                name: dict(cols) for name, cols in assignee_totals.items()
            },
        )

    # ------------------------------------------------------------------
    # Output formatting
    # ------------------------------------------------------------------

    @staticmethod
    def format_json(report: BoardReport) -> str:
        """Format report as JSON string."""
        data = asdict(report)
        # Remove full issue lists to keep JSON compact
        for col in data['columns']:
            col['issues'] = [
                {
                    'number': i.get('number'),
                    'title': i.get('title', ''),
                }
                for i in col.get('issues', [])
            ]
        return json.dumps(data, indent=2, default=str)

    @staticmethod
    def format_markdown(report: BoardReport) -> str:
        """Format report as markdown summary."""
        lines: List[str] = []

        lines.append('# Project Board Status')
        lines.append('')
        lines.append(
            f'**Repo**: {report.repo} | '
            f'**Project**: {report.project} | '
            f'**Generated**: {report.generated_at}'
        )
        lines.append('')

        # Column summary table
        lines.append('## Column Summary')
        lines.append('')
        lines.append('| Column | Issues | WIP Limit | Status |')
        lines.append('|--------|--------|-----------|--------|')

        for col in report.columns:
            if col.wip_limit > 0:
                limit_str = str(col.wip_limit)
                status = 'EXCEEDED' if col.wip_exceeded else 'OK'
            else:
                limit_str = '-'
                status = '-'
            lines.append(
                f'| {col.name} | {col.issue_count} | {limit_str} | {status} |'
            )

        lines.append('')
        lines.append(f'**Total Issues**: {report.total_issues}')
        lines.append('')

        # WIP violations
        if report.wip_violations:
            lines.append('## WIP Limit Violations')
            lines.append('')
            for v in report.wip_violations:
                lines.append(
                    f'- **{v["column"]}**: {v["actual"]} issues '
                    f'(limit: {v["limit"]}, over by {v["over_by"]})'
                )
            lines.append('')

        # Per-assignee breakdown
        if report.assignee_summary:
            lines.append('## Issues by Assignee')
            lines.append('')

            # Gather all column names
            all_cols = [c.name for c in report.columns]
            header = '| Assignee | ' + ' | '.join(all_cols) + ' | Total |'
            separator = '|' + '|'.join(['--------'] * (len(all_cols) + 2)) + '|'
            lines.append(header)
            lines.append(separator)

            for assignee in sorted(report.assignee_summary.keys()):
                col_counts = report.assignee_summary[assignee]
                counts = [str(col_counts.get(c, 0)) for c in all_cols]
                total = sum(col_counts.values())
                lines.append(
                    f'| {assignee} | ' + ' | '.join(counts) + f' | {total} |'
                )

            lines.append('')

        # Issue lists per column
        for col in report.columns:
            if not col.issues:
                continue
            lines.append(f'## {col.name} ({col.issue_count})')
            lines.append('')
            for issue in col.issues:
                number = issue.get('number')
                title = issue.get('title', 'Untitled')
                prefix = f'#{number}' if number else '-'
                lines.append(f'- {prefix}: {title}')
            lines.append('')

        return '\n'.join(lines)

    # ------------------------------------------------------------------
    # Save
    # ------------------------------------------------------------------

    def save_report(
        self,
        report: BoardReport,
        output_path: str,
        fmt: str = 'markdown',
    ) -> None:
        """Save report to file."""
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        if fmt == 'json':
            content = self.format_json(report)
        else:
            content = self.format_markdown(report)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Report saved to {output_path}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='GitHub project board status reporter'
    )
    parser.add_argument(
        '-r', '--repo',
        required=True,
        help='GitHub repository (owner/repo)'
    )
    parser.add_argument(
        '-p', '--project',
        required=True,
        help='Project board number or name'
    )
    parser.add_argument(
        '-f', '--format',
        choices=['markdown', 'json'],
        default='markdown',
        help='Output format (default: markdown)'
    )
    parser.add_argument(
        '-o', '--output',
        default=None,
        help='Output file path (default: stdout)'
    )
    parser.add_argument(
        '--wip-limit',
        type=str,
        action='append',
        default=[],
        help=(
            'WIP limit in "Column:Limit" format '
            '(e.g., "In Progress:5"). Can be specified multiple times.'
        )
    )

    args = parser.parse_args()

    # Parse custom WIP limits
    wip_limits = dict(DEFAULT_WIP_LIMITS)
    for wip_str in args.wip_limit:
        try:
            col, limit = wip_str.rsplit(':', 1)
            wip_limits[col.strip()] = int(limit.strip())
        except (ValueError, IndexError):
            print(f"Warning: Invalid WIP limit format: '{wip_str}'. Use 'Column:Limit'.")

    # Generate report
    reporter = BoardStatusReporter(
        repo=args.repo,
        project=args.project,
        wip_limits=wip_limits,
    )

    print(f"Fetching board status for {args.repo} (project: {args.project})...")
    report = reporter.analyze()

    # Format output
    if args.format == 'json':
        output_content = reporter.format_json(report)
    else:
        output_content = reporter.format_markdown(report)

    # Write or print
    if args.output:
        reporter.save_report(report, args.output, args.format)
    else:
        print(output_content)

    # Print quick summary to stderr so it appears even when stdout is piped
    print(f"\nBoard Summary:", file=sys.stderr)
    for col in report.columns:
        marker = ' [!WIP EXCEEDED]' if col.wip_exceeded else ''
        print(
            f"  {col.name}: {col.issue_count} issues{marker}",
            file=sys.stderr,
        )
    print(f"  Total: {report.total_issues}", file=sys.stderr)

    if report.wip_violations:
        print(f"\nWIP Violations: {len(report.wip_violations)}", file=sys.stderr)
        for v in report.wip_violations:
            print(
                f"  {v['column']}: {v['actual']}/{v['limit']} "
                f"(+{v['over_by']})",
                file=sys.stderr,
            )


if __name__ == '__main__':
    main()
