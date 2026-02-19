# Economy Anti-Patterns

A catalog of common game economy design mistakes, how to detect them early,
and how to fix them once they have taken root. Written for Infinite Voyage but
applicable to any game with a virtual economy.

---

## Anti-Pattern 1: Hyperinflation Spiral

### Description

Currency enters the economy faster than it leaves. Over weeks and months, prices
rise, savings become worthless, and new players face an impossible gap between
what they earn and what things cost.

### Root Causes

- Faucets (currency sources) grow with player count but sinks do not scale.
- New content adds earning opportunities without corresponding spending sinks.
- Duplication exploits or botting inject unearned currency.
- High-level players farm currency at rates far exceeding intended earning curves.

### Detection Methods

| Signal | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| Monthly currency supply growth | < 5% | 5-15% | > 15% |
| Average player balance trend | Stable or slow rise | Doubling every 2-3 months | Doubling monthly |
| Player-to-player trade prices | Stable with minor fluctuation | 20%+ increase per month | Exponential price growth |
| New player purchasing power | Can afford starter gear easily | Starter gear costs 2+ days of play | Starter gear is effectively unaffordable |

```python
def detect_inflation(economy_snapshots, window_days=30):
    """Compare currency supply across time windows."""
    recent = economy_snapshots[-1]["total_currency_supply"]
    past = economy_snapshots[-window_days]["total_currency_supply"]
    growth_rate = (recent - past) / past

    if growth_rate > 0.15:
        return "CRITICAL: Hyperinflation detected"
    elif growth_rate > 0.05:
        return "WARNING: Inflation above target"
    return "HEALTHY"
```

### Fixes

1. **Immediate**: Introduce emergency gold sinks (limited-time cosmetics, repair cost events).
2. **Short-term**: Audit all faucets, reduce the top 2-3 currency sources by 15-25%.
3. **Long-term**: Implement automatic sink scaling -- as total server currency rises, sink costs increase proportionally.
4. **Structural**: Add auction house taxes, equipment degradation, and crafting failure costs as permanent drains.

---

## Anti-Pattern 2: Dead Economy

### Description

Players accumulate currency with nothing meaningful to spend it on. Gold piles up,
and the currency becomes psychologically worthless. Players stop caring about
earning because there is no spending motivation.

### Root Causes

- Spending sinks are too few or too cheap relative to earning rates.
- Best-in-slot gear is acquired through drops only, making gold irrelevant for progression.
- Crafting system produces items worse than dropped gear.
- No recurring costs (repair, consumables, travel fees).

### Detection Methods

| Signal | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| Median player gold balance | 2-5x daily earning | 10-20x daily earning | 50x+ daily earning |
| Daily gold spent / daily gold earned | 0.6 - 0.9 | 0.3 - 0.6 | < 0.3 |
| Vendor usage rate | 60%+ of players use vendors daily | 30-60% | < 30% |
| Player complaints about "useless gold" | Rare | Occasional | Frequent |

### Fixes

1. **Add aspirational sinks**: Expensive cosmetics (mounts, housing, titles) priced at 2-4 weeks of earning.
2. **Add recurring sinks**: Equipment repair, consumable costs, respec fees, travel costs.
3. **Make crafting competitive**: Crafted gear should have unique bonuses that dropped gear lacks.
4. **Gold-gated access**: Some activities cost gold to enter (high-tier dungeons, arena seasons).
5. **Player-to-player economy**: Enable trading so gold flows between players rather than pooling.

---

## Anti-Pattern 3: Pay-to-Win Trap

### Description

Real-money purchases provide gameplay advantages, creating a two-tier player
base. Paying players dominate, free players feel powerless, and the community
fractures.

### Root Causes

- Premium currency can purchase stat-boosting items or gear.
- "Time saver" packs that skip meaningful progression.
- Gacha or loot boxes that award powerful random items.
- Premium-exclusive content that provides mechanical advantages.

### Detection Methods

| Signal | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| Power gap: top spender vs. top free player | < 5% | 5-20% | > 20% |
| PvP win rate correlation with spending | No correlation | Weak correlation (r < 0.3) | Strong correlation (r > 0.5) |
| Community sentiment about fairness | Positive | Mixed | Hostile |
| Free player retention at day 30 | > 25% | 15-25% | < 15% |

### Fixes

1. **Hard rule**: Premium currency buys cosmetics and convenience only. No exceptions.
2. **Audit all purchasable items**: Remove or reclassify anything that affects combat stats.
3. **XP/resource boosters**: Cap at 15% efficiency gain maximum. Never affect drop rates.
4. **Matchmaking**: If any spending advantage exists, separate spenders and non-spenders in competitive modes.
5. **Publish the policy**: Players trust systems they can verify. State the no-pay-to-win commitment publicly.

---

## Anti-Pattern 4: Grind Wall

### Description

Progression slows to a crawl at certain thresholds, forcing players to repeat
the same content for days or weeks with minimal reward. Players feel punished
rather than challenged.

### Root Causes

- Exponential cost curves without corresponding earning curve adjustments.
- Time-gating designed to slow progress but tuned too aggressively.
- Missing mid-tier content creates a vacuum between difficulty levels.
- Intentional friction to push players toward premium purchases.

### Detection Methods

| Signal | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| Time to next meaningful upgrade | 3-7 days | 7-14 days | > 14 days |
| Content repetition rate | < 3 repeats per goal | 3-10 repeats | > 10 repeats of same content |
| Player drop-off at level thresholds | Smooth curve | Noticeable dips at specific levels | Cliff-drop at specific levels |
| Session length at grind points | Normal (30-60 min) | Extended (2+ hours) | Players logging off after 10 min |

```python
def detect_grind_wall(level_data):
    """Find levels where time-to-progress spikes unnaturally."""
    walls = []
    for i in range(1, len(level_data)):
        current = level_data[i]["hours_to_next_level"]
        previous = level_data[i - 1]["hours_to_next_level"]
        if current > previous * 2.0:
            walls.append({
                "level": level_data[i]["level"],
                "hours_required": current,
                "spike_ratio": round(current / previous, 2),
                "severity": "CRITICAL" if current / previous > 3.0 else "WARNING"
            })
    return walls
```

### Fixes

1. **Smooth the curve**: Progression cost should increase by no more than 15-20% per level.
2. **Parallel progression**: Offer side activities (crafting, exploration, PvP) that contribute to the same goal.
3. **Catch-up mechanics**: Rested bonuses, weekly quest resets, or diminishing returns on repeated content.
4. **Milestone rewards**: Large payouts at round-number levels (10, 20, 30) to break up monotony.
5. **Content variety**: At least 3 different activities should contribute to any progression goal.

---

## Anti-Pattern 5: Currency Confusion

### Description

Too many currencies with overlapping purposes. Players cannot remember what
each currency does, where to earn it, or where to spend it. Decision fatigue
sets in and players disengage from the economy entirely.

### Root Causes

- Each new feature ships with its own currency instead of reusing existing ones.
- Currencies exist for technical convenience rather than design purpose.
- No regular audit to merge or retire unused currencies.
- Legacy currencies persist long after their content is outdated.

### Detection Methods

| Signal | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| Total active currencies | 4-6 | 7-9 | 10+ |
| Player understanding (survey) | > 80% can name all currencies | 50-80% | < 50% |
| Currencies with < 5% usage rate | 0 | 1-2 | 3+ |
| Overlapping spend categories | 0 overlaps | 1-2 partial overlaps | Multiple currencies buy same items |

### Fixes

1. **Six currency maximum**: Hard cap on simultaneous active currencies (see currency-templates.md).
2. **Merge overlapping currencies**: If two currencies buy similar things, combine them.
3. **Retire dead currencies**: Convert unused currencies to gold at a fair rate and remove them.
4. **Currency purpose test**: Every currency must answer "What unique thing can ONLY this currency buy?"
5. **UI clarity**: Currency icons, colors, and names must be instantly distinguishable.

---

## Anti-Pattern 6: Vendor Trash Flooding

### Description

Players' inventories fill with low-value items that exist only to be sold to
NPC vendors. Managing inventory becomes a chore rather than a game activity.
Players spend more time sorting junk than playing.

### Root Causes

- Loot tables generate too many common items with no use beyond selling.
- No auto-sell or auto-salvage system.
- Crafting system does not use common materials, making them worthless.
- Inventory space is limited but junk drops are unlimited.

### Detection Methods

| Signal | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| % of drops immediately vendored | < 30% | 30-60% | > 60% |
| Average inventory management time per session | < 2 min | 2-5 min | > 5 min |
| "Inventory full" frequency per hour | < 1 | 1-3 | > 3 |
| Player requests for auto-sell features | Low | Moderate | Dominant community request |

### Fixes

1. **Reduce junk drops**: Replace vendor trash with smaller amounts of gold directly.
2. **Auto-salvage system**: Let players set rules to automatically convert items below a rarity threshold.
3. **Make commons useful**: Crafting recipes that consume large quantities of common materials.
4. **Smart loot**: Filter drops based on player class and level. A mage does not need plate armor drops.
5. **Loot compression**: Instead of 10 items worth 5g each, drop 1 item worth 50g.

---

## Anti-Pattern 7: Exploitable Exchange Rates

### Description

Currency conversion paths create arbitrage opportunities. Players discover
loops where converting Currency A to B to C and back to A yields a profit,
generating infinite currency from nothing.

### Root Causes

- Multiple conversion paths between currencies with inconsistent rates.
- NPC buy/sell spreads that do not account for crafting transformations.
- Player market prices diverging from NPC vendor prices.
- Seasonal event exchanges creating temporary arbitrage windows.

### Detection Methods

```python
def detect_arbitrage(exchange_graph):
    """Find profitable currency conversion cycles."""
    # Bellman-Ford algorithm on -log(exchange_rate) edges
    # Negative cycle = arbitrage opportunity
    currencies = list(exchange_graph.keys())
    dist = {c: 0 for c in currencies}

    for _ in range(len(currencies) - 1):
        for src in exchange_graph:
            for dst, rate in exchange_graph[src].items():
                if dist[src] + (-math.log(rate)) < dist[dst]:
                    dist[dst] = dist[src] + (-math.log(rate))

    # Check for negative cycles
    for src in exchange_graph:
        for dst, rate in exchange_graph[src].items():
            if dist[src] + (-math.log(rate)) < dist[dst]:
                return "ARBITRAGE DETECTED"
    return "NO ARBITRAGE"
```

### Fixes

1. **Minimize conversion paths**: Currencies should not convert into each other (see currency-templates.md).
2. **Transaction taxes**: 5-10% tax on all currency exchanges and trades.
3. **Buy/sell spread**: NPC vendors buy at 30-50% of sell price, never higher.
4. **Rate monitoring**: Automated alerts when player market prices deviate more than 25% from NPC baselines.
5. **Cooldowns**: Rate-limit currency exchanges to prevent high-frequency exploitation.

---

## Anti-Pattern 8: Reward Cliff

### Description

Players transition from one content tier to another and experience a sudden,
dramatic drop in reward efficiency. Content that was rewarding yesterday becomes
worthless today. Players feel their time is being disrespected.

### Root Causes

- Reward scaling tied to content level rather than player level.
- New content tiers reset currency relevance without smooth transitions.
- Expansion launches that invalidate all previous gear and currency.

### Detection Methods

| Signal | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| Reward per hour: old content vs. new | 60-80% ratio | 30-60% ratio | < 30% ratio |
| Player engagement with previous content | Some return for variety | Rapid abandonment | Ghost town immediately |
| Time to regear after content tier change | 1-3 days | 3-7 days | > 7 days |

### Fixes

1. **Overlapping reward curves**: New content rewards 120-150% of old content, not 300%.
2. **Legacy conversion**: Old currency converts to new at a reasonable (not insulting) rate.
3. **Catchup gear**: Vendors sell baseline gear for the new tier at accessible prices.
4. **Transmog/cosmetic value**: Old content retains value for appearance collectors.
5. **Gradual scaling**: Bridge content between tiers that eases the transition.

---

## Quick Reference: Anti-Pattern Severity Matrix

| Anti-Pattern | Player Impact | Revenue Impact | Fix Difficulty | Priority |
|--------------|--------------|----------------|----------------|----------|
| Hyperinflation Spiral | High | Medium | Medium | P0 |
| Dead Economy | Medium | Low | Low | P1 |
| Pay-to-Win Trap | Critical | Short-term gain, long-term loss | High | P0 |
| Grind Wall | High | Medium (churn) | Medium | P1 |
| Currency Confusion | Medium | Low | Low | P2 |
| Vendor Trash Flooding | Low-Medium | None | Low | P2 |
| Exploitable Exchange Rates | Medium | High (economy collapse) | Medium | P0 |
| Reward Cliff | High | Medium (churn) | Medium | P1 |

---

## Prevention Checklist

Run this checklist monthly to catch anti-patterns before they become crises:

```
[ ] Total currency supply growth is below 5% per month
[ ] Median player balance is 2-5x daily earning (not 50x)
[ ] No purchasable item provides a stat or combat advantage
[ ] Time-to-next-upgrade is 3-7 days across all level ranges
[ ] Active currency count is 6 or fewer
[ ] Vendor trash represents less than 30% of all drops
[ ] No profitable currency conversion loops exist
[ ] Old content rewards at least 60% of current content per hour
[ ] New player purchasing power has not degraded over past 3 months
[ ] Player sentiment surveys show > 70% satisfaction with economy fairness
```
