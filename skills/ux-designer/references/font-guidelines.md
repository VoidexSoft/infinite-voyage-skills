# Game Typography Guide

Reference for font selection, sizing, and readability across platforms.
Typography in games must balance aesthetic cohesion with legibility under diverse conditions:
varying screen sizes, viewing distances, localization into dozens of languages, and
accessibility requirements.

---

## 1. Minimum Font Sizes by Platform

Font sizes are specified in logical pixels at each platform's reference resolution. Actual
rendered size depends on display DPI and scaling factor.

### PC (Desktop Monitor, 2-3 ft Viewing Distance)

| Text Role | Minimum Size (1080p) | Recommended Size (1080p) | Minimum Size (1440p) | Minimum Size (4K) |
|-----------|---------------------|-------------------------|---------------------|-------------------|
| Body text | 16px | 18px | 21px | 32px |
| Secondary / hint text | 14px | 16px | 18px | 28px |
| Headings (H1) | 28px | 32px | 37px | 56px |
| Headings (H2) | 22px | 26px | 29px | 44px |
| Button labels | 16px | 18px | 21px | 32px |
| Tooltip text | 14px | 16px | 18px | 28px |
| HUD labels | 14px | 16px | 18px | 28px |
| Damage numbers | 18px | 22px | 24px | 36px |
| Subtitles | 20px | 24px | 27px | 40px |

### Console (TV, 6-10 ft Viewing Distance)

Console text must be significantly larger because players sit farther from the screen.

| Text Role | Minimum Size (1080p) | Recommended Size (1080p) | Minimum Size (4K) |
|-----------|---------------------|-------------------------|-------------------|
| Body text | 24px | 28px | 48px |
| Secondary / hint text | 20px | 24px | 40px |
| Headings (H1) | 36px | 42px | 72px |
| Headings (H2) | 30px | 34px | 60px |
| Button labels | 24px | 28px | 48px |
| Tooltip text | 20px | 24px | 40px |
| HUD labels | 20px | 24px | 40px |
| Damage numbers | 26px | 32px | 52px |
| Subtitles | 28px | 36px | 56px |

### Mobile (Handheld, 12-18 in Viewing Distance)

Mobile uses physical size targets because device DPIs vary widely.

| Text Role | Minimum (dp/pt) | Recommended (dp/pt) | Notes |
|-----------|----------------|---------------------|-------|
| Body text | 14dp | 16dp | Android dp / iOS pt |
| Secondary text | 12dp | 14dp | Avoid below 12dp |
| Headings (H1) | 22dp | 26dp | |
| Headings (H2) | 18dp | 22dp | |
| Button labels | 14dp | 16dp | Touch target min 48dp height |
| Tooltip text | 12dp | 14dp | |
| HUD labels | 12dp | 14dp | |
| Subtitles | 16dp | 20dp | |

### Nintendo Switch (Docked vs Handheld)

| Mode | Body Minimum | Subtitle Minimum | Notes |
|------|-------------|------------------|-------|
| Docked (TV) | 24px at 1080p | 28px | Same as console guidelines |
| Handheld (6.2" screen) | 18px at 720p | 22px | Similar to mobile but higher DPI |

---

## 2. Readable Fonts for Games

### Recommended Font Families

#### Sans-Serif (Primary for UI)

| Font | Weight Range | Strengths | License |
|------|-------------|-----------|---------|
| Inter | 100-900 | Excellent screen readability, large x-height, open source | SIL OFL |
| Noto Sans | 100-900 | Massive language coverage (900+ languages), Google-maintained | SIL OFL |
| Source Sans Pro | 200-900 | Designed for UI, clear at small sizes | SIL OFL |
| Roboto | 100-900 | Clean geometry, good for HUD elements | Apache 2.0 |
| Open Sans | 300-800 | Neutral, highly legible, widely used | SIL OFL |
| Lato | 100-900 | Warm, humanist feel while remaining clear | SIL OFL |

#### Serif (Flavor Text, Lore, Headings)

| Font | Weight Range | Strengths | License |
|------|-------------|-----------|---------|
| Cinzel | 400-900 | Elegant, fantasy/RPG feel, uppercase display | SIL OFL |
| EB Garamond | 400-800 | Classic book typography, excellent for lore text | SIL OFL |
| Playfair Display | 400-900 | High contrast, decorative headings | SIL OFL |
| Merriweather | 300-900 | Designed for screens, readable at small sizes | SIL OFL |

#### Monospace (Debug, Console, Data Tables)

| Font | Weight Range | Strengths | License |
|------|-------------|-----------|---------|
| JetBrains Mono | 100-800 | Designed for code, distinct characters | SIL OFL |
| Fira Code | 300-700 | Ligatures, clear differentiation of similar chars | SIL OFL |
| Source Code Pro | 200-900 | Clean, consistent widths | SIL OFL |

### Font Selection Criteria

When choosing fonts for your game:

1. **x-height** -- Prefer fonts with a tall x-height (the height of lowercase letters like
   "x" and "o"). Taller x-height improves readability at small sizes.
2. **Character distinction** -- Ensure `I` (capital i), `l` (lowercase L), and `1` (one)
   are visually distinct. Same for `O` (capital o) and `0` (zero).
3. **Open counters** -- Letters like `a`, `e`, `c`, `s` should have open, spacious counters
   (the enclosed or partially enclosed spaces in letters).
4. **Weight range** -- At least Regular (400) and Bold (700) for hierarchy. Prefer families
   with 4+ weights.
5. **Hinting** -- Fonts with good screen hinting render crisply at small sizes, especially
   on lower-resolution displays.

---

## 3. Localization Font Considerations

### Script Coverage Requirements

Your game should support at a minimum:

| Script | Languages | Font Requirement |
|--------|-----------|-----------------|
| Latin | English, French, German, Spanish, Portuguese, Italian, Polish, Turkish | Base font must cover Latin Extended |
| Cyrillic | Russian, Ukrainian | Cyrillic block required |
| CJK | Chinese (Simplified/Traditional), Japanese, Korean | Dedicated CJK font required (Noto Sans CJK) |
| Arabic | Arabic, Persian | Right-to-left support, contextual shaping |
| Thai | Thai | Complex script shaping |
| Devanagari | Hindi | Complex script shaping |

### CJK Considerations

- CJK characters are typically wider than Latin characters (full-width vs half-width)
- UI layouts must accommodate ~40% text expansion for CJK compared to English
- Line breaking rules differ: CJK can break at any character; Japanese has special rules
  for punctuation (kinsoku shori)
- Minimum font size for CJK readability is 2px larger than Latin equivalents
- Recommended CJK font: Noto Sans CJK (covers all three scripts, SIL OFL)

### Text Expansion Factors

When designing UI, reserve space for the longest supported language.

| Source Language | Target Language | Typical Expansion |
|----------------|----------------|-------------------|
| English | German | +30% |
| English | French | +20% |
| English | Russian | +20% |
| English | Japanese | -10% to +10% (character density varies) |
| English | Chinese (Simplified) | -30% to +10% |
| English | Arabic | +25% |
| English | Portuguese (BR) | +25% |

### RTL (Right-to-Left) Layout

- Arabic and Hebrew require mirrored UI layouts
- Navigation flows from right to left
- Icons and progress bars reverse direction
- Text alignment flips; numbers remain LTR within RTL text
- Test all UI screens in RTL mode during development

---

## 4. Dynamic Text Scaling

Players must be able to adjust text size to their comfort level.

### Scaling System

| Scale Level | Multiplier | Body Text (1080p PC) | Body Text (1080p Console) |
|-------------|-----------|---------------------|--------------------------|
| Small | 0.85x | 14px | 20px |
| Default | 1.0x | 16px | 24px |
| Large | 1.25x | 20px | 30px |
| Extra Large | 1.5x | 24px | 36px |
| Maximum | 2.0x | 32px | 48px |

### Implementation Rules

1. **Relative units** -- All text sizes defined as multipliers of a base size, never
   hardcoded pixel values in final rendering.
2. **Container reflow** -- UI containers must grow to accommodate larger text. Fixed-size
   containers that clip text are not acceptable.
3. **Truncation** -- If text cannot reflow, truncate with ellipsis (`...`) and provide
   full text in a tooltip or on hover.
4. **Independent scaling** -- Text scale is a separate setting from HUD scale. Players may
   want large text with a compact HUD or vice versa.
5. **Preview** -- Show a live preview of the text size change in the settings screen.
6. **Minimum floor** -- Even at the smallest scale, no text should render below 12px on PC
   or 18px on console at 1080p.

---

## 5. HUD Fonts vs Menu Fonts

Different contexts demand different typographic treatment.

### HUD Typography

The HUD competes with gameplay visuals for attention. HUD text must be instantly readable
in fractions of a second, often in motion.

| Property | Guideline |
|----------|-----------|
| Font family | Sans-serif only (Inter, Roboto, or custom sans-serif) |
| Font weight | Bold (700) or Semi-Bold (600) for all HUD text |
| Font size | Minimum sizes from platform tables above; err on the larger side |
| Text shadow | 2px dark shadow (rgba(0,0,0,0.8)) for readability over any background |
| Outline | 1-2px dark outline as an alternative to shadow |
| Color | High contrast (white on dark backgrounds, outlined on bright scenes) |
| Alignment | Left-aligned for labels; right-aligned for numeric values |
| Kerning | Slightly expanded (+0.02em) for clarity at a glance |
| Anti-aliasing | Subpixel rendering on PC; grayscale on console |
| Motion | HUD text should not animate (no bobbing, shaking, or spinning) |
| Damage numbers | Can use a display/decorative font if legible; bold, large, outlined |

### Menu Typography

Menus are viewed at rest. Players take time to read and navigate. This allows for more
expressive typography.

| Property | Guideline |
|----------|-----------|
| Font family | Sans-serif for body; serif or decorative for headings (e.g., Cinzel for H1) |
| Font weight | Regular (400) for body; Bold (700) for headings; Light (300) for flavor text |
| Font size | Follow minimum platform tables; headings 1.5-2x body size |
| Line height | 1.5x font size for body text; 1.2x for headings |
| Paragraph spacing | 0.75em between paragraphs |
| Max line length | 60-80 characters per line for comfortable reading |
| Color | Primary text color from palette; secondary color for descriptions |
| Alignment | Left-aligned for body; center-aligned for titles and buttons |
| Kerning | Default or slightly tight for headings; default for body |
| Background | Solid or high-opacity panel behind text; never transparent over gameplay |

---

## 6. Font Rendering Quality

### Anti-Aliasing Modes

| Mode | Best For | Notes |
|------|----------|-------|
| Subpixel (ClearType/FreeType) | PC monitors with fixed pixel grid | Sharpest on LCD; artifacts on OLED |
| Grayscale | Console/TV, rotated text, OLED screens | Slightly softer but no color fringing |
| None (bitmap) | Pixel art games, retro aesthetics | Not recommended for most games |

### Rendering Checklist

- [ ] Text is crisp at the smallest supported size on all target platforms
- [ ] No visible aliasing artifacts on diagonal strokes
- [ ] Font weight renders consistently across platforms (PC, PS5, Xbox, Switch)
- [ ] Bold and regular weights are visually distinct at all sizes
- [ ] Text remains readable when the game is running at lower resolutions (720p fallback)

---

## 7. Typography Hierarchy Summary

A consistent hierarchy ensures players instinctively know what to read first.

| Level | Example | Font | Weight | Size (1080p PC) | Color |
|-------|---------|------|--------|-----------------|-------|
| Display | "INFINITE VOYAGE" (title screen) | Cinzel | Bold | 48-64px | Gold `#E2B714` |
| H1 | "Inventory" (screen title) | Cinzel | Bold | 28-32px | Ivory `#F0E6D3` |
| H2 | "Weapons" (section header) | Inter | Semi-Bold | 22-26px | Ivory `#F0E6D3` |
| H3 | "Damage" (stat label) | Inter | Semi-Bold | 18-20px | Ivory `#F0E6D3` |
| Body | "A reliable blade for close combat." | Inter | Regular | 16-18px | Ivory `#F0E6D3` |
| Caption | "Acquired: Chapter 3" | Inter | Regular | 14-16px | Ash `#A0937D` |
| Label | "ATK: 25" | Inter | Bold | 14-16px | Ivory `#F0E6D3` |
| HUD | "HP: 75/100" | Inter | Bold | 16-20px | White `#FFFFFF` |
| Button | "EQUIP" | Inter | Bold | 16-18px | White `#FFFFFF` |
| Tooltip | Item description text | Inter | Regular | 14-16px | Ivory `#F0E6D3` |
| Subtitle | Dialogue captions | Inter | Semi-Bold | 20-24px | White `#FFFFFF` |

---

## Cross-References

- For color values used in text, see `references/color-palettes.md`
- For subtitle sizing requirements, see `references/accessibility-standards.md`
- For HUD text placement, see `references/hud-case-studies.md`
- For localization impact on UI layout, see the Screen Specification Template in `SKILL.md`
