# Common RPG Stat Formulas

A reference of proven stat formulas for Infinite Voyage. Each formula includes the
mathematical definition, behavior characteristics, tuning parameters, and a Python
implementation. Use these as building blocks when constructing balance spreadsheets.

---

## Damage Calculation Formulas

### Flat Damage Reduction (Armor as Subtraction)

The simplest armor model. Armor subtracts directly from incoming damage.

```
final_damage = max(base_damage - armor, minimum_damage)
```

**Characteristics:** Linear, easy to understand, but breaks at extremes. Low-armor
targets take huge damage; high-armor targets become invincible.

**When to use:** Simple games, early prototypes, low-level content where stat ranges
are small.

```python
def flat_damage(base_damage: float, armor: float, min_damage: float = 1.0) -> float:
    """Flat armor subtraction. Guarantees minimum damage."""
    return max(base_damage - armor, min_damage)

# Examples
print(flat_damage(100, 30))   # 70.0 damage (30 armor absorbed)
print(flat_damage(100, 95))   # 5.0 damage (most absorbed)
print(flat_damage(100, 110))  # 1.0 damage (minimum floor)
```

### Percentage Damage Reduction

Armor converts to a percentage that reduces incoming damage. Never reaches 100%.

```
reduction = armor / (armor + scaling_constant)
final_damage = base_damage * (1 - reduction)
```

**Characteristics:** Diminishing returns naturally built in. Each point of armor is
worth less than the previous one. The scaling constant controls how quickly armor
becomes less effective.

**When to use:** Most RPGs. This is the industry standard for good reason.

```python
def percentage_damage(base_damage: float, armor: float,
                      scaling_constant: float = 100.0) -> float:
    """Percentage-based armor reduction with diminishing returns."""
    reduction = armor / (armor + scaling_constant)
    return base_damage * (1 - reduction)

# Examples (scaling_constant = 100)
print(percentage_damage(100, 50))    # 66.7 damage (33% reduction)
print(percentage_damage(100, 100))   # 50.0 damage (50% reduction)
print(percentage_damage(100, 200))   # 33.3 damage (67% reduction)
print(percentage_damage(100, 1000))  # 9.1 damage (91% reduction, never 100%)
```

### Hybrid Damage Reduction

Combines flat reduction with percentage reduction for layered defense.

```
after_flat = max(base_damage - flat_armor, 0)
reduction = percent_armor / (percent_armor + scaling_constant)
final_damage = max(after_flat * (1 - reduction), minimum_damage)
```

**When to use:** Games with multiple defense stats (armor + resistance), or where
you want early-game flat reduction and late-game percentage scaling.

```python
def hybrid_damage(base_damage: float, flat_armor: float,
                  percent_armor: float, scaling_constant: float = 100.0,
                  min_damage: float = 1.0) -> float:
    """Two-layer defense: flat reduction first, then percentage."""
    after_flat = max(base_damage - flat_armor, 0)
    reduction = percent_armor / (percent_armor + scaling_constant)
    return max(after_flat * (1 - reduction), min_damage)

# Example: 100 damage vs 20 flat armor + 80 percent armor
print(hybrid_damage(100, 20, 80))  # 44.4 damage
```

---

## Critical Hit Formula

### Standard Critical Hit

```
if random() < crit_chance:
    final_damage = base_damage * crit_multiplier
else:
    final_damage = base_damage
```

**Tuning guidance:** Crit chance typically 5-25%. Crit multiplier typically 1.5x-2.5x.
Higher crit chance with lower multiplier feels consistent. Lower crit chance with
higher multiplier feels exciting but swingy.

```python
import random

def apply_critical(base_damage: float, crit_chance: float = 0.10,
                   crit_multiplier: float = 2.0) -> tuple[float, bool]:
    """Apply critical hit check. Returns (damage, was_crit)."""
    is_crit = random.random() < crit_chance
    if is_crit:
        return base_damage * crit_multiplier, True
    return base_damage, False

# Expected DPS increase from crit:
# effective_multiplier = 1 + (crit_chance * (crit_multiplier - 1))
# At 10% crit, 2x mult: 1 + (0.10 * 1.0) = 1.10 = 10% DPS increase
```

### Diminishing Crit Chance

Prevents crit stacking from reaching 100%.

```python
def effective_crit_chance(raw_crit: float, soft_cap: float = 0.40,
                          diminishing_factor: float = 0.5) -> float:
    """Crit chance with soft cap and diminishing returns above it."""
    if raw_crit <= soft_cap:
        return raw_crit
    excess = raw_crit - soft_cap
    return soft_cap + excess * diminishing_factor

# Examples
print(effective_crit_chance(0.30))  # 0.30 (below cap, unchanged)
print(effective_crit_chance(0.50))  # 0.45 (above cap, diminished)
print(effective_crit_chance(0.80))  # 0.60 (heavily diminished)
```

---

## Dodge and Evasion Formula

### Level-Adjusted Dodge

Dodge chance scales based on the level difference between attacker and defender.

```
effective_dodge = base_dodge - (attacker_level - defender_level) * level_penalty
effective_dodge = clamp(effective_dodge, floor, cap)
```

```python
def dodge_chance(base_dodge: float, attacker_level: int,
                 defender_level: int, level_penalty: float = 0.02,
                 floor: float = 0.01, cap: float = 0.50) -> float:
    """Dodge chance adjusted by level difference."""
    level_diff = attacker_level - defender_level
    effective = base_dodge - (level_diff * level_penalty)
    return max(floor, min(effective, cap))

# Same level: full dodge chance
print(dodge_chance(0.25, 10, 10))  # 0.25

# Attacker 5 levels higher: dodge reduced
print(dodge_chance(0.25, 15, 10))  # 0.15

# Defender 5 levels higher: dodge increased (capped)
print(dodge_chance(0.25, 5, 10))   # 0.35
```

---

## Level Scaling Formulas

### Linear Scaling

```
stat_at_level = base_stat + (growth_per_level * (level - 1))
```

**Characteristics:** Predictable, easy to balance. Each level feels the same amount
of growth. Works well for small level ranges (1-30).

```python
def linear_scaling(base: float, growth: float, level: int) -> float:
    """Linear stat growth per level."""
    return base + growth * (level - 1)

# Health example: 100 base + 10 per level
for lvl in [1, 10, 25, 50]:
    print(f"Level {lvl}: {linear_scaling(100, 10, lvl)} HP")
# Level 1: 100, Level 10: 190, Level 25: 340, Level 50: 590
```

### Exponential Scaling

```
stat_at_level = base_stat * (growth_rate ^ (level - 1))
```

**Characteristics:** Each level is a percentage increase over the previous. Creates
dramatic power growth. Can spiral out of control at high levels.

**When to use:** Games with prestige/reborn systems, or where power fantasy escalation
is the goal. Requires content to scale exponentially too.

```python
def exponential_scaling(base: float, growth_rate: float, level: int) -> float:
    """Exponential stat growth. growth_rate of 1.05 = 5% per level."""
    return base * (growth_rate ** (level - 1))

# Health example: 100 base, 5% growth per level
for lvl in [1, 10, 25, 50]:
    print(f"Level {lvl}: {exponential_scaling(100, 1.05, lvl):.0f} HP")
# Level 1: 100, Level 10: 155, Level 25: 322, Level 50: 1084
```

### Diminishing Returns Scaling (Logarithmic)

```
stat_at_level = base_stat + (coefficient * ln(level))
```

**Characteristics:** Fast early growth that slows progressively. Each level gives
less than the previous. Prevents runaway power while still rewarding leveling.

**When to use:** Secondary stats (crit, dodge, speed) where you want soft caps
without hard limits.

```python
import math

def diminishing_scaling(base: float, coefficient: float, level: int) -> float:
    """Logarithmic growth with diminishing returns."""
    return base + coefficient * math.log(level)

# Crit chance example: 5% base, 3% coefficient
for lvl in [1, 10, 25, 50]:
    print(f"Level {lvl}: {diminishing_scaling(5, 3, lvl):.1f}% crit")
# Level 1: 5.0%, Level 10: 11.9%, Level 25: 14.7%, Level 50: 16.7%
```

### S-Curve Scaling (Sigmoid)

```
stat_at_level = min_stat + (max_stat - min_stat) / (1 + e^(-steepness * (level - midpoint)))
```

**Characteristics:** Slow start, rapid mid-game growth, then plateaus at max. Creates
a natural "power spike" in the mid-game that feels exciting.

```python
import math

def sigmoid_scaling(level: int, min_val: float, max_val: float,
                    midpoint: float = 25.0, steepness: float = 0.2) -> float:
    """S-curve scaling between min and max values."""
    return min_val + (max_val - min_val) / (1 + math.exp(-steepness * (level - midpoint)))

# Health example: 100 min, 1000 max, midpoint at level 25
for lvl in [1, 10, 25, 40, 50]:
    print(f"Level {lvl}: {sigmoid_scaling(lvl, 100, 1000):.0f} HP")
# Level 1: 108, Level 10: 127, Level 25: 550, Level 40: 873, Level 50: 993
```

---

## Stat Soft Caps and Hard Caps

### Soft Cap Implementation

Stats scale normally up to a threshold, then at a reduced rate beyond it.

```python
def soft_capped_stat(raw_value: float, soft_cap: float,
                     reduction_factor: float = 0.5,
                     hard_cap: float = float('inf')) -> float:
    """Apply soft cap with optional hard cap."""
    if raw_value <= soft_cap:
        return min(raw_value, hard_cap)
    excess = raw_value - soft_cap
    effective = soft_cap + excess * reduction_factor
    return min(effective, hard_cap)

# Speed example: soft cap at 200, hard cap at 300
for raw in [100, 200, 250, 300, 400]:
    print(f"Raw {raw} -> Effective {soft_capped_stat(raw, 200, 0.5, 300):.0f}")
# Raw 100 -> 100, Raw 200 -> 200, Raw 250 -> 225, Raw 300 -> 250, Raw 400 -> 300
```

### Multi-Tier Cap System

Multiple breakpoints with decreasing effectiveness at each tier.

```python
def tiered_cap(raw_value: float, tiers: list[tuple[float, float]]) -> float:
    """
    Multi-tier cap system.
    tiers: list of (threshold, effectiveness) pairs, sorted by threshold.
    Example: [(100, 1.0), (200, 0.5), (300, 0.25)] means:
      0-100: full value, 100-200: 50% value, 200-300: 25% value, 300+: 0%
    """
    effective = 0.0
    prev_threshold = 0.0
    for threshold, effectiveness in tiers:
        if raw_value <= prev_threshold:
            break
        applicable = min(raw_value, threshold) - prev_threshold
        effective += applicable * effectiveness
        prev_threshold = threshold
    return effective

# Armor rating with 3 tiers
tiers = [(100, 1.0), (200, 0.5), (300, 0.25)]
for raw in [50, 100, 150, 200, 300, 500]:
    print(f"Raw {raw} -> Effective {tiered_cap(raw, tiers):.0f}")
# Raw 50 -> 50, Raw 100 -> 100, Raw 150 -> 125, Raw 200 -> 150, Raw 300 -> 175, Raw 500 -> 175
```

---

## XP and Level Curve

### Standard XP Curve

XP required per level increases polynomially.

```python
def xp_for_level(level: int, base_xp: float = 100.0,
                 exponent: float = 1.5, scaling: float = 1.0) -> float:
    """XP required to reach the next level from current level."""
    return base_xp * (level ** exponent) * scaling

def total_xp_to_level(target_level: int, base_xp: float = 100.0,
                      exponent: float = 1.5) -> float:
    """Total cumulative XP needed to reach a target level."""
    return sum(xp_for_level(lvl, base_xp, exponent) for lvl in range(1, target_level))

# XP table for levels 1-10
for lvl in range(1, 11):
    xp_needed = xp_for_level(lvl)
    cumulative = total_xp_to_level(lvl + 1)
    print(f"Level {lvl} -> {lvl+1}: {xp_needed:.0f} XP (cumulative: {cumulative:.0f})")
```

### Time-to-Level Targeting

Design XP curves to hit specific time targets.

```python
def xp_curve_from_time_targets(level_time_targets: dict[int, float],
                                xp_per_minute: float = 50.0) -> dict[int, float]:
    """
    Given target minutes-to-level, calculate XP requirements.
    level_time_targets: {level: minutes_to_reach_from_previous}
    xp_per_minute: expected XP earn rate at that level
    """
    xp_table = {}
    for level, minutes in level_time_targets.items():
        xp_table[level] = minutes * xp_per_minute
    return xp_table

# Design intent: early levels fast, later levels slower
targets = {2: 10, 5: 20, 10: 30, 20: 45, 30: 60, 50: 90}
xp_table = xp_curve_from_time_targets(targets)
for level, xp in xp_table.items():
    print(f"Level {level}: {xp:.0f} XP needed ({targets[level]} min)")
```

---

## Effective Health Pool

Combining health, armor, dodge, and healing into a single survivability metric.

```python
def effective_health(health: float, armor: float, dodge_chance: float,
                     scaling_constant: float = 100.0) -> float:
    """
    Calculate effective health pool considering armor and dodge.
    EHP = Health / ((1 - dodge) * (1 - armor_reduction))
    """
    armor_reduction = armor / (armor + scaling_constant)
    damage_taken_multiplier = (1 - dodge_chance) * (1 - armor_reduction)
    if damage_taken_multiplier <= 0:
        return float('inf')
    return health / damage_taken_multiplier

# Compare classes
print(f"Warrior: {effective_health(500, 100, 0.05):.0f} EHP")   # High HP, high armor
print(f"Rogue:   {effective_health(300, 40, 0.30):.0f} EHP")    # Low HP, high dodge
print(f"Mage:    {effective_health(250, 20, 0.05):.0f} EHP")    # Low everything
```

---

## Formula Selection Guide

| Stat Type     | Recommended Formula       | Reason                                    |
|---------------|---------------------------|-------------------------------------------|
| Health        | Linear or Sigmoid         | Predictable growth, clear power feel      |
| Damage        | Linear with % bonuses     | Base scales linearly, gear adds multipliers|
| Armor         | Percentage reduction      | Diminishing returns prevent invincibility |
| Crit chance   | Diminishing (log)         | Natural soft cap, never reaches 100%      |
| Dodge         | Level-adjusted with cap   | Prevents unhittable builds                |
| XP curve      | Polynomial (1.5 exponent) | Balanced pace, not too fast or slow       |
| Stat caps     | Tiered or soft cap        | Rewards investment without breaking game  |
