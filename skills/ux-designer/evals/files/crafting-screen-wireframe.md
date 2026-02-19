# Crafting Screen Wireframe — Infinite Voyage

## Overview

The crafting screen allows players to combine salvaged materials from derelict ships and alien worlds into usable equipment, consumables, and ship upgrades. Accessible from the player's ship workbench or any planetary crafting station.

## Wireframe Layout

```
┌──────────────────────────────────────────────────────────────┐
│  HEADER: "Stellar Forge — Crafting Station"    [?] [X]      │
│  Location: Orion's Reach Outpost | Tier: Advanced           │
├──────────────┬───────────────────────────┬───────────────────┤
│ CATEGORY     │  RECIPE LIST              │ CRAFTING DETAIL   │
│ SIDEBAR      │                           │                   │
│              │  ┌───────────────────┐    │ Item: [Name]      │
│ [Weapons]    │  │ Plasma Rifle      │    │ Icon: [Preview]   │
│ [Armor]      │  │ ★★★ | 2 Titanium  │    │                   │
│ [Consumables]│  │ Status: Craftable  │    │ Stats:            │
│ [Ship Parts] │  ├───────────────────┤    │ - Damage: +45     │
│ [Mods]       │  │ Cryo Grenade      │    │ - Range: 12m      │
│              │  │ ★★ | 1 Cryogen    │    │ - Fire Rate: 0.8s │
│ ─────────── │  │ Status: Craftable  │    │                   │
│ FILTERS:     │  ├───────────────────┤    │ Materials:        │
│ [Craftable]  │  │ Void Shield Mk3   │    │ ☑ Titanium x2     │
│ [Missing 1]  │  │ ★★★★ | 3 Void     │    │ ☑ Plasma Core x1  │
│ [All]        │  │ Status: Missing 1  │    │ ☒ Quantum Gel x1  │
│              │  └───────────────────┘    │   (have 0/1)      │
│ SORT BY:     │                           │                   │
│ [Name]       │  Page 1 of 3              │ [CRAFT]  [CANCEL] │
│ [Rarity]     │  [<] [1] [2] [3] [>]     │ Craft Time: 8 sec │
│ [Craftable]  │                           │                   │
├──────────────┴───────────────────────────┴───────────────────┤
│ FOOTER: Inventory: 47/60 slots | Credits: 12,400 | [HELP]   │
└──────────────────────────────────────────────────────────────┘
```

## Zone Details

### Category Sidebar (Left, ~15% width)
- 5 crafting categories as icon+text buttons
- Filter toggles below categories
- Sort dropdown at bottom
- Scrollable if more categories are added

### Recipe List (Center, ~40% width)
- Scrollable vertical list of recipe cards
- Each card shows: item name, rarity stars, primary material cost, craftability status
- Color coding: green border = craftable, yellow = missing 1-2 materials, red = missing 3+
- Pagination at bottom for long lists

### Crafting Detail Panel (Right, ~45% width)
- Shows selected recipe details
- Item preview image/icon at top
- Full stat block below preview
- Material checklist with owned/needed counts
- Craft button (primary action) and Cancel button
- Craft time indicator with progress bar during crafting

### Header
- Screen title with crafting station name and tier
- Help button [?] opens crafting tutorial overlay
- Close button [X] returns to game world

### Footer
- Persistent status bar: inventory capacity, credit balance, help shortcut

## Interaction Notes

- Selecting a category filters the recipe list
- Clicking a recipe card populates the detail panel
- Craft button is disabled (grayed) when materials are insufficient
- During crafting, a progress bar replaces the Craft button for the duration
- Missing materials are shown in red with a "Find" link that opens the galaxy map to locate sources
- Long-press on any material shows a tooltip with acquisition locations
- Controller: LB/RB to switch categories, D-pad to navigate recipes, A to select, X to craft

## Error Scenarios to Consider

1. Player tries to craft with full inventory
2. Player disconnects mid-craft (multiplayer)
3. Crafting station tier too low for recipe
4. Materials consumed but craft interrupted (power failure event)
5. Player tries to craft item they already have max copies of
6. Recipe requires materials from a locked region
