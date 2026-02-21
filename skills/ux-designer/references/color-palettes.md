# Game UI Color Palette Guide

Color reference for game UI design. Covers thematic palettes, functional colors,
rarity systems, colorblind-safe alternatives, and contrast requirements. Every color decision
must pair with a non-color indicator (icon, shape, text, or pattern) to remain accessible.

---

## 1. RPG / Fantasy Palettes

### Dark Fantasy (Example Theme)

A muted, atmospheric palette evoking ancient mystery and worn adventure.

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| Background (deep) | Charcoal | `#1A1A2E` | Main menu, overlay backgrounds |
| Background (mid) | Slate | `#16213E` | Panel backgrounds, card surfaces |
| Background (light) | Storm | `#0F3460` | Active panels, selected states |
| Primary accent | Gold | `#E2B714` | Titles, selected items, important highlights |
| Secondary accent | Amber | `#D4A04A` | Secondary headings, breadcrumbs |
| Text (primary) | Ivory | `#F0E6D3` | Body text, labels |
| Text (secondary) | Ash | `#A0937D` | Descriptions, hints, disabled text |
| Interactive | Sapphire | `#3A86FF` | Buttons, links, interactive elements |
| Interactive hover | Sky | `#5FA8FF` | Hover state for interactive elements |
| Danger | Crimson | `#E63946` | Health loss, errors, destructive actions |
| Success | Emerald | `#2EC4B6` | Health gain, success, confirmations |
| Warning | Tangerine | `#FF9F1C` | Caution, low resource, expiring effects |

### High Fantasy (Alternate Bright Theme)

A vibrant palette for players who prefer saturated, heroic aesthetics.

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| Background | Royal blue | `#1B2838` | Main surfaces |
| Primary accent | Bright gold | `#FFD700` | Titles, highlights |
| Secondary accent | Silver | `#C0C0C0` | Borders, dividers |
| Interactive | Vivid blue | `#4169E1` | Buttons, links |
| Danger | Bright red | `#FF4444` | Damage, errors |
| Success | Bright green | `#44FF44` | Healing, completion |

---

## 2. Status Effect Colors

Each status effect uses a distinct color paired with a unique icon shape. The icon is the
primary identifier; color reinforces but never replaces it.

| Status Effect | Color | Hex | Icon Shape | Text Label |
|---------------|-------|-----|------------|------------|
| Poison | Purple-green | `#9B59B6` | Skull and crossbones | "Poisoned" |
| Burn | Orange-red | `#E67E22` | Flame | "Burning" |
| Freeze | Ice blue | `#85C1E9` | Snowflake | "Frozen" |
| Stun | Yellow | `#F1C40F` | Star burst | "Stunned" |
| Bleed | Dark red | `#C0392B` | Blood drop | "Bleeding" |
| Heal over time | Soft green | `#27AE60` | Heart with plus | "Regenerating" |
| Shield / Buff | Cyan | `#1ABC9C` | Shield outline | "Shielded" |
| Slow | Gray-blue | `#7F8C8D` | Snail | "Slowed" |
| Silence | Muted purple | `#8E44AD` | Crossed-out speech | "Silenced" |
| Berserk | Hot red | `#E74C3C` | Fist | "Berserk" |
| Invisible | Translucent white | `#ECF0F1` | Eye with slash | "Invisible" |
| Curse | Dark violet | `#6C3483` | Broken chain | "Cursed" |

### Design Rule

Every status effect entry in the HUD must display:
1. The icon (always visible)
2. The color background or border (reinforcement)
3. A text label on hover or focus (accessibility)
4. Duration timer if applicable (numeric countdown or radial sweep)

---

## 3. Item Rarity Colors

The rarity color system communicates item value at a glance. Each tier uses a distinct color
and a unique border pattern or glow style for colorblind differentiation.

| Rarity | Color | Hex | Border Style | Glow |
|--------|-------|-----|-------------|------|
| Common | Gray | `#95A5A6` | Solid thin (1px) | None |
| Uncommon | Green | `#27AE60` | Solid medium (2px) | None |
| Rare | Blue | `#2980B9` | Solid thick (3px) | Subtle pulse |
| Epic | Purple | `#8E44AD` | Double border | Steady glow |
| Legendary | Orange | `#E67E22` | Animated shimmer | Bright glow |
| Mythic | Red-gold | `#C0392B` | Ornate frame | Flame particle effect |

### Colorblind-Safe Rarity Indicators

In addition to color, each rarity tier uses a supplementary visual cue:

| Rarity | Shape Marker | Text Badge | Sound on Pickup |
|--------|-------------|------------|-----------------|
| Common | No marker | -- | Soft click |
| Uncommon | Single diamond | "U" | Light chime |
| Rare | Double diamond | "R" | Medium chime |
| Epic | Triple diamond | "E" | Rising arpeggio |
| Legendary | Star | "L" | Triumphant fanfare |
| Mythic | Crown | "M" | Dramatic orchestral hit |

### Rarity in Context

- Inventory grid: rarity color as slot border + shape marker in corner
- Loot drops: rarity color as item name text + beam of light color-coded
- Tooltip header: rarity name spelled out ("Rare Iron Sword")
- Shop listings: rarity icon before item name in list view

---

## 4. Colorblind-Safe Alternatives

### Palette Adjustments by Mode

#### Deuteranopia (Red-Green, Green Weak)

| Original | Adjusted | Hex | Notes |
|----------|----------|-----|-------|
| Red `#E63946` | Orange-red `#E86A33` | Shift red toward orange | |
| Green `#27AE60` | Teal `#1ABC9C` | Shift green toward blue-green | |
| Yellow `#F1C40F` | Bright yellow `#FFE066` | Increase brightness | |

#### Protanopia (Red-Green, Red Weak)

| Original | Adjusted | Hex | Notes |
|----------|----------|-----|-------|
| Red `#E63946` | Warm orange `#FF8C42` | Shift red further toward orange | |
| Green `#27AE60` | Blue-green `#17A2B8` | Shift green toward blue | |

#### Tritanopia (Blue-Yellow)

| Original | Adjusted | Hex | Notes |
|----------|----------|-----|-------|
| Blue `#2980B9` | Dark blue `#1A5276` | Darken blue for contrast | |
| Yellow `#F1C40F` | Peach `#FFDAB9` | Shift yellow toward warm neutral | |
| Cyan `#1ABC9C` | Magenta `#C39BD3` | Replace cyan with magenta | |

### Testing Tools

- Simulate color blindness in-engine with post-processing filters
- Use external tools: Color Oracle, Coblis, or Sim Daltonism
- Test all three modes against every UI element that uses color coding
- Verify with actual colorblind testers during playtesting

---

## 5. Dark and Light Themes

### Dark Theme (Default)

| Element | Color | Hex | Contrast vs Background |
|---------|-------|-----|----------------------|
| Background | Near-black | `#121212` | -- |
| Surface | Dark gray | `#1E1E1E` | 1.2:1 (decorative, OK) |
| Primary text | Off-white | `#E0E0E0` | 15.3:1 (exceeds AAA) |
| Secondary text | Medium gray | `#9E9E9E` | 6.1:1 (exceeds AA) |
| Disabled text | Dark gray | `#616161` | 3.3:1 (meets non-text AA) |
| Accent | Gold | `#E2B714` | 8.7:1 (exceeds AAA) |
| Border | Subtle gray | `#333333` | 2.1:1 (decorative, OK) |

### Light Theme

| Element | Color | Hex | Contrast vs Background |
|---------|-------|-----|----------------------|
| Background | Off-white | `#FAFAFA` | -- |
| Surface | Light gray | `#F0F0F0` | 1.1:1 (decorative, OK) |
| Primary text | Near-black | `#212121` | 16.1:1 (exceeds AAA) |
| Secondary text | Medium gray | `#666666` | 5.7:1 (exceeds AA) |
| Disabled text | Light gray | `#BDBDBD` | 1.8:1 (pair with icon) |
| Accent | Deep blue | `#1A237E` | 12.4:1 (exceeds AAA) |
| Border | Medium gray | `#CCCCCC` | 1.6:1 (decorative, OK) |

### Theme Switching

- Player setting in Settings > Display > Theme (Dark / Light / System)
- Transition between themes: 300ms cross-fade to avoid flash
- All screenshots and wireframes should be validated in both themes
- Dark theme is default for immersion; light theme provided for accessibility

---

## 6. Contrast Ratios

### WCAG Contrast Requirements

| Text Type | Minimum Ratio (AA) | Enhanced Ratio (AAA) | Recommended Target |
|-----------|--------------------|--------------------|----------------------|
| Body text (< 18px) | 4.5:1 | 7:1 | 7:1 |
| Large text (>= 18px bold or >= 24px) | 3:1 | 4.5:1 | 4.5:1 |
| UI components and icons | 3:1 | -- | 3:1 |
| Decorative / non-informational | No requirement | -- | -- |

### Measuring Contrast

Contrast ratio formula: `(L1 + 0.05) / (L2 + 0.05)` where L1 is the lighter color's
relative luminance and L2 is the darker color's relative luminance.

### Common Problem Areas in Game UI

| Problem | Example | Fix |
|---------|---------|-----|
| Text on busy backgrounds | Damage numbers over gameplay | Add dark shadow or background pill behind text |
| Transparent overlays | Tooltip with 50% opacity background | Increase opacity to 80%+ or add solid border |
| Colored text on colored background | Red health text on dark red bar | Use white text with colored bar; add outline |
| Small icons on gradient | Minimap icons on terrain | Add contrasting outline or halo around icons |
| HUD over bright environments | White health bar in snowy level | Add dark outline around all HUD elements |

### Contrast Validation Checklist

- [ ] All body text meets 7:1 ratio against its immediate background
- [ ] All large text meets 4.5:1 ratio
- [ ] All interactive elements meet 3:1 ratio against adjacent colors
- [ ] HUD elements remain readable over the brightest and darkest in-game scenes
- [ ] Tooltips and overlays have sufficient background opacity
- [ ] Text outlines or shadows are used wherever backgrounds are unpredictable

---

## 7. Functional Color Assignments

Summary of all functional color roles across the game UI.

| Function | Dark Theme Hex | Light Theme Hex | Must Pair With |
|----------|---------------|----------------|----------------|
| Health | `#E63946` | `#C62828` | Heart icon + numeric value |
| Mana / Energy | `#3A86FF` | `#1565C0` | Crystal icon + numeric value |
| Stamina | `#2EC4B6` | `#00897B` | Lightning icon + numeric value |
| XP / Progress | `#E2B714` | `#F9A825` | Star icon + numeric value |
| Damage dealt | `#FFFFFF` (floating) | `#212121` | Minus sign prefix |
| Healing received | `#2EC4B6` | `#00897B` | Plus sign prefix |
| Error / Invalid | `#E63946` | `#C62828` | X icon + text message |
| Success / Confirm | `#27AE60` | `#2E7D32` | Checkmark icon |
| Warning / Caution | `#FF9F1C` | `#EF6C00` | Triangle icon |
| Info / Neutral | `#3A86FF` | `#1565C0` | Circle-i icon |
| Disabled / Inactive | `#616161` | `#BDBDBD` | Reduced opacity + strikethrough |
| Selected / Active | `#E2B714` | `#F9A825` | Bold border or glow |
| Hover / Focus | `#5FA8FF` | `#42A5F5` | Underline or scale change |

---

## Cross-References

- For colorblind mode implementation details, see `references/accessibility-standards.md`
- For font color and sizing, see `references/font-guidelines.md`
- For rarity color display in context, see `references/ui-patterns.md`
- For HUD color usage examples, see `references/hud-case-studies.md`
