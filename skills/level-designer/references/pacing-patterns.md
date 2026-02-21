# Pacing Design Patterns

Reference guide for structuring tension, release, and rhythm across levels and zones.
Pacing is the difference between a level that feels like a curated experience and one
that feels like a random sequence of encounters.

---

## Core Principle: Tension and Release

Every level is a series of cycles between tension (challenge, danger, uncertainty) and
release (safety, reward, clarity). The ratio and rhythm of these cycles define the
emotional experience of the level.

### Tension Sources

| Source | Effect on Player | Intensity |
|--------|-----------------|-----------|
| Combat | Adrenaline, focus, resource drain | High |
| Environmental hazards | Caution, spatial awareness | Medium-High |
| Time pressure | Urgency, stress, risk-taking | High |
| Resource scarcity | Anxiety, careful planning | Medium |
| Narrative stakes | Emotional investment, dread | Medium |
| Unknown territory | Curiosity mixed with caution | Low-Medium |
| Puzzle under threat | Split attention, cognitive load | Medium |

### Release Sources

| Source | Effect on Player | Recovery Quality |
|--------|-----------------|-----------------|
| Safe room / campfire | Full decompression, planning | High |
| Loot discovery | Dopamine, sense of progress | Medium |
| Vista / scenic moment | Awe, narrative context | Medium |
| NPC interaction | Story engagement, information | Medium |
| Puzzle completion | Satisfaction, mental reset | Medium |
| Shortcut unlocked | Relief, progress validation | Low-Medium |
| Ambient exploration | Curiosity satisfaction | Low |

---

## Tension/Release Cycle Templates

### Short Burst (15-30 minutes)

Best for: Action-heavy zones, dungeon crawls, linear segments.

```
Time:    0    5    10   15   20   25   30
         |    |    |    |    |    |    |
Tension: ####      ########      ##########
Release:     ####          ####
         [Intro] [Rest] [Build] [Rest] [Climax]
```

**Structure:**
1. Opening encounter (intensity 5-6/10) -- 5 min
2. Brief rest and exploration -- 4 min
3. Rising action: 2-3 encounters escalating (6-8/10) -- 10 min
4. Reward and breathing room -- 4 min
5. Climax encounter or boss (8-10/10) -- 7 min

**Cycle count:** 2-3 full tension/release cycles
**Combat-to-rest ratio:** 3:1

### Medium Arc (45-90 minutes)

Best for: Full levels, story chapters, dungeon wings.

```
Time:    0    15   30   45   60   75   90
         |    |    |    |    |    |    |
Tension: ##   ####  ######   ########  ##########
Release:   ###    ##      ###        ##
         [T1] [R1] [T2] [R2] [T3] [R3] [T4] [Climax]
```

**Structure:**
1. Tutorial/introduction encounter -- 10 min
2. Exploration and discovery -- 10 min
3. Two escalating encounters with a puzzle between them -- 15 min
4. Mid-level safe zone with story beat -- 10 min
5. Three encounters with increasing intensity -- 20 min
6. Brief respite before boss area -- 5 min
7. Boss fight -- 15 min
8. Post-boss reward and resolution -- 5 min

**Cycle count:** 4-5 full tension/release cycles
**Combat-to-rest ratio:** 2.5:1

### Long Campaign (2-4 hours)

Best for: Open world regions, multi-session zones, full story acts.

```
Time:    0    30   60   90   120  150  180  210  240
         |    |    |    |    |    |    |    |    |
Tension: ##  ####  ##  ######  ##  ########  ##  ##########
Release:   ##    ##  ##      ##  ##        ##  ##
         [Act 1      ] [Act 2          ] [Act 3            ]
```

**Structure:**
- Three sub-arcs, each following the Medium Arc pattern
- Escalating peak intensity across sub-arcs (Act 1 peaks at 7, Act 2 at 8, Act 3 at 10)
- Major rest point between each act (town, camp, story interlude)
- Overall tension envelope rises gradually across the full session

**Cycle count:** 10-15 full tension/release cycles
**Combat-to-rest ratio:** 2:1

---

## Combat-to-Exploration Ratios

Target ratios vary by genre and zone purpose. These are guidelines, not rigid rules.

### By Genre

| Genre | Combat | Exploration | Puzzle | Narrative | Rest |
|-------|--------|-------------|--------|-----------|------|
| Action RPG | 45-55% | 20-25% | 5-10% | 10-15% | 5-10% |
| Soulslike | 50-60% | 15-20% | 5-10% | 5-10% | 10-15% |
| Adventure RPG | 25-35% | 30-40% | 15-20% | 15-20% | 5% |
| Metroidvania | 35-45% | 30-35% | 15-20% | 5-10% | 5% |
| Open World | 30-40% | 35-45% | 5-10% | 10-15% | 5-10% |

### By Zone Purpose

| Zone Purpose | Combat | Exploration | Puzzle | Narrative |
|-------------|--------|-------------|--------|-----------|
| Tutorial | 20% | 30% | 20% | 30% |
| Standard dungeon | 50% | 25% | 15% | 10% |
| Boss arena | 80% | 5% | 5% | 10% |
| Hub / town | 0% | 40% | 10% | 50% |
| Secret area | 30% | 40% | 25% | 5% |
| Narrative climax | 25% | 10% | 5% | 60% |

---

## Rest Point Design

### Rest Point Types

| Type | Tension Level | Services | Placement Frequency |
|------|--------------|----------|-------------------|
| Full rest (camp/inn) | 0/10 | Save, shop, craft, heal, fast travel | Every 30-60 min |
| Partial rest (checkpoint) | 1-2/10 | Save, heal | Every 10-20 min |
| Momentary rest (safe pocket) | 2-3/10 | Brief pause, minor loot | Every 5-10 min |
| False rest (ambush setup) | Escalates to 8/10 | Appears safe, then triggers combat | Once per zone max |

### Rest Point Placement Rules

1. **Before difficulty spikes** -- Always place a rest point before a boss or encounter that is 3+ intensity points above the zone average
2. **After narrative revelations** -- Let the player absorb story beats in a safe space
3. **At branch points** -- When the player must choose a path, give them safety to deliberate
4. **Never immediately after another rest** -- Two consecutive rest points feel like dead space
5. **Scale with difficulty tier** -- Higher difficulties should have fewer but more impactful rest points
6. **Mark clearly** -- Rest points should be visually distinct (lighting change, music shift, architectural difference)

---

## Save Point Placement

### Save Philosophy

Saves should reduce frustration without eliminating consequence. The goal is to make the
player replay the minimum amount of content necessary to feel the stakes.

### Placement Guidelines

| Context | Save Availability |
|---------|------------------|
| Before boss encounters | Always (mandatory) |
| Before long encounters (5+ min) | Always (mandatory) |
| At zone entrances | Always (mandatory) |
| At branch decision points | Recommended |
| After completing optional content | Recommended |
| Mid-dungeon | Every 15-20 minutes of content |
| During boss fights | Never (except multi-stage with 30+ min total) |
| During puzzles | Only at puzzle start, not mid-solve |

### Auto-Save Triggers

- Entering a new zone or sub-zone
- Defeating a boss or miniboss
- Completing a quest objective
- Finding a unique or legendary item
- After any unskippable cutscene

---

## Content Density

### Target Content Per Hour

The density of meaningful interactions per hour of gameplay. "Meaningful" means the player
makes a decision, overcomes a challenge, or receives information.

| Content Type | Density Target | Notes |
|-------------|---------------|-------|
| Combat encounters | 4-8 per hour | Varies by zone type |
| Loot discoveries | 8-15 per hour | Includes chests, drops, hidden items |
| Narrative beats | 2-4 per hour | Dialogue, lore, story revelations |
| Environmental puzzles | 1-3 per hour | Locks, switches, platforming challenges |
| Environmental storytelling moments | 5-10 per hour | Visual stories, item placement, scene-setting |
| Player decisions | 1-2 per hour | Branch choices, moral decisions, build choices |

### Dead Zone Detection

A dead zone is any stretch of gameplay lasting more than 2 minutes with no meaningful
content. Dead zones feel like padding and break immersion.

**Common dead zone causes:**
- Long hallways between encounters
- Empty rooms with no loot, lore, or visual interest
- Backtracking through cleared areas with no new content
- Travel time between waypoints with nothing to discover

**Fixes:**
- Add environmental storytelling elements every 30-60 seconds of travel
- Place minor loot or collectibles along travel routes
- Add ambient encounters (non-combat wildlife, NPC travelers, weather events)
- Create shortcuts to reduce backtracking

---

## Pacing Graphs

### How to Read a Pacing Graph

```
Intensity
10 |
 9 |                                          *
 8 |                           *         *   * *
 7 |              *       *   * *       * * *
 6 |         *   * *     * * *   *     *
 5 |        * * *   *   *         *   *
 4 |       *     *   * *           * *
 3 |      *       * *               *
 2 |   * *
 1 |  *
 0 | *
   +-----------------------------------------> Time
     [Intro][Build][Peak][Valley][Build][Climax]
```

- **X axis:** Time or encounter sequence
- **Y axis:** Intensity (0 = complete safety, 10 = maximum threat)
- **Peaks:** Combat encounters, boss phases, high-stakes moments
- **Valleys:** Rest points, exploration, reward moments

### Anti-Patterns to Avoid

**Flatline (No Variation):**
```
5 | * * * * * * * * * * * * * * * *
  +-------------------------------->
```
Problem: Monotonous. Player becomes numb to a constant intensity level.

**Relentless Escalation (No Release):**
```
10|                              *
 8|                         *
 6|                    *
 4|               *
 2|          *
 0| *   *
  +-------------------------------->
```
Problem: Exhausting. Player has no recovery time and burns out.

**Sawtooth Without Build (No Anticipation):**
```
10| *    *    *    *    *    *
 0|  *  * *  * *  * *  * *  *
  +-------------------------------->
```
Problem: Jarring. Instant transitions between extremes feel unearned.

**Front-Loaded (All Action, Then Nothing):**
```
10| * * * * *
 5|          * *
 2|              * * * * * * * *
  +-------------------------------->
```
Problem: Anticlimactic. The most intense content comes before the player is invested.

---

## Genre-Specific Pacing Notes

### Action RPG (Default)

- Favor 3:1 combat-to-rest ratio
- Boss fights are the climactic peak of every zone arc
- Exploration serves as the primary release mechanism
- Puzzles provide cognitive variety between combat segments
- Story beats punctuate act transitions

### Soulslike Zones

- Extend tension phases (5-10 minutes without full safety)
- Momentary rests (bonfires) are the primary recovery
- Every encounter should feel consequential
- Boss runs (path from save to boss) should be 1-2 minutes, not longer
- Environmental hazards maintain tension between combat

### Exploration-Heavy Zones

- Invert the ratio: exploration is the primary activity
- Combat encounters are punctuation marks, not the main text
- Discovery is the reward loop (not loot or XP)
- Pacing through environmental variety rather than intensity changes
- Rest points are less critical because base tension is lower

---

## Pacing Review Checklist

- [ ] Zone has at least 3 complete tension/release cycles
- [ ] No dead zones longer than 2 minutes
- [ ] Combat-to-rest ratio matches genre and zone purpose
- [ ] Rest points placed before all major difficulty spikes
- [ ] Save points available at maximum 20-minute intervals
- [ ] Content density meets targets (see table above)
- [ ] Intensity curve has a clear climax near the zone end
- [ ] No two adjacent encounters are identical in type and intensity
- [ ] Post-boss reward moment exists (do not end on combat)
- [ ] Pacing tested with real playthrough timing data
