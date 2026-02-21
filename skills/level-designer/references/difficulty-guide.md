# Difficulty Tuning Guide

Comprehensive reference for tuning encounter difficulty across all tiers.
Use this guide when setting enemy stats, designing adaptive difficulty, and verifying that
encounters feel appropriate for their intended audience.

---

## Difficulty Tiers

Your game can support five difficulty tiers. Each tier targets a different player profile
and adjusts enemy stats, AI behavior, and resource availability.

### Tier Definitions

| Tier | Target Player | Core Philosophy |
|------|--------------|-----------------|
| **Story** | Wants narrative, minimal combat friction | Combat is a formality; players should never be stuck |
| **Easy** | Casual or new to genre | Forgiving mistakes; learning-friendly pacing |
| **Normal** | Experienced with action RPGs | Fair challenge; rewards mastery without punishing mistakes harshly |
| **Hard** | Seeking significant challenge | Demands build optimization and mechanical skill |
| **Nightmare** | Mastery-oriented, willing to retry | Punishing; expects near-perfect execution and deep system knowledge |

### Player Skill Assumptions by Tier

| Skill Dimension | Story | Easy | Normal | Hard | Nightmare |
|----------------|-------|------|--------|------|-----------|
| Dodge success rate | N/A | 30% | 60% | 80% | 95% |
| Optimal DPS uptime | N/A | 20% | 50% | 75% | 90% |
| Resource management | Unlimited | Generous | Moderate | Tight | Minimal |
| Build optimization | None | Minimal | Some | Required | Mandatory |
| Mechanic awareness | Minimal | Basic | Full | Full + timing | Perfect |

---

## Stat Multipliers

All enemy stats are authored at Normal difficulty. Other tiers apply multipliers.

### Core Stat Multipliers

| Stat | Story | Easy | Normal | Hard | Nightmare |
|------|-------|------|--------|------|-----------|
| Enemy HP | 0.50x | 0.75x | 1.00x | 1.40x | 2.00x |
| Enemy Damage | 0.40x | 0.70x | 1.00x | 1.35x | 1.80x |
| Enemy Armor | 0.50x | 0.75x | 1.00x | 1.25x | 1.60x |
| Enemy Count | 0.60x | 0.80x | 1.00x | 1.00x | 1.20x |
| Enemy Speed | 0.80x | 0.90x | 1.00x | 1.10x | 1.15x |
| Heal/Support Rate | 0.30x | 0.60x | 1.00x | 1.30x | 1.50x |

### Behavioral Multipliers

| Behavior | Story | Easy | Normal | Hard | Nightmare |
|----------|-------|------|--------|------|-----------|
| AI aggression | Passive | Cautious | Standard | Aggressive | Relentless |
| Reaction time (ms) | 2000 | 1200 | 800 | 500 | 300 |
| Flanking frequency | Never | Rare | Sometimes | Often | Always |
| Ability usage rate | 0.3x | 0.6x | 1.0x | 1.3x | 1.5x |
| Combo chain length | 1 | 1-2 | 2-3 | 3-4 | 4-5 |

### Player Resource Multipliers

| Resource | Story | Easy | Normal | Hard | Nightmare |
|----------|-------|------|--------|------|-----------|
| Healing item drops | 2.00x | 1.50x | 1.00x | 0.70x | 0.50x |
| Checkpoint frequency | Every encounter | Every 2 encounters | Every 3 encounters | Every 4 encounters | Boss only |
| Death penalty | None | Minimal (keep items) | Standard | Lose consumables | Lose consumables + gold |
| Cooldown reduction | 0.50x | 0.75x | 1.00x | 1.15x | 1.30x |

---

## Scaling Formulas

### Base Enemy Stat Formula

```
EffectiveStat = BaseStat * LevelScaling * TierMultiplier * ZoneModifier
```

Where:
- `BaseStat` is the authored stat at level 1, Normal difficulty
- `LevelScaling = 1 + (EnemyLevel - 1) * 0.08` (8% growth per level)
- `TierMultiplier` is from the multiplier tables above
- `ZoneModifier` is a per-zone adjustment (typically 0.9 to 1.1)

### Damage Curve

Player incoming damage per second (DPS) should follow this curve relative to player EHP:

| Player Level | Normal TTD (seconds) | Hard TTD (seconds) | Nightmare TTD (seconds) |
|-------------|---------------------|--------------------|-----------------------|
| 1-5 | 8-12 | 5-8 | 3-5 |
| 6-15 | 6-10 | 4-6 | 2-4 |
| 16-25 | 5-8 | 3-5 | 2-3 |
| 26-35 | 4-7 | 2-4 | 1.5-2.5 |
| 36+ | 3-6 | 2-3 | 1-2 |

TTD = Time-to-Death (how long the player survives under sustained focus fire with no healing or dodging).

### Health Curve per Tier

Enemy HP should feel proportional to player DPS output. Target kill times for a standard enemy:

| Enemy Role | Story | Easy | Normal | Hard | Nightmare |
|-----------|-------|------|--------|------|-----------|
| Minion | 1-2 sec | 2-3 sec | 3-5 sec | 5-8 sec | 8-12 sec |
| Standard | 3-5 sec | 5-8 sec | 8-12 sec | 12-18 sec | 18-25 sec |
| Elite | 8-12 sec | 15-20 sec | 25-35 sec | 40-55 sec | 60-80 sec |
| Miniboss | 20-30 sec | 45-60 sec | 90-120 sec | 150-200 sec | 240-300 sec |
| Boss | 60-90 sec | 120-180 sec | 300-480 sec | 480-600 sec | 600-900 sec |

---

## Adaptive Difficulty

Your game can support optional adaptive difficulty that adjusts within a tier based on
player performance. This system operates silently and never changes the displayed tier.

### Performance Metrics Tracked

| Metric | What It Measures | Weight |
|--------|-----------------|--------|
| Death frequency | Deaths per hour of gameplay | 0.30 |
| Attempt count | Retries on the same encounter | 0.25 |
| Health on victory | Average HP remaining after encounters | 0.20 |
| Time-to-complete | Encounter duration vs. target | 0.15 |
| Consumable usage | Healing items used per encounter | 0.10 |

### Adaptive Adjustment Range

The adaptive system applies a hidden modifier between 0.85x and 1.15x on top of the tier multiplier.
It never crosses tier boundaries.

```
AdaptiveModifier = clamp(1.0 + (PerformanceScore - 0.5) * 0.30, 0.85, 1.15)
```

Where `PerformanceScore` is a weighted average of the metrics above, normalized to 0.0 (struggling) to 1.0 (dominating).

### Adjustment Rules

- Modifier adjusts after every 3 encounters (not mid-encounter)
- Maximum shift per adjustment: 0.05 in either direction
- Resets to 1.0 on tier change by the player
- Disabled entirely on Nightmare difficulty
- Never affects boss encounters (bosses are always at base tier stats)

### Adjustment Triggers

| Condition | Adjustment |
|-----------|------------|
| 3+ deaths in last 5 encounters | -0.05 modifier (easier) |
| 0 deaths and >70% HP remaining across 5 encounters | +0.05 modifier (harder) |
| Player uses 0 consumables across 3 encounters | +0.03 modifier |
| Player uses 3+ consumables per encounter for 3 encounters | -0.03 modifier |
| Encounter takes 2x target duration | -0.05 modifier |

---

## Difficulty Design Guidelines

### Encounter Design Per Tier

**Story Mode:**
- Enemies telegraph all attacks with exaggerated animations (2+ second tells)
- Auto-aim or generous hitboxes on player attacks
- Enemies attack one at a time when possible
- Instant respawn with no resource loss
- Skip-combat option available for non-boss encounters

**Easy Mode:**
- Clear telegraphs with generous dodge windows (1.5+ seconds)
- Enemies rarely combo or flank
- Abundant healing drops from enemies
- Checkpoints before every significant encounter

**Normal Mode:**
- Standard telegraphs with fair dodge windows (0.8-1.2 seconds)
- Enemies use full ability kits but at moderate frequency
- Healing balanced around smart resource usage
- Standard checkpoint spacing

**Hard Mode:**
- Tighter telegraphs, shorter windows (0.5-0.8 seconds)
- Enemies flank, combo, and use abilities aggressively
- Healing is scarce; player must optimize builds for sustain
- Reduced checkpoints; player must plan around save points

**Nightmare Mode:**
- Minimal telegraphs, expert-only dodge windows (0.3-0.5 seconds)
- Enemies coordinate, chain combos, and exploit player cooldowns
- Healing is extremely limited; every consumable is precious
- Checkpoints only at zone entrances and before bosses
- Additional enemy mechanics not present in lower tiers

### Common Tuning Mistakes

| Mistake | Symptom | Solution |
|---------|---------|----------|
| HP sponge | Enemies feel tedious, not threatening | Reduce HP by 20-30%, increase damage by 10-15% |
| Glass cannon enemies | Fights end too fast, no engagement | Increase HP by 30%, add defensive behaviors |
| Flat difficulty | Every fight feels the same | Vary enemy composition and introduce escalation |
| Spike without teach | Player dies to mechanic they have never seen | Add a low-stakes introduction encounter first |
| Tier collapse | Easy and Normal feel identical | Verify multiplier spread is at least 25% between adjacent tiers |

---

## Verification Checklist

Before finalizing difficulty tuning:

- [ ] Playtest at Story, Normal, and Nightmare with appropriate skill levels
- [ ] Verify TTD values match the table above within 20% tolerance
- [ ] Confirm kill times for each enemy role match the health curve table
- [ ] Test adaptive difficulty triggers across 10+ encounter sequences
- [ ] Verify boss encounters are exempt from adaptive modifiers
- [ ] Check that tier multipliers produce distinct feel (not just stat differences)
- [ ] Validate that behavioral changes (aggression, flanking) work at each tier
- [ ] Ensure no soft-locks exist at any difficulty tier

---

## Quick Reference Card

```
Story:   0.5x HP | 0.4x DMG | Passive AI    | Generous heals | No death penalty
Easy:    0.75x   | 0.7x     | Cautious AI   | Extra heals    | Keep items
Normal:  1.0x    | 1.0x     | Standard AI   | Balanced       | Standard
Hard:    1.4x    | 1.35x    | Aggressive AI | Scarce heals   | Lose consumables
Night:   2.0x    | 1.8x     | Relentless AI | Minimal heals  | Lose consumables + gold
```
