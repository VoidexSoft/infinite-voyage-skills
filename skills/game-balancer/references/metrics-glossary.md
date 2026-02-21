# Game Balance Metrics Glossary

Definitions and formulas for all standard balance metrics.
Organized by domain.

---

## Combat Metrics

### DPS (Damage Per Second)

**Definition**: Average damage output per second of sustained combat.

```python
dps = base_damage * attacks_per_second * hit_chance * (1 + crit_chance * (crit_multiplier - 1))
```

**Variants**:
- **Burst DPS**: Peak damage over a short window (1-3 seconds), including cooldowns
- **Sustained DPS**: Average damage over a full rotation (30+ seconds)
- **Effective DPS**: DPS accounting for target mitigation and downtime

**Healthy ranges** (per content tier):
| Content | Player DPS | Enemy DPS |
|---------|-----------|-----------|
| Early game | 20-50 | 10-25 |
| Mid game | 80-200 | 40-100 |
| Late game | 300-800 | 150-400 |

---

### TTK (Time to Kill)

**Definition**: Seconds required for one entity to defeat another.

```python
ttk = target_ehp / attacker_dps
```

**Why it matters**: TTK determines combat pacing. Too low = fights feel instant and
unreactive. Too high = fights feel tedious.

**Target TTK ranges**:
| Encounter Type | Target TTK | Feel |
|----------------|-----------|------|
| Trash mobs | 2-4s | Quick, satisfying |
| Standard enemies | 5-10s | Requires engagement |
| Elite enemies | 15-30s | Mini-challenge |
| Mini-bosses | 60-120s | Demanding fight |
| Bosses | 180-600s | Epic encounter |
| Raid bosses | 600-900s | Endurance test |

---

### EHP (Effective Hit Points)

**Definition**: Total damage a target can absorb before dying, accounting for all
mitigation.

```python
# With armor (percentage reduction)
ehp = hp / (1 - mitigation_percent)
# or equivalently:
ehp = hp * (1 + armor / armor_constant)

# With dodge
ehp_with_dodge = ehp / (1 - dodge_chance)

# With healing
ehp_with_healing = ehp + (hps * expected_fight_duration)
```

**Use**: Comparing tankiness across builds. A character with 500 HP and 50%
mitigation has the same EHP (1000) as one with 1000 HP and 0% mitigation.

---

### HPS (Healing Per Second)

**Definition**: Average health restored per second.

```python
hps = heal_amount / cast_time
effective_hps = hps * (1 - overheal_rate)
```

**Balance target**: Healing should sustain against 60-80% of incoming damage,
requiring skill-based mitigation (dodging, blocking) for the rest.

---

### TTD (Time to Die)

**Definition**: How long the player survives under sustained enemy damage.

```python
ttd = player_ehp / enemy_dps
```

**Minimum TTD**: Players should always have at least 3-5 seconds to react before
dying. TTD below 2 seconds feels unfair.

---

### Burst Window

**Definition**: The maximum damage achievable in a short time frame by spending
all cooldowns.

```python
burst = sum(ability['damage'] for ability in abilities if ability['cooldown'] == 0)
```

**Balance concern**: If burst > target_hp, one-shots are possible. Burst should
be 30-60% of a typical target's HP to create pressure without instant kills.

---

## Economy Metrics

### GPH (Gold Per Hour)

**Definition**: Average currency earned per hour of active play.

```python
gph = (kills_per_hour * gold_per_kill) + (quests_per_hour * gold_per_quest) + vendor_sales_per_hour
```

**Use**: Benchmarking earning rates across content. All content tiers should offer
competitive GPH to prevent funneling into one activity.

---

### Sink-Faucet Ratio

**Definition**: Ratio of currency removed from the economy to currency created.

```python
sf_ratio = total_currency_sunk / total_currency_created
```

| Ratio | Interpretation |
|-------|---------------|
| < 0.5 | Heavy inflation — currency accumulating too fast |
| 0.7-0.9 | Healthy — slight net positive for players |
| 1.0 | Perfect equilibrium (rare and not necessary) |
| > 1.0 | Deflation — players losing currency over time |

---

### Purchasing Power Index

**Definition**: How much content a unit of currency can buy, tracked over time.

```python
ppi = baseline_item_cost / current_item_cost
```

**Healthy**: PPI stays between 0.8 and 1.2 over any 3-month period. If PPI drops
below 0.5, players feel their earnings are worthless.

---

### Velocity of Currency

**Definition**: How many times currency changes hands in a given period.

```python
velocity = total_transactions / total_currency_supply
```

**High velocity**: Currency flows freely (active economy, lots of trading).
**Low velocity**: Currency pools in player inventories (needs more sinks or
trading incentives).

---

## Progression Metrics

### XP/Hour

**Definition**: Experience earned per hour of active play.

**Balance target**: Should produce level-ups at the target pace (see common-formulas.md
for XP curve formulas). If XP/hour varies by more than 30% across activities, players
will min-max the highest source.

---

### Time to Cap

**Definition**: Total hours from level 1 to maximum level.

| Game Type | Typical Time to Cap |
|-----------|-------------------|
| Mobile/casual | 20-40 hours |
| Standard RPG | 60-120 hours |
| MMO | 100-300 hours |
| Hardcore/endgame | 200-500 hours |

---

### Power Curve

**Definition**: The ratio of player power at level N to player power at level 1.

```python
power_ratio = player_power_at_level_n / player_power_at_level_1
```

**Healthy growth**: Power ratio of 5-10x from level 1 to cap. Above 20x creates
balance nightmares (high-level players trivialize low-level content).

---

### Content Consumption Rate

**Definition**: How fast players progress through available content.

```python
consumption_rate = content_hours_played / content_hours_available
```

**Target**: Players should consume content at 70-80% of creation rate. If they
consume faster, you're running out of content. If slower, content is too grindy.

---

## Fairness Metrics

### Gini Coefficient

**Definition**: Measure of inequality in a distribution. 0 = perfectly equal,
1 = perfectly unequal.

```python
def gini(values):
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    cumulative = sum((2 * i - n - 1) * val for i, val in enumerate(sorted_vals, 1))
    return cumulative / (n * sum(sorted_vals))
```

**Use**: Measuring power distribution across builds, wealth distribution across
players, or win rate distribution across strategies.

| Gini | Interpretation |
|------|---------------|
| 0.0-0.15 | Very equal (maybe too homogeneous) |
| 0.15-0.30 | Healthy variety with balance |
| 0.30-0.45 | Noticeable inequality (monitor closely) |
| 0.45+ | Dominant strategies/builds exist |

---

### Win Rate Spread

**Definition**: The difference between the highest and lowest win rates across
all viable strategies/builds.

```python
spread = max(win_rates) - min(win_rates)
```

| Spread | Interpretation |
|--------|---------------|
| < 5% | Excellent balance |
| 5-10% | Good balance |
| 10-20% | Needs attention |
| > 20% | Dominant strategy exists |

---

### Coefficient of Variation (CV)

**Definition**: Standard deviation as a percentage of the mean. Measures relative
variability.

```python
cv = std_deviation / mean
```

**Use**: Comparing variability across metrics with different scales. A TTK with
CV > 0.5 means combat outcomes are too random.

---

## Engagement Metrics

### Session Length

**Target**: 20-45 minutes average session. Longer sessions indicate engagement
but risk fatigue. Shorter sessions may indicate friction.

### Retention (Day N)

| Day | Good | Average | Concerning |
|-----|------|---------|-----------|
| Day 1 | > 40% | 25-40% | < 25% |
| Day 7 | > 20% | 10-20% | < 10% |
| Day 30 | > 10% | 5-10% | < 5% |

### Fun Ratio

**Definition**: Percentage of session time spent in "fun" activities vs. mandatory
non-fun activities (loading, inventory management, travel).

**Target**: > 80% fun ratio. If players spend more than 20% of their time on
non-gameplay activities, UX improvements are needed.
