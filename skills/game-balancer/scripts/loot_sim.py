#!/usr/bin/env python3
"""
Loot table simulator for game balancing.

Simulates loot drops from a configurable loot table and compares actual
drop rates against expected probabilities. Includes statistical testing
and time-to-drop calculations.
"""

import argparse
import json
import math
from pathlib import Path
from typing import Dict, List, Any
from collections import Counter


class LootItem:
    """Represents a lootable item with drop rate."""

    def __init__(self, name: str, weight: float, drop_rate: float = None):
        """
        Initialize loot item.

        Args:
            name: Item name
            weight: Relative weight/probability
            drop_rate: Optional explicit drop rate (overrides weight)
        """
        self.name = name
        self.weight = weight
        self.drop_rate = drop_rate


class LootTable:
    """Manages loot item definitions and probabilities."""

    def __init__(self, items: List[LootItem]):
        """
        Initialize loot table.

        Args:
            items: List of LootItem objects
        """
        self.items = items
        self._normalize_weights()

    def _normalize_weights(self):
        """Normalize weights to probabilities."""
        # Items with explicit drop_rate keep those
        # Items without use weight-based distribution

        explicit_items = [i for i in self.items if i.drop_rate is not None]
        weight_items = [i for i in self.items if i.drop_rate is None]

        explicit_rate = sum(i.drop_rate for i in explicit_items)

        if explicit_rate >= 1.0:
            raise ValueError("Explicit drop rates exceed 100%")

        remaining_rate = 1.0 - explicit_rate
        total_weight = sum(i.weight for i in weight_items)

        # Assign normalized rates
        for item in explicit_items:
            pass  # Already has drop_rate

        for item in weight_items:
            if total_weight > 0:
                item.drop_rate = (item.weight / total_weight) * remaining_rate
            else:
                item.drop_rate = 0

    def get_drop(self) -> str:
        """
        Simulate a loot drop.

        Returns:
            Name of dropped item
        """
        import random
        r = random.random()
        cumulative = 0

        for item in self.items:
            cumulative += item.drop_rate
            if r < cumulative:
                return item.name

        # Fallback (shouldn't happen with normalized weights)
        return self.items[0].name if self.items else None

    def get_probabilities(self) -> Dict[str, float]:
        """Get theoretical drop probabilities."""
        return {item.name: item.drop_rate for item in self.items}


def chi_squared_test(observed: Dict[str, int], expected: Dict[str, float], total: int) -> Dict[str, Any]:
    """
    Perform chi-squared goodness-of-fit test.

    Args:
        observed: Dictionary of observed counts
        expected: Dictionary of expected probabilities
        total: Total number of trials

    Returns:
        Dictionary with test results
    """
    chi_squared = 0
    degrees_of_freedom = len(expected) - 1

    for item_name, prob in expected.items():
        obs_count = observed.get(item_name, 0)
        exp_count = total * prob

        if exp_count > 0:
            chi_squared += ((obs_count - exp_count) ** 2) / exp_count

    # Chi-squared critical values at 0.05 significance level
    # Covers df 1-30, with Wilson-Hilferty approximation for df > 30
    chi2_critical_005 = {
        1: 3.841, 2: 5.991, 3: 7.815, 4: 9.488, 5: 11.070,
        6: 12.592, 7: 14.067, 8: 15.507, 9: 16.919, 10: 18.307,
        11: 19.675, 12: 21.026, 13: 22.362, 14: 23.685, 15: 24.996,
        16: 26.296, 17: 27.587, 18: 28.869, 19: 30.144, 20: 31.410,
        21: 32.671, 22: 33.924, 23: 35.172, 24: 36.415, 25: 37.652,
        26: 38.885, 27: 40.113, 28: 41.337, 29: 42.557, 30: 43.773,
    }

    if degrees_of_freedom in chi2_critical_005:
        critical_value = chi2_critical_005[degrees_of_freedom]
    elif degrees_of_freedom > 30:
        # Wilson-Hilferty approximation for large df
        z = 1.6449  # z-score for 0.05 significance
        df = degrees_of_freedom
        critical_value = df * (1 - 2 / (9 * df) + z * math.sqrt(2 / (9 * df))) ** 3
    else:
        critical_value = 3.841  # Fallback for df < 1

    return {
        'chi_squared': chi_squared,
        'degrees_of_freedom': degrees_of_freedom,
        'critical_value': critical_value,
        'significant': chi_squared > critical_value,
        'p_value_approx': 'p > 0.05' if not chi_squared > critical_value else 'p < 0.05',
    }


def simulate_drops(loot_table: LootTable, num_drops: int) -> Dict[str, Any]:
    """
    Simulate loot drops.

    Args:
        loot_table: LootTable object
        num_drops: Number of drops to simulate

    Returns:
        Dictionary with simulation results
    """
    drops = [loot_table.get_drop() for _ in range(num_drops)]
    observed_counts = Counter(drops)

    # Get expected probabilities
    expected_probs = loot_table.get_probabilities()

    # Calculate statistics
    results = {
        'total_drops': num_drops,
        'unique_items': len(observed_counts),
        'observed': dict(observed_counts),
        'expected_rates': expected_probs,
        'actual_rates': {},
        'deviations': {},
        'chi_squared_test': None,
    }

    # Calculate actual rates and deviations
    for item_name, probability in expected_probs.items():
        observed_count = observed_counts.get(item_name, 0)
        actual_rate = observed_count / num_drops if num_drops > 0 else 0
        expected_count = num_drops * probability
        deviation = ((actual_rate - probability) / probability * 100) if probability > 0 else 0

        results['actual_rates'][item_name] = actual_rate
        results['deviations'][item_name] = deviation

    # Perform chi-squared test
    results['chi_squared_test'] = chi_squared_test(observed_counts, expected_probs, num_drops)

    return results


def calculate_time_to_drop(
    expected_rate: float,
    kill_rate: float,
    target_quantity: int = 1
) -> Dict[str, float]:
    """
    Calculate expected time to obtain item(s).

    Args:
        expected_rate: Probability of drop per kill (0-1)
        kill_rate: Number of kills per hour
        target_quantity: Number of items desired

    Returns:
        Dictionary with time estimates
    """
    if expected_rate <= 0:
        return {'kills_needed': float('inf'), 'time_hours': float('inf')}

    kills_per_item = 1 / expected_rate
    kills_needed = kills_per_item * target_quantity

    time_hours = kills_needed / kill_rate if kill_rate > 0 else float('inf')

    return {
        'kills_per_item': kills_per_item,
        'kills_needed': kills_needed,
        'time_hours': time_hours,
        'time_days': time_hours / 24,
    }


def load_loot_config(config_path: Path) -> Dict[str, Any]:
    """Load loot table configuration from JSON."""
    with open(config_path, 'r') as f:
        return json.load(f)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description='Loot table simulator')
    parser.add_argument(
        '--config',
        type=Path,
        required=True,
        help='Loot table configuration JSON file'
    )
    parser.add_argument(
        '--drops',
        type=int,
        default=10000,
        help='Number of drops to simulate'
    )
    parser.add_argument(
        '--kill-rate',
        type=float,
        default=10.0,
        help='Kills per hour (for time-to-drop calculations)'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path('loot_results.json'),
        help='Output path for results JSON'
    )

    args = parser.parse_args()

    # Load configuration
    config = load_loot_config(args.config)

    # Create loot table
    items = []
    for item_config in config.get('items', []):
        item = LootItem(
            name=item_config.get('name'),
            weight=item_config.get('weight', 1.0),
            drop_rate=item_config.get('drop_rate'),
        )
        items.append(item)

    loot_table = LootTable(items)

    # Simulate drops
    print(f"Simulating {args.drops} drops...")
    results = simulate_drops(loot_table, args.drops)

    # Add time-to-drop calculations
    results['time_to_drop'] = {}
    for item_name, expected_rate in results['expected_rates'].items():
        results['time_to_drop'][item_name] = calculate_time_to_drop(
            expected_rate,
            args.kill_rate,
            target_quantity=1
        )

    # Save results
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, 'w') as f:
        json.dump(results, f, indent=2)

    # Print summary
    print("\nLoot Simulation Results:")
    print(f"  Total drops: {results['total_drops']}")
    print(f"  Unique items: {results['unique_items']}")

    print("\nDrop Rate Analysis (kill rate: {}/hr):".format(args.kill_rate))
    for item_name in sorted(results['expected_rates'].keys()):
        expected = results['expected_rates'][item_name]
        actual = results['actual_rates'][item_name]
        deviation = results['deviations'][item_name]
        ttd = results['time_to_drop'][item_name]

        print(f"\n  {item_name}:")
        print(f"    Expected: {expected:.2%}")
        print(f"    Actual: {actual:.2%}")
        print(f"    Deviation: {deviation:+.1f}%")
        print(f"    Est. time to drop: {ttd['time_hours']:.1f} hours ({ttd['time_days']:.1f} days)")

    print("\nChi-squared Test:")
    chi = results['chi_squared_test']
    print(f"  χ² = {chi['chi_squared']:.4f}")
    print(f"  Significant? {chi['significant']}")

    print(f"\nSaved results to: {args.output}")


if __name__ == '__main__':
    main()
