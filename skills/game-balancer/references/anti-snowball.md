# Preventing Snowball Mechanics

Strategies and techniques for preventing runaway advantages in Infinite Voyage.
When a player or system gets ahead, these patterns prevent the advantage from
compounding into an unbeatable lead.

---

## What Is Snowballing?

A snowball occurs when early success creates compounding advantages:

```
Early advantage → More resources → Bigger advantage → Even more resources → ...
```

**Why it's critical to prevent**:
- Losing players disengage ("game is already over")
- Outcomes feel predetermined, reducing agency
- Multiplayer matches become unfun for the losing side
- PvE progression becomes trivially easy once ahead of the curve

---

## Detection Methods

### Quantitative Signals

```python
def detect_snowball(match_data, early_cutoff=0.25):
    """
    Check if early-game advantage predicts final outcome.

    early_cutoff: fraction of match time considered "early" (25%)
    """
    early_leader_wins = 0
    total_matches = len(match_data)

    for match in match_data:
        early_end = int(len(match['snapshots']) * early_cutoff)
        early_leader = match['snapshots'][early_end]['leading_player']
        final_winner = match['winner']

        if early_leader == final_winner:
            early_leader_wins += 1

    prediction_rate = early_leader_wins / total_matches
    return {
        'early_prediction_rate': prediction_rate,
        'snowball_severity': 'NONE' if prediction_rate < 0.6
                            else 'MILD' if prediction_rate < 0.7
                            else 'MODERATE' if prediction_rate < 0.8
                            else 'SEVERE'
    }
```

| Metric | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| Early-leader win rate | < 60% | 60-75% | > 75% |
| Comeback frequency | > 30% of matches | 15-30% | < 15% |
| Lead growth rate | Linear or decelerating | Constant acceleration | Exponential |
| Match duration variance | Moderate (games play out) | Low (stomps end fast) | Very low |

### Qualitative Signals

- Players say "GG" in the first 5 minutes
- Losing team/player stops trying
- Matches rarely go to the final phase
- "Feeding" or "throwing" terminology emerges (players giving up)

---

## Anti-Snowball Techniques

### 1. Catch-Up Mechanics

Give losing players bonus resources or abilities to close the gap.

```python
def catch_up_bonus(player_score, leader_score, max_bonus=0.25):
    """
    Scale bonus based on how far behind the player is.
    Returns a multiplier (1.0 = no bonus, 1.25 = max bonus).
    """
    if player_score >= leader_score:
        return 1.0
    gap_ratio = (leader_score - player_score) / max(1, leader_score)
    bonus = min(gap_ratio, max_bonus)
    return 1.0 + bonus
```

**Examples**:
- Mario Kart: Better items for players in lower positions
- Rubber-banding in racing games
- Bonus XP for players below average level

**Design rules**:
- Cap the bonus (never more than 25% boost)
- Make it feel earned ("underdog bonus") not like a handout
- Scale smoothly — don't create a cliff where trailing is suddenly better

---

### 2. Diminishing Returns on Advantage

Make each unit of advantage less impactful than the previous one.

```python
def diminishing_advantage(raw_advantage, soft_cap, hard_cap):
    """
    Apply diminishing returns to an advantage metric.

    Below soft_cap: full value
    Between soft_cap and hard_cap: reduced scaling
    Above hard_cap: no additional benefit
    """
    if raw_advantage <= soft_cap:
        return raw_advantage
    elif raw_advantage <= hard_cap:
        excess = raw_advantage - soft_cap
        diminished = excess * 0.5  # 50% efficiency above soft cap
        return soft_cap + diminished
    else:
        return soft_cap + (hard_cap - soft_cap) * 0.5  # capped
```

**Examples**:
- XP from kills decreases as level gap grows
- Gold income soft caps at a threshold
- Stats have diminishing returns above a soft cap
- Territory control benefits plateau after controlling 60%

---

### 3. Negative Feedback Loops

Systems that naturally resist runaway states.

| Feedback Loop | How It Works |
|---------------|-------------|
| **Threat scaling** | Stronger players attract harder enemies/challenges |
| **Resource scarcity** | Dominant player's resources become harder to acquire |
| **Attention tax** | More territory/units = more to defend and manage |
| **Bounty system** | Leading player becomes a higher-value target |
| **Upkeep costs** | Maintaining a large empire/army costs proportionally more |

**Key principle**: The cost of maintaining an advantage should scale faster than
the benefit of having it.

```python
def upkeep_cost(units_owned, base_cost=10, scaling=1.5):
    """Upkeep grows super-linearly with units owned."""
    return base_cost * (units_owned ** scaling)

# 5 units: 10 * 5^1.5 = 112 gold/turn
# 10 units: 10 * 10^1.5 = 316 gold/turn
# 20 units: 10 * 20^1.5 = 894 gold/turn
```

---

### 4. Comeback Moments

Design specific mechanics or events that create comeback opportunities.

**Structural comebacks**:
- Boss that spawns when one side has a large lead
- Map objectives that appear mid-game and reset advantages
- Sudden-death phase where all previous advantages are reduced
- Item/ability that's only available to the losing side

**Economy comebacks**:
- High-risk/high-reward investments only valuable when behind
- Trading mechanics that transfer wealth from leader to followers
- "Desperation" abilities that are stronger at low HP/resources

**Progression comebacks**:
- Rested XP (offline bonus) for players who log in less
- Weekly reset mechanics that partially equalize
- Season-based resets where everyone starts fresh periodically

---

### 5. Advantage Decay

Advantages naturally diminish over time if not actively maintained.

```python
def decay_advantage(current_advantage, decay_rate=0.05, min_advantage=0):
    """Reduce advantage by decay_rate per time period."""
    new_advantage = current_advantage * (1 - decay_rate)
    return max(min_advantage, new_advantage)
```

**Examples**:
- Killstreaks decay after 60 seconds without a kill
- Resource stockpiles slowly degrade (food spoils, equipment degrades)
- Buff durations are fixed regardless of how far ahead you are
- Territorial control requires upkeep or reverts to neutral

---

### 6. Bounded Advantage Windows

Limit how long an advantage can persist.

| Mechanic | Window | Effect |
|----------|--------|--------|
| Buffs | 30-120 seconds | Power spike is temporary |
| Killstreak bonuses | 3-5 kills, then reset | Advantage caps and resets |
| Economic boosts | Per-session | Resets on logout or new session |
| Map control | Until contested | Must be actively defended |

---

## System-Specific Anti-Snowball Design

### Combat

- **Level scaling**: Enemies scale with player level so overleveling doesn't trivialize content
- **Armor soft cap**: Stacking armor has diminishing returns past 60% mitigation
- **Damage cap**: No single hit should deal more than 70% of a player's max HP
- **Respawn advantage**: Respawning player gets brief invulnerability/buff

### Economy

- **Income cap**: Daily gold earning caps at 150% of the intended daily earning rate
- **Tax brackets**: Higher-wealth players pay proportionally more in transaction fees
- **Inflation controls**: Vendor prices scale with server-wide average wealth
- **Welfare floor**: Minimum earning guarantee regardless of player skill/level

### Progression

- **XP curve**: Later levels require more XP, naturally slowing leaders
- **Catch-up XP**: Lower-level players get bonus XP from group content
- **Content gating**: Even over-leveled players must complete quests to progress
- **Horizontal progression**: End-game power comes from variety, not vertical power

---

## Balance Verification

After implementing anti-snowball mechanics, verify with simulation:

```python
def verify_anti_snowball(matches, early_cutoff=0.25):
    """
    Verify that comebacks are possible and matches feel competitive.
    """
    results = detect_snowball(matches, early_cutoff)

    checks = {
        'early_prediction_rate': results['early_prediction_rate'] < 0.65,
        'average_match_closeness': np.mean([m['score_diff'] for m in matches]) < 0.2,
        'comeback_rate': sum(1 for m in matches if m['comeback']) / len(matches) > 0.25,
        'match_duration_cv': np.std([m['duration'] for m in matches]) / np.mean([m['duration'] for m in matches]) > 0.15,
    }

    return {
        'all_passed': all(checks.values()),
        'details': checks
    }
```

### Success Criteria

| Metric | Target |
|--------|--------|
| Early-leader win rate | < 65% |
| Comeback rate | > 25% of matches |
| Average score closeness | Within 20% at match end |
| Match duration variance | CV > 0.15 (not all stomps or all long) |
| Player satisfaction (survey) | > 70% feel matches are fair |

---

## Quick Reference: Technique Selection

| Problem | Best Technique |
|---------|---------------|
| One player runs away with the game early | Catch-up mechanics + advantage decay |
| Rich get richer (economy) | Diminishing returns + tax brackets |
| Over-leveled player trivializes content | Level scaling + content gating |
| Dominant strategy emerges | Negative feedback loops + bounded windows |
| Multiplayer blowouts | Comeback moments + bounty system |
| Progression gap between old and new players | Catch-up XP + season resets |
