# Data Integrity Checklist

Validation rules for all Infinite Voyage game data. Run this checklist before exporting
data to the game engine, before balance review sessions, and after any bulk data changes.
Each section maps to a specific data table or cross-table relationship.

---

## 1. Unique ID Checks

Every entity in every table must have a unique, non-empty identifier.

### Rules

- [ ] All ID fields are non-empty (no null, no blank, no whitespace-only)
- [ ] All IDs are unique within their table (no duplicates)
- [ ] IDs follow the naming convention: `[type]_[subtype]_[number]`
  - Characters: `char_warrior_001`, `char_mage_001`
  - Items: `item_sword_iron_001`, `item_potion_health_001`
  - Abilities: `ability_fireball_001`, `ability_slash_001`
  - Enemies: `enemy_bandit_001`, `enemy_dragon_001`
- [ ] IDs contain only lowercase letters, numbers, and underscores
- [ ] IDs are immutable -- once assigned, they never change
- [ ] No ID is reused across different tables (global uniqueness)

### Validation Script

```python
import re

def validate_ids(ws, id_col: int = 1, start_row: int = 2) -> list[str]:
    errors = []
    seen = set()
    id_pattern = re.compile(r'^[a-z][a-z0-9_]+$')

    for row in range(start_row, ws.max_row + 1):
        value = ws.cell(row=row, column=id_col).value
        if value is None or str(value).strip() == "":
            errors.append(f"Row {row}: Empty ID")
            continue
        value = str(value).strip()
        if value in seen:
            errors.append(f"Row {row}: Duplicate ID '{value}'")
        seen.add(value)
        if not id_pattern.match(value):
            errors.append(f"Row {row}: ID '{value}' violates naming convention")
    return errors
```

---

## 2. Stat Range Validation

All numeric values must fall within defined acceptable ranges.

### Character Stats

| Stat       | Minimum | Maximum | Notes                              |
|------------|---------|---------|-----------------------------------|
| Health     | 1       | 10000   | Must be positive integer           |
| Damage     | 0       | 500     | Zero is valid (non-combat NPCs)    |
| Defense    | 0       | 300     | Zero is valid                      |
| Dodge%     | 0       | 75      | Hard cap at 75% to prevent unhittable |
| Speed      | 0.5     | 5.0     | Multiplier, 1.0 is baseline        |
| Level      | 1       | 50      | Max level is 50                    |
| Crit%      | 0       | 50      | Hard cap at 50%                    |

### Item Stats

| Stat          | Minimum | Maximum | Notes                           |
|---------------|---------|---------|--------------------------------|
| Base_Damage   | 0       | 400     | Weapons only; zero for non-weapons |
| Base_Defense  | 0       | 200     | Armor only; zero for non-armor  |
| Buy_Price     | 0       | 100000  | Zero means not purchasable      |
| Sell_Price    | 0       | 50000   | Must be less than Buy_Price     |
| Drop_Rate     | 0       | 100     | Percentage, 0 means not dropped |
| Weight        | 0.1     | 50.0    | All items have weight           |
| Max_Stack     | 1       | 999     | 1 for non-stackable             |
| Level_Require | 1       | 50      | Must be within level range      |

### Enemy Stats

| Stat        | Minimum | Maximum  | Notes                            |
|-------------|---------|----------|----------------------------------|
| Health      | 1       | 1000000  | Bosses can have very high health |
| Damage      | 1       | 2000     | Must deal some damage            |
| Defense     | 0       | 500      | Zero defense is valid            |
| XP_Reward   | 1       | 50000    | Must grant some XP               |
| Gold_Drop   | 0       | 10000    | Zero is valid (some drop no gold)|
| Level       | 1       | 55       | Can exceed player cap by 5       |

### Ability Stats

| Stat        | Minimum | Maximum | Notes                            |
|-------------|---------|---------|----------------------------------|
| Damage      | 0       | 500     | Zero for non-damage abilities    |
| Cost        | 0       | 200     | Zero for free abilities          |
| Cooldown    | 0       | 300     | Seconds; zero for no cooldown    |
| Range       | 0       | 50      | Tiles; zero for self-only        |
| AoE_Radius  | 0       | 15      | Tiles; zero for single-target    |
| Level_Unlock| 1       | 50      | Must be within level range       |

### Validation Script

```python
STAT_RANGES = {
    "Health": (1, 10000),
    "Damage": (0, 500),
    "Defense": (0, 300),
    "Dodge%": (0, 75),
    "Speed": (0.5, 5.0),
    "Level": (1, 50),
    "Buy_Price": (0, 100000),
    "Sell_Price": (0, 50000),
    "Drop_Rate": (0, 100),
}

def validate_stat_ranges(ws, column_ranges: dict[str, tuple],
                         start_row: int = 2) -> list[str]:
    errors = []
    headers = {ws.cell(row=1, column=c).value: c
               for c in range(1, ws.max_column + 1)}

    for stat_name, (min_val, max_val) in column_ranges.items():
        if stat_name not in headers:
            continue
        col = headers[stat_name]
        for row in range(start_row, ws.max_row + 1):
            value = ws.cell(row=row, column=col).value
            if value is None:
                continue
            try:
                num = float(value)
                if num < min_val or num > max_val:
                    entity_id = ws.cell(row=row, column=1).value
                    errors.append(
                        f"Row {row} ({entity_id}): {stat_name} = {value} "
                        f"outside range [{min_val}, {max_val}]"
                    )
            except (ValueError, TypeError):
                errors.append(f"Row {row}: {stat_name} = '{value}' is not numeric")
    return errors
```

---

## 3. Required Fields Check

Certain fields must always be populated. Empty cells in required columns indicate
incomplete data that should not be exported.

### Required Fields by Table

| Table      | Required Columns                                              |
|------------|---------------------------------------------------------------|
| Characters | ID, Name, Class, Health, Damage, Defense, Level_Unlock, Status|
| Items      | ID, Name, Type, Rarity, Level_Req, Status                    |
| Abilities  | ID, Name, Class, Damage, Cost, Cooldown, Level_Unlock, Status|
| Enemies    | ID, Name, Type, Health, Damage, XP_Reward, Level             |
| Economy    | Resource_Type, Source, Amount, Frequency                      |
| Loot_Rates | Enemy_ID, Item_ID, Drop_Rate_Percent                         |

### Validation Script

```python
REQUIRED_FIELDS = {
    "Characters": ["ID", "Name", "Class", "Health", "Damage", "Defense",
                   "Level_Unlock", "Status"],
    "Items": ["ID", "Name", "Type", "Rarity", "Level_Req", "Status"],
    "Abilities": ["ID", "Name", "Class", "Damage", "Cost", "Cooldown",
                  "Level_Unlock", "Status"],
    "Enemies": ["ID", "Name", "Type", "Health", "Damage", "XP_Reward", "Level"],
}

def validate_required_fields(ws, required: list[str],
                              start_row: int = 2) -> list[str]:
    errors = []
    headers = {ws.cell(row=1, column=c).value: c
               for c in range(1, ws.max_column + 1)}

    for field in required:
        if field not in headers:
            errors.append(f"Required column '{field}' missing from sheet")
            continue
        col = headers[field]
        for row in range(start_row, ws.max_row + 1):
            value = ws.cell(row=row, column=col).value
            if value is None or str(value).strip() == "":
                entity_id = ws.cell(row=row, column=1).value or f"row_{row}"
                errors.append(f"Row {row} ({entity_id}): Required field '{field}' is empty")
    return errors
```

---

## 4. Formula Consistency

All calculated columns must use consistent formulas. A formula that works differently
in row 5 than in row 50 is a hidden bug.

### Rules

- [ ] Every formula column uses the same formula pattern in every row
- [ ] No hardcoded values embedded in formulas (use named ranges or reference cells)
- [ ] Formula references point to correct columns (no off-by-one column shifts)
- [ ] Division formulas include divide-by-zero protection (IFERROR or IF checks)
- [ ] Percentage calculations are consistent (all 0-100 or all 0.0-1.0, never mixed)
- [ ] Rounding is applied consistently (all ROUND, all FLOOR, or all CEILING)

### Common Formula Errors

| Error                      | Symptom                       | Fix                        |
|----------------------------|-------------------------------|----------------------------|
| Mixed reference styles     | Some rows calculate differently| Standardize $ references   |
| Missing IFERROR            | #DIV/0! errors in empty rows  | Wrap all divisions         |
| Hardcoded row numbers      | Formula breaks when rows move | Use relative references    |
| Inconsistent rounding      | Values differ by 1 between rows| Choose one rounding method |
| Circular reference         | Cells show 0 or error         | Break the dependency cycle |

### Validation Script

```python
def validate_formula_consistency(ws, formula_cols: list[int],
                                  start_row: int = 2) -> list[str]:
    """Check that formula columns use consistent patterns."""
    errors = []
    for col in formula_cols:
        patterns = {}
        col_letter = ws.cell(row=1, column=col).column_letter
        for row in range(start_row, ws.max_row + 1):
            cell = ws.cell(row=row, column=col)
            if cell.value and str(cell.value).startswith("="):
                # Normalize formula by replacing row numbers with 'N'
                normalized = re.sub(r'\d+', 'N', str(cell.value))
                if normalized not in patterns:
                    patterns[normalized] = []
                patterns[normalized].append(row)

        if len(patterns) > 1:
            errors.append(
                f"Column {col_letter}: Inconsistent formulas detected. "
                f"Found {len(patterns)} distinct patterns: {list(patterns.keys())}"
            )
    return errors
```

---

## 5. Cross-Table Reference Validation

References between tables must point to existing entities. An item that drops from
an enemy that does not exist is broken data.

### Reference Relationships

| Source Table | Source Column | Target Table | Target Column | Rule                          |
|-------------|-------------|-------------|--------------|-------------------------------|
| Loot_Rates  | Enemy_ID    | Enemies     | ID           | Every Enemy_ID must exist     |
| Loot_Rates  | Item_ID     | Items       | ID           | Every Item_ID must exist      |
| Abilities   | Class       | Characters  | Class        | Every Class must exist        |
| Items       | Drop_Source | Enemies     | ID           | If enemy ID, must exist       |
| Items       | Craft_Materials | Items   | ID           | Material IDs must exist       |
| Economy     | Source      | (various)   | ID           | Source entity must exist      |

### Rules

- [ ] Every foreign key reference points to an existing primary key
- [ ] No orphaned references (items referencing deleted enemies)
- [ ] No circular dependencies in crafting (item A needs item B needs item A)
- [ ] Drop sources reference valid enemy IDs or valid source types
- [ ] Quest reward items exist in the Items table
- [ ] Ability class assignments match existing character classes

### Validation Script

```python
def validate_cross_references(source_ws, source_col: int,
                               target_ws, target_col: int,
                               start_row: int = 2) -> list[str]:
    """Verify all values in source column exist in target column."""
    errors = []

    # Build set of valid target values
    valid_targets = set()
    for row in range(start_row, target_ws.max_row + 1):
        value = target_ws.cell(row=row, column=target_col).value
        if value:
            valid_targets.add(str(value).strip())

    # Check each source value
    for row in range(start_row, source_ws.max_row + 1):
        value = source_ws.cell(row=row, column=source_col).value
        if value and str(value).strip() not in valid_targets:
            source_id = source_ws.cell(row=row, column=1).value
            errors.append(
                f"Row {row} ({source_id}): Reference '{value}' not found in target table"
            )
    return errors
```

---

## 6. Naming Convention Checks

Consistent naming makes data searchable, sortable, and maintainable.

### Rules

- [ ] IDs use `snake_case` with type prefix (see section 1)
- [ ] Display names use Title Case ("Iron Sword", not "iron sword" or "IRON SWORD")
- [ ] Class names are consistent across tables (same spelling, same capitalization)
- [ ] Rarity values use exact enum values: Common, Uncommon, Rare, Epic, Legendary
- [ ] Status values use exact enum values: Concept, WIP, Ready, Playtested, Final
- [ ] Type values use defined enums per table (Weapon, Armor, Consumable, Misc for items)
- [ ] No trailing whitespace in any text field
- [ ] No special characters in IDs (no spaces, hyphens, or Unicode)

### Enum Definitions

```python
VALID_ENUMS = {
    "Rarity": {"Common", "Uncommon", "Rare", "Epic", "Legendary"},
    "Status": {"Concept", "WIP", "Ready", "Playtested", "Final"},
    "Item_Type": {"Weapon", "Armor", "Consumable", "Accessory", "Material", "Misc"},
    "Character_Class": {"Melee", "Magic", "Agile", "Support"},
    "Enemy_Type": {"Normal", "Elite", "MiniBoss", "Boss", "WorldBoss"},
}

def validate_enums(ws, column_name: str, valid_values: set,
                   start_row: int = 2) -> list[str]:
    errors = []
    headers = {ws.cell(row=1, column=c).value: c
               for c in range(1, ws.max_column + 1)}
    if column_name not in headers:
        return [f"Column '{column_name}' not found"]
    col = headers[column_name]
    for row in range(start_row, ws.max_row + 1):
        value = ws.cell(row=row, column=col).value
        if value and str(value).strip() not in valid_values:
            entity_id = ws.cell(row=row, column=1).value
            errors.append(
                f"Row {row} ({entity_id}): '{value}' is not a valid {column_name}. "
                f"Expected one of: {sorted(valid_values)}"
            )
    return errors
```

---

## 7. Economy Integrity

Special checks for economic data to prevent inflation and broken loops.

### Rules

- [ ] Sell price is always less than buy price (ratio 0.25-0.50)
- [ ] No positive-sum crafting loops (output value < input value)
- [ ] Quest rewards scale appropriately with level (no level-1 quests giving 10000 gold)
- [ ] Enemy gold drops scale with enemy level
- [ ] Total gold sources per hour do not exceed target by more than 20%
- [ ] Total gold sinks per hour are within 20% of total sources
- [ ] No item can be bought and immediately sold for profit
- [ ] Repair costs are a percentage of gear value, not a flat fee

### Validation Script

```python
def validate_economy_integrity(items_ws, start_row: int = 2) -> list[str]:
    errors = []
    headers = {items_ws.cell(row=1, column=c).value: c
               for c in range(1, items_ws.max_column + 1)}

    buy_col = headers.get("Buy_Price")
    sell_col = headers.get("Sell_Price")

    if not buy_col or not sell_col:
        return ["Buy_Price or Sell_Price column not found"]

    for row in range(start_row, items_ws.max_row + 1):
        buy = items_ws.cell(row=row, column=buy_col).value
        sell = items_ws.cell(row=row, column=sell_col).value
        item_id = items_ws.cell(row=row, column=1).value

        if buy and sell:
            try:
                buy_val = float(buy)
                sell_val = float(sell)
                if sell_val >= buy_val and buy_val > 0:
                    errors.append(
                        f"Row {row} ({item_id}): Sell price ({sell_val}) >= "
                        f"Buy price ({buy_val}) -- arbitrage risk!"
                    )
                if buy_val > 0 and sell_val / buy_val > 0.50:
                    errors.append(
                        f"Row {row} ({item_id}): Sell/Buy ratio "
                        f"({sell_val/buy_val:.2f}) exceeds 0.50 threshold"
                    )
            except (ValueError, TypeError):
                pass
    return errors
```

---

## 8. Pre-Export Checklist

Run before any data export to the game engine.

- [ ] All checks in sections 1-7 pass with zero errors
- [ ] All rows have Status of "Ready" or higher (no Concept or WIP in export)
- [ ] Modified dates are within the current development cycle
- [ ] Change log is up to date with latest modifications
- [ ] Export schema matches engine expectations (column names, data types)
- [ ] JSON/CSV output has been spot-checked against source spreadsheet
- [ ] Version number has been incremented
- [ ] Previous export has been archived before overwriting

---

## Running the Full Checklist

```python
def run_full_integrity_check(workbook_path: str) -> dict[str, list[str]]:
    """Run all integrity checks and return categorized results."""
    from openpyxl import load_workbook
    wb = load_workbook(workbook_path)
    results = {}

    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        sheet_errors = []

        # 1. ID checks
        sheet_errors.extend(validate_ids(ws))

        # 2. Required fields
        if sheet_name in REQUIRED_FIELDS:
            sheet_errors.extend(
                validate_required_fields(ws, REQUIRED_FIELDS[sheet_name])
            )

        # 3. Stat ranges
        sheet_errors.extend(validate_stat_ranges(ws, STAT_RANGES))

        # 4. Naming conventions
        for col_name, valid_vals in VALID_ENUMS.items():
            sheet_errors.extend(validate_enums(ws, col_name, valid_vals))

        results[sheet_name] = sheet_errors

    total = sum(len(e) for e in results.values())
    print(f"Total errors found: {total}")
    for sheet, errors in results.items():
        if errors:
            print(f"\n{sheet}: {len(errors)} errors")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"\n{sheet}: PASSED")

    return results
```

When errors are found, fix them in priority order: unique IDs first, then required
fields, then stat ranges, then cross-references, then naming conventions. ID errors
can cascade into cross-reference failures, so always fix those first.
