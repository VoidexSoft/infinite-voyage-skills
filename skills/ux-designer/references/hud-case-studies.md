# HUD Design Case Studies

Analysis of HUD design approaches from notable games, with lessons applicable to Infinite
Voyage. Each case study examines the design philosophy, information density, player context
adaptation, and trade-offs. Use these studies when making HUD decisions for different
gameplay contexts.

---

## 1. Minimal HUD -- The Legend of Zelda: Breath of the Wild

### Philosophy

Show as little as possible. Trust the player to learn through environmental cues and
discovery. The world itself communicates most of the information.

### What Is Displayed

| Element | Visibility | Position |
|---------|-----------|----------|
| Hearts (health) | Always | Top-left |
| Stamina wheel | Only when stamina is being used | Center, around character |
| Mini-map | Always (small, subtle) | Bottom-right |
| Temperature gauge | Only in extreme environments | Next to mini-map |
| Noise indicator (stealth) | Only when crouching | Near character |
| Weapon/shield/bow | Always (small icons) | Top-right |
| Rune ability icons | Always (small) | Top-right, below weapons |

### What Is NOT Displayed

- No XP bar (no traditional leveling)
- No damage numbers
- No enemy health bars (enemies just react to hits)
- No quest markers on the main view (only on map)
- No ability cooldown timers (visual cooldown on rune icons only)

### Information Density

Very low. Roughly 5-8% of the screen is covered by HUD elements at any given time. The
remaining 92-95% is pure gameplay view.

### Pros

- Maximum immersion; the world feels real and uncluttered
- Player focuses on exploration and environment rather than UI indicators
- Encourages experimentation and discovery
- Clean aesthetic matches the game's visual design
- Reduces cognitive load during traversal

### Cons

- New players may feel lost without explicit guidance
- Health is communicated only through hearts (no numeric precision)
- Players must open the menu to check detailed stats, inventory, or quest status
- Requires strong environmental design to compensate for missing HUD information
- Less effective for complex RPGs with many stats and statuses to track

### Key Lessons

- Use a minimal HUD during exploration mode; expand it during combat
- Environmental storytelling can replace HUD indicators (glowing paths, NPC reactions)
- Keep hearts/health simple in the HUD; detailed stats live in the menu
- Consider a "HUD opacity" slider that lets players choose their comfort level

---

## 2. Diegetic HUD -- Dead Space

### Philosophy

All UI elements exist within the game world. The HUD is part of the character's equipment,
making it feel physically real.

### Diegetic Elements

| Element | In-World Representation |
|---------|------------------------|
| Health | Glowing spine indicator on the character's back (segmented bar) |
| Stasis energy | Circular meter on the character's suit |
| Ammo count | Holographic projection from the weapon |
| Inventory | Holographic projection in front of the character |
| Map | Holographic floor projection |
| Objective line | Glowing line projected onto the ground |
| Messages / logs | Holographic playback from audio/video devices in the world |

### What Makes It Work

- The game never pauses for menus (inventory is real-time, increasing tension)
- Health is visible to the player by looking at the character (third-person view)
- The holographic aesthetic matches the sci-fi setting perfectly
- Audio logs play through the character's suit speakers (in-world sound)

### Information Density

Low to medium. Information is present but distributed across the game world rather than
concentrated in screen corners. The player must physically look at their character or
weapon to check status.

### Pros

- Extremely immersive; no "game UI" visible at any time
- Horror tension increases because menus do not pause the game
- Unique and memorable aesthetic identity
- No screen clutter; every pixel shows the game world

### Cons

- Requires third-person camera (hard to see spine health in first-person)
- Information can be obscured by camera angle, lighting, or enemies
- Less accessible for players who need clear, always-visible indicators
- More expensive to develop (every UI element requires 3D modeling and animation)
- Does not scale well to complex RPGs with dozens of status effects
- Reading holographic text at a distance (console/TV) can be challenging

### Key Lessons

- Consider diegetic elements for specific systems (e.g., a magical compass for navigation)
- Do not make ALL UI diegetic in an RPG; the stat complexity is too high
- Use diegetic audio (characters speaking) instead of text pop-ups where possible
- Diegetic elements should supplement, not replace, traditional accessible HUD options

---

## 3. Classic RPG HUD -- Final Fantasy XIV / World of Warcraft

### Philosophy

Show everything the player needs at all times. The HUD is a dashboard for managing complex
systems: health, mana, buffs, debuffs, party status, enemy status, ability cooldowns, chat,
and more.

### Typical Elements

| Element | Position | Details |
|---------|----------|---------|
| Player health/mana bars | Top-left or center-bottom | Numeric + bar |
| Target health bar | Top-center | Enemy name, level, health |
| Party member list | Left side | Names, health bars, status icons |
| Hotbar (abilities) | Bottom-center | 12+ ability slots with cooldown overlays |
| Secondary hotbar | Above primary | Additional abilities or items |
| Minimap | Top-right | Rotates with player; shows objectives |
| Chat log | Bottom-left | Text chat, system messages, combat log |
| Buff/debuff icons | Near health bar | Small icons with duration timers |
| Quest tracker | Right side | Current objectives, progress |
| Experience bar | Bottom, full width | XP progress to next level |
| Gil/currency | Near minimap | Current funds |
| Compass / zone name | Top-center | Current zone label |

### Information Density

Very high. Up to 25-40% of the screen can be covered by HUD elements. Hardcore players
often add even more custom elements (damage meters, threat meters, custom timers).

### Pros

- All critical information is immediately available; no menu diving needed
- Supports complex gameplay with many simultaneous systems (tank, heal, DPS roles)
- Highly customizable (most MMOs allow full HUD layout editing)
- Party and raid coordination relies on visible status information
- Combat log provides precise data for optimization-minded players

### Cons

- Overwhelming for new players; steep learning curve
- Screen clutter reduces immersion
- Difficult to read at console/TV viewing distances
- Requires significant player investment to customize the layout
- Can cause information overload and decision paralysis

### Key Lessons

- Provide a dense HUD mode for players who want detailed combat data
- Default to a simpler layout; let advanced players add elements
- Customization is key: let players move, resize, and toggle every element
- Use progressive disclosure: unlock HUD elements as the player unlocks game systems

---

## 4. Adaptive HUD Systems

An adaptive HUD changes its display based on the player's current context. This is the
recommended approach.

### Context-Based Display Rules

| Context | HUD State | Elements Shown |
|---------|-----------|----------------|
| Exploration (no enemies) | Minimal | Health (if not full), minimap, objective marker |
| Approaching interactable | Minimal + prompt | Add interaction prompt |
| Combat initiated | Full combat | Health, mana, stamina, abilities, enemy health, buffs/debuffs |
| Low health (< 30%) | Urgent | Health bar pulses, vignette, heal prompt highlighted |
| Boss encounter | Boss focus | Simplified: player health + boss health bar (large) |
| Dialogue / cutscene | Hidden | All HUD fades; subtitles only |
| Menu / inventory | Full overlay | Game paused; full menu system visible |
| Photo mode | Clean | All HUD hidden; camera controls only |

### Transition Rules

- HUD elements fade in/out over 300-500ms (not instant)
- Combat HUD appears 500ms after first enemy detection
- Combat HUD lingers 5 seconds after last enemy defeated, then fades
- Low-health indicators activate immediately (no delay)
- Player can force full HUD with a toggle key (default: H on keyboard)

### Pros

- Best of both worlds: minimal during exploration, detailed during combat
- Reduces clutter without sacrificing information access
- Adapts to the player's current need without manual configuration
- More immersive than a static dense HUD

### Cons

- Requires careful tuning of trigger conditions and transition timing
- Players may be surprised when elements appear or disappear
- Edge cases: what if the player is in combat but also in a dialogue?
- Must provide a manual override for players who prefer a static HUD

### Implementation Approach

```
Exploration Mode
  Visible: minimap, objective marker, health (if damaged)
  Hidden: abilities, mana, enemy info, damage numbers
  Trigger: No enemies within detection range

  --> Enemy detected (within 30m)

Combat Mode
  Visible: health, mana, stamina, ability bar, enemy health, status effects
  Hidden: quest tracker (shifts to corner), detailed minimap
  Trigger: Enemy aggro or player attacks

  --> All enemies defeated + 5s delay

Exploration Mode (return)
  Transition: Combat elements fade out over 500ms
```

---

## 5. Comparison Matrix

| Aspect | Minimal (BotW) | Diegetic (Dead Space) | Classic RPG (FFXIV) | Adaptive |
|--------|---------------|----------------------|--------------------|-----------|
| Screen coverage | 5-8% | 0-5% (in-world) | 25-40% | 5-30% (varies) |
| Immersion | Very high | Extremely high | Low-medium | High |
| Information access | Low (must open menus) | Low-medium | Very high | Medium-high |
| New player friendliness | Medium (discovery) | Low (unfamiliar) | Low (overwhelming) | High |
| RPG suitability | Low-medium | Low | Very high | High |
| Accessibility | Medium | Low | High | High (with overrides) |
| Development cost | Low | High (3D UI assets) | Medium | Medium-high (state logic) |
| Customization need | Low | Low | Essential | Medium (auto-adapts) |

---

## 6. HUD Element Placement Guidelines

Regardless of approach, certain placement conventions are standard across games.

### Screen Zone Map

```
 _______________________________________________
|  TOP-LEFT          TOP-CENTER      TOP-RIGHT  |
|  Player health     Boss health     Minimap    |
|  Player status     Zone name       Compass    |
|                                    Currency   |
|  LEFT               CENTER         RIGHT      |
|  Party list         Crosshair      Quest log  |
|  Notifications      Damage nums    Objective  |
|                                               |
|  BOTTOM-LEFT      BOTTOM-CENTER  BOTTOM-RIGHT |
|  Chat log          Ability bar    Ammo count  |
|  Combat log        Quick items    Interact    |
|_________________ XP bar (full width) ________|
```

### Placement Principles

1. **Top-left** is the first place the eye goes (in LTR cultures). Place the most critical
   persistent information here (player health).
2. **Center** should remain as clear as possible to avoid obscuring gameplay.
3. **Bottom-center** is ideal for action bars and ability slots (close to the player's hands
   on a controller/keyboard).
4. **Right side** is good for secondary information (quests, minimap, notifications).
5. **Edges and corners** absorb HUD elements without blocking central gameplay.

### Safe Zones

- **Title safe area:** 5% inset from each screen edge (for TV overscan)
- **Action safe area:** 3.5% inset (minimum for critical UI)
- All HUD elements must be within the title safe area
- Interactive elements should be within the action safe area

---

## 7. Recommended Approach

Based on the case studies above, the recommended HUD strategy is an
**adaptive HUD with manual override** that combines:

1. **Minimal exploration mode** -- Inspired by Breath of the Wild. Show only health (if not
   full), minimap, and current objective. Let the world breathe.

2. **Full combat mode** -- Inspired by classic RPG HUDs. Show health, mana, stamina,
   ability bar, enemy health bars, status effects, and damage numbers.

3. **Diegetic accents** -- Inspired by Dead Space. Use diegetic elements for specific
   flavor (magical compass, character journal, in-world signage).

4. **Full customization** -- Inspired by FFXIV. Allow advanced players to toggle, move,
   and resize every HUD element. Provide presets (Minimal, Standard, Detailed).

5. **Accessibility override** -- A "Show All" mode that forces all HUD elements to remain
   visible at all times, for players who need constant access to information.

---

## Cross-References

- For HUD element colors, see `references/color-palettes.md`
- For HUD text sizing, see `references/font-guidelines.md`
- For feedback effects on HUD elements, see `references/feedback-library.md`
- For HUD interaction patterns, see `references/ui-patterns.md`
- For HUD accessibility requirements, see `references/accessibility-checklist.md`
