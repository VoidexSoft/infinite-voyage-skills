# Polygon Budget Guide

This document defines triangle/polygon budgets for all asset types across target platforms.
Use these budgets as hard limits when writing asset specifications. All counts are in
**triangles** (not quads or polygons) unless otherwise noted.

---

## Platform Tiers

This guide targets three platform tiers. Each tier has different performance
characteristics and memory constraints that directly affect polygon budgets.

| Tier | Platforms | GPU Class | Target FPS | Max On-Screen Tris |
|------|-----------|-----------|------------|---------------------|
| **High** | PC (dedicated GPU), Current-gen Console (PS5/XSX) | RTX 3060+ / RDNA 2 | 60 FPS | 8-12 million |
| **Medium** | PC (integrated GPU), Last-gen Console (PS4/XB1) | GTX 1060 / GCN 4 | 30 FPS | 3-5 million |
| **Low** | Mobile (iOS/Android), Switch | Adreno 640+ / Apple A14+ | 30 FPS | 500k-1.5 million |

---

## Per-Asset Polygon Budgets

### Characters

| Asset Category | High Tier | Medium Tier | Low Tier | Notes |
|----------------|-----------|-------------|----------|-------|
| **Hero Character (Player)** | 50,000-80,000 | 25,000-40,000 | 8,000-15,000 | Always on screen; highest quality |
| **Main NPC (Quest Givers)** | 20,000-40,000 | 12,000-20,000 | 5,000-10,000 | Visible in dialogue close-ups |
| **Supporting NPC** | 10,000-20,000 | 5,000-10,000 | 3,000-5,000 | Mid-range encounters |
| **Background NPC / Crowd** | 5,000-15,000 | 3,000-8,000 | 1,000-3,000 | Seen at distance, many on screen |
| **Enemy (Boss)** | 40,000-70,000 | 20,000-35,000 | 8,000-15,000 | Focal point of combat encounter |
| **Enemy (Standard)** | 10,000-25,000 | 5,000-12,000 | 2,000-5,000 | Multiple on screen simultaneously |
| **Enemy (Fodder / Swarm)** | 3,000-8,000 | 1,500-4,000 | 500-1,500 | 10+ on screen at once |
| **Mount / Companion** | 15,000-30,000 | 8,000-15,000 | 3,000-8,000 | Paired with player character |

### Props and Items

| Asset Category | High Tier | Medium Tier | Low Tier | Notes |
|----------------|-----------|-------------|----------|-------|
| **Hero Weapon (Equipped)** | 5,000-15,000 | 3,000-8,000 | 1,000-3,000 | Visible in first/third person |
| **Held Item / Tool** | 2,000-8,000 | 1,000-4,000 | 500-2,000 | Close to camera |
| **Large Interactive Prop** | 3,000-10,000 | 1,500-5,000 | 500-2,500 | Chests, levers, doors |
| **Medium Prop (Furniture)** | 1,000-5,000 | 500-2,500 | 200-1,000 | Tables, chairs, barrels |
| **Small Prop (Clutter)** | 200-2,000 | 100-1,000 | 50-500 | Bottles, books, debris |
| **Pickup / Collectible** | 500-2,000 | 300-1,000 | 100-500 | Orbs, coins, drops |
| **Vegetation (Tree)** | 3,000-8,000 | 1,500-4,000 | 500-2,000 | Leaf cards + trunk geo |
| **Vegetation (Bush/Grass)** | 500-2,000 | 200-1,000 | 50-500 | Billboard or low-poly cards |

### Environments

| Asset Category | High Tier | Medium Tier | Low Tier | Notes |
|----------------|-----------|-------------|----------|-------|
| **Full Scene (Total Budget)** | 300,000-500,000 | 150,000-250,000 | 50,000-100,000 | Everything visible at once |
| **Modular Wall Section** | 500-2,000 | 300-1,000 | 100-500 | Tileable, per 2m section |
| **Floor Tile** | 200-1,000 | 100-500 | 50-200 | Per 2m x 2m tile |
| **Architectural Piece (Pillar)** | 1,000-4,000 | 500-2,000 | 200-1,000 | Decorative columns, arches |
| **Building Exterior** | 10,000-40,000 | 5,000-20,000 | 2,000-8,000 | Single building facade |
| **Terrain Chunk (64m x 64m)** | 20,000-50,000 | 10,000-25,000 | 5,000-12,000 | Heightmap-based terrain |
| **Skybox / Sky Dome** | 100-500 | 100-500 | 100-500 | Minimal geo, texture-driven |

### VFX and Particles

| Asset Category | High Tier | Medium Tier | Low Tier | Notes |
|----------------|-----------|-------------|----------|-------|
| **Particle Mesh (Single)** | 100-500 | 50-200 | 20-100 | Per particle; multiplied by count |
| **VFX Mesh (Spell Impact)** | 500-2,000 | 200-1,000 | 100-500 | Flash, explosion shape |
| **Decal Mesh** | 4-12 | 4-12 | 4-12 | Flat projection quad |

---

## Level of Detail (LOD) Requirements

Every asset that appears at varying distances must include LOD variants. LOD transitions
should be invisible to the player during normal gameplay.

### LOD Chain Standards

| LOD Level | Triangle Ratio | Transition Distance | Use Case |
|-----------|---------------|---------------------|----------|
| **LOD0** | 100% (full budget) | 0-10m | Close-up, dialogue, inspection |
| **LOD1** | 50% of LOD0 | 10-25m | Standard gameplay distance |
| **LOD2** | 25% of LOD0 | 25-50m | Background, mid-distance |
| **LOD3** | 10% of LOD0 | 50-100m | Far distance, silhouette only |
| **Billboard** | 2-4 tris | 100m+ | Impostor sprite replacement |

### LOD Requirements by Asset Type

| Asset Type | Required LODs | Billboard? | Notes |
|------------|--------------|------------|-------|
| Hero Character | LOD0, LOD1 | No | Always close; 2 LODs sufficient |
| Main NPC | LOD0, LOD1, LOD2 | No | May appear at distance in hubs |
| Background NPC | LOD0, LOD1, LOD2, LOD3 | Optional | Crowd rendering support |
| Boss Enemy | LOD0, LOD1 | No | Combat arena; controlled distance |
| Standard Enemy | LOD0, LOD1, LOD2 | No | Spawns at various distances |
| Large Prop | LOD0, LOD1, LOD2 | No | May be far from player |
| Small Prop | LOD0, LOD1 | No | Culled at distance instead |
| Tree / Vegetation | LOD0, LOD1, LOD2 | Yes | Billboard at extreme distance |
| Building | LOD0, LOD1, LOD2, LOD3 | Optional | Visible across open world |

### LOD Transition Settings

- **Transition type:** Cross-fade (dithered alpha blend over 0.5 seconds)
- **Hysteresis:** 2m buffer to prevent LOD flickering at boundary
- **Screen-size threshold:** Prefer screen-percentage LOD switching over fixed distance
  - LOD0 -> LOD1 at < 30% screen height
  - LOD1 -> LOD2 at < 15% screen height
  - LOD2 -> LOD3 at < 5% screen height

---

## Draw Call Budgets

Draw calls are a critical CPU bottleneck. These budgets apply to the total visible scene.

| Platform Tier | Max Draw Calls Per Frame | Target Draw Calls | Notes |
|---------------|--------------------------|-------------------|-------|
| **High** | 4,000-6,000 | < 3,000 | Instancing and batching enabled |
| **Medium** | 2,000-3,000 | < 1,500 | Aggressive batching required |
| **Low** | 500-1,000 | < 500 | Static/dynamic batching mandatory |

### Draw Call Reduction Strategies

1. **Static batching** -- Combine non-moving objects sharing the same material
2. **GPU instancing** -- Render many copies of the same mesh in one call
3. **Texture atlasing** -- Merge multiple textures so objects share one material
4. **LOD culling** -- Remove objects entirely below a screen-size threshold
5. **Occlusion culling** -- Skip objects hidden behind walls or terrain
6. **Material merging** -- Minimize unique material count per scene (target < 50 unique)

---

## Optimization Targets

### Per-Frame Budgets (Rendering)

| Metric | High Tier | Medium Tier | Low Tier |
|--------|-----------|-------------|----------|
| Total visible triangles | 8M | 4M | 1M |
| Draw calls | 3,000 | 1,500 | 500 |
| Shader passes | 2 (forward+) | 1-2 | 1 (forward) |
| Shadow-casting lights | 4 | 2 | 1 |
| Real-time reflections | Yes (SSR) | Limited | No |
| Post-processing passes | 5-8 | 3-5 | 1-2 |

### Vertex Processing Guidelines

- **Bone influences per vertex:** Max 4 (all tiers); use 2 for mobile fodder enemies
- **Blend shapes per mesh:** Max 8 active simultaneously
- **Vertex attributes:** Position + Normal + Tangent + UV0 + UV1 (lightmap) + Color
- **Skinned mesh count on screen:** High 20, Medium 10, Low 5

---

## Budgeting Workflow

When writing an asset specification, follow this process:

1. **Identify the asset category** from the tables above
2. **Select the primary platform tier** (or specify budgets for all tiers)
3. **Determine how many will be on screen** at once -- divide scene budget accordingly
4. **Assign LOD requirements** based on expected viewing distances
5. **Validate against draw call budget** -- one unique material = one draw call per object
6. **Document the budget** in the asset spec with exact triangle counts per LOD

### Example Budget Calculation

**Scenario:** Combat encounter with 1 player + 1 boss + 6 standard enemies + environment

| Element | Count | Tris Each (LOD0) | Total Tris |
|---------|-------|-------------------|------------|
| Player Character | 1 | 50,000 | 50,000 |
| Boss Enemy | 1 | 60,000 | 60,000 |
| Standard Enemy | 6 | 15,000 | 90,000 |
| Environment | 1 | 200,000 | 200,000 |
| Props / Debris | ~20 | 1,000 avg | 20,000 |
| VFX Meshes | ~10 | 500 avg | 5,000 |
| **Total** | | | **425,000** |

This fits comfortably within the High tier budget (8M) and Medium tier (4M). For Low
tier, apply LOD reductions and reduce enemy count or use LOD1/LOD2 for distant enemies.

---

## Common Mistakes

- **Over-budgeting hero characters** -- A 120k character looks great in a viewer but
  destroys performance alongside a full scene with enemies and VFX
- **Ignoring LODs** -- A 30k NPC at 50 meters is wasting 29k triangles nobody can see
- **Too many unique materials** -- 200 unique materials = 200 draw calls minimum,
  even if triangle counts are low
- **Micro-detail in geometry** -- Rivets, stitching, and engravings belong in normal
  maps, not in triangle budgets
- **Quad-only topology obsession** -- Game meshes are triangulated on export; optimize
  for triangle count, not quad purity

---

## Quick Reference Card

```
HERO CHARACTER:    30k-80k (High)  |  15k-40k (Med)  |  8k-15k (Low)
MAIN NPC:          20k-40k (High)  |  12k-20k (Med)  |  5k-10k (Low)
STANDARD ENEMY:    10k-25k (High)  |   5k-12k (Med)  |  2k-5k  (Low)
BOSS ENEMY:        40k-70k (High)  |  20k-35k (Med)  |  8k-15k (Low)
HERO WEAPON:        5k-15k (High)  |   3k-8k  (Med)  |  1k-3k  (Low)
SMALL PROP:        200-2k  (High)  |  100-1k  (Med)  |  50-500 (Low)
FULL SCENE:       300k-500k(High)  | 150k-250k(Med)  | 50k-100k(Low)
```

---

*Last updated for production pipeline. Budgets subject to revision
based on profiling results during vertical slice and alpha milestones.*
