# Infinite Voyage — Target Platform Constraints

## Device Specifications

| Spec | PC High | PC Medium | PC Low | PS5 / Xbox Series X | Switch 2 | Steam Deck |
|------|---------|-----------|--------|---------------------|----------|------------|
| GPU | RTX 4070+ | RTX 3060 | GTX 1660 | Custom RDNA 2 | Custom Ampere | Custom RDNA 2 (15W) |
| VRAM | 12 GB | 8 GB | 6 GB | 16 GB (shared) | 8 GB (shared) | 8 GB (shared) |
| RAM | 32 GB | 16 GB | 16 GB | 16 GB | 12 GB | 16 GB |
| Target Resolution | 4K / 1440p | 1440p / 1080p | 1080p | 4K (dynamic) | 1080p docked / 720p handheld | 1280x800 |
| Target FPS | 60 / uncapped | 60 | 30-60 | 60 (performance) / 30 (quality) | 30 docked / 30 handheld | 30-40 |
| Storage | NVMe SSD | SSD | HDD supported | SSD | Internal + microSD | NVMe SSD |

## Per-Asset Polygon Budgets

| Asset Category | PC High | PC Medium | PC Low / Steam Deck | Console (Quality) | Switch 2 |
|---------------|---------|-----------|---------------------|-------------------|----------|
| Player Character | 80K tris | 50K tris | 25K tris | 60K tris | 18K tris |
| Major NPC | 60K tris | 35K tris | 18K tris | 45K tris | 12K tris |
| Standard Enemy | 40K tris | 25K tris | 12K tris | 30K tris | 8K tris |
| Elite Enemy | 55K tris | 35K tris | 16K tris | 40K tris | 10K tris |
| Prop (hero) | 15K tris | 10K tris | 5K tris | 12K tris | 3K tris |
| Prop (generic) | 5K tris | 3K tris | 1.5K tris | 4K tris | 1K tris |
| Environment module | 20K tris | 12K tris | 6K tris | 15K tris | 4K tris |

## Texture Budgets

| Asset Category | PC High | PC Medium / Console | PC Low / Deck | Switch 2 |
|---------------|---------|---------------------|---------------|----------|
| Player Character | 4K (4096x4096) | 2K (2048x2048) | 1K (1024x1024) | 512x512 |
| Major NPC | 4K | 2K | 1K | 512x512 |
| Standard Enemy | 2K | 1K | 512x512 | 256x256 |
| Environment Tileset | 4K atlas | 2K atlas | 1K atlas | 512x512 atlas |
| UI Elements | Native res | Native res | Native res | 75% scale |
| Skybox / Panorama | 8K HDR | 4K HDR | 2K HDR | 1K HDR |

## LOD Requirements

All characters and hero props MUST ship with at minimum:

| LOD Level | Distance | Poly Reduction | Texture | Notes |
|-----------|----------|----------------|---------|-------|
| LOD0 | 0 - 10m | Full budget | Full res | Main gameplay view |
| LOD1 | 10 - 25m | 50% of LOD0 | Half res | Mid-distance |
| LOD2 | 25 - 50m | 25% of LOD0 | Quarter res | Background |
| LOD3 | 50m+ | 12% of LOD0 | Eighth res | Distant, optional impostor |

Switch 2: Only LOD0 and LOD1 required. LOD2 replaced by impostor billboard.

## Scene Budgets (Draw Call + Memory)

| Metric | PC High | Console | Switch 2 |
|--------|---------|---------|----------|
| Max draw calls/frame | 4,000 | 3,000 | 1,200 |
| Max on-screen tris | 5M | 3M | 800K |
| Texture streaming pool | 4 GB | 2 GB | 512 MB |
| Max characters on screen | 30 | 20 | 8 |
| Shadow-casting lights | 8 | 4 | 2 |

## Additional Notes
- All assets authored at PC High quality, then downscaled per platform via LOD / mip chain
- Nanite enabled for PC High and Console (environment geometry only, NOT characters)
- Virtual Textures enabled on PC and Console; traditional mipmaps on Switch 2
- Switch 2 builds use simplified shaders (no SSR, no volumetric fog, baked GI only)
- Steam Deck targets PC Low settings with FSR 2.0 upscaling
