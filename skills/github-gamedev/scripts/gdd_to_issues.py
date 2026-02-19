#!/usr/bin/env python3
"""
GDD to GitHub Issues - Converts GDD markdown into GitHub issues.

Parses a GDD file, extracts sections and tasks (TODO, IMPLEMENT, DESIGN, etc.),
and generates GitHub issue creation commands or creates them directly.
"""

import re
import argparse
import subprocess
import json
from pathlib import Path
from typing import List, Tuple, Optional, Dict, Any
from dataclasses import dataclass


@dataclass
class GDDTask:
    """Represents a task extracted from GDD."""
    title: str
    description: str
    section: str
    task_type: str  # 'TODO', 'IMPLEMENT', 'DESIGN', 'TEST', etc.
    labels: List[str]
    body: str


class GDDParser:
    """Parses GDD markdown and extracts tasks."""

    TASK_PATTERNS = {
        r'TODO:\s*(.+?)(?:\n|$)': 'todo',
        r'IMPLEMENT:\s*(.+?)(?:\n|$)': 'implement',
        r'DESIGN:\s*(.+?)(?:\n|$)': 'design',
        r'TEST:\s*(.+?)(?:\n|$)': 'test',
        r'BALANCE:\s*(.+?)(?:\n|$)': 'balance',
        r'FIX:\s*(.+?)(?:\n|$)': 'fix',
        r'OPTIMIZE:\s*(.+?)(?:\n|$)': 'optimize',
        r'DOCUMENT:\s*(.+?)(?:\n|$)': 'documentation',
    }

    # Standard disciplines for feature decomposition
    DECOMPOSITION_DISCIPLINES = [
        {'name': 'Design', 'label': 'design', 'prefix': '[Design]',
         'desc': 'Design specification and requirements for'},
        {'name': 'Code', 'label': 'implement', 'prefix': '[Code]',
         'desc': 'Implementation of'},
        {'name': 'Art', 'label': 'art', 'prefix': '[Art]',
         'desc': 'Art assets and visual design for'},
        {'name': 'Audio', 'label': 'audio', 'prefix': '[Audio]',
         'desc': 'Sound effects and music for'},
        {'name': 'QA', 'label': 'test', 'prefix': '[QA]',
         'desc': 'Testing and quality assurance for'},
        {'name': 'Balance', 'label': 'balance', 'prefix': '[Balance]',
         'desc': 'Numerical balance and tuning for'},
    ]

    def __init__(self, gdd_path: str, feature: Optional[str] = None):
        """Initialize parser with GDD file path and optional feature filter."""
        self.gdd_path = Path(gdd_path)
        if not self.gdd_path.exists():
            raise ValueError(f"GDD file not found: {gdd_path}")

        with open(self.gdd_path, 'r', encoding='utf-8') as f:
            self.content = f.read()

        self.feature = feature
        self.tasks: List[GDDTask] = []

    def _extract_section(self, match) -> str:
        """Extract the section header from content before match."""
        start_pos = match.start()
        content_before = self.content[:start_pos]

        # Find last header
        headers = re.finditer(r'^#+ (.+)$', content_before, re.MULTILINE)
        sections = list(headers)

        if sections:
            return sections[-1].group(1)
        return 'Uncategorized'

    def _categorize_by_section(self, section: str) -> str:
        """Categorize section into GitHub labels."""
        section_lower = section.lower()

        if any(x in section_lower for x in ['mechanic', 'gameplay', 'core', 'system']):
            return 'mechanic'
        elif any(x in section_lower for x in ['narrative', 'story', 'dialogue', 'character']):
            return 'narrative'
        elif any(x in section_lower for x in ['level', 'world', 'map']):
            return 'level-design'
        elif any(x in section_lower for x in ['economy', 'progression', 'balance', 'tuning']):
            return 'economy'
        elif any(x in section_lower for x in ['art', 'visual', 'animation', 'effect']):
            return 'art'
        elif any(x in section_lower for x in ['audio', 'sound', 'music']):
            return 'audio'
        elif any(x in section_lower for x in ['ui', 'ux', 'interface', 'hud']):
            return 'ui'
        elif any(x in section_lower for x in ['technical', 'architecture', 'performance', 'optimization']):
            return 'technical'
        else:
            return 'gameplay'

    def _extract_sections_with_content(self) -> List[Tuple[str, str, int]]:
        """Extract all sections with their content and heading level."""
        sections = []
        header_pattern = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)
        matches = list(header_pattern.finditer(self.content))

        for i, match in enumerate(matches):
            level = len(match.group(1))
            title = match.group(2).strip()
            start = match.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(self.content)
            content = self.content[start:end].strip()
            sections.append((title, content, level))

        return sections

    def _decompose_feature(self, feature_name: str, section_title: str, section_content: str) -> List[GDDTask]:
        """Decompose a feature section into discipline-based tasks."""
        tasks = []
        for discipline in self.DECOMPOSITION_DISCIPLINES:
            title = f"{discipline['prefix']} {feature_name}"[:60]
            body = (
                f"## {discipline['name']} — {feature_name}\n\n"
                f"{discipline['desc']} **{feature_name}**.\n\n"
                f"### GDD Context\n\n"
                f"From section: **{section_title}**\n\n"
                f"{section_content[:500]}\n\n"
                f"### Acceptance Criteria\n\n"
                f"- [ ] {discipline['name']} work completed for {feature_name}\n"
                f"- [ ] Reviewed by team lead\n"
                f"- [ ] Integrated with related systems\n"
            )

            task = GDDTask(
                title=title,
                description=f"{discipline['desc']} {feature_name}",
                section=section_title,
                task_type=discipline['label'].upper(),
                labels=[discipline['label'], 'from-gdd', 'feature-decomposition'],
                body=body,
            )
            tasks.append(task)

        return tasks

    def parse(self) -> List[GDDTask]:
        """Parse GDD and extract all tasks.

        If self.feature is set, performs structured feature decomposition
        on matching sections. Otherwise, scans for explicit task markers.
        """
        if self.feature:
            return self._parse_feature_decomposition()
        return self._parse_task_markers()

    def _parse_feature_decomposition(self) -> List[GDDTask]:
        """Parse GDD using feature decomposition mode."""
        sections = self._extract_sections_with_content()
        feature_lower = self.feature.lower()

        matched = False
        for title, content, level in sections:
            if feature_lower in title.lower():
                matched = True
                self.tasks.extend(
                    self._decompose_feature(self.feature, title, content)
                )

        if not matched:
            # Fallback: treat the feature name as the section
            # and use the entire GDD content as context
            print(f"Warning: No section matching '{self.feature}' found. "
                  f"Generating generic decomposition.")
            self.tasks.extend(
                self._decompose_feature(self.feature, 'GDD', self.content[:500])
            )

        # Also pick up any explicit task markers in the matched sections
        self._parse_task_markers()

        return self.tasks

    def _parse_task_markers(self) -> List[GDDTask]:
        """Parse GDD and extract tasks from explicit markers."""
        # Find all task markers
        for pattern, task_type in self.TASK_PATTERNS.items():
            for match in re.finditer(pattern, self.content):
                task_text = match.group(1).strip()
                section = self._extract_section(match)
                category = self._categorize_by_section(section)

                # Extract context (paragraph containing task)
                start = max(0, match.start() - 200)
                end = min(len(self.content), match.end() + 200)
                context = self.content[start:end].strip()

                # Create task
                task = GDDTask(
                    title=task_text[:60],  # Truncate to reasonable title length
                    description=task_text,
                    section=section,
                    task_type=task_type.upper(),
                    labels=[category, task_type, 'from-gdd'],
                    body=f"From GDD section: **{section}**\n\n{context}\n\nType: {task_type.upper()}"
                )

                self.tasks.append(task)

        return self.tasks

    def generate_gh_commands(self) -> List[str]:
        """Generate gh CLI commands to create issues."""
        commands = []

        for task in self.tasks:
            # Escape special characters
            title = task.title.replace('"', '\\"')
            body = task.body.replace('"', '\\"').replace('\n', '\\n')
            labels = ','.join(task.labels)

            cmd = (
                f'gh issue create '
                f'--title "{title}" '
                f'--body "{body}" '
                f'--label "{labels}"'
            )
            commands.append(cmd)

        return commands

    def save_commands(self, output_path: str) -> None:
        """Save commands to shell script."""
        commands = self.generate_gh_commands()

        script_content = "#!/bin/bash\n"
        script_content += "# Generated GDD to Issues script\n"
        script_content += "# Run with: bash create_issues.sh\n\n"

        for cmd in commands:
            script_content += cmd + "\n"

        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(script_content)

        output_file.chmod(0o755)
        print(f"Script saved to {output_path}")
        print(f"Run with: bash {output_path}")

    def create_issues(self, repo: Optional[str] = None) -> None:
        """Create issues directly using gh CLI."""
        commands = self.generate_gh_commands()

        repo_arg = f"--repo {repo}" if repo else ""

        for i, cmd in enumerate(commands, 1):
            try:
                full_cmd = f"{cmd} {repo_arg}"
                result = subprocess.run(
                    full_cmd,
                    shell=True,
                    capture_output=True,
                    text=True,
                    check=False
                )

                if result.returncode == 0:
                    print(f"✓ Created issue {i}/{len(commands)}: {self.tasks[i-1].title}")
                else:
                    print(f"✗ Failed to create issue {i}: {result.stderr}")

            except Exception as e:
                print(f"✗ Error creating issue {i}: {e}")

    def generate_summary(self) -> Dict[str, Any]:
        """Generate summary of extracted tasks."""
        by_type = {}
        by_label = {}

        for task in self.tasks:
            # By type
            task_type = task.task_type
            if task_type not in by_type:
                by_type[task_type] = []
            by_type[task_type].append(task.title)

            # By label
            for label in task.labels:
                if label not in by_label:
                    by_label[label] = []
                by_label[label].append(task.title)

        return {
            'total_tasks': len(self.tasks),
            'by_type': by_type,
            'by_label': by_label,
            'tasks': [
                {
                    'title': t.title,
                    'type': t.task_type,
                    'section': t.section,
                    'labels': t.labels
                }
                for t in self.tasks
            ]
        }

    def print_summary(self) -> None:
        """Print task summary."""
        summary = self.generate_summary()

        print("\n" + "="*60)
        print("GDD TO ISSUES SUMMARY")
        print("="*60)
        print(f"\nTotal tasks found: {summary['total_tasks']}")

        print("\nBy Task Type:")
        for task_type, tasks in summary['by_type'].items():
            print(f"  {task_type}: {len(tasks)}")

        print("\nBy Category:")
        for label, tasks in summary['by_label'].items():
            if label != 'from-gdd':  # Skip meta-label
                print(f"  {label}: {len(tasks)}")

        print("\nTasks:")
        for task in summary['tasks']:
            print(f"  - [{task['type']}] {task['title']} ({task['section']})")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Convert GDD markdown to GitHub issues'
    )
    parser.add_argument(
        'gdd_file',
        help='Path to GDD markdown file'
    )
    parser.add_argument(
        '-f', '--feature',
        help='Feature name for structured decomposition (generates design/code/art/audio/QA/balance issues)'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output shell script path (default: creates issues directly)'
    )
    parser.add_argument(
        '-r', '--repo',
        help='GitHub repository (owner/repo) for issue creation'
    )
    parser.add_argument(
        '-e', '--execute',
        action='store_true',
        help='Execute issue creation immediately (requires gh CLI and auth)'
    )
    parser.add_argument(
        '-s', '--summary',
        action='store_true',
        help='Print summary of extracted tasks'
    )

    args = parser.parse_args()

    # Parse GDD
    gdd_parser = GDDParser(args.gdd_file, feature=args.feature)
    gdd_parser.parse()

    # Print summary if requested
    if args.summary:
        gdd_parser.print_summary()

    # Create issues
    if args.execute:
        if not args.repo:
            print("Error: --repo required for direct issue creation")
            return
        print(f"Creating issues in {args.repo}...")
        gdd_parser.create_issues(args.repo)
    elif args.output:
        print(f"Generating script to {args.output}...")
        gdd_parser.save_commands(args.output)
    else:
        print("No output specified. Use --output to generate script or --execute to create directly.")
        gdd_parser.print_summary()


if __name__ == '__main__':
    main()
