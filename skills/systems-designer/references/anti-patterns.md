# Game Design Anti-Patterns

Common pitfalls to avoid when designing game systems. Recognizing these patterns helps prevent design dead-ends.

---

## 1. Optimal Strategy (Rock-Paper-Scissors Trivialization)

**Description**: A single strategy exists that is always superior to alternatives. Once discovered, this strategy makes all other choices irrelevant.

**Why It's Bad**:
- Eliminates meaningful decision-making
- Reduces game to execution of known solution
- Encourages dominance through hard counters (not depth)
- Makes balance patches painful (nerfing dominant strategy breaks metagame)
- New players feel lost; experienced players feel limited

**How to Detect It**:
- All competitive players use identical builds/strategies
- Playtesting shows single dominant strategy emerges within 3 playthroughs
- Forum discussions revolve around "meta" with no viable alternatives
- Patch notes constantly rebalance same 2-3 strategies
- Win rate data shows one strategy at 60%+ win rate

**How to Fix It**:
- Introduce hard counters (X beats Y, Y beats Z, Z beats X)
- Add rock-paper-scissors balance to core choices
- Create viable alternative strategies with different skill curves
- Add situational modifiers (terrain, weather) favoring different approaches
- Use randomness to prevent perfect optimization

**Example Fixes**:
- **Before**: Gun always better than melee → **After**: Melee beats at close range, guns beat at distance
- **Before**: One ability dominates → **After**: Three ability types with mutual counters
- **Before**: Single build optimal → **After**: Multiple viable builds countered differently by opponents

---

## 2. Complexity Without Depth

**Description**: Systems have many rules, mechanics, and interactions but lack meaningful strategic choices. Complexity serves no purpose.

**Why It's Bad**:
- Creates high learning curve without payoff
- Makes game feel arbitrary and opaque
- Players memorize rather than understand
- Depth requires fewer, more meaningful choices
- Testing and balance becomes a nightmare
- New players are overwhelmed before learning core gameplay

**How to Detect It**:
- Rulebook is 40+ pages but game still feels random
- Players memorize matchups rather than learning principles
- Tutorial takes 2+ hours before gameplay feels fun
- Playtester feedback: "Too much stuff, unclear why it matters"
- Expert players can't explain why their strategy works

**How to Fix It**:
- Remove rules that don't enable meaningful choices
- Consolidate similar mechanics into unified system
- Ensure each rule directly affects player decision-making
- Simplify interactions (fewer moving parts, clearer relationships)
- Add tutorialization that explains "why" not just "how"

**Example Fixes**:
- **Before**: 12 resource types, 8 unit types, 20 tech trees → **After**: 3 resources, 5 units, clear tech progression
- **Before**: 30 status effects with unique interactions → **After**: 5 core effects (stun, poison, burn, freeze, bleeding) with clear relationships
- **Before**: Arbitrary bonus numbers (+17% crit vs. +3.2% evasion) → **After**: Clear percentage-based modifiers (2x damage, 3s duration)

---

## 3. Snowball Mechanics

**Description**: Early success compounds exponentially, making comebacks nearly impossible. The winner is decided in the first 10% of game.

**Why It's Bad**:
- Eliminates late-game interest (outcome decided early)
- Demoralizes losing players
- Makes comebacks feel impossibly lucky
- Unfair to players with early misfortune
- Bad for multiplayer (sitting around losing)
- Reduces actual match engagement

**How to Detect It**:
- Player with early advantage wins 85%+ of the time
- Winning player keeps growing advantages faster
- Lost player can't meaningfully impact outcome after 20 minutes
- Spectators know outcome before endgame
- Player asks "why keep playing?" when behind

**How to Fix It**:
- Add catch-up mechanics (losing players get bonus resources)
- Implement dynamic difficulty (harder for leader, easier for trailing)
- Cap advantage magnitude (can't snowball past point)
- Increase opponent reward for fighting back
- Add sudden game-changing events late (king of the hill, final boss)
- Use diminishing returns on scaling advantages

**Example Fixes**:
- **Before**: Early kill = 100 gold, permanent stat boost → **After**: Early kill = 50 gold, stat boost caps at +20%
- **Before**: Resource income scales with territory → **After**: Resource income caps, losing players get +10% passive income
- **Before**: Health doesn't exist, whoever has gold advantage wins → **After**: Comeback potential in last 30% of match via sudden events

---

## 4. Mandatory Unfun (Tedious Timesinks)

**Description**: Progression requires completing unfun, repetitive tasks. The path to fun is blocked by boring mechanics.

**Why It's Bad**:
- Players resent forced tedium
- Creates sense of obligation instead of joy
- High abandonment rates (players quit during unfun section)
- Feels like punishment for playing
- Wears out willpower even if core game is fun
- Bad for word-of-mouth (friends don't recommend grindy games)

**How to Detect It**:
- Designer hears: "I don't want to grind that section"
- Telemetry shows 40% dropoff at specific gameplay section
- Playtester: "This task is boring but I have to do it for X"
- Progression gates require 3+ hours of identical repetition
- Tasks have no meaningful choices, pure execution

**How to Fix It**:
- Make boring tasks optional (provide alternative paths)
- Reduce time required (a 5-minute grind is acceptable, 2-hour grind isn't)
- Add variety (randomize locations, encounters, rewards)
- Make tedious tasks progress multiple goals simultaneously
- Compress progression (fewer, more impactful tasks)
- Use automation for repetitive tasks (skip animations, batch operations)

**Example Fixes**:
- **Before**: Must farm 1000 weak enemies for weapon unlock → **After**: Can farm 100 normal enemies OR complete challenge dungeon OR buy from vendor
- **Before**: Must harvest 50 identical crops → **After**: Harvest any 20 crops (different types), get rewards for variety
- **Before**: Level up requires 1M XP from slow grinding → **After**: Level up requires 100k XP, multiple sources (questing, farming, PvP, crafting)

---

## 5. Hidden Information Overload

**Description**: Game mechanics depend on hidden information players can't reasonably discover. Success requires external knowledge or trial-and-error.

**Why It's Bad**:
- Creates frustration (punished for not knowing unknowable)
- Punishes exploration and experimentation
- Favors wiki readers over players
- Makes first playthroughs feel arbitrary
- Reduces player agency (can't plan with incomplete information)
- Encourages metagame knowledge as mandatory skill

**How to Detect It**:
- Playtester says: "How was I supposed to know that?"
- Core strategy requires knowledge from wiki/community
- Damage calculations aren't shown or explainable
- Item effects contradict descriptions
- Optimal strategy is invisible (hidden stats)
- Designer knows something testers don't

**How to Fix It**:
- Show all relevant information (damage calc, hit chance, effects)
- Use clear naming (if hidden, explain why)
- Provide in-game discovery methods (scanning, testing, NPCs explaining)
- Give feedback that reveals mechanics (number popups showing actual damage)
- Make hidden information optional depth (speedrunners vs. casual players)
- Use tutorials to explain key hidden mechanics

**Example Fixes**:
- **Before**: Damage = attack * hidden_formula → **After**: Show damage calc (Base 10 + 20% DEF = 12 damage)
- **Before**: Status effect has hidden duration → **After**: Visual timer or explicit "Poison: 5 turns remaining"
- **Before**: Optimal item combos are mysterious → **After**: Show synergy in item description ("Synergizes with cold effects: +50% freeze duration")

---

## 6. Artificial Difficulty

**Description**: Challenge doesn't come from player skill but from unfair mechanics, RNG, or badly designed encounters. Difficulty is rubber-banded (cheap AI, endless reinforcements).

**Why It's Bad**:
- Players feel cheated, not challenged
- Skill cannot improve outcomes consistently
- Causes frustration instead of satisfaction
- Cheapens victory ("I got lucky" vs. "I got good")
- Bad difficulty curve (stomping then impossible)
- Encourages cheese strategies and exploits

**How to Detect It**:
- Players beat difficult content through exploits, not skill
- Encounters have unlimited reinforcements or healing
- Damage output feels random and unjust
- AI ignores player presence or cheats
- Playtester: "That wasn't fair, that was cheap"
- Winning feels like luck rather than achievement

**How to Fix It**:
- Implement clear, fair AI (visible telegraph, avoidable attacks)
- Use telegraphing (wind-up, sound, visual indicator before attack)
- Make difficulty come from complexity not unlimited resources
- Create fair encounter design (visible threats, avoidable damage)
- Reward skill expression (perfect dodge, perfect parry)
- Scale difficulty based on player demonstrated skill, not arbitrary scaling

**Example Fixes**:
- **Before**: Boss has unlimited minions → **After**: Boss spawns 3 minions total, waves are telegraphed
- **Before**: Surprise instant-kill attack → **After**: 2-second wind-up with visual effect, avoidable by dodging
- **Before**: Enemy ignores player defense stats → **After**: Defense stat directly reduces enemy damage (shown calculation)

---

## 7. False Choices

**Description**: Player appears to have a meaningful decision but one option is mathematically superior. All players choose identical option; choice is illusory.

**Why It's Bad**:
- Wastes mental energy on fake decisions
- Frustrates players who "chose wrong"
- Creates sense of option but eliminates agency
- Wastes design time (false complexity)
- Leads to frustration when optimal path is unclear
- Makes later content inaccessible if early choice gates progression

**How to Detect It**:
- All players choose same option in playtest
- One option is mathematically superior (20% more damage)
- Choosing "wrong" path makes game significantly harder
- Forum discussions about "best choice" (should be subjective)
- Playtester says: "That wasn't a real choice"

**How to Fix It**:
- Make options genuinely different with tradeoffs (damage vs. defense)
- Use rock-paper-scissors balance (each option counters one, loses to one)
- Rebalance so no dominant strategy exists
- Make choices meaningful only in context (what's optimal depends on matchup)
- If decision gates content, ensure all paths are viable
- Accept some choices are preference-based, not optimization-based

**Example Fixes**:
- **Before**: Option A: +10 damage, Option B: +5 damage → **After**: Option A: High damage but slow, Option B: Lower damage but fast combos
- **Before**: Pick sword/magic, but magic is 50% stronger → **After**: Both deal same damage, magic has area effect, sword has range
- **Before**: Choose skill A, but skill B makes game 3x harder → **After**: Skill A good vs. hordes, Skill B good vs. single boss, both accessible

---

## 8. Grind Walls

**Description**: Progression suddenly requires exponentially more repetitive tasks. Players hit a point where advancement feels impossible without significant time investment.

**Why It's Bad**:
- Creates abandonment point (player quits at wall)
- Frustrates players who were progressing smoothly
- Punishes commitment (early players hit wall harder)
- Encourages pay-to-skip mechanics (feels extractive)
- Unfun because no new content, same tasks harder
- Separates casual and hardcore in middle of game

**How to Detect It**:
- Progression takes 1 hour at level 10, 20 hours at level 20
- Playtester suddenly says: "This feels like a job"
- Exponential stat requirements for same activity
- Players resort to farming optimal location repeatedly
- Telemetry shows 50% dropoff at specific level
- No content gates exist before wall (pure grinding)

**How to Fix It**:
- Use linear progression (time to next level stays constant)
- Add content gates instead of grinding (complete dungeon, boss, quest)
- Allow alternative paths to progress (farming OR questing OR PvP)
- Introduce variety (same XP for different activities)
- Cap required grinding (no activity takes >1 hour for major progression)
- Add scaling (harder enemies = more XP, so difficulty increases but grinding speed stays constant)

**Example Fixes**:
- **Before**: Level 10→11: 1 hour, Level 20→21: 40 hours → **After**: Each level 2-3 hours regardless of level
- **Before**: Only way to progress is farming zone A → **After**: Zone A, dungeons, PvP, quests all give equal XP
- **Before**: Boss requires 100 level grind → **After**: Boss dungeon unlocks at level 50, progresses at balanced pace

---

## 9. Feature Creep

**Description**: Game scope continuously expands beyond original design. Every playtesting session adds features instead of refining core. Project becomes bloated and unfocused.

**Why It's Bad**:
- Project never ships (perpetual development)
- Core mechanics never mature (always chasing new features)
- Resources spread too thin (nothing polished)
- Contradicting features create balance nightmares
- Team morale suffers (goalpost keeps moving)
- Design loses coherence (feels like random collection of systems)

**How to Detect It**:
- Feature list grew 50%+ since start of development
- Team asks: "Why is this feature in the game?"
- Balance is constantly broken by new features
- Development velocity is decreasing despite team size
- Playtester: "This game tries to do too much"
- Core loop is unclear because so many subsystems exist

**How to Fix It**:
- Define core pillars (max 3 core mechanics)
- Create feature freeze date (no new features after X date)
- Evaluate new features: "Does this enhance core pillar?"
- Remove features that don't support core pillars
- Use scope matrix: Core features complete, then expand
- Say no to features, even good ideas (they dilute focus)

**Example Fixes**:
- **Before**: Combat, farming, fishing, crafting, pet system, housing, etc. → **After**: Combat (core), farming (supports progression), that's it
- **Before**: Add new feature every playtesting session → **After**: Only add features that fix core issues, rest cut
- **Before**: 20 systems competing for design focus → **After**: Polish 3 systems fully, cut rest

---

## 10. Power Creep

**Description**: New content/items/abilities are progressively more powerful. Soon old content is irrelevant, and power levels become absurd. New players face impossible catch-up.

**Why It's Bad**:
- Invalidates old content immediately
- New players feel behind forever (impossible catch-up)
- Encourages pay-for-power (power is only way to compete)
- Balance spirals out of control
- Game systems become unrecognizable over time
- Veteran players feel betrayed (investment becomes meaningless)

**How to Detect It**:
- New expansion gear makes old gear obsolete
- Damage numbers triple every 6 months
- Playtester says: "Old stuff is trash now"
- Power curve is exponential (level 10 = 100 damage, level 100 = 10,000 damage)
- New players have no way to get current-best items
- Telemetry shows old content has 0% playtime

**How to Fix It**:
- Implement hard power caps (gear past level X doesn't increase damage)
- Use horizontal progression (new items are different, not stronger)
- Make old content scaling with player power
- Reduce new content power creep (new gear = 5% stronger, not 50%)
- Increase catch-up mechanics for new players (veteran quicker leveling)
- Keep old content relevant (end-game content uses low-level mechanics)

**Example Fixes**:
- **Before**: New expansion items 200% stronger than old → **After**: New items 110% stronger (power scaling reduced)
- **Before**: Old dungeons give 1/10th XP of new dungeons → **After**: Dungeons scale to player level, give proportional XP
- **Before**: Can one-shot enemies at endgame, ultimate feels meaningless → **After**: Hard cap at 5x base damage, complexity increases instead
- **Before**: Veterans get gear in 1 hour, newbies need 100 hours to catch up → **After**: Catch-up mechanic: new players get 10x XP for first 50 levels

---

## Prevention Checklist

Use this when designing systems to avoid anti-patterns:

**Balance & Strategy**:
- [ ] Multiple viable strategies exist (not one optimal)
- [ ] Core mechanics have rock-paper-scissors balance (not linear progression)
- [ ] Winning player advantage grows linearly, not exponentially
- [ ] All player choices matter (no false choices)

**Complexity & Learning**:
- [ ] Each rule enables meaningful decisions
- [ ] Tutorial explains "why" not just "how"
- [ ] Hidden mechanics are discoverable or explained
- [ ] Complexity serves gameplay depth (not just existing)

**Progression & Pacing**:
- [ ] Boring tasks are optional or <5 minutes each
- [ ] Progression curve is smooth (not sudden walls)
- [ ] Difficulty grows with player skill, not arbitrarily
- [ ] Content unlocks create pacing, not grinding requirements

**Scope & Focus**:
- [ ] Game has 3 core mechanics (not 30 minor ones)
- [ ] New features enhance core pillars (not dilute)
- [ ] Power is capped (not exponentially scaling)
- [ ] Old content remains relevant
