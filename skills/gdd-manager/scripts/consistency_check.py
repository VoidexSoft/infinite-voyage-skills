#!/usr/bin/env python3
"""
GDD Consistency Checker - Cross-references GDD sections for consistency issues.

Validates GDD structure by checking for:
- Undefined terms referenced across files
- Broken internal links
- Naming inconsistencies
- Orphaned sections
"""

import json
import argparse
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any
from dataclasses import dataclass, asdict
from collections import defaultdict


@dataclass
class ConsistencyIssue:
    """Represents a consistency issue found in GDD."""
    issue_type: str  # 'broken_link', 'undefined_term', 'naming_inconsistency', 'orphaned_section'
    severity: str    # 'error', 'warning', 'info'
    file: str
    message: str
    reference: str = ""


class GDDConsistencyChecker:
    """Checks GDD for consistency issues."""

    def __init__(self, index_path: str, gdd_root: str):
        """Initialize checker with GDD index and root path."""
        self.index_path = Path(index_path)
        self.gdd_root = Path(gdd_root)

        with open(self.index_path, 'r', encoding='utf-8') as f:
            self.index = json.load(f)

        self.issues: List[ConsistencyIssue] = []
        self.defined_terms: Set[str] = set()
        self.referenced_terms: Dict[str, List[str]] = defaultdict(list)
        self.internal_links: Dict[str, List[Tuple[str, str]]] = defaultdict(list)

    def _extract_markdown_terms(self, filepath: Path) -> Set[str]:
        """Extract defined terms from markdown headers."""
        terms = set()
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    # Match headers and bold text
                    match = re.match(r'^#+\s+(.+)$', line)
                    if match:
                        terms.add(match.group(1).lower())
                    # Match **bold** terms
                    for bold_match in re.finditer(r'\*\*(.+?)\*\*', line):
                        terms.add(bold_match.group(1).lower())
        except (UnicodeDecodeError, IOError):
            pass

        return terms

    def _extract_references(self, filepath: Path) -> Tuple[Set[str], List[str]]:
        """Extract term references and internal links from markdown."""
        references = set()
        links = []

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

                # Extract internal links [text](filename.md)
                for match in re.finditer(r'\[(.+?)\]\((.+?\.md)\)', content):
                    links.append((match.group(1), match.group(2)))

                # Extract backtick references
                for match in re.finditer(r'`([^`]+)`', content):
                    references.add(match.group(1).lower())

        except (UnicodeDecodeError, IOError):
            pass

        return references, links

    def check_broken_links(self) -> None:
        """Check for broken internal links."""
        valid_files = set(self.index['files'].keys())

        for filepath_str in self.index['files'].keys():
            filepath = self.gdd_root / filepath_str

            _, links = self._extract_references(filepath)

            for link_text, link_target in links:
                # Resolve relative paths
                target_path = Path(filepath_str).parent / link_target
                normalized_target = str(target_path).replace('\\', '/')

                if normalized_target not in valid_files:
                    self.issues.append(ConsistencyIssue(
                        issue_type='broken_link',
                        severity='error',
                        file=filepath_str,
                        message=f"Link target not found: {link_target}",
                        reference=link_text
                    ))

    def check_undefined_terms(self) -> None:
        """Check for undefined terms referenced across files."""
        # First pass: collect all defined terms
        for filepath_str in self.index['files'].keys():
            filepath = self.gdd_root / filepath_str
            if filepath.suffix == '.md':
                terms = self._extract_markdown_terms(filepath)
                self.defined_terms.update(terms)

        # Second pass: check references
        for filepath_str in self.index['files'].keys():
            filepath = self.gdd_root / filepath_str
            if filepath.suffix == '.md':
                references, _ = self._extract_references(filepath)

                for ref in references:
                    if ref not in self.defined_terms:
                        # Only report if it looks like a term (contains letters)
                        if re.search(r'[a-z]', ref, re.IGNORECASE):
                            self.referenced_terms[ref].append(filepath_str)

                            self.issues.append(ConsistencyIssue(
                                issue_type='undefined_term',
                                severity='warning',
                                file=filepath_str,
                                message=f"Undefined term referenced: {ref}",
                                reference=ref
                            ))

    def check_naming_inconsistencies(self) -> None:
        """Check for naming inconsistencies in files."""
        sections = self.index['sections']
        name_variations: Dict[str, List[str]] = defaultdict(list)

        for filepath_str in self.index['files'].keys():
            filename = Path(filepath_str).stem.lower()
            # Extract base name (without numbers/dates)
            base_name = re.sub(r'[-_](\d+|v\d+|draft)', '', filename)

            name_variations[base_name].append(filepath_str)

        # Check for similar files that might be duplicates
        for base_name, files in name_variations.items():
            if len(files) > 1:
                # Check if they're in different sections
                sections_set = set(
                    self.index['files'][f]['section'] for f in files
                )
                if len(sections_set) > 1:
                    self.issues.append(ConsistencyIssue(
                        issue_type='naming_inconsistency',
                        severity='warning',
                        file=files[0],
                        message=f"Similar files in different sections: {', '.join(files)}",
                        reference=base_name
                    ))

    def check_orphaned_sections(self) -> None:
        """Check for sections with no files."""
        for section, info in self.index['sections'].items():
            if info['count'] == 0:
                self.issues.append(ConsistencyIssue(
                    issue_type='orphaned_section',
                    severity='info',
                    file='',
                    message=f"Empty section: {section}",
                    reference=section
                ))

    def check_all(self) -> List[ConsistencyIssue]:
        """Run all consistency checks."""
        print("Running consistency checks...")
        self.check_broken_links()
        print("  - Checked for broken links")
        self.check_undefined_terms()
        print("  - Checked for undefined terms")
        self.check_naming_inconsistencies()
        print("  - Checked for naming inconsistencies")
        self.check_orphaned_sections()
        print("  - Checked for orphaned sections")

        return self.issues

    def generate_report(self) -> Dict[str, Any]:
        """Generate consistency report."""
        issues_by_type = defaultdict(list)
        issues_by_severity = defaultdict(list)

        for issue in self.issues:
            issues_by_type[issue.issue_type].append(asdict(issue))
            issues_by_severity[issue.severity].append(asdict(issue))

        return {
            'summary': {
                'total_issues': len(self.issues),
                'errors': len(issues_by_severity['error']),
                'warnings': len(issues_by_severity['warning']),
                'info': len(issues_by_severity['info']),
            },
            'by_type': dict(issues_by_type),
            'by_severity': dict(issues_by_severity),
            'issues': [asdict(issue) for issue in self.issues],
        }

    def save_report(self, output_path: str) -> None:
        """Save consistency report to JSON file."""
        report = self.generate_report()
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)

        print(f"\nConsistency report saved to {output_path}")
        print(f"Total issues: {report['summary']['total_issues']}")
        print(f"  - Errors: {report['summary']['errors']}")
        print(f"  - Warnings: {report['summary']['warnings']}")
        print(f"  - Info: {report['summary']['info']}")

    def print_report(self) -> None:
        """Print consistency report to console."""
        report = self.generate_report()

        print("\n" + "="*60)
        print("GDD CONSISTENCY REPORT")
        print("="*60)

        print(f"\nTotal Issues: {report['summary']['total_issues']}")
        print(f"  Errors: {report['summary']['errors']}")
        print(f"  Warnings: {report['summary']['warnings']}")
        print(f"  Info: {report['summary']['info']}")

        for severity in ['error', 'warning', 'info']:
            if report['by_severity'].get(severity):
                print(f"\n{severity.upper()}S:")
                for issue in report['by_severity'][severity]:
                    print(f"  - [{issue['issue_type']}] {issue['file']}: {issue['message']}")
                    if issue['reference']:
                        print(f"    Reference: {issue['reference']}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Check GDD for consistency issues'
    )
    parser.add_argument(
        'index_path',
        help='Path to GDD index JSON file'
    )
    parser.add_argument(
        '-g', '--gdd-root',
        required=True,
        help='Root path of GDD directory'
    )
    parser.add_argument(
        '-o', '--output',
        default='gdd-consistency-report.json',
        help='Output report path (default: gdd-consistency-report.json)'
    )
    parser.add_argument(
        '-p', '--print',
        action='store_true',
        help='Print report to stdout'
    )

    args = parser.parse_args()

    # Run checks
    checker = GDDConsistencyChecker(args.index_path, args.gdd_root)
    checker.check_all()
    checker.save_report(args.output)

    if args.print:
        checker.print_report()


if __name__ == '__main__':
    main()
