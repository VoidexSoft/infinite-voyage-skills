# Cross-Reference Consistency Rules

Rules for validating that GDD sections are internally consistent. Use these
rules with `scripts/consistency_check.py` to detect contradictions and gaps.

---

## Consistency Rule Categories

### Category 1: Mechanic-Economy Consistency

Every mechanic that involves resources must align with the economy section.

| Rule ID | Check | Sections Involved |
|---------|-------|-------------------|
| ME-01 | Every currency referenced in mechanics is defined in economy section | 3 → 5 |
| ME-02 | Every reward in level design has a corresponding economy entry | 6 → 5 |
| ME-03 | Crafting costs in mechanics match pricing in economy | 3 → 5 |
| ME-04 | Loot tables reference only items defined in mechanics/economy | 5 → 3 |
| ME-05 | Shop prices are achievable within target play time | 5 → 12 |

**Example violation**:
```
Section 3 (Combat): "Defeating a boss awards 500 Starlight Crystals"
Section 5 (Economy): [No definition of Starlight Crystals]
→ Rule ME-01 VIOLATION: Undefined currency referenced
```

---

### Category 2: Narrative-Content Consistency

Story elements must match the content they appear in.

| Rule ID | Check | Sections Involved |
|---------|-------|-------------------|
| NC-01 | Every named NPC in dialogue has a character profile | 4 → 4 |
| NC-02 | Quest prerequisites match level design's unlock conditions | 4 → 6 |
| NC-03 | Lore references are internally consistent (no contradictions) | 4 → 4 |
| NC-04 | Zone narrative hooks match level design's zone specs | 4 → 6 |
| NC-05 | Character motivations don't contradict their actions in quests | 4 → 4 |

**Example violation**:
```
Section 4 (Quest): "Speak to Captain Voss in the Starport"
Section 6 (Level Design): [Captain Voss not placed in Starport zone]
→ Rule NC-04 VIOLATION: NPC placement doesn't match quest requirement
```

---

### Category 3: Mechanic-UI Consistency

Every mechanic must have a corresponding UI representation.

| Rule ID | Check | Sections Involved |
|---------|-------|-------------------|
| MU-01 | Every player-facing stat has a UI display element | 3 → 7 |
| MU-02 | Every mechanic input is covered in the input mapping | 3 → 7 |
| MU-03 | Status effects have visual indicators defined | 3 → 7 |
| MU-04 | Tutorial covers all core verbs | 2 → 7 |
| MU-05 | Menu screens exist for every player-accessible system | 3 → 7 |

---

### Category 4: Balance-Parameter Consistency

All balance-relevant values must be properly defined and referenced.

| Rule ID | Check | Sections Involved |
|---------|-------|-------------------|
| BP-01 | Every stat formula references only defined parameters | 3 → 3 |
| BP-02 | Parameter ranges are specified (not just single values) | 3 → 7 |
| BP-03 | Level scaling curves cover the full level range | 5 → 3 |
| BP-04 | Difficulty targets match TTK/DPS ranges in balance docs | 6 → 12 |
| BP-05 | Enemy stats exist for every enemy type in level design | 3 → 6 |

---

### Category 5: Art-Technical Consistency

Visual requirements must be feasible within technical constraints.

| Rule ID | Check | Sections Involved |
|---------|-------|-------------------|
| AT-01 | Polygon budgets don't exceed platform limits | 8 → 10 |
| AT-02 | Texture memory fits within target hardware specs | 8 → 10 |
| AT-03 | Animation counts are feasible for timeline | 8 → 10 |
| AT-04 | VFX requirements don't exceed particle budget | 8 → 10 |
| AT-05 | Audio file sizes fit within storage budget | 9 → 10 |

---

### Category 6: Pillar Alignment

All design decisions should trace back to a design pillar.

| Rule ID | Check | Sections Involved |
|---------|-------|-------------------|
| PA-01 | Each mechanic serves at least one design pillar | 3 → 1 |
| PA-02 | Content design reflects the stated tone/theme | 6 → 1 |
| PA-03 | Monetization doesn't contradict player experience pillars | 11 → 1 |
| PA-04 | Art direction matches stated aesthetic goals | 8 → 1 |
| PA-05 | No section contradicts a stated design pillar | All → 1 |

---

## Automated Consistency Check Format

The `scripts/consistency_check.py` script checks for these patterns and reports
violations in this format:

```json
{
  "violations": [
    {
      "rule_id": "ME-01",
      "severity": "error",
      "source_section": "03-mechanics/combat.md",
      "target_section": "05-economy-progression.md",
      "description": "Currency 'Starlight Crystals' referenced but not defined",
      "line": 47,
      "suggestion": "Add Starlight Crystals definition to economy section"
    }
  ],
  "warnings": [
    {
      "rule_id": "PA-01",
      "severity": "warning",
      "source_section": "03-mechanics/crafting.md",
      "description": "Crafting system does not reference any design pillar",
      "suggestion": "Add pillar justification or reconsider if this system is needed"
    }
  ],
  "summary": {
    "total_checks": 142,
    "passed": 135,
    "errors": 4,
    "warnings": 3
  }
}
```

### Severity Levels

| Level | Meaning | Action Required |
|-------|---------|-----------------|
| **error** | Direct contradiction between sections | Must fix before implementation |
| **warning** | Potential inconsistency or missing reference | Should investigate and resolve |
| **info** | Suggestion for improvement | Optional but recommended |

---

## Manual Consistency Review Process

For deeper review beyond automated checks:

### Step 1: Cross-Reference Walk

Pick any entity (enemy, item, mechanic, NPC) and trace it through all sections:

```
Entity: "Shield Generator" (item)
├── Section 3: Mechanics spec? [Check]
├── Section 5: Economy (price, drop source)? [Check]
├── Section 6: Where does it drop? [Check]
├── Section 7: UI representation? [Check]
├── Section 8: Art asset defined? [Check]
└── Section 9: SFX for activation? [Check]
```

### Step 2: Dependency Verification

For each section, verify its dependencies are up to date:

```
Section 5 (Economy) depends on:
├── Section 3: Item list (are all items priced?) [Verify]
├── Section 6: Loot tables (do sources exist?) [Verify]
└── Section 11: Monetization (no P2W?) [Verify]
```

### Step 3: Number Audit

Check that numerical values are consistent:

```
Section 3: "Boss has 10,000 HP"
Section 6: "Boss fight target: 3 minutes"
Balance check: Player DPS needed = 10000 / 180 = 55.6 DPS
Section 5: "Player DPS at boss level: 40-70 DPS"
→ Consistent (55.6 falls within 40-70 range) ✅
```

---

## Common Inconsistency Patterns

| Pattern | Description | How to Catch |
|---------|-------------|-------------|
| **Orphan entity** | Item/NPC/mechanic referenced but never defined | Cross-reference walk |
| **Stale reference** | Section references outdated values after a change | Dependency verification |
| **Number mismatch** | Two sections cite different values for the same parameter | Number audit |
| **Missing UI** | Mechanic exists but has no player-facing interface | MU rules check |
| **Pillar drift** | Feature doesn't serve any design pillar | PA rules check |
| **Economy leak** | Currency source with no corresponding sink | ME rules check |
