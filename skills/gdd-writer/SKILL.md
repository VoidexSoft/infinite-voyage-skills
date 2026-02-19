---
name: gdd-writer
description: >
  GDD compilation and formatting specialist for Infinite Voyage. Use this skill whenever the user needs to export
  game design document sections into a professional, formatted Word document. Handles: compiling GDD index into single
  document, adding table of contents, headers, page breaks, page numbers, section status indicators, version tracking,
  professional styling for stakeholder review. Trigger when exporting GDD for publisher review, stakeholder presentations,
  milestone documentation, or compiling final design reference. Keywords: compile GDD, export document, TOC, page numbers,
  version tracking, stakeholder review, formatting, professional document. This skill transforms scattered design notes
  from gdd-manager into a polished, printable reference document suitable for publishers, investors, and stakeholders.
---

# GDD Writer (Document Compiler)

You are a technical writer and document architect who understands that a great GDD is both comprehensive and navigable.
Your role is to take the structured index from gdd-manager and compile it into a professional, visually coherent Word
document suitable for stakeholder review, publisher pitches, and team reference. You leverage the `docx` skill to
produce formatted, branded documents with proper structure, navigation aids, and visual hierarchy.

## Design Philosophy

### Readable & Navigable

Game design documents must be easy to find information in:

1. **Table of Contents** — Auto-generated from headers for quick navigation
2. **Section headers** — Clear visual hierarchy (H1 for chapters, H2 for sections, H3 for subsections)
3. **Page breaks** — Strategic breaks prevent sections from appearing mid-page
4. **Page numbers & footers** — Document-wide navigation aids
5. **Bookmarks & links** — Internal cross-references are clickable (Word hyperlinks)

### Visually Professional

Document appearance matters for stakeholder credibility:

- **Consistent styling** — Fonts, colors, spacing follow branded guidelines
- **Visual hierarchy** — Section importance visible at a glance
- **Branded header/footer** — Game logo and project name on every page
- **Status indicators** — Color coding shows which sections are final vs. WIP
- **Proper spacing** — Whitespace prevents wall-of-text appearance

### Version Controlled

Change management is essential for collaborative design:

- **Version number** — Document title page shows version and date
- **Change log** — Final pages list what changed since last version
- **Author attribution** — Sections credited to their primary designer
- **Approval stamps** — Shows who reviewed and approved each major section
- **Revision history** — Tracks document evolution (v0.1 → v1.0 → v1.5)

### Well-Integrated

The document pulls from and links to:

- **GDD manager index** — Canonical source of all sections and metadata
- **Game-balancer outputs** — Balance verification and metrics embedded
- **Narrative assets** — Dialogue samples, character descriptions, story outlines
- **Level designs** — Layout diagrams and progression requirements
- **Art style guide** — Visual reference for consistency
- **Technical specs** — Engine requirements and system architecture

## Core Workflow

### 1. Gather Index from GDD-Manager

Before compiling, retrieve the canonical GDD structure:

1. **Access gdd-manager output** — JSON or Markdown index listing all sections
2. **Read metadata** — Title, version, authors, last updated, status
3. **Parse section hierarchy** — Understand chapter → section → subsection nesting
4. **Check completeness** — Flag missing or WIP sections
5. **Collect status flags** — Which sections are Concept, Draft, Review, Final?

### 2. Plan Document Structure

Decide how to organize the output:

1. **Cover page** — Game title, version, date, studio name
2. **Executive summary** — 1-2 page overview for busy stakeholders
3. **Table of contents** — Auto-generated from headers
4. **Main sections** — Chapter-by-chapter content from gdd-manager
5. **Appendices** — Glossary, reference tables, art style guide
6. **Version history** — Change log and approvals
7. **Back matter** — Contact info, credits, legal notices

### 3. Import Content from GDD-Manager

Pull sections from the structured source:

1. **Read each section** from gdd-manager output
2. **Preserve formatting** — Headers, bold, lists, tables stay intact
3. **Embed images** — Art references, diagrams, interface mockups
4. **Add status badges** — Visual indicators for section completeness
5. **Link references** — Cross-references become clickable (e.g., "see Systems Design section")

### 4. Apply Formatting & Styling

Make the document professional and consistent:

1. **Define styles** — Heading 1, Heading 2, Body text, Callout boxes
2. **Apply branded colors** — Game logo colors in headers, accents
3. **Set margins & spacing** — Professional 1-inch margins, 1.5-line spacing
4. **Add page breaks** — Between major chapters
5. **Insert page numbers** — Footer with "Page X of Y" format
6. **Create headers/footers** — Game name, version, project code

### 5. Generate Navigation Aids

Make content findable:

1. **Table of Contents** — Click to jump to section (Word field, auto-generated)
2. **Bookmarks** — Create internal links for cross-references
3. **Section numbering** — 1. Overview, 1.1 Setting, 1.2 Tone, etc.
4. **Index** — List of key terms with page numbers
5. **Visual status bar** — Section status color-coded

### 6. Add Change Log & Metadata

Document version control:

1. **Title page** — Version number, date, authors
2. **Change log sheet** — What changed in this version?
3. **Approval page** — Signatures (digital or placeholder) from lead designer, director
4. **Contributors list** — Credit all section authors
5. **Distribution note** — "CONFIDENTIAL - Internal Use Only" if applicable

## Document Structure Template

Standard GDD Word document layout:

```
Front Matter
├─ Cover Page
│  ├─ Game Title (large, branded)
│  ├─ Version: X.X
│  ├─ Date: ISO 8601
│  ├─ Studio Name & Logo
│  └─ Confidentiality stamp
│
├─ Executive Summary (1-2 pages)
│  ├─ One-paragraph pitch
│  ├─ Core pillars (3-5 bullet points)
│  ├─ Target audience
│  ├─ Key differentiators
│  └─ Success criteria
│
├─ Quick Facts (1 page table)
│  ├─ Genre, Platform, Target Age
│  ├─ Estimated length, team size, budget
│  └─ Key milestones & dates
│
├─ Table of Contents (auto-generated)

Main Content
├─ 1. High Concept
│  ├─ 1.1 Logline
│  ├─ 1.2 Setting
│  ├─ 1.3 Core Premise
│  └─ 1.4 Target Audience
│
├─ 2. Gameplay
│  ├─ 2.1 Core Mechanics
│  ├─ 2.2 Progression System
│  ├─ 2.3 Combat / Interaction Model
│  └─ 2.4 Victory Conditions
│
├─ 3. Story & Narrative
│  ├─ 3.1 Story Overview
│  ├─ 3.2 Characters
│  ├─ 3.3 Dialogue & Tone
│  └─ 3.4 Narrative Flow
│
├─ 4. Art & Visuals
│  ├─ 4.1 Visual Style
│  ├─ 4.2 Character Design
│  ├─ 4.3 Environment Design
│  └─ 4.4 UI/UX Style Guide
│
├─ 5. Audio & Music
│  ├─ 5.1 Sound Direction
│  ├─ 5.2 Music Themes
│  ├─ 5.3 Voice Acting
│  └─ 5.4 SFX Reference
│
├─ 6. Systems & Mechanics
│  ├─ 6.1 Inventory System
│  ├─ 6.2 Ability/Skill System
│  ├─ 6.3 Equipment & Progression
│  └─ 6.4 Economy Model
│
├─ 7. Level Design
│  ├─ 7.1 Level Structure
│  ├─ 7.2 Progression Curve
│  ├─ 7.3 Key Encounters
│  └─ 7.4 Level Layouts
│
├─ 8. Technical Specifications
│  ├─ 8.1 Engine & Tools
│  ├─ 8.2 Performance Targets
│  ├─ 8.3 Platform-Specific Notes
│  └─ 8.4 Technical Dependencies

Back Matter
├─ A. Appendix: Glossary
├─ B. Appendix: Reference Tables
├─ C. Appendix: Character Stats
├─ D. Appendix: Item Database Summary
├─ E. Change Log & Version History
├─ F. Approvals & Sign-Off
└─ G. Distribution & Legal Notice
```

## Python (python-docx) Code Examples

Use the `python-docx` library to automate GDD document creation.

### Example 1: Create Cover Page with Branding

```python
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from datetime import datetime

# Create document
doc = Document()

# Set margins
sections = doc.sections
for section in sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

# Cover Page
# Add some space
for _ in range(4):
    doc.add_paragraph()

# Title
title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
title_run = title.add_run("INFINITE VOYAGE")
title_run.font.size = Pt(48)
title_run.font.bold = True
title_run.font.color.rgb = RGBColor(0, 102, 255)  # Game's primary color

# Tagline
tagline = doc.add_paragraph()
tagline.alignment = WD_ALIGN_PARAGRAPH.CENTER
tagline_run = tagline.add_run("Game Design Document")
tagline_run.font.size = Pt(24)
tagline_run.font.color.rgb = RGBColor(100, 100, 100)

# Space
doc.add_paragraph()
doc.add_paragraph()

# Metadata table
metadata_table = doc.add_table(rows=6, cols=2)
metadata_table.autofit = False
metadata_table.allow_autofit = False

# Set table width
metadata_table.width = Inches(4)

# Fill in metadata
cells = metadata_table.rows[0].cells
cells[0].text = "Version"
cells[1].text = "1.5"

cells = metadata_table.rows[1].cells
cells[0].text = "Date"
cells[1].text = datetime.now().strftime("%B %d, %Y")

cells = metadata_table.rows[2].cells
cells[0].text = "Studio"
cells[1].text = "Your Game Studio"

cells = metadata_table.rows[3].cells
cells[0].text = "Project Code"
cells[1].text = "INFINITE_VOYAGE_2025"

cells = metadata_table.rows[4].cells
cells[0].text = "Status"
cells[1].text = "Review Phase"

cells = metadata_table.rows[5].cells
cells[0].text = "Lead Designer"
cells[1].text = "Design Team"

# Confidentiality notice
doc.add_paragraph()
doc.add_paragraph()
confidential = doc.add_paragraph()
confidential.alignment = WD_ALIGN_PARAGRAPH.CENTER
conf_run = confidential.add_run("CONFIDENTIAL - INTERNAL USE ONLY")
conf_run.font.size = Pt(14)
conf_run.font.bold = True
conf_run.font.color.rgb = RGBColor(255, 0, 0)

# Page break
doc.add_page_break()

# Save
doc.save("Infinite_Voyage_GDD_v1.5.docx")
print("Cover page created: Infinite_Voyage_GDD_v1.5.docx")
```

### Example 2: Add Content with Auto-Generated TOC

```python
from docx import Document
from docx.shared import Pt, RGBColor
from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml

def add_toc(doc):
    """Add a table of contents field (Word will auto-generate on open)"""
    # This inserts a TOC field that Word auto-generates
    paragraph = doc.add_paragraph()
    run = paragraph.add_run()
    fldChar1 = parse_xml(r'<w:fldChar {} w:fldCharType="begin"/>'.format(nsdecls('w')))
    instrText = parse_xml(r'<w:instrText {} w:space="preserve">TOC \o "1-2" \h \z \u</w:instrText>'.format(nsdecls('w')))
    fldChar2 = parse_xml(r'<w:fldChar {} w:fldCharType="end"/>'.format(nsdecls('w')))

    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)

# Load document
doc = Document("Infinite_Voyage_GDD_v1.5.docx")

# Add TOC after cover
doc.add_page_break()
add_toc(doc)
doc.add_page_break()

# Add sections as Heading 1, Heading 2, etc.
# These will appear in the auto-generated TOC

h1 = doc.add_heading("1. High Concept", level=1)
doc.add_paragraph("Infinite Voyage is a narrative-driven space exploration RPG where players discover ancient civilizations across the stars.")

h2 = doc.add_heading("1.1 Logline", level=2)
doc.add_paragraph("A lone archaeologist travels the galaxy, unraveling the mystery of a vanished cosmic empire while managing resources and making moral choices that reshape civilization.")

h2 = doc.add_heading("1.2 Setting", level=2)
doc.add_paragraph("Year 2847. The Kepler Sector. Recently colonized space where remnants of an ancient, advanced civilization lay dormant in ruins across multiple star systems.")

doc.add_page_break()

h1 = doc.add_heading("2. Gameplay", level=1)
doc.add_paragraph("Core loop: Explore → Discover → Research → Upgrade → Explore further")

h2 = doc.add_heading("2.1 Core Mechanics", level=2)
doc.add_paragraph("Players manage exploration via starship, land on planets, solve puzzles, and battle hostile creatures. Combat is turn-based tactical.")

doc.save("Infinite_Voyage_GDD_v1.5_with_toc.docx")
print("TOC added. When you open the document in Word, update fields (Ctrl+A, F9) to generate TOC.")
```

### Example 3: Import Content from GDD-Manager Index

```python
import json
from docx import Document
from docx.shared import Pt
from pathlib import Path

def load_gdd_index(index_file):
    """Load GDD structure from gdd-manager output"""
    with open(index_file, 'r') as f:
        return json.load(f)

def import_gdd_sections(doc, gdd_index):
    """Add all sections from gdd-manager to document"""
    for section in gdd_index['sections']:
        # Add chapter heading
        doc.add_heading(section['title'], level=1)

        # Add content if available
        if 'content' in section:
            doc.add_paragraph(section['content'])

        # Add subsections
        if 'subsections' in section:
            for subsection in section['subsections']:
                doc.add_heading(subsection['title'], level=2)

                if 'content' in subsection:
                    doc.add_paragraph(subsection['content'])

                # Add sub-subsections
                if 'subsections' in subsection:
                    for sub_subsection in subsection['subsections']:
                        doc.add_heading(sub_subsection['title'], level=3)
                        if 'content' in sub_subsection:
                            doc.add_paragraph(sub_subsection['content'])

        # Page break between chapters
        doc.add_page_break()

# Load GDD index from gdd-manager
gdd_index = load_gdd_index("gdd_manager_index.json")

# Create document
doc = Document()

# Import all sections
import_gdd_sections(doc, gdd_index)

doc.save("Infinite_Voyage_GDD_compiled.docx")
print("GDD compiled from index.")
```

### Example 4: Add Status Indicators and Version Tracking

```python
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from datetime import datetime

doc = Document()

# Status color coding
STATUS_COLORS = {
    "Concept": RGBColor(200, 100, 100),  # Red
    "Draft": RGBColor(200, 150, 100),    # Orange
    "Review": RGBColor(100, 150, 200),   # Blue
    "Final": RGBColor(100, 200, 100),    # Green
}

def add_section_with_status(doc, title, status, content, author):
    """Add a section with status badge and metadata"""
    # Heading
    heading = doc.add_heading(title, level=2)

    # Status badge
    status_para = doc.add_paragraph()
    status_run = status_para.add_run(f"[{status}]")
    status_run.font.bold = True
    status_run.font.size = Pt(11)
    status_run.font.color.rgb = STATUS_COLORS.get(status, RGBColor(100, 100, 100))

    # Author info
    meta_para = doc.add_paragraph(f"Author: {author} | Last Updated: {datetime.now().strftime('%Y-%m-%d')}")
    meta_para.style = 'Normal'
    for run in meta_para.runs:
        run.font.size = Pt(9)
        run.font.italic = True
        run.font.color.rgb = RGBColor(150, 150, 150)

    # Content
    doc.add_paragraph(content)

# Add sections with status
add_section_with_status(
    doc,
    "1.1 Logline",
    "Final",
    "A lone archaeologist travels the galaxy, unraveling the mystery of a vanished cosmic empire.",
    "Sarah Chen"
)

add_section_with_status(
    doc,
    "2.1 Combat System",
    "Review",
    "Turn-based tactical combat with action economy: each character has 2 actions per turn.",
    "Marcus Rodriguez"
)

add_section_with_status(
    doc,
    "3.1 Story Outline",
    "Draft",
    "The main character discovers evidence of an ancient civilization. Three acts, multiple endings.",
    "Jessica Park"
)

add_section_with_status(
    doc,
    "4.1 Visual Style",
    "Concept",
    "Sci-fi aesthetic with bioluminescent alien flora. Inspired by No Man's Sky and Outer Wilds.",
    "David Thompson"
)

# Version history table
doc.add_page_break()
doc.add_heading("Change Log & Version History", level=1)

history_table = doc.add_table(rows=5, cols=4)
history_table.style = 'Light Grid Accent 1'

# Header row
header_cells = history_table.rows[0].cells
header_cells[0].text = "Version"
header_cells[1].text = "Date"
header_cells[2].text = "Changes"
header_cells[3].text = "Author"

# Data rows
rows = [
    ["1.5", "2025-02-19", "Added combat system details, updated economy model", "Sarah Chen"],
    ["1.4", "2025-02-10", "Finalized narrative structure, added character profiles", "Jessica Park"],
    ["1.3", "2025-01-28", "Refined gameplay mechanics, added progression curve", "Marcus Rodriguez"],
    ["1.2", "2025-01-15", "Initial visual style guide and art references", "David Thompson"],
]

for i, row_data in enumerate(rows, 1):
    row = history_table.rows[i]
    for j, cell_data in enumerate(row_data):
        row.cells[j].text = cell_data

doc.save("Infinite_Voyage_GDD_with_status.docx")
print("GDD with status indicators created.")
```

### Example 5: Add Headers, Footers, and Page Numbers

```python
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.shared import OxmlElement

def add_header_footer(doc, game_name, version):
    """Add branded header and footer to all pages"""
    section = doc.sections[0]

    # Header
    header = section.header
    header_para = header.paragraphs[0]
    header_para.text = f"{game_name} - GDD v{version}"
    header_para.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Footer with page numbers
    footer = section.footer
    footer_para = footer.paragraphs[0]
    footer_para.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Add page number field
    run = footer_para.add_run()
    fldChar1 = OxmlElement('w:fldChar')
    fldChar1.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}fldCharType', 'begin')

    instrText = OxmlElement('w:instrText')
    instrText.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}space', 'preserve')
    instrText.text = 'PAGE \\* MERGEFORMAT'

    fldChar2 = OxmlElement('w:fldChar')
    fldChar2.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}fldCharType', 'end')

    run._element.append(fldChar1)
    run._element.append(instrText)
    run._element.append(fldChar2)

    # Add page count
    footer_para.add_run(' of ')

    run2 = footer_para.add_run()
    fldChar3 = OxmlElement('w:fldChar')
    fldChar3.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}fldCharType', 'begin')

    instrText2 = OxmlElement('w:instrText')
    instrText2.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}space', 'preserve')
    instrText2.text = 'NUMPAGES \\* MERGEFORMAT'

    fldChar4 = OxmlElement('w:fldChar')
    fldChar4.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}fldCharType', 'end')

    run2._element.append(fldChar3)
    run2._element.append(instrText2)
    run2._element.append(fldChar4)

# Create document and add header/footer
doc = Document()
add_header_footer(doc, "INFINITE VOYAGE", "1.5")

# Add content
doc.add_heading("Game Design Document", level=1)
doc.add_paragraph("This is the main GDD content...")

# Add multiple pages to show header/footer
for i in range(3):
    doc.add_page_break()
    doc.add_heading(f"Section {i+2}", level=1)
    doc.add_paragraph(f"Page {i+2} content...")

doc.save("Infinite_Voyage_GDD_with_header_footer.docx")
print("Document with header/footer and page numbers created.")
```

## Integration with Other Skills

### GDD-Manager

**From gdd-manager:**
- Canonical GDD index structure (JSON or Markdown)
- Section metadata (title, author, status, last modified)
- Complete content for all sections
- Cross-reference data (which sections link to which)

**To gdd-manager:**
- Document export confirmation (which version was compiled)
- Feedback from review (sections flagged for updates)
- Version bumps and approvals

### Game-Balancer

**From game-balancer:**
- Balance verification reports (is the game balanced?)
- Metrics and statistics (DPS, survivability, economy stability)
- Recommended changes (ability costs, stat adjustments)

**To game-balancer:**
- System descriptions and intended balance targets
- References to balance assumptions in the design

### Narrative Designer

**From narrative-designer:**
- Story outline and plot summary
- Character descriptions and dialogue samples
- Narrative beats and key story moments

**To narrative-designer:**
- Document status (review phase? ready for final?)
- Feedback from stakeholders on story sections
- Change requests for narrative sections

### Level Designer

**From level-designer:**
- Level progression curve and layout diagrams
- Key encounters and enemy compositions
- Progression gates and story integration

**To level-designer:**
- Level design guidelines and constraints
- Document status and deadline

## Best Practices

### Document Organization

1. **One section per page** — Avoids orphaning headers
2. **Consistent hierarchy** — Heading 1 = chapters, Heading 2 = sections, Heading 3 = details
3. **Use page breaks** — Between major chapters for clean page breaks
4. **Proper indentation** — Lists and sublists clearly nested
5. **Table of contents** — Always auto-generated from headings

### Content Quality

1. **Concise writing** — 1-2 pages per section maximum
2. **Visual breaks** — Bullet points, tables, and diagrams prevent walls of text
3. **Cross-references** — Link to related sections ("see Section 2.1")
4. **Images & diagrams** — Art references and UI mockups integrated
5. **Consistent terminology** — Use glossary to avoid ambiguity

### Professional Presentation

1. **Branded styling** — Use game's primary colors and logo
2. **Consistent fonts** — Heading font and body font selected beforehand
3. **Proper margins** — 1 inch on all sides (standard)
4. **Line spacing** — 1.5x for readability
5. **Status indicators** — Color-coded section status (Concept, Draft, Review, Final)

### Version Control

1. **Version numbers** — Semantic versioning (1.0, 1.1, 1.5, 2.0)
2. **Change log** — Every version lists what changed
3. **Author attribution** — Sections credit their primary designer
4. **Approval stamps** — Digital or placeholder signatures from leadership
5. **Distribution notes** — "CONFIDENTIAL - INTERNAL USE ONLY" if applicable

## Output Format

GDD documents are delivered as `.docx` (Microsoft Word) files. Standard naming:

- **Format:** `[GameName]_GDD_v[Version].docx`
- **Example:** `Infinite_Voyage_GDD_v1.5.docx`

Document includes:
- Cover page with metadata
- Executive summary
- Table of contents (auto-generated)
- Full content from gdd-manager
- Appendices (glossary, reference tables)
- Change log and version history
- Approvals and sign-off

All GDD documents are version controlled and tracked in design repository.

## References

- `templates/gdd-cover-page.docx` — Template for professional cover pages
- `templates/gdd-structure.docx` — Standard section hierarchy
- `templates/gdd-styles.docx` — Branded styles and formatting
- `references/python-docx-guide.md` — Automation cookbook
- `references/gdd-writing-style.md` — Tone and voice guidelines
- `references/stakeholder-document-checklist.md` — What stakeholders expect to see
