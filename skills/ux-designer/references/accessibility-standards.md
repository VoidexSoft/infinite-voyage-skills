# Game Accessibility Standards Reference

Comprehensive reference mapping industry accessibility standards to game-specific
requirements. Use this document when designing or auditing game UI to ensure
compliance with legal requirements and inclusive design best practices.

---

## 1. WCAG Mappings for Games

The Web Content Accessibility Guidelines (WCAG 2.1) were written for web content but many
principles translate directly to game interfaces.

### Perceivable (WCAG Principle 1)

| WCAG Criterion | Level | Game Application |
|----------------|-------|------------------|
| 1.1.1 Non-text Content | A | All icons have text labels or tooltips; ability icons include name text |
| 1.3.1 Info and Relationships | A | UI structure is conveyed through layout, not just visual styling |
| 1.3.3 Sensory Characteristics | A | Instructions never rely solely on shape, color, size, or sound |
| 1.4.1 Use of Color | A | Color is never the only means of conveying info (pair with icon/text) |
| 1.4.3 Contrast (Minimum) | AA | Text contrast ratio at least 4.5:1 against background |
| 1.4.6 Contrast (Enhanced) | AAA | Text contrast ratio at least 7:1 for critical gameplay text |
| 1.4.11 Non-text Contrast | AA | UI components and icons have 3:1 contrast against adjacent colors |
| 1.4.12 Text Spacing | AA | No content loss when line height is 1.5x, letter spacing 0.12em |

### Operable (WCAG Principle 2)

| WCAG Criterion | Level | Game Application |
|----------------|-------|------------------|
| 2.1.1 Keyboard | A | All menus navigable with keyboard alone (Tab, Enter, Escape, Arrows) |
| 2.1.2 No Keyboard Trap | A | Player can always exit any menu or dialog with Escape |
| 2.2.1 Timing Adjustable | A | Timed UI events (QTEs, dialogue timers) can be extended or disabled |
| 2.3.1 Three Flashes | A | No element flashes more than 3 times per second |
| 2.4.3 Focus Order | A | Tab order follows logical reading order (left-to-right, top-to-bottom) |
| 2.4.7 Focus Visible | AA | Focused UI element has a clearly visible outline or highlight |
| 2.5.1 Pointer Gestures | A | Complex gestures (pinch, multi-finger) have single-pointer alternatives |

### Understandable (WCAG Principle 3)

| WCAG Criterion | Level | Game Application |
|----------------|-------|------------------|
| 3.1.1 Language of Page | A | Game UI language matches player's selected locale |
| 3.2.1 On Focus | A | Focusing a UI element does not trigger unexpected actions |
| 3.2.2 On Input | A | Changing a setting does not cause unexpected navigation |
| 3.3.1 Error Identification | A | Errors (invalid input, failed action) are clearly described in text |
| 3.3.4 Error Prevention | AA | Destructive actions require confirmation; undo is available |

### Robust (WCAG Principle 4)

| WCAG Criterion | Level | Game Application |
|----------------|-------|------------------|
| 4.1.2 Name, Role, Value | A | UI elements have programmatic names for screen reader compatibility |

---

## 2. CVAA Compliance

The 21st Century Communications and Video Accessibility Act (CVAA) applies to games with
communication features (text chat, voice chat, online multiplayer).

### Requirements

| Requirement | Implementation |
|-------------|----------------|
| Text chat accessibility | Adjustable font size, high contrast mode, text-to-speech option |
| Voice chat accessibility | Push-to-talk alternative, volume control per player, mute option |
| UI navigation | All communication features navigable without vision (screen reader support) |
| Captioning | Real-time captions for voice chat (speech-to-text) |
| Customization | Player can adjust communication UI independently of game UI |

### Applicability to Game Development

- If multiplayer features are added, CVAA compliance becomes mandatory in the US
- Single-player subtitle and caption requirements are covered under general accessibility
- Any in-game messaging system must meet text accessibility standards

---

## 3. Xbox Accessibility Guidelines (XAG)

Microsoft's XAG provides 23 guidelines organized into categories. These are not legal
requirements but represent industry best practices and are required for certain Xbox
certifications.

### Text and UI

| Guideline | Requirement | Priority |
|-----------|-------------|----------|
| XAG 101 | Contrast ratio of at least 4.5:1 for text | Required |
| XAG 102 | Default text size legible at 10 feet on a TV (minimum 28px at 1080p for body text) | Required |
| XAG 103 | Text resizing option (at least 2 size options) | Recommended |
| XAG 104 | Screen narration / text-to-speech for all UI text | Recommended |

### Input

| Guideline | Requirement | Priority |
|-----------|-------------|----------|
| XAG 105 | Full remapping of all controls | Required |
| XAG 106 | Simple input mode (no complex simultaneous inputs) | Recommended |
| XAG 107 | Hold-to-press and toggle alternatives for sustained inputs | Required |
| XAG 108 | Sensitivity and dead zone adjustment for analog inputs | Recommended |

### Difficulty and Assists

| Guideline | Requirement | Priority |
|-----------|-------------|----------|
| XAG 109 | Adjustable difficulty with clear descriptions | Required |
| XAG 110 | Skip or bypass challenging content option | Recommended |
| XAG 111 | Auto-aim and target lock-on options | Recommended |
| XAG 112 | Invincibility or god mode option (assist feature) | Recommended |

### Audio and Visual

| Guideline | Requirement | Priority |
|-----------|-------------|----------|
| XAG 113 | Subtitles for all speech with speaker identification | Required |
| XAG 114 | Closed captions for significant non-speech audio | Recommended |
| XAG 115 | Visual alternatives for audio cues | Required |
| XAG 116 | Independent volume controls (master, music, SFX, dialogue) | Required |
| XAG 117 | Mono audio option | Recommended |
| XAG 118 | Colorblind mode (at least deuteranopia) | Required |
| XAG 119 | High contrast mode or outline option | Recommended |
| XAG 120 | No information conveyed by color alone | Required |
| XAG 121 | Screen shake and camera motion can be reduced or disabled | Required |
| XAG 122 | No flashing above 3Hz threshold | Required |
| XAG 123 | Photosensitivity warning at launch | Required |

---

## 4. Colorblind Modes

Three categories of color vision deficiency must be supported. Each mode adjusts the game's
color palette so that previously indistinguishable colors become distinct.

### Types and Prevalence

| Type | Affected Colors | Prevalence (Male) | Prevalence (Female) |
|------|----------------|-------------------|---------------------|
| Deuteranopia | Red-Green (green weak) | 6% | 0.4% |
| Protanopia | Red-Green (red weak) | 2% | 0.01% |
| Tritanopia | Blue-Yellow | 0.01% | 0.01% |
| Achromatopsia | All colors (monochrome) | 0.003% | 0.003% |

### Implementation Approach

1. **Symbol redundancy** -- Never use color as the sole differentiator. Pair with icons,
   shapes, patterns, or text labels.
2. **Palette swap** -- Provide named colorblind presets that remap problem color pairs.
3. **Custom filters** -- Advanced option: intensity slider and hue rotation per channel.
4. **Preview mode** -- Let all players preview colorblind modes so sighted designers can
   verify readability.

### Color Pairs to Avoid Without Redundancy

- Red and green (health vs poison, enemy vs ally)
- Red and brown (damage vs neutral)
- Blue and purple (mana vs special)
- Green and yellow (buff vs caution)

---

## 5. Subtitle Standards

Subtitles are one of the most-used accessibility features. Quality subtitles go beyond
transcribing words.

### Minimum Requirements

| Feature | Standard |
|---------|----------|
| Font size | Minimum 28px at 1080p (46px recommended for living room) |
| Font style | Sans-serif, medium or bold weight |
| Background | Semi-transparent black box behind text (70-80% opacity) |
| Speaker labels | Character name prefixed in distinct color: `[CAPTAIN]: We march at dawn` |
| Positioning | Bottom-center of screen, above any HUD elements |
| Duration | Minimum 1 second per subtitle, even for short lines |
| Line length | Maximum 2 lines visible simultaneously, ~42 characters per line |

### Enhanced Features

- Size options: Small (28px), Medium (36px), Large (46px), Extra Large (56px)
- Background opacity: adjustable from 0% to 100%
- Text color: white default, customizable
- Directional indicators for off-screen speakers: `[CAPTAIN, left]:` or arrow icon
- Sound descriptions in brackets: `[explosion]`, `[footsteps approaching]`
- Emotion tags when tone is not obvious: `[CAPTAIN, whispering]:`
- Letterboxing option: black bars at top/bottom to create clean subtitle space

---

## 6. Remappable Controls

Full input remapping is a legal and ethical requirement for accessible gaming.

### Requirements

- Every gameplay action must be remappable to any available button or key
- System-level inputs (Pause, Screenshot) may be exempt from remapping
- Conflict detection: warn when two actions share the same binding
- Reset to defaults: one-button option to restore original mappings
- Multiple profiles: save at least 3 custom mapping profiles
- Device-specific mappings: separate bindings for keyboard, gamepad, and touch

### Presets to Include

| Preset Name | Description |
|-------------|-------------|
| Default | Standard WASD + mouse / dual-stick gamepad |
| Left-Handed | Mirrored keyboard layout (IJKL or arrow keys for movement) |
| One-Handed (Left) | All essential actions accessible with left hand only |
| One-Handed (Right) | All essential actions accessible with right hand only |
| Simplified | Reduced inputs; combines actions where possible |
| Adaptive Controller | Optimized for Xbox Adaptive Controller or similar |

---

## 7. One-Handed Play

Games should support meaningful play with a single hand whenever mechanically feasible.

### Design Strategies

1. **Auto-actions** -- Auto-run, auto-aim, auto-attack options that reduce simultaneous inputs
2. **Sequential inputs** -- Replace simultaneous button presses with sequential ones
   (press A then B instead of A+B together)
3. **Toggle over hold** -- All hold actions (sprint, aim, block) have toggle alternatives
4. **Stick-only mode** -- Gamepad mode where one stick handles both movement and camera
   (with aim assist)
5. **Touch overlay** -- On-screen buttons positioned for single-thumb reach on mobile

### Testing

- Verify all critical gameplay paths are completable with one hand
- Test with both left-hand-only and right-hand-only configurations
- Ensure no rapid alternating inputs are required between two sides of the controller

---

## 8. Motion and Photosensitivity

### Requirements

| Feature | Standard |
|---------|----------|
| Screen shake | Must be reducible to 0% via settings slider |
| Camera bob | Must be disableable |
| Motion blur | Must be disableable |
| Field of view | Adjustable (60-120 degrees) on PC; recommended on console |
| Flash effects | Never exceed 3 flashes per second; warn before intense sequences |
| Parallax scrolling | Must be disableable or reducible |
| Photosensitivity warning | Display at game launch before any content plays |

---

## 9. Cognitive Accessibility

### Requirements

| Feature | Standard |
|---------|----------|
| Objective markers | Always visible; optional detailed guidance |
| Difficulty options | At least 3 levels with clear, non-judgmental descriptions |
| Tutorial replay | Accessible from pause menu at any time |
| Reading level | UI text at 8th-grade reading level or below |
| Jargon glossary | In-game reference for all game-specific terms |
| Save system | Frequent auto-save; manual save available anytime |
| Menu depth | Maximum 3 levels of nesting |
| Undo support | Reversible actions where possible (unequip, respec) |

---

## 10. Compliance Checklist Summary

Use this as a quick-reference during design reviews.

| Category | Must Have | Should Have | Nice to Have |
|----------|----------|-------------|--------------|
| Visual | 4.5:1 contrast, no color-only info, text scaling | 7:1 contrast, screen reader, high-contrast mode | Custom color filters |
| Audio | Subtitles, speaker labels, volume controls | Captions for SFX, mono audio, visual audio cues | Speech-to-text chat |
| Motor | Full remapping, hold/toggle options | One-handed presets, adaptive controller support | Eye-tracking support |
| Cognitive | Difficulty options, objective markers, save anytime | Tutorial replay, glossary, simple input mode | AI-driven dynamic difficulty |
| Photosensitivity | No 3Hz+ flashing, launch warning | Reducible screen shake, disable motion blur | Per-effect intensity sliders |

---

## Cross-References

- For the full design-time checklist, see `references/accessibility-checklist.md`
- For colorblind-safe palettes, see `references/color-palettes.md`
- For input device mappings and remapping, see `references/input-devices.md`
- For subtitle font sizing, see `references/font-guidelines.md`
- For the accessibility section in the skill itself, see the Accessibility Checklist in `SKILL.md`
