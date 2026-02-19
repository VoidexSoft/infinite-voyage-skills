# Quest Design Document: "The Cartographer's Gambit"

## Quest Metadata
- **Quest ID:** SQ-7G-03
- **Type:** Side quest (multi-step, branching)
- **Level range:** 19-21
- **Zone:** Sector 7-G periphery (Frozen Drift asteroid field)
- **Giver:** NPC Fen Alizari (freelance cartographer, found at Waystation Omega cantina)
- **Estimated duration:** 40-60 minutes
- **Prerequisites:** Act 2, Step 2 complete (player has reached Sector 7-G)

## Quest Summary
Fen Alizari, a freelance cartographer, has discovered coordinates to a pre-Collapse survey ship frozen in the Frozen Drift asteroid field. The ship's star charts could be worth a fortune to the right buyer — or could reveal a hidden route through the Void Shroud that multiple factions would kill to control. The player must retrieve the charts and decide who benefits from the discovery.

## Quest Hook
Fen approaches the player in the Waystation Omega cantina after overhearing them mention the Shattered Relay. She offers a partnership: her coordinates for the player's ship and combat ability. The split is 50/50 on whatever they find.

**Hook dialogue trigger:** Player enters cantina after completing main quest Step 4 (has Relay Access Keycard in inventory, signaling they're capable).

## Quest Steps

### Step 1: Meet Fen at the Frozen Drift
- **Objective:** Travel to provided coordinates in the Frozen Drift
- **Gate:** Ship fuel >= 10 units
- **On arrival:** Cutscene — massive derelict survey ship embedded in an asteroid, partially cracked open by ice expansion
- **Fen dialogue:** Explains the ship is the CSV Meridian, lost 200 years ago during the Collapse. Its navigational AI was mapping routes through unstable space.

### Step 2: Board the CSV Meridian
- **Objective:** Find a way inside the derelict
- **Approach options:**
  - **A) Dock at main airlock** — Straightforward but triggers security drones (combat encounter)
  - **B) Cut through the hull breach** — Requires Plasma Cutter tool (purchasable at Waystation, 200 credits) but avoids security entirely
  - **C) Hack the docking clamps remotely** — Requires Hacking skill rank 4; silent entry, security drones remain dormant for the entire quest
- **Combat (if triggered):** 3x Survey Sentinel Drones (level 19), patrol pattern — they activate in pairs if one is alerted

### Step 3: Navigate to the Bridge
- **Objective:** Reach the ship's bridge to access the navigational AI
- **Environment:** Zero-gravity interior, debris fields, occasional hull groans (atmospheric audio)
- **Encounters along the route:**
  - **3A — Cargo Bay:** 2x Ice Lurkers (level 19, organic enemies nested in the derelict). Loot: 3x Cryo Compound (crafting material), 75 Astral Credits in salvage
  - **3B — Crew Memorial:** No combat. A makeshift shrine with crew photos and personal effects. Lore datapad: "Captain Vasik's Final Order" (reveals the captain deliberately hid the ship to keep the charts out of Coalition hands during the Collapse). Fen reacts emotionally — she's a descendant of one of the crew.
  - **3C — Engineering Bypass:** Optional shortcut. Requires solving a power routing puzzle (reroute 3 power nodes in sequence within 20 seconds). Success: skip the last corridor and its patrol. Failure: power surge alerts remaining security drones.

### Step 4: Access the Navigational AI
- **Objective:** Interface with the ship's AI core on the bridge
- **Event:** The AI (designation: MERIDIAN) is still partially functional. It recognizes Fen as a crew descendant and speaks to her directly.
- **Revelation:** The star charts don't just show a route through the Void Shroud — they show the location of a Void Anchor, an artifact that could stabilize or weaponize Void energy.
- **Fen's reaction:** She's shaken. This is bigger than a payday. She defers to the player.

### Step 5: DECISION POINT — What to do with the star charts

#### Branch A: "Sell the charts to the Meridian Syndicate"
- **Fen's stance:** Reluctantly agrees. "Credits are credits. But this feels wrong."
- **Contact:** NPC broker Tallis Vek (holographic comm from bridge console)
- **Reward:**
  - 1,500 Astral Credits (split: 750 to player, 750 to Fen)
  - Syndicate Reputation +300
  - Tallis Vek becomes a recurring vendor with black market items
- **Consequence:**
  - Syndicate begins mobilizing toward the Void Anchor (referenced in Act 4)
  - Fen leaves the player's crew with her share; available as a quest giver in Act 4 but relationship is transactional
- **Alignment:** +10 Pragmatism

#### Branch B: "Hand the charts to the Vanguard Coalition"
- **Fen's stance:** Opposes. "The Coalition will weaponize this. That's exactly what Captain Vasik was trying to prevent."
- **If player insists:** Fen argues but ultimately complies. Companion loyalty -2 (or -1 if player passes a Persuasion check, Charisma 16).
- **Contact:** Coalition Commander Dreyar (remote comm)
- **Reward:**
  - 600 Astral Credits (official salvage bounty)
  - Coalition Reputation +500
  - Unique item: Coalition Survey Badge (trinket, +10% scan range)
- **Consequence:**
  - Coalition secures the route and begins fortifying it (affects Act 4 balance of power)
  - Fen becomes distant; still available as quest giver but dialogue is colder
- **Alignment:** +10 Order, +5 Duty

#### Branch C: "Destroy the charts — some things should stay hidden"
- **Fen's stance:** Strongly approves. "Captain Vasik would have wanted this. Some maps are better left undrawn."
- **Action:** Player and Fen overload the AI core, wiping the data permanently
- **Reward:**
  - 0 Astral Credits (no buyer)
  - Fen joins the player's crew as a permanent companion (Cartographer class — provides passive scan bonuses and unique exploration dialogue)
  - Unique achievement: "Uncharted by Choice"
  - Hidden reward: MERIDIAN's gratitude — the AI fragments into a subroutine that inhabits the player's ship, providing occasional navigation hints for the rest of the game
- **Consequence:**
  - No faction gains the Void Anchor location; it becomes a mystery thread in Act 4
  - Strongest narrative payoff but zero economic reward
- **Alignment:** +15 Curiosity, +5 Compassion

## Reward Summary

| Branch | Credits | Reputation | Unique Item | Companion | Story Impact |
|--------|---------|------------|-------------|-----------|-------------|
| A (Sell) | 750 | Syndicate +300 | Vendor unlock | Fen leaves | Syndicate empowered |
| B (Coalition) | 600 | Coalition +500 | Survey Badge | Fen distant | Coalition fortified |
| C (Destroy) | 0 | None | Achievement + AI | Fen joins crew | Mystery preserved |

## Failure States

- **Player death during combat:** Respawn at last checkpoint (start of current step), enemies reset
- **Fen dies:** Cannot happen (she's flagged as essential during quest). She takes a knee at 10% HP and recovers after combat.
- **Player leaves the zone mid-quest:** Quest pauses. Fen sends a message: "Waiting at the Meridian. Don't leave me hanging." Quest marker persists.
- **Player already hostile with Syndicate (Branch A):** Tallis Vek still deals; Syndicate is pragmatic. Dialogue acknowledges tension.
- **Player already hostile with Coalition (Branch B):** Commander Dreyar is suspicious but accepts the charts. Reputation gain is halved (+250 instead of +500).

## Fen Alizari — NPC Profile

- **Role:** Quest giver, potential companion
- **Personality:** Witty, morally flexible but has a conscience. Motivated by curiosity as much as profit.
- **Combat style (if companion):** Mid-range support. Uses scanner drones for enemy tagging and area-of-effect EMP bursts.
- **Voice tone:** Sardonic, warm. Think a smuggler who reads poetry in her downtime.
- **Key relationship stat:** Loyalty (starts at 5/10, modified by quest choices)

## Design Notes

- Branch C is intentionally the "worst" economic choice but the "best" narrative/companion choice. This tests whether the player optimizes for credits or story.
- The Crew Memorial (3B) is placed deliberately before the decision point to emotionally prime the player toward Branch C without forcing it.
- Fen's descendant reveal in Step 4 should feel earned, not contrived — the clues are in her dialogue during Steps 1-3 (she knows too much about the Meridian's layout for a "random" cartographer).
