#!/usr/bin/env python3
"""
Chart generation utilities for game balance data.

Generates charts from JSON data files produced by stat_curves, combat_sim,
economy_sim, loot_sim, and fairness scripts. Supports line, bar, histogram,
and scatter chart types. Uses matplotlib when available; falls back to ASCII
chart rendering otherwise.
"""

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple


# ---------------------------------------------------------------------------
# ASCII chart fallback
# ---------------------------------------------------------------------------

class ASCIIChart:
    """Simple ASCII chart renderer for when matplotlib is unavailable."""

    DEFAULT_WIDTH = 60
    DEFAULT_HEIGHT = 20

    @staticmethod
    def line(
        x_values: List[float],
        y_values: List[float],
        title: str = '',
        width: int = DEFAULT_WIDTH,
        height: int = DEFAULT_HEIGHT,
    ) -> str:
        """Render a line chart as ASCII art."""
        if not x_values or not y_values:
            return '(no data)'

        y_min = min(y_values)
        y_max = max(y_values)
        y_range = y_max - y_min if y_max != y_min else 1.0

        lines: List[str] = []
        if title:
            lines.append(f'  {title}')
            lines.append('')

        # Build canvas
        canvas = [[' ' for _ in range(width)] for _ in range(height)]

        # Map data points to canvas coordinates
        for i, (x, y) in enumerate(zip(x_values, y_values)):
            col = int((i / max(len(x_values) - 1, 1)) * (width - 1))
            row = height - 1 - int(((y - y_min) / y_range) * (height - 1))
            row = max(0, min(height - 1, row))
            col = max(0, min(width - 1, col))
            canvas[row][col] = '*'

        # Render with Y-axis labels
        label_width = max(len(f'{y_max:.1f}'), len(f'{y_min:.1f}'))
        for r in range(height):
            y_val = y_max - (r / max(height - 1, 1)) * y_range
            if r == 0 or r == height - 1 or r == height // 2:
                label = f'{y_val:>{label_width}.1f}'
            else:
                label = ' ' * label_width
            row_str = ''.join(canvas[r])
            lines.append(f'{label} |{row_str}')

        # X-axis
        lines.append(' ' * label_width + ' +' + '-' * width)
        x_min_str = f'{min(x_values):.0f}'
        x_max_str = f'{max(x_values):.0f}'
        padding = width - len(x_min_str) - len(x_max_str)
        lines.append(
            ' ' * (label_width + 2) + x_min_str + ' ' * max(padding, 1) + x_max_str
        )

        return '\n'.join(lines)

    @staticmethod
    def bar(
        labels: List[str],
        values: List[float],
        title: str = '',
        width: int = DEFAULT_WIDTH,
    ) -> str:
        """Render a horizontal bar chart as ASCII art."""
        if not labels or not values:
            return '(no data)'

        lines: List[str] = []
        if title:
            lines.append(f'  {title}')
            lines.append('')

        max_val = max(values) if values else 1.0
        max_label = max(len(str(l)) for l in labels) if labels else 5
        bar_width = width - max_label - 15

        for label, val in zip(labels, values):
            bar_len = int((val / max(max_val, 1e-9)) * bar_width)
            bar = '#' * bar_len
            lines.append(f'{str(label):>{max_label}} | {bar} {val:.2f}')

        return '\n'.join(lines)

    @staticmethod
    def histogram(
        values: List[float],
        bins: int = 10,
        title: str = '',
        width: int = DEFAULT_WIDTH,
    ) -> str:
        """Render a histogram as ASCII art."""
        if not values:
            return '(no data)'

        v_min = min(values)
        v_max = max(values)
        v_range = v_max - v_min if v_max != v_min else 1.0
        bin_width = v_range / bins

        # Count values per bin
        counts = [0] * bins
        for v in values:
            idx = int((v - v_min) / bin_width)
            idx = min(idx, bins - 1)
            counts[idx] += 1

        max_count = max(counts) if counts else 1
        bar_area = width - 25

        lines: List[str] = []
        if title:
            lines.append(f'  {title}')
            lines.append('')

        for i, count in enumerate(counts):
            lo = v_min + i * bin_width
            hi = lo + bin_width
            bar_len = int((count / max(max_count, 1)) * bar_area)
            bar = '#' * bar_len
            lines.append(f'  [{lo:>8.2f}, {hi:>8.2f}) | {bar} {count}')

        return '\n'.join(lines)

    @staticmethod
    def scatter(
        x_values: List[float],
        y_values: List[float],
        title: str = '',
        width: int = DEFAULT_WIDTH,
        height: int = DEFAULT_HEIGHT,
    ) -> str:
        """Render a scatter plot as ASCII art."""
        # Scatter is essentially the same as line for ASCII
        return ASCIIChart.line(x_values, y_values, title, width, height)


# ---------------------------------------------------------------------------
# Matplotlib chart renderer
# ---------------------------------------------------------------------------

def _has_matplotlib() -> bool:
    """Check if matplotlib is available."""
    try:
        import matplotlib
        return True
    except ImportError:
        return False


def render_matplotlib(
    chart_type: str,
    x_values: List[float],
    y_values: List[float],
    labels: Optional[List[str]],
    title: str,
    output_path: Path,
    x_label: str = '',
    y_label: str = '',
) -> None:
    """
    Render chart using matplotlib and save as PNG.

    Args:
        chart_type: 'line', 'bar', 'histogram', or 'scatter'
        x_values: X-axis data
        y_values: Y-axis data
        labels: Optional labels for bar chart categories
        title: Chart title
        output_path: Path to save PNG
        x_label: X-axis label
        y_label: Y-axis label
    """
    import matplotlib
    matplotlib.use('Agg')  # Non-interactive backend
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(12, 6))

    if chart_type == 'line':
        ax.plot(x_values, y_values, marker='o', linewidth=2, markersize=3)
    elif chart_type == 'bar':
        if labels:
            ax.bar(labels, y_values, color='steelblue')
            plt.xticks(rotation=45, ha='right')
        else:
            ax.bar(range(len(y_values)), y_values, color='steelblue')
    elif chart_type == 'histogram':
        bins = max(10, min(50, len(y_values) // 5))
        ax.hist(y_values, bins=bins, color='steelblue', edgecolor='white')
    elif chart_type == 'scatter':
        ax.scatter(x_values, y_values, alpha=0.6, s=20)
    else:
        print(f"Warning: Unknown chart type '{chart_type}', defaulting to line.")
        ax.plot(x_values, y_values, marker='o', linewidth=2, markersize=3)

    ax.set_title(title, fontsize=14, fontweight='bold')
    if x_label:
        ax.set_xlabel(x_label, fontsize=12)
    if y_label:
        ax.set_ylabel(y_label, fontsize=12)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(str(output_path), dpi=150, format='png')
    plt.close()


# ---------------------------------------------------------------------------
# Data extraction from various JSON formats
# ---------------------------------------------------------------------------

def extract_data(
    data: Any,
    x_key: Optional[str] = None,
    y_key: Optional[str] = None,
) -> Tuple[List[float], List[float], Optional[List[str]]]:
    """
    Extract x/y values from JSON data in various formats.

    Supports:
        - stat_curves output: {level: value, ...}
        - combat_sim output: {metric: value, ...}
        - economy_sim output: {balance_history: [...], ...}
        - loot_sim output: {actual_rates: {item: rate}, ...}
        - fairness output: {analysis: {options_analyzed: N, ...}, ...}
        - Generic list of numbers
        - List of {x: ..., y: ...} objects
        - Dict with x_key / y_key arrays

    Returns:
        (x_values, y_values, optional_labels)
    """
    labels: Optional[List[str]] = None

    # --- Case 1: Explicit x/y keys in a dict ---
    if isinstance(data, dict) and x_key and y_key:
        if x_key in data and y_key in data:
            xv = data[x_key]
            yv = data[y_key]
            if isinstance(xv, list) and isinstance(yv, list):
                return (
                    [float(v) for v in xv],
                    [float(v) for v in yv],
                    None,
                )

    # --- Case 2: Dict of str(number) -> number (stat_curves format) ---
    if isinstance(data, dict):
        # Check if all keys look numeric
        numeric_keys = True
        for k in data.keys():
            try:
                float(k)
            except (ValueError, TypeError):
                numeric_keys = False
                break

        if numeric_keys and data:
            sorted_items = sorted(data.items(), key=lambda kv: float(kv[0]))
            x_vals = [float(k) for k, _ in sorted_items]
            y_vals = [float(v) for _, v in sorted_items if isinstance(v, (int, float))]
            if len(x_vals) == len(y_vals) and y_vals:
                return x_vals, y_vals, None

    # --- Case 3: economy_sim balance_history ---
    if isinstance(data, dict) and 'balance_history' in data:
        history = data['balance_history']
        if isinstance(history, list):
            return (
                list(range(len(history))),
                [float(v) for v in history],
                None,
            )

    # --- Case 4: loot_sim actual_rates or expected_rates ---
    if isinstance(data, dict):
        for rate_key in ('actual_rates', 'expected_rates', 'observed'):
            if rate_key in data and isinstance(data[rate_key], dict):
                items = data[rate_key]
                labs = list(items.keys())
                vals = [float(v) for v in items.values()]
                return (
                    list(range(len(labs))),
                    vals,
                    labs,
                )

    # --- Case 5: fairness analysis options ---
    if isinstance(data, dict) and 'analysis' in data:
        analysis = data['analysis']
        if isinstance(analysis, dict):
            # Try to find the raw options elsewhere in the data
            pass

    # --- Case 6: Dict of string -> number (generic named values) ---
    if isinstance(data, dict):
        numeric_vals = {
            k: v for k, v in data.items()
            if isinstance(v, (int, float)) and not isinstance(v, bool)
        }
        if numeric_vals:
            labs = list(numeric_vals.keys())
            vals = [float(v) for v in numeric_vals.values()]
            return list(range(len(labs))), vals, labs

    # --- Case 7: Plain list of numbers ---
    if isinstance(data, list):
        if all(isinstance(v, (int, float)) for v in data):
            return (
                list(range(len(data))),
                [float(v) for v in data],
                None,
            )

        # List of {x, y} objects
        if data and isinstance(data[0], dict):
            xk = x_key or 'x'
            yk = y_key or 'y'
            if xk in data[0] and yk in data[0]:
                return (
                    [float(d[xk]) for d in data],
                    [float(d[yk]) for d in data],
                    None,
                )

    return [], [], None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Generate charts from game balance JSON data'
    )
    parser.add_argument(
        '--data',
        type=Path,
        required=True,
        help='Input JSON data file'
    )
    parser.add_argument(
        '--type',
        choices=['line', 'bar', 'histogram', 'scatter'],
        default='line',
        help='Chart type (default: line)'
    )
    parser.add_argument(
        '--title',
        type=str,
        default='',
        help='Chart title'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=None,
        help='Output PNG file path (default: <data_stem>_chart.png)'
    )
    parser.add_argument(
        '--x-key',
        type=str,
        default=None,
        help='JSON key for x-axis data'
    )
    parser.add_argument(
        '--y-key',
        type=str,
        default=None,
        help='JSON key for y-axis data'
    )
    parser.add_argument(
        '--x-label',
        type=str,
        default='',
        help='X-axis label'
    )
    parser.add_argument(
        '--y-label',
        type=str,
        default='',
        help='Y-axis label'
    )
    parser.add_argument(
        '--ascii',
        action='store_true',
        help='Force ASCII output even if matplotlib is available'
    )

    args = parser.parse_args()

    # Load data
    if not args.data.exists():
        print(f"Error: Data file not found: {args.data}")
        sys.exit(1)

    with open(args.data, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    # Extract x/y values
    x_values, y_values, labels = extract_data(
        raw_data,
        x_key=args.x_key,
        y_key=args.y_key,
    )

    if not y_values:
        print("Error: Could not extract plottable data from input file.")
        print("Tip: Use --x-key and --y-key to specify JSON keys, or check the data format.")
        sys.exit(1)

    # Determine output path
    output_path = args.output or args.data.with_name(
        f'{args.data.stem}_chart.png'
    )

    # Auto-generate title if not provided
    title = args.title or f'{args.data.stem} ({args.type})'

    # Render chart
    use_ascii = args.ascii or not _has_matplotlib()

    if use_ascii:
        if _has_matplotlib() and not args.ascii:
            pass  # Won't reach here, but guard
        elif not _has_matplotlib():
            print("matplotlib not available. Rendering ASCII chart.\n")

        ascii_chart = ASCIIChart()

        if args.type == 'line':
            output_text = ascii_chart.line(x_values, y_values, title)
        elif args.type == 'bar':
            chart_labels = labels or [str(int(x)) for x in x_values]
            output_text = ascii_chart.bar(chart_labels, y_values, title)
        elif args.type == 'histogram':
            output_text = ascii_chart.histogram(y_values, title=title)
        elif args.type == 'scatter':
            output_text = ascii_chart.scatter(x_values, y_values, title)
        else:
            output_text = ascii_chart.line(x_values, y_values, title)

        print(output_text)

        # Also save ASCII output to a .txt file
        txt_path = output_path.with_suffix('.txt')
        txt_path.parent.mkdir(parents=True, exist_ok=True)
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(output_text + '\n')
        print(f"\nSaved ASCII chart to: {txt_path}")

    else:
        render_matplotlib(
            chart_type=args.type,
            x_values=x_values,
            y_values=y_values,
            labels=labels,
            title=title,
            output_path=output_path,
            x_label=args.x_label,
            y_label=args.y_label,
        )
        print(f"Saved chart to: {output_path}")

    # Print data summary
    print(f"\nData Summary:")
    print(f"  Data points: {len(y_values)}")
    print(f"  Y range: [{min(y_values):.4f}, {max(y_values):.4f}]")
    if x_values:
        print(f"  X range: [{min(x_values):.4f}, {max(x_values):.4f}]")
    if labels:
        print(f"  Labels: {len(labels)} categories")


if __name__ == '__main__':
    main()
