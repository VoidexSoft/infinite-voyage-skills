# Onboarding Design Patterns

Reference guide for designing tutorial and onboarding experiences.
Effective onboarding teaches the player how to play without breaking flow, overwhelming
them with information, or removing their sense of agency. This document catalogs proven
patterns, their trade-offs, and metrics for evaluating success.

---

## 1. Tutorial Types

### Guided Tutorial (Linear, Scripted)

A structured sequence where the game walks the player through each mechanic step by step,
often in a dedicated tutorial level.

**Structure:**
1. Lock the player in a controlled environment
2. Present one mechanic at a time with text or voice instruction
3. Require the player to perform the action before proceeding
4. Provide immediate feedback on success or failure
5. Unlock the next mechanic and repeat

**Examples:** Most JRPGs (opening chapters), Portal (test chambers as tutorials)

**Pros:**
- Ensures every player learns every mechanic
- Easy to pace and test
- Good for complex systems that require explanation
- Can integrate with narrative (tutorial as first mission)

**Cons:**
- Can feel restrictive and boring for experienced players
- Breaks immersion if poorly integrated into the story
- Risk of front-loading too much information
- Players who skip retain nothing

**Best for:** Complex RPGs with many interlocking systems, narrative-heavy games where the
tutorial can be part of the story.

### Contextual Tutorial (Just-in-Time)

Instructions appear only when the player encounters a situation that requires a new mechanic.
No dedicated tutorial level; learning happens organically during gameplay.

**Structure:**
1. Player encounters a new situation (locked door, first enemy, etc.)
2. A tooltip or prompt appears explaining the relevant action
3. Player performs the action in a real gameplay context
4. Prompt disappears; mechanic is now known

**Examples:** Breath of the Wild, Elden Ring (minimal prompts at shrines)

**Pros:**
- Feels natural; learning is embedded in gameplay
- No wasted teaching (mechanics are taught when needed)
- Respects player agency (no forced sequences)
- Works well for open-world games with non-linear progression

**Cons:**
- Player may miss prompts during intense moments
- Ordering is unpredictable; player might encounter an advanced mechanic early
- Harder to ensure comprehensive coverage
- Some mechanics may never be encountered if the player avoids certain areas

**Best for:** Open-world games, exploration-focused RPGs, games targeting experienced players.

### Sandbox Tutorial (Free Exploration)

The player is placed in a safe environment with optional guidance. They can experiment
freely and learn at their own pace.

**Structure:**
1. Safe area with all basic mechanics available
2. Optional signs, NPCs, or interactive objects that explain mechanics
3. Player chooses what to engage with and in what order
4. Exit the sandbox when comfortable (or after a time/completion trigger)

**Examples:** Minecraft (no formal tutorial, just the world), Dark Souls (tutorial area)

**Pros:**
- Maximum player agency and freedom
- Supports different learning styles (reading, experimenting, observing)
- Low-pressure environment reduces frustration
- Can revisit the sandbox area later for practice

**Cons:**
- Some players will leave without learning critical mechanics
- Requires careful environment design to implicitly teach without explicit instruction
- Harder to track what the player has or has not learned
- May feel aimless without any guidance

**Best for:** Games targeting hardcore audiences, creative/sandbox games, games with simple
core mechanics but deep mastery.

### Hybrid Tutorial (Recommended)

Combine elements of all three approaches based on the mechanic's complexity and the player's
progress.

| Mechanic Complexity | Tutorial Approach |
|---------------------|-------------------|
| Core (movement, camera) | Brief guided prompt in opening scene |
| Combat basics | Guided training encounter with weak enemy |
| Advanced combat (combos, dodging) | Contextual: prompt appears on first relevant encounter |
| Inventory and equipment | Guided: triggered when player receives first loot |
| Crafting, enchanting | Contextual: prompt at first crafting station |
| Advanced systems (skill trees) | Sandbox: practice area accessible from menu |

---

## 2. Tooltip Progressions

Tooltips should evolve as the player gains experience. Showing the same basic prompt to a
veteran player is patronizing; showing an advanced prompt to a new player is confusing.

### Progression Levels

| Level | Trigger | Tooltip Content | Example |
|-------|---------|----------------|---------|
| First encounter | Mechanic is new | Full explanation + input prompt | "Press [E] to interact with objects in the world. You can talk to NPCs, open chests, and activate switches." |
| Familiar (2-5 uses) | Mechanic used a few times | Shortened prompt | "Press [E] to interact" |
| Experienced (6+ uses) | Mechanic used regularly | Input hint only | "[E]" |
| Mastered (20+ uses) | Mechanic is routine | No prompt (unless re-enabled in settings) | -- |

### Implementation Rules

1. Track per-mechanic usage count in the player profile
2. Reduce tooltip detail at each threshold
3. Allow the player to reset tooltips to "first encounter" from Settings > Gameplay
4. "Tips" toggle in settings: On (all levels) / Reduced (familiar+) / Off (none)
5. Boss mechanics always show full tooltips regardless of experience level

---

## 3. Just-in-Time Teaching

The principle of teaching a mechanic at the exact moment the player needs it, not before.

### Rules

1. **Never teach what is not yet relevant.** Do not explain crafting in the first 10
   minutes if the player will not encounter a crafting station for an hour.
2. **Detect the teaching moment.** The system monitors player state and triggers instruction
   when the relevant condition arises (first combat, first locked door, first death).
3. **Minimal interruption.** Use a corner tooltip or brief NPC line, not a full-screen
   overlay or forced pause.
4. **Allow failure first.** When safe to do so, let the player fail once before explaining.
   Failure is a more memorable teacher than instruction.
5. **Reinforce on repeat failure.** If the player fails the same mechanic 3+ times, offer
   additional guidance (expanded tooltip, hint option, difficulty adjustment prompt).

### Teaching Moment Triggers

| Trigger Condition | Mechanic Taught | Delivery |
|-------------------|-----------------|----------|
| First enemy encounter | Basic attack | Bottom-screen prompt |
| Player takes first damage | Blocking/dodging | Corner tooltip + vignette |
| Player health drops below 30% | Healing item use | Glowing heal button + prompt |
| First locked door | Lock interaction / key use | Contextual prompt |
| First ability unlock | Ability usage | Guided prompt with cooldown explanation |
| First status effect received | Status effects | Status icon tooltip auto-opens |
| First death | Retry system | Death screen with tips |
| Player idle for 30+ seconds in puzzle | Puzzle hint system | "Need a hint? Press [H]" |

---

## 4. Skill Gating

Controlling which abilities and systems the player has access to based on progress. Prevents
information overload by limiting complexity early on.

### Gating Strategy

| Game Phase | Available Systems | Locked Systems |
|-----------|-------------------|----------------|
| Chapter 1 (0-2 hours) | Movement, basic attack, interact | Abilities, crafting, equipment, map |
| Chapter 2 (2-5 hours) | + First ability, equipment, inventory | Crafting, enchanting, advanced combat |
| Chapter 3 (5-10 hours) | + Crafting, map, fast travel | Enchanting, skill tree, multiplayer |
| Chapter 4+ (10+ hours) | All systems unlocked | -- |

### Unlock Communication

When a new system is unlocked:
1. Brief notification banner: "New system unlocked: Crafting!"
2. Optional guided introduction (player can skip: "Would you like a quick tutorial? [Yes/Skip]")
3. Menu entry appears with a "NEW" badge that persists until the player visits the screen
4. NPC or story beat introduces the system narratively
5. The system remains accessible from this point forward

### Gating Rules

- Never lock a system the player has already used
- If the player sequence-breaks (reaches a crafting station early), unlock crafting early
- Story-critical systems unlock automatically; optional systems unlock via discovery
- "Unlock All" cheat code available in accessibility settings for experienced players

---

## 5. Player Freedom vs Guidance

The balance between telling the player what to do and letting them figure it out.

### The Guidance Spectrum

```
FULL GUIDANCE                                              FULL FREEDOM
|-------|----------|----------|----------|----------|--------|
Scripted  Guided    Suggested   Hinted    Minimal    None
tutorial  prompts   objectives  at best   UI cues
```

### Recommended Position

Your game should sit at **"Suggested"** by default, with player-adjustable settings
that shift toward either end.

| Setting | Guidance Level | Description |
|---------|---------------|-------------|
| Story Mode | Full guidance | Detailed prompts, highlighted paths, quest arrows on-screen |
| Standard (default) | Suggested | Objective text visible, minimap markers, contextual prompts |
| Explorer | Hinted | Objective name only, no markers, environmental clues only |
| Pathfinder | Minimal | No quest markers, no prompts, journal only |

### Implementation

- Guidance level is a setting in Settings > Gameplay > Guidance Level
- Affects: tooltip frequency, minimap markers, quest arrows, NPC hint dialogue
- Does NOT affect difficulty (guidance and difficulty are independent axes)
- Each guidance level has a preview description in the settings menu

---

## 6. Retention Metrics

Measure onboarding effectiveness with these metrics.

### Key Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Tutorial completion rate | > 90% | Track how many players complete each tutorial step |
| Time to first meaningful action | < 3 minutes | Time from game start to first combat/interaction |
| Early quit rate (first 30 min) | < 10% | Players who quit and never return within first 30 minutes |
| Mechanic adoption rate | > 80% per mechanic | Percentage of players who use each mechanic at least once |
| Tooltip dismissal speed | Decreasing over time | Average time tooltips are visible before player acts |
| Death-before-learning rate | < 5% | Players who die to a mechanic before being taught it |
| Help menu access rate | < 15% | Players who open the help/tips menu (lower = better onboarding) |
| Settings change rate (controls) | < 20% first session | Players who rebind controls (high rate suggests bad defaults) |
| Return rate (day 2) | > 60% | Players who return the day after first play |

### Warning Signs

| Signal | Indicates | Response |
|--------|-----------|----------|
| High early quit rate | Onboarding is too slow or confusing | Shorten intro, let player play faster |
| Low mechanic adoption | Mechanic is not well taught or not discoverable | Add contextual prompt or hint |
| High death-before-learning | Teaching moment comes too late | Move the teaching trigger earlier |
| High help menu access | Core onboarding is insufficient | Improve in-game prompts |
| High rebind rate | Default controls feel wrong | Revisit default mappings |

---

## 7. Anti-Patterns (What to Avoid)

| Anti-Pattern | Problem | Alternative |
|-------------|---------|-------------|
| Text wall on first screen | Players skip and learn nothing | Use interactive teaching |
| Forced 20-minute tutorial | Players quit from boredom | Keep tutorial under 5 minutes; split across sessions |
| Teaching all mechanics at once | Information overload | Progressive disclosure; one mechanic at a time |
| Unskippable cutscene tutorial | Frustrates replay and experienced players | Always offer "Skip" or "Hold to Skip" |
| No tutorial at all | Alienates casual and new players | At minimum, provide contextual prompts |
| Tutorial that does not match difficulty | Easy tutorial, hard first level | Match tutorial difficulty to first real challenge |
| Locking the camera during tutorial | Feels claustrophobic | Let the player look around even during prompts |
| Rewarding tutorial completion excessively | Sets false expectations for rewards | Keep tutorial rewards modest |
| Testing mechanics in isolation only | Player cannot combine mechanics | Include a combined-mechanics challenge at tutorial end |

---

## 8. Onboarding Flow

### Recommended Sequence (First 15 Minutes)

| Time | Event | Teaching Method | Mechanic |
|------|-------|----------------|----------|
| 0:00 | Game opens, character wakes up in safe area | Environmental | Camera look |
| 0:30 | Prompt appears | Guided | Movement (WASD / Left Stick) |
| 1:00 | Door ahead with glow | Contextual | Interact (E / A) |
| 1:30 | Path leads to open area | Environmental | Exploration |
| 2:00 | Weak enemy appears, blocks path | Guided | Basic attack |
| 3:00 | Enemy attacks back | Contextual | Dodge / Block |
| 4:00 | Second enemy encounter (2 enemies) | Practice | Combat combo |
| 5:00 | Chest with loot | Contextual | Loot pickup |
| 5:30 | "Open inventory to equip" prompt | Guided | Inventory / Equipment |
| 7:00 | NPC introduces first ability | Narrative + Guided | Ability 1 |
| 8:00 | Enemies vulnerable to ability | Practice | Ability in combat |
| 10:00 | Mini-boss encounter | Challenge | Combine attack + dodge + ability |
| 12:00 | Boss drops health potion; player is damaged | Contextual | Healing |
| 13:00 | Exit tutorial area; world opens up | Environmental | Open exploration |
| 14:00 | Quest NPC gives first quest | Narrative | Quest system / objective tracker |
| 15:00 | Player is free | -- | Onboarding complete |

### Post-Onboarding Systems

These systems unlock gradually after the initial 15-minute onboarding:

- **Map and fast travel:** Unlocks when player discovers second area (30-60 min)
- **Crafting:** Unlocks at first crafting station (1-2 hours)
- **Skill tree:** Unlocks at level 3 (2-3 hours)
- **Equipment enchanting:** Unlocks at first enchanting NPC (3-5 hours)
- **Advanced combat (combos, counters):** Contextual prompts at relevant encounters

---

## Cross-References

- For onboarding input prompts by device, see `references/input-devices.md`
- For tooltip sizing and readability, see `references/font-guidelines.md`
- For onboarding feedback effects, see `references/feedback-library.md`
- For the detailed onboarding sequence design, see the Onboarding section in `SKILL.md`
- For accessibility during onboarding, see `references/accessibility-checklist.md`
