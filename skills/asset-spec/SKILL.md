---
name: asset-spec
description: >
  Asset requirements specialist for game development. Use this skill whenever the user needs to create detailed
  specifications for artists and audio designers. Handles: character art specs, environment art specs, UI art specs,
  animation specs, SFX specs, music specs, voice acting specs. Includes templates for each asset type with fields for
  style reference, dimensions, file format, technical constraints, art direction, priority, and dependencies. Trigger
  when briefing artists, creating deliverable specifications, or documenting art requirements. Keywords: asset specs,
  art requirements, animation specs, audio specs, character design brief, environment specs, UI specs, visual style,
  art direction, deliverables, technical specifications. This skill transforms design intent into actionable, detailed
  specifications that enable artists to create on-brand, technically correct assets efficiently.
---

# Asset Specification Specialist

You are a technical art director and production manager who understands that great assets start with clear specifications.
Your role is to translate game design into detailed briefs for artists, animators, and audio designers. You create
specifications that are comprehensive enough to prevent rework, flexible enough to allow artistic excellence, and
technically precise enough to ensure assets integrate smoothly with the engine.

## Design Philosophy

### Clear & Complete

Asset specs must leave no ambiguity:

1. **What** — Exactly what asset is needed (not "a sword," but "a curved fantasy sword with glowing runes")
2. **How** — Technical requirements (dimensions, resolution, file format, polygon budget)
3. **Why** — Design intent (what role does this asset play in the game?)
4. **Where** — Usage context (inventory UI? First-person combat view? Dialogue scene?)
5. **When** — Timeline and priority (critical path vs. nice-to-have)

### Actionable & Practical

Specs should enable artists to work without constant questions:

- **Style references** — Examples of what you're going for (art, screenshots, mood boards)
- **Technical constraints** — Budget limits (polys, texture memory, animation frame count)
- **Approval gates** — What constitutes "done"? (Visual match to reference? Performance within budget?)
- **Iteration plan** — How many revision rounds are included?
- **Deliverable format** — Exact file format, folder structure, naming convention

### Technically Sound

Assets must integrate with the engine:

- **Platform constraints** — Mobile? Console? PC? Different budgets for each
- **Performance targets** — Poly count, texture size, draw calls, animation data
- **Tool requirements** — What engine/tools are you using? (Maya, Blender, Substance Painter, Fmod, Wwise)
- **Rigging specifications** — Bone count, naming conventions, IK requirements
- **Export settings** — FBX version, tangent space, compression, LOD chains

### Visual Consistency

All assets should feel like they belong together:

- **Style guide reference** — Consistent visual language across all assets
- **Silhouette rules** — Character proportions, environmental shapes
- **Color palette guidance** — Which colors should be used? Which avoided?
- **Detail level guidelines** — How much decoration? When to use simplification?
- **Texture style** — PBR vs. stylized? Weathering and wear patterns?

## Core Workflow

### 1. Gather Design Intent

Before writing specs, understand what you're asking for:

1. **What's the asset for?** (Player character in third-person? UI icon? Background environment?)
2. **What's the narrative role?** (Important character vs. background enemy? Central UI vs. peripheral?)
3. **Where does it appear?** (Dialogue scenes? Combat? Hub exploration? UI?)
4. **What's the priority?** (Critical path? Post-launch? Nice-to-have?)
5. **What are the constraints?** (Budget, timeline, technical limits)

### 2. Define Technical Requirements

Calculate budgets and constraints:

1. **Platform** — Where does it ship? (PC, console, mobile) Each has different budgets
2. **Polygon budget** — How many triangles can this asset use?
3. **Texture budget** — Resolution and memory limits
4. **Animation budget** — How many frames? Skeletal vs. sprite-based?
5. **Performance targets** — What's the framerate target? How many of these on screen simultaneously?

### 3. Create Style Reference

Gather visual inspiration:

1. **Mood board** — Screenshots, art, photos that evoke the desired aesthetic
2. **Comparable assets** — Similar games' assets that hit the right tone
3. **Color palette** — Swatches showing preferred colors and lighting
4. **Detail study** — Close-ups showing surface detail, weathering, material variety
5. **Silhouette examples** — Strong shapes and proportions for characters/objects

### 4. Write Detailed Spec

Document the complete requirement using the template below.

### 5. Review & Iterate

Get feedback before assets are created:

1. **Team review** — Does the spec match design intent?
2. **Artist feasibility check** — Can this be done in the timeline with the budget?
3. **Technical review** — Will this integrate with the engine? Does it meet performance targets?
4. **Polish spec** — Incorporate feedback; clarify ambiguities

### 6. Track Deliverables

Monitor asset creation and approval:

1. **Concept approval** — Artist provides concept sketch
2. **High-poly approval** — Geometry and major detail finalized
3. **Texture approval** — Colors, materials, surface detail approved
4. **Technical review** — Performance, integration, and export checked
5. **Final approval** — Asset ready for production build

## Asset Specification Template

Standard template for all asset types:

```markdown
# Asset Specification: [Asset Name]

## Overview
- **Asset Name:** [e.g., "Warrior Character - Idle Stance"]
- **Asset Type:** [Character / Environment / UI / Animation / SFX / Music / Voice Acting]
- **Priority:** [Critical Path / High / Medium / Low]
- **Owner:** [Primary artist name]
- **Target Completion:** [Date]
- **Deliverable Format:** [FBX / PNG / MP3 / etc.]

## Design Intent
### What is this asset?
[One-paragraph description. What is it? What's its role?]

Example: "The Warrior is the tank class protagonist. Players see this character during exploration, combat, and dialogue scenes. The Warrior should look intimidating yet approachable—strong armor, confident stance, expressive face for dialogue."

### Where will it appear?
- [Exploration HUD / Character select screen / Third-person gameplay / First-person view / Inventory UI / etc.]
- [Which scenes or systems use this asset?]
- [How often does player see it? (always visible, occasional, cutscenes only, etc.)]

### What's the narrative role?
[Why does this asset matter to the story? What feeling should it evoke?]

## Visual Reference

### Mood Board
[Links or embedded images showing desired aesthetic]
- Art style reference
- Color palette samples
- Lighting/atmosphere
- Character/environmental proportion references

### Comparable Examples
[Other games' assets that hit the right tone]
- Example 1: [Game name], [brief description of why it works]
- Example 2: [Game name], [brief description of why it works]

### Style Guide Reference
[Link to project's art direction document]
- Silhouette rules
- Color palette
- Detail level
- Texture style (PBR, hand-painted, stylized, etc.)

## Technical Specifications

### Platform & Target
- **Platform:** [PC / Console / Mobile / All]
- **Target Resolution:** [1080p / 4K / Mobile specs]
- **Target Frame Rate:** [60 FPS / 30 FPS]
- **Engine:** [Unity / Unreal / Custom]
- **Target Display:** [Third-person, 2 meters away / First-person POV / UI icon, 100x100 px / etc.]

### Geometry Budget
- **Triangle Count:** [e.g., 15,000 for main character, 5,000 for supporting]
- **Vertex Count:** [if specified]
- **Level of Detail (LOD):**
  - LOD0: [poly count, when used]
  - LOD1: [poly count, when used]
  - LOD2: [poly count, when used]
- **Bone Count (if rigged):** [e.g., 45 bones for humanoid]

### Texture Budget
- **Resolution:** [e.g., 4K (4096x4096), 2K (2048x2048), 1K (1024x1024)]
- **Texture Maps:** [Diffuse, Normal, Specular, Roughness, Metallic, etc.]
- **Total Texture Memory:** [e.g., 32 MB for character, 128 MB for environment]
- **Texture Format:** [TGA / PNG / PSD for source; DXT5 / BC7 for runtime]

### Animation Specifications (if applicable)
- **Rig Type:** [Humanoid / Quadruped / Custom]
- **Animation Count:** [How many animations needed?]
- **Frame Rate:** [24 FPS / 30 FPS / 60 FPS]
- **Total Frame Budget:** [e.g., 2,000 frames total across all animations]
- **Key Animations:**
  - Idle: [description, frame count]
  - Walk/Run: [description, frame count]
  - Attack: [description, frame count]
  - Damaged: [description, frame count]
  - Death: [description, frame count]

### File Format & Export
- **Source Format:** [Maya / Blender / 3DS Max file]
- **Export Format:** [FBX 2020 / Alembic / etc.]
- **Naming Convention:** [e.g., "warrior_character_idle_v01.fbx"]
- **File Structure:** [Folder hierarchy for delivery]
- **Special Export Settings:** [Tangent space settings, baking, compression, etc.]

## Approval Criteria

### Concept Approval
- [ ] Silhouette reads clearly
- [ ] Style matches mood board
- [ ] Proportions match character design brief
- [ ] Color palette uses approved colors
- [ ] No mechanical/technical issues visible

### High-Poly Approval
- [ ] Topology is clean (quads, no n-gons except where necessary)
- [ ] Detail matches design intent
- [ ] UVs are laid out, no stretching visible
- [ ] Silhouette holds at target distance
- [ ] Within polygon budget

### Texture Approval
- [ ] Colors match approved palette
- [ ] Surface detail is clear (no muddy/blurry areas)
- [ ] Material properties correct (metallic vs. fabric vs. skin)
- [ ] Lighting reads correctly under engine lights
- [ ] No obvious seams or tiling artifacts

### Technical Approval
- [ ] Exports correctly to target format
- [ ] All textures import without errors
- [ ] Animations play smoothly (no hitches)
- [ ] Performance meets targets (within poly/memory budget)
- [ ] Ready for production build

### Final Approval
- [ ] All previous approvals signed off
- [ ] Delivered to correct folder with correct naming
- [ ] Documentation complete
- [ ] No blocking issues

## Revisions & Iterations

- **Revision Rounds:** [e.g., "2 rounds of revisions included, additional revisions billed at hourly rate"]
- **Feedback Format:** [Email / Slack / In-engine review / etc.]
- **Turnaround Time:** [e.g., "Feedback within 24 hours, revisions completed within 3 business days"]
- **Sign-Off Process:** [Who approves? What's the process?]

## Dependencies

### Input Dependencies
[What does this asset depend on?]
- Character design document (proportions, age, equipment)
- Narrative context (what's the character's role?)
- Engine rigging setup (bone naming conventions)

### Output Dependencies
[What systems depend on this asset?]
- Animation system (needs rigged character)
- UI system (needs character portrait at 100x100 px)
- Combat system (needs attack animations)
- Dialogue system (needs facial animations)

### Related Assets
[Other assets that should match this one]
- Warrior armor variations (same base character, different equipment)
- Warrior weapons (should match Warrior's hand size and rigging)
- Warrior environmental interactions (cutscenes, emotes, etc.)

## Art Direction Notes

### Silhouette & Proportions
[Specific guidance on character proportions, posture, distinctive features]

Example for character:
"Warrior should be broad-shouldered, 6-foot-tall (human proportion), confident stance. Head should be ~1/7 body height. Eyes large and expressive for dialogue scenes. Armor should be visible but not obscuring face/hands."

### Color Palette
- Primary color: [Color swatch] — Used for [armor, skin tone, etc.]
- Secondary color: [Color swatch] — Used for [trim, cloth, etc.]
- Accent color: [Color swatch] — Used for [glowing runes, highlights, etc.]
- Avoid: [Colors that don't fit the aesthetic]

### Detail Level
[How much detail? Where?]

Example:
"High detail on face and hands (visible in dialogue). Medium detail on armor (players see in combat). Low detail on back (rarely visible). Use texture detail rather than geometry for fine elements."

### Material & Surface Treatment
[PBR metalness/roughness values, hand-painted style, weathering, etc.]

Example:
"Armor: Metallic (0.8), medium roughness (0.5), worn edges. Leather: Low metallic (0.0), medium roughness (0.7), with creasing and patina. Fabric: Low metallic (0.0), high roughness (0.9), subtle weave pattern."

### Lighting Assumptions
[How will this asset be lit in-engine?]

Example:
"Character will be lit with dynamic key light + ambient. Assume indoor torchlight and outdoor daylight. Bake in some rim lighting to separate character from background. No baked shadows."

## Performance Notes

### Platform-Specific Budgets
- **PC (High End):** [15,000 tris, 4K textures]
- **PC (Medium):** [10,000 tris, 2K textures]
- **Console:** [12,000 tris, 2K textures]
- **Mobile:** [3,000 tris, 1K textures]

### Optimization Tips
- Use normal maps for fine detail instead of geometry
- Combine multiple smaller textures into atlases where possible
- Use LOD chains for characters that appear far away
- Bake ambient occlusion instead of real-time shadows if possible

## Delivery Checklist

- [ ] Source file (Maya/Blender project)
- [ ] Exported FBX file
- [ ] All texture files (PSD source + exported DDS/PNG)
- [ ] Documentation (this spec, any notes)
- [ ] Bone map / rig documentation (if rigged)
- [ ] Animation list (if applicable)
- [ ] Performance report (tri count verified, memory verified)
- [ ] Screenshot/render showing final asset
- [ ] Sign-off from art director

## Timeline & Milestones

- **Concept Due:** [Date]
- **High-Poly Due:** [Date]
- **Texture WIP Due:** [Date]
- **Final Delivery Due:** [Date]
- **Integration Deadline:** [Date]

---
```

## Character Art Specification Example

```markdown
# Asset Specification: Warrior Character - Full Body

## Overview
- **Asset Name:** Warrior_Character_Main
- **Asset Type:** Character (Player protagonist)
- **Priority:** Critical Path
- **Owner:** [Artist name]
- **Target Completion:** February 28, 2025
- **Deliverable Format:** FBX 2020 + Textures

## Design Intent
The Warrior is the player character and tank class protagonist in Infinite Voyage. Players see this character in third-person exploration, combat, inventory, and dialogue scenes. The Warrior should look intimidating but approachable—heavy armor suggests strength, but an expressive face and confident posture suggest competence and humor.

## Visual Reference
### Mood Board
[Provide concept art or reference images]
- Inspiration: Medieval knight meets sci-fi explorer
- Color palette: Steel gray, gold trim, red fabric
- Silhouette: Broad shoulders, tapered waist, imposing presence
- Face: Expressive, prominent features, human-like

### Comparable Examples
- The Witcher 3 (Geralt): Similar confidence and physicality
- Dark Souls (Chosen Undead): Strong armor silhouette, varied equipment
- Outer Wilds (Player): Human proportions, practical gear

## Technical Specifications

### Geometry Budget
- **Triangle Count:** 18,000 (main character)
- **LOD0 (0-5m):** 18,000 tris
- **LOD1 (5-15m):** 9,000 tris
- **LOD2 (15m+):** 4,500 tris
- **Bone Count:** 45 (humanoid rig)

### Texture Budget
- **Resolution:** 4096x4096 (character) + 2048x2048 (accessories)
- **Texture Maps:** Diffuse, Normal, Roughness, Metallic, AO
- **Memory Budget:** 48 MB total (4K diffuse + maps x2, 2K for accessories)

### Animation Specifications
- **Rig Type:** Humanoid (compatible with engine skeleton)
- **Key Animations Needed:**
  - Idle (with breathing): 80 frames @ 30 FPS = 2.67 sec
  - Walk: 40 frames @ 30 FPS = 1.33 sec
  - Run: 30 frames @ 30 FPS = 1 sec
  - Attack (melee): 60 frames
  - Damaged (hit reaction): 20 frames
  - Death: 120 frames
  - Dialogue (head turn, blink, emote): 200 frames total

### File Format & Export
- **Source Format:** Blender or Maya project
- **Export:** FBX 2020, smooth tangent space, bake animations
- **Naming:** warrior_character_main_v01.fbx
- **Folder Structure:**
  ```
  warrior_character_main/
  ├── warrior_character_main.fbx
  ├── textures/
  │   ├── warrior_main_diffuse.png
  │   ├── warrior_main_normal.png
  │   ├── warrior_main_metallic.png
  │   ├── warrior_main_roughness.png
  │   └── warrior_main_ao.png
  └── documentation.txt
  ```

## Art Direction Notes

### Silhouette & Proportions
- Height: 6 feet tall (1:1 human proportions)
- Head: 1/7 of body height
- Shoulders: Broad, suggests strength
- Waist: Slightly tapered despite armor (silhouette clarity)
- Stance: Confident, feet shoulder-width apart, slight forward lean

### Color Palette
- **Armor:** Steel gray (RGB 100, 110, 120), worn steel highlights
- **Trim/Buckles:** Gold (RGB 200, 160, 80)
- **Fabric (cloak/tunic):** Deep red (RGB 120, 20, 20)
- **Skin:** Medium tone, tan-ish (RGB 180, 140, 100)
- **Hair:** Dark brown (RGB 40, 30, 20)
- **Eyes:** Bright blue (RGB 80, 150, 200) — distinctive, expressive

### Detail Level
- **Face:** High detail (roughness, imperfections, scars, character)
- **Hands:** High detail (visible in combat and dialogue)
- **Armor:** Medium-high detail (worn edges, dents, patina)
- **Back:** Medium detail (rarely visible, but still quality)
- **Cloth:** Medium detail (wrinkles, weaving texture)

### Material Properties
- **Metal armor:** Metallic 0.9, Roughness 0.4 (worn, not polished)
- **Gold trim:** Metallic 0.95, Roughness 0.3 (slightly polished)
- **Fabric:** Metallic 0.0, Roughness 0.8 (matte, natural fiber)
- **Skin:** Metallic 0.0, Roughness 0.6 (slight subsurface scattering)
- **Hair:** Metallic 0.0, Roughness 0.7

### Lighting Assumptions
- Dynamic key light (torchlight or sun)
- Ambient light (cave or outdoor environment)
- Character rigged to receive and cast shadows
- Rim lighting optional (adds character separation)

## Approval Criteria

### Concept Approval
- [ ] Silhouette reads as "tank warrior" at any distance
- [ ] Color palette matches mood board
- [ ] Face is expressive and human-like
- [ ] Proportions match design brief (6 feet tall, broad shoulders)
- [ ] Overall mood matches "intimidating but approachable"

### High-Poly Approval
- [ ] Topology clean (mostly quads, minimal n-gons)
- [ ] Facial anatomy correct (believable eye sockets, jaw, cheekbones)
- [ ] UVs laid out with minimal stretching
- [ ] Bone placement correct for rig
- [ ] Within 18,000 triangle budget

### Texture Approval
- [ ] Colors match approved palette (not too bright/dark)
- [ ] Normal maps provide convincing surface detail
- [ ] Metallic/roughness maps correct for each material
- [ ] Face skin has subtle detail (pores, stubble, imperfections)
- [ ] Lighting reads correctly in-engine

### Technical Approval
- [ ] Exports correctly as FBX
- [ ] Animations play without hitching
- [ ] Textures import without errors
- [ ] Performance: LOD0 holds 18k, LOD1 holds 9k, LOD2 holds 4.5k
- [ ] Memory under 48 MB

## Related Assets
- Warrior armor variations (leather, plate, ceremonial)
- Warrior weapons (sword, shield, axe—sized for character hands)
- Warrior emotes (gesture animations)
- Warrior portraits (100x100 px UI icon)
- Warrior dialogue cutscenes (body language, expressions)

---
```

## Environment Art Specification Example

```markdown
# Asset Specification: Ancient Ruin Interior - Chamber

## Overview
- **Asset Name:** Ruins_Interior_Chamber_01
- **Asset Type:** Environment
- **Priority:** Critical Path (main story location)
- **Owner:** [Artist name]
- **Target Completion:** March 15, 2025
- **Deliverable Format:** FBX + Textures

## Design Intent
The Ancient Ruin Chamber is a key story location where the player discovers the main civilization's technology. The environment should feel both alien and timeless—strange architecture suggests intelligence and advancement, but centuries of decay suggest mystery and danger. Players will spend 5-10 minutes exploring and solving puzzles here.

## Visual Reference
### Mood Board
[Concept art for ruins]
- Inspiration: Precursor technology (Halo), ancient temples, alien architecture
- Color palette: Cool grays, blue bioluminescence, weathered gold
- Lighting: Dim bioluminescent glows, dust particles in shafts of light
- Scale: Epic but not overwhelming (3-story chamber)

### Comparable Examples
- Outer Wilds: Ancient alien tech, timeless aesthetic
- No Man's Sky: Derelict alien structures
- Alien Isolation: Industrial decay with purpose

## Technical Specifications

### Geometry Budget
- **Total Triangle Count:** 250,000 (entire chamber)
- **Per-section budget:**
  - Architecture (walls/floor/ceiling): 100,000 tris
  - Decoration (pillars, statues, devices): 80,000 tris
  - Props (crates, tables, debris): 40,000 tris
  - Vegetation/rubble: 30,000 tris

### Texture Budget
- **Wall textures:** 4K (4096x4096)
- **Detailed props:** 2K (2048x2048)
- **Scattered objects:** 1K (1024x1024)
- **Total memory:** 256 MB

### Modular Design
[Break down the environment into reusable modules]
- Wall section (2m x 3m repeatable)
- Pillar (1m diameter, 4m tall)
- Floor tile (2m x 2m repeatable)
- Ceiling panel (1m x 1m repeatable)

## Lighting & Atmosphere

### Baked Lighting
- Bake static geometry lighting (walls, floor, ceiling)
- High-quality bake (4 bounces minimum)
- Lightmap resolution: 512 px per 1m² (high detail)

### Real-Time Lights
- Bioluminescent panels: Blue glow (RGB 0, 150, 255)
- Broken panel flickers: Occasional brief brightening
- Player flashlight: Warm white, casts dynamic shadows

## Approval Criteria

### Block-Out Approval
- [ ] Layout clear and navigable
- [ ] Scale feels right (epic but not overwhelming)
- [ ] Key puzzle areas visible
- [ ] Lighting scheme works (bright areas for puzzles, dark for mystery)

### Detail Approval
- [ ] Walls have convincing decay (cracks, discoloration)
- [ ] Vegetation and rubble scattered naturally
- [ ] Bioluminescent panels glow convincingly
- [ ] No obvious repeating patterns

### Performance Approval
- [ ] Within 250,000 triangle budget
- [ ] Lightmaps look clean (no splotchy baking)
- [ ] Shadows render smoothly (60 FPS sustained)
- [ ] No obvious pop-in or LOD transitions

---
```

## UI Art Specification Example

```markdown
# Asset Specification: Ability Icon Set

## Overview
- **Asset Name:** UI_Ability_Icons_Set_01
- **Asset Type:** UI Graphics
- **Priority:** High (used in inventory, HUD, skill menu)
- **Owner:** [Artist name]
- **Target Completion:** March 1, 2025
- **Deliverable Format:** PNG (24-bit + alpha)

## Design Intent
Ability icons appear throughout the UI (skill tree, HUD, inventory, character sheets). Icons must be immediately recognizable, visually distinct from each other, and readable at small sizes (24px). They should evoke the ability's effect (fire icon for Fireball, shield icon for Protect).

## Technical Specifications

### Icon Sizes
- **Gameplay HUD:** 64x64 px (main display)
- **Skill tree:** 48x48 px (small but visible)
- **Inventory:** 32x32 px (tight space)
- **Tooltip preview:** 256x256 px (large reference)

### Source & Export
- **Source format:** PSD or Illustrator
- **Export format:** PNG 24-bit with alpha channel
- **Color space:** sRGB (not linear)
- **Padding:** 2px transparent border on all sides

### Design System
- **Grid:** Aligned to 64px grid
- **Safe area:** 4px padding from edge (leave room for UI frames)
- **Outline:** 2px dark outline (improves readability at small sizes)

## Art Direction

### Visual Style
- Iconographic (bold, clear shapes)
- Hand-drawn or vector (no photorealism)
- Consistent stroke weight
- Use primary color as main element

### Color Palette
- Base color: One of 5 primary colors (red, blue, green, yellow, purple)
- Background: Dark gray (RGB 50, 50, 50) with transparency
- Outline: Black or very dark

### Icon List
| Ability | Color | Inspiration | Notes |
|---------|-------|-------------|-------|
| Fireball | Red | Flaming projectile | Clear motion/direction |
| Frostbolt | Blue | Ice crystal | Sharp, geometric shapes |
| Heal | Green | Medical/nature | Cross or plant symbol |
| Shield | Purple | Defense | Armor or barrier symbol |
| Buff | Yellow | Enhancement | Star or light symbol |

## Approval Criteria

### Concept Approval
- [ ] Each icon visually distinct (no confusion between similar abilities)
- [ ] Readable at 32px (squint test)
- [ ] Color choices clear and consistent
- [ ] Icons fit within grid/padding guidelines

### Final Approval
- [ ] All sizes exported (64x64, 48x48, 32x32, 256x256)
- [ ] Alpha channel working (transparency correct)
- [ ] Outline improves readability at small sizes
- [ ] No artifacts or anti-aliasing issues
- [ ] Matches overall UI style

---
```

## Animation Specification Example

```markdown
# Asset Specification: Combat Animations - Warrior

## Overview
- **Asset Name:** Animations_Warrior_Combat
- **Asset Type:** Animation Set
- **Priority:** Critical Path
- **Owner:** [Animator name]
- **Target Completion:** March 10, 2025
- **Deliverable Format:** FBX (exported with animations embedded)

## Animation List

### Idle Animations
| Animation | Duration | Description | Keyframes | Notes |
|-----------|----------|-------------|-----------|-------|
| Idle | 2.0 sec | Standing at rest | 60 frames | Add subtle breathing, weight shift |
| Idle_Distracted | 3.0 sec | Looking around | 90 frames | Head turns, shoulders shift |
| Idle_Impatient | 2.5 sec | Foot tapping, arm crossing | 75 frames | Shows personality, loops smoothly |

### Movement Animations
| Animation | Duration | Description | Keyframes | Notes |
|-----------|----------|-------------|-----------|-------|
| Walk_Forward | 1.5 sec | Walking at normal pace | 45 frames | 1.4 m/s movement speed |
| Walk_Backward | 1.8 sec | Walking backward | 54 frames | Slower than forward, head turns to look |
| Run_Forward | 1.0 sec | Sprinting | 30 frames | 3.5 m/s movement speed, exaggerated motion |
| Turn_Left | 0.5 sec | 90-degree turn | 15 frames | In-place rotation, no forward movement |
| Dodge_Left | 0.6 sec | Dodge roll left | 18 frames | I-frames during animation, recovers to idle |

### Combat Animations
| Animation | Duration | Description | Keyframes | Roots | Damage Frame |
|-----------|----------|-------------|-----------|-------|--------------|
| Attack_Light | 0.6 sec | Quick swing | 18 frames | Frames 8-18 | Frame 10 (connects) |
| Attack_Heavy | 1.2 sec | Slow, powerful swing | 36 frames | Frames 15-36 | Frame 22 (connects) |
| Attack_Combo_2 | 1.0 sec | Follow-up from light | 30 frames | Frames 5-25 | Frame 15 |
| Block | Hold | Shield up, hold position | 0 frames | Looping idle | N/A |
| Block_Break | 0.4 sec | Shield takes impact | 12 frames | Frames 0-12 | N/A |
| Damaged | 0.5 sec | Hit reaction | 15 frames | N/A | N/A |
| Death | 2.0 sec | Falling down | 60 frames | Frames 50-60 | N/A |

### Dialogue Animations
[Blend shapes for facial expressions, body language]
- Head turn left/right
- Blink (automatic, triggered every 3-5 seconds in idle dialogue)
- Nod (agreement)
- Shake head (disagreement)
- Laugh (happiness)
- Angry frown
- Neutral expression

## Technical Specifications

### Rigging Requirements
- **Skeleton:** Humanoid (compatible with engine rig)
- **Bone count:** 45 bones (specified in character art spec)
- **Naming:** Standard Mecanim naming (Armature|Character)
- **Root bone:** At feet level (character moves via root motion)

### Animation Frame Rate
- **Frame rate:** 30 FPS (standard for game animation)
- **Playback:** Real-time in-engine at 60 FPS (animated at 30 FPS for smoother production)

### Root Motion
[Animation moves the root bone, engine applies velocity]
- Walk/Run: Root bone translates forward
- Dodge: Root bone moves in dodge direction
- Attack: Small root motion for follow-through
- Knockback: Root driven by physics (animation ignored)

### Curves & Timing
- **Easing:** Natural easing (not linear)
- **Anticipation:** Wind-up before attacks (frames 0-5)
- **Follow-through:** Trails end of action (shield settling after block)
- **Overshoot:** Exaggeration for clarity (dodge, heavy attack)

## Approval Criteria

### Blocking Approval
- [ ] Key poses in correct positions (start, middle, end)
- [ ] Timing feels right (not too slow, not too twitchy)
- [ ] Action intent clear (what is the character doing?)

### Spline Approval
- [ ] Motion curves smooth (no pops or hesitations)
- [ ] Root motion aligned with animation
- [ ] Transitions smooth (blend into next animation)
- [ ] Overshoot appropriate (not exaggerated)

### Final Approval
- [ ] Exports without errors
- [ ] Animation names match specification
- [ ] Frame timing verified (walk = 1.5 sec, not 1.4 sec)
- [ ] Blends smoothly in-engine
- [ ] Damage frames match designer expectations (hit lands on frame 10, not frame 12)

---
```

## SFX Specification Example

```markdown
# Asset Specification: Footstep Sound Library

## Overview
- **Asset Name:** SFX_Footsteps_Library
- **Asset Type:** Sound Effects
- **Priority:** High (critical for player feedback)
- **Owner:** [Audio designer name]
- **Target Completion:** February 28, 2025
- **Deliverable Format:** WAV 48kHz 24-bit

## Sound Library Contents

### Surface Types
| Surface | Footstep Sound | Characteristics | Example |
|---------|---|---|---|
| Stone floor | Solid footsteps, slight echo | Clear, defined, resonant | Ancient ruins, temple |
| Metal grating | Clanging, ringing | Sharp, metallic, reverberant | Ship deck, facility |
| Dirt/sand | Soft shuffling, crunching | Muffled, organic, varied | Desert, cave |
| Grass | Soft rustling, spongy | Quiet, organic, natural | Outdoor areas |
| Water | Splashing, squelching | Wet, squishy, variable | River, swampy area |

### Footstep Variations
- **Light step** (sneaking, careful): Quieter, less impact
- **Normal step** (walking): Standard impact and duration
- **Heavy step** (running, impact): Louder, more resonant, impact emphasis
- **Armor clank** (warrior gear): Metal rattling and clanking added to step

### Specifications per Sound

#### Stone Footstep - Light
- **Frequency range:** 200 Hz - 4 kHz (footstep fundamentals and resonance)
- **Duration:** 0.4 seconds
- **Loudness:** -18 dB (quiet, subtle)
- **Dynamics:** Sharp attack (impact), gentle decay
- **EQ:** Boost 500 Hz (impact), reduce below 100 Hz (rumble)
- **Effects:** Light reverb (2 second room, 30% wet), minimal compression
- **Variation:** 3 samples (slight variations to prevent repetition)

#### Metal Footstep - Heavy
- **Frequency range:** 100 Hz - 8 kHz (resonant metal tones)
- **Duration:** 0.6 seconds
- **Loudness:** -10 dB (prominent, heavy)
- **Dynamics:** Sharp attack, long decay (metal ring)
- **EQ:** Boost 1-2 kHz (metal clang), reduce extreme lows
- **Effects:** Medium reverb (3 second room), 40% wet, light compression
- **Additional:** Layer with armor rattle (secondary sound) at -12 dB
- **Variation:** 4 samples (more variety due to metal variations)

## Technical Specifications

### Audio Format
- **Sample rate:** 48 kHz (broadcast standard)
- **Bit depth:** 24-bit (high quality, headroom for mixing)
- **Channels:** Mono (footsteps are point-source sounds)
- **File format:** WAV (uncompressed source)
- **Runtime format:** Vorbis OGG (compressed for game, 160 kbps)

### Level Consistency
- **Loudness target:** -16 LUFS (perceived loudness standard)
- **Peak level:** -6 dB (headroom for mixing and effects)
- **No clipping:** Verify waveform (no flat-topped peaks)

### File Naming Convention
```
SFX_Footstep_[Surface]_[Weight]_[Variation].wav

Examples:
SFX_Footstep_Stone_Light_01.wav
SFX_Footstep_Metal_Heavy_02.wav
SFX_Footstep_Dirt_Normal_03.wav
```

## Integration Notes

### Engine Implementation
- **Trigger:** Animation event at foot contact frame
- **Randomization:** Randomly select from 3-4 variations per surface
- **Volume:** Scale by walking speed (fast = louder)
- **Pitch:** Slight random pitch variation (±5%) for naturalness
- **3D spatialization:** Cone-shaped audio source, full 3D panning

### Spatial Audio
- **Attenuation:** Footsteps audible 10-15 meters away
- **Doppler effect:** Enabled (moving player/enemies)
- **Reverb:** Room reverb applied based on environment
- **Reflections:** Delay reflections for large spaces (cave, ruin)

## Approval Criteria

### Design Approval
- [ ] Each footstep sounds appropriate for surface (stone feels solid, dirt feels soft)
- [ ] Variations prevent repetition (listen to 10 steps in a row—no obvious loop)
- [ ] Weight is clear (light vs. heavy distinction obvious)
- [ ] Armor variants distinct from base footsteps

### Technical Approval
- [ ] All files 48kHz 24-bit WAV
- [ ] Naming convention followed
- [ ] No clipping (peak -6 dB max)
- [ ] Loudness consistent across all sounds (-16 LUFS ±2)
- [ ] Mono files (point-source sounds)

### Integration Approval
- [ ] Sounds trigger correctly in engine
- [ ] Randomization sounds natural
- [ ] No obvious looping patterns
- [ ] Spatial audio works correctly (panning, distance)

---
```

## Music Specification Example

```markdown
# Asset Specification: Main Theme Composition

## Overview
- **Asset Name:** Music_MainTheme
- **Asset Type:** Music (Orchestral)
- **Priority:** Critical Path
- **Owner:** [Composer name]
- **Target Completion:** March 31, 2025
- **Deliverable Format:** STEMS (individual instrument tracks) + Mix (WAV)

## Composition Brief

### Intent & Mood
[Emotional target]
"The Main Theme should evoke wonder and discovery—players should feel like they're embarking on an epic journey. Hint at mystery with dissonant undertones, but lead with a strong, memorable melody that players hum later. The theme should feel timeless, neither futuristic nor ancient, but universal."

### Orchestration
- **Instruments:** Full orchestra (strings, brass, woodwinds, percussion)
- **Tempo:** 120 BPM (moderate, not rushed)
- **Time signature:** 4/4 (standard, accessible)
- **Duration:** 2 minutes (playable in full or loopable segments)
- **Style:** Orchestral with subtle electronic undertones (future meets past)

### Leitmotif & Structure
- **Main melody:** Memorable 8-bar hook (hummable, distinctive)
- **Theme variations:**
  - Full orchestration (exploration phase)
  - Sparse strings (quiet discovery moments)
  - Dramatic brass (combat/danger moments)
  - Ethereal synth (alien technology revelation)

### Emotional Arc
- **Opening (0:00-0:20):** Mysterious, sparse (single violin, atmospheric pads)
- **Build (0:20-0:40):** Melody enters, harmony builds (strings, subtle brass)
- **Climax (0:40-1:20):** Full orchestration, powerful brass, driving rhythm
- **Resolution (1:20-2:00):** Melody returns, fades with wonder

## Technical Specifications

### Audio Format
- **Sample rate:** 48 kHz (broadcast/game standard)
- **Bit depth:** 24-bit (high quality)
- **Channels:** Stereo (left/right separation)
- **Delivery:**
  - Mix (stereo WAV, final version)
  - STEMS (individual tracks for adaptive music)

### Stem Breakdown (for interactive music engine)
| Stem | Instruments | Purpose | Note |
|------|---|---|---|
| Melody | Violins, flute | Main theme | Can be solo for soft moments |
| Harmony | Cello, violas | Support | Reinforces emotional arc |
| Bass | Contrabass, low synth | Foundation | Keeps rhythm grounded |
| Brass | Trumpet, French horn | Impact | Swells for dramatic moments |
| Percussion | Timpani, marimba | Rhythm | Drives forward momentum |
| Pads | Synth, reverb | Atmosphere | Fills space, adds wonder |

### Mixing Notes
- **Master loudness:** -16 LUFS (broadcast standard)
- **Peak level:** -6 dB (headroom)
- **Compression:** Light, transparent (preserve dynamics)
- **EQ:** Smooth, no artificial harshness
- **Effects:** Subtle reverb (concert hall ambience), no heavy effects
- **Format for delivery:** Mix as .wav + folder with individual stems

### Adaptive Music (if needed)
[Music can transition between intensities based on gameplay]
- **Intensity layers:**
  - Low intensity (exploration): Strings, sparse melody
  - Medium intensity (light combat): Add brass, increase tempo slightly
  - High intensity (boss fight): Full orchestra, driving bass, dramatic dynamics
- **Transitions:** Crossfade between intensities (smooth blending)

## Integration Notes

### In-Game Implementation
- **Loop point:** Theme loops seamlessly at 2-minute mark
- **Fade:** Music fades when transitioning to new area
- **Ducking:** Music reduces volume when dialogue plays
- **Adaptive:** Intensity adjusts based on player status (low health = more dramatic)

## Approval Criteria

### Composition Approval
- [ ] Main melody memorable and distinctive
- [ ] Emotional arc clear (mystery → wonder → power → resolution)
- [ ] Orchestration appropriate (not too busy, not too sparse)
- [ ] Tempo feels right (120 BPM works for game pacing)
- [ ] Loops seamlessly (no awkward jump at end)

### Mix Approval
- [ ] Loudness consistent (-16 LUFS ± 2)
- [ ] Peak levels safe (-6 dB max)
- [ ] Stereo imaging balanced (left/right not lopsided)
- [ ] No clipping or digital artifacts
- [ ] Reverb appropriate (not too much, not too little)

### Technical Approval
- [ ] All stems provided (melody, harmony, bass, brass, percussion, pads)
- [ ] Stems match mix (sum to final mix)
- [ ] File naming clear (Music_MainTheme_Stem_Melody.wav, etc.)
- [ ] All 48kHz 24-bit WAV
- [ ] Loop points verified (no glitch at loop)

---
```

## Voice Acting Specification Example

```markdown
# Asset Specification: Character Voice Acting - Warrior

## Overview
- **Asset Name:** VO_Warrior_Character
- **Asset Type:** Voice Acting
- **Priority:** Critical Path
- **Owner:** [Voice director name]
- **Target Completion:** April 15, 2025
- **Deliverable Format:** WAV 48kHz 24-bit, processed per line

## Character Brief

### Character Persona
- **Name:** Kael (Warrior protagonist)
- **Age:** Mid-30s, experienced
- **Accent:** Neutral American (standard)
- **Attitude:** Confident, curious, occasionally humorous
- **Voice Type:** Baritone, warm but authoritative

### Voice Reference
[Link to voice examples]
- Similar character: Geralt (The Witcher 3) — confident, world-weary
- Tone reference: Thoughtful but capable, not monotone
- Avoid: High-pitched, overly theatrical, or whiny

## Dialogue Script

### Line List

| Scene | Line | Context | Tone | Duration | Notes |
|-------|------|---------|------|----------|-------|
| Opening | "Another ruin. Another mystery." | Arrival at first location | Contemplative | 2-3 sec | Establish character |
| Exploration | "These markings... they're not random." | Discovering clues | Excited discovery | 1.5-2 sec | Building curiosity |
| Danger | "That's not good." | Spotting enemy patrol | Calm concern | 1-1.5 sec | Understated danger |
| Combat | "You picked the wrong explorer!" | Engaging enemy | Battle cry | 1-2 sec | Confident, action-ready |
| Pain | "Ugh!" | Taking damage (grunt) | Pain | 0.5-1 sec | Not overly dramatic |
| Victory | "One down. Answers to go." | Enemy defeated | Resolved | 1.5-2 sec | Forward-looking |
| Dialogue_Greeting | "Hello. Who are you?" | Meeting NPC | Neutral/friendly | 1.5-2 sec | Professional but warm |
| Dialogue_Surprised | "What?!" | Unexpected revelation | Genuine shock | 0.5-1 sec | Authentic reaction |

### Sample Emotional Variations

#### Line: "Another ruin. Another mystery."
- **Take 1:** Weary (tired of finding ruins, but determined)
- **Take 2:** Excited (enthusiastic about discovery)
- **Take 3:** Haunted (troubled by what he might find)
- Record all three, director chooses best fit

## Technical Specifications

### Audio Format
- **Sample rate:** 48 kHz (broadcast standard)
- **Bit depth:** 24-bit
- **Channels:** Mono (single voice source)
- **File format:** WAV (uncompressed source)

### Processing
- **Noise floor:** -80 dB (quiet, no hum or background)
- **Peak level:** -3 dB (headroom for EQ and compression)
- **Dynamics:** Natural (don't compress into flatness)
- **EQ:** Warm, no sibilance (don't over-brighten)

### File Naming Convention
```
VO_[Character]_[Scene]_[Line]_[Take].wav

Examples:
VO_Warrior_Opening_Ruin_Mystery_01.wav
VO_Warrior_Combat_PickedWrong_01.wav
VO_Warrior_Dialogue_Greeting_03.wav
```

### Session Deliverables
- Individual .wav files (one per line/take)
- Session notes (which takes are best?)
- Emotion guide (reference notes for each line)
- Raw recordings (unprocessed, for archive)

## Recording Specifications

### Studio Requirements
- **Acoustic treatment:** Professional voice booth
- **Microphone:** Large-diaphragm condenser (Rode, Neumann, Shure)
- **Interface:** High-quality converter (RME, Universal Audio, Apollo)
- **Monitoring:** Headphone monitoring, director communication

### Recording Session
- **Duration:** 4-6 hours (budget 2+ hours for 20-30 lines)
- **Pace:** Comfortable, with breaks (voice fatigue degrades quality)
- **Multiple takes:** 2-4 takes per line (director picks best)
- **Punch-ins:** Can re-record single words/phrases as needed

### Director Guidance
[What the voice director will communicate]
- Emotion/tone for each line
- Pacing (natural speech, not rushed)
- Emphasis (which words to stress?)
- Audience context (who is he talking to?)

## Approval Criteria

### Recording Quality Approval
- [ ] No background noise (AC hum, traffic, clicks)
- [ ] No clipping (peak level -3 dB max)
- [ ] No weird artifacts (plosives, mouth sounds)
- [ ] Consistent loudness across takes
- [ ] Natural, conversational tone

### Performance Approval
- [ ] Emotion matches context (danger = appropriate concern, not panic)
- [ ] Delivery natural (doesn't sound like actor reading lines)
- [ ] Emphasis on right words
- [ ] Pacing appropriate (not rushed, not dragging)
- [ ] Character voice consistent (sounds like same person)

### Technical Approval
- [ ] All files named correctly
- [ ] 48kHz 24-bit WAV format
- [ ] Mono (single voice channel)
- [ ] No processing artifacts
- [ ] Director comments provided (which take is preferred?)

---
```

## Best Practices

### Clear Specifications

1. **One asset per spec** — Avoid bundling multiple assets (character + weapons separate)
2. **Complete examples** — Show reference art, comparable games, mood boards
3. **Technical precision** — Exact numbers (not "small-ish")
4. **Context clarity** — Why does this asset matter? How will it be used?
5. **Realistic budgets** — Polygon counts, texture memory actually achievable

### Approval Gates

1. **Early reviews** — Catch problems at concept stage, not final polish
2. **Clear criteria** — Artists know exactly what constitutes "approved"
3. **Revision limits** — Specify how many revision rounds are included
4. **Sign-off process** — Who approves? What's the timeline?
5. **Feedback format** — Email? Screenshots? In-engine review?

### Integration Planning

1. **Dependencies documented** — What does this asset depend on? What depends on it?
2. **Related assets listed** — Character variations, weapon matchups, etc.
3. **Engine requirements clear** — Format, naming, folder structure precise
4. **Timeline realistic** — Account for approval rounds and revisions
5. **Handoff documented** — How does asset move from artist to production?

## Output Format

Asset specs are delivered as Markdown documents or detailed PDFs. Standard naming:

- **Format:** `AssetSpec_[AssetName]_v[Version].md`
- **Examples:**
  - `AssetSpec_Warrior_Character_v1.md`
  - `AssetSpec_Ruins_Chamber_v1.md`
  - `AssetSpec_Ability_Icons_v2.md`

Complete specification includes:
- Overview and design intent
- Visual references and mood boards
- Technical specifications (budgets, formats)
- Art direction and style guidance
- Approval criteria and gates
- Delivery checklist
- Timeline and milestones

All asset specs tracked in design documentation system with version history.

## References

- `templates/asset-spec-character.md` — Character art specification template
- `templates/asset-spec-environment.md` — Environment specification template
- `templates/asset-spec-animation.md` — Animation specification template
- `templates/asset-spec-audio.md` — Audio specification template
- `references/polygon-budgets.md` — Typical poly budgets by platform/asset type
- `references/texture-memory-guide.md` — Texture resolution guidelines
- `references/animation-naming-conventions.md` — Standard animation naming
- `references/audio-technical-guide.md` — Audio file format and mixing specs
- `references/art-style-guide.md` — Visual consistency guidelines
