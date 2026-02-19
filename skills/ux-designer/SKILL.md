---
name: ux-designer
description: >
  UX/UI design specialist for Infinite Voyage. Use this skill whenever the user needs to design
  player interfaces, information architecture, interaction flows, onboarding experiences, accessibility
  systems, or user feedback. Trigger when designing menus, HUDs, control schemes, tutorial sequences,
  visual/audio feedback, screen layouts, or addressing player confusion about UI. Keywords that should
  trigger this skill: UI flow, wireframe, HUD design, menu system, input mapping, onboarding, tutorial,
  accessibility, colorblind mode, subtitles, feedback design, information architecture, screen layout,
  interaction design, player confusion, or any mention of "the UI feels cluttered" or "I don't know what
  this button does". This skill transforms gameplay clarity into structured, accessible, and responsive
  interface designs that serve the player's needs.
---

# UX/UI Designer

You are a UX architect who understands that great game interfaces are invisible—they serve the player's
needs without drawing attention to themselves. Every element has purpose. Every interaction provides
clarity. Every screen respects the player's cognitive load. Your designs ensure accessibility is built
in from the start, not bolted on later.

## Design Philosophy

### Responsive & Adaptive

Game interfaces must adapt to player context:

1. **Context-Aware Visibility** — Show relevant information only when needed; hide clutter
2. **Progressive Disclosure** — Introduce features gradually; don't overwhelm new players
3. **Responsive Scaling** — UI must work across screen sizes and aspect ratios
4. **Performance Priority** — UI rendering never impacts frame rate or input latency
5. **Player Control** — Players customize scale, opacity, position, and layout

### Readable & Clear

Information must be instantly understandable:

- **Hierarchy** — Most important information is largest, most prominent
- **Color coding** — Color reinforces meaning, not replaces it (colorblind-safe)
- **Consistency** — Same interactions always behave the same way
- **Feedback** — Every action produces immediate visual, audio, or haptic response
- **Affordance** — UI elements suggest their function through design

### Non-Intrusive & Immersive

UI should enhance immersion, not break it:

- **Minimalist design** — Remove unnecessary elements; embrace negative space
- **Diegetic UI** — UI lives in the game world when possible (HUD elements as character screens)
- **Non-diegetic clarity** — When UI must be on-screen, make it distinct and readable
- **Smooth transitions** — No jarring pop-ups; UI animates in/out
- **Aesthetic cohesion** — UI style matches game theme and visual language

### Accessible & Inclusive

Accessibility is design, not an afterthought:

- **No color-only information** — Always pair color with icon, text, or shape
- **Readable fonts** — At least 16px at 1080p; sans-serif for readability
- **High contrast** — Text must be readable by colorblind players and in bright sunlight
- **Customizable controls** — Every input mappable to player's preferred scheme
- **Assist features** — Difficulty options, subtitle/caption support, motion sensitivity
- **Feedback redundancy** — Visual + audio + haptic response on critical actions

## Core Workflow

### 1. Analyze Player Need

Before designing any screen:

1. **Define the interaction** — What does the player need to do? (e.g., "choose a weapon")
2. **Identify context** — When does this happen? In combat? In pause menu? During exploration?
3. **Clarify constraints** — Time pressure? Screen space? Accessibility requirements?
4. **Check existing patterns** — Have you designed something similar? Reuse patterns for consistency
5. **Set success criteria** — How will you know this design works? (completion speed, error rate, clarity rating)

### 2. Map User Flow

Create a flow diagram showing all paths through the interaction.

Use the **User Flow Template** (see section below). For each screen:
- What can the player do?
- What feedback do they get?
- What screen comes next?
- How can they undo/cancel?

### 3. Create Wireframes

Build low-fidelity layouts showing element placement and hierarchy.

Use the **Screen Specification Template** (see section below). For each screen:
- What are the key information zones?
- How is content organized?
- What are the interactive elements?
- What states exist (hover, pressed, disabled)?

### 4. Specify Interactions

Define exactly how each element behaves.

- Input handling — What inputs trigger what actions?
- State changes — What visual/audio feedback occurs?
- Transitions — How do screens open/close/animate?
- Edge cases — What happens on errors, timeouts, or invalid inputs?

### 5. Review Accessibility

Validate the design against accessibility standards.

Use the **Accessibility Checklist** (see section below). Test:
- Colorblind vision modes
- High contrast modes
- Input remapping
- Text readability
- Motion sensitivity

## User Flow Diagram Template

Map every screen and every decision point.

```mermaid
graph TD
    Start["Player Opens Menu"] --> Main["Main Menu Screen<br/>Options: Start, Continue, Settings, Quit"]

    Main -->|Click Start| Difficulty["Difficulty Selection<br/>Easy / Normal / Hard / Custom"]
    Main -->|Click Continue| Load["Loading Level"]
    Main -->|Click Settings| SettingsScreen["Settings Screen"]
    Main -->|Click Quit| Exit["Close Game"]

    SettingsScreen --> AudioSub["Audio Settings"]
    SettingsScreen --> GraphicsSub["Graphics Settings"]
    SettingsScreen --> ControlsSub["Controls & Accessibility"]
    SettingsScreen --> Back["Return to Main Menu"]

    AudioSub --> Back
    GraphicsSub --> Back
    ControlsSub --> Back

    Difficulty --> CharSelect["Character Selection<br/>3 character options"]
    CharSelect --> Confirm["Confirm Selection?<br/>Yes / No / View Stats"]
    Confirm -->|No| CharSelect
    Confirm -->|Yes| Load

    Load --> GameplayHUD["Gameplay HUD<br/>Health, Abilities, Minimap, Objectives"]

    GameplayHUD -->|Player Pauses| PauseMenu["Pause Menu<br/>Resume, Settings, Quit to Main"]

    PauseMenu -->|Resume| GameplayHUD
    PauseMenu -->|Settings| PauseSettings["Pause Settings<br/>Audio, Graphics, Controls"]
    PauseSettings --> PauseMenu
    PauseMenu -->|Quit| Main

    GameplayHUD -->|Level Complete| VictoryScreen["Victory Screen<br/>Score, Rewards, Next Level"]
    GameplayHUD -->|Player Dies| DeathScreen["Death Screen<br/>Retry, Quit, Load Last Checkpoint"]

    DeathScreen -->|Retry| GameplayHUD
    DeathScreen -->|Quit| Main
```

**Best practices:**
- One screen per node
- All possible paths shown
- Branch on user choice, not on hidden logic
- Mark loops (retry, back buttons)
- Identify dead ends (quit, level complete)

## Screen/Wireframe Specification Template

Every screen needs detailed documentation of layout, elements, and states.

```markdown
# Screen: [Name]

## Purpose
[What does this screen do? What decision does it support?]

## Context
- **When appears:** [Trigger—e.g., "After player pauses during gameplay"]
- **Previous screen:** [What comes before?]
- **Next screens:** [What comes after based on player choice?]
- **Duration:** [How long typically displayed? (e.g., "30 sec to 5 min")]

## Information Zones

Describe the layout as a grid or zones:

```
┌─────────────────────────────────────────┐
│ HEADER ZONE (Title, Time, Score)        │
├──────────────┬──────────────────────────┤
│ SIDEBAR      │ MAIN CONTENT AREA        │
│ (Menu Items) │ (Item List, Details)     │
│              │                          │
├──────────────┴──────────────────────────┤
│ FOOTER ZONE (Buttons: Confirm, Cancel)  │
└─────────────────────────────────────────┘
```

### Zone Breakdown

#### Header Zone
- **Height:** [e.g., 60px at 1080p]
- **Content:** [Title text, status info]
- **Elements:**
  - Title: 32px font, center-aligned, main color
  - Subtitle: 14px font, secondary text color
  - Status badge: Icon + text, top-right corner

#### Main Content Zone
- **Aspect:** [Scrollable / Fixed / Expandable]
- **Content:** [List of items, details panel, etc.]
- **Spacing:** [Margins, item padding]
- **Elements:** [Specific UI components]

#### Sidebar Zone
- **Width:** [e.g., 200px]
- **Content:** [Navigation menu, filters, options]
- **Behavior:** [Collapsible on mobile? Fixed position?]

#### Footer Zone
- **Height:** [e.g., 50px]
- **Content:** [Action buttons, cancel button]
- **Elements:** [Confirm, Cancel, Help buttons]

## Interactive Elements

### [Element Name 1]
- **Type:** [Button / Toggle / Slider / Text Input / Dropdown]
- **Label:** [Display text]
- **State:** [Default / Hover / Pressed / Disabled / Focus]
- **Action:** [What happens when interacted?]
- **Feedback:** [Visual change + Sound effect]
- **Accessibility:** [Keyboard shortcut, tooltip]

Example:
### Start Button
- **Type:** Button
- **Label:** "Start Game"
- **State:**
  - Default: Blue background, white text, 32px button height
  - Hover: Lighter blue, scale up 1.05x, cursor changes to pointer
  - Pressed: Darker blue, scale down 0.98x, click sound plays
  - Disabled: Gray background, 50% opacity, cursor not-allowed
- **Action:** Transition to character selection screen
- **Feedback:** Click sound (80dB, 0.2 sec), button flash
- **Accessibility:** Keyboard: Enter/Space to press; Tab to navigate

## States & Transitions

Describe how the screen changes based on player interaction or data:

### State: [Example: "Inventory Empty"]
- **Condition:** [When does this state occur?]
- **Visual change:** [What looks different?]
- **Content:** ["No items" message, empty list styling]
- **Behavior:** [Are elements disabled? Grayed out?]

### State: [Example: "Loading"]
- **Condition:** [Data is loading from server]
- **Visual change:** [Progress bar, loading spinner]
- **Content:** [Loading text, percentage]
- **Behavior:** [Buttons disabled, cancel option available]

### Transition: [Example: "Open to Close"]
- **Type:** [Fade / Slide / Scale / Rotate]
- **Duration:** [0.3 sec]
- **Easing:** [ease-out]
- **Sound:** [Optional sound effect name]

## Layout Responsiveness

How does this screen adapt to different screen sizes?

```markdown
| Screen Size | Layout | Notes |
|---|---|---|
| 1920x1080 | Full layout | All zones visible |
| 1280x720 | Two-column layout | Sidebar collapses to left edge |
| 960x540 | Single column, scrollable | Header + footer fixed, content scrolls |
| 540x960 | Mobile portrait | Sidebar moves to bottom tabs |
```

## Accessibility Checklist for This Screen

- [ ] Text readable at smallest supported resolution
- [ ] Color-blind safe (no red/green only)
- [ ] High contrast mode available
- [ ] All buttons keyboard accessible (Tab, Enter, Escape)
- [ ] Screen reader friendly (semantic HTML, alt text)
- [ ] No flashing content (motion sensitivity)
- [ ] Input remappable (not hardcoded to specific keys)
- [ ] Subtitle support for all audio content

## Wireframe Output

[ASCII art or linked image showing layout]

```
┌──────────────────────────────────┐
│      INVENTORY SCREEN            │
├──────────────────────────────────┤
│ [ < ] Category:Weapons   [ > ]   │
├─────────────┬────────────────────┤
│ Sword       │ Name: Iron Sword   │
│ Axe         │ Damage: 25         │
│ Bow         │ Rarity: Common     │
│ Shield      │ [EQUIP] [DROP]     │
├─────────────┴────────────────────┤
│ [CANCEL]           [CLOSE BAG]    │
└──────────────────────────────────┘
```

---

## Example: Ability Selection Menu

**Purpose:** Allow player to choose which ability to use in combat
**Context:** Appears during turn-based combat when player has multiple abilities
**Duration:** 5-30 seconds (player decides)

### Information Zones

```
┌────────────────────────────────────────┐
│ TITLE: "Choose Ability"      Cost: 25MP│
├────────────────────────────────────────┤
│ [ ] Attack (10 MP, Range 1)            │
│ [ ] Fireball (25 MP, Range 3, AoE)     │
│ [ ] Shield (15 MP, Self, Lasts 2 turn) │
│ [ ] Heal (20 MP, Target 1, +30 HP)     │
├────────────────────────────────────────┤
│ DESCRIPTION: "Rain fire on enemies"    │
│ [CONFIRM]               [CANCEL]       │
└────────────────────────────────────────┘
```

### Interactive Elements

#### Ability List Items
- **Type:** Selectable buttons
- **Label:** "Fireball (25 MP, Range 3, AoE)"
- **States:**
  - Default: Dark background, white text
  - Hover: Light blue background, arrow indicator appears
  - Selected: Blue border, yellow highlight, description updates
  - Disabled: Gray, 50% opacity (if player lacks MP)
- **Action:** Select ability, update description panel, enable CONFIRM button
- **Feedback:** Selection sound (275 Hz beep), description text animates in

#### Confirm Button
- **Type:** Button
- **Label:** "CONFIRM"
- **States:**
  - Default: Blue, enabled
  - Hover: Lighter blue, scale 1.05x
  - Pressed: Darker blue, play sound, execute ability
  - Disabled: Gray, 50% opacity (before selection)
- **Action:** Close menu, execute selected ability in combat
- **Feedback:** Confirmation sound (500 Hz, 0.3 sec), screen flash

### States

#### State: Not Selected
- **Condition:** No ability highlighted
- **Visual:** All items same style, description panel shows "Select an ability"
- **Buttons:** CONFIRM disabled

#### State: Selected
- **Condition:** Player highlighted an ability
- **Visual:** Selected item has blue border, description panel shows ability details
- **Buttons:** CONFIRM enabled

#### State: Unavailable MP
- **Condition:** Player lacks MP for an ability
- **Visual:** Item grayed out, red "Insufficient MP" text overlay
- **Buttons:** Can't select (clicking does nothing)

### Responsiveness

| Size | Layout |
|------|--------|
| 1920x1080 | Full width list, 4 items visible, large descriptions |
| 1280x720 | Full width list, 3 items visible, compact descriptions |
| 960x540 | Scrollable list, 2 items visible, minimal descriptions |

```

## HUD Design Principles

The HUD is the player's window into game state. It must communicate clearly without obscuring gameplay.

### Information Hierarchy

Design the HUD to show what matters most:

```markdown
## HUD Priority Zones

**Always visible (life-critical):**
- Player health / shields
- Active objective / target
- Resource needed for current action (ammo, MP, stamina)

**Visible in context:**
- Minimap (enemy positions, objectives)
- Ability cooldowns
- Equipment status

**Accessible but not always shown:**
- Damage numbers (optional, can disable for clarity)
- Sound visualization (for deaf/hard-of-hearing)
- Performance metrics (FPS, latency—debugging only)

**Hidden by default:**
- Chat log (only shown when player types)
- Full inventory (shown on pause or button press)
- Settings menu (overlay, pause-friendly)
```

### Adaptive Complexity

Adjust HUD density based on player state:

```markdown
## Adaptive HUD States

### Out of Combat
- Minimal HUD: Player health, objective marker only
- Large minimap visible (player exploring)
- Inventory accessible but not shown

### In Combat
- Full HUD: Health, shield, abilities, enemy status, cooldowns
- Minimap repositioned for visibility
- Damage numbers visible
- Target health bar appears above/below enemy

### Boss Battle
- Simplified HUD: Player health, boss health bar prominent
- Large health bars
- Phase indicator
- Objective text large and clear

### Cutscene / Dialogue
- HUD fades completely
- Only subtitle bar visible
- Skip prompt appears (subtle)
```

### Layout Patterns

Common HUD layouts for different game types:

#### Top-Down RPG
```
┌─────────────────────────────────┐
│ Minimap | Objective: Kill Boss  │
│         │ [████████░░] 75%      │
├─────────────────────────────────┤
│ HP: [██████░░░░] 60/100         │
│ MP: [████████░░] 80/100         │
│ Status: Poisoned (3 sec)        │
├─────────────────────────────────┤
│ [⚔ ATK]  [🛡 DEF]  [✨ SPELL]   │
│ [🎯]     [🏃]     [🔨]         │
└─────────────────────────────────┘
```

#### First-Person Shooter
```
┌─────────────────────────────────┐
│           MINIMAP               │
│        [Radar view]             │
├─────────────────────────────────┤
│          GAME VIEW              │
│   (Crosshair centered)          │
│   AMMO: 24/120                  │
│   HEALTH: 75                    │
│   OBJECTIVE: Defend point B     │
├─────────────────────────────────┤
│ [Weapon 1] [2] [3] [4] [5]      │
│ Ability: READY        [E]       │
└─────────────────────────────────┘
```

#### Puzzle / Adventure Game
```
┌─────────────────────────────────┐
│ Objective: Find three keys      │
│ Progress: [██░░░░░░░░] 1/3      │
├─────────────────────────────────┤
│                                 │
│         [Main Gameplay View]    │
│                                 │
│                                 │
├─────────────────────────────────┤
│ Current Puzzle: Door Locked     │
│ Hint: [?] Clue available        │
│ [INVENTORY] [MAP] [HINTS]       │
└─────────────────────────────────┘
```

## Menu System Patterns

Different menu structures for different needs.

### Radial Menu (Favorites/Quick Access)

```
      ↑ Ability 1
      |
← Ability 4 — [CENTER] — Ability 2 →
      |
      ↓ Ability 3

- Use for: Quick access in action-heavy moments
- Advantage: No scrolling, all options visible
- Accessibility: Keyboard (arrow keys/WASD), controller (stick directions)
- Max items: 4-8 comfortably
```

**Implementation:**
- Center cursor/selection point
- Highlight item user aims toward
- Click/press to select
- Escape key returns to game
- Keyboard: Arrow keys select, Space/Enter confirms

### Tabbed Menu (Multiple Categories)

```
┌──────────────────────────────────┐
│ [CHARACTER] [INVENTORY] [SKILLS] │
├──────────────────────────────────┤
│ Name: Hero                       │
│ Level: 12                        │
│ Class: Warrior                   │
│                                  │
│ Stats:                           │
│ STR: 18    DEX: 14   CON: 16    │
│ INT: 10    WIS: 13   CHR: 12    │
│                                  │
│ [CLOSE]                          │
└──────────────────────────────────┘
```

**Implementation:**
- Tabs visible at top/side
- Click tab to switch content
- Keyboard: Tab key cycles through tabs
- Controller: LB/RB cycles tabs
- Content within each tab is independently scrollable

### List Menu (Linear Selection)

```
┌────────────────────────────────┐
│ DIFFICULTY SELECTION           │
├────────────────────────────────┤
│ > EASY                         │
│   NORMAL                       │
│   HARD                         │
│   EXPERT                       │
├────────────────────────────────┤
│ Easy: Recommended for new      │
│ players. Enemies deal 50% less │
│ damage. Tutorial enabled.      │
│                                │
│ [SELECT]           [BACK]      │
└────────────────────────────────┘
```

**Implementation:**
- Scrollable list (or fit all items on screen)
- Arrow/highlight shows selection
- Up/down to navigate
- Enter to confirm
- Escape to go back

### Nested/Hierarchical Menu (Deep Options)

```
MAIN MENU
├─ Start Game
├─ Continue
├─ Settings
│  ├─ Audio
│  │  ├─ Master Volume: [████████░░] 80%
│  │  ├─ Music Volume: [██████░░░░] 60%
│  │  └─ SFX Volume: [█████░░░░░] 50%
│  ├─ Graphics
│  │  ├─ Resolution: 1920x1080
│  │  ├─ Quality: Ultra
│  │  └─ Brightness: [██████████] 100%
│  ├─ Accessibility
│  │  ├─ Colorblind Mode: Deuteranopia
│  │  ├─ Subtitle Size: Large
│  │  └─ Remappable Controls: ON
│  └─ [BACK]
└─ Quit
```

**Implementation:**
- Back button returns to parent menu
- Breadcrumb trail shows where you are: "Settings > Audio"
- Can use Enter/Escape to navigate or dedicated Back button
- Consistent layout as you navigate

### Grid Menu (Visual Selection)

```
┌─────────────────────────────────────┐
│ CHARACTER SELECTION                 │
├─────────────────────────────────────┤
│ [WARRIOR]  [MAGE]    [ROGUE]       │
│ ⚔ Melee   ✨ Magic  🗡 Agility    │
│                                     │
│ [KNIGHT]   [RANGER]  [CLERIC]      │
│ 🛡 Tank   🏹 Ranged  ✚ Support    │
├─────────────────────────────────────┤
│ Selected: WARRIOR                   │
│ Melee specialist. High damage,      │
│ medium durability.                  │
│ [CONFIRM]           [BACK]          │
└─────────────────────────────────────┘
```

**Implementation:**
- Arrange items in grid (2x3, 3x3, etc.)
- Arrow keys navigate grid
- Tab/Shift+Tab skips to next/previous grid
- Larger touch targets for mobile/controller
- Images + text for each option

## Input Mapping Table Template

Every game needs to map player inputs to game actions. Make it customizable.

```markdown
# Input Mapping: [Game Mode/Context]

## Default Keyboard Bindings

| Action | Primary | Secondary | Notes |
|--------|---------|-----------|-------|
| Move Forward | W | Up Arrow | Hold for continuous movement |
| Move Backward | S | Down Arrow | |
| Move Left | A | Left Arrow | |
| Move Right | D | Right Arrow | |
| Jump | SPACE | W (if already moving) | Tap for single jump, hold for higher |
| Attack / Interact | Left Mouse / E | Gamepad A | Context-sensitive |
| Ability 1 | Q | Gamepad X | |
| Ability 2 | R | Gamepad Y | |
| Ability 3 | F | Gamepad B | |
| Ultimate Ability | SHIFT | Gamepad LB | Long cooldown, powerful |
| Open Inventory | I | Gamepad SELECT | Pauses game |
| Open Map | M | Gamepad VIEW | Pauses game |
| Pause Menu | ESC / P | Gamepad START | |
| Crouch | CTRL | Gamepad LT + Move | Reduces visibility, enables stealth |
| Run / Sprint | SHIFT (hold) | Gamepad RT | Uses stamina |
| Switch Weapon | TAB / 1-4 | D-Pad Left/Right | Cycles weapons |
| Reload | R | Gamepad X | Weapon-dependent |
| Use Item | G | Gamepad Y | Consumes from inventory |
| Look Around (FPS) | Mouse Move | Right Stick | Invert Y axis option available |
| Lock On Target | Q (hold) | Gamepad LB (hold) | Combat-only |

## Gamepad Bindings

| Button | Action | Alternative |
|--------|--------|-------------|
| A | Jump | Interact |
| B | Crouch / Dodge | Context ability |
| X | Ability 1 | Use item |
| Y | Ability 2 | Reload |
| LB | Ability 3 | Lock-on |
| RB | Attack / Interact | Sprint |
| LT | Aim (FPS) / Defend | Charge attack |
| RT | Attack | Secondary action |
| Left Stick | Move / Look (FPS) | Customizable sensitivity |
| Right Stick | Look (3rd person) / Melee aim | Customizable sensitivity |
| D-Pad Up | UI navigation / Ability select | Change ability loadout |
| D-Pad Down | UI navigation / Ability select | Cycle subtitles on/off |
| D-Pad Left | Previous weapon | Emote wheel (if multiplayer) |
| D-Pad Right | Next weapon | Quick item use |
| START | Pause menu | Settings |
| SELECT | Inventory / Map | Quick stats |
| Left Stick Click | Melee attack (FPS alternative) | Interact |
| Right Stick Click | Sprint toggle | Secondary action |

## Touch Screen Bindings (Mobile)

| Action | Gesture | Notes |
|--------|---------|-------|
| Move | D-Pad (left side) or Swipe | Customizable position |
| Look Around | Swipe (right side) | Gyroscope alternative |
| Attack | Tap center | Single tap or double-tap |
| Ability 1-4 | Tap ability buttons (right side) | Customizable button size |
| Jump | Tap jump button (right side) | Can disable for platformers |
| Crouch / Stealth | Long-press move | Alternative: separate button |
| Menu | Tap menu button (top-left) | |
| Pause | Tap pause button (top-center) | |
| Inventory | Tap inventory button (top-right) | Can also swipe from edge |

## Accessibility Remapping Rules

- **Must be remappable:**
  - All action buttons (attack, jump, interact, abilities)
  - Menu navigation keys
  - Special accessibility toggles (subtitles, colorblind mode)

- **Cannot be remapped (for safety):**
  - Pause (ESC is sacred—always available)
  - Quick-exit (ALT+F4)
  - Screenshot (PrintScreen)

- **Recommended alternate bindings:**
  - WASD and Arrow Keys always both work
  - One-handed play: All essential actions on one side of keyboard
  - Controller: Support multiple gamepad types (XInput, DInput, PlayStation)

## Conflict Resolution

If player maps two actions to same button:
1. Show warning: "Action X already uses this button. Unbind first? [YES] [NO]"
2. Or auto-unbind the previous action
3. Visual indicator: Red "⚠" shows conflicted keybinds in settings

---

## Example: Combat Input Mapping (Action RPG)

**Context:** Active combat mode

| Action | Keyboard | Gamepad | Notes |
|--------|----------|---------|-------|
| Attack | Left Click | A button | Basic melee combo |
| Heavy Attack | Hold Left Click | A (2 sec) | Slower, more damage |
| Dodge Roll | SPACE (double-tap direction) | B + Direction | I-frames for 0.5 sec |
| Magic Spell | Q | X | Target-based, costs MP |
| Ranged Shot | R | Y | Aim with mouse/right stick |
| Block / Shield | Shift (hold) | LT (hold) | Reduces damage 50% |
| Swap Weapon | Tab | D-Pad Left/Right | 1 sec swap animation |
| Healing Item | G | LB + Y | Uses one item from inventory |
| Lock-On Target | Middle Mouse | RB | Locks rotation to enemy |
| Pause | ESC | START | |

```

## Onboarding Sequence Design

New players need guidance without feeling constrained. Use progressive disclosure and just-in-time learning.

### Progressive Disclosure Strategy

Introduce mechanics one at a time, never all at once.

```markdown
## Onboarding Flow: Infinite Voyage

### Phase 1: Basic Movement (2 minutes)
**Goal:** Player comfortable moving and looking around

1. Game starts. Fade in on player character in safe area.
2. Text prompt: "Use [W/Left Stick] to move forward"
   - Player can't advance until they move forward for 3 seconds
3. Prompt: "Use [A/D/Right Stick] to turn left and right"
4. Prompt: "Hold [SPACE/A Button] to sprint"
   - Safe area is small; player must explore to progress
5. First door appears ahead: "Press [E/X Button] to interact"

**Output:** Player exits safe room → enters tutorial level

### Phase 2: Basic Combat (5 minutes)
**Goal:** Player understands attack-defend cycle

1. Tutorial area shows weak training dummy.
2. Prompt: "Click [Left Mouse/A Button] to attack"
   - Player must hit dummy 3 times
   - Dummy doesn't attack back yet
   - Floating damage numbers show: "15 damage"
3. Prompt: "Hold [Shift/LT] to defend"
   - Dummy starts attacking (slow, telegraphed)
   - Player learns to block by necessity
4. Prompt: "Successful defense! Try a counter-attack"
   - Attack right after defending does bonus damage
5. Dummy defeated → tutorial progresses

**Output:** Player now understands attack/defend rhythm

### Phase 3: Special Abilities (3 minutes)
**Goal:** Player learns one signature ability

1. Level area with 3 weak enemies.
2. NPC appears: "That was good! Now try your special power."
3. Prompt: "Press [Q/X Button] to use Ice Bolt"
   - Ability outlined on screen with description
   - Shows cooldown timer (10 seconds)
   - Player must use it twice to understand cooldown
4. Enemies defeated easily with ability
5. Prompt: "Great! You learned Ice Bolt. You'll unlock more abilities as you level up."

**Output:** Player understands ability system

### Phase 4: Resource Management (2 minutes)
**Goal:** Player knows about health, mana, stamina

1. Tutorial boss appears.
2. Early in fight, player takes damage: "Your health is low!"
   - Red vignette effect activates
   - Health bar displayed prominently
3. Player runs, prompt: "Stamina is depleting. Rest to recover."
   - Player stops running, stamina regenerates (visual feedback)
4. Player tries ability: "Not enough mana! Use basic attacks instead."
   - This teaches resource scarcity naturally
5. Potion prompt: "Use healing potion with [G/Y]"
   - Player uses one potion
6. Tutorial boss defeated

**Output:** Player understands three resources and consequences

### Phase 5: Inventory & Equipment (2 minutes)
**Goal:** Player knows how to manage items

1. Boss defeated, drops loot.
2. Popup: "New item received! Press [I/SELECT] to open inventory"
   - Inventory appears with new sword highlighted
3. Prompt: "Unequip old weapon, equip new sword?"
   - Shows stat comparison
   - Confirm button highlighted
4. Sword equipped: "Your damage increased!"
5. Tutorial ends.

**Output:** Player ready for main game
```

### Just-in-Time Learning

Teach mechanics when the player needs them, not before.

```markdown
## Just-in-Time Teaching Rules

**GOOD**:
- Player encounters lock → "Press [R] to pick lock" prompt appears
- Player gets low health → Warning vignette + "Use [G] to heal"
- Player finds stealth opportunity → "Crouch [CTRL] to sneak"

**BAD**:
- Tutorial teaches lock-picking, then no locks for 10 minutes
- Tutorial teaches stealth, but game never requires stealth
- Game teaches 6 abilities at once, player only needs 1 for first hour

**Implementation:**
1. Identify which mechanic is needed NOW
2. Show minimal prompt (not a cutscene)
3. Let player figure it out through play
4. Only explain if they fail multiple times
5. Offer "Tips" option in pause menu for players who missed prompts
```

### Difficulty-Based Onboarding

Adjust tutorial intensity based on chosen difficulty.

```markdown
## Adaptive Onboarding

### Easy Difficulty
- All prompts visible
- Longer explanations
- Training dummy takes 1 hit instead of 3
- Boss tutorial fight is significantly easier
- Damage numbers are large and obvious
- Cooldown timers very visible

### Normal Difficulty
- Prompts appear but not overwhelming
- Standard explanations
- Training dummy normal difficulty
- Boss fight is challenging but beatable
- Damage numbers standard size
- Cooldown timers visible

### Hard Difficulty
- Minimal prompts (assume player knows genre)
- Brief explanations
- Training dummy is tougher
- Boss fight is very challenging
- Damage numbers optional (can disable)
- Subtle cooldown timers
- "Skip Tutorial" option available

### Custom Difficulty
- Player toggles tutorials on/off individually
- "I want to learn combat, but skip story" option
- Each system (combat, inventory, etc.) can be toggled
```

## Accessibility Checklist

Validate every design against these standards. None are optional.

### Visual Accessibility

- [ ] **Colorblind mode:** Deuteranopia (red-green), Protanopia (red-blind), Tritanopia (blue-yellow)
  - No information conveyed by color alone
  - Red/green pairs always paired with icon, text, or shape
  - HUD includes colorblind-safe palette

- [ ] **High contrast mode:** White/black text on dark/light backgrounds
  - Minimum 7:1 contrast ratio for normal text
  - Minimum 4.5:1 contrast ratio for large text (18px+)
  - Black outline on colored text if needed
  - Dark mode toggle available

- [ ] **Text size & readability:**
  - Minimum 16px at 1080p (scales appropriately)
  - San-serif font (Arial, Verdana, OpenSans)
  - Anti-aliasing enabled
  - Line height at least 1.5x font size
  - Maximum line length 60 characters (reading comfort)

- [ ] **UI scaling:**
  - HUD scale slider (50% - 200%)
  - Font scale slider (separate from HUD)
  - Applies to all screens and menus

### Audio Accessibility

- [ ] **Subtitles & captions:**
  - All dialogue has subtitles (including NPC names)
  - All UI feedback has sound effect legends (icon + name)
  - Subtitles always available, not just on mute
  - Speaker labels for multiplayer (e.g., "[ALLY SOLDIER]: Incoming!")
  - Subtitle size adjustable (3 levels: small, medium, large)
  - Subtitle positioning adjustable (top, center, bottom)

- [ ] **Sound visualization:**
  - Visual indicator for directional audio (mini HUD arrows)
  - Screenflash or visual effect for important sounds (low health warning, ability ready)
  - Icon legend for ability cooldown sounds
  - "Sound on/off" indicator in top corner

- [ ] **Audio volume customization:**
  - Master volume slider
  - Separate: Music, SFX, Dialogue, Ambient
  - Mono option (for hearing aids compatibility)
  - Audio compressor option (reduces loud spikes)

### Motor Accessibility

- [ ] **Customizable controls:**
  - All actions remappable (except sacred Pause key)
  - Preset profiles: WASD, Arrow Keys, Right-Handed, Left-Handed, One-Handed
  - No hardcoded button combinations (CTRL+ALT allowed only for universal functions)
  - Controller support: XInput and DInput

- [ ] **Motion sensitivity:**
  - Camera pan speed adjustable (0.5x - 2.0x)
  - No motion blur option
  - Camera acceleration toggle (for players with tremors)
  - Lock-on target option (reduces need for precise aiming)
  - Aim assist slider (20% - 100%)

- [ ] **Input alternatives:**
  - Single-button or two-button mode (if game supports it)
  - Hold vs. toggle for actions (e.g., run, crouch, aim)
  - Double-tap alternative to long-hold
  - No rapid-button-pressing requirements (or offer alternatives)

- [ ] **UI interaction:**
  - All buttons and selectable items large enough (minimum 44px height/width)
  - Clickable area extends beyond visual boundary
  - Tab navigation through all UI elements
  - Keyboard shortcuts visible (e.g., "[E]" next to "Interact")

### Cognitive Accessibility

- [ ] **Information clarity:**
  - Onscreen text limited (no wall-of-text dialogs)
  - Menus never deeper than 3 levels
  - All icons paired with text labels
  - Consistent button placement (Confirm always same position)
  - Optional complexity: Expert mode vs. Simple mode for menus

- [ ] **Tutorial flexibility:**
  - "Skip tutorial" option always available (even if encouraged against it)
  - "Redo tutorial" option in pause menu
  - Glossary/reference for jargon (in-game or quick Google)
  - Difficulty selector with clear descriptions

- [ ] **Objective clarity:**
  - Current objective always visible on HUD
  - Failed objective explains WHY (not just "FAILED")
  - Waypoint / compass points to next objective
  - Optional minimap shows destination

- [ ] **Animation & flashing:**
  - No autoplaying videos
  - Reduce motion option disables parallax, camera bob, screen shake
  - No flashing more than 3 times per second
  - Warnings before seizure-inducing effects (strobe, intense colors)

### Deaf & Hard of Hearing

- [ ] **Visual feedback required:**
  - Every important sound has a visual equivalent
  - Cooldown sounds → cooldown timer visual
  - Damage taken → red flash + vignette
  - Enemy nearby → mini-map indicator + text
  - Dialogue → subtitles + speaker name

- [ ] **Audio descriptions:**
  - Option for audio descriptions of important visual events
  - Narrative importance marked in subtitles

- [ ] **Captions for music / ambience:**
  - "[Dramatic orchestral music]" in cutscenes
  - "[Wind howling]" for environmental audio
  - "[Footsteps approaching]" for danger audio

### Neurodivergence

- [ ] **ADHD-friendly:**
  - Fast/skipable cutscenes (hold button to skip)
  - Objective clearly marked (no searching for next step)
  - Pause menu available anytime (no combat interruptions)
  - Notifications can be toggled (reduce pop-up fatigue)

- [ ] **Autism-friendly:**
  - Consistent UI patterns across all menus
  - Predictable enemy behaviors (same attack patterns)
  - Optional story summary before major scenes
  - Safe mode: No jump scares or sudden loud noises

- [ ] **Low-distraction mode:**
  - Disable: Animations, visual effects, screen shake, particle effects
  - Mute: Ambient sound, music (dialogue only)
  - Simple: Reduced HUD elements, larger text, reduced colors

### Cross-Disability Validation

- [ ] **Test with actual players:**
  - At least 1 player with each disability type
  - Not just assistive tech, but diverse input methods
  - Iterate based on feedback

- [ ] **Documentation:**
  - Accessibility features listed in game's main menu
  - Keybinds shown with accessibility notes
  - Known limitations listed (e.g., "Audio descriptions not available in multiplayer")

---

## Feedback Design

Every action needs feedback. Feedback can be visual, audio, and/or haptic.

### The Feedback Loop Principle

```
Player Action → Immediate Visual Feedback
             → Sound Effect (0.1-0.3 sec delay max)
             → Haptic Feedback (controller vibration, if available)
             → Status update (HUD change: ammo count, cooldown timer, etc.)
```

### Visual Feedback Examples

#### Button Press
```markdown
**Default state:**
- Color: Blue (#0066FF)
- Size: 80x40px
- Text: "ATTACK"
- Opacity: 100%

**Hover state:**
- Color: Lighter blue (#3399FF)
- Size: 82x42px (scale 1.025x)
- Text: Same
- Opacity: 100%
- Cursor: Pointer

**Pressed state:**
- Color: Darker blue (#003399)
- Size: 78x38px (scale 0.975x)
- Text: Same
- Opacity: 100%
- Duration: 0.1 sec (snap back to default)

**Disabled state:**
- Color: Gray (#666666)
- Size: 80x40px
- Text: Same, 50% opacity
- Opacity: 50%
- Cursor: Not-allowed (⊗)
```

#### Damage Taken
```markdown
**Visual response:**
- Full-screen red vignette (50% opacity) for 0.3 sec
- Screen shake (5px displacement, 0.3 sec duration)
- Player sprite flashes white (hit frame)
- Health bar decreases with animation
- Damage number appears above player: "-25" (red text, floats up and fades)

**Audio response:**
- Punch/impact sound: 500ms duration
- If health critical: Heartbeat sound starts looping

**Haptic response:**
- Controller rumble: Strong pulse (0.3 sec)
- Intensity matches damage (small hit = light rumble, heavy hit = strong rumble)
```

#### Ability Cast
```markdown
**Visual response:**
- Ability icon glows yellow (cast initiated)
- Projectile spawns and travels toward target
- Target hit: Impact effect (explosion, spell burst, etc.)
- Cooldown timer appears on ability icon (counts down)

**Audio response:**
- Cast sound: Magical whoosh (0.1 sec)
- Travel sound: Optional quiet sound following projectile
- Impact sound: Explosion or impact effect (0.3 sec)

**Haptic response:**
- Controller rumble on cast: Medium pulse
- Controller rumble on impact: Pattern based on effect (sharp pulse for explosion)
```

#### Resource Depletion
```markdown
**Low Mana Warning (when < 30% MP):**
- Mana bar turns orange (was blue)
- Screen pulses very subtly (0.5 sec cycle)
- Audio: Quiet alarm sound (looping 1-sec tone, low volume)
- Haptic: Gentle controller vibration (pulsing, 0.5 sec cycle)

**Out of Mana:**
- Mana bar turns red
- Icon for mana-dependent abilities fades out
- Screen pulse stops
- Audio: Sharp "error" beep (0.2 sec)
- Haptic: Single strong pulse

**Mana regenerates:**
- Mana bar animates filling
- Orange/red color fades to blue
- Audio: Subtle "chime" sound (0.3 sec)
- Haptic: Light pulse as regeneration starts
```

### Audio Feedback Examples

#### Sound Design Guidelines

```markdown
## SFX Categories

### UI Feedback (Low volume, non-intrusive)
- Button hover: Light "bleep" (400Hz sine wave, 0.1 sec)
- Button press: Slightly lower pitch "bloop" (250Hz, 0.15 sec)
- Menu open: Gentle "swoosh" (rising pitch, 0.2 sec)
- Menu close: Falling pitch "swoosh" (0.2 sec)
- Error/invalid action: "Buzzer" sound (low frequency, 0.3 sec)

### Gameplay Feedback (Medium volume)
- Hit enemy: Impact sound (varies by weapon: thud, slash, etc.)
- Player hit: Sharp pain sound or "ouch" vocalization
- Ability cast: Magical or mechanical sound matching ability
- Ability impact: Explosive or magical burst sound
- Pickup item: Chime or "sparkle" sound (250-400Hz, 0.3 sec)
- Level up: Ascending arpeggio (0.5 sec)

### Critical Feedback (High volume, attention-getting)
- Low health warning: Heartbeat sound (looping, gets faster as HP drops)
- Enemy nearby: Alert beep (600Hz, 0.2 sec, repeating)
- Boss nearby: Deep warning tone (100Hz, 0.5 sec, repeating)
- Objective complete: Triumphant fanfare (1-2 sec)

### Ambient Feedback (Background)
- Passive cooldown countdown: Subtle ticking (low volume, only when < 2 sec remain)
- Passive resource regeneration: Quiet ambient tone (very low volume)
```

### Haptic Feedback Patterns

Not all actions need haptics—use them for critical feedback.

```markdown
## Haptic Trigger Examples

### Single Pulse (Light)
- Button press, menu selection, item pickup
- Duration: 50ms
- Intensity: 20%

### Double Pulse (Medium)
- Ability used, ability cooldown reached, buff applied
- Duration: 100ms total (50ms pulse, 50ms silence, 50ms pulse)
- Intensity: 40%

### Strong Pulse (Heavy)
- Player hit, taking damage, taking heavy damage, low health warning
- Duration: 200ms
- Intensity: 60-100% (scale with damage)

### Rumble Pattern (Engine Vibration)
- Engine running, vehicle moving, earthquake effect
- Duration: Continuous or long
- Intensity: Variable (20-60%)
- Use: Background vibration, not foreground attention

### Rhythmic Pulse (Attention)
- Boss phase transition, critical warning, imminent death
- Duration: 500ms repeating pattern
- Pattern: 200ms on, 100ms off, 200ms on
- Intensity: 50%
```

### Feedback Checklist

For each interaction in the game:

```markdown
- [ ] Visual feedback: Immediate and clear
- [ ] Audio feedback: Non-intrusive, matches action type
- [ ] Haptic feedback: Used for critical actions (optional for less critical)
- [ ] Accessibility: Works with sound off, vibration off, reduced motion
- [ ] Hierarchy: Most important action has strongest feedback
- [ ] Clarity: Feedback clearly communicates success or failure
- [ ] Performance: Feedback doesn't cause frame drops or input lag
```

## Integration with Other Skills

### Game Balancer

**From game-balancer:**
- Ability cooldown durations and values
- Damage numbers and scaling formulas
- Difficulty settings and stat scaling

**To game-balancer:**
- Request feedback: "Add cooldown timer to HUD for clarity"
- Flag design issues: "Health bar too small at 1080p—hard to read"
- Ask for balance verification: "Does this 2.5-second cooldown feel too long?"

### Narrative Designer

**From narrative-designer:**
- Dialogue text (for subtitle display)
- Character names (for speaker labels)
- Story beats (for objective markers)

**To narrative-designer:**
- Request subtitle timing: "This cutscene needs captions at 0:15 and 0:32"
- Ask for narrative clarity: "Should this tutorial text be two sentences or four?"
- Flag story UI hooks: "Dialogue option 1 is too long—give me shorter text or I'll cut it"

### Systems Designer

**From systems-designer:**
- Mechanic definitions and player actions
- Environmental interaction rules
- Feedback system capabilities (can it vibrate? Has 3D audio?)

**To systems-designer:**
- Request new feedback: "Can we add haptic feedback to ability casts?"
- Ask for system clarification: "How many simultaneous sounds can the engine handle?"
- Flag interaction issues: "Lock-picking mechanic has unclear feedback on success/failure"

### Level Designer

**From level-designer:**
- Encounter types and enemy counts
- Environment hazards and safe zones
- Progression gates and unlock triggers

**To level-designer:**
- Provide HUD layouts for each level type
- Request UI context: "Combat HUD or exploration HUD for this zone?"
- Flag navigation clarity: "Players getting lost—add objective waypoint on minimap"

### Asset Spec

**From asset-spec:**
- Icon specifications and sizes
- Font styles and weights
- Color palettes and visual guidelines

**To asset-spec:**
- Request assets: "Need 24x24px and 48x48px icons for all abilities"
- Ask for specifications: "What's the maximum text height in UI panels?"
- Flag asset issues: "This icon doesn't read clearly at small scale—redesign or enlarge"

## HTML/SVG Wireframe Output Capability

Wireframes can be exported as interactive HTML or static SVG for review and hand-off.

### HTML Wireframe Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Infinite Voyage - Inventory Screen Wireframe</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Arial', sans-serif;
            background: #1a1a1a;
            color: #fff;
            padding: 20px;
        }

        .wireframe {
            max-width: 1200px;
            margin: 0 auto;
            background: #2a2a2a;
            border: 2px solid #444;
            border-radius: 8px;
            overflow: hidden;
        }

        .header {
            background: #0066ff;
            padding: 20px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
        }

        .content {
            display: grid;
            grid-template-columns: 200px 1fr;
            min-height: 400px;
        }

        .sidebar {
            background: #1a1a1a;
            border-right: 1px solid #444;
            padding: 20px;
        }

        .menu-item {
            padding: 10px;
            margin-bottom: 8px;
            background: #333;
            cursor: pointer;
            border-radius: 4px;
            transition: background 0.2s;
        }

        .menu-item:hover {
            background: #0066ff;
        }

        .menu-item.active {
            background: #0066ff;
            border-left: 3px solid #00ccff;
        }

        .main-panel {
            padding: 20px;
            overflow-y: auto;
        }

        .item-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
            gap: 10px;
            margin-bottom: 20px;
        }

        .item-slot {
            aspect-ratio: 1;
            background: #333;
            border: 2px solid #555;
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s;
            font-size: 12px;
            text-align: center;
            padding: 5px;
        }

        .item-slot:hover {
            border-color: #0066ff;
            background: #444;
        }

        .item-slot.selected {
            border-color: #00ccff;
            background: #1a3a5a;
        }

        .footer {
            background: #1a1a1a;
            border-top: 1px solid #444;
            padding: 15px;
            display: flex;
            gap: 10px;
            justify-content: center;
        }

        button {
            padding: 10px 20px;
            font-size: 14px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.2s;
            font-weight: bold;
        }

        .btn-primary {
            background: #0066ff;
            color: white;
        }

        .btn-primary:hover {
            background: #0052cc;
        }

        .btn-secondary {
            background: #555;
            color: white;
        }

        .btn-secondary:hover {
            background: #666;
        }

        .notes {
            margin-top: 30px;
            padding: 15px;
            background: #2a2a2a;
            border-left: 3px solid #0066ff;
            border-radius: 4px;
        }

        .notes h3 {
            margin-bottom: 10px;
            color: #00ccff;
        }

        .notes p {
            font-size: 14px;
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <div class="wireframe">
        <div class="header">Inventory Screen</div>

        <div class="content">
            <div class="sidebar">
                <div class="menu-item active">Weapons</div>
                <div class="menu-item">Armor</div>
                <div class="menu-item">Consumables</div>
                <div class="menu-item">Quest Items</div>
                <div class="menu-item">Misc</div>
            </div>

            <div class="main-panel">
                <h2>Weapons (12/20)</h2>
                <div class="item-grid">
                    <div class="item-slot selected">Iron Sword</div>
                    <div class="item-slot">Fire Sword</div>
                    <div class="item-slot">Bow</div>
                    <div class="item-slot">Dagger</div>
                    <div class="item-slot">Staff</div>
                    <div class="item-slot">Hammer</div>
                </div>

                <h3>Iron Sword</h3>
                <p><strong>Damage:</strong> 25</p>
                <p><strong>Rarity:</strong> Common</p>
                <p><strong>Description:</strong> A reliable blade. Good against most enemies.</p>
                <button class="btn-primary">Equip</button>
                <button class="btn-secondary">Drop</button>
            </div>
        </div>

        <div class="footer">
            <button class="btn-primary">Close Inventory</button>
            <button class="btn-secondary">Back</button>
        </div>
    </div>

    <div class="notes">
        <h3>Design Notes</h3>
        <p>This wireframe shows the inventory screen with sidebar navigation and main item grid.
        Selected item shows stats and action buttons. Mobile version would stack sidebar and main panel vertically.</p>
    </div>
</body>
</html>
```

### Mermaid Diagram Output

Use Mermaid for quick flow diagrams:

```mermaid
graph LR
    A["Main Menu<br/>Start / Continue / Settings"]
    B["Character Select<br/>Choose Class"]
    C["Difficulty Select<br/>Easy / Normal / Hard"]
    D["Game Loading"]
    E["Gameplay HUD<br/>Health / Abilities / Minimap"]

    A -->|Start| B
    B --> C
    C --> D
    D --> E

    E -->|Pause| F["Pause Menu<br/>Resume / Settings / Quit"]
    F -->|Resume| E
    F -->|Settings| G["Settings Screen"]
    G --> F
    F -->|Quit| A
```

## References

- `references/ui-patterns.md` — Common UI patterns and when to use them
- `references/accessibility-standards.md` — WCAG guidelines and game-specific standards
- `references/color-palettes.md` — Colorblind-safe color schemes
- `references/font-guidelines.md` — Readable fonts and sizing at various resolutions
- `references/feedback-library.md` — Archive of sound effects and haptic patterns
- `references/input-devices.md` — Controller, keyboard, and touch mapping standards
- `references/hud-case-studies.md` — Analysis of great HUDs from other games
- `references/onboarding-patterns.md` — Successful tutorial flow examples
- `references/accessibility-checklist.md` — Full validation checklist before shipping

## Output Format

UX/UI designs go to the GDD UI/UX section. Additionally:

- **Screen specifications** → Markdown format for documentation
- **Wireframes** → HTML for interactive review or SVG for hand-off to art team
- **User flows** → Mermaid diagrams exported as PNG/SVG
- **Input mappings** → JSON format for engine import (see `templates/input-map.json`)
- **Accessibility reports** → Checklist with test results and recommendations
- **Feedback specs** → Audio/haptic library linked to specific actions
- **Integration notes** → Linked references to narrative, balance, and systems teams
