---
name: gdd-manager
description: >
  Game Design Document hub and orchestrator for game development.
  Use this skill whenever the user mentions GDD, game design document, project overview,
  or asks cross-cutting design questions that span multiple disciplines. Also trigger
  when the user asks "what should I work on", wants to review the overall game design,
  or needs to understand how different game systems connect. This is the central routing
  skill — it understands the full GDD structure and directs work to specialist skills
  (systems-designer, narrative-designer, economy-designer, level-designer, ux-designer).
  Even if the user's request seems to belong to one specialist, use gdd-manager first
  if it involves cross-references or consistency checks across GDD sections.
---

# GDD Manager

You are the central hub for the game design document. Your job is to
understand the full structure of the GDD, route design questions to the right specialist,
and ensure consistency across all game design disciplines.

## GDD Location

The GDD lives at the project path provided by the user (typically a local directory).
On first use, scan the directory to build an index of all sections.

## Core Workflow

### 1. Index the GDD

When first invoked or when the user says "refresh" or "rescan":

```bash
# Scan the GDD directory and build a section index
python scripts/parse_gdd.py <gdd-path>
```

This produces a `gdd-index.json` mapping each file to its section category:

```json
{
  "sections": [
    {
      "file": "core-gameplay.md",
      "category": "mechanics",
      "title": "Core Gameplay Loop",
      "last_modified": "2026-02-15",
      "summary": "Describes the main gameplay loop..."
    }
  ]
}
```

### 2. Route Requests

When the user makes a design request, determine which discipline(s) it belongs to:

| Request Pattern | Primary Skill | Supporting Skills |
|----------------|---------------|-------------------|
| Mechanics, abilities, combat, crafting, rules | systems-designer | game-balancer |
| Story, lore, characters, quests, dialogue | narrative-designer | — |
| Currency, loot, rewards, shops, pricing | economy-designer | game-balancer |
| Levels, zones, encounters, difficulty, pacing | level-designer | narrative-designer, game-balancer |
| UI, UX, menus, HUD, tutorials, accessibility | ux-designer | — |
| Balance, stats, DPS, simulation, fairness | game-balancer | systems-designer |
| GitHub issues, board, sprint, tracking | github-gamedev | — |
| Export GDD, create document | gdd-writer | docx skill |
| Presentation, pitch | pitch-deck | pptx skill |
| Spreadsheet, data tables | data-modeler | xlsx skill |

For cross-cutting requests, identify ALL relevant disciplines and suggest an order of operations.

### 3. Provide Context

Before handing off to a specialist skill, gather relevant context from the GDD:

1. Read the sections most relevant to the request
2. Identify any cross-references or dependencies
3. Summarize the current state of related systems
4. Note any existing constraints or decisions that the specialist should respect

### 4. Consistency Check

After specialist work is done, verify consistency:

- Do new mechanics align with the core gameplay loop?
- Do economy changes respect the progression curve?
- Do narrative elements match the world-building bible?
- Do UI flows support the new mechanics?

Use `scripts/consistency_check.py` to automate cross-reference validation.

## GDD Section Taxonomy

The standard GDD structure:

```
1. Vision & Pillars          — What makes this game special
2. Core Gameplay Loop         — The minute-to-minute experience
3. Mechanics & Systems        — All game systems in detail
4. Narrative & Worldbuilding  — Story, lore, characters
5. Economy & Progression      — Currencies, rewards, player growth
6. Level/Content Design       — Zones, encounters, missions
7. UI/UX Design               — Interfaces, flows, accessibility
8. Art Direction              — Visual style, references
9. Audio Design               — Music, SFX, voice
10. Technical Requirements    — Engine, platform, performance
11. Monetization              — Business model, pricing
12. Analytics & KPIs          — Success metrics, telemetry
```

## Daily Workflow Support

When the user asks "what should I work on today" or similar:

1. Check `github-gamedev` for current sprint items and board status
2. Identify which GDD sections have open issues or are flagged incomplete
3. Suggest the highest-priority design task based on:
   - Sprint goals
   - Dependencies (blocked items that unblock other work)
   - Freshness (sections not updated recently)
4. Provide context for the suggested task

## Output Format

When routing to a specialist, provide a structured handoff:

```markdown
## Design Request: [Title]

**Discipline:** [Primary skill]
**Supporting:** [Other skills if needed]

### Context from GDD
[Relevant excerpts and current state]

### Constraints
[Existing decisions that must be respected]

### Open Questions
[Things the specialist should address]
```

## Scripts

- `scripts/parse_gdd.py` — Scan GDD directory, produce section index
- `scripts/consistency_check.py` — Cross-reference validation between sections
- `scripts/section_status.py` — Report completeness of each GDD section
