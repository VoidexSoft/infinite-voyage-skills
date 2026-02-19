#!/usr/bin/env python3
"""
Parameter Optimizer for game balance tuning.

Implements hill-climbing and grid-search optimization to find parameter values
that minimize deviation from target metrics (e.g., target DPS, target TTK,
target win rate). Uses the same combat stat concepts as combat_sim.py.

Accepts a JSON config describing parameter ranges, an evaluation function
specification, and target metrics. Outputs the best parameter set as JSON.
"""

import argparse
import json
import math
import random
import itertools
from pathlib import Path
from typing import Dict, List, Any, Tuple, Callable, Optional
from dataclasses import dataclass, asdict, field
from datetime import datetime


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class ParameterRange:
    """Definition of a tunable parameter with its valid range."""
    name: str
    min_value: float
    max_value: float
    step: float = 1.0
    initial: Optional[float] = None

    def clamp(self, value: float) -> float:
        """Clamp value to valid range."""
        return max(self.min_value, min(self.max_value, value))

    def discrete_values(self) -> List[float]:
        """Return all discrete values in the range (for grid search)."""
        values: List[float] = []
        v = self.min_value
        while v <= self.max_value + 1e-9:
            values.append(round(v, 6))
            v += self.step
        return values


@dataclass
class TargetMetric:
    """A metric we want the optimized parameters to achieve."""
    name: str
    target: float
    weight: float = 1.0


@dataclass
class OptimizationResult:
    """Result of an optimization run."""
    method: str
    best_params: Dict[str, float]
    best_score: float
    target_deviations: Dict[str, float]
    iterations: int
    evaluations: int
    elapsed_seconds: float = 0.0


# ---------------------------------------------------------------------------
# Built-in evaluation functions (combat-oriented)
# ---------------------------------------------------------------------------

def _dps_formula(params: Dict[str, float]) -> Dict[str, float]:
    """
    Evaluate DPS-related metrics from combat parameters.

    Expected params: attack_power, attack_speed, critical_chance,
                     critical_multiplier, armor, health
    """
    ap = params.get('attack_power', 10.0)
    speed = params.get('attack_speed', 1.0)
    crit_chance = params.get('critical_chance', 0.0)
    crit_mult = params.get('critical_multiplier', 1.5)
    armor = params.get('armor', 0.0)
    health = params.get('health', 100.0)

    # Effective DPS (before armor)
    base_dps = ap * speed
    crit_dps = base_dps * (1.0 + crit_chance * (crit_mult - 1.0))

    # Post-armor DPS (flat reduction model)
    effective_dps = max(1.0, crit_dps - armor * speed)

    # Time to kill
    ttk = health / max(effective_dps, 0.01)

    # Effective health (inverse of incoming damage rate)
    ehp = health + armor * (health / max(ap, 1.0))

    return {
        'dps': round(crit_dps, 4),
        'effective_dps': round(effective_dps, 4),
        'ttk': round(ttk, 4),
        'ehp': round(ehp, 4),
    }


def _economy_formula(params: Dict[str, float]) -> Dict[str, float]:
    """
    Evaluate economy metrics from economic parameters.

    Expected params: faucet_rate, sink_rate, initial_currency, item_cost
    """
    faucet = params.get('faucet_rate', 100.0)
    sink = params.get('sink_rate', 80.0)
    initial = params.get('initial_currency', 1000.0)
    item_cost = params.get('item_cost', 5000.0)

    net_flow = faucet - sink
    if net_flow > 0:
        time_to_afford = max(0, (item_cost - initial) / net_flow)
    else:
        time_to_afford = 9999.0

    faucet_sink_ratio = faucet / max(sink, 0.01)
    inflation_rate = (net_flow / max(initial, 1.0)) * 100.0

    return {
        'net_flow': round(net_flow, 4),
        'time_to_afford': round(time_to_afford, 4),
        'faucet_sink_ratio': round(faucet_sink_ratio, 4),
        'inflation_rate': round(inflation_rate, 4),
    }


EVAL_FUNCTIONS: Dict[str, Callable[[Dict[str, float]], Dict[str, float]]] = {
    'combat': _dps_formula,
    'economy': _economy_formula,
}


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def compute_score(
    metrics: Dict[str, float],
    targets: List[TargetMetric],
) -> Tuple[float, Dict[str, float]]:
    """
    Compute weighted deviation score (lower is better).

    Returns:
        (total_score, per_target_deviations)
    """
    total = 0.0
    deviations: Dict[str, float] = {}

    for t in targets:
        actual = metrics.get(t.name)
        if actual is None:
            # Metric not produced -- heavy penalty
            dev = 1e6
        else:
            # Relative deviation
            if t.target != 0:
                dev = abs(actual - t.target) / abs(t.target)
            else:
                dev = abs(actual - t.target)
        deviations[t.name] = round(dev, 6)
        total += dev * t.weight

    return round(total, 6), deviations


# ---------------------------------------------------------------------------
# Optimizers
# ---------------------------------------------------------------------------

class HillClimbOptimizer:
    """
    Stochastic hill-climbing optimizer with random restarts.

    At each step, perturbs a random parameter by its step size and keeps the
    change if it improves the score.
    """

    def __init__(
        self,
        parameters: List[ParameterRange],
        targets: List[TargetMetric],
        eval_fn: Callable[[Dict[str, float]], Dict[str, float]],
        max_iterations: int = 5000,
        restarts: int = 5,
        seed: Optional[int] = None,
    ):
        self.parameters = parameters
        self.targets = targets
        self.eval_fn = eval_fn
        self.max_iterations = max_iterations
        self.restarts = restarts
        self.evaluations = 0

        if seed is not None:
            random.seed(seed)

    def _random_params(self) -> Dict[str, float]:
        """Generate random parameter set within ranges."""
        return {
            p.name: round(
                random.uniform(p.min_value, p.max_value), 6
            )
            for p in self.parameters
        }

    def _initial_params(self) -> Dict[str, float]:
        """Generate initial parameter set (use initial values if given)."""
        params: Dict[str, float] = {}
        for p in self.parameters:
            if p.initial is not None:
                params[p.name] = p.initial
            else:
                params[p.name] = round(
                    (p.min_value + p.max_value) / 2.0, 6
                )
        return params

    def _evaluate(self, params: Dict[str, float]) -> Tuple[float, Dict[str, float]]:
        """Evaluate parameter set and return (score, deviations)."""
        self.evaluations += 1
        metrics = self.eval_fn(params)
        return compute_score(metrics, self.targets)

    def optimize(self) -> OptimizationResult:
        """Run hill-climbing optimization with random restarts."""
        import time
        start_time = time.time()

        best_params: Dict[str, float] = {}
        best_score = float('inf')
        best_devs: Dict[str, float] = {}
        total_iterations = 0
        self.evaluations = 0

        for restart in range(self.restarts):
            if restart == 0:
                current = self._initial_params()
            else:
                current = self._random_params()

            current_score, current_devs = self._evaluate(current)

            for iteration in range(self.max_iterations):
                total_iterations += 1

                # Pick a random parameter to perturb
                param = random.choice(self.parameters)
                direction = random.choice([-1, 1])
                step = param.step * direction

                candidate = dict(current)
                candidate[param.name] = param.clamp(
                    candidate[param.name] + step
                )

                cand_score, cand_devs = self._evaluate(candidate)

                if cand_score < current_score:
                    current = candidate
                    current_score = cand_score
                    current_devs = cand_devs

                # Early exit if perfect score
                if current_score < 1e-8:
                    break

            if current_score < best_score:
                best_params = dict(current)
                best_score = current_score
                best_devs = dict(current_devs)

        elapsed = time.time() - start_time

        return OptimizationResult(
            method='hill_climbing',
            best_params=best_params,
            best_score=best_score,
            target_deviations=best_devs,
            iterations=total_iterations,
            evaluations=self.evaluations,
            elapsed_seconds=round(elapsed, 3),
        )


class GridSearchOptimizer:
    """
    Exhaustive grid-search optimizer.

    Evaluates every combination of discrete parameter values. Best for small
    parameter spaces; use with caution on large grids.
    """

    def __init__(
        self,
        parameters: List[ParameterRange],
        targets: List[TargetMetric],
        eval_fn: Callable[[Dict[str, float]], Dict[str, float]],
        max_evaluations: int = 100000,
    ):
        self.parameters = parameters
        self.targets = targets
        self.eval_fn = eval_fn
        self.max_evaluations = max_evaluations
        self.evaluations = 0

    def optimize(self) -> OptimizationResult:
        """Run grid search over all parameter combinations."""
        import time
        start_time = time.time()

        # Build per-parameter value lists
        param_values: List[List[float]] = [
            p.discrete_values() for p in self.parameters
        ]
        param_names = [p.name for p in self.parameters]

        # Estimate grid size
        grid_size = 1
        for vals in param_values:
            grid_size *= len(vals)

        if grid_size > self.max_evaluations:
            print(
                f"Warning: Grid size ({grid_size}) exceeds max evaluations "
                f"({self.max_evaluations}). Sampling randomly."
            )
            return self._random_sample_search(param_names, param_values, start_time)

        best_params: Dict[str, float] = {}
        best_score = float('inf')
        best_devs: Dict[str, float] = {}
        self.evaluations = 0

        for combo in itertools.product(*param_values):
            self.evaluations += 1
            params = dict(zip(param_names, combo))
            metrics = self.eval_fn(params)
            score, devs = compute_score(metrics, self.targets)

            if score < best_score:
                best_score = score
                best_params = dict(params)
                best_devs = dict(devs)

            if best_score < 1e-8:
                break

        elapsed = time.time() - start_time

        return OptimizationResult(
            method='grid_search',
            best_params=best_params,
            best_score=best_score,
            target_deviations=best_devs,
            iterations=self.evaluations,
            evaluations=self.evaluations,
            elapsed_seconds=round(elapsed, 3),
        )

    def _random_sample_search(
        self,
        param_names: List[str],
        param_values: List[List[float]],
        start_time: float,
    ) -> OptimizationResult:
        """Fallback: random sampling when grid is too large."""
        best_params: Dict[str, float] = {}
        best_score = float('inf')
        best_devs: Dict[str, float] = {}
        self.evaluations = 0

        for _ in range(self.max_evaluations):
            self.evaluations += 1
            combo = tuple(random.choice(vals) for vals in param_values)
            params = dict(zip(param_names, combo))
            metrics = self.eval_fn(params)
            score, devs = compute_score(metrics, self.targets)

            if score < best_score:
                best_score = score
                best_params = dict(params)
                best_devs = dict(devs)

            if best_score < 1e-8:
                break

        import time
        elapsed = time.time() - start_time

        return OptimizationResult(
            method='grid_search_sampled',
            best_params=best_params,
            best_score=best_score,
            target_deviations=best_devs,
            iterations=self.evaluations,
            evaluations=self.evaluations,
            elapsed_seconds=round(elapsed, 3),
        )


# ---------------------------------------------------------------------------
# Config loading
# ---------------------------------------------------------------------------

def load_config(config_path: Path) -> Dict[str, Any]:
    """Load optimization configuration from JSON."""
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def parse_parameters(config: Dict[str, Any]) -> List[ParameterRange]:
    """Parse parameter definitions from config."""
    params: List[ParameterRange] = []
    for p in config.get('parameters', []):
        params.append(ParameterRange(
            name=p['name'],
            min_value=p['min'],
            max_value=p['max'],
            step=p.get('step', 1.0),
            initial=p.get('initial'),
        ))
    return params


def parse_targets(config: Dict[str, Any]) -> List[TargetMetric]:
    """Parse target metric definitions from config."""
    targets: List[TargetMetric] = []
    for t in config.get('targets', []):
        targets.append(TargetMetric(
            name=t['name'],
            target=t['target'],
            weight=t.get('weight', 1.0),
        ))
    return targets


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Optimize game balance parameters to match target metrics'
    )
    parser.add_argument(
        '--config',
        type=Path,
        required=True,
        help='Optimization config JSON file (parameters, targets, eval_function)'
    )
    parser.add_argument(
        '--method',
        choices=['hill_climbing', 'grid_search'],
        default='hill_climbing',
        help='Optimization method (default: hill_climbing)'
    )
    parser.add_argument(
        '--iterations',
        type=int,
        default=5000,
        help='Max iterations for hill climbing (default: 5000)'
    )
    parser.add_argument(
        '--restarts',
        type=int,
        default=5,
        help='Random restarts for hill climbing (default: 5)'
    )
    parser.add_argument(
        '--max-evals',
        type=int,
        default=100000,
        help='Max evaluations for grid search (default: 100000)'
    )
    parser.add_argument(
        '--seed',
        type=int,
        default=None,
        help='Random seed for reproducibility'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path('optimized_params.json'),
        help='Output path for results JSON'
    )

    args = parser.parse_args()

    # Load configuration
    config = load_config(args.config)
    parameters = parse_parameters(config)
    targets = parse_targets(config)

    if not parameters:
        print("Error: No parameters defined in config.")
        return

    if not targets:
        print("Error: No target metrics defined in config.")
        return

    # Select evaluation function
    eval_name = config.get('eval_function', 'combat')
    if eval_name not in EVAL_FUNCTIONS:
        print(
            f"Error: Unknown eval_function '{eval_name}'. "
            f"Available: {list(EVAL_FUNCTIONS.keys())}"
        )
        return
    eval_fn = EVAL_FUNCTIONS[eval_name]

    # Print configuration
    print(f"Optimizer: {args.method}")
    print(f"Eval function: {eval_name}")
    print(f"Parameters: {len(parameters)}")
    print(f"Targets: {len(targets)}")
    print()

    # Run optimization
    if args.method == 'hill_climbing':
        optimizer = HillClimbOptimizer(
            parameters=parameters,
            targets=targets,
            eval_fn=eval_fn,
            max_iterations=args.iterations,
            restarts=args.restarts,
            seed=args.seed,
        )
    else:
        optimizer = GridSearchOptimizer(
            parameters=parameters,
            targets=targets,
            eval_fn=eval_fn,
            max_evaluations=args.max_evals,
        )

    print("Running optimization...")
    result = optimizer.optimize()

    # Build output
    output_data = {
        'metadata': {
            'generated_at': datetime.now().isoformat(),
            'config_file': str(args.config),
            'eval_function': eval_name,
        },
        'result': asdict(result),
        'final_metrics': EVAL_FUNCTIONS[eval_name](result.best_params),
        'targets': [asdict(t) for t in targets],
        'parameters': [asdict(p) for p in parameters],
    }

    # Save results
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2)

    # Print results
    print(f"\nOptimization Complete ({result.method})")
    print(f"  Iterations : {result.iterations}")
    print(f"  Evaluations: {result.evaluations}")
    print(f"  Elapsed    : {result.elapsed_seconds:.3f}s")
    print(f"  Best Score : {result.best_score:.6f} (lower is better)")

    print(f"\nOptimized Parameters:")
    for name, value in sorted(result.best_params.items()):
        print(f"  {name}: {value:.4f}")

    final_metrics = output_data['final_metrics']
    print(f"\nResulting Metrics:")
    for name, value in sorted(final_metrics.items()):
        print(f"  {name}: {value:.4f}")

    print(f"\nTarget Deviations:")
    for t in targets:
        dev = result.target_deviations.get(t.name, 'N/A')
        actual = final_metrics.get(t.name, 'N/A')
        if isinstance(dev, float):
            print(f"  {t.name}: target={t.target:.4f}  actual={actual}  deviation={dev:.4%}")
        else:
            print(f"  {t.name}: target={t.target:.4f}  actual={actual}  deviation={dev}")

    print(f"\nSaved results to: {args.output}")


if __name__ == '__main__':
    main()
