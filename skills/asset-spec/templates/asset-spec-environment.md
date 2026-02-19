# Environment Art Asset Specification

> Fill in all fields below. Replace bracketed placeholders with actual values.
> Delete any sections that do not apply, but document why they were removed.
> Reference: `references/polygon-budgets.md`, `references/texture-memory-guide.md`,
> `references/art-style-guide.md`

---

## Overview

| Field | Value |
|-------|-------|
| **Asset Name** | [e.g., `env_ruins_chamber_01`] |
| **Zone Name** | [e.g., Ancient Ruin Interior - Main Chamber] |
| **Asset Type** | Environment |
| **Zone Type** | [Interior / Exterior / Transition / Arena] |
| **Priority** | [Critical Path / High / Medium / Low] |
| **Owner** | [Artist name] |
| **Target Completion** | [YYYY-MM-DD] |
| **Deliverable Format** | [FBX + Textures + Lightmaps] |

---

## Design Intent

### Description
[One-paragraph summary of what this environment is, its narrative purpose, and how long the player spends here.]

### Gameplay Purpose
- [Primary: e.g., Exploration zone with puzzle elements]
- [Secondary: e.g., Combat encounter space for 1-6 enemies]
- [Tertiary: e.g., Story beat -- player discovers key lore item]

### Player Flow
[Describe how the player moves through this space. Entry points, exit points, key landmarks, sight lines, and pacing.]

---

## Mood and Lighting

### Mood Description
[What emotional state should this environment evoke? Reference the art style guide mood boards.]

### Lighting Setup

| Light Source | Type | Color | Intensity | Purpose |
|-------------|------|-------|-----------|---------|
| [e.g., Primary sunlight] | [Directional] | [Warm white `#FFF5E1`] | [High] | [Key light, shadow caster] |
| [e.g., Bioluminescent panels] | [Point / Area] | [Arcane Blue `#00A8E8`] | [Low] | [Accent, atmosphere] |
| [e.g., Ambient fill] | [Ambient] | [Night Blue `#2D3A5C`] | [Low] | [Shadow fill, readability] |

### Lighting Mode
- **Baked / Real-time / Mixed:** [e.g., Mixed -- baked static geo, real-time characters]
- **Lightmap resolution:** [e.g., 512 px per 1m2]
- **Light probe density:** [e.g., 2m grid spacing]
- **Reflection probes:** [Count and placement]

### Time of Day
- [Fixed / Dynamic]
- [If fixed, which time? Reference art-style-guide.md exterior lighting table]

### Atmospheric Effects
- **Fog:** [Yes/No -- type, density, color, distance]
- **Dust particles:** [Yes/No -- density, direction, color]
- **God rays:** [Yes/No -- volumetric or screen-space]
- **Haze:** [Distance haze color and start distance]

---

## Prop List

### Hero Props (High Detail)

| Prop Name | Tri Budget | Texture Res | Interactive | Notes |
|-----------|-----------|-------------|-------------|-------|
| [e.g., Ancient Terminal] | [8,000] | [2048] | [Yes -- puzzle element] | [Emissive glow when active] |
| [e.g., Broken Statue] | [6,000] | [2048] | [No] | [Landmark, visible from entry] |

### Standard Props

| Prop Name | Tri Budget | Texture Res | Count | Notes |
|-----------|-----------|-------------|-------|-------|
| [e.g., Stone pillar] | [2,000] | [1024] | [8] | [Modular, instanced] |
| [e.g., Debris pile] | [1,500] | [1024] | [6] | [3 variations] |
| [e.g., Barrel] | [800] | [512] | [4] | [Atlased with other small props] |

### Clutter / Dressing

| Prop Name | Tri Budget | Texture Res | Count | Notes |
|-----------|-----------|-------------|-------|-------|
| [e.g., Loose rocks] | [200] | [512 atlas] | [20] | [Scatter placement] |
| [e.g., Broken pottery] | [150] | [512 atlas] | [12] | [3 variations] |

### Total Prop Budget

| Category | Tri Budget | Count | Total Tris |
|----------|-----------|-------|------------|
| Hero props | [14,000] | [2] | [14,000] |
| Standard props | [varies] | [18] | [30,000] |
| Clutter | [varies] | [32] | [8,000] |
| **Props subtotal** | | | **[52,000]** |

---

## Terrain and Architecture

### Terrain Specifications

| Parameter | Value |
|-----------|-------|
| **Terrain type** | [Heightmap / Mesh / Modular tiles] |
| **Terrain size** | [e.g., 64m x 64m] |
| **Heightmap resolution** | [e.g., 513x513] |
| **Triangle budget** | [e.g., 25,000] |
| **Splat map layers** | [e.g., 4: stone, dirt, grass, sand] |
| **Splat map resolution** | [e.g., 1024x1024] |
| **Texture tiling** | [e.g., 2048 tiling textures per layer] |

### Modular Architecture

| Module | Dimensions | Tri Budget | Tiling | Notes |
|--------|-----------|-----------|--------|-------|
| [e.g., Wall section] | [4m x 3m] | [1,500] | [Yes, X-axis] | [Snap to 1m grid] |
| [e.g., Floor tile] | [2m x 2m] | [500] | [Yes, XZ] | [4 rotation variants] |
| [e.g., Ceiling panel] | [2m x 2m] | [400] | [Yes, XZ] | [Match floor grid] |
| [e.g., Pillar] | [1m dia x 4m] | [2,000] | [No] | [Unique placement] |
| [e.g., Doorway frame] | [2m x 3m] | [1,200] | [No] | [Fits wall module gap] |
| [e.g., Staircase] | [2m x 4m x 3m] | [2,500] | [No] | [Connects floor levels] |

---

## Skybox

| Parameter | Value |
|-----------|-------|
| **Type** | [Cubemap / Panoramic / Procedural / N/A for interior] |
| **Resolution** | [e.g., 2048 per face] |
| **Dynamic elements** | [Clouds / Stars / Aurora / None] |
| **Color gradient** | [Describe horizon-to-zenith color transition] |
| **Sun/Moon disk** | [Yes/No -- size, color, position] |

---

## Weather Effects

| Parameter | Value |
|-----------|-------|
| **Active weather** | [None / Rain / Snow / Sandstorm / Fog] |
| **Particle system** | [Describe precipitation particles if applicable] |
| **Surface effects** | [Wet surfaces / Snow accumulation / Dust layer] |
| **Sound integration** | [Rain sound, wind sound -- reference audio-technical-guide.md] |
| **Gameplay impact** | [Visibility reduction / movement speed / etc.] |

---

## Ambient Audio

| Sound Layer | Description | Format | Loop | Priority |
|-------------|-------------|--------|------|----------|
| [e.g., Base ambience] | [Wind through stone corridors] | [Stereo, OGG] | [Yes] | [Medium] |
| [e.g., Water drip] | [Occasional water dripping] | [Mono, point source] | [Yes, random interval] | [Low] |
| [e.g., Distant rumble] | [Structural creaking, deep tones] | [Stereo] | [Yes] | [Low] |
| [e.g., Interactive] | [Terminal hum when active] | [Mono, point source] | [Yes] | [Medium] |

### Reverb Zone
- **Reverb type:** [e.g., Large Hall]
- **Decay time:** [e.g., 3.0 sec]
- **Wet mix:** [e.g., 35%]
- **Zone boundaries:** [Describe where reverb zone starts and ends]

---

## Optimization Targets

### Scene Budget

| Category | Triangle Budget | Notes |
|----------|----------------|-------|
| Architecture (walls/floor/ceiling) | [e.g., 100,000] | |
| Terrain | [e.g., 25,000] | |
| Props (all categories) | [e.g., 52,000] | |
| Vegetation | [e.g., 15,000] | |
| VFX meshes | [e.g., 3,000] | |
| **Total scene** | **[e.g., 195,000]** | **Budget: [250,000]** |

### Performance Targets

| Metric | Target | Platform |
|--------|--------|----------|
| **Target FPS** | [e.g., 60] | [e.g., PC High] |
| **Max draw calls** | [e.g., 800] | |
| **Max visible triangles** | [e.g., 250,000] | |
| **Lightmap memory** | [e.g., 64 MB] | |
| **Texture memory (total)** | [e.g., 200 MB] | |
| **Occlusion culling** | [Enabled -- describe occluder placement] | |

### Batching Strategy
- **Static batching:** [Which objects are static batched?]
- **GPU instancing:** [Which objects are instanced? e.g., pillars, floor tiles]
- **Texture atlases:** [Which prop groups share atlas textures?]
- **Material count target:** [e.g., < 30 unique materials in scene]

---

## Approval Criteria

### Block-out Gate
- [ ] Layout is navigable and clear (no dead ends without purpose)
- [ ] Scale feels appropriate (reference human-scale character)
- [ ] Sight lines guide the player toward objectives
- [ ] Combat spaces have adequate cover and movement room
- [ ] Entry and exit points are identifiable

### Detail Gate
- [ ] Architecture modules tile seamlessly (no visible seams)
- [ ] Props placed naturally (not floating, not clipping)
- [ ] Weathering consistent with zone age/history
- [ ] No obvious repeating patterns visible to the player
- [ ] Vegetation and debris scattered believably

### Lighting Gate
- [ ] Key light establishes mood
- [ ] Player character and threats are readable in all areas
- [ ] Interactive objects have visual emphasis (glow, contrast)
- [ ] Lightmap quality clean (no splotches, light leaks, or dark seams)
- [ ] Transitions between light zones are smooth

### Performance Gate
- [ ] Within total triangle budget
- [ ] Draw calls within target
- [ ] Frame rate hits target on specified platform
- [ ] No visible LOD pop-in during normal navigation
- [ ] Occlusion culling functioning correctly

---

## Delivery Checklist

- [ ] Scene file (engine project with all references)
- [ ] Modular architecture FBX exports
- [ ] All texture maps (source PSD + runtime exports)
- [ ] Lightmap bake (if applicable)
- [ ] Prop prefabs with LODs configured
- [ ] Ambient audio configured with zones
- [ ] Occlusion and batching verified
- [ ] Performance profile report
- [ ] Screenshots from key viewpoints
- [ ] This spec document updated with final values

---

## Timeline

| Milestone | Date | Sign-off |
|-----------|------|----------|
| Block-out approved | [YYYY-MM-DD] | [Level Design + Art Director] |
| Architecture detail pass | [YYYY-MM-DD] | [Art Director] |
| Prop placement pass | [YYYY-MM-DD] | [Art Director] |
| Lighting first pass | [YYYY-MM-DD] | [Art Director + Tech Art] |
| Final polish + optimization | [YYYY-MM-DD] | [Tech Art] |
| Engine integration verified | [YYYY-MM-DD] | [Tech Art + QA] |

---

## Dependencies

### Inputs
- [ ] Level design block-out (gameplay layout approved)
- [ ] Narrative context (what happens in this zone?)
- [ ] Modular kit (shared architecture modules)
- [ ] Prop library (existing props to reuse)
- [ ] Lighting reference (mood board approved)

### Outputs
- [ ] Navigation mesh (AI pathfinding depends on final geometry)
- [ ] Collision mesh (physics depends on final geometry)
- [ ] Spawn points (enemy/NPC placement depends on layout)
- [ ] Audio zones (ambience depends on final space)
- [ ] Cinematic cameras (cutscenes depend on final lighting)

---
