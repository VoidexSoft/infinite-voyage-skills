# Stakeholder Document Checklist

Different stakeholders read the GDD for different reasons. This reference
defines what each audience needs, how to create document variants, and the
review and sign-off workflow for Infinite Voyage.

---

## 1. Stakeholder Needs Matrix

### Engineers / Programmers

Engineers translate design into code. They need unambiguous technical truth.

**Must include:**
- Exact formulas and algorithms (damage calc, spawn logic, economy loops)
- State machines and flow diagrams for complex systems
- Data schemas (what fields does an Item have? what types?)
- Edge case enumeration (what happens when health goes below zero?)
- Performance constraints (max entities, tick rate, memory budget)
- API/interface contracts between systems (inventory talks to equipment how?)
- Priority and dependency order (what must be built first?)

**Format preferences:**
- Tables over paragraphs
- Pseudocode or actual code snippets for formulas
- Diagrams with labeled states and transitions
- Numbered requirements they can link to in issue trackers

**What they skip:**
- High-level vision statements
- Marketing language
- Narrative prose (unless it drives a system)

---

### Artists / Animators

Artists need visual direction and production constraints.

**Must include:**
- Art style reference images (mood boards, color palettes)
- Character proportion guides and silhouette requirements
- Environment visual language (materials, lighting direction)
- Asset specifications (texture resolution, polygon budgets, file formats)
- Animation timing requirements (attack is 0.5s, idle loops at 4s)
- UI layout wireframes with annotated spacing and font sizes
- Color-coded status indicators and their hex/RGB values

**Format preferences:**
- Image-heavy pages with annotations
- Side-by-side comparisons (reference vs. target)
- Visual style sheets rather than text descriptions
- Callout boxes highlighting hard constraints vs. creative freedom

**What they skip:**
- Balance spreadsheets
- Server architecture
- Economy formulas

---

### Producers / Project Managers

Producers need scope, timeline, and risk information.

**Must include:**
- Feature list with priority tiers (Must Have, Should Have, Nice to Have)
- Estimated complexity per feature (T-shirt sizing: S, M, L, XL)
- Dependencies between features and teams
- Section completion status (Concept, Draft, Review, Final)
- Open questions with owners and deadlines
- Risk flags (which sections have unresolved design that blocks engineering?)
- Milestone mapping (which GDD sections ship at which milestone?)

**Format preferences:**
- Executive summary at the top of every chapter
- Status dashboards (tables with red/yellow/green indicators)
- Gantt-compatible milestone lists
- Clearly marked "blocked" items

**What they skip:**
- Deep mechanical details (they trust the designer and engineer)
- Narrative prose beyond the summary
- Art style nuances

---

### Executives / Publishers / Investors

Decision-makers need the business case and high-level confidence.

**Must include:**
- Executive summary (1-2 pages maximum for the entire game)
- Elevator pitch (2-3 sentences)
- Core pillars (3-5 bullet points)
- Target audience and market positioning
- Comparable titles with performance data
- Team credentials (who is building this and why they will succeed)
- Scope summary (platforms, estimated dev time, team size, budget range)
- Key differentiators (why this game wins against competitors)
- Risk mitigation summary (biggest risks and how you address them)

**Format preferences:**
- Visual, branded, professional layout
- Charts and graphs over raw data
- Minimal jargon (no "tick rate" or "ECS architecture")
- One strong image per page (concept art, screenshot, mock-up)
- Clear call to action (what do you need from them?)

**What they skip:**
- Everything below the executive summary unless they ask for it
- Technical specifications
- Detailed balance tables
- Individual asset specs

---

### QA / Testers

QA needs testable statements and expected behaviors.

**Must include:**
- Expected behavior for every mechanic ("when X happens, Y results")
- Boundary conditions (min/max values, overflow behavior)
- Error states (what shows when the player has no inventory space?)
- Platform-specific behavior differences
- Accessibility requirements (colorblind modes, subtitle sizing)
- Accepted tolerances (damage can vary +/- 5% due to random spread)

**Format preferences:**
- Numbered requirements (QA-001, QA-002) linkable to test cases
- Given/When/Then format for complex behaviors
- Truth tables for multi-condition logic
- Screenshots of expected UI states

---

## 2. Document Variants

### Full GDD (Internal Reference)

- **Audience:** Entire development team
- **Length:** 80-200+ pages
- **Contents:** Everything -- every section, every detail
- **Distribution:** Internal only, version controlled
- **Update frequency:** Continuous throughout development

### Executive Summary Document

- **Audience:** Publishers, investors, executives
- **Length:** 5-10 pages
- **Contents:** Overview, pillars, market, team, scope, ask
- **Distribution:** External-safe, branded, polished
- **Update frequency:** Per milestone or pitch meeting
- **Derived from:** Full GDD front matter + curated highlights

### Technical Design Document (TDD)

- **Audience:** Engineers, technical leads
- **Length:** 30-80 pages
- **Contents:** Systems architecture, data schemas, formulas, performance
- **Distribution:** Engineering team, technical stakeholders
- **Update frequency:** Sprint-aligned or per-feature
- **Derived from:** Full GDD sections 6-8 + engineering addenda

### Art Bible

- **Audience:** Artists, animators, outsource partners
- **Length:** 20-50 pages
- **Contents:** Visual references, asset specs, style guides, color palettes
- **Distribution:** Art team, external art vendors
- **Update frequency:** Per art milestone
- **Derived from:** Full GDD section 4 + dedicated art reference materials

### Narrative Bible

- **Audience:** Writers, narrative designers, voice directors
- **Length:** 20-60 pages
- **Contents:** Story outline, character profiles, dialogue guidelines, lore
- **Distribution:** Narrative team, VO studio
- **Update frequency:** Per narrative milestone
- **Derived from:** Full GDD section 3 + expanded lore documents

### One-Pager

- **Audience:** Anyone who needs the fastest possible overview
- **Length:** 1 page (front only)
- **Contents:** Title, logline, genre, platform, 3 pillars, one key image
- **Distribution:** Broad -- conferences, networking, email introductions
- **Update frequency:** Rarely (major pivots only)

---

## 3. Review Workflow

### Stage 1: Self-Review (Author)

The section author reviews their own work before requesting feedback.

**Checklist:**
- [ ] Follows the writing style guide (active voice, present tense, specific)
- [ ] All values are filled in (no "TBD" without owner and deadline)
- [ ] Cross-references are correct and link to existing sections
- [ ] Status field is set to "Draft"
- [ ] Spell-check and grammar-check passed
- [ ] Tables are formatted and readable
- [ ] Images have captions

### Stage 2: Peer Review (Discipline Lead)

The discipline lead (lead designer, lead engineer, art director) reviews for
correctness within their domain.

**Checklist:**
- [ ] Mechanics are internally consistent (no contradictions with other sections)
- [ ] Numbers are within expected ranges (not obviously broken)
- [ ] Dependencies are realistic and accounted for
- [ ] Open questions are legitimate (not already answered elsewhere)
- [ ] Edge cases are reasonable and complete
- [ ] Section integrates with adjacent systems

**Output:** Review comments returned to author. Status remains "Draft" until
comments are resolved.

### Stage 3: Cross-Discipline Review

Stakeholders from other disciplines verify the section works for their needs.

**Participants:**
- Engineer reviews designer's mechanic: "Can we build this?"
- Artist reviews designer's visual spec: "Can we create this within budget?"
- Producer reviews scope: "Can we ship this on time?"
- QA reviews testability: "Can we verify this?"

**Checklist:**
- [ ] Feasible within technical constraints
- [ ] Feasible within art production budget
- [ ] Feasible within timeline
- [ ] Testable and verifiable
- [ ] No unresolved cross-discipline conflicts

**Output:** Section marked "Review" when cross-discipline comments are resolved.

### Stage 4: Director Approval

The game director or design director gives final approval.

**Checklist:**
- [ ] Aligns with the game's vision and pillars
- [ ] Consistent with approved creative direction
- [ ] Scope is acceptable
- [ ] Quality meets the bar for the current milestone

**Output:** Section marked "Final." Director name and date recorded.

---

## 4. Sign-Off Process

### Sign-Off Table Template

Each major chapter of the GDD includes a sign-off table:

```
| Role             | Name          | Status   | Date       | Signature |
|------------------|---------------|----------|------------|-----------|
| Section Author   | [Name]        | Approved | [Date]     | [Init.]   |
| Design Lead      | [Name]        | Approved | [Date]     | [Init.]   |
| Engineering Lead | [Name]        | Approved | [Date]     | [Init.]   |
| Art Director     | [Name]        | Pending  |            |           |
| Producer         | [Name]        | Approved | [Date]     | [Init.]   |
| Game Director    | [Name]        | Pending  |            |           |
```

### Sign-Off Rules

1. A section cannot move to "Final" status until all required sign-offs
   are collected.
2. The minimum required sign-offs are: Section Author, Design Lead, and
   one cross-discipline lead relevant to the section.
3. Game Director sign-off is required for Chapters 1 (High Concept),
   2 (Gameplay), and 3 (Story & Narrative). Other chapters require Design
   Lead sign-off as the highest authority.
4. If a signed-off section changes after approval, all sign-offs reset.
   The change log must record what changed and why.
5. Emergency changes during crunch follow a fast-track path: author +
   design lead sign-off only, with full review scheduled for the next
   sprint.

---

## 5. Distribution & Confidentiality

### Classification Levels

| Level | Label | Distribution |
|---|---|---|
| Public | PUBLIC | Anyone (press releases, store pages) |
| Partner | PARTNER CONFIDENTIAL | Publishers, platform holders, outsource |
| Internal | INTERNAL ONLY | Full-time team members |
| Restricted | RESTRICTED | Leads and directors only |

### Document Watermarking

External documents include:
- Recipient name in the footer ("Prepared for: [Publisher Name]")
- Date of distribution
- "CONFIDENTIAL" watermark on every page
- Version number (so you know which version leaked if it does)

### Distribution Log

Track who received which version:

```
| Recipient        | Company    | Version | Date       | Classification  |
|------------------|------------|---------|------------|-----------------|
| John Smith       | Publisher  | 1.5     | 2025-03-01 | PARTNER CONF.   |
| Internal Team    | Studio     | 1.5     | 2025-02-28 | INTERNAL ONLY   |
| Board of Dirs.   | Studio     | Exec v1 | 2025-03-05 | RESTRICTED      |
```

---

## 6. Quick Reference: Who Gets What

| Content Area | Engineers | Artists | Producers | Execs | QA |
|---|---|---|---|---|---|
| Executive Summary | Skim | Skim | Read | **Read** | Skim |
| Core Mechanics | **Read** | Skim | Scope | Skip | **Read** |
| Story & Narrative | Reference | Reference | Scope | Summary | Reference |
| Art & Visuals | Specs only | **Read** | Scope | Highlights | Reference |
| Systems Design | **Read** | Skip | Scope | Skip | **Read** |
| Level Design | **Read** | **Read** | Scope | Skip | **Read** |
| Technical Specs | **Read** | Skip | Scope | Skip | Reference |
| Economy Model | **Read** | Skip | Scope | Summary | **Read** |
| Appendices | Reference | Reference | Reference | Skip | **Read** |
| Change Log | Skim | Skim | **Read** | Skip | **Read** |

**Read** = Primary audience, must review in detail
Skim = Should be aware of, not required to review
Reference = Consult as needed
Scope = Review for scope/timeline impact only
Summary = Only needs the executive-level summary
Skip = Not relevant to their role
