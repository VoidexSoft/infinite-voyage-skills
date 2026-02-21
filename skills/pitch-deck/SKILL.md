---
name: pitch-deck
description: >
  Pitch presentation specialist for game development. Use this skill whenever the user needs to create professional
  slide presentations for publishers, investors, milestone reviews, or team presentations. Handles: publisher pitch
  decks, investor presentations, milestone review decks, team presentations, game reveal decks, and funding pitches.
  Includes standard slide structures for game pitches (hook, vision, gameplay, market, team, ask), visual style
  guidelines, speaker notes, and backup slides. Trigger when pitching to publishers, seeking investment, presenting
  milestones, or conducting team presentations. Keywords: pitch deck, publisher pitch, investor presentation, slide
  deck, game pitch, presentation, milestone presentation, team presentation. This skill transforms game design into
  persuasive, visually compelling presentations that secure funding, greenlight approvals, and team alignment.
---

# Pitch Deck Specialist

You are a presentation strategist and visual communicator who understands that game pitches succeed on clarity,
passion, and credibility. Your role is to transform game design into compelling slide decks suitable for publishers,
investors, team presentations, and milestone reviews. You leverage the `pptx` skill to produce professional,
branded presentations that tell the game's story in minutes while leaving decision-makers convinced and engaged.

## Design Philosophy

### Compelling & Persuasive

Great pitch decks convince people to invest:

1. **Hook first** — Open with the most compelling idea, not the title
2. **Clear ask** — Explicit request (funding amount, approval, partnership)
3. **Problem-solution pairing** — Why does this game matter? What problem does it solve?
4. **Proof points** — Playtesting feedback, market analysis, competitive advantages
5. **Emotional resonance** — Game passion should be visible and contagious

### Visually Professional

Presentation quality reflects on the game:

- **Consistent branding** — Game colors, fonts, logo on every slide
- **High-quality visuals** — Gameplay footage, concept art, not placeholders
- **Minimal text** — Bullets, not paragraphs; speaker delivers the words
- **Strong imagery** — One powerful image per slide (not cluttered layouts)
- **Data visualization** — Charts, graphs for market/financial data

### Structured & Navigable

Audiences need clear flow:

- **Agenda slide** — What's coming? ("5 minutes covering: Vision, Gameplay, Market")
- **Section headers** — Clear topic transitions
- **Progress indicators** — Subtle visual cues showing progress through deck (dots, bar, slide count)
- **Backup slides** — Deep-dive content not needed in main pitch
- **Speaker notes** — Detailed talking points for each slide

### Flexible & Modular

Different audiences need different emphasis:

- **Publisher pitch** — Gameplay first, market second, team third
- **Investor pitch** — Market & financials first, gameplay second, team third
- **Team presentation** — Vision first, milestones second, roadmap third
- **Milestone review** — Progress first, challenges second, next steps third
- **Game reveal** — Gameplay hook first, story second, release date last

## Core Workflow

### 1. Define Your Audience & Ask

Before building slides, clarify who you're pitching and what you want:

1. **Who is listening?** (Publishers, investors, team, press, players)
2. **What is your ask?** ($2M funding, greenlight approval, partnership, hype)
3. **How much time do you have?** (30 seconds elevator pitch, 5-minute deck, 20-minute presentation)
4. **What do they care about?** (Market size, gameplay innovation, team track record, ROI)
5. **What objections will they have?** (Prepare counter-evidence)

### 2. Structure the Story

Plan your narrative arc:

1. **Opening hook** (30 seconds) — The one thing that grabs attention
2. **Problem statement** (1 minute) — Why does this game matter?
3. **Vision & pillars** (1 minute) — Core design philosophy
4. **Gameplay walkthrough** (2 minutes) — Show actual mechanics
5. **Market opportunity** (1 minute) — Why will players buy this?
6. **Team & credentials** (1 minute) — Who's shipping this?
7. **Ask & timeline** (30 seconds) — What do you need and when?
8. **Call to action** — What happens next?

### 3. Create Slide Outline

Plan each slide before designing:

Use the **Pitch Deck Template** (see section below). Map out:
- Slide title or theme
- Key talking point (1-2 sentences max)
- Visual (gameplay footage, concept art, chart, diagram)
- Speaker notes (detailed explanation)
- Transitions & animations (if needed)

### 4. Design Visually

Apply consistent, game-appropriate styling:

1. **Define color palette** — 2-3 primary colors from game branding
2. **Choose fonts** — One for headings, one for body (sans-serif for screen)
3. **Set slide master** — Logo, footer, background applied to all slides
4. **Create templates** — Reusable layouts for title, content, comparison slides
5. **Embed media** — Gameplay video, concept art, promotional assets

### 5. Add Speaker Notes

Detailed notes for presenter:

1. **What to say** — Detailed explanation of slide content
2. **Timing** — How long should this slide take? (e.g., "2 minutes")
3. **Transitions** — How does this connect to the next slide?
4. **Key callouts** — Emphasis points ("Make sure to mention our playtest results")
5. **Backup content** — If asked questions, what slides to jump to?

### 6. Prepare Backup Slides

Deep-dive content not needed in main pitch:

1. **Technical specs** — Engine, platforms, performance targets
2. **Detailed mechanics** — How does economy balancing work?
3. **Financial projections** — Revenue forecasts, cost breakdowns
4. **Character backstories** — Full character bios (if narrative-focused)
5. **Competitive analysis** — How do you compare to similar games?

## Standard Pitch Deck Structure

Typical game pitch flow:

```
Slide 1: Title Slide
- Game Title (large)
- Tagline
- Studio Name
- Date
- Optional: Press contact info

Slide 2: Opening Hook (30 sec)
- One sentence pitch
- Eye-catching image or video
- Make them lean forward

Slide 3: Problem Statement (1 min)
- What gap does this game fill?
- Market opportunity
- Why players want this

Slide 4: Vision & Pillars (1 min)
- Core design philosophy
- 3-5 key pillars
- Visual representation (e.g., three icons)

Slide 5: Gameplay Hook (1 min)
- What's the core gameplay loop?
- Gameplay screenshot or short video
- "You play as X and do Y to achieve Z"

Slide 6: Game Features (1-2 min)
- Key mechanics
- System depth
- What makes it special?

Slide 7: Visual Style (1 min)
- Art direction
- Concept art or in-game screenshot
- How does it look?

Slide 8: Narrative (1 min, if story-focused)
- Story premise
- Character hook
- Narrative depth

Slide 9: Market Opportunity (1 min)
- Target audience
- Market size
- Comparable titles
- Revenue potential

Slide 10: Team & Credentials (1 min)
- Key leadership
- Track record
- Why you'll ship this

Slide 11: Roadmap & Timeline (1 min)
- Key milestones
- Launch date
- Post-launch content

Slide 12: The Ask (30 sec)
- Funding needed (if applicable)
- Partnership type (if applicable)
- Timeline for next steps

Slide 13: Call to Action
- Contact info
- How to reach you
- Thank you
```

## Python (python-pptx) Code Examples

Automate pitch deck creation with `python-pptx`.

### Example 1: Create Branded Title Slide

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from datetime import datetime

# Create presentation with 16:9 widescreen aspect ratio
prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(5.625)

# Define branded colors
BRAND_PRIMARY = RGBColor(0, 102, 255)  # Blue
BRAND_SECONDARY = RGBColor(255, 153, 0)  # Orange
BRAND_DARK = RGBColor(20, 20, 40)  # Dark blue
BRAND_LIGHT = RGBColor(240, 245, 255)  # Light blue

# Slide 1: Title Slide
slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
background = slide.background
fill = background.fill
fill.solid()
fill.fore_color.rgb = BRAND_LIGHT

# Add background shape
background_shape = slide.shapes.add_shape(1, 0, 0, prs.slide_width, prs.slide_height)
background_shape.fill.solid()
background_shape.fill.fore_color.rgb = BRAND_DARK
background_shape.line.color.rgb = BRAND_DARK

# Add game title
title_box = slide.shapes.add_textbox(
    Inches(0.5), Inches(1.5), Inches(9), Inches(1)
)
title_frame = title_box.text_frame
title_frame.text = "INFINITE VOYAGE"
title_frame.word_wrap = True

# Format title
title_paragraph = title_frame.paragraphs[0]
title_paragraph.alignment = PP_ALIGN.CENTER
title_run = title_paragraph.runs[0]
title_run.font.size = Pt(72)
title_run.font.bold = True
title_run.font.color.rgb = BRAND_PRIMARY

# Add tagline
tagline_box = slide.shapes.add_textbox(
    Inches(0.5), Inches(2.6), Inches(9), Inches(0.5)
)
tagline_frame = tagline_box.text_frame
tagline_frame.text = "Explore. Discover. Survive."
tagline_paragraph = tagline_frame.paragraphs[0]
tagline_paragraph.alignment = PP_ALIGN.CENTER
tagline_run = tagline_paragraph.runs[0]
tagline_run.font.size = Pt(28)
tagline_run.font.color.rgb = BRAND_SECONDARY

# Add date and studio
footer_box = slide.shapes.add_textbox(
    Inches(0.5), Inches(4.8), Inches(9), Inches(0.5)
)
footer_frame = footer_box.text_frame
footer_frame.text = f"Your Game Studio | {datetime.now().strftime('%B %Y')}"
footer_paragraph = footer_frame.paragraphs[0]
footer_paragraph.alignment = PP_ALIGN.CENTER
footer_run = footer_paragraph.runs[0]
footer_run.font.size = Pt(14)
footer_run.font.color.rgb = RGBColor(150, 150, 150)

# Save
prs.save("Infinite_Voyage_Pitch_Deck.pptx")
print("Title slide created: Infinite_Voyage_Pitch_Deck.pptx")
```

### Example 2: Add Content Slides with Bullets

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

# Load presentation
prs = Presentation("Infinite_Voyage_Pitch_Deck.pptx")

BRAND_PRIMARY = RGBColor(0, 102, 255)
BRAND_DARK = RGBColor(20, 20, 40)

def add_content_slide(prs, title, bullets, speaker_notes=""):
    """Add a standard content slide with title and bullets"""
    # Use title and content layout
    slide = prs.slides.add_slide(prs.slide_layouts[1])

    # Set background
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(255, 255, 255)

    # Add title
    title_shape = slide.shapes.title
    title_shape.text = title
    title_shape.text_frame.paragraphs[0].font.size = Pt(44)
    title_shape.text_frame.paragraphs[0].font.bold = True
    title_shape.text_frame.paragraphs[0].font.color.rgb = BRAND_DARK

    # Add accent line under title
    line = slide.shapes.add_connector(1, Inches(0.5), Inches(1.1), Inches(9.5), Inches(1.1))
    line.line.color.rgb = BRAND_PRIMARY
    line.line.width = Pt(3)

    # Add bullet points
    content_shape = slide.placeholders[1]
    text_frame = content_shape.text_frame
    text_frame.clear()

    for i, bullet_text in enumerate(bullets):
        if i == 0:
            p = text_frame.paragraphs[0]
        else:
            p = text_frame.add_paragraph()

        p.text = bullet_text
        p.level = 0
        p.font.size = Pt(20)
        p.font.color.rgb = BRAND_DARK
        p.space_before = Pt(6)
        p.space_after = Pt(6)

    # Add speaker notes
    if speaker_notes:
        notes_slide = slide.notes_slide
        notes_text_frame = notes_slide.notes_text_frame
        notes_text_frame.text = speaker_notes

    return slide

# Add slides
add_content_slide(
    prs,
    "The Problem",
    [
        "Space exploration games focus on combat or survival, not discovery",
        "Players want narrative depth and meaningful exploration",
        "Market for story-driven sci-fi games is underserved",
        "Opportunity: Blend exploration, discovery, and resource management"
    ],
    speaker_notes="Emphasize the market gap. Players love games like No Man's Sky and Outer Wilds, but want deeper narrative. That's our opportunity."
)

add_content_slide(
    prs,
    "Our Vision",
    [
        "A narrative-driven space exploration RPG",
        "Discover ruins of an ancient civilization",
        "Uncover the mystery through exploration and research",
        "Make choices that reshape the galaxy"
    ],
    speaker_notes="This is Infinite Voyage. Emphasis on discovery and player agency."
)

add_content_slide(
    prs,
    "Core Pillars",
    [
        "Exploration: Vast, hand-crafted star systems to discover",
        "Discovery: Ancient technology with secrets to uncover",
        "Consequence: Your choices reshape civilization",
        "Resource Management: Manage ship systems and supplies"
    ],
    speaker_notes="Four core pillars define the game. Hit each one."
)

add_content_slide(
    prs,
    "Gameplay Loop",
    [
        "Explore: Land on planets, find ruins",
        "Discover: Research ancient technology",
        "Upgrade: Improve ship and equipment",
        "Explore Further: Access new areas with upgrades",
        "Repeat: Loop deepens with more content"
    ],
    speaker_notes="The core gameplay loop is simple but deep. Takes 2-3 minutes per cycle, scales to 50+ hours."
)

# Save
prs.save("Infinite_Voyage_Pitch_Deck.pptx")
print("Content slides added.")
```

### Example 3: Add Market/Team Slides with Tables

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

prs = Presentation("Infinite_Voyage_Pitch_Deck.pptx")

BRAND_PRIMARY = RGBColor(0, 102, 255)
BRAND_DARK = RGBColor(20, 20, 40)

# Slide: Target Market
slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank

# Title
title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.6))
title_frame = title_box.text_frame
title_frame.text = "Market Opportunity"
title_frame.paragraphs[0].font.size = Pt(44)
title_frame.paragraphs[0].font.bold = True
title_frame.paragraphs[0].font.color.rgb = BRAND_DARK

# Market data table
rows, cols = 4, 3
left = Inches(1)
top = Inches(1.2)
width = Inches(8)
height = Inches(3)

table_shape = slide.shapes.add_table(rows, cols, left, top, width, height).table

# Header row
table_shape.cell(0, 0).text = "Market Segment"
table_shape.cell(0, 1).text = "Size"
table_shape.cell(0, 2).text = "Growth"

# Data rows
data = [
    ["Story-Driven Games", "$15B", "+8% YoY"],
    ["Space Exploration Games", "$2.3B", "+12% YoY"],
    ["Indie/AA Games", "$500M", "+25% YoY"],
]

for i, row_data in enumerate(data, 1):
    for j, cell_data in enumerate(row_data):
        table_shape.cell(i, j).text = cell_data

# Speaker notes
notes_slide = slide.notes_slide
notes_slide.notes_text_frame.text = "Market is growing, especially for indie story-driven games. Infinite Voyage targets the intersection of these markets. We estimate TAM of $100M+ for a successful title."

# Save
prs.save("Infinite_Voyage_Pitch_Deck.pptx")
print("Market slide added.")
```

### Example 4: Add Team & Call-to-Action Slides

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

prs = Presentation("Infinite_Voyage_Pitch_Deck.pptx")

BRAND_PRIMARY = RGBColor(0, 102, 255)
BRAND_DARK = RGBColor(20, 20, 40)
BRAND_SECONDARY = RGBColor(255, 153, 0)

# Slide: The Team
slide = prs.slides.add_slide(prs.slide_layouts[6])

# Title
title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.6))
title_frame = title_box.text_frame
title_frame.text = "The Team"
title_frame.paragraphs[0].font.size = Pt(44)
title_frame.paragraphs[0].font.bold = True
title_frame.paragraphs[0].font.color.rgb = BRAND_DARK

# Team members
team_members = [
    ("Sarah Chen", "Game Director", "10+ years AAA experience (BioWare)"),
    ("Marcus Rodriguez", "Lead Programmer", "5 years indie dev, Unity expert"),
    ("Jessica Park", "Narrative Designer", "Published author, game writer (Telltale)"),
]

y_position = 1.2
for name, role, credentials in team_members:
    # Name
    name_box = slide.shapes.add_textbox(Inches(1), Inches(y_position), Inches(8), Inches(0.35))
    name_frame = name_box.text_frame
    name_frame.text = name
    name_frame.paragraphs[0].font.size = Pt(18)
    name_frame.paragraphs[0].font.bold = True
    name_frame.paragraphs[0].font.color.rgb = BRAND_PRIMARY

    # Role
    role_box = slide.shapes.add_textbox(Inches(1.5), Inches(y_position + 0.35), Inches(7.5), Inches(0.25))
    role_frame = role_box.text_frame
    role_frame.text = role
    role_frame.paragraphs[0].font.size = Pt(14)
    role_frame.paragraphs[0].font.bold = True
    role_frame.paragraphs[0].font.color.rgb = BRAND_DARK

    # Credentials
    cred_box = slide.shapes.add_textbox(Inches(1.5), Inches(y_position + 0.6), Inches(7.5), Inches(0.25))
    cred_frame = cred_box.text_frame
    cred_frame.text = credentials
    cred_frame.paragraphs[0].font.size = Pt(12)
    cred_frame.paragraphs[0].font.color.rgb = RGBColor(100, 100, 100)

    y_position += 1.0

# Slide: The Ask
slide = prs.slides.add_slide(prs.slide_layouts[6])

# Background color
background = slide.background
fill = background.fill
fill.solid()
fill.fore_color.rgb = BRAND_PRIMARY

# Title
title_box = slide.shapes.add_textbox(Inches(0.5), Inches(1), Inches(9), Inches(1))
title_frame = title_box.text_frame
title_frame.text = "The Ask"
title_frame.word_wrap = True
title_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
title_frame.paragraphs[0].font.size = Pt(48)
title_frame.paragraphs[0].font.bold = True
title_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)

# Amount
amount_box = slide.shapes.add_textbox(Inches(1), Inches(2.2), Inches(8), Inches(0.8))
amount_frame = amount_box.text_frame
amount_frame.text = "$2.5M Funding"
amount_frame.word_wrap = True
amount_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
amount_frame.paragraphs[0].font.size = Pt(40)
amount_frame.paragraphs[0].font.bold = True
amount_frame.paragraphs[0].font.color.rgb = BRAND_SECONDARY

# Timeline
timeline_box = slide.shapes.add_textbox(Inches(1), Inches(3.2), Inches(8), Inches(0.5))
timeline_frame = timeline_box.text_frame
timeline_frame.text = "18-month development cycle to launch"
timeline_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
timeline_frame.paragraphs[0].font.size = Pt(18)
timeline_frame.paragraphs[0].font.color.rgb = RGBColor(200, 200, 200)

# Slide: Thank You / Contact
slide = prs.slides.add_slide(prs.slide_layouts[6])

# Background
background = slide.background
fill = background.fill
fill.solid()
fill.fore_color.rgb = BRAND_DARK

# Thank you
thank_you_box = slide.shapes.add_textbox(Inches(1), Inches(1.5), Inches(8), Inches(1))
thank_you_frame = thank_you_box.text_frame
thank_you_frame.text = "Thank You"
thank_you_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
thank_you_frame.paragraphs[0].font.size = Pt(54)
thank_you_frame.paragraphs[0].font.bold = True
thank_you_frame.paragraphs[0].font.color.rgb = BRAND_PRIMARY

# Contact info
contact_box = slide.shapes.add_textbox(Inches(1), Inches(3), Inches(8), Inches(1.5))
contact_frame = contact_box.text_frame
contact_frame.word_wrap = True

contact_text = "Questions?\n\nSarah Chen | Game Director\nsarah@yourgamestudio.com | (555) 123-4567\ninfinitevoyage.com"
contact_frame.text = contact_text
contact_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
contact_frame.paragraphs[0].font.size = Pt(16)
contact_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)

for paragraph in contact_frame.paragraphs:
    paragraph.alignment = PP_ALIGN.CENTER
    for run in paragraph.runs:
        run.font.color.rgb = RGBColor(255, 255, 255)

# Save
prs.save("Infinite_Voyage_Pitch_Deck.pptx")
print("Team and call-to-action slides added. Presentation ready!")
```

## Pitch Deck Types & Customization

### Publisher Pitch (5 minutes)
Focus: Gameplay and market fit
Structure:
1. Hook (What's the game?)
2. Gameplay walkthrough (Show it in action)
3. Visual style (How does it look?)
4. Market opportunity (Who will buy this?)
5. Timeline & team (When and who?)
6. The ask (Partnership? Publishing deal?)

### Investor Pitch (10 minutes)
Focus: Market, team, financials
Structure:
1. Problem statement (Why this game matters)
2. Market opportunity (How big is it?)
3. Vision & gameplay (What makes it special?)
4. Comparable titles (Competitive analysis)
5. Financial projections (Revenue, profitability)
6. Team & track record (Why we'll succeed)
7. Funding use (What will money go toward?)
8. The ask (Equity? Debt? Partnership?)

### Team Presentation (20 minutes)
Focus: Design deep-dive
Structure:
1. Vision (Where we're going)
2. Pillars (What matters most)
3. Systems deep-dive (How it works)
4. Art direction (How it looks)
5. Narrative (Story beats)
6. Progression curve (How it scales)
7. Challenges & solutions (What's hard? How are we solving it?)
8. Roadmap & timeline (Key milestones)

### Milestone Review (15 minutes)
Focus: Progress and next steps
Structure:
1. Last milestone recap (What we said we'd do)
2. What we shipped (What we actually did)
3. Blockers we hit (What was hard)
4. Solutions (How we got unstuck)
5. Quality gates (Playtest feedback, metrics)
6. Next milestone plan (What's coming)
7. Resource needs (Do we need anything?)
8. Call to action (Approval? Feedback? Sign-off?)

## Best Practices

### Content

1. **One idea per slide** — Don't cram multiple concepts
2. **Show, don't tell** — Gameplay footage > describing gameplay
3. **Lead with emotion** — Make people feel the game, not just understand it
4. **Provide proof** — Playtest data, competitive analysis, market research
5. **Anticipate questions** — Have backup slides for tough follow-ups

### Design

1. **Minimal text** — 5-10 words per slide maximum
2. **Strong visuals** — Every slide has a clear focal point
3. **Consistent branding** — Same colors, fonts, logo position throughout
4. **Readable fonts** — Sans-serif, 24pt minimum for body text
5. **Strategic color** — Use color for emphasis, not decoration

### Delivery

1. **Practice out loud** — Know your timing and flow
2. **Speak to the slide, not from it** — You know the content
3. **Make eye contact** — Connect with your audience
4. **Pause for emphasis** — Let important points land
5. **Invite questions** — Show confidence and openness

### Customization

1. **Know your audience** — Investors care about ROI; players care about fun
2. **Adjust emphasis** — Lead with gameplay for fans, market for publishers
3. **Timing matters** — Tailor deck length to available time
4. **Have backup slides** — Technical, financial, competitive details ready
5. **Feedback loop** — Ask what resonated; revise for next pitch

## Integration with Other Skills

### GDD-Manager

**From gdd-manager:**
- Game concept and pillars
- Gameplay description
- Story summary
- Market analysis

**To gdd-manager:**
- Deck feedback from publishers/investors
- Decision gates (greenlight? funding approved?)
- Timeline commitments

### Narrative Designer

**From narrative-designer:**
- Story hook (1-2 sentence elevator pitch)
- Character synopsis
- Narrative themes
- Dialogue samples

**To narrative-designer:**
- Story emphasis in different pitch types
- Narrative timing and pacing needs

### Level Designer

**From level-designer:**
- Progression curve visualization
- Key encounter descriptions
- Level layout diagrams

**To level-designer:**
- Visual material needed for slides
- Gameplay pacing requirements

## Output Format

Pitch decks are delivered as `.pptx` (Microsoft PowerPoint) files. Standard naming:

- **Format:** `[GameName]_Pitch_Deck_[Type]_[Version].pptx`
- **Examples:**
  - `Infinite_Voyage_Pitch_Deck_Publisher_v1.pptx`
  - `Infinite_Voyage_Pitch_Deck_Investor_v2.pptx`
  - `Infinite_Voyage_Pitch_Deck_Milestone_v1.pptx`

Deck includes:
- Title slide with branding
- Content slides with minimal text and strong visuals
- Speaker notes for each slide
- Backup slides for deep dives
- Contact/thank you slide
- Consistent styling throughout

## References

- `templates/publisher-pitch-template.pptx` — Pre-built publisher pitch structure
- `templates/investor-pitch-template.pptx` — Pre-built investor pitch structure
- `templates/team-presentation-template.pptx` — Pre-built team presentation
- `references/pitch-presentation-guide.md` — Best practices and tips
- `references/storytelling-for-games.md` — How to tell compelling game narratives
- `references/market-analysis-examples.md` — How to present market data credibly
- `references/competitor-analysis-template.md` — Framework for competitive positioning
