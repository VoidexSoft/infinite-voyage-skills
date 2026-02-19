# openpyxl Quick Reference for Game Data

Practical openpyxl patterns for building and maintaining Infinite Voyage balance
spreadsheets. Every example is oriented toward game data tasks: stat tables, loot
databases, economy models, and balance tracking.

---

## Creating a Workbook

### Basic Workbook Setup

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

wb = Workbook()

# Rename default sheet
ws = wb.active
ws.title = "Characters"

# Add additional sheets
ws_items = wb.create_sheet("Items")
ws_economy = wb.create_sheet("Economy")
ws_changelog = wb.create_sheet("ChangeLog")

wb.save("infinite_voyage_data.xlsx")
```

### Game Data Workbook Template

```python
def create_game_data_workbook(filename: str) -> Workbook:
    """Create a standard game data workbook with common sheets."""
    wb = Workbook()

    sheet_configs = [
        ("Characters", ["ID", "Name", "Class", "Health", "Damage", "Defense",
                        "Dodge%", "Speed", "Level_Unlock", "Rarity", "Status", "Notes"]),
        ("Items", ["ID", "Name", "Type", "Rarity", "Level_Req", "Base_Damage",
                   "Base_Defense", "Special", "Buy_Price", "Sell_Price", "Drop_Rate",
                   "Status", "Notes"]),
        ("Abilities", ["ID", "Name", "Class", "Damage", "Cost", "Cooldown",
                       "Range", "AoE", "Level_Unlock", "DPM_Ratio", "Status", "Notes"]),
        ("Enemies", ["ID", "Name", "Type", "Health", "Damage", "Defense",
                     "XP_Reward", "Gold_Drop", "Level", "Zone", "Status", "Notes"]),
    ]

    for i, (name, headers) in enumerate(sheet_configs):
        ws = wb.active if i == 0 else wb.create_sheet(name)
        if i == 0:
            ws.title = name
        apply_headers(ws, headers)

    wb.save(filename)
    return wb
```

---

## Formatting Cells

### Header Styling

```python
def apply_headers(ws, headers: list[str]):
    """Apply styled headers to a worksheet."""
    header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
    header_font = Font(name="Calibri", size=11, color="FFFFFF", bold=True)
    header_align = Alignment(horizontal="center", vertical="center", wrap_text=True)
    thin_border = Border(
        bottom=Side(style="medium", color="000000")
    )

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col)
        cell.value = header
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = header_align
        cell.border = thin_border

    # Freeze top row for scrolling
    ws.freeze_panes = "A2"
```

### Rarity Color Coding

```python
RARITY_COLORS = {
    "Common":    PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid"),
    "Uncommon":  PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid"),
    "Rare":      PatternFill(start_color="BDD7EE", end_color="BDD7EE", fill_type="solid"),
    "Epic":      PatternFill(start_color="D9B3FF", end_color="D9B3FF", fill_type="solid"),
    "Legendary": PatternFill(start_color="FFD966", end_color="FFD966", fill_type="solid"),
}

def apply_rarity_colors(ws, rarity_col: int, start_row: int = 2):
    """Color-code rows based on rarity value."""
    for row in range(start_row, ws.max_row + 1):
        rarity = ws.cell(row=row, column=rarity_col).value
        if rarity in RARITY_COLORS:
            fill = RARITY_COLORS[rarity]
            for col in range(1, ws.max_column + 1):
                ws.cell(row=row, column=col).fill = fill
```

### Status Column Styling

```python
STATUS_COLORS = {
    "Concept":    Font(color="999999", italic=True),
    "WIP":        Font(color="FF8C00", bold=True),
    "Ready":      Font(color="008000"),
    "Playtested": Font(color="0000FF"),
    "Final":      Font(color="006400", bold=True),
}

def apply_status_styling(ws, status_col: int, start_row: int = 2):
    """Style status cells based on their value."""
    for row in range(start_row, ws.max_row + 1):
        cell = ws.cell(row=row, column=status_col)
        if cell.value in STATUS_COLORS:
            cell.font = STATUS_COLORS[cell.value]
```

---

## Conditional Formatting

### Color Scales for Balance Data

Color scales visually highlight outliers in numeric columns -- essential for spotting
balance anomalies.

```python
from openpyxl.formatting.rule import ColorScaleRule, CellIsRule, FormulaRule

def add_balance_color_scale(ws, col_letter: str, min_row: int = 2, max_row: int = 100):
    """
    Green-Yellow-Red color scale for balance columns.
    Low values = green (good), high values = red (potential problem).
    """
    cell_range = f"{col_letter}{min_row}:{col_letter}{max_row}"
    rule = ColorScaleRule(
        start_type="min", start_color="63BE7B",   # Green
        mid_type="percentile", mid_value=50, mid_color="FFEB84",  # Yellow
        end_type="max", end_color="F8696B"         # Red
    )
    ws.conditional_formatting.add(cell_range, rule)

# Example: highlight damage column (column E) with balance scale
# add_balance_color_scale(ws, "E", 2, 50)
```

### Threshold Highlighting

```python
def highlight_outliers(ws, col_letter: str, low_threshold: float,
                       high_threshold: float, max_row: int = 100):
    """Highlight values outside acceptable range."""
    cell_range = f"{col_letter}2:{col_letter}{max_row}"

    # Red for values above threshold
    red_fill = PatternFill(start_color="FF6B6B", end_color="FF6B6B", fill_type="solid")
    ws.conditional_formatting.add(cell_range,
        CellIsRule(operator="greaterThan", formula=[str(high_threshold)], fill=red_fill))

    # Blue for values below threshold
    blue_fill = PatternFill(start_color="6B9FFF", end_color="6B9FFF", fill_type="solid")
    ws.conditional_formatting.add(cell_range,
        CellIsRule(operator="lessThan", formula=[str(low_threshold)], fill=blue_fill))

# Example: highlight damage values outside 10-50 range
# highlight_outliers(ws, "E", 10, 50)
```

### Duplicate ID Detection

```python
def highlight_duplicate_ids(ws, id_col_letter: str = "A", max_row: int = 100):
    """Highlight duplicate IDs in red -- critical data integrity check."""
    cell_range = f"{id_col_letter}2:{id_col_letter}{max_row}"
    # COUNTIF formula to detect duplicates
    formula = f'COUNTIF(${id_col_letter}:${id_col_letter},{id_col_letter}2)>1'
    red_fill = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")
    ws.conditional_formatting.add(cell_range,
        FormulaRule(formula=[formula], fill=red_fill))
```

---

## Formulas

### Calculated Columns

```python
def add_dps_formula(ws, damage_col: str, cooldown_col: str,
                    output_col: str, start_row: int = 2):
    """Add DPS = Damage / Cooldown formula column."""
    ws.cell(row=1, column=ws[f"{output_col}1"].column).value = "DPS"
    for row in range(start_row, ws.max_row + 1):
        formula = f"=IF({cooldown_col}{row}>0,{damage_col}{row}/{cooldown_col}{row},0)"
        ws.cell(row=row, column=ws[f"{output_col}1"].column).value = formula

def add_cost_efficiency_formula(ws, damage_col: str, cost_col: str,
                                 output_col: str, start_row: int = 2):
    """Add Cost Efficiency = Damage / Cost formula."""
    ws.cell(row=1, column=ws[f"{output_col}1"].column).value = "Cost_Efficiency"
    for row in range(start_row, ws.max_row + 1):
        formula = f"=IF({cost_col}{row}>0,{damage_col}{row}/{cost_col}{row},\"Free\")"
        ws.cell(row=row, column=ws[f"{output_col}1"].column).value = formula
```

### Summary Formulas

```python
def add_summary_section(ws, data_start_row: int, data_end_row: int,
                        summary_start_row: int):
    """Add summary statistics below the data table."""
    summary_row = summary_start_row
    ws.cell(row=summary_row, column=1).value = "--- SUMMARY ---"
    ws.cell(row=summary_row, column=1).font = Font(bold=True, size=12)

    stats = [
        ("Count", "COUNTA"),
        ("Average", "AVERAGE"),
        ("Min", "MIN"),
        ("Max", "MAX"),
        ("StdDev", "STDEV"),
    ]

    for i, (label, func) in enumerate(stats):
        row = summary_row + 1 + i
        ws.cell(row=row, column=1).value = label
        ws.cell(row=row, column=1).font = Font(bold=True)
        # Apply to numeric columns (D onwards)
        for col_idx in range(4, ws.max_column + 1):
            col_letter = ws.cell(row=1, column=col_idx).column_letter
            formula = f"={func}({col_letter}{data_start_row}:{col_letter}{data_end_row})"
            ws.cell(row=row, column=col_idx).value = formula
```

### Cross-Sheet Lookups

```python
def add_cross_sheet_lookup(ws, lookup_col: str, source_sheet: str,
                           source_key_col: str, source_value_col: str,
                           output_col: str, start_row: int = 2):
    """
    VLOOKUP from another sheet. Example: look up enemy name from enemy ID.
    """
    ws.cell(row=1, column=ws[f"{output_col}1"].column).value = f"Lookup_{source_sheet}"
    for row in range(start_row, ws.max_row + 1):
        formula = (
            f"=IFERROR(VLOOKUP({lookup_col}{row},"
            f"'{source_sheet}'!{source_key_col}:{source_value_col},"
            f"COLUMN({source_value_col}1)-COLUMN({source_key_col}1)+1,FALSE),\"NOT FOUND\")"
        )
        ws.cell(row=row, column=ws[f"{output_col}1"].column).value = formula
```

---

## Charts

### Stat Comparison Bar Chart

```python
from openpyxl.chart import BarChart, Reference

def add_stat_comparison_chart(ws, title: str, name_col: int, data_cols: list[int],
                               start_row: int = 1, end_row: int = 10,
                               chart_position: str = "A15"):
    """Bar chart comparing stats across entities (e.g., class comparison)."""
    chart = BarChart()
    chart.type = "col"
    chart.title = title
    chart.style = 10
    chart.y_axis.title = "Value"
    chart.x_axis.title = "Entity"
    chart.width = 20
    chart.height = 12

    categories = Reference(ws, min_col=name_col, min_row=start_row + 1, max_row=end_row)

    for col in data_cols:
        data = Reference(ws, min_col=col, min_row=start_row, max_row=end_row)
        chart.add_data(data, titles_from_data=True)

    chart.set_categories(categories)
    ws.add_chart(chart, chart_position)

# Example: compare Health, Damage, Defense across characters
# add_stat_comparison_chart(ws, "Class Stat Comparison", 2, [4, 5, 6], 1, 5)
```

### Progression Curve Line Chart

```python
from openpyxl.chart import LineChart

def add_progression_chart(ws, title: str, level_col: int, stat_cols: list[int],
                          start_row: int = 1, end_row: int = 50,
                          chart_position: str = "A20"):
    """Line chart showing stat progression over levels."""
    chart = LineChart()
    chart.title = title
    chart.style = 10
    chart.y_axis.title = "Stat Value"
    chart.x_axis.title = "Level"
    chart.width = 22
    chart.height = 14

    categories = Reference(ws, min_col=level_col, min_row=start_row + 1, max_row=end_row)

    for col in stat_cols:
        data = Reference(ws, min_col=col, min_row=start_row, max_row=end_row)
        chart.add_data(data, titles_from_data=True)

    chart.set_categories(categories)
    ws.add_chart(chart, chart_position)
```

---

## Data Validation

### Dropdown Lists

```python
from openpyxl.worksheet.datavalidation import DataValidation

def add_rarity_dropdown(ws, col_letter: str, max_row: int = 100):
    """Add rarity dropdown validation to a column."""
    dv = DataValidation(
        type="list",
        formula1='"Common,Uncommon,Rare,Epic,Legendary"',
        allow_blank=True
    )
    dv.error = "Invalid rarity. Choose from: Common, Uncommon, Rare, Epic, Legendary"
    dv.errorTitle = "Invalid Rarity"
    dv.prompt = "Select item rarity"
    dv.promptTitle = "Rarity"
    ws.add_data_validation(dv)
    dv.add(f"{col_letter}2:{col_letter}{max_row}")

def add_status_dropdown(ws, col_letter: str, max_row: int = 100):
    """Add status dropdown validation to a column."""
    dv = DataValidation(
        type="list",
        formula1='"Concept,WIP,Ready,Playtested,Final"',
        allow_blank=False
    )
    dv.error = "Invalid status."
    ws.add_data_validation(dv)
    dv.add(f"{col_letter}2:{col_letter}{max_row}")
```

### Numeric Range Validation

```python
def add_range_validation(ws, col_letter: str, min_val: float, max_val: float,
                         max_row: int = 100):
    """Validate that numeric values fall within an acceptable range."""
    dv = DataValidation(
        type="decimal",
        operator="between",
        formula1=str(min_val),
        formula2=str(max_val)
    )
    dv.error = f"Value must be between {min_val} and {max_val}"
    dv.errorTitle = "Out of Range"
    ws.add_data_validation(dv)
    dv.add(f"{col_letter}2:{col_letter}{max_row}")

# Examples
# add_range_validation(ws, "D", 1, 10000)     # Health: 1 to 10000
# add_range_validation(ws, "G", 0, 100)        # Dodge%: 0 to 100
# add_range_validation(ws, "J", 0, 100)        # Drop rate: 0 to 100
```

### Unique ID Validation (Script-Based)

```python
def validate_unique_ids(ws, id_col: int = 1, start_row: int = 2) -> list[str]:
    """Check for duplicate IDs and return error messages."""
    seen = {}
    errors = []
    for row in range(start_row, ws.max_row + 1):
        cell_value = ws.cell(row=row, column=id_col).value
        if cell_value is None:
            continue
        if cell_value in seen:
            errors.append(
                f"Duplicate ID '{cell_value}' at rows {seen[cell_value]} and {row}"
            )
        else:
            seen[cell_value] = row
    return errors
```

---

## Named Ranges

```python
from openpyxl.workbook.defined_name import DefinedName

def define_named_range(wb, name: str, sheet_title: str, cell_range: str):
    """Create a named range for cross-sheet references."""
    defined_name = DefinedName(name, attr_text=f"'{sheet_title}'!{cell_range}")
    wb.defined_names.add(defined_name)

# Example named ranges for game data
# define_named_range(wb, "CharacterIDs", "Characters", "$A$2:$A$100")
# define_named_range(wb, "ItemIDs", "Items", "$A$2:$A$500")
# define_named_range(wb, "RarityList", "Config", "$A$2:$A$6")
# define_named_range(wb, "StatusList", "Config", "$B$2:$B$6")
```

---

## Column Width Auto-Sizing

```python
def auto_size_columns(ws, min_width: float = 8, max_width: float = 40):
    """Approximate auto-sizing based on content length."""
    for col in ws.columns:
        max_length = 0
        col_letter = col[0].column_letter
        for cell in col:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))
        adjusted = min(max(max_length + 2, min_width), max_width)
        ws.column_dimensions[col_letter].width = adjusted
```

---

## Complete Example: Balance Review Sheet

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

def create_balance_review_sheet():
    """Full example: create a balance review workbook for ability comparison."""
    wb = Workbook()
    ws = wb.active
    ws.title = "Ability_Balance"

    headers = ["ID", "Name", "Class", "Damage", "Cost", "Cooldown",
               "DPS", "Cost_Eff", "Status", "Balance_Note"]
    apply_headers(ws, headers)

    # Sample data
    abilities = [
        ["ab_fireball", "Fireball", "Mage", 40, 25, 8, None, None, "Ready", ""],
        ["ab_frostbolt", "Frostbolt", "Mage", 30, 15, 5, None, None, "Ready", ""],
        ["ab_slash", "Slash", "Warrior", 25, 0, 0.5, None, None, "Ready", ""],
        ["ab_shield", "Shield Bash", "Warrior", 15, 10, 6, None, None, "WIP", ""],
    ]

    for row_idx, ability in enumerate(abilities, 2):
        for col_idx, value in enumerate(ability, 1):
            ws.cell(row=row_idx, column=col_idx).value = value
        # DPS formula: Damage / Cooldown
        ws.cell(row=row_idx, column=7).value = f"=IF(F{row_idx}>0,D{row_idx}/F{row_idx},0)"
        # Cost Efficiency: Damage / Cost
        ws.cell(row=row_idx, column=8).value = (
            f'=IF(E{row_idx}>0,D{row_idx}/E{row_idx},"Free")'
        )

    # Add conditional formatting for balance
    add_balance_color_scale(ws, "G", 2, 10)
    highlight_outliers(ws, "D", 10, 50)

    # Add validation
    add_status_dropdown(ws, "I")

    auto_size_columns(ws)
    wb.save("ability_balance_review.xlsx")
    print("Balance review sheet created.")

# create_balance_review_sheet()
```

---

## Tips for Game Data Spreadsheets

1. **Always freeze the header row** -- game data sheets get long fast
2. **Use named ranges** for any value referenced across sheets
3. **Add data validation** to every column that has a fixed set of valid values
4. **Color-code by rarity/status** -- visual scanning is faster than reading
5. **Include a formula reference** section at the bottom of calculation sheets
6. **Save frequently** -- openpyxl does not auto-save
7. **Keep one workbook per major system** -- Characters, Items, Economy as separate files
8. **Version your files** -- include date or version number in the filename
