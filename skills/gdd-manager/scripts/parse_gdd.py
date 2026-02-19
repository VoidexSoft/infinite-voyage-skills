#!/usr/bin/env python3
"""
GDD Parser - Scans a GDD directory and generates a structured index.

This script walks through a GDD directory, categorizes files by type and content,
extracts metadata (titles, modification dates), and outputs a comprehensive JSON index.
"""

import os
import json
import argparse
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional


class GDDParser:
    """Parser for Game Design Document directory structures."""

    # File pattern to GDD section mapping
    SECTION_MAPPING = {
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

    def __init__(self, gdd_path: str):
        """Initialize parser with GDD directory path."""
        self.gdd_path = Path(gdd_path)
        if not self.gdd_path.is_dir():
            raise ValueError(f"GDD path does not exist: {gdd_path}")

        self.index = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'gdd_root': str(self.gdd_path),
                'total_files': 0,
            },
            'sections': {},
            'files': {},
        }

    def _categorize_file(self, filepath: Path) -> str:
        """Categorize a file based on name and content patterns."""
        filename = filepath.name.lower()

        # Check filename patterns
        for pattern, section in self.SECTION_MAPPING.items():
            if re.match(pattern, filename):
                return section

        # Check file content for markdown headers
        if filepath.suffix in ['.md', '.txt']:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read(500)  # Read first 500 chars
                    for pattern, section in self.SECTION_MAPPING.items():
                        if re.search(pattern, content, re.IGNORECASE):
                            return section
            except (UnicodeDecodeError, IOError):
                pass

        return 'uncategorized'

    def _extract_title(self, filepath: Path) -> Optional[str]:
        """Extract title from markdown headers or filename."""
        if filepath.suffix in ['.md']:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    for line in f:
                        match = re.match(r'^#+\s+(.+)$', line)
                        if match:
                            return match.group(1)
            except (UnicodeDecodeError, IOError):
                pass

        # Fallback to filename
        return filepath.stem.replace('_', ' ').replace('-', ' ').title()

    def _get_file_stats(self, filepath: Path) -> Dict[str, Any]:
        """Get file metadata."""
        try:
            stat = filepath.stat()
            return {
                'size_bytes': stat.st_size,
                'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                'created': datetime.fromtimestamp(stat.st_ctime).isoformat(),
            }
        except OSError:
            return {
                'size_bytes': 0,
                'modified': None,
                'created': None,
            }

    def parse(self) -> Dict[str, Any]:
        """Parse GDD directory and generate index."""
        # Walk through directory
        for root, dirs, files in os.walk(self.gdd_path):
            # Skip hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]

            for filename in files:
                if filename.startswith('.'):
                    continue

                filepath = Path(root) / filename
                rel_path = str(filepath.relative_to(self.gdd_path))

                section = self._categorize_file(filepath)
                title = self._extract_title(filepath)
                stats = self._get_file_stats(filepath)

                # Add to files index
                self.index['files'][rel_path] = {
                    'name': filename,
                    'path': rel_path,
                    'section': section,
                    'title': title,
                    'extension': filepath.suffix,
                    'stats': stats,
                }

                # Add to sections index
                if section not in self.index['sections']:
                    self.index['sections'][section] = {
                        'count': 0,
                        'files': [],
                    }

                self.index['sections'][section]['files'].append(rel_path)
                self.index['sections'][section]['count'] += 1
                self.index['metadata']['total_files'] += 1

        return self.index

    def save_index(self, output_path: str) -> None:
        """Save index to JSON file."""
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.index, f, indent=2)

        print(f"Index saved to {output_path}")
        print(f"Total files: {self.index['metadata']['total_files']}")
        print(f"Sections: {list(self.index['sections'].keys())}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Parse GDD directory and generate index'
    )
    parser.add_argument(
        'gdd_path',
        help='Path to GDD directory'
    )
    parser.add_argument(
        '-o', '--output',
        default='gdd-index.json',
        help='Output JSON file path (default: gdd-index.json)'
    )
    parser.add_argument(
        '-p', '--print',
        action='store_true',
        help='Print index to stdout'
    )

    args = parser.parse_args()

    # Parse GDD
    gdd_parser = GDDParser(args.gdd_path)
    index = gdd_parser.parse()

    # Save index
    gdd_parser.save_index(args.output)

    # Print if requested
    if args.print:
        print("\n" + "="*50)
        print("GDD INDEX")
        print("="*50)
        print(json.dumps(index, indent=2))


if __name__ == '__main__':
    main()
