# Game Mechanic Patterns

A catalog of proven, reusable game mechanic patterns. Use these templates when designing core systems.

---

## 1. Resource Management

**Description**: Players acquire, spend, and balance multiple resource types to achieve goals. The core challenge is making strategic allocation decisions under scarcity.

**Core Loop**:
1. Gather/earn resource(s)
2. Decide how to allocate resources
3. Execute action using resources
4. Observe consequences
5. Repeat with changed state

**Key Parameters**:
- `resource_types`: How many distinct resources (2-4 typically optimal)
- `generation_rate`: How fast resources accumulate
- `storage_capacity`: Maximum resources player can hold
- `conversion_rates`: How to exchange one resource for another
- `sink_costs`: Where resources are consumed

**Design Considerations**:
- Keep resource types distinct in acquisition method and use case
- Avoid single dominant resource that trivializes choices
- Make resource scarcity feel earned, not arbitrary
- Provide feedback on resource gain/loss
- Balance passive generation with active farming

**Examples**:
- **Clash of Clans**: Gold, Elixir, Dark Elixir with distinct generation and uses
- **Civilization**: Turns, Culture, Science, Gold with trading
- **Plants vs Zombies**: Sun resource for tower placement
- **Stardew Valley**: Money, Energy, Relationships, Supplies

**Implementation Checklist**:
- [ ] Define minimum 2 resource types
- [ ] Set generation/acquisition rates per resource
- [ ] Define storage limits
- [ ] Create resource sinks (where they're spent)
- [ ] Add feedback UI for changes
- [ ] Balance conversion rates
- [ ] Test for dominant strategy

---

## 2. Risk-Reward

**Description**: Players choose between safe/low-reward and dangerous/high-reward options. The core tension is deciding whether the potential gain justifies the risk.

**Core Loop**:
1. Evaluate risky option
2. Decide risk tolerance
3. Commit to action
4. Resolve outcome (succeed or fail)
5. Adapt strategy based on result

**Key Parameters**:
- `success_probability`: Percentage chance of success
- `reward_magnitude`: How much player gains if successful
- `penalty_magnitude`: How much player loses if failed
- `expected_value`: (reward × probability) - (penalty × (1 - probability))
- `volatility`: How much outcomes vary

**Design Considerations**:
- Make probability clear or learnable through experimentation
- Ensure positive expected value exists for skilled players
- Use penalties that hurt but don't completely reset progress
- Vary risk/reward ratios to create tactical decision points
- Consider player psychology (players often avoid risks)

**Examples**:
- **Dark Souls**: Risk corpse run to retrieve souls (high penalty if fail)
- **Inscryption**: Challenging encounters for better cards
- **XCOM**: High-risk shots with varying hit percentages
- **Poker**: Betting mechanics with variable odds
- **Slay the Spire**: Risk damage for better rewards in encounters

**Implementation Checklist**:
- [ ] Define success probability formula
- [ ] Set reward value
- [ ] Set penalty value
- [ ] Calculate expected value (should be positive for skill)
- [ ] Create visual indicators of risk
- [ ] Implement penalty mechanics
- [ ] Test risk preference curve (should appeal to multiple playstyles)

---

## 3. Combo Systems

**Description**: Players chain actions together to create emergent effects beyond individual abilities. Success requires planning and execution timing.

**Core Loop**:
1. Identify combo potential
2. Execute first action in sequence
3. Execute subsequent actions quickly
4. System detects sequence and applies bonus
5. Larger combos reward player more

**Key Parameters**:
- `combo_length`: How many actions needed for bonus
- `timing_window`: How long between actions to maintain combo
- `combo_multiplier`: Bonus per additional action (usually escalates)
- `reset_condition`: What breaks the combo
- `visual_feedback_timing`: When to show combo counter

**Design Considerations**:
- Keep timing windows generous enough for skill expression, not rhythm game precision
- Make combos visible and satisfying to execute
- Escalate rewards significantly (1.1x per action minimum)
- Allow combo reset without punishing the player too severely
- Create natural "combo chains" where actions lead to combo opportunities

**Examples**:
- **Devil May Cry**: Action combos with style ranking
- **Marvel's Spider-Man**: Chained melee combos
- **Peglin**: Pin bounces creating chain reactions
- **Just Cause 3**: Destruction chains for multipliers
- **Monster Hunter**: Element status buildup combos

**Implementation Checklist**:
- [ ] Define combo length (3-5 actions typical)
- [ ] Set timing window duration
- [ ] Create combo multiplier formula
- [ ] Implement action sequencing detection
- [ ] Build visual feedback (counter, effects, sounds)
- [ ] Define reset conditions
- [ ] Test skill ceiling (combos should be learnable)

---

## 4. Cooldown Rotation

**Description**: Player manages multiple abilities with independent cooldowns, creating a rhythm of available actions. The challenge is adapting rotation to situation while cooldowns recharge.

**Core Loop**:
1. Execute available ability
2. Ability enters cooldown
3. Use other available abilities
4. Wait for high-impact ability to come off cooldown
5. Repeat with situational adjustments

**Key Parameters**:
- `ability_cooldown`: Time until reuse (3-20 seconds typical)
- `ability_power`: Relative strength of ability
- `cooldown_reduction`: Methods to reduce cooldown timers
- `cooldown_reset`: Abilities that reset other cooldowns
- `global_cooldown`: Enforced delay between any action

**Design Considerations**:
- Create clear visual countdown indicators
- Balance global cooldown vs. per-ability cooldowns
- Use cooldowns to gate power spikes, not to create dead time
- Reward skillful ability sequencing with cooldown reduction
- Vary cooldown lengths to prevent perfect rotations

**Examples**:
- **World of Warcraft**: Boss abilities and player rotations
- **League of Legends**: Ability cooldowns with cooldown reduction items
- **Valorant**: Ability charges with cooldown resets
- **Dark Souls**: Dodge roll with stamina recovery
- **MOBA games**: Ultimate ability cooldowns

**Implementation Checklist**:
- [ ] Define 3-5 core abilities
- [ ] Set cooldown durations per ability
- [ ] Create cooldown UI (circular progress indicator)
- [ ] Implement cooldown reduction mechanics
- [ ] Add audio/visual cues for cooldown ready
- [ ] Test rotation flow (shouldn't have dead time)
- [ ] Balance damage output across cooldown cycle

---

## 5. Positioning

**Description**: Spatial positioning and movement create tactical depth. Character placement determines available actions, defensive options, and risks.

**Core Loop**:
1. Observe board/map state
2. Assess positioning advantages
3. Move to advantageous position
4. Take action from new position
5. Opponent counters position

**Key Parameters**:
- `movement_range`: How far character can move per turn
- `range_modifiers`: How distance affects attack power
- `cover_system`: What provides defense and how much
- `positioning_advantage`: Bonus for flanking/high ground
- `punishment_for_bad_position`: Damage/vulnerability from wrong position

**Design Considerations**:
- Make positioning immediately consequential (not purely symbolic)
- Create natural cover and high ground opportunities
- Reward aggressive positioning with risk
- Punish passive positioning subtly (missed opportunities vs. direct damage)
- Use elevation, walls, and enemy placement to guide positioning options

**Examples**:
- **XCOM**: Overwatch and cover systems
- **Tactics Ogre**: Height, range, and unit positioning
- **Fire Emblem**: Weapon range and promotion bonuses
- **Divinity: Original Sin 2**: Surface interactions and height advantage
- **Into the Breach**: Movement as core tactical puzzle

**Implementation Checklist**:
- [ ] Define movement rules and ranges
- [ ] Implement pathfinding system
- [ ] Create cover system (full vs. partial)
- [ ] Add height/elevation system
- [ ] Define positioning bonuses/penalties
- [ ] Test sightlines (can units target what they can see)
- [ ] Balance offense vs. defense via positioning

---

## 6. Crafting & Synthesis

**Description**: Players combine base materials into more valuable items, creating progression through collection and creation. The depth comes from recipe variety and material discovery.

**Core Loop**:
1. Gather/obtain base materials
2. Discover or know recipe
3. Spend materials
4. Receive crafted item
5. Use item or craft with it

**Key Parameters**:
- `recipe_complexity`: Single vs. multiple material recipes
- `material_rarity`: How common each ingredient is
- `recipe_discovery`: Learning vs. known recipes
- `crafting_time`: Instant vs. time-based crafting
- `failure_chance`: Can crafting fail and consume materials

**Design Considerations**:
- Make recipe outcomes feel logical (fire + ice ≠ heal potion)
- Provide multiple ways to obtain key materials (farming, trading, looting)
- Use crafting progression to gate content (early recipes simple, late complex)
- Balance crafted item power vs. found items
- Create breakpoints where new recipes unlock
- Avoid crafting busywork (if crafting's frequent, make it fast)

**Examples**:
- **Minecraft**: Block combination recipes
- **Alchemy**: Potion brewing with ingredient combinations
- **Monster Hunter**: Weapon upgrading and crafting
- **Valheim**: Workbench crafting and upgrades
- **Breath of the Wild**: Cooking with ingredient combinations

**Implementation Checklist**:
- [ ] Define 10-20 base recipes
- [ ] Establish material sources
- [ ] Set crafting times/costs
- [ ] Create failure mechanics (if any)
- [ ] Design progression (easy early, complex late)
- [ ] Make recipes learnable/discoverable
- [ ] Balance: Is crafted gear optimal?

---

## 7. Procedural Generation

**Description**: Algorithmic content creation produces varied, replayable game spaces. Player discovery and adaptation to novel situations create replayability.

**Core Loop**:
1. Initialize generation parameters
2. Run generation algorithm
3. Player explores generated content
4. Encounter novel situations
5. Adapt strategy to content variation
6. Repeat with new generation seed

**Key Parameters**:
- `seed`: Deterministic generation starting point
- `generation_rules`: Algorithm producing content (perlin noise, cellular automata, recursive division)
- `constraint_system`: What must/must-not appear together
- `density_parameters`: How packed with content is the space
- `variation_parameters`: How different can areas be

**Design Considerations**:
- Always validate generation output (ensure playability)
- Create sensible geographic/dungeon logic (water flows downhill, etc.)
- Vary generation rules by region/biome for diversity
- Ensure progression always possible despite randomness
- Use seeds for reproducibility and sharing

**Examples**:
- **Spelunky**: Level generation with predetermined chunks
- **Minecraft**: Biome-based infinite generation
- **Hades**: Room-based roguelike generation
- **Dead Cells**: Layer-based encounter generation
- **No Man's Sky**: Planetary and creature generation

**Implementation Checklist**:
- [ ] Choose generation algorithm (noise, cellular, grammar)
- [ ] Implement constraint system
- [ ] Add validation pass (ensure playability)
- [ ] Set density parameters
- [ ] Create biome/region variation
- [ ] Test distribution (ensure variety feels natural)
- [ ] Implement seed-based reproducibility

---

## 8. Deck Building

**Description**: Players collect cards and construct limited decks, creating deckbuilding strategy meta. Constraints (deck size, card count limits) create interesting tradeoffs.

**Core Loop**:
1. Acquire new cards
2. Modify deck composition
3. Play cards in matches
4. Refine deck based on performance
5. Return to step 1

**Key Parameters**:
- `deck_size`: Minimum/maximum cards in deck
- `card_copy_limits`: How many copies of same card allowed (typically 2-3)
- `card_rarity`: Distribution of card power levels
- `synergy_bonuses`: Cards that combo with each other
- `curve`: Distribution of card costs/power

**Design Considerations**:
- Create clear power differences between cards (rare >> common)
- Design supporting cards that enable strategies (not just stat sticks)
- Make curve matter (if cost-based, ensure all costs viable)
- Create deck archetypes that play differently
- Use rarity to gate experimentation (can only craft 1 legendary weekly, etc.)

**Examples**:
- **Magic: The Gathering**: Physical deckbuilding with mana curve
- **Slay the Spire**: Run-based deckbuilding with random card offers
- **Hearthstone**: Constructed deck building with class restriction
- **Marvel Snap**: 12-card snap deckbuilding
- **Inscryption**: Roguelike deckbuilding within runs

**Implementation Checklist**:
- [ ] Define card set (50-200 cards minimum for depth)
- [ ] Set deck size limits
- [ ] Create card rarity/acquisition system
- [ ] Design synergies and combos
- [ ] Implement curve balancing
- [ ] Create deck archetype identities
- [ ] Test power level distribution

---

## 9. Roguelike Progression

**Description**: Players make permanent progress despite regular failures (death). Meta-progression rewards persist across runs, reducing difficulty and expanding options over time.

**Core Loop**:
1. Start new run with base stats
2. Collect upgrades/items during run
3. Make decisions about loadout
4. Encounter increasingly difficult challenges
5. Fail/succeed and end run
6. Gain permanent upgrade tokens
7. Return to step 1 with more options

**Key Parameters**:
- `difficulty_curve`: How fast difficulty ramps per run
- `meta_progression_rate`: How much permanent progress per run
- `power_cap`: How strong player can become
- `asymptotic_difficulty`: Where difficulty plateaus
- `unlock_frequency`: How often new content unlocks

**Design Considerations**:
- Make each run feel unique despite meta-progression
- Ensure early runs stay engaging (not gated behind progression)
- Create hard caps so infinite grinding doesn't break balance
- Make permanent unlocks meaningful (not just +1% damage)
- Balance difficulty so players have success/failure mix (50-70% success optimal)

**Examples**:
- **Hades**: Weapon/power unlocks with difficulty modifiers
- **Dead Cells**: Permanent item unlocks reducing grind
- **Risk of Rain 2**: Difficulty unlocks and item pool expansion
- **Binding of Isaac**: Unlock-based content expansion
- **Slay the Spire**: Ascension difficulty system

**Implementation Checklist**:
- [ ] Design meta-progression reward system (3-5 upgradeable tracks)
- [ ] Set run difficulty curve (should hit skill ceiling ~run 10-20)
- [ ] Create unlock frequency (one unlock every 2-3 runs)
- [ ] Define power cap (when does progression plateau)
- [ ] Test feel at different progression levels
- [ ] Ensure fun at progression 0 and max

---

## 10. Pet/Companion Systems

**Description**: AI-controlled allies follow player, provide support, and create combined strategies. Companions add depth through synergy and divided attention.

**Core Loop**:
1. Summon/activate companion
2. Issue commands or play passively
3. Companion acts (attack, heal, buff)
4. Companion cooldowns recharge
5. Coordinate companion + player actions
6. React to companion behavior

**Key Parameters**:
- `companion_ai_level`: Passive vs. semi-intelligent vs. fully autonomous
- `command_input_frequency`: How often player directs actions
- `companion_power_budget`: How strong companion is vs. player
- `ability_synergies`: How companion abilities combine with player abilities
- `companion_positioning`: Can player control position or automatic

**Design Considerations**:
- Make companion actions predictable so player can plan
- Give clear visual feedback on companion status/abilities
- Create synergies between player and companion (not just stacking)
- Avoid micro-management fatigue (clear AI or simple commands)
- Balance companion power so it's mandatory without being overpowered

**Examples**:
- **Nioh**: Spirit summons providing temporary boosts
- **Dark Souls**: NPC summons for boss help
- **Persona**: Party members in turn-based combat
- **Stardew Valley**: Horse and pets following player
- **Final Fantasy**: Party-based combat with AI actions

**Implementation Checklist**:
- [ ] Define companion stats (HP, damage, abilities)
- [ ] Implement pathfinding and positioning
- [ ] Create ability set (3-4 core abilities)
- [ ] Build command system (auto, follow, attack, etc.)
- [ ] Design synergies with player abilities
- [ ] Balance power budget (companion should be 20-40% of player power)
- [ ] Test responsiveness and predictability

---

## Pattern Selection Guide

Use this matrix to select appropriate patterns for your game:

| Pattern | Single Player | Multiplayer | Turn-Based | Real-Time | Combat | Exploration |
|---------|---------------|-------------|-----------|-----------|--------|-------------|
| Resource Management | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Risk-Reward | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Combo Systems | ✓ | ✓ | - | ✓ | ✓ | - |
| Cooldown Rotation | ✓ | ✓ | ✓ | ✓ | ✓ | - |
| Positioning | ✓ | ✓ | ✓ | ✓ | ✓ | - |
| Crafting/Synthesis | ✓ | ✓ | ✓ | ✓ | - | ✓ |
| Procedural Generation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Deck Building | ✓ | ✓ | ✓ | - | ✓ | - |
| Roguelike Progression | ✓ | - | ✓ | ✓ | ✓ | ✓ |
| Pet/Companion | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
