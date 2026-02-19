# Infinite Voyage GDD — Change Log v1.0 → v1.1

## Summary

Version 1.1 reflects the design review held on 2026-02-03 with the full leads team.
Changes focus on combat rebalancing, narrative branching revisions, and newly drafted
multiplayer co-op specification. Several sections have been promoted from Concept to Draft.

---

## Changes by Section

### 2.3 Combat — Turn-Based Tactical
- **Type:** Revision (major)
- **Author:** Marcus Rodriguez
- **Details:**
  - Replaced fixed 2-action-per-turn system with flexible Action Point (AP) pool (6 AP per turn).
  - Light attacks cost 2 AP, heavy attacks cost 4 AP, abilities cost 3-5 AP.
  - Added Overwatch mechanic: spend remaining AP to react during enemy turn.
  - Removed "Combo Chain" system (moved to cut-features backlog).
  - Updated damage formula: `base_dmg * (1 + skill_bonus) * element_multiplier`.

### 3.2 Characters — Crew Roster & NPCs
- **Type:** Addition
- **Author:** Jessica Park
- **Details:**
  - Added two new crew members: Dr. Yuki Tanaka (xenobiologist) and Kael Drift (smuggler pilot).
  - Revised loyalty mission triggers: now tied to story act progression instead of arbitrary thresholds.
  - Added NPC faction reputation table showing how crew reacts to faction standing.

### 3.4 Narrative Flow — Three-Act Structure
- **Type:** Revision (minor)
- **Author:** Jessica Park
- **Details:**
  - Act 2 branching paths reduced from 5 to 3 for scope management.
  - Added "Point of No Return" warning system before Act 3 lock-in.
  - Clarified ending conditions: 4 distinct endings based on faction alignment + crew loyalty.

### 6.2 Ability System — Xenotech Augments
- **Type:** Revision (minor)
- **Author:** Marcus Rodriguez
- **Details:**
  - Augment slots increased from 3 to 4 per character.
  - Added augment synergy bonuses when equipping augments from the same Precursor set.
  - Rebalanced cooldown timers: short (2 turns), medium (4 turns), long (6 turns).

### 6.4 Economy Model — Credits & Barter
- **Type:** Revision (minor)
- **Author:** Marcus Rodriguez
- **Details:**
  - Increased baseline quest reward from 150 to 200 credits.
  - Added barter skill check: Charisma modifier affects buy/sell prices by +/- 15%.
  - Removed credit-sink "luxury cabin upgrade" (player feedback: felt unrewarding).

### 9.1 Co-op Mode — 2-Player Expedition
- **Type:** New section (promoted from Concept to Draft)
- **Author:** Amir Patel
- **Details:**
  - Defined co-op as drop-in/drop-out with tethered exploration radius (500m).
  - Host player controls narrative decisions; guest receives "advisor" dialogue options.
  - Loot is instanced per player; quest progress syncs to host save.
  - Added latency tolerance spec: playable up to 150ms round-trip.

### 9.2 Asynchronous Features — Expedition Logs
- **Type:** New section (promoted from Concept to Draft)
- **Author:** Amir Patel
- **Details:**
  - Players can leave "Expedition Logs" (text + screenshot) at discovered locations.
  - Other players find logs as collectibles; upvoting increases visibility.
  - No direct player interaction — fully asynchronous, similar to Dark Souls messages.

### 12.2 Milestone Schedule
- **Type:** Revision (minor)
- **Author:** Sarah Chen
- **Details:**
  - Vertical Slice milestone moved from 2026-06-01 to 2026-07-15 (combat rework buffer).
  - Added new milestone: "Co-op Prototype" at 2026-09-01.
  - Alpha target remains 2027-03-01.

---

## Sections Unchanged in v1.1

- 1. High Concept (all subsections)
- 2.1 Core Loop
- 2.2 Progression System
- 2.4 Victory Conditions & Endings
- 3.1 Story Overview
- 3.3 Dialogue System & Tone
- 4. Art & Visuals (all subsections)
- 5. Audio & Music (all subsections)
- 6.1 Inventory System
- 6.3 Equipment & Crafting
- 7. Level Design (all subsections)
- 8. Technical Specifications (all subsections)
- 10. Monetization & Live Service (all subsections)
- 11. Accessibility & Localization (all subsections)
- 12.1 Team Structure & Roles
- 12.3 Risk Register
- 12.4 Budget Overview
