# Comprehensive Accessibility Checklist

Pre-ship validation checklist. Every item must be verified before
release. This checklist covers visual, audio, motor, and cognitive accessibility. Use it
during design reviews, QA testing, and certification preparation.

Mark items as:
- [x] Passed
- [ ] Not yet verified
- [!] Failed (needs fix)
- [~] Partially implemented (needs improvement)
- [N/A] Not applicable to this build

---

## 1. Visual Accessibility

### 1.1 Text Size and Readability

- [ ] Body text is at least 16px at 1080p on PC
- [ ] Body text is at least 24px at 1080p on console
- [ ] Body text is at least 14dp on mobile
- [ ] Text scaling option is available (at least 3 levels: small, default, large)
- [ ] Maximum text scaling (2x) does not clip or overflow containers
- [ ] Minimum text scaling does not go below 12px on PC or 18px on console
- [ ] Text scaling is independent from HUD scaling
- [ ] Font is sans-serif for all gameplay-critical text (HUD, menus, subtitles)
- [ ] Line height is at least 1.5x font size for body text
- [ ] Maximum line length does not exceed 80 characters
- [ ] Decorative/stylized fonts are used only for titles, never for critical information
- [ ] All text is anti-aliased and renders crisply at the target resolution
- [ ] Character distinction: I (capital i), l (lowercase L), 1 (one), O, and 0 are distinct

### 1.2 Contrast

- [ ] All body text meets WCAG AA contrast ratio (4.5:1 minimum)
- [ ] All large text (18px+ bold or 24px+) meets 3:1 contrast ratio
- [ ] Critical gameplay text (health, damage numbers) meets WCAG AAA (7:1)
- [ ] UI components and icons meet 3:1 contrast against adjacent colors
- [ ] HUD elements remain readable over the brightest in-game scene
- [ ] HUD elements remain readable over the darkest in-game scene
- [ ] Text on variable backgrounds uses shadow, outline, or opaque backing
- [ ] High contrast mode is available in settings (increases all ratios by 50%+)
- [ ] High contrast mode can be toggled without restarting the game

### 1.3 Colorblind Support

- [ ] No information is conveyed by color alone (always paired with icon, text, or shape)
- [ ] Colorblind mode option is available in settings
- [ ] At least deuteranopia (red-green) mode is supported
- [ ] Protanopia mode is supported
- [ ] Tritanopia (blue-yellow) mode is supported
- [ ] Status effects use distinct icon shapes in addition to color
- [ ] Item rarity uses border patterns or markers in addition to color
- [ ] Minimap markers use distinct shapes in addition to color
- [ ] Enemy vs ally differentiation does not rely solely on red vs green
- [ ] Health and mana bars are distinguishable without color (position, label, icon)
- [ ] Colorblind modes have been tested by colorblind individuals

### 1.4 Screen Reader and Text-to-Speech

- [ ] All UI elements have programmatic labels (name, role, state)
- [ ] Screen reader navigation follows logical tab order
- [ ] Screen reader announces screen transitions and context changes
- [ ] Images and icons have alt text or equivalent spoken description
- [ ] Text-to-speech option is available for all on-screen text
- [ ] Text-to-speech reads in the player's selected language
- [ ] Focus indicators are clearly visible when using screen reader navigation

### 1.5 Visual Effects

- [ ] No element flashes more than 3 times per second
- [ ] Photosensitivity warning is displayed at game launch
- [ ] Screen shake intensity is adjustable (slider from 0% to 100%)
- [ ] Screen shake can be disabled entirely (0% setting)
- [ ] Motion blur can be disabled
- [ ] Camera bob can be disabled
- [ ] Parallax effects can be disabled
- [ ] Field of view is adjustable (at least 60-120 degrees on PC)
- [ ] "Reduce motion" setting disables all non-essential animations
- [ ] Warning is shown before any intense visual sequence (strobe, rapid motion)

---

## 2. Audio Accessibility

### 2.1 Subtitles

- [ ] Subtitles are available for all spoken dialogue
- [ ] Subtitles are enabled by default (opt-out, not opt-in)
- [ ] Subtitles include speaker identification labels
- [ ] Speaker labels use distinct colors or formatting per character
- [ ] Subtitle text size is adjustable (at least 3 levels)
- [ ] Subtitle background opacity is adjustable (0% to 100%)
- [ ] Subtitles do not exceed 2 lines on screen simultaneously
- [ ] Subtitle line length does not exceed 42 characters per line
- [ ] Subtitles persist for at least 1 second, even for short lines
- [ ] Subtitles are positioned within the title-safe area
- [ ] Subtitle position is customizable (top, center, bottom)

### 2.2 Captions and Sound Descriptions

- [ ] Closed captions are available for significant non-speech audio
- [ ] Environmental sounds have visual indicators: `[footsteps]`, `[explosion]`
- [ ] Music context is captioned: `[tense music]`, `[calm melody]`
- [ ] Directional audio has visual representation (arrow indicators on HUD)
- [ ] Danger sounds have visual equivalents (minimap markers, screen edge flash)
- [ ] Ability-ready audio cue has a corresponding visual indicator (icon glow/flash)
- [ ] Low-health audio warning has a corresponding visual indicator (vignette, bar pulse)

### 2.3 Volume Controls

- [ ] Master volume slider is available
- [ ] Separate sliders for: Music, Sound Effects, Dialogue, Ambient
- [ ] Each volume slider ranges from 0% to 100%
- [ ] Volume changes take effect immediately (live preview)
- [ ] Mono audio option is available (for single-ear hearing or hearing aids)
- [ ] Audio compressor / dynamic range option is available (reduces loud peaks)
- [ ] Muting one category does not mute others
- [ ] Volume settings persist between game sessions

### 2.4 Audio Descriptions

- [ ] Option for audio descriptions of important visual events (cutscene narration)
- [ ] Audio descriptions do not overlap with dialogue
- [ ] Audio descriptions can be toggled independently from subtitles

---

## 3. Motor Accessibility

### 3.1 Control Remapping

- [ ] All gameplay actions are remappable to any key or button
- [ ] Keyboard and gamepad remapping are available independently
- [ ] Conflict detection warns when two actions share the same binding
- [ ] "Reset to defaults" option is available
- [ ] At least 3 custom control profiles can be saved
- [ ] Control presets are available: Default, Left-Handed, One-Handed (L), One-Handed (R)
- [ ] Remapping screen shows all current bindings in a scannable table
- [ ] Remapped controls are reflected in all in-game prompts and tooltips

### 3.2 Hold vs Toggle

- [ ] All sustained actions have a hold/toggle option (sprint, aim, block, crouch)
- [ ] Hold vs toggle is configurable per-action, not globally only
- [ ] Default is hold for combat actions; toggle for movement modifiers
- [ ] Toggle indicators are visible on HUD (e.g., sprint icon when toggled on)

### 3.3 Aim Assistance

- [ ] Auto-aim option is available with adjustable strength (Off / Low / Medium / High)
- [ ] Target lock-on is available (single button to lock camera and attacks to nearest enemy)
- [ ] Aim assist does not interfere with manual aiming when set to Off
- [ ] Lock-on can cycle between targets (left/right input)
- [ ] Lock-on disengages at configurable range

### 3.4 Input Timing

- [ ] Quick-time events (QTEs) have extended time options or can be disabled
- [ ] No rapid button-mashing requirements (or alternatives provided)
- [ ] Input buffer window is adjustable (100ms to 500ms)
- [ ] Double-tap actions have a configurable timing window
- [ ] Timed dialogue choices can be paused or extended

### 3.5 Touch and Pointer

- [ ] All interactive elements are at least 48x48dp on touch devices
- [ ] Touch targets have at least 8dp spacing between them
- [ ] On-screen button layout is customizable (drag to reposition)
- [ ] On-screen button size is adjustable (small, medium, large)
- [ ] On-screen button opacity is adjustable (20% to 100%)
- [ ] Complex gestures (pinch, multi-finger) have single-tap alternatives
- [ ] Touch dead zone is adjustable

### 3.6 Alternative Input Devices

- [ ] Xbox Adaptive Controller is supported
- [ ] Co-pilot mode is supported (two controllers share one player input)
- [ ] External switch devices are supported (minimum 2-switch play)
- [ ] Eye tracking input is supported (or planned for future update)
- [ ] Voice commands for basic actions are supported (or planned)

---

## 4. Cognitive Accessibility

### 4.1 Difficulty and Pacing

- [ ] At least 3 difficulty levels are available with clear descriptions
- [ ] Difficulty descriptions are non-judgmental (no "Baby Mode" labeling)
- [ ] Difficulty can be changed at any time without restarting
- [ ] Custom difficulty allows per-system adjustments (damage, enemy count, timing)
- [ ] Auto-save occurs frequently (at least every 5 minutes of gameplay)
- [ ] Manual save is available at any time (not restricted to save points)
- [ ] Game speed can be adjusted (0.5x to 1.0x) or paused during action
- [ ] There is no penalty for pausing (enemies freeze, timers stop)

### 4.2 UI Simplification

- [ ] A "Simple UI" mode is available that reduces HUD elements to essentials
- [ ] All icons are paired with text labels
- [ ] Consistent button placement across all screens (Confirm always in the same position)
- [ ] Menu depth does not exceed 3 levels
- [ ] Breadcrumb trail shows current menu location
- [ ] No more than 7 options visible per menu screen (without scrolling)
- [ ] Active selection is highlighted with both color and shape/border change
- [ ] Undo is available for reversible actions (unequip, respec, sell)
- [ ] Destructive actions require confirmation with the safe option as default

### 4.3 Objective Clarity

- [ ] Current objective is always visible on the HUD (or accessible with one button)
- [ ] Objective tracker updates dynamically as progress is made
- [ ] Waypoint/compass marker points to next objective
- [ ] Minimap shows objective destination
- [ ] Failed objectives explain why they failed (not just "FAILED")
- [ ] Quest log provides full details of all active and completed quests
- [ ] Objective guidance level is adjustable (detailed markers to no markers)

### 4.4 Tutorials and Help

- [ ] Tutorial can be skipped at any point
- [ ] Tutorial can be replayed from the pause menu
- [ ] Contextual tips appear for new mechanics (just-in-time teaching)
- [ ] Tip frequency is adjustable (All / Reduced / Off)
- [ ] In-game glossary defines all game-specific terms
- [ ] Loading screen tips provide useful gameplay information
- [ ] Help button is always accessible from any menu screen
- [ ] Tooltip progression reduces verbosity as the player gains experience

### 4.5 Reading and Language

- [ ] UI text is at or below an 8th-grade reading level
- [ ] Abbreviations and jargon are defined on first use
- [ ] Numbers use locale-appropriate formatting (commas, periods)
- [ ] Date and time formats follow the player's locale
- [ ] Critical information is communicated through multiple channels (text + icon + color)

---

## 5. Platform-Specific Checks

### PC

- [ ] All menus are fully navigable with keyboard only (Tab, Arrows, Enter, Escape)
- [ ] All menus are fully navigable with mouse only
- [ ] Keyboard shortcuts are displayed next to their actions
- [ ] Resolution and windowed mode options are available
- [ ] Ultra-wide (21:9) and super ultra-wide (32:9) aspect ratios are supported
- [ ] UI scales correctly from 720p to 4K

### Console

- [ ] All text is readable at 10-foot viewing distance on a 1080p TV
- [ ] Gamepad-only navigation works for all menus
- [ ] Platform-specific button icons are displayed correctly (Xbox/PS/Switch)
- [ ] Title-safe area (5% inset) is respected for all HUD elements
- [ ] Game meets platform certification accessibility requirements

### Mobile

- [ ] Touch targets meet minimum size requirements (48x48dp)
- [ ] UI adapts to portrait and landscape orientations (if both supported)
- [ ] System accessibility features are respected (TalkBack, VoiceOver, Dynamic Type)
- [ ] On-screen controls do not obscure critical gameplay areas
- [ ] Game is playable with external controller (MFi, HID gamepad)

---

## 6. Testing Protocol

### Manual Testing Requirements

| Test | Method | Frequency |
|------|--------|-----------|
| Colorblind simulation | Apply deuteranopia/protanopia/tritanopia filter to all screens | Every UI change |
| Keyboard-only navigation | Unplug mouse; navigate all menus with keyboard | Every sprint |
| Gamepad-only navigation | Use only gamepad for entire game flow | Every sprint |
| Screen reader | Enable platform screen reader; verify all elements are announced | Monthly |
| Large text mode | Set text to maximum scale; verify no clipping or overflow | Every UI change |
| High contrast mode | Enable high contrast; verify all elements remain visible | Every sprint |
| Reduced motion | Enable reduced motion; verify no essential info is lost | Every sprint |
| One-handed play | Complete a combat encounter with one hand only | Every combat change |
| Subtitle verification | Play all dialogue with audio muted; verify subtitles are complete | Before release |

### Automated Checks

| Check | Tool | Threshold |
|-------|------|-----------|
| Contrast ratio | Automated screenshot analysis | Fail if any text < 4.5:1 |
| Flash detection | Frame-by-frame brightness analysis | Fail if > 3 flashes/sec |
| Touch target size | Layout inspector | Fail if any target < 48dp |
| Text overflow | Render at max scale + longest locale | Fail if any text clips |
| Missing labels | UI tree walker | Fail if any interactive element has no label |

---

## 7. Certification Standards Reference

| Standard | Requirement Level | Relevant Sections |
|----------|------------------|-------------------|
| WCAG 2.1 AA | Recommended baseline | Sections 1.1, 1.2, 2.1, 3.1, 4.1 |
| CVAA | Required (if communication features exist) | Section 2.1, 2.3 |
| Xbox Accessibility Guidelines (XAG) | Required (Xbox release) | All sections |
| PlayStation Accessibility Guidelines | Required (PS release) | All sections |
| Nintendo Accessibility Guidelines | Recommended (Switch release) | All sections |
| Section 508 (US) | Informational (government procurement) | Sections 1, 2, 3 |
| EN 301 549 (EU) | Informational (EU digital accessibility) | Sections 1, 2, 3 |

For detailed standards mapping, see `references/accessibility-standards.md`.

---

## 8. Sign-Off

Before release, the following stakeholders must sign off on accessibility:

| Reviewer | Area | Status |
|----------|------|--------|
| UX Designer | Visual, cognitive, interaction design | [ ] Approved |
| QA Lead | All automated and manual test results | [ ] Approved |
| Audio Designer | Subtitles, captions, volume controls | [ ] Approved |
| Input Designer | Remapping, hold/toggle, accessibility controllers | [ ] Approved |
| Accessibility Consultant | Full checklist review | [ ] Approved |
| Player Testers (diverse abilities) | Real-world usability | [ ] Approved |

---

## Cross-References

- For detailed accessibility standards, see `references/accessibility-standards.md`
- For colorblind palette details, see `references/color-palettes.md`
- For font sizing requirements, see `references/font-guidelines.md`
- For input remapping specifications, see `references/input-devices.md`
- For feedback accessibility constraints, see `references/feedback-library.md`
- For the in-SKILL accessibility checklist, see the Accessibility Checklist in `SKILL.md`
