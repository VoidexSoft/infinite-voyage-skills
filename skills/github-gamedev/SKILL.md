---
name: github-gamedev
description: >
  Game development project management and GitHub issue orchestration for game development.
  Use this skill whenever the user mentions GitHub, issues, project boards, sprints, tasks,
  milestones, tracking, project status, or board management. Trigger when converting design
  decisions into tracked work items, when planning sprints, when generating team reports, or
  when checking project health. Keywords that should trigger this skill include: GitHub,
  gh, issue, PR, pull request, board, column, sprint, milestone, task, ticket, backlog,
  in progress, review, done, project status, burndown, velocity, GDD-to-issues, tracking.
  This skill bridges design work (GDD, mechanics, level layouts) into executable GitHub issues
  with proper decomposition, labeling, and project board management. It handles the full
  lifecycle: design → decomposition → issue creation → board management → reporting.
---

# GitHub GameDev

You are the project management nerve center for the game project. Your job is to translate
game design work into tracked, actionable GitHub issues and manage the project board to keep
the team synchronized and progressing toward sprint goals.

## Core Philosophy

Game development is complex work spanning art, code, design, audio, and QA. GitHub becomes
useful only when:
1. **Issues map to real work units** — not too granular (100+ issues per feature), not too coarse (one issue per discipline)
2. **Design decisions are decomposed first** — before creating issues, clarify what actually needs to be done
3. **Labels tell the story** — a glance at labels reveals what type of work and priority
4. **Board columns match workflow** — work flows left-to-right through Backlog → Sprint → In Progress → Review → Done
5. **Reports are actionable** — sprint velocity, burndown, and status reports inform iteration speed and blockers

## Core Workflow

### 1. Parse Design Decisions

When the user presents a design decision (from GDD, a design document, or verbal description):

**Questions to ask:**
- What **part of the game** does this affect? (mechanics, narrative, art, level, UI, audio, balance)
- What **dependencies** does this have on other systems?
- What **existing content** needs to be modified vs. created from scratch?
- What's the **target ship date** for this feature?
- Who **owns** each part of the work? (systems programmer, character artist, designer, etc.)

**Example:**
- **Design Decision:** "The Void Engine has a new ability: 'Phase Shift' lets the player warp through walls and enemies for 2 seconds"
- **Parsing:**
  - Mechanics: New player ability with 8s cooldown, phase duration configurable
  - Balance: Need to verify it doesn't trivialize level design
  - Art: Need VFX for phase entry/exit and shimmer while phased
  - Audio: Need SFX for ability activation and phase state loop
  - QA: Need test cases for wall clipping, enemy collision during phase, ability interactions
  - Level Design: Needs playtesting to ensure puzzle design still works

### 2. Decompose into Tasks

Break the design decision into **concrete, assignable work items**. Each issue should represent
1-3 days of focused work (for a single person).

Use this decomposition framework:

```
FEATURE: [Feature Name]
├── DESIGN
│   ├── Define mechanics (cooldown, duration, interaction with X system)
│   ├── Write design doc section
│   └── Mark for balance review
├── CODE
│   ├── Implement ability system hooks
│   ├── Implement phase shift state machine
│   ├── Implement collision/clipping handling
│   └── Implement ability cooldown UI
├── ART
│   ├── Design phase entry VFX
│   ├── Design phase exit VFX
│   ├── Create shimmer/phase shader for player
│   └── Create ability icon
├── AUDIO
│   ├── Record/source activation SFX
│   ├── Record/source phase loop ambient
│   └── Integrate into audio engine
├── QA
│   ├── Test wall clipping edge cases
│   ├── Test ability vs. enemy types
│   ├── Test ability interactions (cooldown stacking, etc.)
│   └── Verify physics doesn't break during phase
└── BALANCE
    └── Playtesting pass: verify puzzles still valid, difficulty unchanged
```

### 3. Create/Update GitHub Issues

Use the `gh` CLI to create issues. **Never use the web interface for bulk operations** — the CLI is
more reliable and scriptable.

**Basic issue creation:**

```bash
# Single issue
gh issue create \
  --title "Implement Phase Shift ability state machine" \
  --body "Create the core ability logic for Phase Shift.

## Acceptance Criteria
- [ ] Ability can be activated (input binding exists)
- [ ] Duration is configurable (default 2s)
- [ ] Cooldown is configurable (default 8s)
- [ ] Player cannot take damage while phased
- [ ] Player collision with enemies disabled while phased

## Depends On
- #123 (Ability system framework)

## Testing
- Verify phase state machine transitions correctly
- Verify cooldown counts down during and after phase
- Verify player is invulnerable while phased" \
  --label "code,core-systems" \
  --milestone "v0.2-void-engine" \
  --project-v2 "My Game"
```

**Script for bulk creation (use `gdd_to_issues.py`):**

```bash
# Convert GDD design decision to issues
python scripts/gdd_to_issues.py \
  --gdd-section "void-engine-abilities.md" \
  --feature "Phase Shift" \
  --repo "user/my-game"
```

This script reads a design section and produces:
- One **design** issue (define mechanics, write doc, get team feedback)
- One **code** issue per programmer task (typically 2-4 issues)
- One **art** issue per asset type (VFX, shader, icon, etc.)
- One **audio** issue per SFX/music element
- One **QA** issue per testing area
- One **balance** issue for review/tuning

### 4. Update Project Board

The project board has fixed columns matching the workflow:

```
[ Backlog ] → [ Sprint ] → [ In Progress ] → [ Review ] → [ Done ]
```

**Column semantics:**

| Column | Meaning | Entry Criteria | Exit Criteria |
|--------|---------|---|---|
| **Backlog** | Unscheduled work; ready to estimate but not committed | Issue created, unclear who will do it, no sprint assigned | Moved to Sprint during sprint planning |
| **Sprint** | Committed to this sprint; team member assigned | Assignee confirmed, sprint added, dependencies tracked | Moved to In Progress when work starts |
| **In Progress** | Someone is actively working on this right now | Work started, assignee confirmed, progress visible | Ready for review (PR open, QA started, design complete) |
| **Review** | Work complete; waiting for feedback/approval (PR review, QA testing, design approval) | PR submitted, QA testing started, or design doc awaits feedback | Feedback incorporated and ready to merge/ship |
| **Done** | Work shipped and merged; ready for playtesting/release | PR merged, QA passed, or design milestone reached | Ready for next cycle |

**Move issues to Sprint at sprint planning:**

```bash
# List all backlog issues (not in any sprint)
gh issue list --label "code,art,audio" --state open -q 'not:(project:"My Game")' --json number,title

# Assign issues to sprint (example: moving issue #456 to "Sprint 5")
gh issue edit 456 --add-project "My Game" --add-assignee "alice"
```

**Automate board updates with `board_status.py`:**

```bash
# Scan issues and auto-move based on PR status, completion status, etc.
python scripts/board_status.py \
  --repo "user/my-game" \
  --auto-promote  # Move In Progress → Review if PR linked and passing CI
```

### 5. Generate Reports

Use `sprint_report.py` to produce weekly/sprint reports:

```bash
# Generate sprint status report
python scripts/sprint_report.py \
  --repo "user/my-game" \
  --sprint "5" \
  --format "markdown" \
  > sprint_5_status.md
```

Report includes:
- **Sprint Goal** (from sprint description)
- **Velocity** (issues completed this sprint vs. last sprint)
- **Burndown** (issues remaining day-by-day)
- **Status by Discipline** (# issues: Backlog, In Progress, Review, Done for each label)
- **Blockers** (issues with "blocker" label + who's blocking whom)
- **At Risk** (issues approaching deadline with no linked PRs/completion)
- **Completed This Sprint** (issues moved to Done, with links)
- **Upcoming Dependencies** (next sprint issues that depend on this sprint's work)

## Issue Creation Templates

Use these templates when creating issues from design work. Store them in
`templates/` for `gh issue create --template` support.

### Template: Feature Issue

```markdown
# [Feature Name]

## Summary
One-sentence description of what this feature adds to the game.

## Design Reference
Link to GDD section or design doc defining this feature.

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Implementation Notes
- [Optional context or guidance]

## Depends On
- #123 (Parent issue or prerequisite)

## Blocks
- #456 (Issues waiting for this one)

## Testing
Specific test cases or QA focus areas.

## Screenshots/References
[If applicable: concept art, reference images, debug screenshots]

## Labels
- `[discipline]` (code, art, audio, design, qc, balance)
- `[size]` (small, medium, large)
- `[priority]` (p0-critical, p1-high, p2-medium, p3-low)
```

### Template: Bug Issue

```markdown
# [Bug Title]

## Environment
- Build: [commit hash or version]
- Platform: [Windows/Mac/Linux/Console]
- Reproducible: [Always / Sometimes / Rarely]

## Steps to Reproduce
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happens]

## Severity
- [ ] Critical (game crash, progression blocker)
- [ ] High (major feature broken)
- [ ] Medium (feature partially broken or workaround exists)
- [ ] Low (minor visual glitch, doesn't affect gameplay)

## Video/Screenshot
[Attach proof if possible]

## Root Cause (if known)
[Optional: developer hypothesis about what's wrong]

## Blocks
- #789 (Other issues affected by this bug)
```

### Template: Design Task

```markdown
# [Design Task Title]

## Objective
What design question are we answering or what design artifact are we creating?

## Current State
[How is this currently designed/handled?]

## Success Criteria
- [ ] Criteria 1
- [ ] Criteria 2
- [ ] Criteria 3

## Open Questions
- [Question 1]
- [Question 2]

## Resources
- Reference: [Link to GDD section]
- Related: [Link to related design tasks or issues]

## Deliverables
[What does "done" look like? Design doc section? Spreadsheet? Updated GDD?]

## Depends On
- #111 (Other design decisions this depends on)
```

### Template: Art Asset Issue

```markdown
# [Asset Name]

## Specification
- **Type:** [Model / Texture / VFX / Animation / UI / Icon]
- **Resolution/Size:** [Dimensions, polygon count, frame count, etc.]
- **Deadline:** [Release date or dependent feature]
- **Priority:** [p0/p1/p2/p3]

## Reference
[Concept art, style guide, or reference images]

## Requirements
- [ ] Requirement 1
- [ ] Requirement 2
- [ ] Requirement 3

## Acceptance Criteria
- [ ] Asset matches style guide
- [ ] Asset optimized for performance (polycount, texture size, draw calls)
- [ ] Asset integrated into game (material assigned, animation rigged, etc.)

## Depends On
- #222 (Other assets or tasks this depends on)

## Integration Notes
[Where/how will this asset be used in the game?]
```

### Template: Audio Task

```markdown
# [Audio Task]

## Type
- [ ] Record/Source SFX
- [ ] Create/Compose Music
- [ ] Voice Recording
- [ ] Audio Integration
- [ ] Audio Mix

## Specification
- **Duration:** [If music, how many seconds / loops?]
- **Mood/Style:** [Describe tone and musical style]
- **Context:** [Where/when is this played?]
- **Technical Specs:** [Sample rate, format, loudness targets]

## Reference Audio
[Link to reference tracks or audio examples]

## Requirements
- [ ] Audio created/sourced
- [ ] Audio meets technical specs
- [ ] Audio integrated into engine
- [ ] Audio mixed to game standards

## Depends On
- #333 (Mechanical implementation that this audio supports)
```

### Template: Balance Pass

```markdown
# Balance Pass: [System Name]

## Scope
What subsystem are we balancing? (e.g., combat, economy, progression, specific mechanic)

## Current Metrics
[Populate from balance simulations or telemetry]
- Metric 1: Current value | Target range | Status (✅/❌)
- Metric 2: Current value | Target range | Status (✅/❌)

## Balance Targets
- [Target 1: description and acceptable range]
- [Target 2: description and acceptable range]

## Proposed Changes
- [Change 1: parameter adjustment + expected effect]
- [Change 2: parameter adjustment + expected effect]

## Testing Plan
- [ ] Run simulations with new parameters
- [ ] Compare before/after metrics
- [ ] Check for side effects on related systems
- [ ] Playtest with new parameters

## Depends On
- #444 (Mechanic implementation that must exist before balancing)

## Blocks
- #555 (Content (levels, encounters) that waits for this balance pass)

## Reference
[Link to design doc or balance simulation results]
```

## Label Taxonomy

Use consistent labels to categorize work. Each issue should have **at least one discipline label**
and **at least one priority label**.

### Discipline Labels

These categorize what type of work the issue is:

```
code          → Programming (C++, C#, Unreal, Unity, scripting)
art           → Visual assets (models, textures, VFX, animation)
audio         → Sound (SFX, music, voice, mixing)
design        → Game design (mechanics, level layout, progression)
qc            → Quality assurance (testing, bug hunting)
balance       → Balance review and tuning (numerical analysis)
ui            → User interface (menus, HUD, flows, accessibility)
docs          → Documentation (GDD sections, design docs, code docs)
infra         → Infrastructure (build system, CI/CD, tooling, pipelines)
```

### Priority Labels

These indicate urgency and importance:

```
p0-critical   → Blocks shipping, game-breaking bug, top priority
p1-high       → Important feature, should land this sprint
p2-medium     → Nice to have, can slip if needed
p3-low        → Polish, future work, low urgency
```

### Size Labels

Estimate effort (for velocity tracking and sprint planning):

```
small         → 1-2 days of focused work for one person
medium        → 3-5 days of focused work for one person
large         → 1+ weeks of focused work or multi-person effort
epic          → Major feature spanning multiple sprints (consider breaking down)
```

### Status Labels

Track non-standard work states:

```
blocked       → Work cannot proceed (waiting on external dependency)
waiting-feedback → Waiting for approval, review, or stakeholder input
technical-spike → Research task to answer open question (not shippable)
bug           → Bug fix (in addition to discipline label)
```

### System Labels

Tag issues by game system or feature area:

```
void-engine      → Void Engine (player character, core abilities)
enemy-ai         → Enemy AI and behavior
level-design     → Level layout, encounter design, progression
narrative        → Story, dialogue, lore
ui-menus         → Menu system, settings
ui-hud           → In-game HUD and overlays
economy          → Currency, loot, progression systems
balance          → Stats, tuning, fairness (in addition to balance label)
optimization     → Performance, memory, loading
accessibility   → Accessibility features
```

### Example Label Combinations

```
code, p1-high, medium, void-engine
  → High-priority programming work on the Void Engine, estimated 3-5 days

art, qc, small, balance
  → QA work verifying art assets, small task, related to balance review

design, p2-medium, waiting-feedback, level-design
  → Design work on level layout, waiting for approval, medium effort

audio, p0-critical, large, narrative
  → Audio work for narrative/story, critical to shipping, large effort

docs, p3-low, small, infra
  → Documentation of infrastructure/tooling, low priority
```

## Sprint Planning Workflow

Sprint planning happens at the start of each sprint (typically weekly or bi-weekly).

### Before Sprint Planning

1. **Groom the backlog** — ensure all issues are well-defined, estimated, and prioritized
2. **Identify blockers** — check which backlog issues are blocked by in-progress work
3. **Review capacity** — how many person-days of work can the team take on?
4. **Align on goals** — what should this sprint accomplish? (feature X, bug fixes, tech debt)

### During Sprint Planning (gh CLI steps)

```bash
# 1. List all backlog issues, not yet in a sprint
gh issue list \
  --label "p0-critical,p1-high" \
  --state open \
  --json "number,title,labels" \
  | grep -v "sprint" \
  | head -20

# 2. For each issue the team commits to, add to sprint
gh issue edit 789 --add-milestone "Sprint 5"
gh issue edit 789 --add-assignee "alice"

# 3. Verify sprint lineup (all issues have assignee, milestone, estimate)
gh issue list --milestone "Sprint 5" --json "number,assignees,labels,title"

# 4. Export sprint plan to CSV or report
gh issue list --milestone "Sprint 5" --json "number,title,labels,assignees" \
  --query '.[] | "\(.number),\(.title),\(.assignees[0].login),\(.labels[0].name)"' \
  > sprint_5_plan.csv
```

### Use sprint_planning.py helper

```bash
python scripts/sprint_planning.py \
  --repo "user/my-game" \
  --sprint "5" \
  --mode "plan" \
  --capacity "80"  # 80 person-days available this sprint
```

This script:
1. Lists all unscheduled backlog issues
2. Suggests issues to add based on priority and dependencies
3. Calculates remaining capacity as you commit issues
4. Warns about risky commitments (too much large work, unresolved blockers)
5. Exports a commit plan

### After Sprint Planning

```bash
# Lock the sprint (no more changes to committed issues)
gh issue edit 123 --lock --lock-reason "Sprint 5 locked at 2026-02-19"

# Post sprint goal + plan in team chat
python scripts/sprint_report.py --sprint "5" --format "slack" | slack send --channel "#gamedev"
```

## GDD-to-Issues Decomposition Process

Use `gdd_to_issues.py` to automate creation of issues from design decisions. The script parses
a GDD section and generates issues following the decomposition framework.

### Step 1: Write a GDD Section

Create or update a GDD markdown file with structured design decisions. Example:

```markdown
# Void Engine Abilities

## Phase Shift

The Void Engine can activate Phase Shift, warping through walls and enemies for a short
duration. This ability is the core mobility tool and puzzle solver.

### Mechanics
- **Activation:** Press [Ability 1] key / Gamepad Button
- **Duration:** 2 seconds (configurable, see balance section)
- **Cooldown:** 8 seconds (configurable)
- **Energy Cost:** 25 units (if energy system exists)
- **Effects While Phased:**
  - Player passes through solid geometry (walls, doors, obstacles)
  - Player passes through enemies (cannot collide)
  - Player cannot take damage from enemies or hazards
  - Player cannot attack, use other abilities, or interact with objects
  - Visual feedback: shimmer shader on player, audio loop while phased

### Design Notes
- Phase Shift is the **primary puzzle-solving tool**. Level design should require or
  suggest phase shifts to progress.
- Should not trivialize combat. Limited duration and cooldown prevent spam.
- Blocks level-design work until mechanics are implemented.

### Dependencies
- Requires: Ability system framework (issue #111)
- Blocks: All puzzles using Phase Shift (issues #222, #333, #444)

### Balance Notes
- Invulnerability during phase is core to fantasy, do not remove
- Cooldown tuning pending playtesting; may need longer cooldown if puzzles too easy
```

### Step 2: Run gdd_to_issues.py

```bash
python scripts/gdd_to_issues.py \
  --gdd-file "void-engine-abilities.md" \
  --feature "Phase Shift" \
  --repo "user/my-game" \
  --dry-run  # First, show what would be created without creating issues
```

Script output:

```
GDD to Issues Converter

Feature: Phase Shift
  Found feature block in void-engine-abilities.md

Would create the following issues:

[DESIGN] Phase Shift - Define mechanics
  Labels: design, p1-high, medium, void-engine
  Dependencies: #111 (Ability system framework)

[CODE] Phase Shift - Implement ability state machine
  Labels: code, p1-high, large, void-engine
  Dependencies: #111

[CODE] Phase Shift - Implement collision/phase handling
  Labels: code, p1-high, medium, void-engine
  Dependencies: [Phase Shift - Implement ability state machine]

[ART] Phase Shift - Create entry/exit VFX
  Labels: art, p1-high, medium, void-engine
  Dependencies: [Phase Shift - Implement ability state machine]

[ART] Phase Shift - Create phase shimmer shader
  Labels: art, p1-high, medium, void-engine

[ART] Phase Shift - Create ability icon
  Labels: art, p2-medium, small, void-engine

[AUDIO] Phase Shift - SFX for ability activation
  Labels: audio, p1-high, small, void-engine
  Dependencies: [Phase Shift - Implement ability state machine]

[AUDIO] Phase Shift - Audio loop for phase state
  Labels: audio, p1-high, small, void-engine
  Dependencies: [Phase Shift - Implement ability state machine]

[QC] Phase Shift - Test collision and clipping
  Labels: qc, p1-high, medium, void-engine
  Dependencies: [Phase Shift - Implement collision/phase handling]

[BALANCE] Phase Shift - Balance review and tuning
  Labels: balance, p2-medium, medium, void-engine
  Dependencies: [QC - Test collision and clipping]

Total: 10 issues | Estimated effort: 3.5 weeks (1 large + 7 medium + 2 small)
Dependencies resolved: Yes ✅

Run with --execute to create all issues.
```

### Step 3: Execute Issue Creation

```bash
# Create all issues for real
python scripts/gdd_to_issues.py \
  --gdd-file "void-engine-abilities.md" \
  --feature "Phase Shift" \
  --repo "user/my-game" \
  --execute
```

Script:
1. Creates each issue with proper body, labels, and milestone
2. Links issues via "depends on" relationships using GitHub issue relationships
3. Assigns default milestone (e.g., next sprint)
4. Returns issue numbers and links for verification

```
Created 10 issues:

#789 [DESIGN] Phase Shift - Define mechanics
  https://github.com/user/my-game/issues/789

#790 [CODE] Phase Shift - Implement ability state machine
  https://github.com/user/my-game/issues/790
  Depends on: #111
  Blocks: #791, #795, #796

#791 [CODE] Phase Shift - Implement collision/phase handling
  https://github.com/user/my-game/issues/791
  Depends on: #790
  ...
```

## Project Board Management

The project board is the single source of truth for what the team is working on. Keep it
updated in real-time.

### Board Columns (Left to Right)

```
Backlog → Sprint → In Progress → Review → Done
```

**Column Movement:**

```
Backlog
  │
  ├─ Issues created but not yet assigned to a sprint
  ├─ Acceptance criteria defined
  ├─ Dependencies identified
  └─ Ready to be pulled into a sprint
       │
       ▼
   Sprint
     │
     ├─ Assignee confirmed
     ├─ Milestone set (sprint name)
     ├─ Issues are "committed" to this sprint
     └─ Work should start within 1-2 days
          │
          ▼
      In Progress
        │
        ├─ Assignee actively working
        ├─ PR opened (if code) or work started (if art/audio/design)
        ├─ Status update every day
        └─ Move to Review when work is submittable
             │
             ▼
          Review
            │
            ├─ PR submitted for review (if code)
            ├─ QA testing in progress (if feature)
            ├─ Design awaiting approval (if design)
            ├─ Art awaiting integration (if art)
            └─ Move to Done when approved/merged
                 │
                 ▼
              Done
                │
                ├─ PR merged to main
                ├─ QA passed
                ├─ Design approved and implemented
                └─ Ready for next sprint cycle or release
```

### Automate Board Updates with board_status.py

```bash
# Run this daily or in CI/CD to auto-promote issues through the board
python scripts/board_status.py \
  --repo "user/my-game" \
  --auto-promote \
  --auto-close-done  # Move issues to Done if PR merged + CI passing

# Output includes:
# - Issues moved from In Progress → Review (work ready)
# - Issues moved from Review → Done (work approved/merged)
# - Issues at risk (in progress >3 days with no PR, no progress)
# - Blockers (issues blocking many others)
```

### Manual Board Updates (gh CLI)

```bash
# Move issue to a different column (project v2)
gh issue edit 789 --project-v2 "My Game" --column "In Progress"

# Or use project ID directly (faster)
gh issue edit 789 --project "2"

# Bulk move issues (e.g., move all done issues from current sprint to archive)
gh issue list --milestone "Sprint 5" --search "is:closed" --state closed \
  | while read issue; do
    gh issue edit $issue --project "2" --column "Done"
  done
```

### Monitor Board Health

```bash
# Issues stuck in Review > 3 days
gh issue list --state open --search "updated:<2026-02-16" --json "number,title,updatedAt" \
  | jq '.[] | select(.title | contains("Review"))'

# Unassigned issues in Sprint (should be none)
gh issue list --milestone "Sprint 5" --json "number,title,assignees" \
  | jq '.[] | select(.assignees | length == 0)'

# Blockers (issues blocking many others)
gh issue list --label "blocked" --json "number,title,body" \
  | jq '.[] | select(.body | contains("Blocks"))'
```

## Milestone Tracking

Milestones organize work into releases or big phases.

### Milestone Hierarchy

```
Version 1.0 (Major Release)
├── Sprint 1 (Week 1-2)
├── Sprint 2 (Week 3-4)
├── Sprint 3 (Week 5-6)
└── [QA/Polish/Final Release]

Version 1.1 (Minor Release)
├── Sprint 4 (Week 7-8)
└── ...
```

Or organize by feature:

```
Feature: Void Engine
├── Ability System Framework
├── Phase Shift Ability
├── Temporal Slash Ability
├── Void Engine Boss Fight
└── [Balance/QA/Shipping]
```

### Create Milestones

```bash
# Create a sprint milestone
gh milestone create \
  --title "Sprint 5" \
  --description "Void Engine abilities pt. 1" \
  --due-date "2026-03-09"

# Create a feature milestone
gh milestone create \
  --title "Feature: Void Engine" \
  --description "All Void Engine content (abilities, boss, integration)" \
  --due-date "2026-03-23"

# Assign issues to milestone
gh issue edit 789 --add-milestone "Sprint 5"

# Track milestone progress
gh milestone view "Sprint 5" --json "title,closedIssues,openIssues" \
  | jq '. | "\(.title): \(.closedIssues) done, \(.openIssues) remaining"'
```

## Sprint Report Generation

Generate comprehensive sprint status reports for team syncs, standups, or stakeholder updates.

### Generate Sprint Report

```bash
python scripts/sprint_report.py \
  --repo "user/my-game" \
  --sprint "5" \
  --format "markdown"  # or "html", "json", "slack", "csv"
```

Report template:

```markdown
# Sprint 5 Status Report

**Duration:** 2026-02-19 to 2026-03-09
**Sprint Goal:** Implement Void Engine core abilities (Phase Shift, Temporal Slash)

---

## Summary
- **Issues Completed:** 18 / 24 (75%)
- **Velocity:** 18 points (last sprint: 16 points) → +12% improvement
- **On Track:** ✅ Yes, within target velocity
- **Blockers:** 1 critical blocker

---

## Status by Discipline

### Code (Programming)
- Backlog: 2 | Sprint: 4 | In Progress: 3 | Review: 1 | Done: 7

### Art (Visual Assets)
- Backlog: 1 | Sprint: 3 | In Progress: 2 | Review: 1 | Done: 5

### Audio
- Backlog: 0 | Sprint: 2 | In Progress: 1 | Review: 0 | Done: 2

### Design
- Backlog: 1 | Sprint: 1 | In Progress: 0 | Review: 0 | Done: 1

### QC (Testing)
- Backlog: 0 | Sprint: 2 | In Progress: 1 | Review: 1 | Done: 2

### Balance
- Backlog: 0 | Sprint: 1 | In Progress: 0 | Review: 0 | Done: 0

---

## Burndown

```
24 | ███░░░░░░░
22 | ███░░░░░░░
20 | ████░░░░░░
18 | █████░░░░░  ← Current (day 5/8)
16 | ██████░░░░
14 | ███████░░░
12 | ████████░░
10 | █████████░
 8 | ██████████
   └──────────────
     D1 D2 D3 D4 D5 D6 D7 D8
```

**Interpretation:** On pace for 19-20 issues done. One issue unexpectedly complex (Phase Shift collision).

---

## Completed Issues (18)

✅ #789 [DESIGN] Phase Shift - Define mechanics
✅ #790 [CODE] Phase Shift - Implement ability state machine
✅ #791 [CODE] Phase Shift - Implement collision/phase handling
✅ #795 [ART] Phase Shift - Create entry/exit VFX
✅ #796 [ART] Phase Shift - Create phase shimmer shader
... (13 more)

---

## In Progress (7)

🔄 #792 [CODE] Temporal Slash - Implement ability (3 days in)
🔄 #797 [ART] Temporal Slash - VFX concept (2 days in)
🔄 #798 [AUDIO] Void Engine - SFX library (4 days in)
... (4 more)

---

## Blockers (1 Critical)

❌ **#800 [CODE] Collision system refactor — BLOCKING:** #791, #801, #802, #803
   - **Issue:** Current collision layer model doesn't support "phased" collision states
   - **Owner:** @charlie
   - **Status:** 80% done, expected to unblock by end of day tomorrow (2026-02-20)
   - **Mitigation:** Temporal Slash art work continues in parallel

---

## At Risk (Issues Approaching Deadline)

⚠️ #810 [QC] Temporal Slash - Full playtesting — in progress 2 days, no test results posted
   - Expected to finish by 2026-02-28, but no progress indicator
   - Recommend: Daily check-in with QA lead

---

## Metrics

| Metric | Sprint 4 | Sprint 5 (Current) | Target | Status |
|--------|----------|-------------------|--------|--------|
| **Velocity** | 16 points | 18 points | 20 points | 🟡 90% |
| **Average Issue Cycle Time** | 2.8 days | 3.1 days | <3 days | 🟡 Just over |
| **Code Review Turnaround** | 1.2 days | 1.5 days | <1 day | 🔴 Late |
| **QA Throughput** | 4 issues | 5 issues | 6 issues | 🟡 Slight backlog |

---

## Next Sprint Goals (Sprint 6)

1. Finish Void Engine abilities (Temporal Slash, complete Phase Shift balance)
2. Integrate Void Engine into boss encounter
3. Begin UX/tutorial work for Void Engine mechanics
4. Tech debt: Optimize collision system for shipping

---

## Team Notes

- **Great work:** Art team shipped high-quality VFX on schedule
- **Challenge:** Collision system is complex; estimate was 2 days, took 4
- **Suggestion:** Reserve 15-20% buffer for complex systems work in future sprints
```

### Export Sprint Report to Different Formats

```bash
# Markdown (for docs, PRs, wikis)
python scripts/sprint_report.py --sprint "5" --format "markdown" > sprint_5.md

# HTML (for email or web publishing)
python scripts/sprint_report.py --sprint "5" --format "html" > sprint_5.html

# JSON (for dashboards or data analysis)
python scripts/sprint_report.py --sprint "5" --format "json" > sprint_5.json

# Slack markdown (for team channel)
python scripts/sprint_report.py --sprint "5" --format "slack" | \
  curl -X POST -d @- https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK
```

## Label Taxonomy Reference

### All Available Labels (Organized by Category)

**Discipline Labels:**
- `code` — Programming
- `art` — Visual assets
- `audio` — Sound
- `design` — Game design
- `qc` — Quality assurance
- `balance` — Balance review
- `ui` — User interface
- `docs` — Documentation
- `infra` — Infrastructure

**Priority Labels:**
- `p0-critical` — Game-breaking, top priority
- `p1-high` — Important, should this sprint
- `p2-medium` — Nice to have
- `p3-low` — Polish, low urgency

**Size Labels:**
- `small` — 1-2 days
- `medium` — 3-5 days
- `large` — 1+ weeks

**Status Labels:**
- `blocked` — Cannot proceed
- `waiting-feedback` — Waiting for input
- `technical-spike` — Research task
- `bug` — Bug fix

**System Labels:**
- `void-engine` — Void Engine (protagonist)
- `enemy-ai` — Enemy behavior
- `level-design` — Level layout
- `narrative` — Story
- `ui-menus` — Menus
- `ui-hud` — HUD
- `economy` — Currency/loot
- `optimization` — Performance
- `accessibility` — Accessibility features

**Example issue with all label types:**

```bash
gh issue create \
  --title "Phase Shift - Implement ability state machine" \
  --label "code,p1-high,large,void-engine"
```

## gh CLI Cheat Sheet

Common commands for issue and project management:

```bash
# ========== LIST & SEARCH ==========

# List open issues
gh issue list --state open

# List by label
gh issue list --label "code,p1-high"

# List by milestone
gh issue list --milestone "Sprint 5"

# List by assignee
gh issue list --assignee "alice"

# List closed issues (completed work)
gh issue list --state closed --limit 50

# ========== CREATE & EDIT ==========

# Create issue with title and labels
gh issue create --title "Task title" --label "code,p1-high,medium"

# Create with body (use heredoc for multi-line)
gh issue create --title "Title" --body "$(cat <<'EOF'
## Summary
Details here

## Acceptance Criteria
- [ ] Item 1
- [ ] Item 2
EOF
)"

# Create with milestone and project
gh issue create --title "Title" --milestone "Sprint 5" --project "My Game"

# Edit issue (add labels)
gh issue edit 789 --add-label "code,large"

# Edit issue (set milestone)
gh issue edit 789 --add-milestone "Sprint 5"

# Edit issue (assign to person)
gh issue edit 789 --add-assignee "alice"

# ========== RELATIONSHIPS ==========

# View issue with all details
gh issue view 789

# View issue as JSON (parse with jq)
gh issue view 789 --json "number,title,labels,assignees,milestone,body"

# Link issues (issue 789 depends on 456)
gh issue edit 789 --add-body "Depends on #456"

# ========== PROJECT BOARD ==========

# View all issues in a project (project v2)
gh issue list --project "My Game"

# Move issue to column in project board
gh issue edit 789 --project "My Game" --column "In Progress"

# ========== FILTERING ==========

# Complex filter example
gh issue list \
  --state open \
  --label "code,p0-critical,p1-high" \
  --milestone "Sprint 5" \
  --assignee "alice" \
  --json "number,title,labels" \
  --jq '.[] | select(.title | contains("ability")) | "\(.number): \(.title)"'

# Issues updated in last 3 days
gh issue list --search "updated:>2026-02-16"

# Issues with no assignee
gh issue list --assignee "@none"

# ========== BULK OPERATIONS ==========

# Bulk assign issues
gh issue list --milestone "Sprint 5" --state open | while read issue; do
  gh issue edit $issue --add-assignee "alice"
done

# Bulk label issues
for i in 789 790 791; do
  gh issue edit $i --add-label "code,void-engine"
done

# ========== EXPORT & REPORTING ==========

# Export as CSV
gh issue list --milestone "Sprint 5" \
  --json "number,title,assignees,labels" \
  --jq '.[] | [.number, .title, .assignees[0].login, .labels[0].name] | @csv' \
  > sprint_5.csv

# Export as JSON
gh issue list --milestone "Sprint 5" --json "number,title,labels,assignees" > sprint_5.json
```

## Scripts Reference

All scripts are in `scripts/` and can be run from the repository root.

### gdd_to_issues.py

Convert a GDD section into GitHub issues with proper decomposition.

```bash
python scripts/gdd_to_issues.py \
  --gdd-file "path/to/gdd-section.md" \
  --feature "Feature Name" \
  --repo "owner/repo" \
  --dry-run  # Preview without creating
  --execute  # Actually create issues
```

**Input:** Markdown file with design decision blocks
**Output:** GitHub issues (code, art, audio, design, qc, balance) with labels and dependencies

### board_status.py

Automate board column movement based on PR status, completion, etc.

```bash
python scripts/board_status.py \
  --repo "owner/repo" \
  --auto-promote     # Move In Progress → Review if PR linked and CI passing
  --auto-close-done  # Move Review → Done if PR merged
  --report           # Print status summary
```

**Output:** Issues moved, blockers identified, at-risk issues flagged

### sprint_report.py

Generate comprehensive sprint status reports.

```bash
python scripts/sprint_report.py \
  --repo "owner/repo" \
  --sprint "5" \
  --format "markdown"  # Options: markdown, html, json, slack, csv
  --output "report.md" # Optional: write to file instead of stdout
```

**Output:** Sprint summary, velocity, burndown, status by discipline, blockers, completed issues

### sprint_planning.py

Assist with sprint planning: estimate, capacity planning, dependency check.

```bash
python scripts/sprint_planning.py \
  --repo "owner/repo" \
  --sprint "5" \
  --mode "plan"       # Options: plan, validate, forecast
  --capacity "80"     # Available person-days for sprint
```

**Output:** Sprint plan suggestions, capacity utilization, risky commitments flagged

## Integration with Other Skills

### From gdd-manager

When gdd-manager routes design work to you:
1. You receive design decision(s) from GDD sections
2. Use `gdd_to_issues.py` to decompose and create issues
3. Return issue links for gdd-manager to reference in its routing/consistency checks

### From systems-designer, narrative-designer, level-designer, etc.

When specialist designers complete design work:
1. They describe mechanics, narrative, level changes
2. You decompose into issues and track in GitHub
3. You report back velocity and burndown to help estimate remaining work

### From game-balancer

When game-balancer identifies balance changes:
1. You create balance pass issues with specific parameter changes
2. Link to code/art issues that depend on the balance
3. Track balance issues through Review until playtesting confirms tuning

### To data-modeler, gdd-writer, pitch-deck

When exporting game design:
1. You provide issue completion status and metrics
2. Data-modeler queries GitHub for parameter tables to export to spreadsheet
3. gdd-writer pulls completed design issues to update GDD
4. pitch-deck queries GitHub for progress snapshots

## Output Format

**When asked for project status:** Provide sprint report with velocity, burndown, blockers

**When asked to create issues:** Provide links to created issues and summary

**When asked for next steps:** List issues in "Sprint" column ranked by priority

**When asked about team capacity:** Run sprint_planning.py and report available person-days

## Example Full Workflow

### Example: "Convert the Phase Shift design into trackable work"

```bash
# 1. Parse the design (in gdd-manager context, you receive the GDD section)
# GDD section: void-engine-abilities.md with "## Phase Shift" section

# 2. Use gdd_to_issues.py to decompose
python scripts/gdd_to_issues.py \
  --gdd-file "void-engine-abilities.md" \
  --feature "Phase Shift" \
  --repo "user/my-game" \
  --dry-run

# 3. Review the proposed issues (dry-run output shows ~10 issues)

# 4. Execute issue creation
python scripts/gdd_to_issues.py \
  --gdd-file "void-engine-abilities.md" \
  --feature "Phase Shift" \
  --repo "user/my-game" \
  --execute

# 5. Assign to sprint and team members (during sprint planning)
gh issue edit 789 --add-milestone "Sprint 5" --add-assignee "alice"
gh issue edit 790 --add-milestone "Sprint 5" --add-assignee "bob"
# ... for all 10 issues

# 6. Move to "Sprint" column on board
for i in 789 790 791 792 793 794 795 796 797 798; do
  gh issue edit $i --project "My Game" --column "Sprint"
done

# 7. Daily: Check board status
python scripts/board_status.py --repo "user/my-game" --report

# 8. End of sprint: Generate report
python scripts/sprint_report.py --repo "user/my-game" --sprint "5" --format "markdown"
```

## Best Practices

1. **Issues should be assignable to one person** — if an issue needs 2+ people, break it down
2. **Estimate before committing to a sprint** — size labels prevent overcommit
3. **Link related issues** — helps identify dependencies early
4. **Update issues daily** — move columns, add progress comments, surface blockers
5. **Close issues when work ships** — don't let done work linger in "Review"
6. **Review board health weekly** — burndown, blockers, at-risk items
7. **Retrospect on estimates** — if estimates are consistently wrong, calibrate
8. **Keep labels consistent** — discipline + priority + size at minimum
9. **Use milestones for releases** — easier to track progress toward shipping
10. **Automate what you can** — board_status.py, sprint_report.py save time

---

**Last Updated:** 2026-02-19
**Skill Maintainer:** GitHub GameDev Team
