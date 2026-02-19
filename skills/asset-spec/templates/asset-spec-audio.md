# Audio Asset Specification

> Fill in all fields below. Replace bracketed placeholders with actual values.
> Delete any sections that do not apply, but document why they were removed.
> Reference: `references/audio-technical-guide.md`

---

## Overview

| Field | Value |
|-------|-------|
| **Asset Name** | [e.g., `SFX_Sword_Combat_Set`] |
| **Asset Category** | [SFX / Music / Voice Over / Ambience] |
| **Priority** | [Critical Path / High / Medium / Low] |
| **Owner** | [Audio designer / Composer / VO director name] |
| **Target Completion** | [YYYY-MM-DD] |
| **Deliverable Format** | [WAV 48kHz 24-bit] |

---

## Asset Description

### What Is This Audio For?
[One-paragraph description of the audio asset, its purpose, and when the player hears it.]

### Context of Use
- **Game system:** [Combat / Exploration / UI / Dialogue / Cinematic]
- **Trigger:** [Animation event / Player action / Zone entry / Scripted event]
- **Frequency:** [Constant loop / Frequent (every few seconds) / Occasional / One-time]
- **Emotional target:** [Describe the feeling this sound should evoke]

---

## Format Requirements

| Parameter | Value |
|-----------|-------|
| **Sample rate** | [48,000 Hz (standard)] |
| **Bit depth** | [24-bit (source) / 16-bit (runtime)] |
| **Channels** | [Mono / Stereo -- see channel rules in audio-technical-guide.md] |
| **Source format** | [WAV PCM (mandatory for source delivery)] |
| **Runtime format** | [Vorbis OGG / ADPCM / PCM 16-bit -- per audio-technical-guide.md] |
| **Runtime bitrate** | [e.g., 160 kbps for OGG] |

---

## Sound List

### SFX / VO / Ambience Items

| # | Sound Name | Description | Duration | Variations | Loop | Notes |
|---|-----------|-------------|----------|------------|------|-------|
| 1 | [e.g., `SFX_Sword_Swing_Light_01`] | [Light sword whoosh] | [0.3s] | [3] | [No] | [Pitched up slightly from heavy] |
| 2 | [e.g., `SFX_Sword_Swing_Heavy_01`] | [Heavy sword whoosh] | [0.5s] | [3] | [No] | [Lower pitch, more body] |
| 3 | [e.g., `SFX_Sword_Hit_Flesh_01`] | [Sword impact on organic target] | [0.4s] | [4] | [No] | [Include subtle squelch layer] |
| 4 | [e.g., `SFX_Sword_Hit_Metal_01`] | [Sword impact on metal armor/shield] | [0.5s] | [4] | [No] | [Metallic ring + impact thud] |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |

### Music Tracks (if Asset Category is Music)

| # | Track Name | Description | Duration | Stems | Loop Point | Notes |
|---|-----------|-------------|----------|-------|------------|-------|
| 1 | [e.g., `MUS_Exploration_Theme_A`] | [Main exploration theme] | [2:30] | [6] | [At 2:28] | [Seamless loop] |
| 2 | [e.g., `MUS_Combat_Intensity_Low`] | [Low-intensity combat music] | [1:45] | [4] | [At 1:43] | [Cross-fades with medium] |
| 3 | | | | | | |

### Total Asset Count

| Type | Count | Total Variations | Total Duration |
|------|-------|-----------------|----------------|
| [e.g., Swing SFX] | [2] | [6] | [2.4s] |
| [e.g., Impact SFX] | [2] | [8] | [3.6s] |
| **Total** | **[4]** | **[14]** | **[6.0s]** |

---

## Variation Requirements

| Sound | Min Variations | Randomization | Pitch Range | Volume Range |
|-------|---------------|---------------|-------------|--------------|
| [e.g., Sword swing] | [3 per weight class] | [Round-robin or random, no immediate repeat] | [+/- 5%] | [+/- 2 dB] |
| [e.g., Impact] | [4 per surface type] | [Random, weighted toward less-recently-played] | [+/- 3%] | [+/- 1 dB] |
| [e.g., Footstep] | [4 per surface] | [Round-robin] | [+/- 5%] | [+/- 2 dB] |

### Variation Rules
- Minimum 3 variations for any frequently-triggered sound (footsteps, impacts, swings)
- Minimum 2 variations for occasional sounds (ability casts, UI confirms)
- Single variation acceptable for one-time sounds (cinematics, unique VO lines)
- No two consecutive plays should be the same sample

---

## Loudness Target

| Parameter | Value | Reference |
|-----------|-------|-----------|
| **Integrated loudness (LUFS)** | [e.g., -16 LUFS for standard SFX] | [See audio-technical-guide.md] |
| **True peak ceiling** | [e.g., -1 dBTP] | [Never exceed across any sample] |
| **Loudness range (LRA)** | [e.g., 8-14 LU for SFX] | [Dynamic range] |
| **Category bus** | [e.g., SFX_Combat bus] | [Where this routes in the mixer] |

### Per-Sound Loudness Notes
[Document any sounds that intentionally deviate from the category target, with justification.]

| Sound | Target LUFS | Reason |
|-------|------------|--------|
| [e.g., Critical hit impact] | [-12 LUFS] | [Intentionally louder for emphasis] |
| [e.g., Ambient drip] | [-28 LUFS] | [Background detail, must not distract] |

---

## Spatial Settings

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Spatialization** | [3D / 2D (screen space) / N/A] | |
| **Min distance** | [e.g., 1m] | [Full volume within this radius] |
| **Max distance** | [e.g., 30m] | [Inaudible beyond this] |
| **Attenuation curve** | [Logarithmic / Linear / Custom] | [Reference audio-technical-guide.md] |
| **Doppler effect** | [Enabled / Disabled] | [For moving sources] |
| **Occlusion** | [Enabled / Disabled] | [Low-pass when behind walls] |
| **Spread** | [e.g., 0 (point) to 360 (omnidirectional)] | |
| **Reverb send** | [e.g., 50% to zone reverb bus] | [Wet/dry mix for room effect] |

---

## Priority and Polyphony

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Priority level** | [0-255; see priority table in audio-technical-guide.md] | |
| **Max instances** | [e.g., 4 simultaneous] | [Limit concurrent plays of this sound] |
| **Stealing behavior** | [Oldest / Quietest / Farthest / None] | [What happens when max instances exceeded] |
| **Virtualization** | [Enabled / Disabled] | [Continue tracking position when stolen] |

---

## Memory Budget

| Parameter | Value |
|-----------|-------|
| **Source file size (total, all variations)** | [e.g., 12 MB uncompressed WAV] |
| **Runtime compressed size** | [e.g., 2.4 MB as Vorbis OGG] |
| **Load strategy** | [Loaded into RAM / Streamed from disk] |
| **Streaming buffer** | [e.g., 256 KB if streamed] |
| **Memory category** | [e.g., SFX_Combat pool] |

### Memory Budget Justification
[Explain why the load strategy was chosen. Reference the decision matrix in audio-technical-guide.md.]

---

## Middleware Configuration (FMOD / Wwise)

| Parameter | Value |
|-----------|-------|
| **Event name** | [e.g., `event:/SFX/Combat/Sword_Swing`] |
| **Bank** | [e.g., `SFX_Combat.bank`] |
| **Bus routing** | [e.g., `bus:/SFX/Combat`] |
| **Parameters** | [List RTPC / game parameters that affect this sound] |
| **Snapshots** | [Any snapshot states that modify this sound] |

### Parameter Mapping

| Parameter Name | Type | Range | Effect |
|----------------|------|-------|--------|
| [e.g., `SwingSpeed`] | [Float] | [0.0 - 1.0] | [Pitch: 0.9x at 0.0 to 1.1x at 1.0] |
| [e.g., `SurfaceType`] | [Int / Label] | [0-4] | [Selects impact sound layer: flesh/metal/stone/wood/dirt] |
| [e.g., `Distance`] | [Float] | [0 - max dist] | [Automatic attenuation + low-pass filter] |

---

## Naming Convention

All files must follow the naming pattern from `references/audio-technical-guide.md`:

```
[Category]_[Subject]_[Action]_[Variant].wav

Examples for this spec:
  [e.g., SFX_Sword_SwingLight_01.wav]
  [e.g., SFX_Sword_SwingLight_02.wav]
  [e.g., SFX_Sword_SwingLight_03.wav]
  [e.g., SFX_Sword_HitFlesh_01.wav]
  [e.g., SFX_Sword_HitFlesh_02.wav]
```

---

## Approval Criteria

### Design Gate
- [ ] Sound matches intended emotional tone
- [ ] Volume sits correctly in category mix (not too loud or quiet)
- [ ] Variations sound natural and distinct (no obvious repetition)
- [ ] Duration matches gameplay timing (attack sounds sync with animation)
- [ ] Spatial behavior feels correct (distance, direction, occlusion)

### Technical Gate
- [ ] All files are 48 kHz / 24-bit WAV (source)
- [ ] Naming convention followed exactly
- [ ] No clipping (true peak below ceiling)
- [ ] Integrated loudness within target range
- [ ] Mono/stereo config correct for spatialization type
- [ ] No DC offset, clicks, pops, or unwanted noise

### Integration Gate
- [ ] Triggers correctly from game events
- [ ] Priority and stealing behavior verified under load
- [ ] Randomization sounds natural (no immediate repeats)
- [ ] Spatial attenuation and occlusion working
- [ ] Memory usage within budget
- [ ] No audible compression artifacts at runtime bitrate

---

## Delivery Checklist

- [ ] All source WAV files (48 kHz / 24-bit)
- [ ] Files named per convention
- [ ] Middleware event configured (FMOD/Wwise project file)
- [ ] Parameter mappings documented and tested
- [ ] Loudness report (LUFS measurements per file)
- [ ] Memory usage report (compressed sizes)
- [ ] Integration test notes (tested in-engine)
- [ ] This spec document updated with final values

---

## Timeline

| Milestone | Date | Sign-off |
|-----------|------|----------|
| Sound design first pass | [YYYY-MM-DD] | [Audio Lead] |
| Mix and loudness pass | [YYYY-MM-DD] | [Audio Lead] |
| Middleware integration | [YYYY-MM-DD] | [Audio Lead + Tech] |
| In-engine testing | [YYYY-MM-DD] | [Audio Lead + QA] |
| Final delivery | [YYYY-MM-DD] | [Audio Lead] |

---

## Dependencies

### Inputs
- [ ] Animation timing data (when do sounds trigger?)
- [ ] Gameplay design values (attack speeds, movement speeds)
- [ ] Zone / environment info (reverb zones, occlusion geometry)
- [ ] Mixer bus structure (where does this sound route?)
- [ ] Memory budget allocation (how much RAM for this category?)

### Outputs
- [ ] Animation system (animation events trigger these sounds)
- [ ] VFX system (some VFX are synced to audio cues)
- [ ] Gameplay feel (combat responsiveness depends on audio timing)
- [ ] Accessibility (subtitles/captions may reference VO/SFX events)

### Related Audio Assets
- [List other audio specs that must be mixed relative to this one]
- [e.g., This sword SFX set must sit below dialogue but above ambient]
- [e.g., Impact sounds must layer cleanly with hit reaction VO barks]

---
