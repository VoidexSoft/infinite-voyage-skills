# Common Game UI Patterns

Reference guide for recurring UI patterns in game design. Each pattern includes structure,
best use cases, and trade-offs. Designed for Infinite Voyage but applicable across RPG and
action-adventure genres.

---

## 1. Radial Menus

A circular menu where options radiate outward from a center point. The player holds a button
to open the menu and aims toward a sector to select an option.

### Structure

```
        [Heal]
          |
  [Buff] --- [Attack]
          |
       [Defend]
```

### When to Use

- Quick-access actions during real-time gameplay (ability selection, item use)
- Situations where pausing breaks flow (action combat, exploration)
- When the option count is between 4 and 8

### Pros

- All options visible simultaneously without scrolling
- Selection is fast (aim + release)
- Works well with both mouse and analog stick
- Keeps the player in the game world (semi-transparent overlay)

### Cons

- Limited to roughly 8 items before sectors become too narrow
- Difficult to use with keyboard-only input (requires directional simulation)
- Touch screen accuracy drops with smaller sectors
- Not ideal for hierarchical or nested content

### Implementation Notes

- Sector highlight follows cursor or stick direction
- Release the trigger button to confirm selection
- Keyboard fallback: number keys 1-8 mapped to sectors clockwise from top
- Minimum sector angle: 45 degrees (8 items max)

---

## 2. Tab Navigation

Horizontal or vertical tabs that divide content into discrete categories. Only one tab's
content is visible at a time.

### Structure

```
[Character] [Inventory] [Skills] [Map] [Settings]
------------------------------------------------------
|                                                    |
|              Active Tab Content                    |
|                                                    |
------------------------------------------------------
```

### When to Use

- Menus with multiple distinct categories (inventory types, settings groups)
- When content within each category is self-contained
- Pause menus and full-screen overlays

### Pros

- Familiar pattern; low learning curve
- Scales to many categories (scroll tabs if needed)
- Each tab can have independent scroll state
- Clear visual indicator of current location

### Cons

- Only one category visible at a time (no cross-category comparison)
- Tab bar consumes screen space
- Deep nesting within tabs creates confusion
- Switching tabs can feel slow if content loads dynamically

### Implementation Notes

- Keyboard: Tab / Shift+Tab cycles through tabs
- Gamepad: LB / RB cycles tabs (standard convention)
- Active tab uses distinct color or underline
- Remember last-selected tab when reopening the menu

---

## 3. Inventory Grids

A grid of uniformly sized slots representing the player's carried items. Each slot holds
one item (or a stack) with an icon and optional quantity badge.

### Structure

```
[Sword] [Shield] [Potion] [Ring ]
[Helm ] [Armor ] [Boots ] [     ]
[Gem  ] [Scroll] [Key   ] [     ]
```

### When to Use

- Item management screens (equipment, crafting materials, loot)
- When the player needs a visual overview of many items at once
- Games with fixed inventory capacity (slot count = carry limit)

### Pros

- Compact representation of many items
- Drag-and-drop rearrangement feels natural
- Visual icons enable fast scanning without reading text
- Grid size directly communicates capacity

### Cons

- Small icons may be hard to distinguish (especially on consoles viewed from a couch)
- Grid navigation with a gamepad is slower than a list
- Tooltip or detail panel required to show item stats
- Irregular item sizes (2x1, 2x2 Tetris-style) increase complexity

### Implementation Notes

- Minimum slot size: 48x48px at 1080p (64x64px recommended for console)
- Hover tooltip shows item name, rarity, and primary stat
- Right-click or secondary button opens context menu (Equip, Drop, Compare)
- Empty slots should be visually distinct (dashed border, dimmed background)
- Keyboard: arrow keys navigate, Enter selects, Escape closes

---

## 4. Tooltip Systems

Floating information panels that appear on hover, focus, or long-press to provide details
about a UI element without navigating away.

### Structure

```
 ________________________
| Iron Sword             |
| Damage: 25             |
| Rarity: Common         |
| "A reliable blade."    |
|________________________|
```

### When to Use

- Supplementary information for items, abilities, status effects, or stats
- Anywhere the player might ask "what does this do?"
- In combination with grid inventories, skill trees, and stat screens

### Pros

- Provides detail without leaving the current screen
- Reduces visual clutter (information hidden until requested)
- Can include rich content (comparison stats, lore, icons)

### Cons

- Not accessible without hover capability (touch and gamepad need alternatives)
- Can obscure underlying content if poorly positioned
- Delay timing is critical (too fast = flickering, too slow = unresponsive)
- Players may not realize tooltips exist without prompting

### Implementation Notes

- Appear after 300ms hover delay; disappear after 200ms on mouse-out
- Gamepad: show tooltip for the focused/selected item automatically
- Touch: long-press (500ms) triggers tooltip; tap elsewhere dismisses
- Position logic: prefer appearing above or to the right; flip if near screen edge
- Anchor point follows the cursor but clamps to viewport bounds

---

## 5. Contextual Action Prompts

On-screen prompts that appear when the player is near an interactive object, showing the
available action and its bound input.

### Structure

```
        [E] Interact
        [F] Pick Up
```

### When to Use

- World interactions (doors, NPCs, loot, levers)
- Context-sensitive actions that change based on proximity or game state
- Replacing permanent on-screen buttons with situational prompts

### Pros

- Teaches controls organically through play
- Reduces HUD clutter (prompts only appear when relevant)
- Adapts label to current input device (shows keyboard key or gamepad button)
- Reinforces input bindings through repetition

### Cons

- Can crowd the screen if multiple interactables are nearby
- Players may miss prompts if they appear in a low-attention area
- Must update dynamically when the player rebinds controls
- Priority system needed when actions overlap

### Implementation Notes

- Display the prompt within 2 meters of the interactable (world space)
- Use the player's current input device icon (keyboard glyph or gamepad button)
- Priority order when multiple prompts overlap: story-critical > combat > loot > ambient
- Animate in with a quick fade (150ms); animate out when out of range
- Accessibility: pair icon with text label; never rely on icon alone

---

## 6. Quick-Select Wheels

A variant of the radial menu specifically designed for rapid item or weapon switching
during gameplay without pausing.

### Structure

```
      [Sword]
   [Staff] [Bow]
      [Axe]
```

### When to Use

- Weapon or loadout switching during combat
- Consumable item use (potions, scrolls, bombs)
- Emote or communication wheels in multiplayer

### Pros

- Faster than opening an inventory screen
- Supports muscle memory after repeated use
- Can slow or pause time while the wheel is open (design choice)
- Visually distinct from the full inventory

### Cons

- Same sector-size limits as radial menus (4-8 items)
- Players must pre-assign items to wheel slots
- Additional management layer (assigning items to wheel vs. just using inventory)
- Quick-select conflicts with other hold-button inputs

### Implementation Notes

- Hold a dedicated button (e.g., Q on keyboard, D-Pad on gamepad) to open
- Time-slow effect: reduce game speed to 25% while wheel is open
- Slots are player-configurable from the inventory screen
- Visual: show item icon, name, and remaining quantity
- Cooldown indicator overlaid on slot if item is on cooldown

---

## 7. Notification Systems

Transient messages that inform the player of events, rewards, status changes, or system
messages without requiring interaction.

### Types

| Type | Position | Duration | Example |
|------|----------|----------|---------|
| Toast | Top-right corner | 3-5 sec | "Achievement Unlocked: First Blood" |
| Banner | Top-center, full width | 2-4 sec | "New Area Discovered: Shadow Vale" |
| Inline | Near relevant HUD element | 2-3 sec | "+50 XP" next to XP bar |
| Queue | Stacked in corner | Sequential | Multiple loot pickups |

### When to Use

- Event announcements (level up, achievement, quest update)
- Loot and reward confirmation
- System alerts (auto-save, connection status, error messages)
- Social notifications in multiplayer (friend online, party invite)

### Pros

- Non-blocking; gameplay continues uninterrupted
- Can queue multiple notifications without overlapping
- Severity levels allow visual differentiation (info, warning, critical)
- Dismissible or auto-fading reduces distraction

### Cons

- Easy to miss during intense gameplay
- Too many notifications cause "notification fatigue"
- Must handle queue overflow (cap at 3-5 visible, queue the rest)
- Positioning must avoid covering critical HUD elements

### Implementation Notes

- Maximum 3 visible notifications; additional ones queue and appear as older ones fade
- Each notification type has a priority level (critical > quest > loot > social)
- Critical notifications (low health, disconnection) use center-screen placement
- Animate in from the edge (slide + fade, 200ms); animate out (fade, 300ms)
- Player setting: notification frequency (All, Important Only, Critical Only, None)
- Log all notifications in a viewable history (accessible from pause menu)

---

## 8. Progress Bars and Meters

Visual representations of quantities, progress, or thresholds using filled bars, arcs,
or segmented indicators.

### Variants

| Variant | Use Case | Example |
|---------|----------|---------|
| Linear bar | Health, mana, XP | `[||||||||--] 80%` |
| Segmented bar | Shield charges, lives | `[||] [||] [  ]` |
| Circular arc | Cooldown timers, compass | Clock-style fill |
| Stacked bar | Multi-resource display | HP over shield |

### When to Use

- Any numeric value the player must monitor during gameplay
- Cooldown timers on abilities
- Loading screens and quest progress
- Boss health indicators

### Pros

- Instantly readable without parsing numbers
- Color changes can signal thresholds (green > yellow > red)
- Animating the fill provides satisfying feedback
- Compact representation of proportional data

### Cons

- Exact values are hard to read (pair with numeric label for precision)
- Multiple bars can clutter the HUD
- Color alone must not convey meaning (accessibility)
- Non-linear values (logarithmic scaling) can mislead players

### Implementation Notes

- Always include a numeric value alongside the bar for accessibility
- Use threshold colors: above 60% green, 30-60% yellow, below 30% red
- Add secondary indicators: icons or text at each threshold
- Animate changes smoothly (lerp over 300ms) rather than jumping instantly
- For cooldowns, use a radial sweep (clock wipe) over the ability icon

---

## 9. Confirmation Dialogs

Modal overlays that require the player to confirm or cancel a significant or destructive
action before it executes.

### Structure

```
 _________________________________
| Are you sure you want to        |
| delete this save file?          |
|                                 |
| This action cannot be undone.   |
|                                 |
|    [DELETE]       [CANCEL]      |
|_________________________________|
```

### When to Use

- Destructive actions (delete save, drop rare item, quit without saving)
- Irreversible purchases or trades
- Actions with significant consequence (respec all skills, reset progress)

### Pros

- Prevents accidental loss of progress or items
- Gives the player a moment to reconsider
- Clear communication of consequences

### Cons

- Overuse creates "confirmation fatigue" (players click through without reading)
- Interrupts flow for frequent actions
- Must be designed so the "safe" option (Cancel) is the default/focused button

### Implementation Notes

- Default focus on the Cancel / safe option, not the destructive option
- Destructive button uses a warning color (red) with explicit label ("Delete", not "OK")
- Require a distinct input for confirmation (e.g., hold button for 1 second for permanent deletes)
- Keyboard: Escape always maps to Cancel; Enter maps to the focused button
- Never stack confirmation dialogs (one at a time)

---

## Pattern Selection Guide

| Scenario | Recommended Pattern |
|----------|-------------------|
| Quick ability use in combat | Radial Menu or Quick-Select Wheel |
| Browsing equipment categories | Tab Navigation |
| Managing 20+ items | Inventory Grid + Tooltips |
| Interacting with world objects | Contextual Action Prompts |
| Informing player of events | Notification System (Toast/Banner) |
| Monitoring health and mana | Progress Bars |
| Confirming destructive actions | Confirmation Dialog |
| Comparing two items side by side | Split Tooltip or Comparison Panel |
| Navigating deep settings | Nested/Hierarchical Menu (see SKILL.md) |
| Selecting from 3-6 visual options | Grid Menu (see SKILL.md) |

---

## Cross-References

- For menu structures (list, nested, grid), see the Menu System Patterns section in `SKILL.md`
- For input mappings per pattern, see `references/input-devices.md`
- For accessibility validation per pattern, see `references/accessibility-checklist.md`
- For color usage in UI patterns, see `references/color-palettes.md`
