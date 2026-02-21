# Texture Memory Guide

This document provides texture resolution guidelines, memory footprint calculations,
compression format comparisons, and VRAM budgets for all target platforms. Use this
guide when specifying texture requirements in asset specs.

---

## Resolution Tiers

Standard texture resolutions follow powers of two. Each step up quadruples the number
of pixels and roughly quadruples memory consumption.

| Resolution | Pixel Count | Common Use |
|------------|------------|------------|
| **256x256** | 65,536 | Small props, UI icons, decal details |
| **512x512** | 262,144 | Medium props, distant objects, tiling textures |
| **1024x1024** (1K) | 1,048,576 | Standard props, supporting characters, small environment pieces |
| **2048x2048** (2K) | 4,194,304 | Hero weapons, main NPCs, environment hero pieces |
| **4096x4096** (4K) | 16,777,216 | Player character, boss enemies, terrain splat maps |
| **8192x8192** (8K) | 67,108,864 | Terrain mega-textures only (virtual texturing required) |

### Resolution Selection Guidelines

| Asset Type | High Tier | Medium Tier | Low Tier |
|------------|-----------|-------------|----------|
| Player Character (body) | 4096 | 2048 | 1024 |
| Player Character (face) | 2048 | 1024 | 512 |
| Main NPC | 2048 | 1024 | 512 |
| Background NPC | 1024 | 512 | 256 |
| Boss Enemy | 4096 | 2048 | 1024 |
| Standard Enemy | 2048 | 1024 | 512 |
| Hero Weapon | 2048 | 1024 | 512 |
| Large Prop | 2048 | 1024 | 512 |
| Medium Prop | 1024 | 512 | 256 |
| Small Prop | 512 | 256 | 128 |
| Environment (tiling) | 2048 | 1024 | 512 |
| Terrain Splat Map | 4096 | 2048 | 1024 |
| Skybox (per face) | 2048 | 1024 | 512 |
| UI Element | 512-2048 | 512-1024 | 256-512 |
| VFX / Particle | 512 | 256 | 128 |

---

## Memory Footprint by Format

Memory consumption depends on resolution and compression format. All values below are
for a single texture map at the specified resolution.

### Uncompressed Formats (Source / Authoring)

| Resolution | RGBA 32-bit | RGB 24-bit | Grayscale 8-bit |
|------------|-------------|------------|-----------------|
| 256x256 | 256 KB | 192 KB | 64 KB |
| 512x512 | 1 MB | 768 KB | 256 KB |
| 1024x1024 | 4 MB | 3 MB | 1 MB |
| 2048x2048 | 16 MB | 12 MB | 4 MB |
| 4096x4096 | 64 MB | 48 MB | 16 MB |

### DXT / BC Formats (PC and Console Runtime)

| Format | Bits/Pixel | Use Case | Quality |
|--------|-----------|----------|---------|
| **BC1 (DXT1)** | 4 bpp | RGB without alpha; diffuse maps | Good for opaque |
| **BC3 (DXT5)** | 8 bpp | RGBA with alpha; diffuse + transparency | Good general purpose |
| **BC4** | 4 bpp | Single channel; roughness, height maps | Excellent for grayscale |
| **BC5** | 8 bpp | Two channels; normal maps (RG) | Excellent for normals |
| **BC7** | 8 bpp | RGBA high quality; best visual fidelity | Best quality, slower encode |

| Resolution | BC1 (4 bpp) | BC3/BC5/BC7 (8 bpp) | BC4 (4 bpp) |
|------------|-------------|----------------------|-------------|
| 256x256 | 32 KB | 64 KB | 32 KB |
| 512x512 | 128 KB | 256 KB | 128 KB |
| 1024x1024 | 512 KB | 1 MB | 512 KB |
| 2048x2048 | 2 MB | 4 MB | 2 MB |
| 4096x4096 | 8 MB | 16 MB | 8 MB |

### ASTC Formats (Mobile Runtime)

ASTC is the preferred mobile compression format. Block size determines quality vs. size.

| Block Size | Bits/Pixel | Quality | Use Case |
|------------|-----------|---------|----------|
| **4x4** | 8.0 bpp | Highest | Hero characters, close-up textures |
| **5x5** | 5.12 bpp | High | Main NPCs, important props |
| **6x6** | 3.56 bpp | Medium | Standard assets, environment tiles |
| **8x8** | 2.0 bpp | Low | Background elements, distant objects |
| **10x10** | 1.28 bpp | Lowest | Skybox, terrain far LODs |

| Resolution | ASTC 4x4 (8 bpp) | ASTC 6x6 (3.56 bpp) | ASTC 8x8 (2 bpp) |
|------------|-------------------|----------------------|-------------------|
| 256x256 | 64 KB | 28 KB | 16 KB |
| 512x512 | 256 KB | 114 KB | 64 KB |
| 1024x1024 | 1 MB | 455 KB | 256 KB |
| 2048x2048 | 4 MB | 1.78 MB | 1 MB |
| 4096x4096 | 16 MB | 7.12 MB | 4 MB |

---

## Mipmap Memory Cost

Mipmaps add approximately 33% overhead to base texture memory. Each mip level is
half the resolution of the previous level, down to 1x1.

| Base Resolution | Base Memory (BC7) | With Mipmaps (BC7) | Mip Overhead |
|-----------------|-------------------|---------------------|-------------|
| 256x256 | 64 KB | 85 KB | +21 KB (33%) |
| 512x512 | 256 KB | 341 KB | +85 KB (33%) |
| 1024x1024 | 1 MB | 1.33 MB | +0.33 MB (33%) |
| 2048x2048 | 4 MB | 5.33 MB | +1.33 MB (33%) |
| 4096x4096 | 16 MB | 21.33 MB | +5.33 MB (33%) |

### Mipmap Guidelines

- **Always generate mipmaps** for 3D scene textures (prevents aliasing and shimmer)
- **Skip mipmaps** for UI textures displayed at fixed pixel sizes
- **Skip mipmaps** for textures used only in post-processing
- **Mip bias:** Apply a slight negative bias (-0.5) for hero assets to keep them sharp
- **Streaming mips:** On High/Medium tier, stream top 2 mip levels on demand to save VRAM

---

## Texture Atlas Strategies

Atlasing combines multiple textures into one larger texture to reduce draw calls
and improve batching. Use atlases for assets that share materials.

### When to Atlas

| Scenario | Atlas? | Reason |
|----------|--------|--------|
| Multiple props in same room | Yes | Reduces draw calls, same material |
| Character body + accessories | Maybe | Only if UVs can share space cleanly |
| Tiling environment textures | No | Tiling requires full UV range [0,1] |
| UI icon sets | Yes | All icons in one sheet, one draw call |
| VFX sprite sheets | Yes | Animation frames in grid layout |
| Unique hero assets | No | Need full UV space for quality |

### Atlas Size Guidelines

| Atlas Resolution | Max Items | Minimum Item Size | Use Case |
|-----------------|-----------|-------------------|----------|
| 1024x1024 | 16-64 | 128x128 each | Small props, clutter |
| 2048x2048 | 16-64 | 256x256 each | Medium props, furniture |
| 4096x4096 | 16-64 | 512x512 each | Large prop sets, modular env |

### Atlas Best Practices

1. **Padding:** Add 2-4 pixel border between atlas entries to prevent bleed at mip levels
2. **Power of two:** Keep atlas dimensions as powers of two
3. **Channel packing:** Pack grayscale maps into RGBA channels (R=metallic, G=roughness, B=AO, A=height)
4. **Consistent texel density:** All items in an atlas should have similar pixels-per-meter
5. **Group by usage:** Atlas items that appear together in the same scene

---

## VRAM Budgets by Platform

Total VRAM available and recommended texture memory budgets. The texture budget is a
subset of total VRAM (the rest is used by framebuffers, shaders, meshes, render targets).

| Platform | Total VRAM | Texture Budget | Notes |
|----------|-----------|----------------|-------|
| **PC High (RTX 3060+)** | 8-12 GB | 3-5 GB | Texture streaming available |
| **PC Medium (GTX 1060)** | 4-6 GB | 1.5-2.5 GB | Must manage aggressively |
| **PS5 / Xbox Series X** | 16 GB unified | 4-6 GB (textures) | Shared with system RAM |
| **PS4 / Xbox One** | 5-8 GB unified | 1.5-2.5 GB | Very tight budget |
| **Nintendo Switch** | 4 GB unified | 0.5-1 GB | Aggressive compression required |
| **Mobile (High End)** | 4-6 GB unified | 0.5-1.5 GB | ASTC compression mandatory |
| **Mobile (Low End)** | 2-3 GB unified | 256-512 MB | Minimum viable quality |

### Per-Scene Texture Budget Breakdown

Example scene budget for Medium tier (2 GB total texture budget):

| Category | Budget | Notes |
|----------|--------|-------|
| Terrain / Landscape | 400 MB | Tiling textures + splat maps |
| Environment Props | 300 MB | Modular pieces, atlased |
| Characters (all on screen) | 200 MB | Player + NPCs + enemies |
| Weapons / Equipment | 100 MB | Held items, visible gear |
| VFX / Particles | 50 MB | Sprite sheets, noise textures |
| UI / HUD | 50 MB | Icons, frames, fonts |
| Skybox / Sky | 50 MB | Cubemap or panoramic |
| Lightmaps | 200 MB | Baked lighting data |
| Shadowmaps / RTs | 200 MB | Runtime render targets |
| **Headroom (reserve)** | 450 MB | Streaming buffer, spikes |
| **Total** | **2,000 MB** | |

---

## Compression Quality Tradeoffs

### Format Recommendations by Map Type

| Texture Map | PC/Console Format | Mobile Format | Channel Usage |
|-------------|-------------------|---------------|---------------|
| **Albedo (Diffuse)** | BC7 (best) or BC1 (no alpha) | ASTC 6x6 | RGB color + optional A alpha |
| **Normal Map** | BC5 (RG) | ASTC 4x4 | RG = tangent-space XY; reconstruct Z |
| **Roughness** | BC4 (single channel) | ASTC 8x8 | R channel only |
| **Metallic** | BC4 (single channel) | ASTC 8x8 | R channel only |
| **Ambient Occlusion** | BC4 (single channel) | ASTC 8x8 | R channel only |
| **Emissive** | BC7 or BC1 | ASTC 6x6 | RGB color |
| **Height / Displacement** | BC4 (single channel) | ASTC 8x8 | R channel only |
| **Opacity / Alpha Mask** | BC4 or packed in diffuse A | ASTC 6x6 | Single channel or alpha |

### Channel Packing Strategy

Reduce texture count by packing grayscale maps into a single RGBA texture:

```
ORM Texture (common PBR packing):
  R = Ambient Occlusion
  G = Roughness
  B = Metallic
  A = Height (optional)

Format: BC7 (8 bpp) or BC3 (8 bpp)
```

This converts 3-4 separate textures into 1, saving significant VRAM and draw calls.

### Quality Comparison

| Scenario | BC1 | BC3 | BC7 | Visual Impact |
|----------|-----|-----|-----|---------------|
| Smooth color gradients | Banding visible | Minor banding | Smooth | Use BC7 for skin, sky |
| Hard edges / text | Artifacts at edges | Minor artifacts | Clean | Use BC7 for UI, text |
| Noisy / organic surfaces | Acceptable | Good | Excellent | BC1 acceptable for dirt, bark |
| Normal maps | Not suitable | Acceptable | Good | Use BC5 instead |
| Alpha cutout (leaves) | DXT1A (1-bit) | Smooth alpha | Smooth | BC3 minimum for foliage |

---

## Texture Streaming

For High and Medium tiers, texture streaming reduces peak VRAM usage by loading only
the mip levels needed for the current view.

### Streaming Configuration

| Setting | Value | Notes |
|---------|-------|-------|
| Streaming pool size | 1-2 GB | Dedicated budget for streamed textures |
| Min resident mips | 2-3 | Always keep lowest mips in memory |
| Load priority radius | 20m | Full resolution within this distance |
| Fade-in time | 0.3 sec | Blend from low to high mip over time |
| Max pending loads | 32 | Concurrent texture load requests |

### Streaming Priority

1. **Always loaded:** Player character, HUD, equipped weapons, skybox
2. **High priority:** Current zone terrain, nearby NPCs, active enemies
3. **Medium priority:** Props within 20m, distant terrain, far buildings
4. **Low priority:** Background decoration, ultra-distant objects

---

## Texel Density Standards

Texel density (pixels per meter) should be consistent within a scene to avoid
visual mismatches where some surfaces look sharp and others look blurry.

| Quality Level | Texel Density | Example |
|---------------|---------------|---------|
| **Hero** | 1024 px/m | Player character face, hero weapon blade |
| **High** | 512 px/m | Main NPC, interactive props |
| **Standard** | 256 px/m | Environment surfaces, standard props |
| **Background** | 128 px/m | Distant surfaces, ceilings |
| **Minimal** | 64 px/m | Skybox, extreme distance |

### Calculating Texel Density

```
Texel Density = Texture Resolution / Object UV Coverage in Meters

Example: 2048x2048 texture on a 2m x 2m wall section
  = 2048 / 2 = 1024 px/m (Hero density)

Example: 1024x1024 texture on a 4m x 4m floor tile
  = 1024 / 4 = 256 px/m (Standard density)
```

---

## Quick Reference Card

```
UNCOMPRESSED:   1K = 4 MB    |  2K = 16 MB   |  4K = 64 MB   (RGBA 32-bit)
BC1 (DXT1):     1K = 512 KB  |  2K = 2 MB    |  4K = 8 MB    (RGB, no alpha)
BC7:            1K = 1 MB    |  2K = 4 MB    |  4K = 16 MB   (RGBA, best quality)
ASTC 6x6:      1K = 455 KB  |  2K = 1.78 MB |  4K = 7.12 MB (Mobile standard)
+ MIPMAPS:      Add ~33% to all values above
```

---

*Last updated for production pipeline. Budgets subject to adjustment
after VRAM profiling during alpha milestone.*
