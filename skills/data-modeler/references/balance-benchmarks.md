# Balance Benchmark Targets

Reference tables for game balance targets in Infinite Voyage. These benchmarks are derived
from established RPG design conventions and should be used as starting points, not rigid
rules. Adjust based on playtesting results and the specific feel you want for the game.

---

## Time to Kill (TTK) Ranges

TTK is the time it takes for one combatant to defeat another under standard conditions
(no healing, no fleeing, appropriate gear for level).

### PvE TTK Targets

| Enemy Type          | TTK Target (seconds) | Rationale                                   |
|---------------------|----------------------|---------------------------------------------|
| Trash mob (1 enemy) | 3-8                  | Quick, satisfying, keeps pace up            |
| Trash pack (3-5)    | 10-20                | Group requires AoE or focus fire decisions  |
| Elite enemy         | 20-45                | Noticeable challenge, uses multiple abilities|
| Mini-boss           | 60-120               | Sustained engagement, learn attack patterns |
| Dungeon boss        | 120-300              | Major encounter, multiple phases            |
| Raid boss           | 300-600              | Group coordination, endurance test          |
| World boss          | 600-1200             | Community event, attrition over time        |

### PvP TTK Targets

| Format              | TTK Target (seconds) | Rationale                                   |
|---------------------|----------------------|---------------------------------------------|
| 1v1 Arena           | 15-30                | Long enough for counterplay, short enough to be decisive |
| 3v3 Arena           | 20-45                | Team fights need time for coordination      |
| Open world PvP      | 10-20                | Faster pace, escape should be possible      |
| Battleground (large) | 8-15                | Respawns are frequent, quick eliminations   |

### TTK Warning Signs

- **Under 3 seconds (PvE trash):** Combat feels button-mashy, no engagement
- **Over 15 seconds (PvE trash):** Combat feels tedious, pacing drags
- **Under 5 seconds (PvP 1v1):** One-shot territory, no counterplay
- **Over 60 seconds (PvP 1v1):** Stalemates, healer dominance, boredom

---

## DPS Ratios by Role

Relative damage output between roles, normalized to the DPS role as 1.0.

### Standard Trinity Model (Tank / DPS / Healer)

| Role    | DPS Ratio | Health Ratio | Healing Ratio | Notes                        |
|---------|-----------|--------------|---------------|------------------------------|
| Tank    | 0.40-0.50 | 1.8-2.5      | 0.0-0.2       | Damage is threat generation  |
| DPS     | 1.0       | 0.8-1.0      | 0.0-0.1       | Baseline for all ratios      |
| Healer  | 0.25-0.35 | 0.9-1.2      | 1.0           | Healing output = DPS output  |
| Support | 0.50-0.70 | 1.0-1.3      | 0.3-0.5       | Hybrid damage and utility    |

### Extended Roles

| Role       | DPS Ratio | Survivability | Utility     | Notes                      |
|------------|-----------|---------------|-------------|----------------------------|
| Bruiser    | 0.70-0.80 | High          | Low         | Off-tank, sustained damage |
| Assassin   | 1.2-1.5   | Very Low      | Low         | Burst damage, squishy      |
| Mage (AoE) | 0.80-1.0  | Low           | Medium      | Per-target lower, total higher |
| Ranger     | 0.90-1.0  | Medium        | Medium      | Consistent safe damage     |
| Controller | 0.30-0.50 | Medium        | Very High   | CC and debuffs over damage |

### Role Balance Rule of Thumb

The "power budget" for any role should sum to approximately the same total:

```
Power Budget = Damage + Survivability + Utility + Healing
```

A DPS that deals 1.0x damage should have ~0.8x survivability and ~0.2x utility.
A Tank that has 2.0x survivability should have ~0.5x damage and ~0.5x utility.
No role should exceed a total power budget of ~2.5x across all categories.

---

## Gold Economy Targets

### Gold Earn Rates by Activity

| Activity                | Gold per Hour | Level Range | Notes                        |
|-------------------------|---------------|-------------|------------------------------|
| Questing (main story)   | 400-800       | All         | Primary gold source early    |
| Questing (side quests)  | 200-500       | All         | Supplemental, optional       |
| Mob grinding            | 150-400       | All         | Scales with mob level        |
| Dungeon runs            | 500-1000      | 10+         | High reward for group play   |
| Crafting/gathering      | 200-600       | 5+          | Depends on market demand     |
| Daily quests            | 300-500       | Max level   | Consistent endgame income    |
| Raids                   | 800-1500      | Max level   | Weekly cap recommended       |

### Gold Sink Targets

| Sink                    | Cost Range        | Frequency        | Notes                      |
|-------------------------|-------------------|------------------|----------------------------|
| Gear repairs            | 5-50 per repair   | Every 1-2 hours  | Steady drain, not punishing|
| Consumables             | 10-100 each       | Per encounter     | Optional but recommended   |
| Fast travel             | 20-200 per trip   | Several per hour | Convenience tax            |
| Gear upgrades           | 500-5000 per tier | Every 5-10 levels| Major milestone purchases  |
| Respec/rebuild          | 100-1000          | Occasional       | Not punitive, but not free |
| Cosmetics (gold)        | 1000-50000        | Aspirational     | Long-term gold sinks       |
| Housing/furniture       | 500-10000 per item| Ongoing          | Endless sink potential     |
| Auction house tax       | 5-10% of sale     | Per transaction  | Inflation control          |

### Economy Health Indicators

| Metric                          | Healthy Range        | Warning Sign            |
|---------------------------------|----------------------|-------------------------|
| Net gold flow per hour          | Slightly positive    | Strongly positive = inflation |
| Time to afford level-appropriate gear | 1-3 hours      | Over 5 hours = frustration |
| Gold at max level (100 hours in) | 10000-50000         | Over 100000 = sink shortage |
| Vendor buy/sell ratio           | 0.25-0.50            | Over 0.75 = arbitrage risk |
| Repair cost as % of hourly income | 5-15%              | Over 25% = feels punitive |

---

## XP Curve Targets

### Time-to-Level Benchmarks

| Level Range | Minutes per Level | Cumulative Hours | Design Intent               |
|-------------|-------------------|------------------|-----------------------------|
| 1-5         | 10-15             | 0.8-1.2          | Tutorial, hook phase        |
| 6-10        | 15-20             | 2.0-3.0          | Core systems learned        |
| 11-20       | 20-30             | 5.5-8.0          | Mid-game expansion          |
| 21-30       | 30-45             | 10-15            | Build specialization        |
| 31-40       | 40-60             | 17-25            | Late-game challenge         |
| 41-50       | 50-75             | 25-40            | Endgame preparation         |

### XP Source Distribution

| Source               | % of Total XP | Notes                              |
|----------------------|---------------|------------------------------------|
| Main story quests    | 40-50%        | Primary leveling path              |
| Side quests          | 20-30%        | Enough to over-level if completed  |
| Mob kills            | 10-20%        | Supplemental, not primary          |
| Dungeons/instances   | 10-15%        | Group content bonus                |
| Exploration/discovery| 5-10%         | Reward for Explorers               |

### Leveling Pace Rules

- A player doing only main story quests should reach max level at about 80% of
  story completion
- A player doing all side quests should be 2-3 levels ahead of main story curve
- Pure mob grinding should take 2-3x longer than questing to reach the same level
- No single XP source should be more than 3x efficient than the next best option

---

## Item Power Budget

### Stat Budget by Rarity

Each rarity tier has a total stat budget allocated across all properties on the item.

| Rarity    | Stat Budget | Primary Stat | Secondary Stats | Special Effects |
|-----------|-------------|--------------|-----------------|-----------------|
| Common    | 100%        | 60-70%       | 30-40%          | None            |
| Uncommon  | 130%        | 55-65%       | 30-40%          | 0-1 minor       |
| Rare      | 170%        | 50-60%       | 25-35%          | 1 moderate      |
| Epic      | 220%        | 45-55%       | 25-35%          | 1-2 significant |
| Legendary | 280%        | 40-50%       | 20-30%          | 1-2 powerful    |

### Weapon Damage by Level and Rarity

Base damage values for a level 1 Common weapon are the 100% baseline.

| Level | Common | Uncommon | Rare   | Epic   | Legendary |
|-------|--------|----------|--------|--------|-----------|
| 1     | 10     | 13       | 17     | 22     | 28        |
| 10    | 25     | 33       | 43     | 55     | 70        |
| 20    | 45     | 59       | 77     | 99     | 126       |
| 30    | 70     | 91       | 119    | 154    | 196       |
| 40    | 100    | 130      | 170    | 220    | 280       |
| 50    | 135    | 176      | 230    | 297    | 378       |

### Item Level vs. Player Level

- Items should drop at or near the player's current level
- Items up to 3 levels below should still feel usable
- Items 5+ levels below should feel noticeably weak
- Items from higher-level content should feel like a meaningful upgrade
- Best-in-slot items should require endgame content, not just high level

---

## Encounter Difficulty Ratings

### Difficulty Tiers

| Tier       | Expected Deaths | Retry Rate | Target Audience        |
|------------|-----------------|------------|------------------------|
| Trivial    | 0               | 0%         | Below-level content    |
| Easy       | 0               | Under 5%   | Casual-friendly        |
| Normal     | 0-1             | 10-20%     | Average player         |
| Hard       | 1-3             | 30-50%     | Experienced players    |
| Very Hard  | 3-5             | 50-70%     | Optimizers and veterans|
| Extreme    | 5+              | 70-90%     | Hardcore challenge     |

### Encounter Composition Guidelines

| Encounter Type     | Enemy Count | Elite Ratio | Healer Ratio | Notes               |
|--------------------|-------------|-------------|--------------|----------------------|
| Random encounter   | 2-4         | 0%          | 0%           | Quick and simple     |
| Camp/outpost       | 4-8         | 10-20%      | 0-10%        | Light challenge      |
| Dungeon pull       | 3-6         | 20-30%      | 10-20%       | Tactical decisions   |
| Boss + adds        | 1 + 2-4     | Boss only   | 0-20% adds   | Focus fire required  |
| Ambush             | 4-6         | 10%         | 0%           | Surprise, positioning|
| Siege/defense      | 8-12 waves  | Escalating  | Escalating   | Endurance test       |

### Difficulty Scaling Formula

For content that scales to player level:

```
enemy_level = player_level + difficulty_offset
enemy_stat_multiplier = 1.0 + (difficulty_tier * 0.15)
```

| Difficulty Tier | Level Offset | Stat Multiplier |
|-----------------|-------------|-----------------|
| Easy            | -2          | 0.85            |
| Normal          | 0           | 1.00            |
| Hard            | +1          | 1.15            |
| Very Hard       | +2          | 1.30            |
| Extreme         | +3          | 1.50            |

---

## Progression Milestone Checklist

Use this to verify that the overall progression feels right at key milestones.

| Milestone          | Level | Playtime (hrs) | Should Have                         | Should Feel            |
|--------------------|-------|----------------|-------------------------------------|------------------------|
| Tutorial complete  | 3     | 0.5-1          | Basic abilities, starter gear       | Confident in controls  |
| First dungeon      | 8     | 3-5            | Full ability bar, group intro       | Excited for challenge  |
| Mid-story twist    | 20    | 10-15          | Build defined, strong gear          | Invested in story      |
| Class specialization | 25  | 15-20          | Spec choice, signature ability      | Powerful and unique    |
| Final story boss   | 40    | 25-35          | Near-complete build, epic gear      | Ready for the challenge|
| Endgame unlocked   | 50    | 35-45          | Max abilities, endgame systems open | Motivated to continue  |

---

## Using These Benchmarks

1. **Start with the tables above** as your initial design targets
2. **Build data models** in the data-modeler spreadsheets using these numbers
3. **Run game-balancer simulations** to verify the numbers play correctly
4. **Playtest with archetypes** to validate the feel matches the math
5. **Iterate** -- these benchmarks are starting points, not final answers
6. **Document deviations** -- if you intentionally break from a benchmark, note why

When a value in your game differs significantly from these benchmarks, that is not
necessarily a problem -- but it should be a conscious, documented design decision
rather than an accident.
