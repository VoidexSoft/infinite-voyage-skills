# Infinite Voyage — Game Development Skills

A modular skill set for AI-assisted game development on the **Infinite Voyage** project. These skills work with Claude (via Claude Code / Cowork) to provide specialized game design capabilities.

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

```
skills/
├── gdd-manager/          # Hub skill
│   ├── SKILL.md
│   └── scripts/
├── systems-designer/     # Mechanics specialist
│   ├── SKILL.md
│   └── references/
├── narrative-designer/   # Story specialist
│   ├── SKILL.md
│   └── references/
├── economy-designer/     # Economy specialist
│   └── SKILL.md
├── level-designer/       # Content specialist
│   └── SKILL.md
├── ux-designer/          # UX specialist
│   └── SKILL.md
├── game-balancer/        # Balance analyst
│   ├── SKILL.md
│   └── scripts/          # Python simulation tools
├── playtest-simulator/   # Virtual QA
│   └── SKILL.md
├── github-gamedev/       # Project management
│   ├── SKILL.md
│   └── scripts/
├── data-modeler/         # Spreadsheet templates
│   └── SKILL.md
├── gdd-writer/           # Document export
│   └── SKILL.md
├── pitch-deck/           # Presentations
│   └── SKILL.md
└── asset-spec/           # Asset requirements
    └── SKILL.md
```

## Requirements

- Claude Code or Cowork with skill support
- Python 3.8+ (for balancer and utility scripts)
- GitHub CLI (`gh`) for github-gamedev skill
- matplotlib (optional, for chart generation)

## License

Proprietary — ONDI Technology Joint Stock Company
