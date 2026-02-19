#!/usr/bin/env python3
"""
Stat scaling curve generator for game balancing.

Generates level-based stat scaling curves with various mathematical models
(linear, exponential, diminishing returns, S-curve, stepped).

Outputs JSON mapping of level to stat values, with optional matplotlib visualization.
"""

import argparse
import json
import math
from pathlib import Path
from typing import Dict, List


def linear_curve(level: int, base: float, growth: float, cap: float = None) -> float:
    """
    Linear scaling: stat = base + (level - 1) * growth

    Args:
        level: Current level (1-indexed)
        base: Base stat value at level 1
        growth: Stat gained per level
        cap: Optional maximum stat value

    Returns:
        Scaled stat value
    """
    value = base + (level - 1) * growth
    if cap is not None:
        value = min(value, cap)
    return value


def exponential_curve(level: int, base: float, growth: float, cap: float = None) -> float:
    """
    Exponential scaling: stat = base * (growth ^ (level - 1))

    Args:
        level: Current level (1-indexed)
        base: Base stat value at level 1
        growth: Exponential growth factor (typically 1.01-1.5)
        cap: Optional maximum stat value

    Returns:
        Scaled stat value
    """
    value = base * (growth ** (level - 1))
    if cap is not None:
        value = min(value, cap)
    return value


def diminishing_curve(level: int, base: float, growth: float, cap: float) -> float:
    """
    Diminishing returns: approaches cap logarithmically.
    stat = cap - (cap - base) / (1 + growth * (level - 1))

    Args:
        level: Current level (1-indexed)
        base: Base stat value at level 1
        growth: Growth rate (controls how quickly cap is approached)
        cap: Maximum stat value (hard cap)

    Returns:
        Scaled stat value
    """
    if cap is None:
        cap = base * 2
    value = cap - (cap - base) / (1 + growth * (level - 1))
    return value


def s_curve(level: int, base: float, growth: float, cap: float) -> float:
    """
    S-curve (sigmoid) scaling: slow start, rapid middle, slow end.
    Uses normalized sigmoid function.

    Args:
        level: Current level (1-indexed)
        base: Base stat value at level 1
        growth: Growth rate (steepness of curve)
        cap: Maximum stat value (approaches asymptotically)

    Returns:
        Scaled stat value
    """
    if cap is None:
        cap = base * 2

    # Normalize level to sigmoid input range
    x = (level - 1) * growth / 10
    # Sigmoid function
    sigmoid = 1 / (1 + math.exp(-x))
    # Scale to range [base, cap]
    value = base + (cap - base) * sigmoid
    return value


def stepped_curve(level: int, base: float, growth: float, cap: float = None) -> float:
    """
    Stepped scaling: increases at fixed intervals.
    Implements 5-level steps by default.

    Args:
        level: Current level (1-indexed)
        base: Base stat value at level 1
        growth: Stat increase per step (5 levels)
        cap: Optional maximum stat value

    Returns:
        Scaled stat value
    """
    steps = (level - 1) // 5
    value = base + steps * growth
    if cap is not None:
        value = min(value, cap)
    return value


def generate_curve(
    curve_type: str,
    base: float,
    max_level: int,
    growth: float,
    cap: float = None
) -> Dict[int, float]:
    """
    Generate a complete stat scaling curve.

    Args:
        curve_type: Type of curve (linear, exponential, diminishing, s_curve, stepped)
        base: Base stat value at level 1
        max_level: Maximum level to generate
        growth: Growth rate/factor (curve-type dependent)
        cap: Optional cap value (required for diminishing, s_curve)

    Returns:
        Dictionary mapping level to stat value
    """
    curve_functions = {
        'linear': linear_curve,
        'exponential': exponential_curve,
        'diminishing': diminishing_curve,
        's_curve': s_curve,
        'stepped': stepped_curve,
    }

    if curve_type not in curve_functions:
        raise ValueError(f"Unknown curve type: {curve_type}")

    func = curve_functions[curve_type]
    curve_data = {}

    for level in range(1, max_level + 1):
        curve_data[level] = func(level, base, growth, cap)

    return curve_data


def save_json(data: Dict, output_path: Path) -> None:
    """Save curve data to JSON file."""
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved JSON to: {output_path}")


def plot_curve(
    data: Dict[int, float],
    curve_type: str,
    output_path: Path = None
) -> None:
    """
    Generate matplotlib chart of the curve.

    Args:
        data: Dictionary of level->value mappings
        curve_type: Type of curve (for title)
        output_path: Path to save PNG (if provided)
    """
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not available. Skipping chart generation.")
        return

    levels = sorted(data.keys())
    values = [data[level] for level in levels]

    plt.figure(figsize=(10, 6))
    plt.plot(levels, values, marker='o', linewidth=2, markersize=4)
    plt.xlabel('Level', fontsize=12)
    plt.ylabel('Stat Value', fontsize=12)
    plt.title(f'Stat Scaling Curve ({curve_type.title()})', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=150, format='png')
        print(f"Saved chart to: {output_path}")
    else:
        plt.show()

    plt.close()


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Generate stat scaling curves for game balancing'
    )
    parser.add_argument(
        '--type',
        choices=['linear', 'exponential', 'diminishing', 's_curve', 'stepped'],
        default='linear',
        help='Type of scaling curve'
    )
    parser.add_argument(
        '--base',
        type=float,
        default=10,
        help='Base stat value at level 1'
    )
    parser.add_argument(
        '--max-level',
        type=int,
        default=100,
        help='Maximum level to generate'
    )
    parser.add_argument(
        '--growth',
        type=float,
        default=0.5,
        help='Growth rate/factor (curve-type dependent)'
    )
    parser.add_argument(
        '--cap',
        type=float,
        default=None,
        help='Stat cap (for diminishing/s_curve)'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path('stat_curve.json'),
        help='Output path for JSON file'
    )
    parser.add_argument(
        '--plot',
        action='store_true',
        help='Generate matplotlib chart'
    )

    args = parser.parse_args()

    # Generate curve
    curve_data = generate_curve(
        curve_type=args.type,
        base=args.base,
        max_level=args.max_level,
        growth=args.growth,
        cap=args.cap
    )

    # Save JSON
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    save_json(curve_data, output_path)

    # Plot if requested
    if args.plot:
        chart_path = output_path.with_suffix('.png')
        plot_curve(curve_data, args.type, chart_path)

    # Print summary
    min_val = min(curve_data.values())
    max_val = max(curve_data.values())
    print(f"\nCurve Summary ({args.type}):")
    print(f"  Level 1: {curve_data[1]:.2f}")
    print(f"  Level {args.max_level}: {curve_data[args.max_level]:.2f}")
    print(f"  Min: {min_val:.2f}, Max: {max_val:.2f}")
    print(f"  Total growth: {((max_val - min_val) / min_val * 100):.1f}%")


if __name__ == '__main__':
    main()
