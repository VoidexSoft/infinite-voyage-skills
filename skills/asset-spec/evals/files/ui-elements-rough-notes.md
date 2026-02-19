# UI Elements Needing Art Specs — Infinite Voyage

Quick brain dump from design meeting 2026-02-18. Need formal specs for all of these ASAP.

## HUD Elements

- **Ability icons** — 6 navigator abilities (Warp Jump, Gravity Well, Stellar Shield, Nebula Cloak, Ion Surge, Quantum Lock). Need them in 4 sizes for HUD bar, skill tree, inventory tooltip, and radial menu. Cooldown overlay state too.
- **Health bar** — segmented shield + hull integrity display. Should pulse red when critical (<20%). Needs normal, damaged, recharging, and overcharged states.
- **Minimap frame** — circular minimap with sector overlay. Must show friendly (blue), hostile (red), and POI (gold) pings. Fog of war gradient at edges. Compass heading tick marks around the ring.
- **Fuel gauge** — vertical bar, left side of HUD. Five segment colors from green (full) to red (empty). Animated particle effect when burning fuel during warp.

## Menu Elements

- **Inventory slot frame** — 64x64 grid cells with rarity borders: Common (gray), Rare (blue), Epic (purple), Legendary (gold animated shimmer). Empty slot has subtle inner glow.
- **Star chart node** — hexagonal system node for the galaxy map. States: undiscovered (dark), scanned (dim outline), visited (full color), current (pulsing glow + ring). Lines connecting visited nodes.
- **Dialogue choice button** — pill-shaped, max 3 visible at once. Hover highlight, selected state, locked/grayed-out state for skill-check fails. Needs to accommodate 2 lines of text.

## Notification / Feedback

- **Damage numbers** — floating combat text. Crit (large, gold, bounce), normal (white), heal (green, float up), shield (blue, spark effect). Font is Orbitron Bold.
- **Loot popup** — bottom-right toast with item icon, name, rarity color strip. Auto-dismiss after 4s. Stack up to 3 visible.
- **Objective marker** — diamond shape, world-space + screen-edge clamp. Distance text below. Active (bright), completed (checkmark fade), optional (dashed outline).

## General Notes
- Target resolutions: 1920x1080 (base), 2560x1440, 3840x2160
- UI scale settings: 80%, 100%, 120%
- Must support colorblind mode (use shapes/patterns in addition to color coding)
- Art style: clean sci-fi holographic, slight glow, thin stroke outlines, semi-transparent panels
- Engine: Unreal Engine 5, UMG widgets
- Export as PNG sprite sheets + individual sliced assets
