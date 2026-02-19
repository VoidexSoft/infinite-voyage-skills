# Common Game Balance Formulas

A reference library of standard formulas used in RPGs, action games, and
roguelikes. Each formula includes its purpose, parameters, behavior, and
when to use it.

---

## Stat Scaling Curves

### Linear Scaling

```python
def linear(base, growth, level):
    return base + growth * (level - 1)
```

| Parameter | Meaning |
|-----------|---------|
| `base` | Starting value at level 1 |
| `growth` | Fixed increase per level |

**Behavior**: Steady, predictable growth. Power difference between adjacent levels
stays constant.

**Use when**: You want predictable, easy-to-communicate scaling (e.g., "each level
gives +5 HP"). Good for tutorial-phase stats.

**Caution**: At high levels, growth becomes negligible relative to total (level 100:
+5 HP on top of 500 HP is only 1% increase).

---

### Exponential Scaling

```python
def exponential(base, growth_rate, level):
    return base * (growth_rate ** (level - 1))
```

| Parameter | Meaning |
|-----------|---------|
| `base` | Starting value at level 1 |
| `growth_rate` | Multiplicative factor per level (e.g., 1.05 = 5% per level) |

**Behavior**: Each level is a fixed percentage stronger than the previous.
Accelerates at higher levels.

**Use when**: Progression should feel increasingly powerful (e.g., RPG damage
scaling, enemy HP in later zones).

**Caution**: Grows fast. At 5% per level: level 50 is 11.5x base, level 100 is
131x base. Cap or transition curves to prevent absurd values.

**Common growth rates**:
- 1.02-1.03: Gentle scaling (hundreds of levels)
- 1.05-1.08: Standard RPG scaling (50-100 levels)
- 1.10-1.15: Aggressive scaling (20-40 levels)

---

### Diminishing Returns

```python
def diminishing_returns(base, cap, rate, level):
    return cap - (cap - base) * math.exp(-rate * (level - 1))
```

| Parameter | Meaning |
|-----------|---------|
| `base` | Starting value |
| `cap` | Maximum asymptotic value |
| `rate` | How quickly it approaches the cap |

**Behavior**: Fast growth early, then slows as it approaches the cap. Never
exceeds the cap value.

**Use when**: A stat should be investable but not infinitely stackable
(e.g., armor, crit chance, cooldown reduction, dodge chance).

**Common caps**:
- Crit chance: 50-75%
- Dodge/evasion: 40-60%
- Cooldown reduction: 40-50%
- Armor mitigation: 75-85%

---

### S-Curve (Logistic)

```python
def s_curve(base, cap, midpoint, steepness, level):
    return base + (cap - base) / (1 + math.exp(-steepness * (level - midpoint)))
```

| Parameter | Meaning |
|-----------|---------|
| `base` | Minimum value |
| `cap` | Maximum value |
| `midpoint` | Level where growth is fastest |
| `steepness` | How sharp the transition is |

**Behavior**: Slow start, rapid growth in the middle, then plateaus. Creates a
natural "power spike" at the midpoint.

**Use when**: Progression should have a clear power spike moment (e.g., class
unlock at level 20 feels transformative, then stabilizes).

---

### Stepped Curve

```python
def stepped(base, growth, level, step_size=5):
    return base + growth * (level // step_size)
```

**Behavior**: Flat within each tier, jumps at breakpoints. Creates clear
progression milestones.

**Use when**: Progression should have noticeable tier boundaries
(e.g., gear tiers every 10 levels, skill unlocks every 5 levels).

---

### Polynomial Scaling

```python
def polynomial(base, coefficient, level, power=2):
    return base + coefficient * ((level - 1) ** power)
```

**Behavior**: Quadratic (power=2) grows faster than linear but slower than
exponential. Cubic (power=3) is more aggressive.

**Use when**: You need something between linear and exponential. Good for XP
requirements per level.

---

## XP and Progression Formulas

### XP Required Per Level

```python
# Standard quadratic XP curve
def xp_to_level(level, base_xp=100, exponent=1.5):
    return int(base_xp * (level ** exponent))

# Equivalent: XP for a given level
# Level 1:  100 XP
# Level 10: 3,162 XP
# Level 50: 35,355 XP
```

**Tuning guide**:
- `exponent = 1.0`: Linear (constant time per level) — casual-friendly
- `exponent = 1.5`: Moderate curve — standard RPG feel
- `exponent = 2.0`: Steep curve — endgame grind, use sparingly

### Total XP to Reach Level

```python
def total_xp_to_level(target_level, base_xp=100, exponent=1.5):
    return sum(xp_to_level(l, base_xp, exponent) for l in range(1, target_level))
```

### Expected Time Per Level

```python
def hours_per_level(level, xp_per_hour, base_xp=100, exponent=1.5):
    return xp_to_level(level, base_xp, exponent) / xp_per_hour
```

**Target**: 15-30 minutes per level in early game, 1-2 hours mid-game,
2-4 hours late-game. Beyond 4 hours per level risks grind wall anti-pattern.

---

## Combat Formulas

### Damage Calculation

**Flat reduction (armor as flat damage reduction)**:
```python
damage = max(1, raw_damage - armor)
```
Simple but breaks at high armor values (damage goes to 1).

**Percentage reduction (armor as mitigation %)**:
```python
mitigation = armor / (armor + constant)  # e.g., constant = 100
damage = raw_damage * (1 - mitigation)
```
Self-balancing: doubling armor doesn't double mitigation. The `constant` controls
how much armor is needed for 50% reduction.

| Constant | Armor for 50% mitigation | Feel |
|----------|-------------------------|------|
| 50 | 50 armor | Squishy game, armor matters early |
| 100 | 100 armor | Standard RPG |
| 200 | 200 armor | Armor is a long-term investment |

**Effective HP (EHP)**:
```python
ehp = hp * (1 + armor / constant)
# or equivalently:
ehp = hp / (1 - mitigation)
```

### Time to Kill (TTK)

```python
ttk = target_ehp / attacker_dps
```

**Target TTK ranges** (PvE):
- Trash mobs: 2-4 seconds
- Standard enemies: 5-10 seconds
- Elite enemies: 15-30 seconds
- Mini-bosses: 60-120 seconds
- Bosses: 180-600 seconds (3-10 minutes)

### DPS Calculation

```python
# Base DPS
dps = (base_damage * hits_per_second)

# With critical hits
dps = base_damage * hits_per_second * (1 + crit_chance * (crit_multiplier - 1))

# With hit chance
dps = base_damage * hits_per_second * hit_chance * (1 + crit_chance * (crit_multiplier - 1))
```

### Healing Per Second (HPS)

```python
hps = heal_amount / cast_time
effective_hps = hps * (1 - overheal_rate)
```

**Balance target**: Tank HPS should sustain against 70-80% of incoming DPS,
requiring active play (dodging, abilities) for the remaining 20-30%.

---

## Economy Formulas

### Gold Per Hour (GPH)

```python
gph = (mob_kills_per_hour * avg_gold_per_kill) +
      (quests_per_hour * avg_quest_gold) +
      (loot_sales_per_hour * avg_sale_value)
```

### Time to Afford Item

```python
hours_to_afford = item_price / gph
```

**Target**: Key upgrades should take 1-3 play sessions to afford. Aspirational
items (mounts, cosmetics) can take 2-4 weeks.

### Inflation Rate

```python
monthly_inflation = (total_currency_end - total_currency_start) / total_currency_start
```

**Healthy range**: 0-5% monthly. Above 5% requires intervention (see
economy-anti-patterns.md).

### Sink-Faucet Ratio

```python
sink_faucet_ratio = total_currency_removed / total_currency_created
```

**Target**: 0.7-0.9 (slight net inflow to reward play, but mostly balanced).

---

## Loot and Probability

### Drop Rate Verification

```python
# Expected drops in N kills
expected = drop_rate * n_kills

# Standard deviation (binomial)
std_dev = math.sqrt(n_kills * drop_rate * (1 - drop_rate))

# 95% confidence interval
ci_low = expected - 1.96 * std_dev
ci_high = expected + 1.96 * std_dev
```

### Pity System (Guaranteed Drop)

```python
def pity_drop_rate(base_rate, attempts_since_last, pity_threshold):
    if attempts_since_last >= pity_threshold:
        return 1.0  # guaranteed
    # Escalating probability
    return base_rate + (1 - base_rate) * (attempts_since_last / pity_threshold) ** 2
```

### Expected Attempts for Drop

```python
# Average attempts needed for a drop with probability p
expected_attempts = 1 / drop_rate

# Attempts for X% confidence of at least one drop
attempts_for_confidence = math.log(1 - confidence) / math.log(1 - drop_rate)
# e.g., 95% confidence for 1% drop: log(0.05) / log(0.99) = 299 attempts
```

### Rarity Tier Distribution

Standard rarity distribution:

| Rarity | Drop Rate | Typical Range |
|--------|-----------|---------------|
| Common | 50-60% | White/grey items |
| Uncommon | 20-30% | Green items |
| Rare | 8-15% | Blue items |
| Epic | 2-5% | Purple items |
| Legendary | 0.5-1% | Orange/gold items |
| Mythic | 0.01-0.1% | Red/prismatic items |

---

## Difficulty Scaling

### Level-Based Difficulty

```python
def enemy_power(base_power, enemy_level, player_level):
    level_diff = enemy_level - player_level
    return base_power * (1.05 ** level_diff)
```

### Adaptive Difficulty (Rubber-Banding)

```python
def adaptive_multiplier(deaths_recent, kills_recent, window=10):
    ratio = kills_recent / max(1, deaths_recent)
    if ratio > 3:  # player stomping
        return 1.1  # slightly harder
    elif ratio < 0.5:  # player struggling
        return 0.9  # slightly easier
    return 1.0
```

**Caution**: Keep adjustments subtle (5-10% range). Large swings feel unfair.

### Multi-Player Scaling

```python
def group_scaling(base_hp, player_count, scaling_factor=0.75):
    return base_hp * (1 + scaling_factor * (player_count - 1))
```

**scaling_factor guide**:
- 0.5: Each additional player adds 50% HP (casual-friendly)
- 0.75: Standard scaling (encourages grouping)
- 1.0: Linear scaling (each player adds full HP equivalent)

---

## Quick Reference Card

| Need | Formula | Key Parameters |
|------|---------|----------------|
| Stat growth | `base + growth * level` | base, growth |
| Percentage scaling | `base * (rate ^ level)` | base, rate |
| Soft cap | `cap - (cap - base) * e^(-rate * level)` | cap, rate |
| Armor mitigation | `armor / (armor + K)` | K (100 typical) |
| DPS | `damage * speed * (1 + crit% * (crit_mult - 1))` | damage, speed, crit |
| TTK | `EHP / DPS` | — |
| XP per level | `base * level^exponent` | base, exponent |
| Expected drops | `1 / drop_rate` | drop_rate |
| Inflation | `(end - start) / start` | monthly |
