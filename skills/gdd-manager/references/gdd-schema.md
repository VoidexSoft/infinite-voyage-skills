# GDD Section Taxonomy

The standard structure for the Infinite Voyage Game Design Document. Every GDD
section maps to one or more specialist skills. Use this schema when parsing,
indexing, and validating the GDD.

---

## Section Map

| # | Section | Description | Primary Skill | Supporting Skills |
|---|---------|-------------|---------------|-------------------|
| 1 | Vision & Pillars | What makes this game special | gdd-manager | — |
| 2 | Core Gameplay Loop | The minute-to-minute experience | systems-designer | game-balancer |
| 3 | Mechanics & Systems | All game systems in detail | systems-designer | game-balancer, economy-designer |
| 4 | Narrative & Worldbuilding | Story, lore, characters | narrative-designer | level-designer |
| 5 | Economy & Progression | Currencies, rewards, player growth | economy-designer | game-balancer, data-modeler |
| 6 | Level/Content Design | Zones, encounters, missions | level-designer | narrative-designer, game-balancer |
| 7 | UI/UX Design | Interfaces, flows, accessibility | ux-designer | — |
| 8 | Art Direction | Visual style, references | asset-spec | — |
| 9 | Audio Design | Music, SFX, voice | asset-spec | narrative-designer |
| 10 | Technical Requirements | Engine, platform, performance | github-gamedev | — |
| 11 | Monetization | Business model, pricing | economy-designer | ux-designer |
| 12 | Analytics & KPIs | Success metrics, telemetry | game-balancer | data-modeler |

---

## Detailed Section Specifications

### 1. Vision & Pillars

**Purpose**: Define the game's identity and non-negotiable design principles.

**Required contents**:
- Elevator pitch (1-2 sentences)
- Design pillars (3-5 core principles that guide all decisions)
- Target audience definition
- Platform targets
- Competitive positioning (what makes this different)
- Tone and aesthetic summary

**Validation rules**:
- Every other section should reference at least one pillar
- Pillars should be specific enough to make decisions (not "fun gameplay")
- Maximum 5 pillars (more = unfocused)

**Example pillar format**:
```markdown
## Pillar: Meaningful Exploration
Every location the player visits should contain discoverable content that
rewards curiosity — hidden lore, optional challenges, or narrative context.
No area should exist solely as transit space.
```

---

### 2. Core Gameplay Loop

**Purpose**: Define the minute-to-minute, session-to-session, and long-term
play patterns.

**Required contents**:
- Minute-to-minute loop diagram (what does 5 minutes of play look like?)
- Session loop (what does a 30-60 minute session look like?)
- Long-term loop (what drives play over weeks/months?)
- Core verbs (the 3-5 primary actions players perform)
- Feedback cycles (how does player action lead to satisfying response?)

**Validation rules**:
- Loop must connect to at least 2 other GDD sections (mechanics + economy typically)
- Core verbs should be reflected in UI/UX section's interaction design
- Session loop should fit target session length (see Analytics & KPIs)

---

### 3. Mechanics & Systems

**Purpose**: Detailed specification of every game system.

**Required contents per system**:
- System name and one-line description
- Player-facing description (what the player experiences)
- Technical specification (parameters, formulas, state machines)
- System interactions (how it connects to other mechanics)
- Edge cases and exploit potential
- Parameter tables (for game-balancer to tune)

**Validation rules**:
- Every mechanic must have parameters defined (no "magic numbers" in prose)
- System interactions must form a connected graph (no orphan systems)
- Must include state diagrams for state-based mechanics
- Parameters must have initial values and acceptable ranges

**Subsections**:
- 3.1 Combat
- 3.2 Movement & Navigation
- 3.3 Crafting & Gathering
- 3.4 Social Systems (if applicable)
- 3.5 Meta-Systems (achievements, challenges, seasonal)

---

### 4. Narrative & Worldbuilding

**Purpose**: Story, characters, lore, and all text content.

**Required contents**:
- World overview and history
- Main story arc (beginning, middle, end)
- Character profiles (protagonist, key NPCs, antagonists)
- Quest structure and progression
- Dialogue style guide and tone
- Branching narrative map (if applicable)
- Lore codex structure

**Validation rules**:
- Character motivations must be internally consistent
- Quest rewards must align with economy section
- Narrative pacing must match level design section's content flow
- Lore references must not contradict each other

---

### 5. Economy & Progression

**Purpose**: Define all currencies, rewards, pricing, and player growth systems.

**Required contents**:
- Currency list with sources and sinks
- Loot table specifications
- Pricing models for vendors/shops
- Progression curve (XP, levels, power growth)
- Sink-faucet flow diagram
- Monetization tie-ins (if any)

**Validation rules**:
- Every currency must have at least one sink and one faucet
- Loot tables must sum to valid probabilities
- Progression curve must produce target time-to-cap (see metrics-glossary.md)
- No arbitrage loops in currency exchange (see economy-anti-patterns.md)

---

### 6. Level/Content Design

**Purpose**: Zones, encounters, maps, and content progression.

**Required contents**:
- World map / zone overview
- Per-zone specifications (enemies, hazards, loot, narrative hooks)
- Encounter design templates
- Difficulty curve across all content
- Play-time estimates per zone
- Gating and unlock conditions

**Validation rules**:
- Difficulty curve must be smooth (no sudden spikes without narrative reason)
- Zone loot must align with economy section's drop tables
- Encounter design must use mechanics defined in section 3
- Play-time estimates must sum to target total content hours

---

### 7. UI/UX Design

**Purpose**: All player-facing interfaces, flows, and accessibility.

**Required contents**:
- Screen inventory (list of all screens/menus)
- User flow diagrams for key actions
- Wireframes or mockups for critical screens
- Input mapping (controller, keyboard, touch)
- Accessibility features and compliance targets
- Onboarding/tutorial flow

**Validation rules**:
- Every mechanic in section 3 must have a corresponding UI element
- Input mapping must not conflict (no duplicate bindings)
- Accessibility must meet minimum standards (see accessibility-checklist.md)
- Tutorial must cover all core verbs from section 2

---

### 8. Art Direction

**Purpose**: Visual identity, style guides, and asset requirements.

**Required contents**:
- Art style definition with reference images
- Color palette
- Character art guidelines
- Environment art guidelines
- UI art style guide
- Technical art constraints (polygon budgets, texture sizes)

**Validation rules**:
- Art style must support the tone defined in section 1
- Technical constraints must align with section 10 (Technical Requirements)
- Asset lists must cover all entities defined in sections 3-6

---

### 9. Audio Design

**Purpose**: Music, sound effects, voice acting, and ambient audio.

**Required contents**:
- Audio style guide (tone, genre, influences)
- Music requirements per zone/scene
- SFX list for mechanics and UI
- Voice acting requirements (if any)
- Adaptive audio design (how music responds to gameplay)

**Validation rules**:
- SFX list must cover all mechanics in section 3
- Music zones must align with level design in section 6
- Voice requirements must align with dialogue in section 4

---

### 10. Technical Requirements

**Purpose**: Engine, platform, performance, and infrastructure.

**Required contents**:
- Target platforms and minimum specs
- Engine and framework choices
- Performance targets (FPS, load times, memory)
- Networking requirements (if multiplayer)
- Save system design
- Build and deployment pipeline

**Validation rules**:
- Performance targets must support art assets in section 8
- Save system must persist all progression from section 5
- Networking must support all multiplayer mechanics in section 3

---

### 11. Monetization

**Purpose**: Business model and premium content strategy.

**Required contents**:
- Business model (premium, F2P, subscription, hybrid)
- Premium currency design (if any)
- Store/shop design
- Battle pass / seasonal content (if any)
- Pricing strategy
- Ethical guidelines (no pay-to-win commitment)

**Validation rules**:
- Premium currency must not buy gameplay advantages (see economy-anti-patterns.md)
- Pricing must align with economy section's earning rates
- Store UI must be documented in section 7

---

### 12. Analytics & KPIs

**Purpose**: Define success metrics and what to measure.

**Required contents**:
- Core KPIs (retention, session length, conversion, revenue)
- Engagement metrics per feature
- Balance health metrics (see metrics-glossary.md)
- A/B testing plan for key decisions
- Telemetry event list
- Dashboard requirements

**Validation rules**:
- Every KPI must have a target value and acceptable range
- Telemetry events must cover all core loop actions from section 2
- Balance metrics must align with game-balancer's monitoring needs

---

## File Naming Convention

GDD files should follow this pattern:

```
gdd/
├── 01-vision-pillars.md
├── 02-core-loop.md
├── 03-mechanics/
│   ├── 03-01-combat.md
│   ├── 03-02-movement.md
│   └── 03-03-crafting.md
├── 04-narrative/
│   ├── 04-01-world-overview.md
│   ├── 04-02-main-story.md
│   └── 04-03-characters.md
├── 05-economy-progression.md
├── 06-level-design/
│   ├── 06-01-world-map.md
│   └── 06-02-zone-specs/
├── 07-ui-ux.md
├── 08-art-direction.md
├── 09-audio-design.md
├── 10-technical.md
├── 11-monetization.md
└── 12-analytics-kpis.md
```

Sections with many subsections (3, 4, 6) use subdirectories. Simple sections
are single files.

---

## Cross-Reference Index

Use this to quickly find which sections reference each other:

```
Section 1 (Vision) ←→ All sections (pillars inform everything)
Section 2 (Loop) → 3 (Mechanics), 5 (Economy), 7 (UX), 12 (KPIs)
Section 3 (Mechanics) → 4 (Narrative hooks), 5 (Rewards), 6 (Content), 7 (UI)
Section 4 (Narrative) → 6 (Level placement), 9 (Voice/audio)
Section 5 (Economy) → 3 (Costs/rewards), 6 (Loot), 11 (Monetization)
Section 6 (Level Design) → 3 (Mechanics used), 4 (Story beats), 5 (Loot tables)
Section 7 (UX) → 3 (Mechanic UI), 8 (Art style), 11 (Store UI)
Section 8 (Art) → 10 (Technical constraints)
Section 9 (Audio) → 3 (SFX), 4 (Voice), 6 (Zone music)
Section 10 (Technical) → 8 (Asset budgets), 12 (Telemetry infra)
Section 11 (Monetization) → 5 (Economy), 7 (Store UI)
Section 12 (KPIs) → 2 (Loop metrics), 5 (Economy health), 11 (Revenue)
```
