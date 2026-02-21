# Balancing Methodology

A step-by-step process for balancing game systems. Follow this
workflow whenever tuning stats, abilities, items, enemies, or economy values.

---

## The 6-Step Balance Process

### Step 1: Define the Balance Target

Before adjusting any numbers, answer these questions:

| Question | Example Answer |
|----------|---------------|
| What system are we balancing? | Melee combat damage vs. armor |
| What's the success metric? | TTK between 3-5 seconds for equal-level fights |
| What's the acceptable variance? | ±10% from target TTK |
| What constraints exist? | Must preserve "tanky warrior" fantasy |
| What's the player fantasy? | Hits should feel impactful but not instant-kill |

**Anti-pattern**: Balancing without a clear target leads to endless tweaking with
no convergence. Always define "done" before starting.

### Step 2: Gather Current Data

Collect all relevant parameters from the GDD and existing data:

```
1. Read the relevant GDD section for design intent
2. Extract current parameter values (stat tables, formulas, curves)
3. Identify related systems that feed into or depend on this one
4. Check if previous balance passes exist (learn from past iterations)
5. Note player feedback or playtest observations
```

**Key principle**: Never balance in isolation. A damage buff is also a TTK nerf,
an economy inflation, and a difficulty reduction.

### Step 3: Build the Mathematical Model

Create a simplified model that captures the essential behavior:

```python
# Good model: captures the key relationship
damage = base_damage * (1 + power / 100)
mitigated = damage * (100 / (100 + armor))
ttk = target_hp / (mitigated / attack_speed)

# Bad model: too many variables, impossible to tune
damage = base * power_scaling * weapon_modifier * buff_stack *
         crit_chance * crit_multiplier * elemental_bonus * ...
```

**Guidelines**:
- Start with the simplest model that produces meaningful results
- Add complexity only when the simple model fails to predict observed behavior
- Document every assumption ("assumes no crits, no buffs, no positional bonus")
- Use Python scripts in `scripts/` for computation

### Step 4: Run Simulations

Choose the right simulation approach:

| Approach | When to Use | Script |
|----------|-------------|--------|
| Analytical (closed-form) | Simple systems with no randomness | Manual calculation |
| Monte Carlo | Systems with RNG (crit, dodge, proc) | `scripts/combat_sim.py` |
| Sweep | Testing parameter ranges | `scripts/optimizer.py` |
| Time-series | Economy, progression over time | `scripts/economy_sim.py` |
| Distribution check | Loot tables, drop rates | `scripts/loot_sim.py` |

**Minimum run count**: 10,000 iterations for Monte Carlo to get stable results.
Use 100,000 for high-variance systems (loot with rare drops).

### Step 5: Analyze and Recommend

Present results in this standard format:

```markdown
## Balance Report: [System Name]

### Summary
[One sentence verdict: balanced, needs tuning, or fundamentally broken]

### Key Metrics
| Metric | Current | Target | Range | Status |
|--------|---------|--------|-------|--------|
| [name] | [value] | [goal] | [min-max] | [pass/fail] |

### Distribution Analysis
[Histogram or box plot of key metric distribution]
[Note: mean, median, std dev, outliers]

### Recommendations
1. Change [parameter] from [old] to [new] — expected effect: [what changes]
2. Change [parameter] from [old] to [new] — expected effect: [what changes]

### Side Effects
- Changing X will also affect [related system] because [reason]
- Edge case: [scenario] could become [problem] — monitor after change

### Confidence Level
[High/Medium/Low] — [reason for confidence level]
```

### Step 6: Iterate and Verify

After applying changes:

1. Re-run the same simulation with new parameters
2. Compare before/after distributions side-by-side
3. Check for unintended effects on connected systems
4. Produce a diff report: what changed, what improved, what regressed
5. If metrics are within target range: **done**. If not: return to Step 5.

**Convergence rule**: If 3 iterations haven't converged, the model may be wrong.
Re-examine assumptions in Step 3 before continuing.

---

## Balance Principles

### 1. Balance for the Median, Tune for the Extremes

Design for the typical player experience first. Then check:
- Does the optimal player break it? (check ceiling)
- Does the struggling player hate it? (check floor)
- Adjust floor/ceiling without destroying the median experience

### 2. Relative Balance > Absolute Balance

Players don't notice that sword damage is exactly 100. They notice that:
- Sword does 2x more damage than mace (feels unfair)
- Sword takes 2x longer to kill than expected (feels weak)
- All weapons kill in roughly the same time (feels balanced)

Focus on **ratios and comparisons**, not absolute numbers.

### 3. Perception Matters More Than Math

A mechanic that is mathematically balanced but *feels* unfair will generate
complaints. Common perception gaps:

| Math Says | Player Feels | Why |
|-----------|-------------|-----|
| 50% chance to crit | "I never crit" | Negative outcomes are remembered more |
| Equal DPS, different burst | "Burst class is OP" | Burst damage feels more impactful |
| 5% stat difference | "Completely unplayable" | Context-dependent (PvP vs PvE) |

Address perception through:
- Pseudo-random distribution (prevent long streaks of bad luck)
- Visual/audio feedback that reinforces fairness
- Transparent formulas (show damage calculations)

### 4. The 80/20 Rule of Balance

80% of balance problems come from 20% of parameters. Identify and focus on the
**critical few**:

- **Combat**: Base damage, armor formula, attack speed, HP scaling
- **Economy**: Gold per hour, top 3 sinks, top 3 faucets
- **Progression**: XP curve, level-up rewards, content gating thresholds
- **Loot**: Drop rate for highest rarity, expected value per hour

### 5. Never Balance by Nerfing Fun

If something feels great but is too strong:
- First try: buff the alternatives to match
- Second try: nerf the mechanic's efficiency, not its feel
- Last resort: direct nerf (with clear communication to players)

---

## Common Pitfalls

| Pitfall | Description | Prevention |
|---------|-------------|------------|
| Balancing to spreadsheet | Numbers look good on paper but play poorly | Always playtest after mathematical balance |
| Chasing outliers | Nerfing based on top 1% of players | Balance for median, cap for extremes |
| Oscillating nerfs | Buff A, nerf B, buff A again | Make smaller changes (5-10%), wait for data |
| Ignoring system coupling | Changing one stat breaks three other systems | Map dependencies before changing anything |
| Premature optimization | Tuning numbers before mechanics are finalized | Lock mechanics first, then tune numbers |

---

## Balance Documentation Template

For every balance change, record:

```markdown
## Balance Change: [Date] — [System]

**Author**: [name]
**Trigger**: [what prompted this change]
**Parameters changed**:
  - [param]: [old] → [new] (reason)
**Simulation results**: [link to report]
**Side effects checked**: [list of connected systems verified]
**Status**: [applied / reverted / monitoring]
```

Keep a running log so future balance passes can learn from past decisions.
