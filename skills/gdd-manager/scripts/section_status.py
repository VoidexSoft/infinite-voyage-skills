#!/usr/bin/env python3
"""
GDD Section Status Reporter - Reports completeness of each GDD section.

Analyzes a GDD directory (or a gdd-index.json from parse_gdd.py) and evaluates
each section for: content presence, required subsections, cross-references,
and word count. Outputs a JSON report with per-section completeness scores
and prints a summary table to stdout.
"""

import argparse
import json
import os
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Set
from dataclasses import dataclass, asdict, field
from datetime import datetime


@dataclass
class SubsectionInfo:
    """Information about a subsection within a GDD section."""
    title: str
    word_count: int
    has_content: bool


@dataclass
class SectionStatus:
    """Completeness status for a single GDD section."""
    name: str
    file_count: int
    total_word_count: int
    has_content: bool
    subsection_count: int
    required_subsections_present: int
    required_subsections_total: int
    cross_reference_count: int
    completeness_score: float
    files: List[str] = field(default_factory=list)
    missing_subsections: List[str] = field(default_factory=list)
    subsections: List[Dict[str, Any]] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)


# Required subsections per GDD section type
REQUIRED_SUBSECTIONS: Dict[str, List[str]] = {
    'mechanics': [
        'overview', 'core loop', 'controls', 'rules', 'feedback',
    ],
    'narrative': [
        'overview', 'characters', 'story', 'dialogue', 'themes',
    ],
    'economy': [
        'overview', 'currencies', 'sources', 'sinks', 'progression',
    ],
    'progression': [
        'overview', 'leveling', 'rewards', 'milestones', 'unlocks',
    ],
    'level_design': [
        'overview', 'layout', 'objectives', 'encounters', 'flow',
    ],
    'world_building': [
        'overview', 'lore', 'regions', 'factions', 'history',
    ],
    'art_direction': [
        'overview', 'style guide', 'color palette', 'references', 'assets',
    ],
    'audio_design': [
        'overview', 'music', 'sound effects', 'ambience', 'voice',
    ],
    'ui_ux': [
        'overview', 'wireframes', 'flow', 'accessibility', 'hud',
    ],
    'technical': [
        'overview', 'architecture', 'performance', 'platforms', 'tools',
    ],
    'balance': [
        'overview', 'parameters', 'formulas', 'tuning', 'testing',
    ],
    'production': [
        'overview', 'schedule', 'milestones', 'team', 'risks',
    ],
}

# Minimum word count thresholds for scoring
MIN_WORD_COUNT_SECTION = 100
GOOD_WORD_COUNT_SECTION = 500


class SectionStatusReporter:
    """Analyzes GDD sections and reports completeness."""

    def __init__(
        self,
        gdd_root: Optional[str] = None,
        index_path: Optional[str] = None,
    ):
        """
        Initialize reporter.

        Provide either gdd_root (directory path) or index_path (gdd-index.json).
        If both are given, index_path is used for section/file metadata and
        gdd_root is used to read file contents.

        Args:
            gdd_root: Path to GDD directory
            index_path: Path to gdd-index.json produced by parse_gdd.py
        """
        self.gdd_root: Optional[Path] = Path(gdd_root) if gdd_root else None
        self.index: Optional[Dict[str, Any]] = None
        self.section_statuses: List[SectionStatus] = []

        if index_path:
            index_file = Path(index_path)
            if not index_file.exists():
                raise FileNotFoundError(f"Index file not found: {index_path}")
            with open(index_file, 'r', encoding='utf-8') as f:
                self.index = json.load(f)
            # Derive gdd_root from index if not provided
            if self.gdd_root is None:
                stored_root = self.index.get('metadata', {}).get('gdd_root')
                if stored_root:
                    self.gdd_root = Path(stored_root)

        if self.gdd_root and not self.gdd_root.is_dir():
            raise ValueError(f"GDD root directory not found: {self.gdd_root}")

        if self.gdd_root is None and self.index is None:
            raise ValueError(
                "Provide at least one of --gdd-root or --index."
            )

    # ------------------------------------------------------------------
    # Content helpers
    # ------------------------------------------------------------------

    def _read_file(self, filepath: Path) -> str:
        """Safely read a text file and return its contents."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except (UnicodeDecodeError, IOError):
            return ''

    def _count_words(self, text: str) -> int:
        """Count words in text, ignoring markdown syntax."""
        # Strip markdown headers, links, images, code fences
        cleaned = re.sub(r'```[\s\S]*?```', '', text)
        cleaned = re.sub(r'!\[.*?\]\(.*?\)', '', cleaned)
        cleaned = re.sub(r'\[.*?\]\(.*?\)', '', cleaned)
        cleaned = re.sub(r'^#{1,6}\s+', '', cleaned, flags=re.MULTILINE)
        cleaned = re.sub(r'[*_`~>|#\-]', '', cleaned)
        return len(cleaned.split())

    def _extract_headings(self, text: str) -> List[str]:
        """Extract markdown headings (all levels) as lowercase strings."""
        headings: List[str] = []
        for match in re.finditer(r'^#{1,6}\s+(.+)$', text, re.MULTILINE):
            headings.append(match.group(1).strip().lower())
        return headings

    def _count_cross_references(self, text: str) -> int:
        """Count internal cross-references (links to .md files and backtick refs)."""
        md_links = len(re.findall(r'\[.+?\]\(.+?\.md\)', text))
        backtick_refs = len(re.findall(r'`[^`]+`', text))
        return md_links + backtick_refs

    # ------------------------------------------------------------------
    # Section scanning
    # ------------------------------------------------------------------

    def _build_index_from_directory(self) -> Dict[str, Any]:
        """Build a minimal index by scanning the GDD directory directly."""
        section_mapping = {
            r'.*mechanics.*': 'mechanics',
            r'.*gameplay.*': 'mechanics',
            r'.*core.*loop.*': 'mechanics',
            r'.*narrative.*': 'narrative',
            r'.*story.*': 'narrative',
            r'.*dialogue.*': 'narrative',
            r'.*character.*': 'narrative',
            r'.*economy.*': 'economy',
            r'.*progression.*': 'progression',
            r'.*level.*design.*': 'level_design',
            r'.*world.*': 'world_building',
            r'.*art.*': 'art_direction',
            r'.*visual.*': 'art_direction',
            r'.*audio.*': 'audio_design',
            r'.*sound.*': 'audio_design',
            r'.*ui.*': 'ui_ux',
            r'.*interface.*': 'ui_ux',
            r'.*technical.*': 'technical',
            r'.*architecture.*': 'technical',
            r'.*performance.*': 'technical',
            r'.*balance.*': 'balance',
            r'.*tuning.*': 'balance',
            r'.*schedule.*': 'production',
            r'.*pipeline.*': 'production',
        }

        sections: Dict[str, List[str]] = {}
        files: Dict[str, Dict[str, Any]] = {}

        for root, dirs, filenames in os.walk(self.gdd_root):
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for filename in filenames:
                if filename.startswith('.'):
                    continue
                filepath = Path(root) / filename
                rel_path = str(filepath.relative_to(self.gdd_root))
                fname_lower = filename.lower()

                section = 'uncategorized'
                for pattern, sec in section_mapping.items():
                    if re.match(pattern, fname_lower):
                        section = sec
                        break

                files[rel_path] = {
                    'name': filename,
                    'path': rel_path,
                    'section': section,
                    'extension': filepath.suffix,
                }

                sections.setdefault(section, [])
                sections[section].append(rel_path)

        return {
            'metadata': {'gdd_root': str(self.gdd_root)},
            'sections': {
                name: {'count': len(fpaths), 'files': fpaths}
                for name, fpaths in sections.items()
            },
            'files': files,
        }

    def _analyze_section(
        self,
        section_name: str,
        file_paths: List[str],
    ) -> SectionStatus:
        """Analyze a single GDD section and return its status."""
        total_words = 0
        all_headings: List[str] = []
        total_xrefs = 0
        subsections_info: List[SubsectionInfo] = []
        has_any_content = False

        for rel_path in file_paths:
            if self.gdd_root is None:
                continue

            filepath = self.gdd_root / rel_path
            if not filepath.exists():
                continue

            if filepath.suffix not in ('.md', '.txt', '.rst'):
                # Non-text files count as content but not for word/heading analysis
                has_any_content = True
                continue

            content = self._read_file(filepath)
            if not content.strip():
                continue

            has_any_content = True
            words = self._count_words(content)
            total_words += words
            headings = self._extract_headings(content)
            all_headings.extend(headings)
            total_xrefs += self._count_cross_references(content)

            for heading in headings:
                sub_info = SubsectionInfo(
                    title=heading,
                    word_count=0,  # Approximation; heading-level word counts are expensive
                    has_content=True,
                )
                subsections_info.append(sub_info)

        # Evaluate required subsections
        required = REQUIRED_SUBSECTIONS.get(section_name, [])
        heading_set: Set[str] = set(all_headings)
        present_required = 0
        missing: List[str] = []

        for req in required:
            # Fuzzy match: check if any heading contains the required term
            found = any(req in h for h in heading_set)
            if found:
                present_required += 1
            else:
                missing.append(req)

        # Calculate completeness score (0-100%)
        score = self._calculate_score(
            has_content=has_any_content,
            word_count=total_words,
            file_count=len(file_paths),
            required_present=present_required,
            required_total=len(required),
            xref_count=total_xrefs,
        )

        notes: List[str] = []
        if not has_any_content:
            notes.append('Section has no content')
        if total_words < MIN_WORD_COUNT_SECTION and has_any_content:
            notes.append(
                f'Low word count ({total_words}); '
                f'consider expanding (target >= {MIN_WORD_COUNT_SECTION})'
            )
        if missing:
            notes.append(
                f'Missing subsections: {", ".join(missing)}'
            )
        if total_xrefs == 0 and has_any_content:
            notes.append('No cross-references found; consider linking related sections')

        return SectionStatus(
            name=section_name,
            file_count=len(file_paths),
            total_word_count=total_words,
            has_content=has_any_content,
            subsection_count=len(subsections_info),
            required_subsections_present=present_required,
            required_subsections_total=len(required),
            cross_reference_count=total_xrefs,
            completeness_score=score,
            files=file_paths,
            missing_subsections=missing,
            subsections=[asdict(s) for s in subsections_info],
            notes=notes,
        )

    @staticmethod
    def _calculate_score(
        has_content: bool,
        word_count: int,
        file_count: int,
        required_present: int,
        required_total: int,
        xref_count: int,
    ) -> float:
        """
        Calculate a completeness score from 0.0 to 100.0.

        Weighting:
            30% - has content with adequate word count
            30% - required subsections present
            20% - cross-references
            20% - file coverage
        """
        if not has_content:
            return 0.0

        # Content depth score (0-1)
        if word_count >= GOOD_WORD_COUNT_SECTION:
            content_score = 1.0
        elif word_count >= MIN_WORD_COUNT_SECTION:
            content_score = 0.5 + 0.5 * (
                (word_count - MIN_WORD_COUNT_SECTION)
                / (GOOD_WORD_COUNT_SECTION - MIN_WORD_COUNT_SECTION)
            )
        else:
            content_score = 0.5 * (word_count / max(MIN_WORD_COUNT_SECTION, 1))

        # Required subsections score (0-1)
        if required_total > 0:
            subsection_score = required_present / required_total
        else:
            # No requirements defined -- give full marks if content exists
            subsection_score = 1.0

        # Cross-reference score (0-1), cap at 10 refs
        xref_score = min(xref_count / 10.0, 1.0) if xref_count > 0 else 0.0

        # File coverage score (0-1), cap at 3 files
        file_score = min(file_count / 3.0, 1.0)

        total = (
            0.30 * content_score
            + 0.30 * subsection_score
            + 0.20 * xref_score
            + 0.20 * file_score
        )

        return round(total * 100.0, 1)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def analyze(self) -> List[SectionStatus]:
        """Analyze all sections and return status list."""
        if self.index is None:
            self.index = self._build_index_from_directory()

        sections = self.index.get('sections', {})

        self.section_statuses = []
        for section_name, section_info in sections.items():
            file_paths = section_info.get('files', [])
            status = self._analyze_section(section_name, file_paths)
            self.section_statuses.append(status)

        # Sort by completeness score ascending (least complete first)
        self.section_statuses.sort(key=lambda s: s.completeness_score)

        return self.section_statuses

    def generate_report(self) -> Dict[str, Any]:
        """Generate JSON-serializable report."""
        if not self.section_statuses:
            self.analyze()

        total_sections = len(self.section_statuses)
        avg_score = (
            sum(s.completeness_score for s in self.section_statuses)
            / max(total_sections, 1)
        )
        complete_sections = sum(
            1 for s in self.section_statuses if s.completeness_score >= 80.0
        )
        incomplete_sections = sum(
            1 for s in self.section_statuses if s.completeness_score < 50.0
        )

        return {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'gdd_root': str(self.gdd_root) if self.gdd_root else None,
            },
            'summary': {
                'total_sections': total_sections,
                'average_score': round(avg_score, 1),
                'complete_sections': complete_sections,
                'incomplete_sections': incomplete_sections,
            },
            'sections': [asdict(s) for s in self.section_statuses],
        }

    def save_report(self, output_path: str) -> None:
        """Save report to JSON file."""
        report = self.generate_report()
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)

        print(f"Report saved to {output_path}")

    def print_summary(self) -> None:
        """Print a summary table to stdout."""
        if not self.section_statuses:
            self.analyze()

        report = self.generate_report()
        summary = report['summary']

        print()
        print("=" * 78)
        print("GDD SECTION STATUS REPORT")
        print("=" * 78)
        print()
        print(f"Total Sections : {summary['total_sections']}")
        print(f"Average Score  : {summary['average_score']:.1f}%")
        print(f"Complete (>=80): {summary['complete_sections']}")
        print(f"Needs Work (<50): {summary['incomplete_sections']}")
        print()

        # Table header
        header = (
            f"{'Section':<20} {'Score':>6} {'Files':>5} "
            f"{'Words':>7} {'Subsec':>8} {'XRefs':>6} {'Status':<12}"
        )
        print(header)
        print("-" * len(header))

        for status in self.section_statuses:
            score = status.completeness_score
            if score >= 80.0:
                status_label = 'Complete'
            elif score >= 50.0:
                status_label = 'Partial'
            elif score > 0.0:
                status_label = 'Needs Work'
            else:
                status_label = 'Empty'

            subsec_str = (
                f"{status.required_subsections_present}"
                f"/{status.required_subsections_total}"
            )

            row = (
                f"{status.name:<20} {score:>5.1f}% {status.file_count:>5} "
                f"{status.total_word_count:>7} {subsec_str:>8} "
                f"{status.cross_reference_count:>6} {status_label:<12}"
            )
            print(row)

        print()

        # Print notes for sections that need attention
        sections_with_notes = [
            s for s in self.section_statuses if s.notes
        ]
        if sections_with_notes:
            print("NOTES:")
            for status in sections_with_notes:
                for note in status.notes:
                    print(f"  [{status.name}] {note}")
            print()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Report completeness of each GDD section'
    )
    parser.add_argument(
        '-g', '--gdd-root',
        help='Path to GDD directory (scanned directly if no index is provided)'
    )
    parser.add_argument(
        '-i', '--index',
        help='Path to gdd-index.json (from parse_gdd.py)'
    )
    parser.add_argument(
        '-o', '--output',
        default='gdd-section-status.json',
        help='Output JSON report path (default: gdd-section-status.json)'
    )
    parser.add_argument(
        '-p', '--print',
        action='store_true',
        dest='print_table',
        help='Print summary table to stdout'
    )

    args = parser.parse_args()

    if not args.gdd_root and not args.index:
        parser.error('Provide at least one of --gdd-root or --index')

    # Analyze sections
    reporter = SectionStatusReporter(
        gdd_root=args.gdd_root,
        index_path=args.index,
    )
    reporter.analyze()

    # Save JSON report
    reporter.save_report(args.output)

    # Always print the summary table (or when explicitly requested)
    reporter.print_summary()


if __name__ == '__main__':
    main()
