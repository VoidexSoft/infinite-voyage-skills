# Playtesting Checklist for Levels

Structured checklist for conducting and evaluating playtests of level content.
Use this before and during playtesting sessions to ensure comprehensive coverage.
Results feed back into level design iteration.

---

## Pre-Test Setup

Before the playtest session, prepare the following:

### Test Environment

- [ ] Build is stable and representative of intended experience
- [ ] All encounters in the test zone are functional (no placeholder enemies or broken triggers)
- [ ] Save system is operational (player can resume if session is interrupted)
- [ ] Telemetry capture is active (heat maps, death locations, path tracking, time stamps)
- [ ] Recording software is running (screen capture and audio if possible)
- [ ] Test difficulty tier matches the tier being evaluated

### Tester Profile

Document the tester before the session begins:

| Field | Value |
|-------|-------|
| Tester ID | [Anonymous identifier] |
| Experience level | [None / Casual / Experienced / Expert] |
| Genre familiarity | [Familiar with action RPGs? Similar games played?] |
| Previous exposure | [First time with this build? Returning tester?] |
| Accessibility needs | [Colorblind? Motor impairment? Hearing?] |
| Test difficulty tier | [Story / Easy / Normal / Hard / Nightmare] |
| Session duration target | [How long should this test run?] |

### Test Objectives

Define what you are testing before the session starts:

- [ ] Primary objective stated (e.g., "Can players navigate the Sunken Ruins without external guidance?")
- [ ] Secondary objectives listed (e.g., "Do players discover the optional cave?")
- [ ] Success criteria defined (e.g., "80% of testers reach the boss within 45 minutes")
- [ ] Failure criteria defined (e.g., "More than 3 deaths at the same encounter indicates a spike")

---

## 1. Navigation Clarity

Can the player find their way through the level without getting lost?

### Observation Points

- [ ] **Critical path is discoverable** -- Player finds the main route without hints within 2 minutes of entering a new area
- [ ] **Landmark visibility** -- Key landmarks are visible from the player's natural sight line
- [ ] **Backtrack prevention** -- Player does not accidentally return to already-completed areas
- [ ] **Dead-end communication** -- When the player reaches a dead end, they understand it is intentional (secret area or locked gate) rather than a navigation failure
- [ ] **Vertical navigation** -- If the level has multiple elevations, the player understands how to move between them
- [ ] **Map utility** -- If a map is available, the player consults it and finds it helpful
- [ ] **Environmental guidance** -- Lighting, audio, and visual cues successfully guide the player

### Metrics to Capture

| Metric | Target | Red Flag |
|--------|--------|----------|
| Time to find critical path | Under 60 sec per area | Over 3 minutes of wandering |
| Wrong-direction events | 0-1 per zone | 3+ per zone |
| Map opens per hour | 2-4 (healthy consultation) | 8+ (player is lost) |
| Player asks for help | Never (unguided test) | Any request indicates navigation failure |
| Backtrack frequency | Intentional only | Unintentional backtracking |

---

## 2. Objective Visibility

Does the player understand what they need to do and where they need to go?

### Observation Points

- [ ] **Current objective is clear** -- Player can articulate their current goal at any point
- [ ] **Next objective is communicated** -- After completing an encounter, the player knows what comes next
- [ ] **Optional content is distinguishable** -- Player can tell the difference between main path and side content
- [ ] **Quest log accuracy** -- If objectives are tracked in UI, they match the actual game state
- [ ] **Environmental signposting** -- The environment suggests the next objective (open door, lit path, NPC gesture)
- [ ] **Objective pacing** -- New objectives appear at a rate the player can absorb (not too many at once)

### Metrics to Capture

| Metric | Target | Red Flag |
|--------|--------|----------|
| Time between objective completions | 5-15 minutes | Over 20 min with no progress |
| "What do I do now?" moments | 0 per zone | Any occurrence |
| Objective completion order | Matches intended sequence | Out-of-order completion |
| Optional content engagement | 40-60% of testers attempt | Under 20% means it is too hidden |

---

## 3. Difficulty Spikes

Are there sudden jumps in difficulty that frustrate the player?

### Observation Points

- [ ] **Death clustering** -- Deaths are spread across encounters, not concentrated at one point
- [ ] **Attempt count per encounter** -- No mandatory encounter requires more than the tier's expected attempts
- [ ] **Player expression during spikes** -- Note frustration (sighing, controller squeeze, verbal complaints)
- [ ] **Recovery from failure** -- After dying, the player understands what they did wrong and has a plan
- [ ] **Spike vs. wall** -- A difficulty spike is challenging but learnable; a wall feels impossible
- [ ] **Resource state at spike** -- Player has adequate healing and abilities when reaching difficult encounters
- [ ] **Teach-before-test** -- Every mechanic tested in a difficult encounter was taught earlier

### Metrics to Capture

| Metric | Target | Red Flag |
|--------|--------|----------|
| Deaths per encounter (Normal) | 0-3 | 5+ on a single encounter |
| Consecutive deaths at same point | 0-2 | 4+ (difficulty wall) |
| Health at encounter start | Above 50% | Consistently below 30% |
| Consumable usage per encounter | 0-2 | 4+ (resource drain wall) |
| Rage quit incidents | 0 | Any session abandonment due to difficulty |
| Time-to-complete vs. target | Within 30% | Over 200% of target |

---

## 4. Time-to-Complete

Does the level take the intended amount of time to play through?

### Observation Points

- [ ] **Total zone time matches target** -- Actual playtime is within 20% of design estimate
- [ ] **Individual encounter times match** -- Each encounter takes approximately the designed duration
- [ ] **Exploration time is meaningful** -- Time spent exploring feels rewarding, not aimless
- [ ] **Puzzle solve times** -- Puzzles take the intended time (not too fast = too easy, not too slow = too obtuse)
- [ ] **Pacing feels natural** -- The player does not feel rushed or bored

### Metrics to Capture

| Metric | How to Capture | Notes |
|--------|---------------|-------|
| Total zone completion time | Session timer | Compare to design target |
| Per-encounter time | Telemetry timestamps | Flag any over 150% of target |
| Time in safe zones | Telemetry | Under 10% feels rushed; over 30% suggests lost/bored |
| Time in optional content | Telemetry | Healthy range: 15-30% of total |
| Idle time (no inputs) | Input tracking | Over 30 seconds may indicate confusion or AFK |

---

## 5. Frustration Points

Identify moments that cause negative player experiences beyond intended challenge.

### Observation Points

- [ ] **Camera issues** -- Camera does not fight the player or obscure important information
- [ ] **Hitbox clarity** -- Player attacks and dodges connect/avoid as visually expected
- [ ] **Unfair deaths** -- No deaths feel "cheap" (off-screen attacks, instant kills without warning)
- [ ] **Repetitive failure loops** -- Dying and retrying does not force replaying more than 2 minutes of content
- [ ] **UI obstruction** -- HUD elements do not block important gameplay information
- [ ] **Control responsiveness** -- Inputs register immediately; no input lag or buffering issues
- [ ] **Loading times** -- Death-to-retry loading is under 10 seconds
- [ ] **Audio frustrations** -- No repetitive dialogue or sound effects on death loops

### Common Frustration Categories

| Category | Symptom | Design Fix |
|----------|---------|-----------|
| **Checkpoint distance** | Replaying 3+ min of content after death | Add intermediate checkpoint |
| **Unclear mechanic** | Player does not understand why they died | Add tutorial encounter or telegraph |
| **Resource starvation** | Player runs out of healing before a boss | Add resource drops or rest point |
| **Tedious travel** | Long walks between action | Add shortcut or fast travel |
| **Inventory management** | Constant menu juggling | Reduce loot volume or add auto-sort |
| **Unskippable content** | Forced cutscene or dialogue on every retry | Make skippable after first view |
| **Inconsistent rules** | Mechanic works differently than taught | Unify behavior across encounters |

---

## 6. Discovery Rates

How effectively do players find optional content, secrets, and environmental storytelling?

### Observation Points

- [ ] **Secret area discovery** -- Track which percentage of testers find each secret
- [ ] **Lore object interaction** -- Track how many lore objects are read/inspected
- [ ] **Optional encounter engagement** -- Track how many testers attempt optional challenges
- [ ] **Environmental storytelling comprehension** -- Ask testers what they think happened in a space
- [ ] **Hidden mechanic discovery** -- Track whether players find interactive environmental elements

### Metrics to Capture

| Content Type | Target Discovery Rate | Adjustment if Low | Adjustment if High |
|-------------|----------------------|-------------------|--------------------|
| Side paths | 50-70% | Add visual hints (light, color) | Ensure reward matches difficulty |
| Hidden rooms | 20-40% | Add subtle audio or visual cues | Acceptable; secrets should be rare |
| Lore objects on path | 70-90% | Reposition to be more visible | N/A (working as intended) |
| Lore objects hidden | 30-50% | Add environmental framing | Acceptable |
| Optional encounters | 40-60% | Make entrance more visible | Verify difficulty is appropriate |
| Environmental stories | 60-80% comprehension | Strengthen visual cues | N/A (working as intended) |

---

## 7. Completion Rates

Track overall success in completing the level and its components.

### Metrics to Capture

| Metric | Target (Normal) | Intervention Threshold |
|--------|----------------|----------------------|
| Zone completion rate | 90%+ | Below 80% requires redesign |
| Boss defeat rate (within 5 attempts) | 75%+ | Below 60% indicates overtuning |
| Optional content completion | 40-60% | Below 20% indicates poor discoverability |
| Side quest completion | 50-70% | Below 30% indicates unclear objectives |
| Full zone completion (100%) | 15-25% | Below 5% indicates excessive hidden content |
| Collectible found rate (per item) | Varies by placement | Items with 0% discovery must be repositioned |

### Abandonment Analysis

When a tester stops playing, record:

| Data Point | Purpose |
|-----------|---------|
| Last location | Identify where players quit |
| Last encounter attempted | Identify difficulty walls |
| Session duration | Compare to target |
| Death count at abandon point | Quantify frustration threshold |
| Verbal feedback | Qualitative reason for stopping |

---

## Post-Test Debrief

After each playtest session, conduct a brief interview (5-10 minutes):

### Standard Questions

1. What was the most enjoyable part of the level?
2. What was the most frustrating part?
3. Did you ever feel lost? Where?
4. Did you ever feel the difficulty was unfair? When?
5. What do you think happened in [specific environmental storytelling area]?
6. Did you find any secrets? How did you discover them?
7. Would you replay this level? Why or why not?
8. On a scale of 1-10, how would you rate the overall experience?

### Data Compilation

After all test sessions, compile:

- [ ] Heat map of player movement (identify dead zones and hot spots)
- [ ] Death location map (identify difficulty spikes)
- [ ] Average and median completion times per encounter
- [ ] Discovery rates for all optional content
- [ ] Aggregated frustration points with frequency counts
- [ ] Tester satisfaction scores with standard deviation
- [ ] Priority-ranked list of issues to address in the next iteration

---

## Iteration Criteria

| Priority | Condition | Action |
|----------|-----------|--------|
| Critical | Completion rate below 70% | Redesign blocking encounter or navigation |
| High | 3+ testers report same frustration point | Fix in next build |
| Medium | Discovery rate below target for main path content | Adjust visual guidance |
| Low | Discovery rate below target for secrets | Add subtle hints (optional) |
| Monitor | Time-to-complete over 120% of target | Investigate cause, may be acceptable |
