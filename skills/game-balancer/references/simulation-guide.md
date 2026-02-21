# Simulation Guide

How to set up, run, and interpret Monte Carlo and other simulations for game
balance work.

---

## When to Simulate vs. When to Calculate

| Approach | Use When | Example |
|----------|----------|---------|
| **Analytical** (closed-form math) | No randomness, simple formulas | "What's the TTK with these stats?" |
| **Monte Carlo** (random sampling) | RNG-dependent outcomes | "What's the TTK distribution with crit and dodge?" |
| **Sweep** (parameter space search) | Finding optimal parameter values | "What armor value gives 50% mitigation?" |
| **Time-series** (step-by-step) | Systems evolving over time | "How does the economy look after 6 months?" |

**Rule of thumb**: If the system has any randomness (crit, dodge, proc, drop rate),
use Monte Carlo. If it's deterministic, use analytical.

---

## Monte Carlo Simulation Basics

### The Core Pattern

```python
import numpy as np
from collections import defaultdict

def monte_carlo(simulate_fn, n_runs=10000, seed=42):
    """
    Run a simulation function n_runs times and collect results.

    Args:
        simulate_fn: Function that returns a dict of metrics for one run
        n_runs: Number of simulations (10k minimum, 100k for rare events)
        seed: Random seed for reproducibility

    Returns:
        Dict of metric_name -> list of values across all runs
    """
    np.random.seed(seed)
    results = defaultdict(list)

    for _ in range(n_runs):
        outcome = simulate_fn()
        for key, value in outcome.items():
            results[key].append(value)

    return dict(results)
```

### How Many Runs?

| Scenario | Minimum Runs | Reason |
|----------|-------------|--------|
| Combat (crit/dodge) | 10,000 | Common events (5-30% chance) converge quickly |
| Loot (rare drops) | 100,000 | Need volume to observe 0.1-1% drop rates |
| Economy (many variables) | 50,000 | Complex interactions need more samples |
| Edge cases (extreme builds) | 100,000 | Looking for worst-case scenarios |

**Verification**: Run twice with different seeds. If results differ by more than 2%,
increase the run count.

---

## Combat Simulation

### Setup

```python
def setup_combat_sim(attacker, defender):
    """
    Create a combat simulation function.

    attacker/defender are dicts with keys:
        hp, damage, attack_speed, armor, crit_chance, crit_multiplier,
        dodge_chance, abilities (list of ability dicts)
    """
    def simulate():
        atk_hp = attacker['hp']
        def_hp = defender['hp']
        time = 0.0
        turns = 0
        damage_dealt = 0

        while atk_hp > 0 and def_hp > 0:
            # Attacker turn
            if np.random.random() > defender['dodge_chance']:
                dmg = attacker['damage']
                if np.random.random() < attacker['crit_chance']:
                    dmg *= attacker['crit_multiplier']
                # Apply armor
                mitigation = defender['armor'] / (defender['armor'] + 100)
                dmg *= (1 - mitigation)
                def_hp -= dmg
                damage_dealt += dmg
            time += 1.0 / attacker['attack_speed']
            turns += 1

            if def_hp <= 0:
                break

            # Defender turn (simplified)
            if np.random.random() > attacker['dodge_chance']:
                dmg = defender['damage']
                if np.random.random() < defender['crit_chance']:
                    dmg *= defender['crit_multiplier']
                mitigation = attacker['armor'] / (attacker['armor'] + 100)
                dmg *= (1 - mitigation)
                atk_hp -= dmg
            time += 1.0 / defender['attack_speed']
            turns += 1

        return {
            'winner': 'attacker' if def_hp <= 0 else 'defender',
            'ttk': time,
            'turns': turns,
            'attacker_hp_remaining': max(0, atk_hp),
            'defender_hp_remaining': max(0, def_hp),
            'total_damage_dealt': damage_dealt
        }

    return simulate
```

### Using scripts/combat_sim.py

```bash
# Run combat simulation from JSON config
python scripts/combat_sim.py --config combat_config.json --runs 10000

# combat_config.json format:
{
  "attacker": {"hp": 1000, "damage": 50, "attack_speed": 1.5, ...},
  "defender": {"hp": 800, "damage": 40, "attack_speed": 1.2, ...},
  "runs": 10000,
  "output": "combat_results.json"
}
```

---

## Economy Simulation

### Setup

```python
def setup_economy_sim(faucets, sinks, player_count, duration_days):
    """
    Simulate economy over time.

    faucets: list of {"name": str, "gold_per_day_per_player": float}
    sinks: list of {"name": str, "gold_per_day_per_player": float, "optional": bool}
    """
    def simulate():
        total_supply = 0
        daily_snapshots = []

        for day in range(duration_days):
            # Faucets: all players earn
            daily_in = sum(f['gold_per_day_per_player'] for f in faucets) * player_count
            # Add randomness (±20% daily variance)
            daily_in *= np.random.uniform(0.8, 1.2)

            # Sinks: mandatory sinks always apply, optional sinks probability-based
            daily_out = 0
            for s in sinks:
                amount = s['gold_per_day_per_player'] * player_count
                if s.get('optional', False):
                    amount *= np.random.uniform(0.3, 0.8)  # partial participation
                daily_out += amount

            total_supply += daily_in - daily_out
            daily_snapshots.append(total_supply)

        return {
            'final_supply': total_supply,
            'peak_supply': max(daily_snapshots),
            'avg_daily_inflation': (daily_snapshots[-1] - daily_snapshots[0]) / max(1, duration_days),
            'monthly_inflation_rate': (daily_snapshots[-1] - daily_snapshots[0]) / max(1, daily_snapshots[0])
        }

    return simulate
```

---

## Loot Simulation

### Setup

```python
def setup_loot_sim(loot_table, n_drops):
    """
    Verify loot table drop rates.

    loot_table: list of {"item": str, "weight": float}
    Total weights do not need to sum to 1 (will be normalized).
    """
    items = [entry['item'] for entry in loot_table]
    weights = np.array([entry['weight'] for entry in loot_table])
    probabilities = weights / weights.sum()

    def simulate():
        drops = np.random.choice(items, size=n_drops, p=probabilities)
        counts = {item: 0 for item in items}
        for drop in drops:
            counts[drop] += 1

        return {
            f'{item}_rate': count / n_drops
            for item, count in counts.items()
        }

    return simulate
```

---

## Analyzing Simulation Results

### Standard Statistics

```python
def analyze_results(results, metric_name):
    values = results[metric_name]
    return {
        'mean': np.mean(values),
        'median': np.median(values),
        'std': np.std(values),
        'min': np.min(values),
        'max': np.max(values),
        'p5': np.percentile(values, 5),    # worst 5% of outcomes
        'p95': np.percentile(values, 95),   # best 5% of outcomes
        'cv': np.std(values) / np.mean(values),  # coefficient of variation
    }
```

### Interpreting Key Metrics

| Metric | Good Sign | Bad Sign |
|--------|-----------|----------|
| **CV (coefficient of variation)** | < 0.2 (consistent outcomes) | > 0.5 (wildly variable) |
| **p5 to p95 range** | Narrow (predictable) | Wide (too much RNG) |
| **Mean vs Median** | Close together (symmetric) | Far apart (skewed distribution) |
| **Min** | Reasonable worst case | Absurdly bad (feels unfair) |

### Visualization

```python
import matplotlib.pyplot as plt

def plot_distribution(values, title, target_range=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(values, bins=50, edgecolor='black', alpha=0.7)
    ax.axvline(np.mean(values), color='red', linestyle='--', label=f'Mean: {np.mean(values):.2f}')
    ax.axvline(np.median(values), color='blue', linestyle='--', label=f'Median: {np.median(values):.2f}')

    if target_range:
        ax.axvspan(target_range[0], target_range[1], alpha=0.1, color='green', label='Target Range')

    ax.set_title(title)
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.legend()
    plt.tight_layout()
    plt.savefig(f'{title.lower().replace(" ", "_")}.png', dpi=150)
    plt.close()
```

Use `scripts/visualize.py` for pre-built chart functions.

---

## Simulation Workflow Checklist

```
[ ] Define what you're measuring and what "balanced" looks like
[ ] Choose simulation type (Monte Carlo, sweep, time-series)
[ ] Set parameters from current GDD values
[ ] Run with minimum required iterations
[ ] Verify reproducibility (same seed = same results)
[ ] Analyze distribution (mean, median, std, percentiles)
[ ] Compare against target ranges
[ ] Visualize (histogram for distributions, time-series for economy)
[ ] Document findings in balance report format
[ ] If out of range: adjust parameters and re-run
```

---

## Common Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| Too few runs | Unstable results, false conclusions | Use 10k+ minimum |
| No seed | Can't reproduce results | Always set `np.random.seed()` |
| Ignoring distributions | Mean looks fine but outliers are terrible | Always check p5/p95 |
| Simulating in isolation | Combat sim ignores economy, economy sim ignores progression | Note which systems are excluded and why |
| Over-fitting to simulation | Tuning parameters to match sim exactly | Sim is a model, not the game — use as guide, not gospel |
