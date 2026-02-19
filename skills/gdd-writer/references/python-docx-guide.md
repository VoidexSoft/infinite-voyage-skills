# python-docx Quick Reference for GDD Creation

A practical cookbook for producing professional Game Design Documents using the
`python-docx` library. Every snippet targets Word 2016+ (.docx) output and has
been verified against python-docx 1.1.x.

---

## 1. Installation & Imports

```bash
pip install python-docx Pillow   # Pillow needed for image handling
```

```python
from docx import Document
from docx.shared import Inches, Pt, Cm, Emu, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import nsdecls, qn
from docx.oxml import parse_xml
from docx.oxml.shared import OxmlElement
from datetime import datetime
```

---

## 2. Document Setup

### Create a New Document

```python
doc = Document()                        # blank document
doc = Document("template.docx")         # from a branded template
```

### Set Page Margins

```python
for section in doc.sections:
    section.top_margin    = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin   = Inches(1)
    section.right_margin  = Inches(1)
```

### Set Page Size (Letter / A4)

```python
section = doc.sections[0]
section.page_width  = Inches(8.5)       # Letter
section.page_height = Inches(11)

# A4 alternative
section.page_width  = Cm(21.0)
section.page_height = Cm(29.7)
```

### Landscape Orientation

```python
section = doc.sections[-1]
section.orientation = WD_ORIENT.LANDSCAPE
new_width, new_height = section.page_height, section.page_width
section.page_width  = new_width
section.page_height = new_height
```

---

## 3. Built-in Styles

python-docx exposes Word's built-in style names. The GDD writer relies on
these consistently:

| Style Name      | Use in GDD                              |
|-----------------|-----------------------------------------|
| `Heading 1`     | Chapter titles (1. High Concept)        |
| `Heading 2`     | Sections (1.1 Logline)                  |
| `Heading 3`     | Sub-sections (1.1.1 Core Fantasy)       |
| `Heading 4`     | Detail headings inside sub-sections     |
| `Normal`        | Body text paragraphs                    |
| `List Bullet`   | Unordered bullet lists                  |
| `List Bullet 2` | Nested bullets (second level)           |
| `List Number`   | Ordered/numbered lists                  |
| `Quote`         | Pull-quotes, designer notes             |
| `Caption`       | Image and table captions                |

### Applying Styles

```python
doc.add_heading("1. High Concept", level=1)          # Heading 1
doc.add_heading("1.1 Logline", level=2)               # Heading 2
doc.add_paragraph("Body text here.")                   # Normal
doc.add_paragraph("First bullet", style="List Bullet") # Bullet
```

### Customizing a Style

```python
style = doc.styles["Heading 1"]
font = style.font
font.name = "Segoe UI"
font.size = Pt(28)
font.bold = True
font.color.rgb = RGBColor(0, 102, 255)
```

### Creating a Custom Style

```python
from docx.enum.style import WD_STYLE_TYPE

callout_style = doc.styles.add_style("Callout", WD_STYLE_TYPE.PARAGRAPH)
callout_style.font.name = "Consolas"
callout_style.font.size = Pt(10)
callout_style.font.italic = True
callout_style.font.color.rgb = RGBColor(80, 80, 80)
callout_style.paragraph_format.left_indent = Inches(0.5)
```

---

## 4. Text Formatting

### Paragraph-Level

```python
para = doc.add_paragraph()
para.alignment = WD_ALIGN_PARAGRAPH.CENTER
fmt = para.paragraph_format
fmt.space_before = Pt(6)
fmt.space_after  = Pt(12)
fmt.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
fmt.first_line_indent = Inches(0.25)
```

### Run-Level (Inline Formatting)

```python
para = doc.add_paragraph()
run = para.add_run("Bold text")
run.bold = True

run2 = para.add_run(" and italic")
run2.italic = True

run3 = para.add_run(" with color")
run3.font.color.rgb = RGBColor(255, 0, 0)
run3.font.size = Pt(14)
run3.font.underline = True
```

---

## 5. Tables

### Basic Table

```python
table = doc.add_table(rows=3, cols=4)
table.style = "Light Grid Accent 1"
table.alignment = WD_TABLE_ALIGNMENT.CENTER
```

### Populating Cells

```python
header = table.rows[0].cells
header[0].text = "Stat"
header[1].text = "Base"
header[2].text = "Growth"
header[3].text = "Cap"

data = [
    ("Health",    "100", "+15/lvl", "500"),
    ("Attack",    "12",  "+3/lvl",  "80"),
]
for i, row_data in enumerate(data, start=1):
    row = table.rows[i].cells
    for j, val in enumerate(row_data):
        row[j].text = val
```

### Adding Rows Dynamically

```python
row_cells = table.add_row().cells
row_cells[0].text = "Defense"
row_cells[1].text = "8"
```

### Setting Column Widths

```python
from docx.shared import Inches

table.columns[0].width = Inches(2.0)
table.columns[1].width = Inches(1.5)
```

### Shading Header Row

```python
for cell in table.rows[0].cells:
    shading = parse_xml(
        f'<w:shd {nsdecls("w")} w:fill="0066FF"/>'
    )
    cell._tc.get_or_add_tcPr().append(shading)
    for p in cell.paragraphs:
        for run in p.runs:
            run.font.color.rgb = RGBColor(255, 255, 255)
            run.font.bold = True
```

### Merging Cells

```python
cell_a = table.cell(0, 0)
cell_b = table.cell(0, 3)
cell_a.merge(cell_b)
cell_a.text = "Character Stat Overview"
```

---

## 6. Images

### Insert Image at Full Width

```python
doc.add_picture("concept_art.png", width=Inches(6.5))
```

### Insert Image Inline

```python
para = doc.add_paragraph()
run = para.add_run()
run.add_picture("icon.png", width=Inches(0.5))
```

### Add a Caption Below an Image

```python
doc.add_picture("map_overview.png", width=Inches(5))
caption = doc.add_paragraph("Figure 1: World Map Overview", style="Caption")
caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
```

---

## 7. Page Breaks

### Explicit Page Break

```python
doc.add_page_break()
```

### Page Break Before a Paragraph (keep-with-next style)

```python
para = doc.add_heading("2. Gameplay", level=1)
para.paragraph_format.page_break_before = True
```

---

## 8. Headers & Footers

### Simple Text Header

```python
section = doc.sections[0]
header = section.header
header.is_linked_to_previous = False
header_para = header.paragraphs[0]
header_para.text = "INFINITE VOYAGE - Game Design Document v1.5"
header_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
header_para.style = doc.styles["Normal"]
for run in header_para.runs:
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(150, 150, 150)
```

### Footer with Page Numbers

```python
footer = section.footer
footer.is_linked_to_previous = False
footer_para = footer.paragraphs[0]
footer_para.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Helper to add a Word field
def add_field(run, field_code):
    fldChar_begin = OxmlElement("w:fldChar")
    fldChar_begin.set(qn("w:fldCharType"), "begin")
    run._r.append(fldChar_begin)

    instrText = OxmlElement("w:instrText")
    instrText.set(qn("xml:space"), "preserve")
    instrText.text = field_code
    run._r.append(instrText)

    fldChar_end = OxmlElement("w:fldChar")
    fldChar_end.set(qn("w:fldCharType"), "end")
    run._r.append(fldChar_end)

run_prefix = footer_para.add_run("Page ")
run_prefix.font.size = Pt(9)

run_page = footer_para.add_run()
add_field(run_page, "PAGE")
run_page.font.size = Pt(9)

run_of = footer_para.add_run(" of ")
run_of.font.size = Pt(9)

run_total = footer_para.add_run()
add_field(run_total, "NUMPAGES")
run_total.font.size = Pt(9)
```

### Different First Page Header (for Cover Page)

```python
section.different_first_page_header_footer = True
first_header = section.first_page_header
first_header.paragraphs[0].text = ""   # blank on cover page
```

---

## 9. Table of Contents

Word TOC fields are generated from heading styles. python-docx inserts the
field code; Word populates it when the document is opened.

```python
def insert_toc(doc, levels="1-3"):
    """Insert a TOC field that Word auto-generates on open/update."""
    para = doc.add_paragraph()
    run = para.add_run()

    fld_begin = OxmlElement("w:fldChar")
    fld_begin.set(qn("w:fldCharType"), "begin")
    run._r.append(fld_begin)

    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = f' TOC \\o "{levels}" \\h \\z \\u '
    run._r.append(instr)

    fld_end = OxmlElement("w:fldChar")
    fld_end.set(qn("w:fldCharType"), "end")
    run._r.append(fld_end)

    return para

# Usage
doc.add_heading("Table of Contents", level=1)
insert_toc(doc, levels="1-3")
doc.add_page_break()
```

After opening the generated .docx in Word, press Ctrl+A then F9 to refresh
the TOC.

---

## 10. Cover Page

A full cover page recipe combining several techniques above.

```python
def create_cover_page(doc, title, subtitle, version, studio, date_str):
    """Build a branded cover page for the GDD."""
    # Vertical spacing
    for _ in range(5):
        doc.add_paragraph()

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p_title.add_run(title)
    r.font.size = Pt(48)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0, 102, 255)

    # Subtitle
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = p_sub.add_run(subtitle)
    r2.font.size = Pt(24)
    r2.font.color.rgb = RGBColor(100, 100, 100)

    # Spacer
    doc.add_paragraph()

    # Metadata table
    meta = doc.add_table(rows=4, cols=2)
    meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("Version", version),
        ("Date", date_str),
        ("Studio", studio),
        ("Classification", "CONFIDENTIAL"),
    ]
    for i, (label, value) in enumerate(meta_data):
        meta.rows[i].cells[0].text = label
        meta.rows[i].cells[1].text = value

    doc.add_page_break()

# Example call
create_cover_page(
    doc,
    title="INFINITE VOYAGE",
    subtitle="Game Design Document",
    version="1.5",
    studio="Voyage Interactive",
    date_str=datetime.now().strftime("%B %d, %Y"),
)
```

---

## 11. Section Status Badges

Color-coded status indicators that appear next to each section heading.

```python
STATUS_COLORS = {
    "Final":   RGBColor(34, 139, 34),
    "Review":  RGBColor(30, 120, 200),
    "Draft":   RGBColor(200, 150, 50),
    "Concept": RGBColor(200, 60, 60),
}

def add_status_badge(paragraph, status):
    run = paragraph.add_run(f"  [{status}]")
    run.font.size = Pt(10)
    run.font.bold = True
    run.font.color.rgb = STATUS_COLORS.get(status, RGBColor(128, 128, 128))

# Usage
heading = doc.add_heading("2.1 Combat System", level=2)
add_status_badge(heading, "Review")
```

---

## 12. Bookmarks & Internal Hyperlinks

### Creating a Bookmark

```python
def add_bookmark(paragraph, bookmark_name):
    tag = OxmlElement("w:bookmarkStart")
    tag.set(qn("w:id"), "0")
    tag.set(qn("w:name"), bookmark_name)
    paragraph._p.append(tag)

    tag_end = OxmlElement("w:bookmarkEnd")
    tag_end.set(qn("w:id"), "0")
    paragraph._p.append(tag_end)
```

### Linking to a Bookmark

```python
def add_internal_hyperlink(paragraph, bookmark_name, display_text):
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("w:anchor"), bookmark_name)

    run_elem = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0066FF")
    rPr.append(color)
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rPr.append(u)
    run_elem.append(rPr)

    text = OxmlElement("w:t")
    text.text = display_text
    run_elem.append(text)
    hyperlink.append(run_elem)

    paragraph._p.append(hyperlink)
```

---

## 13. Complete GDD Assembly Pattern

Putting it all together in a single generation pipeline.

```python
def build_gdd(gdd_data, output_path):
    doc = Document()

    # 1. Cover page
    create_cover_page(
        doc,
        title=gdd_data["title"],
        subtitle="Game Design Document",
        version=gdd_data["version"],
        studio=gdd_data["studio"],
        date_str=gdd_data["date"],
    )

    # 2. Table of contents
    doc.add_heading("Table of Contents", level=1)
    insert_toc(doc)
    doc.add_page_break()

    # 3. Sections from index
    for chapter in gdd_data["chapters"]:
        h1 = doc.add_heading(chapter["title"], level=1)
        h1.paragraph_format.page_break_before = True
        add_status_badge(h1, chapter.get("status", "Draft"))

        for para_text in chapter.get("paragraphs", []):
            doc.add_paragraph(para_text)

        for section in chapter.get("sections", []):
            h2 = doc.add_heading(section["title"], level=2)
            add_status_badge(h2, section.get("status", "Draft"))
            for para_text in section.get("paragraphs", []):
                doc.add_paragraph(para_text)

    # 4. Headers and footers
    for section in doc.sections:
        section.different_first_page_header_footer = True
        hdr = section.header
        hdr.paragraphs[0].text = f"{gdd_data['title']} - GDD v{gdd_data['version']}"

    # 5. Save
    doc.save(output_path)
    return output_path
```

---

## 14. Common Pitfalls

| Problem | Cause | Fix |
|---|---|---|
| TOC shows "No table of contents entries found" | Headings not using built-in styles | Use `doc.add_heading()` not manual bold |
| Images blurry in Word | DPI too low | Supply images at 150+ DPI |
| Page numbers not showing | Fields not updated | Open in Word, Ctrl+A, F9 |
| Table overflows page | Column widths exceed margins | Set explicit widths or use autofit |
| Style not found error | Style name mismatch | Use exact names: "List Bullet" not "Bullet List" |
| Footer repeats first-page header | `is_linked_to_previous` still True | Set `is_linked_to_previous = False` |

---

## 15. Useful Constants

```python
# Infinite Voyage brand palette
IV_BLUE    = RGBColor(0, 102, 255)
IV_DARK    = RGBColor(20, 20, 40)
IV_ORANGE  = RGBColor(255, 153, 0)
IV_LIGHT   = RGBColor(240, 245, 255)
IV_GREY    = RGBColor(100, 100, 100)

# Standard GDD margins
MARGIN = Inches(1)

# Standard heading sizes
H1_SIZE = Pt(28)
H2_SIZE = Pt(22)
H3_SIZE = Pt(16)
H4_SIZE = Pt(13)
BODY_SIZE = Pt(11)
```
