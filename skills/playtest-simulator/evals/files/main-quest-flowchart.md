# Main Quest Flowchart: "Signal in the Static" — Act 2

## Overview
- **Quest level:** 18-22
- **Estimated duration:** 3-4 hours
- **Prerequisites:** Act 1 complete, player has the Void Resonance Scanner
- **Branches:** 2 major decision points, 3 possible endings for this act

## Quest Flow

```
[START: Act 2 Begins]
    |
    v
[Step 1] Receive transmission from NPC Kael at Waystation Omega
    |  (auto-trigger on entering Sector 7)
    |  Gate: Player level >= 18
    v
[Step 2] Travel to Sector 7-G and locate the Shattered Relay
    |  Gate: Ship fuel >= 30 units (travel cost: 25 units)
    |  Optional: Side conversation with NPC Mira (foreshadows Act 3)
    v
[Step 3] Dock at the Shattered Relay
    |  Gate: None (auto-dock cutscene)
    v
[Step 4] Clear the Docking Bay (Encounter E1)
    |  Gate: Combat completion
    |  Reward: Relay Access Keycard, 150 Astral Credits
    v
[Step 5] Restore station atmosphere
    |  METHOD A: Solve Atrium Pressure Puzzle (E2)
    |      Gate: Complete valve puzzle
    |      Time: ~5 minutes
    |  METHOD B: Use Ventilation Shaft (Secret S2)
    |      Gate: Scanner pulse to find vent + combat 2x Vent Crawlers
    |      Time: ~3 minutes
    |      Bonus: Engineering Note lore pickup
    v
[Step 6] Access Command Deck
    |  Gate: Relay Access Keycard (from Step 4)
    v
[Step 7] Download Void Signal data from command terminals
    |  Gate: Interact with terminal (3-second channel)
    |  Trigger: Starts wave defense encounter (E3)
    v
[Step 8] Defend the terminals during data download (E3)
    |  Gate: Survive 3 waves, at least 1 terminal intact
    |  Fail condition: All 3 terminals destroyed -> go to [Step 8F]
    v
[Step 8F — FAIL BRANCH] Salvage partial data
    |  Narrative: Download is corrupted, only fragments recovered
    |  Effect: Act 2 ending C is locked; only endings A or B available
    |  Continues to Step 9
    v
[Step 9] Confront the Relay Overseer (Boss)
    |  Gate: Reach reactor level via E4
    |  Boss fight: Relay Overseer, 3 phases
    |
    |--- [SECRET PATH] If player has Engineering Note (from S2):
    |       Can input failsafe code during Phase 2
    |       -> Skips Phase 3, unlocks unique reward
    |       -> Boss is "redeemed" instead of destroyed
    v
=== DECISION POINT 1 ===
[Step 10] After defeating/redeeming the Overseer, choose what to do with the Void Signal data:

    CHOICE A: "Send data to the Vanguard Coalition"
        |  Alignment shift: +15 Order
        |  NPC Kael: Approves
        |  Reward: 500 Astral Credits, Vanguard Reputation +200
        |  Consequence: Coalition fleet mobilizes (affects Act 3 opening)
        v
    [Step 11A] Kael transmits data to Coalition command
        |  Cutscene: Coalition ships jump into sector
        v
    === DECISION POINT 2A ===
    [Step 12A] Coalition wants to destroy the relay to prevent Void spread:

        CHOICE A1: "Agree — destroy the relay"
            |  Alignment: +10 Order
            |  Consequence: Relay destroyed, zone becomes inaccessible
            |  Reward: Coalition Medal of Service (unique trinket, +5% XP in Coalition space)
            |  -> ACT 2 ENDING A: "By the Book"
            v
        CHOICE A2: "Refuse — the relay has historical value"
            |  Alignment: +5 Curiosity, -5 Order
            |  Consequence: Tension with Coalition, but relay preserved
            |  Reward: Kael's Trust (companion loyalty +1)
            |  -> ACT 2 ENDING B: "Dissenting Voice"
            v

    CHOICE B: "Keep data for yourself"
        |  Alignment shift: +10 Independence, -10 Order
        |  NPC Kael: Disapproves (companion loyalty -1)
        |  Reward: Void Signal Decoder (unique item, used in Act 4 side quest)
        |  Consequence: Player has leverage but no allies for Act 3 opening
        v
    [Step 11B] Kael confronts the player about the decision
        |  Dialogue: Persuade check (Charisma 14) to maintain relationship
        |  Pass: Kael reluctantly stays, loyalty neutral
        |  Fail: Kael leaves the crew temporarily (rejoins in Act 3, Scene 4)
        v
    -> ACT 2 ENDING C: "Lone Signal"
       (only available if terminals survived in Step 8)

=== ACT 2 COMPLETE ===
```

## Gate Summary

| Step | Gate Type | Requirement | Fail Behavior |
|------|-----------|-------------|---------------|
| 1 | Level | Player level >= 18 | Quest not offered; NPC says "Come back when you're stronger" |
| 2 | Resource | Ship fuel >= 30 | Player must refuel; fuel available at Waystation Omega (50 credits/unit) |
| 4 | Combat | Defeat all enemies in E1 | Retry; enemies respawn on death |
| 5 | Puzzle/Combat | E2 puzzle or S2 vent path | Infinite retry (puzzle resets); vent path is permanent |
| 6 | Key item | Relay Access Keycard | Always obtained in Step 4 |
| 8 | Combat/Survival | 1+ terminal survives | Branch to Step 8F if all destroyed |
| 9 | Combat | Defeat Relay Overseer | Retry; boss resets on death |
| 10 | Player choice | Select A or B | No default; must choose |
| 11B | Skill check | Charisma 14 | Binary pass/fail |
| 12A | Player choice | Select A1 or A2 | No default; must choose |

## Pacing Targets

| Segment | Target Duration | Intensity |
|---------|----------------|-----------|
| Steps 1-3 (setup) | 10-15 min | Low (travel, dialogue) |
| Steps 4-5 (entry) | 15-20 min | Medium (combat, puzzle) |
| Steps 6-8 (climax buildup) | 15-20 min | High (wave defense) |
| Step 9 (boss) | 8-12 min | Very High (boss fight) |
| Steps 10-12 (resolution) | 10-15 min | Low (dialogue, choices) |

## Known Risks
- Step 2 fuel gate may surprise players who spent fuel on optional travel
- Step 8 terminal destruction can feel punishing if player doesn't realize terminals are destructible
- Choice B in Step 10 has a hidden skill check that may feel unfair to players who didn't invest in Charisma
- Ending C being locked by Step 8 failure is not communicated to the player
