# Currency System Templates

Reference library of currency system templates. Use these as
starting points when designing new currency types or restructuring existing ones.

---

## Currency Classification

Every currency in a game economy falls into one of three categories:

| Category | Purpose | Source | Real-Money Link |
|----------|---------|--------|-----------------|
| **Primary** | Core gameplay loop, earned through all activities | Gameplay only | Never directly purchasable |
| **Secondary** | Specialized progression, faction gating, or activity rewards | Specific activities | Never directly purchasable |
| **Premium** | Cosmetics, convenience, monetization | Purchased or earned slowly | Directly purchasable |

### Design Rule

Primary currency drives power progression. Premium currency drives cosmetic progression.
These two paths must never cross. A player who spends real money should look different,
not be stronger.

---

## Template 1: Primary Currency (Gold)

```yaml
currency_id: gold
display_name: Gold
icon: coin_gold.png
category: primary
description: >
  The universal currency of Infinite Voyage. Earned through all gameplay
  activities and spent on equipment, consumables, crafting, and services.

properties:
  cap: null                  # No maximum balance
  tradeable: true            # Can be exchanged between players
  account_wide: false        # Per-character balance
  decimal_places: 0          # Whole numbers only
  purchasable_with_real_money: false

earning_rates:
  # Rates calibrated for mid-game (level 25-35) player
  mob_kills:
    rate: 5-15 per kill
    hourly_estimate: 1,200
    notes: Scales with mob level and zone difficulty
  quest_completion:
    rate: 100-500 per quest
    hourly_estimate: 800
    notes: Main quests pay 3x side quests
  dungeon_completion:
    rate: 500-2,000 per run
    hourly_estimate: 1,500
    notes: Bonus for first clear of the day
  daily_login:
    rate: 200 flat
    frequency: once per day
  world_events:
    rate: 300-1,000 per event
    hourly_estimate: 600
    notes: Participation-based scaling

spending_sinks:
  equipment_purchase:
    range: 100-10,000
    frequency: Every 2-5 levels
  equipment_repair:
    range: 5% of item base cost
    frequency: Every 2-3 hours of combat
  consumables:
    range: 10-100 per item
    frequency: Constant during combat
  crafting_fees:
    range: 50-5,000
    frequency: Per craft
  fast_travel:
    range: 25-200
    frequency: Multiple times per session
  auction_house_tax:
    range: 5% of sale price
    frequency: Per transaction
  respec_cost:
    range: 500-5,000
    frequency: Occasional

daily_target_balance:
  earning: 4,500-6,000
  spending: 3,500-5,500
  net: +500 to +1,000 (slight surplus intended)
```

### Gold Earning Curve by Level

| Level Range | Hourly Earn Rate | Target Equipment Cost | Days to Next Tier |
|-------------|------------------|-----------------------|-------------------|
| 1-10        | 400-800          | 500                   | 1-2               |
| 11-20       | 800-1,500        | 2,000                 | 2-3               |
| 21-35       | 1,500-3,000      | 5,000                 | 3-4               |
| 36-50       | 3,000-5,000      | 12,000                | 4-5               |
| 50+ (endgame) | 5,000-8,000    | 25,000                | 5-7               |

---

## Template 2: Secondary Currency (Faction Marks)

```yaml
currency_id: faction_marks
display_name: "[Faction] Marks"
icon: mark_{faction}.png
category: secondary
description: >
  Reputation tokens earned by completing activities for a specific faction.
  Spent exclusively at that faction's vendor for unique gear and recipes.

properties:
  cap: 10,000               # Weekly soft cap resets every Monday
  tradeable: false           # Soulbound to character
  account_wide: false
  decimal_places: 0
  purchasable_with_real_money: false

earning_rates:
  faction_quests:
    rate: 50-150 per quest
    daily_limit: 5 quests
  faction_dungeon:
    rate: 200-400 per clear
    weekly_limit: 3 clears
  faction_world_boss:
    rate: 500 per kill
    weekly_limit: 1 kill
  faction_daily_bounty:
    rate: 75 flat
    frequency: once per day

spending_sinks:
  faction_gear:
    range: 500-5,000
    notes: Equivalent to raid-tier gear, different aesthetic
  faction_recipes:
    range: 1,000-3,000
    notes: Exclusive crafting recipes
  faction_mount:
    cost: 8,000
    notes: Cosmetic mount, long-term goal
  faction_title:
    cost: 10,000
    notes: Prestige display

weekly_target:
  earning: 1,500-2,500
  spending: 500-2,000
  notes: Players stockpile toward large purchases over 3-6 weeks
```

### Faction Currency Design Principles

1. **Exclusivity** -- Faction Marks buy things Gold cannot. This gives them meaning.
2. **Weekly Cadence** -- Earning is gated weekly to prevent no-life advantages.
3. **Long-term Goals** -- The most desirable items take 4-8 weeks of consistent play.
4. **No Cross-Faction Trading** -- Each faction's marks are independent currencies.

---

## Template 3: Premium Currency (Stardust)

```yaml
currency_id: stardust
display_name: Stardust
icon: stardust.png
category: premium
description: >
  Premium currency used for cosmetics and convenience items.
  Primarily purchased with real money but earnable in small amounts
  through gameplay.

properties:
  cap: null
  tradeable: false
  account_wide: true         # Shared across all characters
  decimal_places: 0
  purchasable_with_real_money: true

real_money_pricing:
  - amount: 100    price_usd: 0.99    bonus: 0%
  - amount: 500    price_usd: 4.99    bonus: 0%
  - amount: 1100   price_usd: 9.99    bonus: 10%
  - amount: 2400   price_usd: 19.99   bonus: 20%
  - amount: 6500   price_usd: 49.99   bonus: 30%
  - amount: 14000  price_usd: 99.99   bonus: 40%

free_earning_rates:
  daily_login_streak:
    rate: 5 per day (streak bonus up to 15)
    monthly_max: 250
  battle_pass_free_track:
    rate: 200 per season (60 days)
  achievement_milestones:
    rate: 10-50 per milestone
    lifetime_total: ~2,000
  seasonal_events:
    rate: 50-100 per event
    frequency: 4 events per year

spending_categories:
  cosmetic_skins:
    range: 200-1,500
    notes: Character appearance, weapon skins
  emotes:
    range: 100-300
  mounts_cosmetic:
    range: 500-2,000
  battle_pass_premium:
    cost: 950
    frequency: Once per 60-day season
  inventory_expansion:
    cost: 200
    max_purchases: 10
  name_change:
    cost: 300
  character_slot:
    cost: 500

design_constraints:
  - NEVER sell stat boosts, weapons, or armor with Stardust
  - NEVER sell loot table advantages or drop rate boosts
  - NEVER gate gameplay content behind Stardust
  - Cheapest cosmetic (100 Stardust) earnable free in ~10 days
  - Battle pass purchasable with free earnings every ~4 seasons
```

---

## Exchange Rate Matrix

Currencies in Infinite Voyage do **not** convert directly into each other. This
prevents premium currency from becoming a backdoor to power progression.

| From / To         | Gold | Faction Marks | Stardust |
|--------------------|------|---------------|----------|
| **Gold**           | --   | Not possible  | Not possible |
| **Faction Marks**  | Not possible | --   | Not possible |
| **Stardust**       | Not possible | Not possible | -- |

### Why No Exchange?

- Gold-to-Stardust would let wealthy players bypass monetization.
- Stardust-to-Gold would create pay-to-win through currency laundering.
- Faction Marks are intentionally isolated to preserve their prestige value.

If an indirect exchange is ever needed (e.g., Stardust buys XP boosters that
accelerate Gold earning), cap the indirect benefit at no more than 15% efficiency
gain to prevent abuse.

---

## Template 4: Seasonal Currency (Voyage Tokens)

```yaml
currency_id: voyage_tokens
display_name: Voyage Tokens
icon: token_season.png
category: seasonal
description: >
  Limited-time currency earned during seasonal events. Expires at
  end of season. Spent on exclusive seasonal cosmetics and consumables.

properties:
  cap: 5,000
  tradeable: false
  account_wide: true
  expires: end of current season
  purchasable_with_real_money: false

earning_rates:
  seasonal_quests:
    rate: 100-300 per quest
    daily_limit: 3 quests
  seasonal_dungeon:
    rate: 500 per clear
    weekly_limit: 1 clear
  seasonal_challenges:
    rate: 50-200 per challenge
    notes: Progressive difficulty tiers

spending_sinks:
  seasonal_cosmetic:
    range: 500-3,000
  seasonal_consumable:
    range: 50-200
  seasonal_title:
    cost: 4,000

season_length: 60 days
design_notes: >
  Players should be able to earn the flagship seasonal cosmetic (3,000 tokens)
  within 40 days of moderate play (4-5 sessions/week). This leaves a 20-day
  buffer for casual players. Tokens convert to Gold at 1:2 ratio on season end
  as a consolation, not as a strategy.
```

---

## Currency Health Checklist

Use this checklist when designing or auditing any currency:

```
[ ] Currency has a clear, distinct purpose not served by other currencies
[ ] Earning rate feels rewarding without trivializing spending decisions
[ ] Multiple earning sources exist (not a single bottleneck)
[ ] Multiple spending sinks exist (not a single purpose)
[ ] Daily net balance is slightly positive (players feel progress)
[ ] No direct or indirect path from premium currency to power advantage
[ ] Cap (if any) is communicated clearly to players
[ ] Currency name and icon are immediately recognizable
[ ] New players encounter and understand the currency within first 2 hours
[ ] Endgame players still have meaningful uses for the currency
```

---

## Example: Full Currency Table for Infinite Voyage

| Currency | Category | Earn Source | Spend Sink | Cap | Tradeable | Real Money |
|----------|----------|------------|------------|-----|-----------|------------|
| Gold | Primary | All activities | Gear, crafting, services | None | Yes | No |
| Faction Marks | Secondary | Faction activities | Faction vendor | 10,000/wk | No | No |
| Dungeon Crystals | Secondary | Dungeon clears | Dungeon vendor gear | 3,000/wk | No | No |
| Arena Points | Secondary | PvP matches | PvP vendor gear | 5,000/wk | No | No |
| Stardust | Premium | Purchases + small free earn | Cosmetics, convenience | None | No | Yes |
| Voyage Tokens | Seasonal | Seasonal events | Seasonal cosmetics | 5,000 | No | No |
| Crafting Scraps | Material | Salvaging items | Crafting recipes | None | Yes | No |

### Design Notes

- **Six currencies maximum** at any point in the game. More than six creates
  cognitive overload and "currency confusion" (see economy-anti-patterns.md).
- Every currency answers the question: "What unique thing can I buy with this
  that I cannot buy with anything else?"
- If two currencies buy overlapping items, merge them or differentiate their
  inventories.
