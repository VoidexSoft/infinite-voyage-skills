# Audio Technical Guide — Infinite Voyage

This document defines audio format specifications, loudness standards, memory budgets,
and middleware configuration for all audio assets in Infinite Voyage. Use this guide
when writing audio asset specifications for SFX, music, voice acting, and ambience.

---

## Audio Format Specifications

### Source Formats (Authoring / Delivery)

All audio delivered to the project must be in high-quality source format. Compression
is applied during the build pipeline, not by the audio designer.

| Format | Extension | Use Case | Notes |
|--------|-----------|----------|-------|
| **WAV (PCM)** | `.wav` | Primary source format | Uncompressed, lossless; preferred for all deliverables |
| **AIFF** | `.aif` | Alternate source format | Equivalent to WAV; accepted but WAV preferred |
| **FLAC** | `.flac` | Archival only | Lossless compressed; not used in pipeline directly |

**Do not deliver** MP3, OGG, AAC, or WMA as source files. These are lossy and cannot
be re-encoded without generation loss.

### Runtime Formats (In-Engine)

The build pipeline compresses source audio into platform-appropriate formats.

| Format | Extension | Compression | Quality | Use Case |
|--------|-----------|-------------|---------|----------|
| **Vorbis OGG** | `.ogg` | Lossy, variable bitrate | Good | SFX, ambience, voice (PC/Console) |
| **OPUS** | `.opus` | Lossy, low-latency | Excellent | Voice chat, streaming (if supported) |
| **ADPCM** | `.wav` (ADPCM) | Lossy, 4:1 ratio | Moderate | Short SFX, footsteps (low CPU decode) |
| **PCM 16-bit** | `.wav` | Uncompressed | Perfect | Critical SFX needing zero latency |
| **AAC** | `.m4a` | Lossy | Good | Music streaming on mobile |
| **AT9** | `.at9` | Lossy, hardware decode | Excellent | PlayStation exclusive format |
| **XMA** | `.xma` | Lossy, hardware decode | Excellent | Xbox exclusive format |

### Recommended Runtime Settings

| Audio Category | PC/Console Format | Mobile Format | Bitrate |
|----------------|-------------------|---------------|---------|
| **SFX (short)** | Vorbis OGG | ADPCM | 128-192 kbps |
| **SFX (critical)** | PCM 16-bit | ADPCM | Uncompressed |
| **Music** | Vorbis OGG | AAC | 192-256 kbps |
| **Voice Over** | Vorbis OGG | Vorbis OGG | 96-128 kbps |
| **Ambience** | Vorbis OGG | Vorbis OGG | 128-160 kbps |

---

## Sample Rate Specifications

| Sample Rate | Use Case | Notes |
|-------------|----------|-------|
| **48,000 Hz (48 kHz)** | Standard for all game audio | Broadcast/film standard; default for Infinite Voyage |
| **44,100 Hz (44.1 kHz)** | Acceptable alternate | CD standard; convert to 48 kHz in pipeline if needed |
| **96,000 Hz (96 kHz)** | Recording / processing only | Downsample to 48 kHz for delivery |
| **22,050 Hz** | Not recommended | Audible quality loss on modern hardware |

### Bit Depth

| Bit Depth | Use Case | Dynamic Range |
|-----------|----------|---------------|
| **24-bit** | Source delivery standard | 144 dB (exceeds human hearing) |
| **16-bit** | Runtime / final export | 96 dB (sufficient for playback) |
| **32-bit float** | Internal processing only | Infinite headroom; used in DAWs |

**Standard delivery: 48 kHz / 24-bit WAV (mono or stereo as specified)**

---

## Channel Configurations

| Config | Channels | Use Case |
|--------|----------|----------|
| **Mono** | 1 | Point-source SFX (footsteps, impacts, voice), 3D spatialized sounds |
| **Stereo** | 2 (L/R) | Music, ambient beds, UI sounds, non-spatialized audio |
| **Quad** | 4 | Ambience beds (rare; engine handles spatialization) |
| **5.1 Surround** | 6 | Music stems, cinematics (console/PC only) |
| **7.1 Surround** | 8 | Cinematic audio only (console/PC only) |
| **Ambisonics (1st order)** | 4 (W/X/Y/Z) | VR ambience (if VR support is added) |

### Channel Assignment Rules

| Audio Type | Channel Config | Reason |
|------------|---------------|--------|
| Footsteps | Mono | 3D positioned at character feet |
| Weapon impacts | Mono | 3D positioned at impact point |
| Voice acting | Mono | 3D positioned at character head |
| UI clicks / confirms | Stereo | Non-spatialized, plays in screen space |
| Music | Stereo | Non-spatialized, full stereo image |
| Ambient loops (wind, rain) | Stereo | Ambient bed, not point-source |
| Ambient point source (torch, waterfall) | Mono | 3D positioned in world |
| Cinematic audio | 5.1 or Stereo | Depends on platform support |

---

## Loudness Standards

All audio in Infinite Voyage follows integrated loudness targeting for consistent
player experience. Loudness is measured in LUFS (Loudness Units relative to Full Scale).

### LUFS Targets by Category

| Category | Target LUFS | Peak Ceiling | Range (LRA) | Notes |
|----------|------------|--------------|-------------|-------|
| **Master Mix** | -16 LUFS | -1 dBTP | 8-12 LU | Overall game output |
| **Music** | -18 LUFS | -1 dBTP | 6-10 LU | Sits under dialogue and SFX |
| **Dialogue / VO** | -14 LUFS | -1 dBTP | 4-8 LU | Most prominent; must be clear |
| **SFX (Standard)** | -16 LUFS | -1 dBTP | 8-14 LU | General sound effects |
| **SFX (Impact/Combat)** | -12 LUFS | -1 dBTP | 6-10 LU | Punchy, attention-grabbing |
| **SFX (UI)** | -20 LUFS | -3 dBTP | 2-4 LU | Subtle, non-intrusive |
| **Ambience** | -24 LUFS | -6 dBTP | 4-8 LU | Background atmosphere |
| **Cinematics** | -16 LUFS | -1 dBTP | 10-16 LU | Broadcast standard |

### Loudness Measurement Tools

- **LUFS Meter:** Use an ITU-R BS.1770-compliant meter (available in most DAWs)
- **True Peak:** Measure inter-sample peaks (dBTP), not just sample peaks (dBFS)
- **Short-term:** Measure 3-second windows for moment-to-moment consistency
- **Integrated:** Measure full clip duration for overall level

### Dynamic Range Guidelines

- **Dialogue:** Compress to maintain intelligibility; target 4-8 LU range
- **Music:** Preserve dynamics but keep within 6-10 LU range
- **SFX:** Allow transients (impacts) but control sustained sounds
- **Ambience:** Consistent level; minimal dynamics (4-8 LU range)
- **Never exceed -1 dBTP** on any individual asset (headroom for mixing and runtime effects)

---

## Compression Settings

### Vorbis OGG Encoding

| Quality Level | Bitrate (Approx.) | Use Case |
|---------------|-------------------|----------|
| Q0 (64 kbps) | 64 kbps | Low-priority background sounds |
| Q3 (112 kbps) | 112 kbps | Voice, standard ambience |
| Q5 (160 kbps) | 160 kbps | Standard SFX, music |
| Q7 (224 kbps) | 224 kbps | High-quality music, critical SFX |
| Q10 (500 kbps) | ~500 kbps | Maximum quality (rarely needed) |

**Default project setting: Q5 (160 kbps) for SFX, Q7 (224 kbps) for music**

### ADPCM Settings

- **Compression ratio:** 4:1 (always fixed)
- **Quality:** Lower than Vorbis but nearly zero CPU decode cost
- **Best for:** Short, percussive sounds (footsteps, clicks, impacts)
- **Avoid for:** Music, sustained tones, speech (audible artifacts)

---

## Memory Budgets

### Per-Platform Audio Memory

| Platform | Total Audio RAM | Loaded Budget | Streaming Budget |
|----------|----------------|---------------|------------------|
| **PC High** | 512 MB | 256 MB | 256 MB streaming pool |
| **PC Medium** | 256 MB | 128 MB | 128 MB streaming pool |
| **PS5 / Xbox Series X** | 384 MB | 192 MB | 192 MB streaming pool |
| **PS4 / Xbox One** | 256 MB | 128 MB | 128 MB streaming pool |
| **Nintendo Switch** | 128 MB | 64 MB | 64 MB streaming pool |
| **Mobile High** | 128 MB | 64 MB | 64 MB streaming pool |
| **Mobile Low** | 64 MB | 32 MB | 32 MB streaming pool |

### Per-Category Memory Allocation

Example allocation for 256 MB total audio RAM (Medium tier):

| Category | Loaded | Streamed | Total | Notes |
|----------|--------|----------|-------|-------|
| SFX (combat) | 40 MB | 0 | 40 MB | Instant playback required |
| SFX (environment) | 20 MB | 10 MB | 30 MB | Some streamed for variety |
| SFX (UI) | 10 MB | 0 | 10 MB | Always loaded |
| Voice Over | 5 MB | 40 MB | 45 MB | Stream dialogue on demand |
| Music | 2 MB | 60 MB | 62 MB | Stream all music |
| Ambience | 10 MB | 30 MB | 40 MB | Loop points loaded, tails streamed |
| Cinematics | 0 | 20 MB | 20 MB | Fully streamed |
| Reserve / Headroom | 9 MB | 0 | 9 MB | Buffer for spikes |
| **Total** | **96 MB** | **160 MB** | **256 MB** | |

---

## Streaming vs. Loaded Audio

### Decision Matrix

| Criteria | Load into RAM | Stream from Disk |
|----------|--------------|-----------------|
| Playback latency | Instant (< 1 ms) | 50-200 ms startup delay |
| Memory cost | Full file in RAM | Small buffer only (~256 KB) |
| Simultaneous instances | Unlimited (same memory) | Limited by I/O bandwidth |
| File duration | Short (< 5 seconds) | Long (> 5 seconds) |
| Trigger frequency | High (many per second) | Low (occasional) |
| Random access | Yes (seek anywhere) | Sequential only |

### Streaming vs. Loaded by Category

| Audio Type | Strategy | Reason |
|------------|----------|--------|
| Footsteps | **Loaded** | Triggered rapidly, must be instant |
| Weapon impacts | **Loaded** | Timing-critical, combat feedback |
| UI sounds | **Loaded** | Must feel responsive |
| Vocal barks (short) | **Loaded** | Quick combat callouts |
| Dialogue lines | **Streamed** | Long files, sequential playback |
| Music tracks | **Streamed** | Very large files, one at a time |
| Ambient loops | **Loaded** (short) / **Streamed** (long) | Depends on loop length |
| Cinematic audio | **Streamed** | Large, sequential, one-time playback |

---

## Middleware Notes

### FMOD Studio

FMOD is the primary audio middleware for Infinite Voyage.

| Setting | Value | Notes |
|---------|-------|-------|
| **FMOD Studio version** | 2.02.x | Keep in sync with engine plugin |
| **Max channels** | 256 (PC/Console), 64 (Mobile) | Polyphony limit |
| **Virtual voices** | 512 | Voices beyond channel limit are virtualized |
| **Sample rate** | 48,000 Hz | Must match project standard |
| **Speaker mode** | 7.1 (PC/Console), Stereo (Mobile) | Auto-downmix as needed |
| **DSP buffer size** | 1024 samples (PC), 2048 (Mobile) | Balance latency vs. stability |

#### FMOD Bank Organization

| Bank Name | Contents | Load Strategy |
|-----------|----------|---------------|
| `Master.bank` | Bus structure, routing | Always loaded |
| `Master.strings.bank` | Event name lookup table | Always loaded |
| `SFX_Combat.bank` | Weapon, impact, ability sounds | Loaded in combat zones |
| `SFX_Environment.bank` | Door, lever, trap sounds | Loaded per zone |
| `SFX_UI.bank` | Menu, button, notification sounds | Always loaded |
| `SFX_Footsteps.bank` | All footstep variations | Always loaded |
| `Music_Exploration.bank` | Exploration music tracks | Streamed |
| `Music_Combat.bank` | Combat music tracks | Streamed |
| `VO_[Character].bank` | Per-character voice lines | Streamed on demand |
| `AMB_[Zone].bank` | Zone-specific ambience | Loaded per zone |

### Wwise (Alternate)

If the project migrates to Wwise, apply these equivalent settings:

| FMOD Concept | Wwise Equivalent |
|-------------|------------------|
| Event | Event |
| Bank | SoundBank |
| Bus | Audio Bus |
| Snapshot | State / Switch |
| Parameter | RTPC (Real-Time Parameter Control) |
| Virtual voice | Virtual Voice system |
| 3D Panner | 3D Spatialization |

---

## 3D Audio and Spatialization

### Attenuation Curves

| Sound Type | Min Distance | Max Distance | Curve | Falloff |
|------------|-------------|-------------|-------|---------|
| Footstep | 0.5 m | 15 m | Logarithmic | Natural |
| Weapon hit | 1 m | 30 m | Logarithmic | Natural |
| Voice (dialogue) | 0.5 m | 10 m | Linear | Gentle |
| Voice (shout) | 1 m | 50 m | Logarithmic | Natural |
| Ambient point (torch) | 0.5 m | 8 m | Inverse | Gentle |
| Ambient point (waterfall) | 2 m | 40 m | Logarithmic | Natural |
| Explosion | 2 m | 80 m | Logarithmic | Steep |
| Music | N/A | N/A | None | Non-spatialized |
| UI | N/A | N/A | None | Non-spatialized |

### Occlusion and Obstruction

- **Occlusion:** Full blockage (wall between listener and source); apply low-pass filter + volume reduction
- **Obstruction:** Partial blockage (object partially blocks path); apply subtle low-pass only
- **Raycast frequency:** Every 100 ms (balance accuracy vs. CPU cost)
- **Filter settings:** Occlusion cuts above 1 kHz; Obstruction cuts above 4 kHz

### Reverb Zones

| Environment | Reverb Type | Decay Time | Wet Mix |
|-------------|------------|------------|---------|
| Open outdoor | Plate (small) | 0.5 sec | 10% |
| Forest | Early reflections | 1.0 sec | 15% |
| Stone corridor | Hall (small) | 2.0 sec | 30% |
| Large cave | Hall (large) | 4.0 sec | 40% |
| Metal room | Room (bright) | 1.5 sec | 25% |
| Underwater | Custom (muffled) | 0.8 sec | 60% |

---

## Audio Priority System

When the number of playing sounds exceeds the channel limit, lower-priority sounds
are virtualized (silenced but tracked) or stolen.

| Priority Level | Value | Category | Behavior at Limit |
|----------------|-------|----------|-------------------|
| **Critical** | 0-10 | Player VO, UI confirm, music | Never stolen |
| **High** | 11-50 | Combat SFX, enemy VO, ability SFX | Stolen last |
| **Medium** | 51-150 | Footsteps, prop interactions | Standard stealing |
| **Low** | 151-200 | Ambient point sources, distant sounds | Stolen first |
| **Background** | 201-255 | Wind detail, particle sounds, foley | Aggressively stolen |

---

## Naming Convention for Audio Files

```
[Category]_[Subject]_[Action]_[Variant].wav

Categories: SFX, MUS, VO, AMB
Variants: Two-digit numbers (01, 02, 03)

Examples:
  SFX_Footstep_Stone_Light_01.wav
  SFX_Sword_Hit_Metal_03.wav
  MUS_Exploration_Theme_A.wav
  VO_Warrior_Combat_BattleCry_02.wav
  AMB_Forest_Wind_Loop_01.wav
```

---

*Last updated for Infinite Voyage production pipeline. Audio specifications are
mandatory for all audio deliverables. Middleware settings subject to version updates.*
