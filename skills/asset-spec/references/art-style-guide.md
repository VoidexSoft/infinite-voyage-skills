# Art Style Guide — Infinite Voyage

This document defines the visual identity of Infinite Voyage. Every asset created for
the game must align with these guidelines to ensure a cohesive visual experience.
Reference this guide in every asset specification.

---

## Visual Pillars

The art direction of Infinite Voyage rests on five visual pillars. Every art decision
should serve at least one of these pillars.

### 1. Grounded Wonder

The world feels real enough to inhabit but extraordinary enough to explore. Environments
are rooted in believable geology, architecture, and ecology, but punctuated by elements
that could not exist in our world -- crystalline formations, bioluminescent flora,
gravity-defying ruins. The wonder comes from contrast: familiar landscapes disrupted
by the impossible.

### 2. Weathered History

Everything in the world has a past. Surfaces show wear, erosion, and repair. Armor has
dents and polished spots from use. Walls bear the marks of centuries. Nothing looks
factory-new. This weathering tells stories without words and gives the world a sense
of deep time and lived experience.

### 3. Readable Silhouettes

At every distance, the player should instantly identify what they are looking at.
Characters, enemies, and interactive objects must have strong, distinctive outlines.
In combat, the player must distinguish friend from foe at a glance. Shape language
is prioritized over texture detail.

### 4. Warm Palette, Cool Mystery

The known world -- friendly settlements, allied NPCs, safe zones -- uses warm tones
(amber, gold, sienna, terracotta). The unknown -- ruins, hostile territories, ancient
technology -- uses cool tones (steel blue, teal, violet, silver). This duality guides
the player emotionally through the world.

### 5. Purposeful Detail

Detail is allocated where the player looks. Faces and hands receive the most attention.
Hero weapons and interactive objects are next. Background elements and distant
terrain use broad strokes. Ornamental detail serves the narrative (runes tell a story,
wear patterns reveal use) rather than existing for its own sake.

---

## Color Palette

### Primary Palette

The primary palette defines the core colors used across the game. These appear most
frequently and establish the overall tone.

| Color | Hex | RGB | Use |
|-------|-----|-----|-----|
| Warm Stone | `#C4A882` | 196, 168, 130 | Architecture, terrain, neutral surfaces |
| Deep Earth | `#5C4033` | 92, 64, 51 | Shadows, wood, organic materials |
| Sky Gold | `#D4A843` | 212, 168, 67 | Sunlight, warmth indicators, friendly accents |
| Iron Gray | `#6B7280` | 107, 114, 128 | Metal, armor, industrial surfaces |
| Night Blue | `#2D3A5C` | 45, 58, 92 | Shadows, night scenes, mystery areas |

### Secondary Palette

Secondary colors support the primary palette and add variety without overwhelming it.

| Color | Hex | RGB | Use |
|-------|-----|-----|-----|
| Verdant Green | `#4A7C59` | 74, 124, 89 | Vegetation, healing, nature magic |
| Rust Red | `#8B3A2F` | 139, 58, 47 | Danger, damage indicators, dried blood |
| Dust Rose | `#B5838D` | 181, 131, 141 | Fabric, textiles, organic warmth |
| Slate Teal | `#4A8C8C` | 74, 140, 140 | Water, ancient tech active, cool balance |
| Pale Sand | `#E8DCC8` | 232, 220, 200 | Highlights, parchment, light surfaces |

### Accent Palette

Accents are used sparingly for emphasis, interactivity, and magical elements.

| Color | Hex | RGB | Use |
|-------|-----|-----|-----|
| Arcane Blue | `#00A8E8` | 0, 168, 232 | Active ancient technology, portals |
| Ember Orange | `#E85D04` | 232, 93, 4 | Fire, critical alerts, lava |
| Spirit Violet | `#7B2D8E` | 123, 45, 142 | Corruption, dark magic, mystery |
| Life Green | `#38B000` | 56, 176, 0 | Healing, buffs, positive status |
| Void White | `#F0F0F0` | 240, 240, 240 | Celestial elements, holy effects |

### Color Usage Rules

1. **70/20/10 rule** -- 70% primary palette, 20% secondary, 10% accents
2. **Warm for safety** -- Friendly NPCs, safe areas, and health use warm tones
3. **Cool for danger** -- Enemies, hazards, and the unknown use cool tones
4. **Accents for interactivity** -- Glow, pulse, or highlight on interactive objects
5. **Desaturation with distance** -- Far objects shift toward desaturated palette
6. **Never pure black or white** -- Darkest value: `#1A1A2E`; lightest: `#F0F0F0`

---

## Rendering Style

### Overall Approach

Infinite Voyage uses a **stylized realism** approach. Surfaces use physically-based
rendering (PBR) with metalness/roughness workflow, but textures are hand-adjusted to
emphasize form and readability over photographic accuracy.

| Attribute | Direction |
|-----------|-----------|
| Geometry | Realistic proportions with slight stylization (slightly larger heads, expressive hands) |
| Textures | PBR base with hand-painted detail overlay (edge wear, color variation) |
| Lighting | Physically-based with artistic overrides (fill lights, rim lights for readability) |
| Shadows | Soft shadows with slight warmth in ambient; cool in direct shadow |
| Post-processing | Subtle color grading, light bloom, depth of field for cinematics |

### PBR Material Conventions

All materials use the metalness/roughness PBR workflow.

#### Required Texture Maps

| Map | Format | Channel | Notes |
|-----|--------|---------|-------|
| **Albedo (Base Color)** | sRGB | RGB | No lighting baked in; pure color |
| **Normal Map** | Linear | RG (reconstruct B) | Tangent-space; OpenGL Y+ convention |
| **ORM (packed)** | Linear | R=AO, G=Roughness, B=Metallic | Channel-packed for efficiency |
| **Emissive** | sRGB | RGB | Only where needed (glowing elements) |
| **Height / Displacement** | Linear | R | For parallax or tessellation (optional) |

#### Material Value Ranges

| Material | Metallic | Roughness | Notes |
|----------|----------|-----------|-------|
| Raw metal (iron, steel) | 0.85-1.0 | 0.3-0.6 | Rougher = more weathered |
| Polished metal (gold, silver) | 0.9-1.0 | 0.1-0.3 | Smooth, reflective |
| Painted metal | 0.0 | 0.4-0.7 | Paint is non-metallic; only bare spots are metal |
| Stone / rock | 0.0 | 0.6-0.9 | Rough, matte; slight variation |
| Wood | 0.0 | 0.5-0.8 | Moderate roughness; grain direction visible |
| Leather | 0.0 | 0.5-0.7 | Smooth areas on wear spots |
| Fabric / cloth | 0.0 | 0.7-0.95 | Very rough; absorbs light |
| Skin (human) | 0.0 | 0.4-0.6 | Use subsurface scattering where available |
| Crystal / glass | 0.0 (transparent) | 0.0-0.2 | Specular reflections; refraction optional |
| Wet surface (any) | Same as dry | Dry value - 0.3 | Wetness lowers roughness |

---

## Lighting Mood

### Exterior Lighting

| Time of Day | Key Light Color | Intensity | Shadow Tone | Mood |
|-------------|----------------|-----------|-------------|------|
| Dawn | Warm amber `#FFB347` | Medium | Cool blue-violet | Hopeful, fresh |
| Midday | Warm white `#FFF5E1` | High | Neutral gray | Clear, active |
| Golden hour | Deep gold `#E89B3A` | Medium-high | Deep warm brown | Nostalgic, warm |
| Dusk | Rose-orange `#E8735A` | Medium | Blue-purple | Winding down |
| Night | Pale blue `#8CA8D4` | Low | Deep blue-black | Mysterious, quiet |
| Overcast | Desaturated gray `#C0C0C0` | Medium-low | Soft, diffuse | Somber, moody |

### Interior Lighting

| Setting | Key Light Source | Color | Fill | Mood |
|---------|-----------------|-------|------|------|
| Torchlit dungeon | Point lights (torches) | Warm orange `#FF8C42` | Faint cool bounce | Dangerous, tense |
| Ancient ruin | Bioluminescent panels | Cool teal `#4AC4C4` | Dark, minimal fill | Alien, mysterious |
| Friendly tavern | Fireplace + candles | Warm gold `#E8C547` | Warm ambient fill | Safe, inviting |
| Crystal cave | Emissive crystals | Violet-blue `#8B5CF6` | Scattered refractions | Wondrous, magical |
| Open temple | Shafts of sunlight | Warm white `#FFF8E7` | Blue ambient fill | Sacred, grand |

### Lighting Rules

1. **Always have a readable key light** -- Even in dark scenes, the player and threats must be visible
2. **Warm key, cool fill** (or vice versa) -- Complementary temperatures create depth
3. **Rim light for characters** -- Separate characters from background in dark scenes
4. **Emissive accents for guidance** -- Subtle glow on interactive objects and paths
5. **Avoid flat lighting** -- Every scene needs shadow contrast for depth perception

---

## VFX Style

### Particle Effects

| Element | Style | Color | Opacity | Notes |
|---------|-------|-------|---------|-------|
| Fire | Animated flipbook, soft edges | Orange core, yellow edges | 60-80% | Additive blending |
| Smoke | Billowing cards, slow drift | Gray, slight warm tint | 30-50% | Alpha blended |
| Magic (arcane) | Geometric shapes, rune patterns | Arcane Blue `#00A8E8` | 50-70% | Glow + distortion |
| Healing | Rising particles, soft bloom | Life Green `#38B000` | 40-60% | Soft additive |
| Impact dust | Burst + fade, small particles | Warm Stone tint | 40-60% | Brief duration |
| Blood / damage | Directional spray, decal splat | Rust Red `#8B3A2F` | 70-90% | Physics-affected |
| Electric / lightning | Branching lines, bright flash | Pale blue-white | 80-100% | Very brief, high contrast |

### VFX Rules

1. **Readable over any background** -- Effects must be visible on both dark and light surfaces
2. **Duration matches impact** -- Light attacks get quick, subtle VFX; heavy attacks get big VFX
3. **Color-coded by school** -- Fire = orange, ice = blue, nature = green, dark = violet
4. **Never obscure gameplay** -- VFX should enhance, not block the player's view of threats
5. **Scale with importance** -- Basic abilities get subtle effects; ultimates get spectacle

---

## UI Art Direction

### UI Style

The Infinite Voyage interface uses a **diegetic-adjacent** style. UI elements are not
part of the game world, but they borrow materials and motifs from the world. Frames
use weathered metal and parchment textures. Icons use stylized iconography consistent
with the game's aesthetic.

### UI Color Scheme

| Element | Color | Notes |
|---------|-------|-------|
| Background panels | `#1A1A2E` at 85% opacity | Dark, translucent |
| Frame borders | `#6B7280` (Iron Gray) | Metallic, beveled |
| Text (primary) | `#F0F0F0` (Void White) | High contrast on dark |
| Text (secondary) | `#C4A882` (Warm Stone) | Lower emphasis |
| Highlight / selected | `#D4A843` (Sky Gold) | Active state |
| Disabled | `#4A4A5A` | Dimmed, inactive |
| Health | `#8B3A2F` (Rust Red) | Health bar, damage |
| Mana / Energy | `#00A8E8` (Arcane Blue) | Resource bar |
| XP / Progress | `#D4A843` (Sky Gold) | Progress indicators |
| Alert / Error | `#E85D04` (Ember Orange) | Critical notifications |

### UI Typography

| Use | Font Style | Size Range | Weight |
|-----|-----------|------------|--------|
| Headers | Serif, decorative | 24-48 pt | Bold |
| Body text | Sans-serif, clean | 14-18 pt | Regular |
| Labels | Sans-serif, condensed | 10-14 pt | Medium |
| Damage numbers | Display, impact | 24-72 pt | Black |
| Tooltips | Sans-serif | 12-14 pt | Regular |

---

## Mood Board Descriptions

The following mood board descriptions guide the overall visual targets. Actual mood
boards should be assembled with reference images in the team's shared art folder.

### Board 1: The Known World

A sunlit village built into a hillside, stone and timber construction with warm-toned
plaster walls. Clotheslines and market stalls add color. Paths are worn cobblestone.
Vegetation is lush but controlled -- gardens, not wilderness. People move with purpose.
The feeling is lived-in warmth, like a place you want to return to.

### Board 2: The Ruins Below

A vast underground chamber lit by faint bioluminescent patterns on the walls. The
architecture is geometric and alien -- smooth curves and precise angles unlike
anything human-built. Centuries of dust and debris soften the edges. Occasional shafts
of light from cracks above create dramatic pools of illumination. The feeling is
awe mixed with unease.

### Board 3: The Wild Frontier

Rolling hills and ancient forests under a wide sky. Rock formations jut from the
landscape at dramatic angles. Weather-worn standing stones mark forgotten paths. The
vegetation shifts from temperate to alien as you move away from settlements -- familiar
oaks giving way to spiraling crystalline growths. The feeling is vast freedom with
hints of the strange.

### Board 4: The Hostile Depths

Narrow corridors carved into dark stone. Faintly glowing corruption creeps along
surfaces like luminous fungus. The architecture was once magnificent but is now twisted
and broken. Shadows are deep and move at the edges of torchlight. The air feels thick.
Every surface tells a story of conflict and decay. The feeling is claustrophobic tension.

### Board 5: The Ascension

High altitude environments bathed in golden light. Cloud layers visible below. Ancient
structures reach skyward -- observatories, bridges between peaks, monuments to a
civilization that looked upward. Materials shift from stone to metal to crystal. The
wind is visible in cloth and particle effects. The feeling is transcendent discovery.

---

## Character Proportions

### Player Characters

| Attribute | Value | Notes |
|-----------|-------|-------|
| Head-to-body ratio | 1:7 | Realistic adult proportions |
| Shoulder width | 2 head-widths (male) / 1.7 (female) | Slightly heroic |
| Hand size | Slightly oversized (+10%) | Better readability in third person |
| Eye size | Slightly large (+15%) | More expressive for dialogue |
| Overall build | Athletic, capable | Adventurers, not bodybuilders |

### NPC Variation

NPCs should vary more widely than player characters to create visual variety. Age,
body type, and posture should reflect their role (merchant is soft and round; guard
is broad and stiff; scholar is thin and stooped).

### Enemy Design

Enemies follow exaggerated proportions to be instantly identifiable as threats:
- **Small enemies:** 0.5-0.8x player height, quick silhouette
- **Standard enemies:** 0.9-1.2x player height, distinct shape language
- **Large enemies:** 1.5-3x player height, imposing presence
- **Bosses:** Variable, but always the dominant visual element in their arena

---

## Material Weathering Standards

All materials should show appropriate wear. The degree of weathering communicates
the object's history.

| Weathering Level | Description | Example |
|-----------------|-------------|---------|
| **New** | Minimal wear, clean surfaces | Freshly forged weapon, new fabric |
| **Used** | Edge wear, minor scuffs, natural patina | Player's starting equipment |
| **Worn** | Significant scratches, faded color, repairs visible | Veteran NPC gear |
| **Aged** | Heavy patina, cracks, moss/lichen, structural damage | Ancient ruins, old furniture |
| **Ruined** | Broken, collapsed, overgrown, barely recognizable | Deep dungeon structures |

### Weathering Rules

1. **Player equipment:** Used to Worn (shows experience, not neglect)
2. **Settlement objects:** New to Used (maintained by inhabitants)
3. **Wild objects:** Worn to Aged (exposed to elements)
4. **Ruin objects:** Aged to Ruined (centuries of decay)
5. **Ancient tech:** Aged surface, pristine core (durable materials, worn exterior)

---

*Last updated for Infinite Voyage pre-production. This guide is a living document
and will be updated as the art direction evolves through vertical slice and alpha.*
