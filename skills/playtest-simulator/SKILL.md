---
name: playtest-simulator
description: >
  Virtual playtesting simulator for Infinite Voyage. Use this skill whenever the user
  wants to test a design without real players, predict how different player types would
  experience content, find exploits or degenerate strategies, check pacing, or validate
  that a mechanic feels right before implementation. Also trigger on phrases like "what
  would happen if a player does X", "is this exploitable", "how would a speedrunner
  approach this", "does the difficulty feel right", or "simulate a playthrough". This
  skill runs player archetypes through game content to surface issues before they reach
  real players — it's the cheapest QA you'll ever do.
---

# Playtest Simulator

You simulate how different player archetypes would experience game content. Instead
of guessing "would players enjoy this?", you systematically walk through the content
as different player types and report what each one would experience, exploit, or
struggle with.

## Why Virtual Playtesting Matters

Real playtesting is irreplaceable, but it's also expensive and slow. Virtual playtesting
catches obvious issues early — degenerate strategies, pacing problems, unclear objectives,
broken reward loops — so that real playtests can focus on subtler experiential questions.

## Player Archetypes

Each archetype represents a real player behavior pattern. When simulating, think like
this person — their goals, attention patterns, patience level, and decision-making style.

### Core Archetypes

#### The Optimizer (Min-Maxer)
- **Goal:** Maximum efficiency, best outcomes with least effort
- **Behavior:** Reads wikis, calculates DPS, ignores flavor text, exploits edge cases
- **Attention:** Focused on numbers, skip cutscenes, read tooltips carefully
- **Patience:** High for optimization, low for mandatory "slow" content
- **Decision style:** Always picks the mathematically optimal choice
- **Tests for:** Exploits, degenerate strategies, balance issues, dominant strategies

#### The Explorer
- **Goal:** See everything, discover secrets, understand the world
- **Behavior:** Goes off the critical path, reads lore, tries weird combinations
- **Attention:** High for environmental details, moderate for combat mechanics
- **Patience:** Very high — will spend hours exploring if the world is interesting
- **Decision style:** Picks the most interesting/unusual option
- **Tests for:** Content gaps, unreachable areas, narrative inconsistencies, missing rewards for curiosity

#### The Casual
- **Goal:** Have fun without stress, progress at a comfortable pace
- **Behavior:** Follows the main path, uses recommended builds, plays in short sessions
- **Attention:** Moderate — will read tutorials but forget complex mechanics
- **Patience:** Low for frustration, moderate for grinding if rewards feel good
- **Decision style:** Path of least resistance or most emotionally appealing
- **Tests for:** Difficulty spikes, confusing mechanics, unclear objectives, frustrating bottlenecks

#### The Completionist
- **Goal:** 100% everything — all quests, all collectibles, all achievements
- **Behavior:** Systematic coverage, tracks progress, revisits areas
- **Attention:** Very high for checklists and tracking, moderate for moment-to-moment gameplay
- **Patience:** Extremely high — will grind anything that has a progress bar
- **Decision style:** Does everything; if forced to choose, picks what completes more content
- **Tests for:** Missing content flags, impossible completions, tedious requirements, unclear progress tracking

#### The Socializer
- **Goal:** Shared experiences, cooperation, showing off
- **Behavior:** Seeks group content, shows cosmetics, helps new players
- **Attention:** Split between game and social interaction
- **Patience:** High for social content, low for mandatory solo content
- **Decision style:** What creates the best story to tell others
- **Tests for:** Solo bottlenecks in multiplayer progression, flex/cosmetic gaps, co-op feasibility

#### The Speedrunner
- **Goal:** Complete content as fast as possible, find skips
- **Behavior:** Sequence breaks, movement tech, skip everything optional
- **Attention:** Hyper-focused on routes and glitches
- **Patience:** Very high for routing, zero for unskippable content
- **Decision style:** Whatever is fastest, regardless of intended design
- **Tests for:** Sequence breaks, unskippable barriers, movement exploits, unintended shortcuts

## Simulation Workflow

### 1. Define the Scenario

```markdown
## Playtest Scenario: [Name]

**Content being tested:** [specific mechanic, quest, zone, or system]
**Test objective:** [what question are we trying to answer?]
**Archetypes to simulate:** [which player types, or "all"]
**Assumptions:**
- Player level/gear: [starting conditions]
- Knowledge level: [first playthrough vs experienced]
- Available resources: [currency, items, abilities]
```

### 2. Walk Through as Each Archetype

For each archetype, narrate their experience step by step:

```markdown
### [Archetype Name] Playthrough

**Entry point:** [How they arrive at this content]

**Step 1:** [What they encounter]
- **Sees:** [What's visible/obvious]
- **Decides:** [What this archetype would choose and why]
- **Feels:** [Emotional state — excited, bored, confused, frustrated]

**Step 2:** [Next encounter/decision]
...

**Outcome:** [How they exit this content]
- **Time spent:** [estimated duration]
- **Satisfaction:** [1-5 scale with reason]
- **Would they return?** [yes/no and why]
```

### 3. Identify Issues

Compile issues found across all archetypes:

```markdown
## Issues Found

### Critical (blocks progress or ruins experience)
- **[Issue]:** Found by [archetype]. [Description]. [Severity justification].

### Major (significantly degrades experience)
- **[Issue]:** Found by [archetype]. [Description].

### Minor (noticeable but not harmful)
- **[Issue]:** Found by [archetype]. [Description].

### Observations (design notes, not necessarily issues)
- **[Observation]:** [What was noticed and why it matters]
```

### 4. Recommend Fixes

For each issue, suggest a concrete fix:

```markdown
## Recommendations

| Issue | Fix | Affected Skills | Priority |
|-------|-----|----------------|----------|
| [Issue] | [Proposed solution] | [systems/narrative/etc] | [P0-P3] |
```

## Simulation Types

### Combat Encounter Test

Simulate how each archetype handles a specific fight:

```markdown
**Setup:** [Enemy composition, environment, player resources]

**Optimizer:** Calculates optimal rotation. Finds [exploit/strategy].
  DPS check: [does the math work?] TTK: [estimated]
**Casual:** Uses basic attacks and one ability. Struggles with [mechanic].
  Dies? [yes/no] Frustration point: [where they get stuck]
**Explorer:** Tries environmental interactions. Discovers [hidden thing].
**Speedrunner:** Attempts to skip via [method]. Succeeds? [yes/no]
```

### Quest Flow Test

Simulate how each archetype experiences a quest:

```markdown
**Quest:** [Name]
**Objective clarity:** Can each archetype understand what to do?
**Navigation:** Can they find where to go?
**Pacing:** How long does each step take per archetype?
**Choice quality:** Do branching paths feel meaningfully different?
**Reward satisfaction:** Does the reward match the effort?
```

### Economy Flow Test

Simulate how each archetype interacts with economic systems over time:

```markdown
**Duration:** [simulated play hours]
**Archetype economy behavior:**
- Optimizer: [min-max spending strategy]
- Casual: [natural spending pattern]
- Completionist: [completionist spending pattern]

**Results:**
- Currency accumulation rate per archetype
- Time to afford key items
- Pain points (can't afford X when they need it)
- Exploitation potential (infinite currency loops?)
```

### Onboarding Test

Simulate a new player's first hour:

```markdown
**Minute 0-5:** [What happens, what's clear, what's confusing]
**Minute 5-15:** [First real gameplay, first challenge]
**Minute 15-30:** [First meaningful choice or system unlock]
**Minute 30-60:** [Core loop established?]

**Retention risk points:** [moments where a player might quit]
**"Aha!" moments:** [moments where the game clicks]
```

## Exploit Detection Checklist

When simulating the Optimizer archetype, specifically check for:

- [ ] **Infinite resource loops** — Can any cycle generate net positive resources?
- [ ] **Sequence breaks** — Can content be accessed out of intended order?
- [ ] **Stat stacking** — Can any stat be pushed to game-breaking levels?
- [ ] **AI manipulation** — Can enemy AI be trivially exploited (kiting, stuck on geometry)?
- [ ] **Timer abuse** — Can any time-based mechanic be paused/exploited?
- [ ] **Duplication** — Can items/currency be duplicated through any interaction?
- [ ] **Negative value exploits** — Do any systems break with zero or negative values?
- [ ] **Edge case combinations** — Do any 2+ mechanics combine in unintended ways?

## Output Format

### Playtest Report

```markdown
# Playtest Report: [Content Name]
**Date:** [date]
**Archetypes tested:** [list]
**Content version:** [GDD section/commit reference]

## Executive Summary
[2-3 sentences: overall assessment and most critical finding]

## Archetype Experiences
[Detailed walkthrough per archetype]

## Issues Found
[Categorized by severity]

## Recommendations
[Prioritized fixes with skill assignments]

## Balance Flags
[Items for game-balancer to investigate]

## Narrative Flags
[Items for narrative-designer to review]

## Next Steps
[What to test after fixes are applied]
```

## Integration

- **From level-designer:** Receives encounter/zone designs to test
- **From systems-designer:** Receives mechanic specs to stress-test
- **From economy-designer:** Receives economy models to simulate long-term
- **To game-balancer:** Sends balance issues and exploit reports
- **To narrative-designer:** Sends narrative inconsistencies and pacing issues
- **To github-gamedev:** Sends bug reports and improvement tasks

## References

- `references/player-archetypes.md` — Extended archetype profiles with behavioral research
- `references/exploit-patterns.md` — Common game exploit catalog with detection methods
- `references/simulation-scenarios.md` — Pre-built scenario templates
- `references/reporting-format.md` — Full playtest report structure
