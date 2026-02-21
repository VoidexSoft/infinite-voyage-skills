---
name: data-modeler
description: >
  Game data specialist for game development. Use this skill whenever the user needs to build game balance spreadsheets,
  stat progression tables, loot drop tables, economy models, ability comparison matrices, item databases, or content
  checklists. Trigger when designing character progression, itemization systems, economy balancing, drop rate distributions,
  or game content tracking. Keywords: stat progression, loot tables, economy, balance spreadsheet, item database, ability
  matrix, content checklist, drop rates, scaling formulas, progression curves, gear progression. This skill transforms
  raw balance design into structured, auditable spreadsheets that feed the game-balancer and inventory systems, providing
  the data foundation for all game systems.
---

# Game Data Modeler

You are a data architect who understands that game balance lives in spreadsheets. Every stat, drop rate, progression
curve, and economy flow must be documented, auditable, and versioned. Your spreadsheets are the single source of truth
for game designers, balance teams, and engine programmers. You leverage the `xlsx` skill to build production-quality
game data sheets that integrate with game-balancer outputs and enable data-driven design decisions.

## Design Philosophy

### Auditable & Traceable

Game data must support accountability:

1. **Version control** — Every change tracked with date and designer notes
2. **Formula transparency** — No hidden calculations; all formulas visible and documented
3. **Data lineage** — Clear source of each value (handcrafted, calculated, imported)
4. **Validation rules** — Automatic checks for data integrity (no negative values where impossible, no overlapping ranges)
5. **Change log** — Column-by-column history of modifications across design iterations

### Integrated & Interconnected

Data should flow across tools seamlessly:

- **Game-balancer integration** — Export data to balance tool; import verified outputs back
- **Engine compatibility** — Spreadsheets export to JSON/CSV for engine consumption
- **Cross-sheet references** — Item database links to economy flows; abilities link to progression
- **Dependency tracking** — Clear visibility of which systems depend on which data
- **Circular dependency detection** — Warnings when feedback loops create instability

### Scalable & Flexible

Spreadsheets must grow with the game:

- **Template-driven** — Reusable structures for similar content types (enemies, items, abilities)
- **No hard-coded limits** — Rows and columns scale naturally as content expands
- **Conditional formatting** — Visual rules highlight anomalies (outlier damage values, unreachable progression tiers)
- **Automated summaries** — Dashboard tabs showing critical metrics (total balance, economy stability)
- **Multi-tab organization** — Clear separation of concerns (stats, loot, economy, scaling, etc.)

### Accurate & Precise

Numbers must be trustworthy:

- **Consistent decimal handling** — All currencies/percentages use defined precision
- **Rounding rules** — Explicit handling of fractional values (always round up? nearest integer?)
- **Unit clarity** — Damage is in hit points? Percentage? Multiplier?
- **Sanity checks** — Automatic warnings for suspicious values (boss health = 1 HP, damage > health)
- **Cross-validation** — Spot-checks against design intent (does progression curve match narrative beats?)

## Core Workflow

### 1. Define Data Structure

Before building a spreadsheet, clarify what you're modeling:

1. **Identify entities** — What are you tracking? (characters, items, abilities, enemies, economy nodes)
2. **List attributes** — What properties does each entity have? (health, damage, rarity, drop chance)
3. **Set constraints** — What rules apply? (health >= 0, rarity must be one of: common/rare/epic, damage must scale with level)
4. **Plan relationships** — How do different data types connect? (items drop from enemies, abilities unlock at level thresholds)
5. **Design for scale** — How will this spreadsheet grow? (100 items now, 500 items by launch?)

### 2. Build Master Data Tables

Create the canonical source for each data type.

Use the **Master Data Table Template** (see section below). Each table:
- Has a unique ID column (searchable, referenceable)
- Includes human-readable names and descriptions
- Contains all numeric properties and their units
- Provides validation and formatting rules
- Includes versioning and change log

### 3. Create Calculation Sheets

Build derived data from master tables.

Use the **Calculation Sheet Template** (see section below). For each calculated value:
- Document the formula in a separate reference column
- Show intermediate calculation steps
- Cross-reference master table rows
- Include sanity check ranges (this value should be between X and Y)

### 4. Build Integration Points

Export data to other systems.

Use the **Export Template** (see section below). For each output:
- Define JSON/CSV schema
- Map spreadsheet columns to output fields
- Validate exported data matches system expectations
- Version exports and track which game build used which export

### 5. Create Audit Trail

Track changes over time for game balance iteration.

Use the **Change Log Template** (see section below). For every modification:
- Record timestamp, designer, changed cells
- Explain WHY the change was made
- Measure impact (did this break anything?)
- Mark status (pending playtesting, verified, rolled back)

## Master Data Table Template

Every data type needs a master table.

```
Sheet Name: [Entity Type] (e.g., "Characters", "Items", "Abilities")

Columns:
A. ID                [UNIQUE, TEXT, Primary Key]
B. Name              [TEXT, Human-readable name]
C. Description       [TEXT, 200-char description]
D. [Property 1]      [NUMBER, Unit in header]
E. [Property 2]      [NUMBER, Unit in header]
...
Z. Notes             [TEXT, Design notes, design intent, edge cases]
AA. Version          [TEXT, Last modified version]
AB. Modified Date    [DATE, ISO 8601]
AC. Modified By      [TEXT, Designer name]

Example: Character Master Data
```

| ID | Name | Class | Health | Damage | Defense | Dodge% | Level Unlock | Rarity | Notes | Modified | By |
|----|------|-------|--------|--------|---------|--------|--------------|--------|-------|----------|-----|
| char_001 | Warrior | Melee | 100 | 25 | 15 | 10% | 1 | Starter | Tank class. Baseline for balance. | 2025-02-19 | Alex |
| char_002 | Mage | Magic | 60 | 35 | 8 | 5% | 1 | Starter | High damage, low defense. Squishy. | 2025-02-19 | Alex |
| char_003 | Rogue | Agile | 70 | 28 | 10 | 25% | 5 | Common | High dodge, medium stats. Balanced. | 2025-02-18 | Jordan |

**Best practices:**
- One row = one entity
- ID is immutable (never changes once assigned)
- Names are descriptive but concise
- All properties in same units (e.g., all percentages as whole numbers 0-100, not 0.0-1.0)
- Notes column clarifies design intent (why is Mage damage higher than Warrior?)
- Versioning tracks balance iteration history

### Master Data Example: Item Database

```
Sheet Name: Items

Columns:
A. Item_ID          [Unique identifier, e.g., "item_sword_001"]
B. Item_Name        [Display name, e.g., "Iron Sword"]
C. Item_Type        [Weapon | Armor | Consumable | Misc]
D. Rarity           [Common | Uncommon | Rare | Epic | Legendary]
E. Level_Require    [Minimum player level to equip]
F. Base_Damage      [Base damage value, numbers only]
G. Special_Effect   [Bonus effect, if any, or "None"]
H. Price_Buy        [NPC shop buy price in gold]
I. Price_Sell       [NPC shop sell value in gold]
J. Drop_Rate        [Probability 0-100% or "Fixed"]
J. Drop_Source      [Enemy ID | Chest | Quest | Craft]
K. Craft_Materials  [Material list or "N/A"]
L. Craft_Cost       [Gold cost to craft or "N/A"]
M. Weight           [For inventory management]
N. Tradeable        [Y/N - Can player trade this?]
O. Stackable        [Y/N - Multiple copies stack?]
P. Max_Stack        [If stackable, max quantity]
Q. Icon_File        [Asset reference, e.g., "art/items/sword_001.png"]
R. Status           [WIP | Ready | Playtested | Final]
S. Notes            [Design intent, balance reasoning]
T. Modified_Date    [ISO date]
U. Modified_By      [Designer name]

Example rows:
iron_sword_001 | Iron Sword | Weapon | Common | 1 | 15 | None | 100 | 50 | 10% | Bandit (5%) | None | 0 | 2.5 | Y | N | 1 | sword_001 | Ready | Standard starting weapon. Balanced baseline. | 2025-02-19 | Alex
fire_sword_001 | Flaming Sword | Weapon | Rare | 10 | 22 | +5 Fire Damage | 500 | 250 | 3% | Dragon (8%) | Ore x3 + Coal x1 | 200 | 3.0 | Y | N | 1 | sword_fire | Playtested | High damage, elemental bonus. Crafted or dropped. | 2025-02-18 | Jordan
```

## Calculation Sheet Template

Derived data and scaling formulas go here.

```
Sheet Name: [Name] (e.g., "Level Scaling", "Economy Balance", "Drop Rates")

Structure:
- Row 1: Headers with units clearly marked
- Column A-B: Master reference (ID, Name from master table)
- Column C onwards: Calculated values with formulas visible
- Separate "Formula Reference" section at bottom explaining each calculation

Example: Character Scaling by Level
```

| Char_ID | Char_Name | Level | Health_Base | Health_Per_Lvl | Total_Health | Damage_Base | Damage_Per_Lvl | Total_Damage | Defense_Bonus | Formula_Used |
|---------|-----------|-------|-------------|----------------|--------------|-------------|----------------|--------------|---------------|---------------|
| char_001 | Warrior | 1 | 100 | 8 | 100 | 25 | 1.5 | 25 | 0 | =C4 + D4*(E4-1) |
| char_001 | Warrior | 5 | 100 | 8 | 132 | 25 | 1.5 | 31 | 5 | =C4 + D4*(E4-1) |
| char_001 | Warrior | 10 | 100 | 8 | 172 | 25 | 1.5 | 38 | 10 | =C4 + D4*(E4-1) |
| char_001 | Warrior | 20 | 100 | 8 | 252 | 25 | 1.5 | 54 | 20 | =C4 + D4*(E4-1) |

**Formula Reference Section (at bottom of sheet):**
```
Total_Health = Health_Base + (Health_Per_Lvl × (Level - 1))
Total_Damage = Damage_Base + (Damage_Per_Lvl × (Level - 1))
Defense_Bonus = Level // 5 (integer divide)

Sanity Checks:
- Total_Health should never exceed 500 at level 50
- Total_Damage should scale linearly (no exponential spikes)
```

### Calculation Example: Loot Drop Rates

```
Sheet Name: Loot_Rates

Columns:
A. Enemy_ID
B. Enemy_Name
C. Item_ID
D. Item_Name
E. Rarity
F. Drop_Rate_Percent
G. Drop_Probability_Check
H. Expected_Drops_Per_100_Kills
I. Avg_Gold_Per_Kill
J. Total_Gold_Per_100_Kills

Example:
enemy_bandit_001 | Bandit | item_sword_001 | Iron Sword | Common | 5% | 0.05 | 5 | 25 | 2500
enemy_bandit_001 | Bandit | item_dagger_002 | Dagger | Common | 8% | 0.08 | 8 | 25 | 2500
enemy_bandit_001 | Bandit | item_ring_gold | Gold Ring | Rare | 1% | 0.01 | 1 | 25 | 2500

Notes:
- Drop_Rate_Percent column is the design intent (what we *want* to drop)
- Drop_Probability_Check converts to 0.0-1.0 range for random() calls in engine
- Expected_Drops shows what happens across 100 sample kills
- Verify total probability per enemy ≤ 100% (or < 100 if not all slots filled)
```

## Stat Progression Table

Define how stats scale with player level or item quality.

```
Sheet Name: Stat_Progression

Columns:
A. Level / Tier
B. Base_Health
C. Base_Damage
D. Base_Defense
E. Base_Crit_Chance
F. Notes

Example:
Level | Health | Damage | Defense | Crit_Rate | Notes
1     | 100    | 10     | 5       | 5%        | Starting stats
5     | 140    | 14     | 7       | 5%        | First progression
10    | 200    | 20     | 10      | 8%        | Mid-game milestone
20    | 340    | 32     | 15      | 10%       | Late-game power spike
30    | 500    | 45     | 20      | 12%       | Near endgame
50    | 900    | 75     | 30      | 15%       | Max level (capped)

Sanity Checks:
- Health scales linearly (approximately 1% per level)
- Damage scales with diminishing returns (not exponential)
- At level 50, player should feel powerful but not broken
```

## Economy Flow Model

Map resource flows through the game (gold earned, spent, sinks, sources).

```
Sheet Name: Economy

Columns:
A. Resource_Type (Gold, Crafting_Materials, etc.)
B. Source (Enemy drops, Quests, Crafting, Salvage)
C. Amount_Per_Action
D. Frequency (Per kill, Per quest, Per hour of play)
E. Total_Per_Hour (Amount × Frequency)
F. Sink (Items, Upgrades, Fast_Travel, Repairs)
G. Sink_Cost
H. Net_Flow (Source - Sink)
I. Status (Balanced / Surplus / Deficit)

Example Gold Flow:
Gold | Enemy Kill | 10-50 | Once per kill | 300/hour | Item Purchase | 100 | +200/hour | Balanced
Gold | Quest Reward | 500 | Once per quest (30 min) | 1000/hour | Gear Repair | 50 | +950/hour | Surplus (late-game needs sink)
Gold | Chest Loot | 25 | Once per 5 chests | 100/hour | Upgrade | 200 | -100/hour | Deficit (needs more sources)

Balance Goal: Source total ≈ Sink total
If Surplus: Add sinks (cosmetics, convenience, fast-travel)
If Deficit: Add sources (enemy drops, quest rewards)
```

## Ability Comparison Matrix

Compare abilities side-by-side for balance.

```
Sheet Name: Ability_Matrix

Columns:
A. Ability_ID
B. Ability_Name
C. Class / Character
D. Damage (or Effect)
E. Cost (Mana/Stamina/Cooldown)
F. Cost_Efficiency (Damage ÷ Cost)
G. Range
H. AoE_Radius
I. Cooldown_Seconds
J. Level_Unlock
K. Status
L. Notes

Example:
ability_fireball | Fireball | Mage | 40 | 25 MP | 1.6 DPM | 10 tiles | 3 tiles | 8 sec | 5 | Ready | High damage, balanced cost. Use as mage primary.
ability_frostbolt | Frostbolt | Mage | 30 | 15 MP | 2.0 DPM | 12 tiles | 1 tile | 5 sec | 1 | Ready | Lower damage but efficient. Quick cast.
ability_meteor | Meteor Strike | Mage | 80 | 50 MP | 1.6 DPM | 15 tiles | 5 tiles | 15 sec | 15 | Playtested | Powerful AoE. Long cooldown justified.
ability_slash | Basic Slash | Warrior | 25 | 0 MP (melee) | ∞ | 1.5 tiles | 0 | 0.5 sec | 1 | Ready | No cost. Primary attack.

Analysis Column (add as needed):
- Cost_Efficiency: Damage ÷ Cost = damage output per resource unit
- Compare abilities in same tier to spot outliers
- Abilities with Cost_Efficiency > 3.0 are overpowered
- Abilities with Cost_Efficiency < 0.8 need buffs
```

## Content Checklist

Track content creation status across the game.

```
Sheet Name: Content_Checklist

Columns:
A. System / Area
B. Feature / Asset
C. Status (Concept | WIP | Playtested | Approved | Final)
D. Priority (Critical | High | Medium | Low)
E. Owner
F. Dependencies
G. Target_Completion
H. Notes
I. Blocker (Yes/No)
J. Blocker_Details

Example:
Character | Warrior Class | Final | Critical | Alex | Balance review from JP | 2025-02-20 | All abilities finalized | No | —
Character | Mage Class | Playtested | Critical | Jordan | Damage scaling verification | 2025-02-22 | Damage feels high. Awaiting feedback. | Yes | Game balancer needs to verify ability costs
Items | Iron Sword | Final | High | Morgan | Drop rate balancing | 2025-02-19 | Item complete. Can be spawned. | No | —
Items | Fire Sword | WIP | High | Morgan | Recipe & crafting setup | 2025-02-25 | Waiting for crafting system design | Yes | Crafting not implemented yet
Economy | Gold Sinks | Concept | Medium | Casey | Economy flow model approval | 2025-03-01 | Need approval on fast-travel cost | No | —
UI | Inventory Screen | Approved | High | Sam | Wireframe finalization | 2025-02-21 | Layout ready for art. | No | —

Dashboard Summary (below main table):
Critical blockers: 1 (Mage balance)
High-priority WIP: 2
Ready for testing: 5
Final: 8
```

## Integration with Game-Balancer

The data-modeler supplies raw data; game-balancer runs simulations and returns verified outputs.

### Export to Game-Balancer

1. **Create export sheet** named `Export_To_GameBalancer`
2. **Include columns:**
   - Entity ID and name
   - All numeric properties (damage, health, cost, cooldown)
   - Relationships (character abilities, item drops)
   - Validation rules (min/max ranges)

3. **Format for JSON export:**

```json
{
  "entities": {
    "characters": [
      {
        "id": "char_001",
        "name": "Warrior",
        "health": 100,
        "damage": 25,
        "abilities": ["ability_slash", "ability_block"]
      }
    ],
    "items": [
      {
        "id": "item_sword_001",
        "name": "Iron Sword",
        "damage": 15,
        "rarity": "Common"
      }
    ]
  },
  "validation_rules": {
    "health": { "min": 1, "max": 1000 },
    "damage": { "min": 0, "max": 200 }
  }
}
```

### Import Game-Balancer Results

1. **Create import sheet** named `Import_From_GameBalancer`
2. **Columns:**
   - Entity ID (matches export)
   - Original value
   - Recommended balance change
   - Reasoning (e.g., "DPM too high by 15%")
   - Confidence (High / Medium / Low)

3. **Review changes and apply:**
   - Copy recommended values to master tables
   - Document decision (Accept / Reject / Modify)
   - Run sanity checks again
   - Update version numbers

4. **Example result:**

| Entity_ID | Entity_Name | Property | Original_Value | Recommended | Reasoning | Confidence | Decision | Applied |
|-----------|-------------|----------|----------------|-------------|-----------|------------|----------|---------|
| ability_fireball | Fireball | Damage | 40 | 35 | DPM too high vs. comparable abilities | High | Accept | Yes |
| char_002 | Mage | Health | 60 | 65 | Glass cannon, but dies too fast in playtests | Medium | Accept | Yes |
| item_sword_001 | Iron Sword | Base_Damage | 15 | 16 | Slightly underpowered for level 1 progression | Low | Reject | No |

## Openpyxl Code Examples

Automate spreadsheet creation and updates with Python.

### Example 1: Create a Master Data Table

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from datetime import datetime

# Create workbook
wb = Workbook()
ws = wb.active
ws.title = "Characters"

# Define headers
headers = ["ID", "Name", "Class", "Health", "Damage", "Defense", "Dodge%", "Level Unlock", "Status", "Notes", "Modified", "By"]

# Add headers with formatting
header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
header_font = Font(color="FFFFFF", bold=True)

for col_num, header in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col_num)
    cell.value = header
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center")

# Add data rows
characters = [
    {"id": "char_001", "name": "Warrior", "class": "Melee", "health": 100, "damage": 25, "defense": 15, "dodge": 10, "unlock": 1, "status": "Ready", "notes": "Tank baseline", "date": "2025-02-19", "by": "Alex"},
    {"id": "char_002", "name": "Mage", "class": "Magic", "health": 60, "damage": 35, "defense": 8, "dodge": 5, "unlock": 1, "status": "Ready", "notes": "High damage", "date": "2025-02-19", "by": "Alex"},
]

for row_num, char in enumerate(characters, 2):
    ws.cell(row=row_num, column=1).value = char["id"]
    ws.cell(row=row_num, column=2).value = char["name"]
    ws.cell(row=row_num, column=3).value = char["class"]
    ws.cell(row=row_num, column=4).value = char["health"]
    ws.cell(row=row_num, column=5).value = char["damage"]
    ws.cell(row=row_num, column=6).value = char["defense"]
    ws.cell(row=row_num, column=7).value = char["dodge"]
    ws.cell(row=row_num, column=8).value = char["unlock"]
    ws.cell(row=row_num, column=9).value = char["status"]
    ws.cell(row=row_num, column=10).value = char["notes"]
    ws.cell(row=row_num, column=11).value = char["date"]
    ws.cell(row=row_num, column=12).value = char["by"]

# Set column widths
ws.column_dimensions["A"].width = 12
ws.column_dimensions["B"].width = 15
ws.column_dimensions["C"].width = 12
ws.column_dimensions["D"].width = 10
ws.column_dimensions["E"].width = 10
ws.column_dimensions["F"].width = 10
ws.column_dimensions["G"].width = 10
ws.column_dimensions["H"].width = 13
ws.column_dimensions["I"].width = 10
ws.column_dimensions["J"].width = 20
ws.column_dimensions["K"].width = 12
ws.column_dimensions["L"].width = 10

# Save
wb.save("game_data_characters.xlsx")
print("Spreadsheet created: game_data_characters.xlsx")
```

### Example 2: Add Calculated Columns with Formulas

```python
from openpyxl import load_workbook

wb = load_workbook("game_data_characters.xlsx")
ws = wb["Characters"]

# Add formula column for "Damage per Health" ratio
ws.cell(row=1, column=13).value = "DPS_Ratio"

for row_num in range(2, len(ws._cells) + 1):
    damage_cell = ws.cell(row=row_num, column=5)
    health_cell = ws.cell(row=row_num, column=4)
    ratio_cell = ws.cell(row=row_num, column=13)

    # Formula: Damage / Health
    ratio_cell.value = f"={damage_cell.coordinate}/{health_cell.coordinate}"

# Add conditional formatting to highlight outliers
from openpyxl.formatting.rule import CellIsRule

red_fill = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")
yellow_fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")

# Highlight damage values > 40
ws.conditional_formatting.add(f"E2:E{len(ws._cells)}",
    CellIsRule(operator='greaterThan', formula=['40'], fill=red_fill))

# Highlight status = "WIP"
ws.conditional_formatting.add(f"I2:I{len(ws._cells)}",
    CellIsRule(operator='equal', formula=['"WIP"'], fill=yellow_fill))

wb.save("game_data_characters_updated.xlsx")
print("Formulas and formatting added.")
```

### Example 3: Validate Data Integrity

```python
from openpyxl import load_workbook

def validate_spreadsheet(file_path):
    wb = load_workbook(file_path)
    ws = wb.active

    errors = []

    # Check headers
    expected_headers = ["ID", "Name", "Class", "Health", "Damage", "Defense", "Dodge%", "Level Unlock", "Status", "Notes"]
    for col_num, expected in enumerate(expected_headers, 1):
        actual = ws.cell(row=1, column=col_num).value
        if actual != expected:
            errors.append(f"Column {col_num}: Expected '{expected}', got '{actual}'")

    # Validate data rows
    for row_num in range(2, ws.max_row + 1):
        id_val = ws.cell(row=row_num, column=1).value
        health = ws.cell(row=row_num, column=4).value
        damage = ws.cell(row=row_num, column=5).value
        dodge = ws.cell(row=row_num, column=7).value

        # Health must be positive
        if health and health <= 0:
            errors.append(f"Row {row_num} ({id_val}): Health must be > 0, got {health}")

        # Damage must be non-negative
        if damage and damage < 0:
            errors.append(f"Row {row_num} ({id_val}): Damage must be >= 0, got {damage}")

        # Dodge must be 0-100%
        if dodge and (dodge < 0 or dodge > 100):
            errors.append(f"Row {row_num} ({id_val}): Dodge must be 0-100%, got {dodge}%")

    if errors:
        print("Validation FAILED:")
        for error in errors:
            print(f"  - {error}")
        return False
    else:
        print("Validation PASSED: All data integrity checks passed.")
        return True

validate_spreadsheet("game_data_characters.xlsx")
```

### Example 4: Export to JSON for Engine

```python
from openpyxl import load_workbook
import json

def export_to_json(excel_file, json_file):
    wb = load_workbook(excel_file)
    ws = wb.active

    # Get headers
    headers = [ws.cell(row=1, column=col).value for col in range(1, ws.max_column + 1)]

    # Build data array
    data = []
    for row_num in range(2, ws.max_row + 1):
        row_data = {}
        for col_num, header in enumerate(headers, 1):
            value = ws.cell(row=row_num, column=col_num).value
            row_data[header] = value
        data.append(row_data)

    # Save as JSON
    output = {
        "sheet_name": ws.title,
        "timestamp": datetime.now().isoformat(),
        "row_count": len(data),
        "data": data
    }

    with open(json_file, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"Exported {len(data)} rows to {json_file}")

export_to_json("game_data_characters.xlsx", "game_data_characters.json")
```

## Integration with Other Skills

### Game-Balancer

**From game-balancer:**
- Simulation results (damage DPS, survivability metrics, balance scores)
- Outlier detection (abilities that are too strong/weak)
- Progression curve analysis (power growth matches design intent?)

**To game-balancer:**
- Raw stat tables and formulas
- Current balance state and known issues
- Areas where player feedback revealed imbalance

### Systems Designer

**From systems-designer:**
- Mechanic definitions (how much mana does casting cost? how long are cooldowns?)
- System constraints (no more than 20 active abilities, inventory cap at 99 items)
- Feedback on viability (can players actually use this item, or is it too rare?)

**To systems-designer:**
- Spreadsheet exports in JSON/CSV format for engine consumption
- Database schemas and relationships
- Version tracking and change history

### Narrative Designer

**From narrative-designer:**
- Level progression gates (story unlocks ability X at narrative beat Y)
- Loot story integration (certain items drop only after story milestones)
- NPC shop inventories (what does this merchant sell based on story progress?)

**To narrative-designer:**
- Level unlock requirements and progression tiers
- Item availability and rarity distributions
- Economy thresholds (when does player have enough gold for milestone X?)

### Level Designer

**From level-designer:**
- Enemy encounters and composition (5 bandits + 1 bandit leader = recommended level 5)
- Chest loot (what drops from chests in this area?)
- Resource distribution (gold, consumables, upgrade materials per level)

**To level-designer:**
- Monster stat tables (health, damage, AI behavior)
- Loot tables per enemy/chest type
- Progression curve validation (is this challenge appropriate for level X?)

## Best Practices

### Design Phase

1. **Start with master tables** — Define all entities before calculations
2. **Document units clearly** — Avoid confusion (is this damage in HP? Percentage?)
3. **Use meaningful IDs** — "char_001" and "weapon_sword_iron" are clear; "a1" is not
4. **Provide context** — Notes column explains WHY values are what they are
5. **Plan for scale** — Structure spreadsheets to grow from 100 items to 1000 items

### Iteration Phase

1. **Version frequently** — Save snapshots before big balance changes
2. **Track changes** — Every modification logged with timestamp and reason
3. **Run validations** — Automated checks flag impossible data early
4. **Cross-reference** — Use lookups to ensure consistency across sheets
5. **Playtest with data** — Export and test in-game before shipping

### Integration Phase

1. **Export regularly** — JSON/CSV exports for engine integration
2. **Validate exports** — Spot-checks to verify data round-tripped correctly
3. **Version control** — Commit spreadsheets to git for team collaboration
4. **Automate updates** — Scripts sync spreadsheet changes to code
5. **Document all formulas** — Future designers need to understand your calculations

## Output Format

Game data lives in `.xlsx` spreadsheets. Primary outputs:

- **Master data sheets** → Individual tab for each entity type (Characters, Items, Abilities, etc.)
- **Calculated sheets** → Derived values, formulas, scaling curves
- **Export sheets** → JSON/CSV formatted data for engine consumption
- **Change log sheet** → Version history and balance iteration notes
- **Dashboard sheet** → Summary metrics and status indicators

All spreadsheets committed to version control with timestamps and designer attribution.

## References

- `templates/character-master.xlsx` — Template for character data
- `templates/item-database.xlsx` — Template for item creation
- `templates/economy-model.xlsx` — Template for economic balance
- `templates/export-schema.json` — JSON schema for engine export
- `references/stat-formulas.md` — Archive of proven progression formulas
- `references/balance-benchmarks.md` — Balance targets and metrics
- `references/openpyxl-guide.md` — Python automation cookbook
- `references/data-integrity-checklist.md` — Validation rules for each data type
