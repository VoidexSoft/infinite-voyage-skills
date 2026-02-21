# Player Feedback Patterns Library

Catalog of feedback patterns for game development. Every player action should produce
immediate, proportional, multi-sensory feedback. This library defines reusable patterns
for visual, audio, and haptic feedback, along with intensity scaling rules and guidance on
positive versus negative feedback loops.

---

## 1. Visual Feedback Patterns

### Screen Shake

A brief displacement of the camera to communicate impact or danger.

| Parameter | Light | Medium | Heavy | Extreme |
|-----------|-------|--------|-------|---------|
| Displacement | 2-3px | 5-8px | 10-15px | 20-30px |
| Duration | 100ms | 200ms | 350ms | 500ms |
| Frequency | 30Hz | 25Hz | 20Hz | 15Hz |
| Decay | Linear | Ease-out | Ease-out | Exponential |

**Use cases:**
- Light: landing from a small jump, minor hit received
- Medium: standard melee attack landed, taking moderate damage
- Heavy: critical hit landed, explosion nearby
- Extreme: boss attack, massive environmental event

**Accessibility:** Must be reducible to 0% via Settings > Accessibility > Screen Shake slider.
At 0%, replace with a subtle vignette pulse instead.

### Screen Flash

A brief full-screen or partial-screen color overlay.

| Variant | Color | Opacity | Duration | Trigger |
|---------|-------|---------|----------|---------|
| Damage taken | Red `#E63946` | 30-50% | 200ms | Player loses HP |
| Heal received | Green `#2EC4B6` | 20-30% | 300ms | Player gains HP |
| Critical hit dealt | White `#FFFFFF` | 40-60% | 150ms | Player lands a crit |
| Level up | Gold `#E2B714` | 30-40% | 400ms | Player levels up |
| Shield break | Cyan `#85C1E9` | 25-35% | 250ms | Shield depleted |
| Stun received | Yellow `#F1C40F` | 40% | 300ms, pulsing | Player is stunned |

**Accessibility:** Flash effects must never exceed 3 flashes per second. Provide an option
to disable screen flashes entirely; replace with border glow or HUD indicator.

### Vignette Effects

Darkening or coloring the screen edges to communicate persistent states.

| State | Color | Intensity | Fade In | Fade Out |
|-------|-------|-----------|---------|----------|
| Low health (< 30%) | Red | 30-60% (pulses) | 500ms | 300ms when healed |
| Poisoned | Purple-green | 20-30% | 400ms | 300ms when cured |
| Underwater / suffocating | Blue-black | 40-70% (increases) | 1s | 500ms |
| Berserk mode | Red-orange | 20-30% | 300ms | 500ms |
| Safe zone / resting | Warm amber | 10-15% | 1s | 1s |

### Particle Effects

Short-lived particle bursts attached to characters, impacts, or UI elements.

| Event | Particle Type | Count | Lifetime | Color |
|-------|--------------|-------|----------|-------|
| Item pickup | Sparkle / star | 8-12 | 0.5s | Gold |
| Level up | Rising embers | 20-30 | 1.5s | Gold + white |
| Critical hit | Spark burst | 10-15 | 0.3s | White + weapon element color |
| Heal | Rising crosses / hearts | 6-10 | 1.0s | Green |
| Poison tick | Dripping bubbles | 4-6 | 0.8s | Purple-green |
| Death | Dissolve / scatter | 30-50 | 2.0s | Character color fading to gray |
| Shield activate | Hexagonal fragments | 12-18 | 0.5s | Cyan |
| Fire spell | Trailing embers | 15-25 | 1.0s | Orange-red gradient |

**Performance note:** Particle count should scale with graphics quality setting. Low quality
uses 50% particle count; Ultra uses 150%.

### Floating Text

Numeric or textual feedback that appears in world space and drifts upward before fading.

| Type | Color | Size | Motion | Duration |
|------|-------|------|--------|----------|
| Damage dealt | White `#FFFFFF` | 18-22px | Float up + slight random X | 1.0s |
| Critical damage | Yellow `#FFD700` | 26-32px, bold | Float up + scale pop | 1.2s |
| Healing | Green `#2EC4B6` | 18-22px | Float up | 1.0s |
| XP gained | Gold `#E2B714` | 16-18px | Float up to XP bar | 1.5s |
| Status applied | Status color | 14-16px | Float up | 0.8s |
| Miss | Gray `#9E9E9E` | 14px, italic | Drift + fade fast | 0.6s |
| Blocked | Cyan `#85C1E9` | 18px | Bounce back | 0.8s |

**Accessibility:** Floating text can be toggled off. When off, damage information is
communicated solely through health bar changes and HUD log.

---

## 2. Audio Feedback Patterns

### Hit Confirms

Audio cues that confirm an attack has connected with a target.

| Attack Type | Sound Character | Pitch | Duration | Volume |
|-------------|----------------|-------|----------|--------|
| Light melee | Sharp tap | 800-1200Hz | 50-100ms | 60% |
| Heavy melee | Deep thud | 200-400Hz | 150-250ms | 80% |
| Critical melee | Layered: thud + ring | 200Hz + 2000Hz | 200-300ms | 90% |
| Arrow/projectile | Soft thwip on launch, thud on impact | 600Hz / 300Hz | 100ms / 100ms | 70% |
| Magic spell | Ethereal whoosh + impact burst | 500-1500Hz sweep | 300-500ms | 75% |
| Blocked attack | Metallic clang | 1000-1500Hz | 100-150ms | 70% |
| Missed attack | Quiet whoosh (no impact) | 400-600Hz | 200ms | 40% |

### Level Up / Achievement

Celebratory audio for milestone events.

| Event | Sound Character | Duration | Notes |
|-------|----------------|----------|-------|
| Level up | Ascending arpeggio (C-E-G-C) | 1.0-1.5s | Layer with shimmering pad |
| Achievement unlocked | Fanfare (3-note brass) | 1.0s | Distinct from level up; memorable |
| Quest complete | Triumphant chord resolve | 1.5-2.0s | Warm, satisfying resolution |
| New ability learned | Magical chime cascade | 0.8-1.2s | Rising pitch sequence |
| Rare item found | Sparkle + low choir hit | 1.0-1.5s | Builds anticipation |
| Boss defeated | Orchestral stinger | 2.0-3.0s | Full, dramatic, uses game's motif |

### UI Navigation Sounds

Subtle audio feedback for menu interactions.

| Action | Sound | Pitch | Duration | Volume |
|--------|-------|-------|----------|--------|
| Hover / focus | Soft click | 400Hz | 30ms | 25% |
| Select / confirm | Medium click | 600Hz | 50ms | 40% |
| Cancel / back | Low tone | 250Hz | 80ms | 35% |
| Error / invalid | Buzz | 150Hz | 120ms | 50% |
| Tab switch | Soft slide | 500Hz sweep | 100ms | 30% |
| Slider adjust | Tick | 700Hz | 20ms per step | 20% |
| Toggle on | Rising pip | 600-800Hz | 60ms | 35% |
| Toggle off | Falling pip | 800-600Hz | 60ms | 35% |
| Open menu | Whoosh + settle | 300-500Hz sweep | 200ms | 40% |
| Close menu | Reverse whoosh | 500-300Hz sweep | 150ms | 35% |

### Environmental Audio Cues

Sounds that communicate game state without requiring visual attention.

| Cue | Sound | Behavior | Purpose |
|-----|-------|----------|---------|
| Low health | Heartbeat, increasing tempo | Loops; tempo scales with HP % | Urgency |
| Ability ready | Bright chime | Plays once when cooldown ends | Awareness |
| Enemy nearby | Low rumble or tension string | Fades in based on proximity | Alertness |
| Out of mana | Hollow empty sound | Plays on attempted cast | Resource awareness |
| Status expired | Soft deflation tone | Plays when buff/debuff ends | Status tracking |
| Save complete | Soft confirmation ding | Plays once | Reassurance |

---

## 3. Haptic Feedback Patterns

Haptic patterns for gamepad (vibration motors) and supported devices with advanced haptics
(DualSense adaptive triggers, HD Rumble).

### Basic Vibration Patterns

| Pattern Name | Left Motor | Right Motor | Duration | Use Case |
|-------------|-----------|------------|----------|----------|
| Light tap | 0% | 20% | 50ms | UI selection, item pickup |
| Medium pulse | 30% | 30% | 100ms | Ability cast, door open |
| Heavy impact | 60% | 80% | 200ms | Taking damage, landing heavy |
| Double tap | 20% / 20% | 20% / 20% | 50ms-50ms-50ms | Buff applied, notification |
| Sustained rumble | 15% | 15% | Continuous | Vehicle, environmental hazard |
| Escalating pulse | 10% to 80% | 10% to 80% | 500ms ramp | Charging attack, countdown |
| Heartbeat | 40%-0%-60%-0% | 40%-0%-60%-0% | 800ms cycle | Low health warning |

### DualSense Adaptive Trigger Patterns (PS5)

| Trigger State | Resistance | Use Case |
|---------------|-----------|----------|
| Free | No resistance | Normal movement, menu navigation |
| Light tension | 20% resistance at 50% pull | Drawing bowstring, aiming |
| Heavy tension | 60% resistance at 30% pull | Blocking with heavy shield |
| Click point | Resistance spike at 70% | Trigger pull (crossbow release) |
| Vibrating | Oscillating resistance | Reeling in fish, unstable terrain |

### HD Rumble Patterns (Nintendo Switch)

| Pattern | Description | Use Case |
|---------|-------------|----------|
| Rolling ball | Simulated rolling object | Puzzle rolling mechanic |
| Clicking | Rapid small taps | Lock picking, gear mechanism |
| Water flow | Gentle continuous oscillation | Swimming, water environment |
| Impact cascade | Multiple decreasing impacts | Chain reaction, domino effect |

---

## 4. Feedback Intensity Scaling

Feedback intensity should scale proportionally to the significance of the event.

### Scaling Matrix

| Event Significance | Screen Shake | Flash | Sound Volume | Haptic | Particles |
|-------------------|-------------|-------|-------------|--------|-----------|
| Trivial (UI click) | None | None | 25% | Light tap | None |
| Minor (small hit) | Light | Subtle | 50% | Medium | 5-8 |
| Moderate (ability) | Medium | Moderate | 70% | Medium | 10-15 |
| Major (critical) | Heavy | Strong | 85% | Heavy | 15-25 |
| Epic (boss/level up) | Extreme | Dramatic | 100% | Sustained | 25-50 |

### Dynamic Scaling Rules

1. **Damage proportional** -- Shake and flash scale with damage as a percentage of max HP.
   A 50% HP hit produces a stronger response than a 5% HP hit.
2. **Frequency dampening** -- Repeated identical feedback within 500ms reduces intensity by
   30% per repetition to prevent sensory overload. Resets after 2 seconds of no triggers.
3. **Stacking cap** -- Maximum 3 simultaneous feedback effects. Additional effects queue
   and play after the earliest effect ends.
4. **Player preference** -- Each feedback channel (visual, audio, haptic) has an independent
   intensity slider in settings (0% to 100%).
5. **Context adjustment** -- Feedback intensity reduces by 30% during cutscenes and
   dialogue to avoid disrupting narrative moments.

---

## 5. Positive Feedback Loops

Patterns that reward the player and reinforce desired behavior.

### Reward Escalation

| Action | First Time | Repeated | Streak (3+) |
|--------|-----------|----------|-------------|
| Enemy kill | Damage number + small chime | Same | Combo counter + escalating pitch |
| Item pickup | Sparkle + chime | Same (slightly quieter) | Multi-pickup swoosh + stacking count |
| Objective progress | Banner notification | Progress bar update | Milestone fanfare at 25/50/75/100% |
| Perfect dodge | Flash + whoosh | Same + style points | Slow-mo + dramatic sound |
| Combo hit | Hit confirm | Increasing pitch | Screen zoom + bass drop at max combo |

### Streak and Combo Feedback

As the player chains successful actions, feedback escalates:

1. **Hit 1-2:** Standard hit confirm audio + floating damage number
2. **Hit 3-5:** Audio pitch rises; particle count increases; combo counter appears
3. **Hit 6-9:** Screen edges glow; music intensity increases; haptic pulses sync to rhythm
4. **Hit 10+:** Full visual flourish; unique combo-finish sound; XP multiplier shown

### Satisfying Feedback Principles

- **Immediate:** Feedback arrives within 1 frame (16ms) of input for actions, within 100ms
  for state changes
- **Proportional:** Bigger action = bigger response (but never disruptive)
- **Layered:** Visual + audio + haptic together feel more rewarding than any single channel
- **Distinct:** Each action has a unique feedback signature; the player can identify the
  action by sound alone
- **Crescendo:** Repeated success builds toward a climax (combo finisher, streak bonus)

---

## 6. Negative Feedback Patterns

Patterns that communicate failure, danger, or penalty without frustrating the player.

### Damage and Failure Communication

| Event | Visual | Audio | Haptic |
|-------|--------|-------|--------|
| Minor damage | Red vignette (light) | Impact thud | Light pulse |
| Major damage | Red vignette (heavy) + shake | Heavy impact + grunt | Heavy impact |
| Status effect applied | Edge glow in status color | Debuff chime | Double tap |
| Death | Screen desaturates to gray | Music fades, low drone | Sustained rumble fading |
| Failed action | Element flashes red briefly | Error buzz | Quick double tap |
| Out of resource | Resource bar flashes | Empty/hollow sound | No haptic |
| Missed attack | No visual on target | Quiet whoosh | No haptic |

### Negative Feedback Guidelines

1. **Informative, not punishing** -- Negative feedback should tell the player what happened
   and suggest what to do differently, not just signal "you failed."
2. **Brief duration** -- Negative feedback fades faster than positive feedback. Pain
   lingers less than reward.
3. **No repeated stacking** -- If the player is taking continuous damage, use a sustained
   vignette rather than rapid repeated flashes.
4. **Recovery signal** -- When the negative state ends (healed, status cured), play a
   distinct "recovery" sound and visual to communicate the threat has passed.
5. **Escape clarity** -- During danger, the UI should highlight the path to safety
   (heal button glows, safe zone marked on minimap).

---

## 7. Feedback by Game Context

### Exploration

| Feedback | Intensity | Notes |
|----------|-----------|-------|
| Ambient audio | Low | Birdsong, wind, footsteps; builds atmosphere |
| Discovery chime | Medium | New area, hidden item found |
| Danger proximity | Low to medium | Music shifts, subtle controller vibration |
| Interaction prompt | Low | Soft pop-in sound for "[E] Interact" |

### Combat

| Feedback | Intensity | Notes |
|----------|-----------|-------|
| Hit confirms | Medium to high | Every attack landing feels impactful |
| Damage taken | Medium to high | Proportional to damage percentage |
| Ability effects | High | Spells and skills are visually dramatic |
| Kill confirm | Medium | Distinct from hit confirm; satisfying |
| Combo chain | Escalating | Builds with successful chains |

### Menu / Inventory

| Feedback | Intensity | Notes |
|----------|-----------|-------|
| Navigation | Very low | Soft clicks, minimal haptic |
| Selection | Low | Slightly louder click, light tap |
| Error / invalid | Low to medium | Brief buzz, no screen shake |
| Equip item | Low to medium | Satisfying "click into place" sound |
| Discard item | Low | Quiet thud, no celebration |

---

## 8. Feedback Implementation Checklist

For each player action in the game, verify:

- [ ] Visual feedback is immediate and proportional
- [ ] Audio feedback matches the action and does not overlap disruptively
- [ ] Haptic feedback is present for significant actions (optional for trivial ones)
- [ ] Feedback works with each channel disabled (sound off, haptics off, reduced motion)
- [ ] Positive feedback is more prominent than negative feedback
- [ ] No feedback exceeds the photosensitivity threshold (3 flashes/second)
- [ ] Player can adjust intensity per channel independently
- [ ] Repeated rapid actions dampen gracefully (no stacking overload)
- [ ] Feedback is distinct enough to identify the action without other context

---

## Cross-References

- For visual feedback colors, see `references/color-palettes.md`
- For haptic device capabilities, see `references/input-devices.md`
- For accessibility constraints on feedback, see `references/accessibility-standards.md`
- For HUD feedback integration, see `references/hud-case-studies.md`
- For detailed audio specs, see the Feedback Design section in `SKILL.md`
