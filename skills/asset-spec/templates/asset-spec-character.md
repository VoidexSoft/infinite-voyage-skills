# Character Art Asset Specification

> Fill in all fields below. Replace bracketed placeholders with actual values.
> Delete any sections that do not apply, but document why they were removed.
> Reference: `references/polygon-budgets.md`, `references/texture-memory-guide.md`,
> `references/art-style-guide.md`

---

## Overview

| Field | Value |
|-------|-------|
| **Asset Name** | [e.g., `char_warrior_main`] |
| **Character Name** | [e.g., Kael the Warrior] |
| **Asset Type** | Character |
| **Role** | [Player / Main NPC / Supporting NPC / Enemy / Boss / Companion] |
| **Priority** | [Critical Path / High / Medium / Low] |
| **Owner** | [Artist name] |
| **Target Completion** | [YYYY-MM-DD] |
| **Deliverable Format** | [FBX 2020 + Textures] |

---

## Character Identity

### Description
[One-paragraph summary of who this character is, their personality, and their narrative role in Infinite Voyage.]

### Visual Archetype
[What should the player feel when they see this character? What genre archetypes does this character reference?]

### Key Distinguishing Features
- [Feature 1: e.g., Glowing rune scar across left cheek]
- [Feature 2: e.g., Oversized gauntlet on right hand]
- [Feature 3: e.g., Tattered cloak with embroidered sigil]

---

## Visual Reference

### Mood Board
[Link to mood board or describe reference images]
- Art style reference: [Description or link]
- Color palette samples: [Description or link]
- Comparable character from other media: [e.g., Geralt from The Witcher 3 -- confident, weathered]

### Style Guide Alignment
- **Rendering style:** [Stylized realism per art-style-guide.md]
- **Weathering level:** [New / Used / Worn / Aged -- per art-style-guide.md]
- **Proportion rules:** [Head ratio, shoulder width, hand size -- per art-style-guide.md]

---

## Polygon Budget

| LOD Level | Triangle Count | Use Distance | Notes |
|-----------|---------------|--------------|-------|
| **LOD0** | [e.g., 50,000] | 0-10m | Full detail; dialogue, close combat |
| **LOD1** | [e.g., 25,000] | 10-25m | Standard gameplay |
| **LOD2** | [e.g., 12,500] | 25-50m | Background / distance |
| **LOD3** | [e.g., 5,000] | 50m+ | Far distance (if needed) |

- **Platform tier:** [High / Medium / Low -- reference polygon-budgets.md]
- **Max simultaneous on screen:** [e.g., 1 for player; 6 for this enemy type]
- **Bone count:** [e.g., 45 for humanoid rig]
- **Bone influences per vertex:** [4 max; 2 for mobile]

---

## Texture Requirements

| Texture Map | Resolution | Format (Runtime) | Channel Usage |
|-------------|-----------|------------------|---------------|
| **Albedo (Base Color)** | [e.g., 4096x4096] | [BC7 / ASTC 6x6] | RGB color |
| **Normal Map** | [e.g., 4096x4096] | [BC5 / ASTC 4x4] | RG tangent-space |
| **ORM (packed)** | [e.g., 4096x4096] | [BC7 / ASTC 6x6] | R=AO, G=Roughness, B=Metallic |
| **Emissive** | [e.g., 2048x2048] | [BC1 / ASTC 8x8] | RGB glow areas (if needed) |

- **Total estimated VRAM:** [e.g., 48 MB with mipmaps]
- **Texel density target:** [e.g., 512-1024 px/m on body; 1024 px/m on face]
- **Texture atlas:** [Yes/No -- atlas with equipment variants?]

---

## Rig Requirements

| Parameter | Value |
|-----------|-------|
| **Rig type** | [Humanoid / Quadruped / Custom] |
| **Skeleton** | [Engine standard humanoid / Custom skeleton] |
| **Total bone count** | [e.g., 45] |
| **Facial bones** | [e.g., 12 for expression; or blend shapes] |
| **Blend shapes** | [Count and list: e.g., 8 facial expressions] |
| **IK targets** | [Feet, hands, head look-at] |
| **Physics bones** | [e.g., Cape: 4 chain bones; Hair: 3 chain bones] |
| **Naming convention** | [Engine standard -- e.g., Mecanim naming] |

---

## Animation Requirements

List all animations required for this character. Reference `references/animation-naming-conventions.md`.

### Locomotion

| Clip Name | Frames | Loop | Root Motion | Priority |
|-----------|--------|------|-------------|----------|
| [e.g., `char_[name]_idle`] | [90] | [Yes] | [No] | [Critical] |
| [e.g., `char_[name]_walk_fwd`] | [40] | [Yes] | [Yes] | [Critical] |
| [e.g., `char_[name]_run_fwd`] | [24] | [Yes] | [Yes] | [Critical] |

### Combat

| Clip Name | Frames | Loop | Root Motion | Damage Frame | Priority |
|-----------|--------|------|-------------|--------------|----------|
| [e.g., `char_[name]_attack_light_01`] | [20] | [No] | [Yes] | [Frame 10] | [Critical] |

### Abilities

| Clip Name | Frames | Loop | Root Motion | Priority |
|-----------|--------|------|-------------|----------|
| [e.g., `char_[name]_cast_start`] | [15] | [No] | [No] | [High] |

### Interaction / Emotes

| Clip Name | Frames | Loop | Priority |
|-----------|--------|------|----------|
| [e.g., `char_[name]_emote_wave`] | [50] | [No] | [Low] |

---

## VFX Requirements

| Effect | Trigger | Attachment Point | Color | Notes |
|--------|---------|-----------------|-------|-------|
| [e.g., Weapon trail] | [Attack animations] | [Weapon bone] | [Per art style guide] | [Additive blending] |
| [e.g., Footstep dust] | [OnFootstep events] | [Foot bones] | [Warm Stone tint] | [Scale with terrain] |
| [e.g., Ability cast glow] | [Cast animations] | [Hands] | [Arcane Blue] | [Emissive + particles] |

---

## Audio Requirements

| Sound Type | Trigger | Variations | Notes |
|------------|---------|------------|-------|
| [Footsteps] | [Animation events] | [4 per surface type] | [Reference audio-technical-guide.md] |
| [Attack swoosh] | [Attack animations] | [3 light, 3 heavy] | [Mono, 48kHz/24-bit] |
| [Hit reaction grunt] | [Hit animations] | [4 variations] | [Short, < 1 sec] |
| [Death sound] | [Death animation] | [2 variations] | [Include cloth/armor foley] |
| [Voice barks] | [Combat triggers] | [6-10 lines] | [See VO spec if applicable] |

---

## Reference Images

### Front View
[Placeholder for concept art -- front orthographic view]

### Side View
[Placeholder for concept art -- side orthographic view]

### Back View
[Placeholder for concept art -- back orthographic view]

### Detail Callouts
[Close-up references for face, hands, distinctive equipment, material details]

### Color Key
- **Primary color:** [Swatch + hex] -- Used for [armor / skin / etc.]
- **Secondary color:** [Swatch + hex] -- Used for [trim / cloth / etc.]
- **Accent color:** [Swatch + hex] -- Used for [glowing elements / highlights / etc.]

---

## Approval Criteria

### Concept Gate
- [ ] Silhouette reads clearly at gameplay distance
- [ ] Color palette aligns with art style guide
- [ ] Proportions match character design brief
- [ ] Distinguishing features are visible and unique
- [ ] Mood matches character identity

### Model Gate
- [ ] Triangle count within LOD0 budget
- [ ] Topology is clean (quads preferred, no n-gons)
- [ ] UVs laid out with target texel density
- [ ] Silhouette holds at LOD1 distance
- [ ] Rig deforms cleanly in key poses

### Texture Gate
- [ ] Albedo colors match approved palette (no baked lighting)
- [ ] Normal map provides convincing surface detail
- [ ] Material values within PBR ranges (per art-style-guide.md)
- [ ] Emissive areas glow correctly in-engine
- [ ] No visible seams, stretching, or tiling artifacts

### Integration Gate
- [ ] Exports to target format without errors
- [ ] All LODs transition smoothly
- [ ] Animations play correctly on rig
- [ ] VFX attach and trigger as specified
- [ ] Performance within polygon and texture budgets
- [ ] Memory footprint verified

---

## Delivery Checklist

- [ ] Source files (Maya/Blender project with layers intact)
- [ ] Exported FBX per LOD level
- [ ] All texture maps (source PSD + runtime-ready exports)
- [ ] Rig documentation (bone map, naming reference)
- [ ] Animation clips (separate FBX or embedded)
- [ ] Screenshots / turntable render of final asset
- [ ] Performance verification (triangle count, VRAM usage)
- [ ] This spec document updated with final values

---

## Timeline

| Milestone | Date | Sign-off |
|-----------|------|----------|
| Concept approved | [YYYY-MM-DD] | [Art Director] |
| High-poly model approved | [YYYY-MM-DD] | [Art Director] |
| Textures WIP review | [YYYY-MM-DD] | [Art Director] |
| Rig + animation first pass | [YYYY-MM-DD] | [Anim Lead] |
| Final asset delivery | [YYYY-MM-DD] | [Art Director + Tech Art] |
| Engine integration verified | [YYYY-MM-DD] | [Tech Art] |

---

## Dependencies

### Inputs (this asset needs)
- [ ] Character design document (narrative, personality, backstory)
- [ ] Approved concept art (front/side/back)
- [ ] Engine skeleton / rig template
- [ ] Animation state machine structure

### Outputs (other assets need this)
- [ ] Animation system (needs rigged mesh)
- [ ] UI system (needs character portrait icon)
- [ ] VFX system (needs bone attachment points)
- [ ] Audio system (needs animation event markers)

### Related Assets
- [Equipment variations: list armor/weapon sets that must fit this character]
- [Companion/mount: if this character rides or pairs with another asset]
- [Portrait icon: UI thumbnail derived from this character model]

---
