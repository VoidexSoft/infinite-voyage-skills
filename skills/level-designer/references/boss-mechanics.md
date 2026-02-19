# Boss Fight Design Reference

Archive of boss fight design patterns, telegraph systems, phase structures, and mechanical
frameworks. Use this reference when designing new boss encounters or reviewing existing ones.

---

## Phase Design Patterns

Every boss fight should have phases. Phases create narrative structure within the fight,
introduce escalation, and give the player a sense of progress.

### Two-Phase (Simple Boss / Miniboss)

| Phase | HP Range | Purpose | Intensity |
|-------|----------|---------|-----------|
| Phase 1 | 100-50% | Teach core mechanics | 6-7/10 |
| Phase 2 | 50-0% | Escalate with new mechanic or increased aggression | 8-9/10 |

**Best for:** Minibosses, early-game bosses, encounters under 5 minutes.

**Transition:** Visual transformation, brief invulnerability with animation, or arena change.

### Three-Phase (Standard Boss)

| Phase | HP Range | Purpose | Intensity |
|-------|----------|---------|-----------|
| Phase 1 | 100-70% | Introduce the boss, teach attack patterns | 5-6/10 |
| Phase 2 | 70-35% | Add complexity, introduce new mechanic | 7-8/10 |
| Phase 3 | 35-0% | Desperation mode, highest intensity, combined mechanics | 9-10/10 |

**Best for:** Zone bosses, story-critical encounters, 8-15 minute fights.

**Transition:** Phase 2 often triggered by a scripted ability. Phase 3 typically marked by
visual transformation (corruption spreading, armor breaking, second form revealed).

### Four-Phase (Epic Boss)

| Phase | HP Range | Purpose | Intensity |
|-------|----------|---------|-----------|
| Phase 1 | 100-75% | Introduction and pattern learning | 5/10 |
| Phase 2 | 75-50% | First escalation, arena modification | 7/10 |
| Phase 3 | 50-25% | Major mechanic shift, adds or environmental change | 8-9/10 |
| Phase 4 | 25-0% | Final stand, all mechanics combined, enrage potential | 10/10 |

**Best for:** Act bosses, final bosses, raid encounters, 15-25 minute fights.

**Transition:** Each transition should feel like a meaningful story moment. The boss is
not just getting harder; it is revealing more of itself.

### Intermission Pattern

Insert a non-combat intermission between phases:

```
Phase 1 -> [Intermission: Puzzle/Platforming] -> Phase 2 -> [Intermission: Story Beat] -> Phase 3
```

**Best for:** Long boss encounters that need pacing relief. The intermission resets player
tension and lets them approach the next phase with fresh focus.

---

## Telegraph Systems

Telegraphs are the communication layer between boss and player. Every attack must be
readable. The quality of a boss fight depends on how well it communicates.

### Telegraph Hierarchy

| Telegraph Level | Warning Time | When to Use |
|----------------|-------------|-------------|
| **Long telegraph** | 2.0-3.0 sec | New mechanics, high-damage attacks, phase transitions |
| **Standard telegraph** | 1.0-1.5 sec | Regular abilities, standard rotational attacks |
| **Short telegraph** | 0.5-0.8 sec | Quick attacks in established patterns, combo follow-ups |
| **Micro telegraph** | 0.2-0.4 sec | Hard/Nightmare-only variants, punish attacks for greedy play |

### Telegraph Types

| Type | Description | Example |
|------|-------------|---------|
| **Animation wind-up** | Boss performs a preparatory motion | Arm raised before slam, coiling before leap |
| **Ground indicator** | Danger zone highlighted on floor | Red circles, glowing lines, crack patterns |
| **Audio cue** | Distinct sound before the attack | Charging sound, boss vocalization, weapon hum |
| **Particle effect** | Visual energy buildup | Glowing hands, swirling energy, element gathering |
| **Environmental cue** | Arena itself signals danger | Lights dim, ground shakes, water ripples |
| **Boss state change** | Visible transformation before attack | Eyes glow, stance shifts, wings spread |

### Telegraph Design Rules

1. **Layer multiple telegraph types** -- Use at least 2 of the 6 types for every major attack
2. **Consistent color language** -- Red = damage zone, yellow = caution zone, blue = safe zone
3. **Audio must be distinct** -- Each boss attack should have a unique sound profile
4. **First encounter teaches** -- The first time an attack appears, use a long telegraph
5. **Subsequent uses can shorten** -- After 2-3 exposures, the telegraph can reduce by up to 30%
6. **Never remove telegraphs entirely** -- Even on Nightmare, attacks must have at least a micro telegraph
7. **Phase transitions are always safe** -- The player should never die during a transition animation

---

## Vulnerability Windows

Vulnerability windows are when the player can safely deal damage. They create the rhythm
of a boss fight: dodge, wait, punish, repeat.

### Window Types

| Type | Duration | Design Purpose |
|------|----------|---------------|
| **Post-attack recovery** | 1-3 sec | Boss recovers after a big attack; reward for dodging |
| **Mechanic completion** | 3-5 sec | Player completes a mechanic (break shield, solve puzzle) |
| **Stagger/stun** | 2-4 sec | Boss takes enough damage to trigger a stagger state |
| **Environmental exposure** | 3-6 sec | Boss is hit by environmental hazard and becomes vulnerable |
| **Phase transition** | 2-3 sec | Brief window during transformation animation |
| **Exhaustion** | 4-8 sec | Boss uses a big ability and needs to recharge |

### Window Frequency

| Fight Duration | Recommended Windows | Average Window Duration |
|---------------|-------------------|----------------------|
| Under 5 min | 4-6 | 2-3 sec each |
| 5-10 min | 8-12 | 2-4 sec each |
| 10-15 min | 12-18 | 3-5 sec each |
| 15+ min | 16-24 | 3-6 sec each |

### DPS Check Windows

Special windows that test whether the player has adequate damage output:

- Appear 1-2 times per boss fight maximum
- Duration: 8-15 seconds
- Failure consequence: Boss heals, adds spawn, or arena becomes more dangerous
- Never make DPS check failure instantly lethal -- it should extend the fight, not end it
- Clearly communicated: "Destroy the crystal before the ritual completes" type framing

---

## Add Waves

Additional enemies during boss fights serve specific design purposes.

### Add Wave Purposes

| Purpose | Enemy Type | Spawn Timing | Player Response |
|---------|-----------|-------------|----------------|
| **Resource generation** | Weak minions that drop health/mana | Between boss attack patterns | Kill for sustain |
| **Distraction** | Medium enemies that threaten the player | During DPS windows | Must manage or ignore |
| **Mechanic enforcement** | Enemies tied to a boss mechanic | When mechanic activates | Must interact to progress |
| **Pressure escalation** | Increasing numbers over time | Periodic spawns | Manage or face overwhelming odds |

### Add Wave Rules

1. **Maximum concurrent adds:** Never more than 4-6 at once during a boss fight
2. **Spawn location:** Always from visible spawn points, never behind the player without warning
3. **Clear priority:** It should be obvious whether to focus boss or adds
4. **Do not create add-lock:** If adds respawn, killing the boss should be possible while adds are alive
5. **Reward add management:** Killing adds should yield resources or temporary boss vulnerability
6. **Scale with party size:** Solo encounters should have fewer adds than group content

---

## Environmental Mechanics

The boss arena is a participant in the fight, not just a backdrop.

### Arena Hazard Types

| Hazard | Activation | Avoidance | Interaction |
|--------|-----------|-----------|-------------|
| **Floor damage zones** | Boss ability or timed cycle | Move to safe zones | Can sometimes lure boss into them |
| **Falling debris** | Phase transition or timed | Watch shadows/indicators | May create temporary cover |
| **Rising water/lava** | Gradual, forces vertical movement | Move to high ground | Boss may be immune or also affected |
| **Shrinking arena** | Phase-based, permanent | Stay in bounds | Increases encounter density |
| **Destructible pillars** | Boss charges through them | Bait boss into pillars for stagger | Limited supply, strategic resource |
| **Elemental zones** | Rotating or boss-created | Move with rotation | May buff player attacks of matching element |

### Arena Design Principles

1. **Readable geometry** -- The player must immediately understand what is safe and what is dangerous
2. **Multiple elevations** -- Height differences create tactical variety
3. **Cover with durability** -- Destructible cover adds resource management to the fight
4. **No invisible walls** -- If it looks like you can go there, you should be able to
5. **Arena changes with phases** -- The space should evolve as the fight progresses
6. **Recovery points** -- At least one area where the player can briefly disengage

---

## Enrage Timers

Enrage timers prevent fights from lasting indefinitely and create urgency.

### Enrage Types

| Type | Behavior | Purpose |
|------|----------|---------|
| **Soft enrage** | Boss gradually becomes stronger over time (stacking damage buff) | Prevents indefinite attrition strategies |
| **Hard enrage** | Boss becomes unbeatable after a set time (one-shot attacks) | Enforces DPS requirement |
| **Phase enrage** | Individual phase has a timer; failure means harder next phase | Rewards efficient damage per phase |
| **Healing enrage** | Boss starts healing if fight goes too long | Punishes passive play without instant death |

### Enrage Timer Guidelines

| Fight Duration Target | Soft Enrage Start | Hard Enrage |
|---------------------|------------------|-------------|
| 5 min fight | 6 min | 8 min |
| 10 min fight | 12 min | 15 min |
| 15 min fight | 18 min | 22 min |
| 20+ min fight | 24 min | 30 min |

**Rule of thumb:** Soft enrage at 1.2x target duration. Hard enrage at 1.5x target duration.

### Communication

- Soft enrage: Visual change on boss (glowing, darkening, growing), audio intensity increase
- Hard enrage: Screen effects, boss dialogue or roar, unmistakable visual warning 30 seconds before

---

## Reward Structures

Boss rewards should feel proportional to the challenge and serve as a capstone for the zone.

### Reward Tiers

| Boss Type | XP Multiplier | Loot Quality | Unique Drop Rate | Additional Rewards |
|-----------|--------------|-------------|-----------------|-------------------|
| Miniboss | 3-5x standard encounter | Zone-appropriate rare | 10-20% | Area unlock |
| Zone Boss | 8-12x standard encounter | Guaranteed rare, chance at epic | 25-40% | Story progression, zone completion |
| Act Boss | 15-25x standard encounter | Guaranteed epic | 50-75% | Major story unlock, new region access |
| Final Boss | 30-50x standard encounter | Guaranteed legendary | 100% | Game completion, new game+ unlock |

### First-Kill Bonuses

- First defeat of a boss grants a one-time bonus reward (additional unique item, title, cosmetic)
- This encourages engagement and rewards the initial learning investment
- Subsequent kills drop standard loot table only

### Difficulty-Based Rewards

| Tier | Loot Bonus | XP Bonus | Exclusive Drops |
|------|-----------|----------|----------------|
| Story | 0.5x | 0.5x | None |
| Easy | 0.75x | 0.75x | None |
| Normal | 1.0x | 1.0x | None |
| Hard | 1.5x | 1.5x | Hard-exclusive cosmetics |
| Nightmare | 2.0x | 2.0x | Nightmare-exclusive gear and titles |

---

## Boss Design Checklist

- [ ] Boss has 2-4 clearly defined phases
- [ ] Every attack has a layered telegraph (visual + audio minimum)
- [ ] Vulnerability windows appear at predictable intervals
- [ ] Add waves serve a clear purpose (not just more enemies)
- [ ] Arena participates in the fight and evolves with phases
- [ ] Enrage timer exists and is communicated to the player
- [ ] Rewards feel proportional to challenge and duration
- [ ] Fight is testable and beatable at all difficulty tiers
- [ ] No phase has a period longer than 30 seconds with no player agency
- [ ] Boss defeat triggers a satisfying audio-visual payoff
- [ ] Respawn point is within 60 seconds of boss arena entrance
- [ ] Fight teaches or tests a mechanic the zone introduced
