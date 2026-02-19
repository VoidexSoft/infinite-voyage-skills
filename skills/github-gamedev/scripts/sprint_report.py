#!/usr/bin/env python3
"""
Sprint Report Generator - Creates sprint reports from GitHub issues.

Queries GitHub via gh CLI for issues in a milestone/project,
calculates velocity, groups by category, and generates markdown report.
"""

import subprocess
import json
import re
import argparse
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime
from collections import defaultdict


class SprintReporter:
    """Generates sprint reports from GitHub."""

    def __init__(self, repo: str, milestone: Optional[str] = None, project: Optional[str] = None):
        """Initialize reporter with repo and optional milestone/project."""
        self.repo = repo
        self.milestone = milestone
        self.project = project

        # Verify gh CLI
        self._verify_gh_cli()

    def _verify_gh_cli(self) -> None:
        """Verify gh CLI is installed and authenticated."""
        try:
            subprocess.run(
                ['gh', '--version'],
                capture_output=True,
                check=True
            )
        except (FileNotFoundError, subprocess.CalledProcessError):
            raise RuntimeError(
                "gh CLI not found or not authenticated. "
                "Install: https://cli.github.com/"
            )

    def _run_gh_query(self, query: str) -> List[Dict[str, Any]]:
        """Execute gh CLI query and return JSON results."""
        try:
            result = subprocess.run(
                ['gh', 'issue', 'list', '--repo', self.repo, '--json', query],
                capture_output=True,
                text=True,
                check=True
            )
            return json.loads(result.stdout)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"gh query failed: {e.stderr}")

    def _get_issues(self, status: str = 'all') -> List[Dict[str, Any]]:
        """Get issues by status (all, open, closed)."""
        filters = f"--state {status}"

        if self.milestone:
            filters += f" --milestone '{self.milestone}'"

        try:
            result = subprocess.run(
                (
                    f'gh issue list --repo {self.repo} '
                    f'{filters} '
                    f'--json "number,title,state,labels,assignees,createdAt,closedAt,body"'
                ),
                shell=True,
                capture_output=True,
                text=True,
                check=True
            )
            return json.loads(result.stdout)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to fetch issues: {e.stderr}")

    def _get_project_issues(self) -> List[Dict[str, Any]]:
        """Get issues from project."""
        try:
            result = subprocess.run(
                (
                    f'gh project item-list {self.project} '
                    f'--repo {self.repo} '
                    f'--format json'
                ),
                shell=True,
                capture_output=True,
                text=True,
                check=True
            )
            return json.loads(result.stdout)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to fetch project items: {e.stderr}")

    def calculate_velocity(self, issues: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate sprint velocity metrics."""
        closed_issues = [i for i in issues if i.get('state') == 'CLOSED']
        open_issues = [i for i in issues if i.get('state') == 'OPEN']

        # Extract story points from labels (assumes label format "points-5")
        def extract_points(labels: List[Dict[str, str]]) -> int:
            if not labels:
                return 1  # Default: 1 point
            for label in labels:
                label_name = label.get('name', '')
                if label_name.startswith('points-'):
                    try:
                        return int(label_name.split('-')[1])
                    except (IndexError, ValueError):
                        pass
            return 1

        closed_points = sum(extract_points(i.get('labels', [])) for i in closed_issues)
        open_points = sum(extract_points(i.get('labels', [])) for i in open_issues)

        return {
            'total_issues': len(issues),
            'closed_count': len(closed_issues),
            'open_count': len(open_issues),
            'closed_points': closed_points,
            'open_points': open_points,
            'total_points': closed_points + open_points,
            'velocity': closed_points,
            'completion_rate': len(closed_issues) / len(issues) if issues else 0,
        }

    def group_by_label(self, issues: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """Group issues by primary label."""
        grouped = defaultdict(list)

        for issue in issues:
            labels = issue.get('labels', [])
            if labels:
                # Use first label as primary
                primary_label = labels[0].get('name', 'untagged')
            else:
                primary_label = 'untagged'

            grouped[primary_label].append(issue)

        return dict(grouped)

    def group_by_assignee(self, issues: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """Group issues by assignee."""
        grouped = defaultdict(list)

        for issue in issues:
            assignees = issue.get('assignees', [])
            if assignees:
                for assignee in assignees:
                    grouped[assignee.get('login', 'unassigned')].append(issue)
            else:
                grouped['unassigned'].append(issue)

        return dict(grouped)

    def generate_report(self) -> str:
        """Generate markdown sprint report."""
        # Fetch issues
        all_issues = self._get_issues('all')
        open_issues = self._get_issues('open')
        closed_issues = self._get_issues('closed')

        # Calculate metrics
        velocity = self.calculate_velocity(all_issues)

        # Group issues
        by_label = self.group_by_label(all_issues)
        by_assignee_open = self.group_by_assignee(open_issues)

        # Generate markdown
        report = "# Sprint Report\n\n"

        # Header info
        report += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        if self.milestone:
            report += f"Milestone: {self.milestone}\n\n"
        if self.project:
            report += f"Project: {self.project}\n\n"

        # Velocity section
        report += "## Velocity\n\n"
        report += f"- **Total Issues**: {velocity['total_issues']}\n"
        report += f"- **Closed**: {velocity['closed_count']} ({velocity['completion_rate']:.1%})\n"
        report += f"- **Open**: {velocity['open_count']}\n"
        report += f"- **Story Points (Closed)**: {velocity['closed_points']}\n"
        report += f"- **Story Points (Total)**: {velocity['total_points']}\n"
        report += f"- **Velocity**: {velocity['velocity']} points\n\n"

        # Status breakdown
        report += "## Status Breakdown\n\n"
        report += "| Status | Count | %  |\n"
        report += "|--------|-------|----|\n"
        report += f"| Closed | {velocity['closed_count']} | {velocity['completion_rate']:.1%} |\n"
        report += f"| Open   | {velocity['open_count']} | {1 - velocity['completion_rate']:.1%} |\n\n"

        # By category/label
        if by_label:
            report += "## By Category\n\n"
            for label, issues in sorted(by_label.items()):
                closed_count = sum(1 for i in issues if i.get('state') == 'CLOSED')
                report += f"### {label.capitalize()}\n\n"
                report += f"- Total: {len(issues)}\n"
                report += f"- Closed: {closed_count}\n\n"

        # By assignee (open issues only)
        if by_assignee_open:
            report += "## Open Issues by Assignee\n\n"
            for assignee, issues in sorted(by_assignee_open.items()):
                report += f"### {assignee}\n\n"
                for issue in issues:
                    report += f"- #{issue['number']}: {issue['title']}\n"
                report += "\n"

        # Issue list (closed)
        if closed_issues:
            report += "## Completed Issues\n\n"
            for issue in closed_issues:
                report += f"- ✓ #{issue['number']}: {issue['title']}\n"
            report += "\n"

        # Issue list (open)
        if open_issues:
            report += "## Open Issues\n\n"
            for issue in open_issues:
                report += f"- [ ] #{issue['number']}: {issue['title']}\n"
            report += "\n"

        return report

    def save_report(self, output_path: str) -> None:
        """Save report to file."""
        report = self.generate_report()

        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)

        print(f"Report saved to {output_path}")

    def print_report(self) -> None:
        """Print report to stdout."""
        report = self.generate_report()
        print(report)


def _convert_format(report_md: str, fmt: str, reporter: SprintReporter) -> str:
    """Convert markdown report to the requested format."""
    if fmt == 'markdown':
        return report_md

    if fmt == 'html':
        # Simple markdown-to-HTML conversion
        html = report_md
        html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
        html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
        html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
        html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
        html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
        html = re.sub(r'\|(.+)\|', r'<td>\1</td>', html)
        lines = html.split('\n')
        result = ['<html><body>']
        for line in lines:
            if line.strip().startswith('<'):
                result.append(line)
            elif line.strip():
                result.append(f'<p>{line}</p>')
        result.append('</body></html>')
        return '\n'.join(result)

    if fmt == 'json':
        all_issues = reporter._get_issues('all')
        velocity = reporter.calculate_velocity(all_issues)
        by_label = reporter.group_by_label(all_issues)
        by_assignee = reporter.group_by_assignee(all_issues)
        return json.dumps({
            'generated': datetime.now().isoformat(),
            'milestone': reporter.milestone,
            'velocity': velocity,
            'by_label': {k: len(v) for k, v in by_label.items()},
            'by_assignee': {k: len(v) for k, v in by_assignee.items()},
            'issues': all_issues,
        }, indent=2, default=str)

    if fmt == 'slack':
        # Slack-friendly formatting (mrkdwn)
        slack = report_md
        slack = re.sub(r'^# (.+)$', r'*\1*', slack, flags=re.MULTILINE)
        slack = re.sub(r'^## (.+)$', r'*\1*', slack, flags=re.MULTILINE)
        slack = re.sub(r'^### (.+)$', r'*\1*', slack, flags=re.MULTILINE)
        # Convert markdown tables to simple text
        slack = re.sub(r'\|[-|]+\|', '', slack)
        return slack

    if fmt == 'csv':
        all_issues = reporter._get_issues('all')
        lines = ['number,title,state,labels,assignees']
        for issue in all_issues:
            labels = ';'.join(l.get('name', '') for l in issue.get('labels', []))
            assignees = ';'.join(a.get('login', '') for a in issue.get('assignees', []))
            title = issue.get('title', '').replace(',', ';')
            lines.append(f"{issue.get('number', '')},{title},{issue.get('state', '')},{labels},{assignees}")
        return '\n'.join(lines)

    return report_md


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate sprint report from GitHub issues'
    )
    parser.add_argument(
        '-r', '--repo',
        required=True,
        help='GitHub repository (owner/repo)'
    )
    parser.add_argument(
        '-m', '--milestone',
        help='Filter by milestone name'
    )
    parser.add_argument(
        '-p', '--project',
        help='Filter by project ID'
    )
    parser.add_argument(
        '-s', '--sprint',
        help='Sprint identifier (e.g. "Sprint 5"). If provided, used as milestone filter and report title.'
    )
    parser.add_argument(
        '-f', '--format',
        choices=['markdown', 'html', 'json', 'slack', 'csv'],
        default='markdown',
        help='Output format (default: markdown)'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output file path (default: stdout)'
    )

    args = parser.parse_args()

    # Sprint flag overrides milestone
    milestone = args.sprint or args.milestone

    # Generate report
    reporter = SprintReporter(
        repo=args.repo,
        milestone=milestone,
        project=args.project
    )

    report_md = reporter.generate_report()

    # Convert format
    output = _convert_format(report_md, args.format, reporter)

    if args.output:
        output_file = Path(args.output)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"Report saved to {args.output}")
    else:
        print(output)


if __name__ == '__main__':
    main()
