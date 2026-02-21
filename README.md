# Game Design Studio — Game Development Skills

A modular skill set for AI-assisted game development. These skills work with Claude (via Claude Code / Cowork) to provide specialized game design capabilities.

## Skills Overview

### Core Designer Skills
| Skill | Purpose |
|-------|---------|
| `gdd-manager` | Central hub — routes design work, maintains GDD consistency |
| `systems-designer` | Game mechanics, rules, abilities, systemic interactions |
| `narrative-designer` | Story, lore, quests, dialogue trees, character profiles |
| `economy-designer` | Currencies, loot tables, pricing, sink/faucet analysis |
| `level-designer` | Encounters, zones, difficulty curves, progression pacing |
| `ux-designer` | UI flows, wireframes, input mapping, accessibility |

### Analytical Skills
| Skill | Purpose |
|-------|---------|
| `game-balancer` | Numerical balance, Monte Carlo simulations, stat curves, fairness analysis |
| `playtest-simulator` | Virtual playtesting with player archetypes |
| `data-modeler` | Game data spreadsheets (extends xlsx skill) |

### Production Skills
| Skill | Purpose |
|-------|---------|
| `github-gamedev` | GitHub issues, project boards, sprint planning |
| `gdd-writer` | Formatted GDD export (extends docx skill) |
| `pitch-deck` | Game pitch presentations (extends pptx skill) |
| `asset-spec` | Art & audio asset requirement sheets |

## Installation

Copy the `skills/` directory to your Claude skills location:

```bash
# For Cowork / Claude Desktop
cp -r skills/* ~/.claude/skills/

# Or symlink for development
ln -s $(pwd)/skills/* ~/.claude/skills/
```

## Project Structure

Each skill follows a consistent directory layout:

```
skills/<skill-name>/
├── SKILL.md              # Skill definition and prompt
├── evals/files/          # Evaluation test files
├── references/           # Domain knowledge documents
├── scripts/              # Python automation tools
└── templates/            # Output templates and schemas
```

### Full Tree

```
skills/
├── asset-spec/                       # Art & audio asset requirements
│   ├── SKILL.md
│   ├── evals/files/
│   ├── references/
│   │   ├── animation-naming-conventions.md
│   │   ├── art-style-guide.md
│   │   ├── audio-technical-guide.md
│   │   ├── polygon-budgets.md
│   │   └── texture-memory-guide.md
│   ├── scripts/
│   └── templates/
│       ├── asset-spec-animation.md
│       ├── asset-spec-audio.md
│       ├── asset-spec-character.md
│       └── asset-spec-environment.md
│
├── data-modeler/                     # Game data spreadsheets
│   ├── SKILL.md
│   ├── evals/files/
│   ├── references/
│   │   ├── balance-benchmarks.md
│   │   ├── data-integrity-checklist.md
│   │   ├── openpyxl-guide.md
│   │   └── stat-formulas.md
│   ├── scripts/
│   └── templates/
│       ├── export-schema.json
│       └── generate_templates.py
│
├── economy-designer/                 # Currencies, loot, sink/faucet
│   ├── SKILL.md
│   ├── evals/files/
│   ├── references/
│   │   ├── currency-templates.md
│   │   ├── economy-anti-patterns.md
│   │   ├── loot-table-library.md
│   │   └── monetization-case-studies.md
│   ├── scripts/
│   │   └── inflation_tracker.py
│   └── templates/
│
├── game-balancer/                    # Numerical balance & simulations
│   ├── SKILL.md
│   ├── evals/files/
│   ├── references/
│   ├── scripts/
│   │   ├── combat_sim.py
│   │   ├── economy_sim.py
│   │   ├── fairness.py
│   │   ├── loot_sim.py
│   │   ├── optimizer.py
│   │   ├── stat_curves.py
│   │   └── visualize.py
│   └── templates/
│
├── gdd-manager/                      # Central hub & GDD consistency
│   ├── SKILL.md
│   ├── evals/files/
│   ├── references/
│   ├── scripts/
│   │   ├── consistency_check.py
│   │   ├── parse_gdd.py
│   │   └── section_status.py
│   └── templates/
│
├── gdd-writer/                       # Formatted GDD export
│   ├── SKILL.md
│   ├── evals/files/
│   ├── references/
│   │   ├── gdd-writing-style.md
│   │   ├── python-docx-guide.md
│   │   └── stakeholder-document-checklist.md
│   ├── scripts/
│   └── templates/
│       └── generate_templates.py
│
├── github-gamedev/                   # GitHub project management
│   ├── SKILL.md
│   ├── evals/files/
│   ├── references/
│   ├── scripts/
│   │   ├── board_status.py
│   │   ├── gdd_to_issues.py
│   │   ├── sprint_planning.py
│   │   └── sprint_report.py
│   └── templates/
│
├── level-designer/                   # Encounters, zones, pacing
│   ├── SKILL.md
│   ├── evals/files/
│   ├── references/
│   │   ├── boss-mechanics.md
│   │   ├── difficulty-guide.md
│   │   ├── encounter-checklist.md
│   │   ├── environmental-storytelling.md
│   │   ├── pacing-patterns.md
│   │   ├── player-testing-checklist.md
│   │   └── progression-examples.md
│   ├── scripts/
│   └── templates/
│       └── encounter.json
│
├── narrative-designer/               # Story, lore, quests, dialogue
│   ├── SKILL.md
│   ├── evals/files/
│   ├── references/
│   │   ├── branching-patterns.md
│   │   ├── character-template.md
│   │   ├── dialogue-format.md
│   │   ├── narrative-bible.md
│   │   ├── quest-template.md
│   │   └── world-timeline.md
│   ├── scripts/
│   └── templates/
│
├── pitch-deck/                       # Game pitch presentations
│   ├── SKILL.md
│   ├── evals/files/
│   ├── references/
│   │   ├── competitor-analysis-template.md
│   │   ├── market-analysis-examples.md
│   │   ├── pitch-presentation-guide.md
│   │   └── storytelling-for-games.md
│   ├── scripts/
│   └── templates/
│       └── generate_templates.py
│
├── playtest-simulator/               # Virtual playtesting with archetypes
│   ├── SKILL.md
│   ├── evals/files/
│   ├── references/
│   │   ├── exploit-patterns.md
│   │   ├── player-archetypes.md
│   │   ├── reporting-format.md
│   │   └── simulation-scenarios.md
│   ├── scripts/
│   └── templates/
│
├── systems-designer/                 # Game mechanics & rules
│   ├── SKILL.md
│   ├── evals/files/
│   ├── references/
│   │   ├── anti-patterns.md
│   │   └── mechanic-patterns.md
│   ├── scripts/
│   └── templates/
│
└── ux-designer/                      # UI flows, wireframes, accessibility
    ├── SKILL.md
    ├── evals/files/
    ├── references/
    │   ├── accessibility-checklist.md
    │   ├── accessibility-standards.md
    │   ├── color-palettes.md
    │   ├── feedback-library.md
    │   ├── font-guidelines.md
    │   ├── hud-case-studies.md
    │   ├── input-devices.md
    │   ├── onboarding-patterns.md
    │   └── ui-patterns.md
    ├── scripts/
    └── templates/
        └── input-map.json
```

## Requirements

- Claude Code or Cowork with skill support
- Python 3.8+ (for balancer and utility scripts)
- GitHub CLI (`gh`) for github-gamedev skill
- matplotlib (optional, for chart generation)

## License

Proprietary — ONDI Technology Joint Stock Company
