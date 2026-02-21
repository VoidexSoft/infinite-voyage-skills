# Game Design Studio — Skill & Agent Architecture

## Executive Summary

A modular skill set designed for daily game development work. The architecture splits game design into specialized disciplines, adds balancing/analytics capabilities, and integrates with your GitHub workflow. Each skill follows the Claude Code skill framework (SKILL.md + scripts + references) and can be used standalone or composed into multi-agent workflows.

---

## 1. High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    ORCHESTRATION LAYER                          │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────────┐ │
│  │  GDD Manager │  │ GitHub Sync  │  │  Sprint Planner       │ │
│  │  (hub skill) │  │ (issues +    │  │  (board → tasks →     │ │
│  │              │  │  projects)   │  │   daily work)         │ │
│  └──────┬───────┘  └──────┬───────┘  └───────────┬───────────┘ │
│         │                 │                       │             │
├─────────┼─────────────────┼───────────────────────┼─────────────┤
│         │         DESIGNER SKILLS                 │             │
│         │                                         │             │
│  ┌──────┴───────────────────────────────────────┐ │             │
│  │                                               │ │             │
│  │  ┌─────────────┐  ┌─────────────────────────┐│ │             │
│  │  │  Systems    │  │  Narrative Designer      ││ │             │
│  │  │  Designer   │  │  (story, lore, quests,   ││ │             │
│  │  │  (mechanics,│  │   dialogue trees)        ││ │             │
│  │  │   rules,    │  └─────────────────────────┘│ │             │
│  │  │   loops)    │                              │ │             │
│  │  └─────────────┘  ┌─────────────────────────┐│ │             │
│  │                   │  Level/Content Designer  ││ │             │
│  │  ┌─────────────┐  │  (encounters, maps,      ││ │             │
│  │  │  Economy    │  │   progression)           ││ │             │
│  │  │  Designer   │  └─────────────────────────┘│ │             │
│  │  │  (currency, │                              │ │             │
│  │  │   loot,     │  ┌─────────────────────────┐│ │             │
│  │  │   pricing)  │  │  UX/UI Designer         ││ │             │
│  │  └─────────────┘  │  (flows, wireframes,     ││ │             │
│  │                   │   accessibility)         ││ │             │
│  │                   └─────────────────────────┘│ │             │
│  └───────────────────────────────────────────────┘ │             │
│                                                     │             │
├─────────────────────────────────────────────────────┼─────────────┤
│                  ANALYTICAL LAYER                   │             │
│                                                     │             │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────┐│             │
│  │  Game        │  │  Playtest    │  │  Data      ││             │
│  │  Balancer    │  │  Simulator   │  │  Modeler   ││             │
│  │  (numbers,   │  │  (Monte      │  │  (xlsx     ││             │
│  │   curves,    │  │   Carlo,     │  │   tables,  ││             │
│  │   fairness)  │  │   scenarios) │  │   charts)  ││             │
│  └──────────────┘  └──────────────┘  └────────────┘│             │
│                                                     │             │
├─────────────────────────────────────────────────────┼─────────────┤
│                  PRODUCTION LAYER                   │             │
│                                                     │             │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────┐│             │
│  │  GDD Writer  │  │  Pitch Deck  │  │  Asset     ││             │
│  │  (docx/md    │  │  Creator     │  │  Spec      ││             │
│  │   export)    │  │  (pptx)      │  │  Generator ││             │
│  └──────────────┘  └──────────────┘  └────────────┘│             │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
```

---

## 2. Skill Inventory

### Tier 1 — Core Designer Skills (build first)

| # | Skill Name | Role | Key Capabilities |
|---|-----------|------|------------------|
| 1 | `gdd-manager` | Hub / Orchestrator | Read & navigate GDD sections, route tasks to specialist skills, maintain consistency across documents |
| 2 | `systems-designer` | Core Mechanics | Design game loops, define rules, create mechanic specs, analyze systemic interactions |
| 3 | `narrative-designer` | Story & World | Write lore, quest lines, dialogue trees, character arcs, branching narratives |
| 4 | `economy-designer` | In-Game Economy | Currency systems, loot tables, pricing models, sink/faucet analysis, monetization |
| 5 | `level-designer` | Content & Progression | Encounter design, difficulty curves, map/zone specs, progression pacing |
| 6 | `ux-designer` | Player Experience | UI flow diagrams, wireframes (SVG/HTML), accessibility review, onboarding flows |

### Tier 2 — Analytical Skills (build second)

| # | Skill Name | Role | Key Capabilities |
|---|-----------|------|------------------|
| 7 | `game-balancer` | Numerical Balance | Stat curves, DPS calculations, Monte Carlo simulations, fairness checks, parameter tuning |
| 8 | `playtest-simulator` | Virtual Playtesting | Simulate player archetypes through game scenarios, identify exploits, measure pacing |
| 9 | `data-modeler` | Spreadsheet Analysis | Leverages existing `xlsx` skill — builds game-specific templates (loot tables, stat sheets, economy models) |

### Tier 3 — Production & Workflow Skills (build third)

| # | Skill Name | Role | Key Capabilities |
|---|-----------|------|------------------|
| 10 | `github-gamedev` | Project Management | Sync GDD sections to GitHub issues, update project boards, generate sprint tasks from design decisions |
| 11 | `gdd-writer` | Document Export | Leverages `docx` skill — formatted GDD export with TOC, diagrams, version history |
| 12 | `pitch-deck` | Presentation | Leverages `pptx` skill — game pitch decks, publisher presentations, milestone reviews |
| 13 | `asset-spec` | Art & Audio Specs | Generate asset requirement sheets, style guides, reference boards for artists/audio |

---

## 3. Detailed Skill Specifications

### 3.1 `gdd-manager` — The Hub Skill

**Purpose:** Central coordinator that understands the full GDD structure and routes work to specialist skills.

**Trigger conditions:**
- User mentions GDD, game design document, or project overview
- User asks a cross-cutting design question
- User wants to review or update the overall game design
- User says "what should I work on next"

**Core workflow:**
```
1. Load GDD index (table of contents / section map)
2. Identify which specialist domain the request belongs to
3. Provide context from related GDD sections
4. Suggest which skill(s) to invoke
5. After specialist work, validate consistency with rest of GDD
```

**Key files:**
```
gdd-manager/
├── SKILL.md              # Routing logic, GDD structure awareness
├── references/
│   ├── gdd-schema.md     # Standard GDD section taxonomy
│   ├── consistency.md    # Cross-reference rules between sections
│   └── templates/
│       ├── section-template.md
│       └── review-checklist.md
└── scripts/
    ├── parse_gdd.py      # Parse GDD directory into structured index
    └── diff_sections.py  # Detect inconsistencies between sections
```

**GDD Section Taxonomy (gdd-schema.md):**
```
1. Vision & Pillars
2. Core Gameplay Loop
3. Mechanics & Systems
4. Narrative & Worldbuilding
5. Economy & Progression
6. Level/Content Design
7. UI/UX Design
8. Art Direction
9. Audio Design
10. Technical Requirements
11. Monetization
12. Analytics & KPIs
```

---

### 3.2 `systems-designer` — Core Mechanics Specialist

**Purpose:** Design, document, and analyze game mechanics and systemic interactions.

**Trigger conditions:**
- User discusses mechanics, rules, abilities, combat, crafting, or any game system
- User wants to add/modify a gameplay feature
- User asks "how should X mechanic work"

**Core workflow:**
```
1. Read relevant GDD mechanics sections
2. Analyze the design request against existing systems
3. Propose mechanic design with:
   - Player-facing description (what the player experiences)
   - Technical specification (parameters, formulas, states)
   - System interactions (how it connects to other mechanics)
   - Edge cases and exploit potential
4. Output as structured markdown with diagrams (mermaid)
5. Flag items needing balancer review
```

**Key outputs:**
- Mechanic specification documents (markdown)
- State diagrams (mermaid)
- Interaction matrices (which systems affect which)
- Parameter tables (for balancer to tune)

**References:**
```
references/
├── mechanic-patterns.md     # Common mechanic archetypes (RPG, roguelike, etc.)
├── interaction-matrix.md    # Template for system interaction analysis
├── state-machine-guide.md   # How to spec state-based mechanics
└── anti-patterns.md         # Common design pitfalls to avoid
```

---

### 3.3 `narrative-designer` — Story & World Specialist

**Purpose:** Create and maintain narrative content — lore, quests, dialogue, characters.

**Trigger conditions:**
- User discusses story, lore, characters, quests, dialogue, or worldbuilding
- User wants to write quest content or NPC dialogue
- User asks about narrative structure or branching

**Core workflow:**
```
1. Load narrative bible / lore documents
2. Understand the narrative context and tone
3. Generate content following established voice/style
4. Structure output in game-ready format:
   - Dialogue trees (JSON/YAML with branching)
   - Quest specs (objectives, rewards, prerequisites)
   - Lore entries (in-game codex format)
5. Check for continuity with existing narrative
```

**Key outputs:**
- Dialogue trees (JSON format for engine import)
- Quest design documents
- Character profiles and arcs
- Lore codex entries
- Branching narrative flowcharts (mermaid)

**Dialogue tree format:**
```json
{
  "id": "npc_merchant_001",
  "speaker": "Zara",
  "lines": [
    {
      "id": "greeting",
      "text": "Welcome, traveler. The stars spoke of your arrival.",
      "conditions": ["quest_active:starmap"],
      "responses": [
        {"text": "What do you know about the starmap?", "next": "starmap_info"},
        {"text": "Just browsing.", "next": "shop_menu"},
        {"text": "[Leave]", "next": "exit"}
      ]
    }
  ]
}
```

**References:**
```
references/
├── narrative-bible.md       # Tone, themes, vocabulary guidelines
├── dialogue-format.md       # JSON schema for dialogue trees
├── quest-template.md        # Standard quest structure
├── character-template.md    # Character profile format
└── branching-patterns.md    # Common narrative branching patterns
```

---

### 3.4 `economy-designer` — In-Game Economy Specialist

**Purpose:** Design and analyze virtual economies — currencies, loot, pricing, sinks/faucets.

**Trigger conditions:**
- User discusses currency, loot, rewards, pricing, shops, crafting costs
- User asks about economy balance or monetization
- User wants to design a reward structure

**Core workflow:**
```
1. Load economy model documents
2. Analyze current sink/faucet balance
3. Design new economic elements with:
   - Faucet analysis (where currency enters the system)
   - Sink analysis (where currency leaves the system)
   - Velocity estimation (how fast currency flows)
   - Inflation/deflation projections
4. Output parameter tables and formulas
5. Flag items for balancer simulation
```

**Key outputs:**
- Economy flow diagrams (mermaid)
- Loot tables with probability distributions
- Currency sink/faucet spreadsheets (via xlsx skill)
- Pricing models with elasticity curves
- Monetization impact assessments

**References:**
```
references/
├── economy-patterns.md       # F2P, premium, hybrid economy models
├── sink-faucet-guide.md      # Balancing resource flows
├── loot-table-format.md      # Standard loot table schema
├── pricing-formulas.md       # Common pricing curves
└── monetization-ethics.md    # Player-friendly monetization guidelines
```

---

### 3.5 `level-designer` — Content & Progression Specialist

**Purpose:** Design encounters, zones, difficulty curves, and progression pacing.

**Trigger conditions:**
- User discusses levels, zones, encounters, difficulty, progression, or pacing
- User wants to design a new area or encounter
- User asks about difficulty scaling

**Core workflow:**
```
1. Load progression curve and existing content map
2. Analyze where new content fits in the player journey
3. Design content with:
   - Encounter specification (enemies, hazards, objectives)
   - Difficulty parameters (for balancer to tune)
   - Reward structure (ties to economy designer)
   - Narrative hooks (ties to narrative designer)
   - Estimated play time and pacing
4. Output as structured spec with visual aids
```

**Key outputs:**
- Encounter design specs
- Zone layout descriptions with key landmarks
- Difficulty curve charts (SVG/HTML)
- Progression maps showing unlock paths
- Play-time estimates per content segment

**References:**
```
references/
├── difficulty-curves.md      # Linear, logarithmic, S-curve patterns
├── encounter-template.md     # Standard encounter spec format
├── pacing-guide.md           # Tension/release rhythms
├── progression-patterns.md   # Gating, branching, open-world patterns
└── content-density.md        # How much content per hour of play
```

---

### 3.6 `ux-designer` — Player Experience Specialist

**Purpose:** Design UI flows, wireframes, onboarding, and accessibility features.

**Trigger conditions:**
- User discusses UI, UX, menus, HUD, tutorials, onboarding, or accessibility
- User wants to design a screen or flow
- User asks about player experience or usability

**Core workflow:**
```
1. Understand the player interaction being designed
2. Map the user flow (entry → action → feedback → exit)
3. Create wireframe (SVG or HTML prototype)
4. Specify interaction details:
   - Input mapping (controller, keyboard, touch)
   - Feedback (visual, audio, haptic)
   - Error states and edge cases
   - Accessibility considerations
5. Output flow diagrams and wireframe files
```

**Key outputs:**
- User flow diagrams (mermaid or SVG)
- Interactive wireframes (HTML/React prototypes)
- Input mapping tables
- Accessibility audit checklists
- Onboarding sequence specs

**References:**
```
references/
├── ui-patterns.md            # Common game UI patterns (inventory, map, dialog)
├── wireframe-guide.md        # How to create effective wireframes
├── accessibility-checklist.md # Game accessibility guidelines
├── input-mapping.md          # Controller/keyboard/touch conventions
└── onboarding-patterns.md    # Tutorial and first-time experience patterns
```

---

### 3.7 `game-balancer` — The Analytical Powerhouse

**Purpose:** Numerically balance game systems through simulation, math, and iterative tuning.

**Trigger conditions:**
- User asks to balance stats, abilities, items, enemies, or economy
- User wants to run simulations or check fairness
- User mentions DPS, TTK, win rates, or any balance metric
- Any designer skill flags something for balance review

**Core workflow:**
```
1. Load current parameter tables and formulas
2. Identify what needs balancing and success criteria
3. Build mathematical model:
   - Define variables and constraints
   - Set up simulation (Python)
   - Run Monte Carlo or optimization
4. Analyze results:
   - Distribution plots (matplotlib → PNG)
   - Statistical summary
   - Outlier and exploit detection
5. Recommend parameter adjustments
6. Export updated tables (via xlsx skill)
```

**Key capabilities:**
- **Stat curve generation:** Level-based scaling (linear, exponential, S-curve, diminishing returns)
- **Combat simulation:** DPS/TTK/EHP calculations, 1v1 and group combat Monte Carlo
- **Economy simulation:** Currency flow over time, inflation tracking
- **Loot simulation:** Drop rate verification, expected value per hour
- **Fairness analysis:** Gini coefficient for power distribution, win rate variance
- **Parameter optimization:** Gradient descent or evolutionary algorithms for target metrics

**Scripts:**
```
scripts/
├── stat_curves.py        # Generate and visualize scaling curves
├── combat_sim.py         # Monte Carlo combat simulator
├── economy_sim.py        # Economy flow simulation
├── loot_sim.py           # Loot table probability simulator
├── optimizer.py          # Parameter optimization engine
├── fairness.py           # Gini coefficient, variance analysis
└── visualize.py          # Chart generation utilities
```

**References:**
```
references/
├── balancing-methodology.md  # Step-by-step balancing process
├── common-formulas.md        # RPG stat formulas, XP curves, etc.
├── simulation-guide.md       # How to set up Monte Carlo sims
├── metrics-glossary.md       # DPS, TTK, EHP, etc. definitions
└── anti-snowball.md          # Preventing runaway advantage
```

---

### 3.8 `playtest-simulator` — Virtual Playtesting

**Purpose:** Simulate different player archetypes playing through game content to find issues.

**Trigger conditions:**
- User wants to test a design without real players
- User asks "what would happen if a player does X"
- User wants to find exploits or degenerate strategies

**Core workflow:**
```
1. Define player archetypes:
   - Optimizer (min-maxer, finds exploits)
   - Explorer (tries everything, ignores meta)
   - Casual (follows path of least resistance)
   - Completionist (does everything)
2. Load game content and rules
3. Simulate each archetype's decision-making through content
4. Report:
   - Pain points per archetype
   - Exploits discovered
   - Pacing issues
   - Difficulty spikes/valleys
5. Recommend design adjustments
```

**References:**
```
references/
├── player-archetypes.md      # Bartle types + modern extensions
├── exploit-patterns.md       # Common game exploits to check for
├── simulation-scenarios.md   # Template scenarios to run
└── reporting-format.md       # Playtest report structure
```

---

### 3.9 `github-gamedev` — Project Management Integration

**Purpose:** Bridge between game design work and GitHub issues/project boards.

**Trigger conditions:**
- User wants to sync design decisions to GitHub
- User asks to create issues from a design document
- User wants to update the project board
- User asks "what's the project status"

**Core workflow:**
```
1. Parse GDD section or design document
2. Decompose into implementable tasks
3. Create/update GitHub issues with:
   - Clear title and description
   - Labels (design, art, code, audio, etc.)
   - Milestone assignment
   - Links to relevant GDD sections
4. Update project board columns
5. Generate sprint summaries
```

**Key capabilities:**
- GDD section → GitHub issues (batch creation)
- Design decision → issue update with rationale
- Project board status → progress report
- Sprint planning assistance
- Milestone tracking and burndown estimates

**Scripts:**
```
scripts/
├── gdd_to_issues.py      # Parse GDD and create GitHub issues
├── board_status.py       # Fetch and summarize project board
└── sprint_report.py      # Generate sprint progress report
```

---

### 3.10 `data-modeler` — Game Data Spreadsheets

**Purpose:** Extends the existing `xlsx` skill with game-specific spreadsheet templates.

**Trigger conditions:**
- User wants game data in spreadsheet format
- User needs loot tables, stat sheets, or economy models in Excel
- Balancer outputs need to be formatted for team sharing

**Templates provided:**
- Stat progression tables (all entities)
- Loot/drop rate tables
- Economy flow models (sink/faucet tracking)
- Content checklist / completion matrix
- Ability/skill comparison matrices
- Item database sheets

---

## 4. Cross-Skill Interactions

The skills are designed to work together. Here's how they interact:

```
systems-designer ──defines mechanics──→ game-balancer ──tunes numbers──→ data-modeler
       │                                      ↑                              │
       │                                      │                              │
       ├──creates rewards──→ economy-designer ─┘                              │
       │                          │                                           │
       │                          └──pricing──→ level-designer                │
       │                                            │                         │
       │                                            ├──encounters──→ playtest-simulator
       │                                            │                         │
       ├──narrative hooks──→ narrative-designer──────┘                         │
       │                                                                      │
       └──ui requirements──→ ux-designer                                      │
                                                                              │
gdd-manager ──orchestrates all──→ gdd-writer ──exports──→ docx/pdf           │
       │                                                                      │
       └──tasks──→ github-gamedev ←──data──────────────────────────────────────┘
```

**Example workflow: "Add a new enemy type"**
```
1. gdd-manager    → Identifies: needs systems, narrative, level, balance work
2. systems-designer → Defines enemy mechanics, abilities, AI behavior
3. narrative-designer → Creates lore, encounter dialogue, death lines
4. level-designer → Places in zones, sets spawn rules, designs encounters
5. game-balancer  → Tunes HP/damage/speed, runs combat simulation
6. playtest-simulator → Tests all archetypes vs new enemy
7. economy-designer → Sets loot drops, XP rewards
8. data-modeler   → Updates master stat spreadsheet
9. github-gamedev → Creates implementation issues for each discipline
10. gdd-writer    → Updates GDD bestiary section
```

---

## 5. Implementation Plan

### Phase 1: Foundation (Week 1-2)

**Build first — used daily:**

| Priority | Skill | Effort | Dependencies |
|----------|-------|--------|-------------|
| P0 | `gdd-manager` | 2 days | None — hub skill, build first |
| P0 | `systems-designer` | 2 days | gdd-manager |
| P0 | `game-balancer` | 3 days | systems-designer (heaviest scripts) |
| P1 | `github-gamedev` | 2 days | gh CLI available |

**Deliverables:**
- 4 functional skills with SKILL.md, scripts, references
- Eval cases for each skill
- GDD parsed and indexed

### Phase 2: Design Specialists (Week 3-4)

| Priority | Skill | Effort | Dependencies |
|----------|-------|--------|-------------|
| P1 | `narrative-designer` | 2 days | gdd-manager |
| P1 | `economy-designer` | 2 days | systems-designer, game-balancer |
| P1 | `level-designer` | 2 days | systems-designer, narrative-designer |
| P2 | `ux-designer` | 2 days | None |

### Phase 3: Analytics & Production (Week 5-6)

| Priority | Skill | Effort | Dependencies |
|----------|-------|--------|-------------|
| P2 | `playtest-simulator` | 3 days | All designer skills |
| P2 | `data-modeler` | 1 day | xlsx skill, game-balancer |
| P2 | `gdd-writer` | 1 day | docx skill, gdd-manager |
| P3 | `pitch-deck` | 1 day | pptx skill |
| P3 | `asset-spec` | 1 day | gdd-manager |

### Phase 4: Iteration & Eval (Ongoing)

- Run skill-creator's **Improve** mode on each skill
- Build comprehensive eval suites
- Cross-skill integration testing
- Tune based on daily usage patterns

---

## 6. Technical Architecture Decisions

### Skill vs Agent vs Subagent

| Component | Implementation | Reason |
|-----------|---------------|--------|
| Designer skills (6) | **Skill** (SKILL.md) | Loaded into context on trigger, domain knowledge + workflow |
| game-balancer | **Skill + scripts** | Heavy computation in Python scripts, orchestration in SKILL.md |
| playtest-simulator | **Subagent** (via Task tool) | Long-running simulation, benefits from isolated context |
| github-gamedev | **Skill + gh CLI** | Direct GitHub integration via bash |
| gdd-manager | **Skill** | Routing logic, lightweight |
| data-modeler | **Skill** (extends xlsx) | Adds templates on top of existing xlsx skill |

### File Format Standards

| Data Type | Format | Reason |
|-----------|--------|--------|
| Game parameters | JSON | Engine-importable, version-controllable |
| Dialogue trees | JSON | Structured, engine-ready |
| Lore/narrative | Markdown | Human-readable, diffable |
| Stat tables | XLSX | Shareable with non-technical team |
| Diagrams | Mermaid | Renderable in GitHub, lightweight |
| Wireframes | HTML/SVG | Interactive, no special tools needed |
| Reports | DOCX | Professional, distributable |

### Directory Structure per Skill

```
skill-name/
├── SKILL.md                    # Main instructions (< 500 lines)
├── LICENSE.txt                 # License
├── scripts/                    # Python utilities
│   ├── __init__.py
│   └── [domain-specific].py
├── references/                 # Deep-dive documentation
│   ├── [topic].md
│   └── ...
├── templates/                  # Output templates
│   ├── [template].md
│   └── [template].json
└── evals/                      # Test cases
    ├── evals.json
    └── files/                  # Sample input files
```

---

## 7. Leveraging Existing Skills

The architecture is designed to **compose with** existing Anthropic skills:

| Existing Skill | Used By | How |
|---------------|---------|-----|
| `xlsx` | data-modeler, game-balancer, economy-designer | Game data spreadsheets, simulation output tables |
| `docx` | gdd-writer | Formatted GDD export with TOC, styles |
| `pptx` | pitch-deck | Publisher presentations, milestone reviews |
| `pdf` | gdd-writer | PDF export of finalized GDD sections |
| `skill-creator` | All skills (meta) | Evaluate and improve each skill iteratively |

---

## 8. Daily Workflow Example

```
Morning:
  → "What should I work on today?"
  → github-gamedev fetches board status, gdd-manager suggests priorities

Design Session:
  → "Let's design the shield mechanic"
  → systems-designer creates mechanic spec
  → game-balancer runs combat sim with shields
  → ux-designer sketches shield UI indicator

Afternoon:
  → "Balance the new shield values"
  → game-balancer runs Monte Carlo, suggests parameters
  → data-modeler updates the stat spreadsheet
  → playtest-simulator tests optimizer archetype exploiting shields

End of Day:
  → "Create issues for the shield feature"
  → github-gamedev decomposes into 8 implementation issues
  → Updates project board
  → gdd-writer updates the mechanics section
```

---

## 9. Community & Open Source Integration

**Recommended community skills to watch/adopt:**
- **Machinations integration** — Dynamic balance editor, exports JSON/XML
- **Mermaid diagram skill** — Enhanced diagram generation for game flows
- **GitHub Actions skill** — CI/CD for game builds
- **Image generation skill** — Concept art and reference images

**Standards to follow:**
- All skills packaged as `.skill` files for sharing
- Eval suites included for quality assurance
- Compatible with skill-creator's improve/benchmark workflow
