#!/usr/bin/env python3
"""
Fairness and balance analysis tool for game elements.

Analyzes game options (classes, weapons, builds) to compute fairness metrics
including Gini coefficient, coefficient of variation, and balance ratings.
"""

import argparse
import json
import math
import statistics
from pathlib import Path
from typing import Dict, List, Any, Tuple


def gini_coefficient(values: List[float]) -> float:
    """
    Calculate Gini coefficient (inequality measure, 0-1).

    0 = perfect equality, 1 = perfect inequality

    Args:
        values: List of numeric values

    Returns:
        Gini coefficient
    """
    if not values or len(values) < 2:
        return 0

    sorted_values = sorted(values)
    n = len(sorted_values)
    cumsum = 0

    for i, val in enumerate(sorted_values):
        cumsum += (i + 1) * val

    gini = (2 * cumsum) / (n * sum(sorted_values)) - (n + 1) / n

    return max(0, gini)  # Ensure non-negative


def coefficient_of_variation(values: List[float]) -> float:
    """
    Calculate coefficient of variation (relative std dev).

    Useful for comparing variability across different scales.

    Args:
        values: List of numeric values

    Returns:
        Coefficient of variation (std_dev / mean)
    """
    if not values or len(values) < 2:
        return 0

    mean = statistics.mean(values)
    if mean == 0:
        return float('inf')

    stdev = statistics.stdev(values)
    return stdev / mean


def detect_outliers(values: List[float]) -> List[Tuple[int, float]]:
    """
    Detect outliers using IQR method.

    Args:
        values: List of numeric values

    Returns:
        List of (index, value) tuples for outliers
    """
    if len(values) < 4:
        return []

    sorted_values = sorted(values)
    n = len(sorted_values)

    q1_idx = n // 4
    q3_idx = (3 * n) // 4

    q1 = sorted_values[q1_idx]
    q3 = sorted_values[q3_idx]

    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outliers = []
    for i, val in enumerate(values):
        if val < lower_bound or val > upper_bound:
            outliers.append((i, val))

    return outliers


def rate_balance(gini: float, cv: float) -> str:
    """
    Rate overall balance based on fairness metrics.

    Args:
        gini: Gini coefficient (0-1)
        cv: Coefficient of variation

    Returns:
        Balance rating: excellent, good, fair, or poor
    """
    avg_score = (gini + min(cv, 1.0)) / 2

    if avg_score < 0.15:
        return 'excellent'
    elif avg_score < 0.30:
        return 'good'
    elif avg_score < 0.50:
        return 'fair'
    else:
        return 'poor'


def analyze_fairness(
    options: Dict[str, float],
    metric_name: str = 'power'
) -> Dict[str, Any]:
    """
    Analyze fairness of game options.

    Args:
        options: Dictionary of option name to numeric value
        metric_name: Name of metric being analyzed

    Returns:
        Dictionary with fairness analysis
    """
    if not options:
        return {}

    values = list(options.values())
    names = list(options.keys())

    # Basic statistics
    min_val = min(values)
    max_val = max(values)
    mean_val = statistics.mean(values)
    median_val = statistics.median(values)
    stdev_val = statistics.stdev(values) if len(values) > 1 else 0

    # Fairness metrics
    gini = gini_coefficient(values)
    cv = coefficient_of_variation(values)

    # Outlier detection
    outliers = detect_outliers(values)
    outlier_names = [names[idx] for idx, _ in outliers]

    # Power/gap analysis
    range_spread = max_val - min_val
    spread_pct = (range_spread / mean_val * 100) if mean_val > 0 else 0

    # Balance rating
    rating = rate_balance(gini, cv)

    return {
        'metric': metric_name,
        'options_analyzed': len(options),
        'min': min_val,
        'max': max_val,
        'mean': mean_val,
        'median': median_val,
        'stdev': stdev_val,
        'range': range_spread,
        'range_percent': spread_pct,
        'gini_coefficient': gini,
        'coefficient_of_variation': cv,
        'outliers': {name: options[name] for name in outlier_names},
        'outlier_count': len(outliers),
        'balance_rating': rating,
        'skewness': _calculate_skewness(values),
    }


def _calculate_skewness(values: List[float]) -> float:
    """
    Calculate Fisher-Pearson coefficient of skewness.

    Positive = right-skewed (tail on right)
    Negative = left-skewed (tail on left)
    """
    if len(values) < 3:
        return 0

    mean_val = statistics.mean(values)
    stdev_val = statistics.stdev(values)

    if stdev_val == 0:
        return 0

    skewness = sum((x - mean_val) ** 3 for x in values) / (len(values) * stdev_val ** 3)
    return skewness


def compare_groups(
    groups: Dict[str, Dict[str, float]],
    metric_name: str = 'power'
) -> Dict[str, Any]:
    """
    Compare fairness metrics across multiple groups.

    Args:
        groups: Dictionary of group name to options dictionary
        metric_name: Name of metric being analyzed

    Returns:
        Comparative analysis
    """
    group_analyses = {}
    all_means = []

    for group_name, options in groups.items():
        analysis = analyze_fairness(options, metric_name)
        group_analyses[group_name] = analysis
        all_means.append(analysis['mean'])

    # Calculate comparative statistics
    mean_of_means = statistics.mean(all_means) if all_means else 0
    mean_variance = statistics.variance(all_means) if len(all_means) > 1 else 0

    comparison = {
        'groups_analyzed': len(groups),
        'mean_of_means': mean_of_means,
        'variance_of_means': mean_variance,
        'group_analyses': group_analyses,
    }

    return comparison


def load_fairness_config(config_path: Path) -> Dict[str, Any]:
    """Load fairness analysis configuration from JSON."""
    with open(config_path, 'r') as f:
        return json.load(f)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description='Game fairness and balance analyzer')
    parser.add_argument(
        '--config',
        type=Path,
        required=True,
        help='Configuration JSON file with game options'
    )
    parser.add_argument(
        '--metric',
        type=str,
        default='power',
        help='Name of metric being analyzed'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path('fairness_results.json'),
        help='Output path for results JSON'
    )

    args = parser.parse_args()

    # Load configuration
    config = load_fairness_config(args.config)

    # Detect if single option set or multiple groups
    options = config.get('options', {})
    groups = config.get('groups', {})

    results = {
        'metric': args.metric,
        'timestamp': None,
    }

    if options and not groups:
        # Single group analysis
        analysis = analyze_fairness(options, args.metric)
        results['analysis'] = analysis
        results['type'] = 'single'

        # Generate recommendations
        results['recommendations'] = _generate_recommendations(analysis)

    elif groups:
        # Multi-group analysis
        comparison = compare_groups(groups, args.metric)
        results['comparison'] = comparison
        results['type'] = 'comparison'

    # Save results
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, 'w') as f:
        json.dump(results, f, indent=2)

    # Print summary
    print("\nFairness Analysis Results:")

    if results['type'] == 'single':
        analysis = results['analysis']
        print(f"\nMetric: {analysis['metric']}")
        print(f"Options analyzed: {analysis['options_analyzed']}")
        print(f"\nStatistics:")
        print(f"  Min: {analysis['min']:.2f}")
        print(f"  Max: {analysis['max']:.2f}")
        print(f"  Mean: {analysis['mean']:.2f}")
        print(f"  Median: {analysis['median']:.2f}")
        print(f"  Std Dev: {analysis['stdev']:.2f}")
        print(f"  Range: {analysis['range']:.2f} ({analysis['range_percent']:.1f}%)")

        print(f"\nFairness Metrics:")
        print(f"  Gini coefficient: {analysis['gini_coefficient']:.4f} (0=equal, 1=unequal)")
        print(f"  Coefficient of variation: {analysis['coefficient_of_variation']:.4f}")
        print(f"  Skewness: {analysis['skewness']:.4f}")

        print(f"\nBalance Rating: {analysis['balance_rating'].upper()}")

        if analysis['outliers']:
            print(f"\nOutliers detected ({analysis['outlier_count']}):")
            for name, value in analysis['outliers'].items():
                print(f"  {name}: {value:.2f}")

        if results['recommendations']:
            print(f"\nRecommendations:")
            for rec in results['recommendations']:
                print(f"  - {rec}")

    else:
        comparison = results['comparison']
        print(f"\nComparative Analysis (Groups: {comparison['groups_analyzed']})")
        print(f"  Mean of means: {comparison['mean_of_means']:.2f}")
        print(f"  Variance of means: {comparison['variance_of_means']:.2f}")

        print(f"\nPer-Group Analysis:")
        for group_name, analysis in comparison['group_analyses'].items():
            print(f"\n  {group_name}:")
            print(f"    Options: {analysis['options_analyzed']}")
            print(f"    Mean: {analysis['mean']:.2f}")
            print(f"    Gini: {analysis['gini_coefficient']:.4f}")
            print(f"    Rating: {analysis['balance_rating']}")

    print(f"\nSaved results to: {args.output}")


def _generate_recommendations(analysis: Dict[str, Any]) -> List[str]:
    """Generate balance recommendations based on analysis."""
    recommendations = []

    gini = analysis['gini_coefficient']
    cv = analysis['coefficient_of_variation']
    outliers = analysis['outlier_count']

    if gini > 0.4:
        recommendations.append("High inequality detected. Consider adjusting extreme values.")

    if cv > 0.5:
        recommendations.append("High variation detected. Consider balancing spread.")

    if outliers > 0:
        recommendations.append(f"Found {outliers} outlier(s). Consider reviewing these values.")

    if not recommendations:
        recommendations.append("Balance appears good. No major adjustments needed.")

    return recommendations


if __name__ == '__main__':
    main()
