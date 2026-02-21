# GDD Writing Style Guide

Standards for clear, professional, and unambiguous game design documentation for
game development projects.

---

## 1. Voice & Tense

### Use Active Voice

Active voice makes responsibilities and behaviors explicit. Passive voice hides
the actor and introduces ambiguity about who or what performs an action.

| Bad (Passive) | Good (Active) |
|---|---|
| The enemy is damaged by the player. | The player damages the enemy. |
| Experience points are awarded when a quest is completed. | The system awards experience points when the player completes a quest. |
| Items can be equipped from the inventory screen. | The player equips items from the inventory screen. |

### Use Present Tense

GDDs describe how the game works, not how it will work. Present tense signals
that the design is the current specification.

| Bad (Future) | Good (Present) |
|---|---|
| The player will be able to fast-travel. | The player fast-travels between discovered waypoints. |
| Enemies will drop loot upon death. | Enemies drop loot upon death. |
| The HUD will show remaining health. | The HUD displays remaining health. |

Exception: Roadmap sections and planned features may use future tense when
describing work not yet designed. Mark those sections with a "[PLANNED]" tag.

---

## 2. Specificity Over Vagueness

### Quantify Everything

Vague descriptions generate conflicting interpretations across disciplines.
Provide exact numbers, ranges, or formulas.

| Vague | Specific |
|---|---|
| The sword does a lot of damage. | The Iron Sword deals 24 base damage per hit. |
| Enemies spawn frequently. | The spawner creates 3 enemies every 15 seconds. |
| The cooldown is short. | The ability has a 4-second cooldown. |
| Health regenerates slowly. | Health regenerates at 2 HP per second out of combat. |
| The map is large. | The world map spans 4 km x 4 km of traversable terrain. |

### Name Things Precisely

Use the canonical name for every system, item, character, and mechanic. Define
names in the glossary and use them identically everywhere.

| Inconsistent | Consistent |
|---|---|
| "health", "HP", "hit points", "life" | "Health" (always capitalized, always this word) |
| "the shop", "vendor", "merchant NPC" | "Merchant" (defined in glossary) |
| "XP", "experience", "exp" | "XP" (abbreviation defined in glossary) |

---

## 3. Measurable Descriptions

When describing game feel, player experience, or pacing, anchor descriptions
to measurable criteria that engineers and QA can verify.

### Bad: Subjective Only

> "Combat should feel fast and exciting."

### Good: Measurable + Subjective Context

> "Combat encounters last 30-90 seconds on average. The player performs at least
> one action every 2 seconds. The target sensation is urgency: players should
> feel time pressure without feeling overwhelmed. If average encounter length
> exceeds 120 seconds in playtesting, revisit enemy health values."

### Template for Measurable Descriptions

```
[Feature] targets [quantitative metric].
The intended player experience is [subjective description].
Success criteria: [testable condition].
If [failure condition], adjust [specific parameter].
```

---

## 4. Avoiding Ambiguity

### Eliminate Weasel Words

Remove words that sound meaningful but convey no information:

- "various" -- list them instead
- "several" -- give the exact count
- "etc." -- finish the list or write "including X, Y, and Z"
- "somehow" -- describe the mechanism
- "fairly", "quite", "somewhat" -- quantify or remove
- "might", "could", "may" -- decide and state definitively
- "as needed" -- define the conditions
- "TBD" -- acceptable only with an owner and deadline: "[TBD - Sarah, March 15]"

### Resolve "It Depends" Situations

If behavior varies by context, enumerate every case:

```
Damage Calculation:
- Melee attacks: base_damage * (1 + strength_modifier)
- Ranged attacks: base_damage * (1 + dexterity_modifier) * distance_falloff
- Magic attacks: base_damage * (1 + intelligence_modifier) - target_resistance
```

### One Statement Per Sentence

Compound sentences with multiple mechanics invite misreading. Split them.

| Bad | Good |
|---|---|
| The player attacks the enemy and if the enemy dies it drops loot and the player gains XP and the quest updates. | The player attacks the enemy. On death, the enemy drops loot. The player gains XP. The quest log updates to reflect the kill. |

---

## 5. Section Structure Conventions

### Standard Section Template

Every GDD section follows this skeleton:

```markdown
## [Number] [Section Title]

**Status:** [Concept | Draft | Review | Final]
**Owner:** [Name]
**Last Updated:** [Date]

### Overview
One paragraph summarizing what this section covers and why it matters.

### Details
The full specification. Use sub-headings, tables, and bullet lists.

### Rules & Constraints
Numbered list of hard rules the implementation must follow.

### Edge Cases
What happens in unusual situations? Enumerate them.

### Dependencies
Which other sections does this depend on? List cross-references.

### Open Questions
Numbered list of unresolved design questions with assigned owners.
```

### Heading Hierarchy

- **Heading 1** -- Chapters (1. High Concept, 2. Gameplay)
- **Heading 2** -- Sections (2.1 Core Mechanics)
- **Heading 3** -- Sub-sections (2.1.1 Attack Types)
- **Heading 4** -- Detail blocks within sub-sections

Never skip a level (do not go from H1 to H3).

### Numbering Convention

Use decimal numbering aligned to the heading hierarchy:

```
1. High Concept
  1.1 Logline
  1.2 Setting
    1.2.1 Geography
    1.2.2 History
2. Gameplay
  2.1 Core Mechanics
```

---

## 6. Cross-Referencing

### Internal References

When one section depends on or references another, use explicit
cross-references with the section number:

> "The Merchant sells items from the Equipment Table (see Section 6.3
> Equipment & Progression)."

### Reference Format

```
(see Section [Number] [Title])
```

Always include both the number and the title so the reference survives
reordering.

### Dependency Direction

State dependencies explicitly:

> "This section depends on Section 6.4 Economy Model for pricing data."

> "Section 7.2 Progression Curve consumes the XP tables defined here."

---

## 7. Version Control Notes

### Document Versioning Scheme

```
Major.Minor

Major: Increments on structural changes (new chapters, reorganization)
Minor: Increments on content updates within existing structure

Examples:
  0.1 -- Initial outline, section titles only
  0.5 -- First draft of all sections
  1.0 -- First complete review-ready version
  1.1 -- Post-review revisions
  2.0 -- Major restructure after vertical slice feedback
```

### Change Log Entry Format

```
| Version | Date       | Author       | Changes                              |
|---------|------------|--------------|--------------------------------------|
| 1.2     | 2025-03-15 | Sarah Chen   | Updated combat formulas in Sec 2.3   |
| 1.1     | 2025-03-01 | Marcus R.    | Added economy balance tables Sec 6.4 |
| 1.0     | 2025-02-15 | Design Team  | Initial complete version              |
```

### Tracking Changes Within Sections

Use inline markers for recent changes so reviewers can spot updates:

```
[ADDED v1.2] The parry window is 200ms, reduced from 300ms.
[CHANGED v1.2] Base enemy health increased from 80 to 100.
[REMOVED v1.2] Removed the stagger mechanic from basic attacks.
```

Remove these markers after two version increments to avoid clutter.

---

## 8. Formatting Conventions

### Tables Over Prose for Data

Whenever you have structured data (stats, item lists, progression curves),
use a table. Tables are scannable; paragraphs are not.

### Bullet Lists for Requirements

Use bullet lists when listing requirements, features, or constraints. Each
bullet is one testable statement.

### Bold for Key Terms

Bold the first occurrence of a defined term in each section:

> "The **Starship** is the player's primary mode of interstellar travel."

### Code Blocks for Formulas

```
damage = base_damage * (1 + modifier) * critical_multiplier
```

### Callout Boxes for Warnings

> **DESIGN NOTE:** This mechanic is intentionally simple for the vertical
> slice. Post-milestone, expand with elemental types and combo chains.

> **TECH CONSTRAINT:** The spawner cannot exceed 50 active entities due to
> physics engine limitations. See Section 8.2 Performance Targets.

---

## 9. Examples: Good vs. Bad GDD Writing

### Example 1: Describing a Mechanic

**Bad:**
> "Players can craft things. There are various recipes and some are harder
> than others. Crafting takes some time and uses materials the player has
> collected. The crafted items can be pretty powerful."

**Good:**
> "The Crafting System allows the player to combine Materials into Equipment
> at any Workbench. Each recipe requires 2-5 specific Materials and a minimum
> Crafting Skill level (see Section 6.2 Ability/Skill System). Crafting time
> ranges from 5 seconds (common items) to 30 seconds (legendary items).
> Crafted Equipment has a 15% stat bonus over equivalent looted Equipment,
> incentivizing engagement with the system."

### Example 2: Describing Progression

**Bad:**
> "The player gets stronger over time by leveling up and finding better gear.
> There are lots of levels and the difficulty scales accordingly."

**Good:**
> "The player progresses through 50 levels. Each level grants 3 Attribute
> Points and 1 Skill Point. Attribute Points allocate to Strength, Dexterity,
> Intelligence, or Vitality (see Appendix C for stat growth tables). Enemy
> difficulty scales by zone, not by player level: Zone 1 enemies are levels
> 1-10, Zone 2 enemies are levels 8-18, creating a 2-level overlap that
> provides a difficulty buffer. The player reaches Level 50 in approximately
> 40-50 hours of gameplay."

### Example 3: Describing UI

**Bad:**
> "The inventory shows the player's items. It should be easy to use and
> look nice."

**Good:**
> "The Inventory Screen displays the player's carried items in a grid layout
> (6 columns x 8 rows, 48 slots maximum). Each slot shows the item icon,
> rarity border color (Common=grey, Rare=blue, Epic=purple, Legendary=gold),
> and stack count for consumables. The player sorts items by Type, Rarity,
> or Recent via toggle buttons in the top-right corner. Equipping an item
> requires dragging it to the corresponding Equipment Slot on the character
> silhouette (left panel). Tooltips appear on hover after 300ms delay,
> showing item name, stats, flavor text, and sell value."

---

## 10. Checklist Before Submitting a Section

Use this checklist before marking any section as "Review" status:

- [ ] All values are specific numbers, not vague qualifiers
- [ ] Active voice is used throughout
- [ ] Present tense is used (except roadmap items)
- [ ] Every system, item, and mechanic uses its canonical name
- [ ] Cross-references include both section number and title
- [ ] No weasel words remain (various, several, etc., somehow)
- [ ] Open questions have assigned owners and deadlines
- [ ] Tables are used for structured data instead of paragraphs
- [ ] Formulas use code blocks
- [ ] Status, Owner, and Last Updated fields are current
- [ ] Edge cases are enumerated
- [ ] Dependencies are listed
