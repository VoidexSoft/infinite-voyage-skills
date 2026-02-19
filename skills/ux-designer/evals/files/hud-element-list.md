# HUD Element List — Infinite Voyage

## Reference Resolution: 1920x1080 (1080p baseline)

All sizes and positions are specified at 1080p. Scaling rules must be defined for 4K (3840x2160), ultrawide (3440x1440), and mobile (portrait and landscape).

---

## Always-Visible Elements

### 1. Health Bar
- **Position:** Bottom-left, 32px from edge
- **Size:** 280px wide x 24px tall
- **Content:** Segmented bar (4 segments = 4 health pips), numeric overlay "75/100"
- **Color:** Green > Yellow > Red gradient as health drops
- **Icon:** Heart icon, 24x24px, left of bar

### 2. Shield Bar
- **Position:** Directly above Health Bar, 4px gap
- **Size:** 280px wide x 16px tall
- **Content:** Smooth fill bar, numeric overlay "50/50"
- **Color:** Cyan/blue
- **Icon:** Shield icon, 16x16px, left of bar

### 3. Stamina Bar
- **Position:** Below Health Bar, 4px gap
- **Size:** 200px wide x 10px tall
- **Content:** Smooth fill, no numeric display
- **Color:** Yellow/gold
- **Icon:** Lightning bolt, 12x12px, left of bar

### 4. Minimap
- **Position:** Top-right corner, 24px from edges
- **Size:** 200x200px (circular)
- **Content:** Top-down radar, player arrow center, objective pings, enemy dots
- **Border:** 2px ring, semi-transparent dark background
- **Interaction:** Click to expand to full map

### 5. Objective Tracker
- **Position:** Right side, below minimap, 24px from right edge
- **Size:** 300px wide x variable height (max 180px)
- **Content:** Current quest name (16px bold), 1-3 sub-objectives (14px), progress indicators
- **Background:** Semi-transparent dark panel, rounded corners 8px

### 6. Crosshair / Interaction Reticle
- **Position:** Screen center
- **Size:** 32x32px default, expands to 48x48px during combat spread
- **Content:** Dynamic crosshair that changes shape based on weapon type
- **Color:** White with 1px dark outline for contrast on bright backgrounds

---

## Context-Visible Elements (Appear When Relevant)

### 7. Ability Bar
- **Position:** Bottom-center, 48px from bottom edge
- **Size:** 4 slots, each 64x64px with 8px gaps = 280px total width
- **Content:** Ability icons with cooldown overlay (radial wipe), keybind labels
- **States:** Ready (full color), Cooling down (dark overlay + timer), Unavailable (desaturated)
- **Trigger:** Visible in combat, fades 3 sec after exiting combat

### 8. Ammo Counter
- **Position:** Bottom-right, 32px from edges
- **Size:** 120px wide x 48px tall
- **Content:** "24 / 120" (magazine / reserve), weapon icon 32x32px
- **Font:** 28px bold (magazine), 18px regular (reserve)
- **Trigger:** Visible when ranged weapon is equipped

### 9. Enemy Health Bar
- **Position:** Floating above targeted enemy, world-space
- **Size:** 160px wide x 12px tall (scales with distance)
- **Content:** Health fill, enemy name (12px), level indicator
- **Color:** Red fill, white text
- **Trigger:** Visible when enemy is targeted or recently damaged

### 10. Damage Numbers
- **Position:** Floating from damage point, world-space
- **Size:** 20-36px font depending on damage magnitude
- **Content:** Numeric damage value, color-coded by type
- **Colors:** White = normal, Yellow = critical, Blue = shield, Red = self-damage
- **Animation:** Float upward 60px over 0.8 sec, fade out
- **Trigger:** On any damage event (can be disabled in settings)

### 11. Interaction Prompt
- **Position:** Bottom-center, 120px from bottom
- **Size:** Variable width x 40px tall
- **Content:** "[E] Open Container" or "[A] Talk to NPC" — keybind + action label
- **Background:** Semi-transparent dark pill shape
- **Trigger:** Within 3m of interactable object, facing it

### 12. Status Effects Tray
- **Position:** Below shield bar, left side
- **Size:** Row of 28x28px icons, max 6 visible
- **Content:** Active buffs/debuffs with duration timers
- **Overflow:** "..." indicator if more than 6 active, click to expand
- **Trigger:** When any status effect is active

---

## Hidden Elements (Shown on Demand)

### 13. Full Map Overlay
- **Position:** Center screen overlay, 80% screen coverage
- **Size:** 1536x864px at 1080p
- **Trigger:** M key or click minimap

### 14. Quick Inventory Wheel
- **Position:** Center screen radial menu
- **Size:** 400x400px radius
- **Content:** 8 slots for consumables and quick-use items
- **Trigger:** Hold Tab key

### 15. Chat Log
- **Position:** Bottom-left, above health bars
- **Size:** 400px wide x 200px tall
- **Content:** Recent messages, auto-fade after 5 sec
- **Trigger:** Press Enter to open, messages appear briefly when received

### 16. FPS / Latency Counter
- **Position:** Top-left corner, 8px from edges
- **Size:** 80px wide x 20px tall
- **Content:** "60 FPS | 32ms"
- **Trigger:** Enabled in settings, debug/performance mode
