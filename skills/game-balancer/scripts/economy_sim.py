#!/usr/bin/env python3
"""
Economy flow simulator for game balancing.

Simulates currency flow over time with configurable sources (faucets) and
drains (sinks). Analyzes inflation/deflation, affordability, and balance.
"""

import argparse
import json
import math
from pathlib import Path
from typing import Dict, List, Any


class EconomySimulator:
    """Simulates game economy over time."""

    def __init__(
        self,
        initial_currency: float,
        faucets: List[Dict[str, float]],
        sinks: List[Dict[str, float]],
        target_items: Dict[str, float] = None,
        max_turns: int = 365,
    ):
        """
        Initialize economy simulator.

        Args:
            initial_currency: Starting currency amount per player
            faucets: List of currency sources, each with 'name' and 'amount' (per turn)
            sinks: List of currency drains, each with 'name' and 'amount' (per turn)
            target_items: Dictionary of item names and their costs
            max_turns: Number of turns to simulate
        """
        self.initial_currency = initial_currency
        self.faucets = faucets
        self.sinks = sinks
        self.target_items = target_items or {}
        self.max_turns = max_turns

    def calculate_faucet_total(self) -> float:
        """Get total currency generated per turn."""
        return sum(f.get('amount', 0) for f in self.faucets)

    def calculate_sink_total(self) -> float:
        """Get total currency removed per turn."""
        return sum(s.get('amount', 0) for s in self.sinks)

    def simulate(self) -> Dict[str, Any]:
        """
        Run economy simulation.

        Returns:
            Dictionary with simulation results
        """
        balance_history = [self.initial_currency]
        current_balance = self.initial_currency

        faucet_total = self.calculate_faucet_total()
        sink_total = self.calculate_sink_total()
        net_flow = faucet_total - sink_total

        # Simulate each turn
        for turn in range(1, self.max_turns + 1):
            current_balance += net_flow
            balance_history.append(current_balance)

        # Calculate statistics
        min_balance = min(balance_history)
        max_balance = max(balance_history)
        final_balance = balance_history[-1]

        # Calculate inflation rate
        inflation_rate = (net_flow / max(self.initial_currency, 1)) * 100 if self.max_turns > 0 else 0

        # Calculate time to afford items
        time_to_afford = {}
        for item_name, cost in self.target_items.items():
            if cost <= self.initial_currency:
                time_to_afford[item_name] = 0
            elif net_flow > 0:
                turns_needed = (cost - self.initial_currency) / net_flow
                time_to_afford[item_name] = turns_needed
            else:
                time_to_afford[item_name] = float('inf')

        # Build results
        results = {
            'max_turns': self.max_turns,
            'initial_balance': self.initial_currency,
            'final_balance': final_balance,
            'min_balance': min_balance,
            'max_balance': max_balance,
            'net_flow_per_turn': net_flow,
            'faucets_per_turn': faucet_total,
            'sinks_per_turn': sink_total,
            'faucet_sink_ratio': faucet_total / sink_total if sink_total > 0 else 0,
            'inflation_rate': inflation_rate,
            'balance_history': balance_history,
            'time_to_afford': time_to_afford,
            'economy_status': self._classify_economy(net_flow, inflation_rate),
        }

        return results

    def _classify_economy(self, net_flow: float, inflation_rate: float) -> str:
        """Classify economy health."""
        if abs(net_flow) < 0.01:
            return 'balanced'
        elif net_flow > 0:
            if inflation_rate > 10:
                return 'hyperinflation'
            elif inflation_rate > 2:
                return 'inflation'
            else:
                return 'slow_growth'
        else:
            return 'deflation'


def calculate_sink_faucet_analysis(results: Dict[str, Any]) -> Dict[str, Any]:
    """
    Analyze sink and faucet balance.

    Args:
        results: Simulation results

    Returns:
        Analysis dictionary
    """
    ratio = results['faucet_sink_ratio']

    if ratio == 0:
        analysis_text = 'No currency sources (economy dies)'
    elif ratio < 0.5:
        analysis_text = 'Severe deflation risk (sinks heavily outweigh faucets)'
    elif ratio < 0.95:
        analysis_text = 'Mild deflation (more sinks than faucets)'
    elif ratio < 1.05:
        analysis_text = 'Balanced (faucets ≈ sinks)'
    elif ratio < 2.0:
        analysis_text = 'Mild inflation (more faucets than sinks)'
    else:
        analysis_text = 'Severe inflation risk (faucets heavily outweigh sinks)'

    return {
        'ratio': ratio,
        'analysis': analysis_text,
        'recommendation': _get_balance_recommendation(ratio),
    }


def _get_balance_recommendation(ratio: float) -> str:
    """Get recommendation for economy balance."""
    if 0.95 <= ratio <= 1.05:
        return 'Economy appears balanced'
    elif ratio < 0.95:
        return 'Consider adding currency sources or reducing sinks'
    else:
        return 'Consider adding currency sinks or reducing sources'


def calculate_velocity(balance_history: List[float]) -> float:
    """
    Calculate velocity of currency change (average change per turn).

    Args:
        balance_history: List of balance values per turn

    Returns:
        Average change per turn
    """
    if len(balance_history) < 2:
        return 0

    total_change = balance_history[-1] - balance_history[0]
    turns = len(balance_history) - 1

    return total_change / turns if turns > 0 else 0


def load_economy_config(config_path: Path) -> Dict[str, Any]:
    """Load economy configuration from JSON."""
    with open(config_path, 'r') as f:
        return json.load(f)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description='Economy flow simulator')
    parser.add_argument(
        '--config',
        type=Path,
        required=True,
        help='Economy configuration JSON file'
    )
    parser.add_argument(
        '--turns',
        type=int,
        default=365,
        help='Number of turns to simulate'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path('economy_results.json'),
        help='Output path for results JSON'
    )
    parser.add_argument(
        '--plot',
        action='store_true',
        help='Generate matplotlib chart'
    )

    args = parser.parse_args()

    # Load configuration
    config = load_economy_config(args.config)

    # Create simulator
    sim = EconomySimulator(
        initial_currency=config.get('initial_currency', 1000),
        faucets=config.get('faucets', []),
        sinks=config.get('sinks', []),
        target_items=config.get('target_items', {}),
        max_turns=args.turns,
    )

    # Run simulation
    print(f"Simulating economy for {args.turns} turns...")
    results = sim.simulate()

    # Add analysis
    results['sink_faucet_analysis'] = calculate_sink_faucet_analysis(results)
    results['velocity'] = calculate_velocity(results['balance_history'])

    # Save results
    args.output.parent.mkdir(parents=True, exist_ok=True)

    # Convert to JSON-serializable format
    output_data = dict(results)
    with open(args.output, 'w') as f:
        json.dump(output_data, f, indent=2)

    # Print summary
    print("\nEconomy Simulation Results:")
    print(f"  Initial balance: {results['initial_balance']:.2f}")
    print(f"  Final balance: {results['final_balance']:.2f}")
    print(f"  Min balance: {results['min_balance']:.2f}")
    print(f"  Max balance: {results['max_balance']:.2f}")

    print(f"\nFlow Analysis:")
    print(f"  Faucets (per turn): {results['faucets_per_turn']:.2f}")
    print(f"  Sinks (per turn): {results['sinks_per_turn']:.2f}")
    print(f"  Net flow (per turn): {results['net_flow_per_turn']:.2f}")
    print(f"  Faucet/Sink ratio: {results['faucet_sink_ratio']:.2f}")
    print(f"  Inflation rate: {results['inflation_rate']:.2f}% per turn")
    print(f"  Economy status: {results['economy_status']}")

    print(f"\nBalance Assessment:")
    analysis = results['sink_faucet_analysis']
    print(f"  {analysis['analysis']}")
    print(f"  {analysis['recommendation']}")

    if results['time_to_afford']:
        print(f"\nTime to Afford Items:")
        for item, turns in results['time_to_afford'].items():
            if turns == float('inf'):
                print(f"  {item}: Impossible (net flow <= 0)")
            else:
                days = turns / 24 if turns < 1000 else turns / 365
                unit = 'hours' if turns < 1000 else 'days'
                print(f"  {item}: {turns:.1f} turns ({days:.1f} {unit})")

    # Plot if requested
    if args.plot:
        try:
            import matplotlib.pyplot as plt

            plt.figure(figsize=(12, 6))
            turns = range(len(results['balance_history']))
            plt.plot(turns, results['balance_history'], linewidth=2)
            plt.xlabel('Turn', fontsize=12)
            plt.ylabel('Currency Balance', fontsize=12)
            plt.title('Economy Balance Over Time', fontsize=14, fontweight='bold')
            plt.grid(True, alpha=0.3)
            plt.tight_layout()

            chart_path = args.output.with_suffix('.png')
            plt.savefig(chart_path, dpi=150, format='png')
            print(f"\nSaved chart to: {chart_path}")
            plt.close()

        except ImportError:
            print("\nmatplotlib not available. Skipping chart generation.")

    print(f"\nSaved results to: {args.output}")


if __name__ == '__main__':
    main()
