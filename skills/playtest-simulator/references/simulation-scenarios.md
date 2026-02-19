# Predefined Simulation Scenarios

Ready-to-use scenario templates for virtual playtesting in Infinite Voyage. Each scenario
defines the test objective, relevant archetypes, setup parameters, and evaluation criteria.
Select the scenario that matches the design question you need to answer.

---

## Scenario 1: First-Hour Experience

### Objective
Validate that the first 60 minutes of gameplay hook all player types, teach core
mechanics effectively, and create a desire to continue playing.

### Archetypes to Simulate
All six. The first hour is the most critical retention window and must work for
every player type.

### Setup Parameters
```
Player Level:       1 (fresh start)
Prior Knowledge:    None (first playthrough, no wiki, no guides)
Difficulty:         Default
Starting Resources: Tutorial-provided items only
Session Context:    Player just downloaded the game and launched it for the first time
```

### Evaluation Criteria
- **0-5 minutes:** Does the player understand what the game is? Is the first input satisfying?
- **5-15 minutes:** Is the first real challenge clear and achievable? Does the Casual complete
  it without frustration? Does the Optimizer find it too trivial?
- **15-30 minutes:** Has the player made a meaningful choice? Does the Explorer have
  something to discover off the main path?
- **30-60 minutes:** Is the core gameplay loop established? Does the player understand
  the primary progression system?
- **Retention verdict:** Would each archetype want to play a second session?

### Key Metrics
| Metric                          | Target              |
|---------------------------------|---------------------|
| Time to first player input      | Under 30 seconds    |
| Time to first meaningful choice | Under 15 minutes    |
| Time to core loop established   | Under 45 minutes    |
| Confusion events (Casual)       | Zero critical        |
| Boredom events (Optimizer)      | Under 2 instances   |
| Discovery moments (Explorer)    | At least 3          |

---

## Scenario 2: Mid-Game Grind Check

### Objective
Identify where mid-game progression feels like a grind rather than meaningful advancement.
Detect pacing valleys where players lose motivation.

### Archetypes to Simulate
Casual, Completionist, Optimizer. These three experience grind most differently.

### Setup Parameters
```
Player Level:       Mid-range (40-60% through content)
Prior Knowledge:    Moderate (understands all core systems)
Gear State:         Appropriate for level, no lucky drops
Resources:          Average accumulation for playtime invested
Session Context:    Player has been playing for 15-20 hours total
Quest State:        Main story at midpoint, several side quests available
```

### Evaluation Criteria
- **Progression rate:** How much power/level/story progress per hour of play?
- **Variety:** Are players doing different activities or repeating the same loop?
- **Reward satisfaction:** Do rewards feel meaningful or are they incremental stat bumps?
- **Goal clarity:** Does the player know what to work toward next?
- **Session motivation:** At the end of a session, does the player have a reason to return?

### Key Metrics
| Metric                          | Target              |
|---------------------------------|---------------------|
| Level-ups per hour              | At least 0.5        |
| New ability/item unlocks per hr | At least 1          |
| Repeated activity tolerance     | Max 3 before varied |
| Casual quit-risk moments        | Under 1 per session |
| Optimizer engagement drop       | No flat plateaus    |

### Red Flags
- Casual archetype runs out of easy content and faces a difficulty wall
- Optimizer finds the mathematically optimal mid-game loop and it is boring
- Completionist faces a checklist so long it feels demoralizing rather than motivating
- Main story stops providing new mechanics or reveals

---

## Scenario 3: Endgame Loop

### Objective
Validate that endgame content provides sufficient depth, variety, and motivation for
long-term engagement after the main story concludes.

### Archetypes to Simulate
Optimizer, Completionist, Socializer. These are the archetypes most likely to stay
at endgame.

### Setup Parameters
```
Player Level:       Max or near-max
Prior Knowledge:    Expert (knows all systems deeply)
Gear State:         Strong but not best-in-slot
Resources:          Substantial currency reserves
Session Context:    Player finished the main story, looking for reasons to keep playing
Quest State:        Main story complete, endgame systems unlocked
```

### Evaluation Criteria
- **Activity variety:** How many distinct endgame activities exist?
- **Progression depth:** Is there meaningful advancement beyond max level?
- **Social engagement:** Does endgame encourage group play?
- **Goal structure:** Are there short-term, medium-term, and long-term goals?
- **Power ceiling:** Is the gap between "good gear" and "best gear" motivating or demoralizing?

### Key Metrics
| Metric                          | Target              |
|---------------------------------|---------------------|
| Distinct endgame activities     | At least 4          |
| Time to best-in-slot (estimate) | 40-80 hours         |
| Weekly engagement hooks         | At least 3          |
| Group content availability      | At least 2 activities|
| Meaningful daily goals          | 3-5 per session     |

---

## Scenario 4: Economy Stress Test

### Objective
Verify that the game economy remains stable under different player behaviors and over
extended simulated time periods. Identify inflation risks, deflation traps, and
exploitable loops.

### Archetypes to Simulate
Optimizer, Casual, Completionist. Each interacts with the economy very differently.

### Setup Parameters
```
Simulation Duration:  100 hours of simulated play per archetype
Gold Sources Active:  Enemy drops, quest rewards, vendor sales, crafting
Gold Sinks Active:    Repairs, consumables, fast travel, gear upgrades, crafting costs
Marketplace:          Active (if applicable)
Starting Gold:        0 (simulate from fresh start)
```

### Evaluation Criteria
- **Inflation check:** Does gold accumulate faster than sinks can absorb it?
- **Deflation check:** Are there points where players cannot afford necessary items?
- **Exploit scan:** Can any loop generate net-positive gold infinitely?
- **Fairness:** Can the Casual afford essential items at a reasonable pace?
- **Sink adequacy:** Do gold sinks feel meaningful or punitive?

### Key Metrics
| Metric                          | Target              |
|---------------------------------|---------------------|
| Gold per hour (Casual)          | 200-500             |
| Gold per hour (Optimizer)       | 500-1200            |
| Essential item affordability    | Within 2 hours max  |
| Net gold flow at hour 50        | Near zero (balanced)|
| Exploit loop profit per hour    | Zero (none exist)   |

### Stress Test Matrix
Run each combination and check for instability:
- Optimizer only buying (hoarding)
- Optimizer only selling (dumping)
- All archetypes at endgame with nothing left to buy
- New player entering a mature economy
- Sudden influx of rare items from a new content drop

---

## Scenario 5: PvP Balance Check

### Objective
Validate that player-versus-player combat is competitive across all classes, builds,
and gear levels within the intended PvP bracket.

### Archetypes to Simulate
Optimizer (primary), Casual (secondary). PvP is dominated by Optimizers but must
not be hostile to Casuals.

### Setup Parameters
```
Player Level:       PvP bracket level (e.g., max level)
Gear State:         Standardized (equal gear) AND natural (earned gear)
Classes:            All available classes, one simulation per matchup
Build Variety:      Meta build + 2 off-meta builds per class
Arena Type:         1v1 and small group (3v3)
Match Count:        10 simulated matches per matchup
```

### Evaluation Criteria
- **Win rate distribution:** No class should exceed 60% win rate against any other class
- **TTK (Time to Kill):** Should fall within the target range for the genre
- **Counterplay:** Every strategy must have at least one viable counter
- **Build diversity:** Meta builds should not be more than 20% stronger than off-meta
- **Casual viability:** A Casual player should win ~30% of matches against an Optimizer
  of equal gear level (skill matters but gear/build is not everything)

### Key Metrics
| Metric                          | Target              |
|---------------------------------|---------------------|
| Highest class win rate          | Under 55%           |
| Lowest class win rate           | Above 45%           |
| Average TTK                     | 15-30 seconds       |
| One-shot potential              | Zero (no one-shots) |
| Build diversity in top 10       | At least 4 builds   |

---

## Scenario 6: New Player Retention

### Objective
Identify the specific moments in the first 3 days of play where new players are most
likely to quit, and validate that retention mechanics are effective.

### Archetypes to Simulate
Casual (primary), Explorer (secondary). These represent the largest new-player segments.

### Setup Parameters
```
Player Level:       1, progressing naturally
Prior Knowledge:    Zero (no guides, no friends playing)
Session Pattern:    Day 1: 45 min, Day 2: 30 min, Day 3: 30 min (realistic casual)
Interruption Model: Player gets distracted once per session for 5 minutes
Return Context:     Player forgot some controls between sessions
```

### Evaluation Criteria
- **Day 1 hook:** Does the first session end with curiosity about what comes next?
- **Day 2 return:** Is there a reason to come back? Does the game remind them?
- **Day 2 re-onboarding:** Can the player pick up where they left off without confusion?
- **Day 3 habit formation:** Is a daily routine established? Do they know their next goal?
- **Churn moments:** Document every point where the simulated player considers quitting

### Key Metrics
| Metric                          | Target              |
|---------------------------------|---------------------|
| Day 1 completion rate           | 90%+ reach session end naturally |
| Day 2 return motivation (1-5)   | 4+                  |
| Day 2 re-orientation time       | Under 2 minutes     |
| Day 3 established routine       | Yes                 |
| Total churn risk moments        | Under 3 across all days |

---

## Scenario 7: Whale Spending Path

### Objective
Map the complete monetization journey of a high-spending player to validate that
spending feels rewarding, does not create pay-to-win dynamics, and does not lead
to buyer's remorse.

### Archetypes to Simulate
Optimizer-Socializer hybrid (the typical whale profile). This player wants to be
powerful AND to be seen as powerful.

### Setup Parameters
```
Player Level:       1, progressing with spending
Budget:             Unlimited (simulate uncapped spending)
Spending Triggers:  Convenience, power, cosmetics, time-saving, social status
Session Pattern:    Daily, 1-2 hours
Monetization Menu:  All available premium items and services
Comparison Baseline: Free-to-play Optimizer playing the same content
```

### Evaluation Criteria
- **Spending satisfaction curve:** Does each purchase feel good? Does value per dollar
  decrease gracefully or hit a cliff?
- **Power advantage:** How much stronger is the whale vs. F2P at equal playtime?
- **Social perception:** Would other players resent or admire the whale's purchases?
- **Buyer's remorse triggers:** At what spending level does the player feel they
  overspent or were manipulated?
- **Content access:** Does spending unlock content that F2P players cannot access at all?

### Key Metrics
| Metric                          | Target              |
|---------------------------------|---------------------|
| Spending satisfaction at $50    | High (clear value)  |
| Spending satisfaction at $200   | Moderate (still worth it) |
| Spending satisfaction at $500+  | Diminishing but not regretful |
| Power gap vs F2P (same hours)   | Under 15% stat advantage |
| P2W perception by F2P players   | Low ("cosmetic envy, not power envy") |
| Regret-inducing purchases       | Zero                |

### Spending Path Checkpoints
Document the whale's spending at each milestone:
1. **First purchase:** What triggers it? How much? What do they buy?
2. **$25 mark:** What have they gained? How does the game feel different?
3. **$100 mark:** Are they still getting new value or repeating purchases?
4. **$250 mark:** Has spending become habitual? Are they still enjoying it?
5. **$500+ mark:** What is left to buy? Is there fatigue or continued desire?

---

## Running a Scenario

To execute any scenario above:

1. **Copy the setup parameters** into your simulation context
2. **Select the specified archetypes** and fully adopt each mindset
3. **Walk through the content** step by step, documenting decisions and reactions
4. **Evaluate against the criteria** and fill in the metrics table with findings
5. **Flag any metric that misses its target** as an issue in the playtest report
6. **Recommend specific fixes** for each flagged issue
7. **Note cross-scenario dependencies** (e.g., a mid-game grind issue that also affects retention)

## Combining Scenarios

Some design questions require running multiple scenarios in sequence:

- **Full lifecycle test:** Run scenarios 1, 2, 3 in order (first hour, mid-game, endgame)
- **Economy validation:** Run scenario 4, then verify with scenarios 2 and 3
- **Monetization audit:** Run scenario 7, then cross-check with scenarios 5 and 6
- **New content drop:** Run scenario 6 for returning players, then scenario 2 at the new content level

Always document which scenarios were combined and how findings from one informed the next.
