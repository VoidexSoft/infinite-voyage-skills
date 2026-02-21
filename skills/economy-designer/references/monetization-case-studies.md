# Monetization Case Studies

Analysis of game monetization models, strategies, and ethical principles.
Use these case studies as reference when designing your game's monetization
system or evaluating proposed changes.

---

## Model 1: Battle Pass (Seasonal Progression Monetization)

### How It Works

Players purchase access to a premium reward track that unlocks items as they
play during a limited-time season (typically 60-90 days). A free track exists
alongside the premium track, giving all players some rewards.

### Structure

```
Season Length: 60 days
Tiers: 50 levels
Free Track: 50 rewards (consumables, small currency, 1-2 cosmetics)
Premium Track: 50 rewards (cosmetics, emotes, mounts, premium currency)
Premium Price: 950 Stardust (~$9.99 USD)
Premium Currency Return: 300 Stardust (covers ~30% of next pass)
```

| Tier | Free Track Reward | Premium Track Reward |
|------|-------------------|----------------------|
| 1 | 50 Gold | Seasonal Banner |
| 5 | Minor Health Potion x10 | Weapon Skin: Frostblade |
| 10 | 100 Gold | Character Skin: Winter Explorer |
| 15 | Crafting Materials x5 | 50 Stardust |
| 20 | 200 Gold | Emote: Snowball Throw |
| 25 | Voyage Tokens x100 | Mount Skin: Frost Stag |
| 30 | Minor Mana Potion x10 | 100 Stardust |
| 35 | 300 Gold | Pet: Snow Owl |
| 40 | Crafting Materials x10 | Character Skin: Ice Monarch |
| 45 | 500 Gold | 150 Stardust |
| 50 | Title: Seasonal Voyager | Legendary Mount: Crystal Drake |

### Revenue Projection

```
Assumptions:
  Monthly Active Users (MAU): 100,000
  Battle Pass Purchase Rate: 15-25% of MAU
  Price: $9.99

Conservative (15%): 15,000 x $9.99 = $149,850/season
Moderate (20%):     20,000 x $9.99 = $199,800/season
Optimistic (25%):   25,000 x $9.99 = $249,750/season

Annual (6 seasons): $899,100 - $1,498,500
```

### Player Perception

- **Positive**: Players feel they earn rewards through gameplay, not just buying them.
- **Positive**: Clear value proposition -- see all rewards upfront before purchasing.
- **Negative risk**: FOMO pressure if seasonal items never return. Mitigate by bringing items back after 2 seasons at reduced availability.
- **Negative risk**: If progression requires excessive daily play, it feels like a job. Target 60% completion with 4 sessions per week.

### Design Rules for Your Game

1. Battle pass must never contain stat-boosting items on the premium track.
2. Free track must feel worthwhile on its own, not just a teaser.
3. Players who miss a season can earn previous cosmetics (at reduced rate) two seasons later.
4. Premium currency return should be 25-35% of pass cost to reward loyal players without making the pass free.

---

## Model 2: Cosmetic-Only Store

### How It Works

All purchasable items are purely visual. No gameplay advantage is sold. Revenue
comes from players who want to express identity and stand out visually.

### Catalog Structure

| Category | Price Range (Stardust) | Price Range (USD) | Rotation |
|----------|------------------------|--------------------|---------:|
| Character Skins | 500-1,500 | $4.99-$14.99 | Permanent |
| Weapon Skins | 200-800 | $1.99-$7.99 | Permanent |
| Mount Skins | 800-2,000 | $7.99-$19.99 | Permanent |
| Emotes | 100-300 | $0.99-$2.99 | Permanent |
| Pets | 400-1,200 | $3.99-$11.99 | Permanent |
| Seasonal Bundles | 1,500-3,000 | $14.99-$29.99 | Limited (60 days) |
| Name/Title Effects | 200-500 | $1.99-$4.99 | Permanent |

### Revenue Projection

```
Assumptions:
  MAU: 100,000
  Monthly Spending Rate: 5-10% of MAU make a purchase
  Average Transaction Value: $8.00

Conservative (5%):  5,000 x $8.00 = $40,000/month
Moderate (8%):      8,000 x $8.00 = $64,000/month
Optimistic (10%):  10,000 x $8.00 = $80,000/month

Annual: $480,000 - $960,000
```

### Player Perception

- **Positive**: Community trusts the game. "Fair" reputation drives word-of-mouth growth.
- **Positive**: No resentment between paying and free players.
- **Negative risk**: Revenue per user is lower than aggressive monetization models.
- **Negative risk**: Requires high-quality art production to sustain interest.

### Design Rules for Your Game

1. Every cosmetic must be visually distinct and high quality. Low-effort recolors erode trust.
2. Price anchoring: Always have a few premium items ($15-20) to make mid-range items ($5-8) feel reasonable.
3. Preview system: Players must be able to preview any cosmetic on their character before buying.
4. Gifting: Allow players to purchase cosmetics for friends. Social spending increases revenue 15-20%.

---

## Model 3: Energy / Stamina System

### How It Works

Players have a regenerating resource (energy, stamina, action points) that limits
how much core content they can play per day. Premium currency can refill energy
for additional play.

### Structure

```yaml
energy_system:
  max_energy: 100
  regen_rate: 1 per 5 minutes (12 per hour)
  full_recharge: 8 hours 20 minutes
  activities:
    dungeon_run: 20 energy
    quest: 10 energy
    arena_match: 15 energy
  refill_options:
    free_refill:
      amount: 50
      frequency: once per day
    premium_refill:
      amount: 100
      cost: 50 Stardust (~$0.50)
      daily_limit: 3
    level_up_refill:
      amount: 100
      frequency: on level up
```

### Revenue Projection

```
Assumptions:
  MAU: 100,000
  Daily Refill Purchase Rate: 3-8% of DAU (DAU = 40% of MAU)
  Average Refills per Purchaser: 1.5/day
  Cost per Refill: $0.50

Conservative (3%): 40,000 x 0.03 x 1.5 x $0.50 x 30 = $27,000/month
Moderate (5%):     40,000 x 0.05 x 1.5 x $0.50 x 30 = $45,000/month
Optimistic (8%):   40,000 x 0.08 x 1.5 x $0.50 x 30 = $72,000/month

Annual: $324,000 - $864,000
```

### Player Perception

- **Positive**: Creates natural play sessions, prevents burnout.
- **Negative**: Players feel restricted. "I want to play but the game won't let me."
- **Negative**: Perceived as mobile-game monetization, carries stigma in PC/console markets.
- **Negative**: Whales can gain progression advantage by buying unlimited energy.

### Recommendation

**Do not implement an energy system for core gameplay.** Energy systems work for
mobile games where short sessions are expected. For your game's target
audience (PC/console RPG players), energy systems feel hostile.

If session-limiting is needed for balance reasons, use **daily reward caps** instead:
players can keep playing but earn reduced rewards after the daily target. This
respects player time without artificial gates.

---

## Model 4: Hybrid Model (Recommended)

### How It Works

Combine battle pass, cosmetic store, and optional convenience purchases into a
unified system. No energy gates, no pay-to-win, no loot boxes.

### Revenue Streams

| Stream | % of Revenue | Description |
|--------|-------------|-------------|
| Battle Pass | 35-40% | Seasonal pass, ~$10/season, 6 seasons/year |
| Cosmetic Store | 30-35% | Permanent and rotating cosmetic items |
| Convenience Items | 15-20% | Inventory expansion, character slots, name changes |
| Starter/Welcome Pack | 5-10% | One-time bundle for new players ($4.99) |
| Supporter Pack | 5% | Annual pack with exclusive title + cosmetics ($24.99) |

### Combined Revenue Projection

```
Assumptions:
  MAU: 100,000

Revenue Stream Breakdown:
  Battle Pass:     $175,000/season x 6 = $1,050,000/year
  Cosmetic Store:  $60,000/month x 12  = $720,000/year
  Convenience:     $30,000/month x 12  = $360,000/year
  Starter Packs:   500 new players/month x $4.99 x 12 = $29,940/year
  Supporter Packs: 2,000 x $24.99       = $49,980/year

Total Annual Revenue Estimate: $2,209,920
Revenue per MAU per Year (ARPMAU): $22.10
Monthly ARPPU (paying users, ~20% of MAU): $9.21
```

### Player Perception

- **Positive**: Multiple price points serve different budgets.
- **Positive**: Players choose how they want to spend, no forced purchases.
- **Positive**: Ethical reputation becomes a marketing advantage.
- **Negative risk**: Requires consistent content pipeline to sustain cosmetic sales.

---

## Model 5: Premium (Buy-to-Play)

### How It Works

Players pay an upfront price for the game. Post-launch revenue comes from
expansions and optional cosmetics.

### Structure

```
Base Game: $39.99
Major Expansion (annual): $29.99
Cosmetic Store: Optional, identical to Model 2
```

### Revenue Projection

```
Year 1:
  Base Game Sales: 200,000 units x $39.99 = $7,998,000
  Cosmetic Store:  $40,000/month x 12     = $480,000
  Total Year 1: $8,478,000

Year 2:
  Expansion Sales: 120,000 units x $29.99 = $3,598,800
  New Player Sales: 50,000 x $39.99       = $1,999,500
  Cosmetic Store: $50,000/month x 12      = $600,000
  Total Year 2: $6,198,300

Year 3+:
  Revenue declines unless new expansions or major content sustain interest.
```

### Player Perception

- **Positive**: No psychological manipulation. Players paid, they own the game.
- **Positive**: Community goodwill is very high.
- **Negative**: Revenue is front-loaded. Long-term sustainability depends on expansion cycle.
- **Negative**: Higher barrier to entry reduces player base size.

---

## Ethical Monetization Principles

These principles govern all monetization decisions.

### Principle 1: Transparency

Every cost, drop rate, and earning rate is either displayed in-game or
documented in public patch notes. Players must be able to make informed
purchasing decisions.

**Implementation**: Shop items show exact contents. Loot tables are published.
Premium currency costs are displayed in both Stardust and approximate USD value.

### Principle 2: No Predatory Mechanics

The following mechanics are permanently banned:

| Mechanic | Why It Is Banned |
|----------|-----------------|
| Loot boxes with random power items | Gambling mechanics exploit compulsive behavior |
| Gacha pulls for gameplay-affecting items | Random power purchases are inherently pay-to-win |
| Limited-time power items | Creates FOMO pressure to spend on non-cosmetics |
| Mandatory spending walls | Players must never be blocked by a paywall |
| Hidden odds or rates | Deception violates player trust |
| Dark patterns in UI | Misleading "discount" timers, confusing currency displays |

### Principle 3: Respect Player Time

A player who spends 0 dollars and plays 15 hours per week should have a
complete, satisfying experience. Premium purchases enhance the experience
visually and conveniently but never gatekeep content.

**Metric**: Free players should reach endgame content within 20% more time
than paying players, not 200% more.

### Principle 4: Whale Protection

Design monetization that discourages excessive spending:

```yaml
whale_protection:
  daily_spending_cap: $50 USD equivalent
  weekly_spending_cap: $150 USD equivalent
  monthly_spending_cap: $300 USD equivalent
  notification_thresholds:
    - at: $25/day
      message: "You've spent $25 today. Remember to spend responsibly."
    - at: $100/week
      message: "Weekly spending reminder. Need a break?"
  cooldown_prompt:
    trigger: 3 purchases within 10 minutes
    message: "Take a moment before your next purchase."
```

### Principle 5: Earnable Everything

Every item available for premium currency must also be earnable through gameplay.
The premium path is faster, not exclusive.

| Item | Premium Path | Free Path |
|------|-------------|-----------|
| Character Skin (1,000 Stardust) | Instant purchase | ~60 days of free Stardust earning |
| Battle Pass (950 Stardust) | Instant purchase | ~4 seasons of free Stardust earning |
| Mount Skin (1,500 Stardust) | Instant purchase | ~90 days of free Stardust earning |

---

## Revenue Projection Template

Use this template when modeling revenue for a new monetization feature:

```python
def project_revenue(
    mau: int,
    conversion_rate: float,
    avg_transaction_value: float,
    transactions_per_buyer_per_month: float,
    months: int = 12
) -> dict:
    """Project revenue for a monetization feature."""
    monthly_buyers = mau * conversion_rate
    monthly_revenue = monthly_buyers * avg_transaction_value * transactions_per_buyer_per_month
    annual_revenue = monthly_revenue * months

    return {
        "monthly_buyers": int(monthly_buyers),
        "monthly_revenue": round(monthly_revenue, 2),
        "annual_revenue": round(annual_revenue, 2),
        "arpmau": round(annual_revenue / mau / months, 2),
        "arppu": round(
            monthly_revenue / monthly_buyers if monthly_buyers > 0 else 0, 2
        )
    }

# Example: Cosmetic store projection
result = project_revenue(
    mau=100_000,
    conversion_rate=0.08,
    avg_transaction_value=8.00,
    transactions_per_buyer_per_month=1.5
)
# {'monthly_buyers': 8000, 'monthly_revenue': 96000.0,
#  'annual_revenue': 1152000.0, 'arpmau': 0.96, 'arppu': 12.0}
```

---

## Monetization Health Metrics

Track these metrics monthly to ensure monetization remains healthy:

| Metric | Target | Warning | Action Required |
|--------|--------|---------|-----------------|
| Conversion rate (MAU to payer) | 5-15% | < 3% or > 25% | Review pricing or value proposition |
| ARPPU (monthly) | $8-$15 | < $5 or > $30 | Adjust catalog or investigate whale behavior |
| Refund rate | < 2% | 2-5% | Investigate purchase satisfaction |
| Day-30 retention (free players) | > 25% | 15-25% | Check for paywall perception |
| Day-30 retention (paying players) | > 40% | 25-40% | Check for buyer's remorse |
| Community sentiment on monetization | > 70% positive | 50-70% | Review recent changes |
| Revenue concentration (top 1% of spenders) | < 30% of revenue | 30-50% | Activate whale protection measures |

---

## Monetization Decision Framework

When evaluating any new monetization proposal, answer these five questions:

1. **Does it sell power?** If yes, reject it. No exceptions.
2. **Can a free player earn the same thing through gameplay?** If no, add a free path.
3. **Does it create FOMO pressure?** If yes, add a return window (items come back after 2 seasons).
4. **Would you be comfortable if a journalist wrote about this feature?** If no, redesign it.
5. **Does it respect the player's budget?** If spending feels mandatory or the value is unclear, redesign it.

If a proposal passes all five questions, proceed to revenue modeling and player testing.
