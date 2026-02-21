# Input Device Reference

Comprehensive reference for input devices for game development. Covers keyboard and
mouse layouts, gamepad mappings for all major platforms, touch screen gestures, accessibility
controllers, simultaneous input handling, and input priority rules.

---

## 1. Keyboard + Mouse Layouts

### Standard WASD Layout (Default)

| Zone | Keys | Actions |
|------|------|---------|
| Movement | W/A/S/D | Forward / Left / Backward / Right |
| Camera | Mouse movement | Look around |
| Primary action | Left Mouse Button (LMB) | Attack / Interact (context) |
| Secondary action | Right Mouse Button (RMB) | Block / Aim / Alt interact |
| Middle mouse | Middle Mouse Button (MMB) | Lock-on target |
| Abilities | Q, E, R, F | Ability slots 1-4 |
| Sprint | Left Shift (hold or toggle) | Run faster, consume stamina |
| Crouch / Stealth | Left Ctrl | Toggle crouch |
| Jump | Space | Jump, double-tap for dodge roll |
| Interact | E (when not in combat) | Context prompt (talk, pick up, open) |
| Inventory | I | Open inventory screen |
| Map | M | Open world map |
| Journal / Quest | J | Open quest journal |
| Character sheet | C | Open character stats |
| Pause | Escape | Pause menu (always available) |
| Quick save | F5 | Save current game state |
| Quick load | F9 | Load last quick save |
| Screenshot | F12 / PrintScreen | Capture screen |
| UI scale up | Ctrl + Plus | Increase HUD/text scale |
| UI scale down | Ctrl + Minus | Decrease HUD/text scale |

### Arrow Keys Layout (Left-Handed Alternative)

| Zone | Keys | Actions |
|------|------|---------|
| Movement | Arrow keys | Directional movement |
| Abilities | Numpad 1-4 | Ability slots |
| Sprint | Right Shift | Run |
| Crouch | Right Ctrl | Toggle crouch |
| Jump | Numpad 0 | Jump |
| Interact | Numpad Enter | Context interact |
| Primary action | LMB | Attack |
| Secondary action | RMB | Block |

### One-Handed (Left Only)

| Zone | Keys | Actions |
|------|------|---------|
| Movement | W/A/S/D | Directional movement |
| Abilities | Q, E, R, F | Ability slots |
| Sprint | Left Shift | Run |
| Crouch | Left Ctrl | Crouch |
| Jump | Space | Jump |
| Attack | Tab | Primary attack (auto-aim enabled) |
| Interact | G | Context interact |
| Menu | Tilde (~) | Pause / menu |

### Mouse Button Modifiers

| Input | Standard | With Shift | With Ctrl |
|-------|----------|-----------|----------|
| LMB | Attack | Heavy attack | Aimed shot |
| RMB | Block / Aim | Parry (timed) | Cancel action |
| MMB | Lock-on | Cycle target | Release lock-on |
| Scroll up | Next weapon | Next ability | Zoom in (map) |
| Scroll down | Prev weapon | Prev ability | Zoom out (map) |
| Mouse 4 (side) | Quick item use | -- | -- |
| Mouse 5 (side) | Dodge roll | -- | -- |

---

## 2. Gamepad Mappings

### Xbox Controller

| Button | Action | Hold Action | Context Variation |
|--------|--------|-------------|-------------------|
| A | Jump / Confirm (menus) | -- | Interact (when prompted) |
| B | Dodge / Cancel (menus) | Crouch toggle | -- |
| X | Ability 1 / Reload | Heavy ability | -- |
| Y | Ability 2 / Use item | Switch weapon | -- |
| LB | Ability 3 | -- | -- |
| RB | Light attack | -- | -- |
| LT | Block / Aim | Charge block | -- |
| RT | Heavy attack | Charge attack | -- |
| Left Stick | Move | Click: Sprint toggle | -- |
| Right Stick | Camera | Click: Lock-on toggle | -- |
| D-Pad Up | Quick item 1 | -- | HUD toggle |
| D-Pad Down | Quick item 2 | -- | -- |
| D-Pad Left | Prev weapon | -- | -- |
| D-Pad Right | Next weapon | -- | -- |
| Start (Menu) | Pause menu | -- | -- |
| Select (View) | Map / Inventory | -- | -- |

### PlayStation Controller (DualSense / DualShock)

| Button | PS Label | Action |
|--------|----------|--------|
| Cross | X | Jump / Confirm |
| Circle | O | Dodge / Cancel |
| Square | Square | Ability 1 |
| Triangle | Triangle | Ability 2 |
| L1 | L1 | Ability 3 |
| R1 | R1 | Light attack |
| L2 | L2 | Block / Aim (adaptive trigger tension) |
| R2 | R2 | Heavy attack (adaptive trigger click) |
| L3 | L3 | Sprint toggle |
| R3 | R3 | Lock-on toggle |
| Touchpad press | Touchpad | Map toggle |
| Touchpad swipe | Touchpad | Gesture shortcuts (left=inventory, right=journal) |
| Options | Options | Pause menu |
| Create | Create | Screenshot / clip |

#### DualSense-Specific Features

- **Adaptive triggers:** L2 has tension for bow draw; R2 has a click point for heavy attacks
- **Haptic feedback:** HD haptics replace traditional rumble; see `references/feedback-library.md`
- **Speaker:** Short audio cues (item pickup chime) play through controller speaker
- **Light bar:** Reflects player health color (green > yellow > red)

### Nintendo Switch (Pro Controller / Joy-Cons)

| Button | Action | Notes |
|--------|--------|-------|
| A (right) | Confirm / Jump | Note: A/B positions swapped vs Xbox |
| B (bottom) | Cancel / Dodge | |
| X (top) | Ability 1 | |
| Y (left) | Ability 2 | |
| L | Ability 3 | |
| R | Light attack | |
| ZL | Block / Aim | |
| ZR | Heavy attack | |
| Left Stick | Move | Click: Sprint |
| Right Stick | Camera | Click: Lock-on |
| D-Pad | Quick items / weapon switch | |
| Plus (+) | Pause menu | |
| Minus (-) | Map / Inventory | |

#### Joy-Con Considerations

- Single Joy-Con mode: simplified control scheme with auto-aim and auto-block
- SL/SR buttons map to L/R for single Joy-Con play
- Motion controls: optional aiming via gyroscope (sensitivity adjustable)
- HD Rumble: same patterns as DualSense haptics (see feedback library)

---

## 3. Touch Screen Gestures

### Core Gesture Vocabulary

| Gesture | Action | Notes |
|---------|--------|-------|
| Tap | Interact / Confirm | Single tap on interactive elements |
| Double tap | Dodge roll | Quick double tap anywhere on movement side |
| Long press (500ms) | Inspect / Tooltip | Shows item details, NPC info |
| Swipe (left side) | Move | Virtual D-pad or floating joystick |
| Swipe (right side) | Camera look | Touch-drag to rotate view |
| Pinch | Zoom (map only) | Two-finger pinch on map screen |
| Two-finger tap | Block | Quick block during combat |
| Swipe up (right side) | Jump | Vertical swipe on camera side |
| Swipe down (right side) | Crouch | Vertical swipe down |
| Edge swipe (left) | Open inventory | Swipe from left screen edge |
| Edge swipe (right) | Open quest log | Swipe from right screen edge |
| Shake device | Optional: undo last action | Must be explicitly enabled |

### On-Screen Button Layout

```
 ___________________________________________
|                                           |
|  [Pause]  [Quest]  [Health Bar]  [Map]    |
|                                           |
|  [D-pad]                       [Ability1] |
|   area         GAME VIEW      [Ability2]  |
|                                [Attack]   |
|  [Sprint]                      [Block]    |
|                                [Jump]     |
|___________________________________________|
```

### Touch-Specific Rules

- Minimum touch target size: 48x48dp (per Material Design guidelines)
- Minimum spacing between adjacent buttons: 8dp
- Player can reposition all on-screen buttons (drag to customize layout)
- Opacity of on-screen controls: adjustable (20% to 100%)
- Auto-hide controls during cutscenes and dialogue

---

## 4. Accessibility Controllers

### Xbox Adaptive Controller

A flat, programmable controller with two large buttons and 19 jacks for external inputs.

| Feature | Support Requirement |
|---------|-------------------|
| Large buttons (A/B) | Map to primary and secondary action |
| External switch jacks | All 19 jacks must map to any game action |
| Co-pilot mode | Second controller supplements first (shared input) |
| Profiles | Support multiple saved mapping profiles |
| Latency | Same input latency as standard controller |

### Switch Access / External Switches

- Support scanning mode: automatic cycling through options with single-switch confirm
- Minimum: two-switch play (navigate + confirm)
- Optimal: four-switch play (up, down, select, back)
- Dwell time customizable (200ms to 2000ms)

### Eye Tracking

| Feature | Implementation |
|---------|----------------|
| Gaze-based cursor | Move cursor / selection with eye position |
| Dwell click | Stare at element for configurable duration to activate |
| Gaze + switch | Look at target, press switch to confirm |
| Calibration | In-game calibration wizard accessible from settings |
| Smoothing | Adjustable smoothing to reduce jitter (low/medium/high) |

### Voice Control

| Command | Action |
|---------|--------|
| "Attack" | Primary attack |
| "Block" | Block/defend |
| "Use [item name]" | Use named item from quick slots |
| "Open inventory" | Open inventory screen |
| "Pause" | Pause menu |
| "Select [option]" | Choose highlighted or named menu option |

---

## 5. Simultaneous Input Handling

The game must handle multiple input devices being active at the same time.

### Scenarios

| Scenario | Behavior |
|----------|----------|
| Keyboard + Gamepad plugged in | Use last active device for button prompts |
| Keyboard typing + mouse clicking | Both active simultaneously (standard PC) |
| Gamepad + mouse (Steam Deck) | Both functional; prompts follow last used |
| Touch + external keyboard (tablet) | Touch for gameplay; keyboard for chat/menus |
| Two gamepads | Player 1 and Player 2 assignment (if co-op supported) |
| Adaptive controller + standard | Co-pilot mode: inputs from both are merged |

### Device Detection

1. On startup, detect all connected devices
2. Display button prompts matching the most recently used device
3. Switch prompts within 500ms of detecting a different device input
4. Never lock the player to a single input device during gameplay
5. Settings menu shows input settings for all detected devices

### Prompt Icon Sets

Maintain icon sets for each supported device:

| Device | Icon Style | Example |
|--------|-----------|---------|
| Keyboard | Key cap shape with letter | `[E]`, `[Space]`, `[Shift]` |
| Xbox | Colored button shapes | Green A, Red B, Blue X, Yellow Y |
| PlayStation | Shape symbols | Cross, Circle, Square, Triangle |
| Switch | Letter buttons (ABXY, swapped) | A (right position), B (bottom) |
| Touch | Gesture icons | Tap hand, swipe arrow, pinch fingers |
| Generic gamepad | Numbered buttons | Button 1, Button 2, etc. |

---

## 6. Input Priority

When multiple inputs conflict or compete, the system resolves using priority rules.

### Priority Rules

| Rule | Description |
|------|-------------|
| Latest wins | For movement: last directional input overrides previous |
| Interrupt allowed | Dodge/block can interrupt attack wind-up |
| Queue system | Inputs during recovery frames are queued and execute after recovery |
| Menu priority | Menu inputs always take priority over gameplay inputs |
| System priority | Pause (Escape/Start) overrides all other inputs at all times |
| Debounce | Rapid repeated inputs are debounced at 50ms minimum interval |

### Input Buffer

- Buffer window: 200ms (configurable: 100-500ms in settings)
- Queued inputs: maximum 1 queued action (prevents accidental double actions)
- Cancel window: player can release a queued input within 100ms to cancel it
- Buffer display: optional visual indicator showing buffered action (for advanced players)

### Dead Zones

| Input | Default Dead Zone | Range |
|-------|------------------|-------|
| Left stick | 15% | 5-30% (adjustable) |
| Right stick | 10% | 5-30% (adjustable) |
| L2/R2 triggers | 5% | 0-20% (adjustable) |
| Mouse movement | 0 (no dead zone) | N/A |
| Touch drag | 10px minimum displacement | 5-20px (adjustable) |

---

## 7. Input Configuration Template

### Settings Screen Structure

```
Input Settings
  |-- Active Device: [Auto-Detect / Keyboard / Gamepad / Touch]
  |-- Button Prompts: [Auto / Keyboard / Xbox / PlayStation / Switch]
  |
  |-- Keyboard & Mouse
  |     |-- Key Bindings (full remapping table)
  |     |-- Mouse Sensitivity: [slider 0.1 - 5.0]
  |     |-- Mouse Acceleration: [Off / Low / Medium / High]
  |     |-- Invert Y Axis: [Off / On]
  |     |-- Raw Input: [Off / On]
  |
  |-- Gamepad
  |     |-- Button Bindings (full remapping table)
  |     |-- Stick Sensitivity: [slider 0.1 - 5.0]
  |     |-- Stick Dead Zone: [slider 5% - 30%]
  |     |-- Trigger Dead Zone: [slider 0% - 20%]
  |     |-- Invert Y Axis: [Off / On]
  |     |-- Vibration: [Off / On, intensity slider 0-100%]
  |     |-- Adaptive Triggers (PS5): [Off / On]
  |
  |-- Touch
  |     |-- Button Layout: [Default / Custom]
  |     |-- Button Size: [Small / Medium / Large]
  |     |-- Button Opacity: [slider 20% - 100%]
  |     |-- Gyroscope Aiming: [Off / On, sensitivity slider]
  |
  |-- Accessibility
  |     |-- Hold vs Toggle: [per-action setting]
  |     |-- Input Buffer Window: [slider 100-500ms]
  |     |-- Auto-Aim: [Off / Low / Medium / High]
  |     |-- Auto-Sprint: [Off / On]
  |     |-- Simplified Controls: [Off / On]
  |
  |-- Presets
        |-- Default
        |-- Left-Handed
        |-- One-Handed (Left)
        |-- One-Handed (Right)
        |-- Adaptive Controller
        |-- Custom Profile 1
        |-- Custom Profile 2
        |-- Custom Profile 3
        |-- [Reset to Default]
```

---

## 8. Platform-Specific Notes

| Platform | Key Consideration |
|----------|------------------|
| PC (Steam) | Support Steam Input API for universal controller remapping |
| PC (non-Steam) | Support XInput and DirectInput natively |
| PlayStation | Must use PS button labels and icons (certification requirement) |
| Xbox | Must use Xbox button labels (certification requirement) |
| Nintendo Switch | Handle A/B swap (A is confirm on Switch, B is confirm on some regions) |
| Mobile (iOS) | Support MFi controllers; respect system accessibility settings |
| Mobile (Android) | Support HID gamepads; respect TalkBack integration |
| Steam Deck | Treat as gamepad by default; support trackpad as mouse fallback |

---

## Cross-References

- For input mapping JSON template, see `templates/input-map.json`
- For haptic feedback patterns by device, see `references/feedback-library.md`
- For remapping accessibility requirements, see `references/accessibility-standards.md`
- For input-related onboarding prompts, see `references/onboarding-patterns.md`
- For the detailed input mapping tables, see the Input Mapping section in `SKILL.md`
