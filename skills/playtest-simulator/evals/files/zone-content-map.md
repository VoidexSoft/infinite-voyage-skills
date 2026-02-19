# Zone Content Map: The Shattered Relay (Sector 7-G)

## Zone Overview

- **Level range:** 18-22
- **Biome:** Derelict orbital station, partially collapsed into an ice moon's crust
- **Estimated clear time:** 45-60 minutes (critical path), 90-120 minutes (full clear)
- **Entry requirement:** Main quest "Signal in the Static" Act 2 started
- **Exit points:** 2 (main hangar, emergency airlock)

## Critical Path Encounters

### E1 — Docking Bay Ambush
- **Type:** Combat
- **Enemies:** 4x Scrap Drones (level 18), 1x Corrupted Loader Bot (level 19, mini-boss)
- **Mechanics:** Loader Bot has a magnetic pull that drags players into melee; drones flank from vents
- **Terrain:** Open bay with cargo containers for cover, 2 explosive fuel cells on the ground
- **Drops:** Standard loot table, Loader Bot drops Relay Access Keycard

### E2 — Atrium Pressure Puzzle
- **Type:** Puzzle
- **Mechanic:** Reroute coolant through 3 valve terminals to repressurize the central atrium. Valves must be activated within 30 seconds of each other or they reset.
- **Fail state:** None (puzzle resets indefinitely)
- **Hint system:** Environmental sparks show which pipes are active

### E3 — Command Deck Defense
- **Type:** Combat (wave survival)
- **Wave 1:** 6x Scrap Drones (level 18)
- **Wave 2:** 3x Void Stalkers (level 20, stealth melee), 2x Scrap Drones
- **Wave 3:** 1x Relay Overseer (level 22, boss — see Boss section)
- **Duration:** ~8 minutes total
- **Terrain:** Elevated command platform with 3 access corridors, 1 turret (player-activatable)
- **Fail state:** If all terminals destroyed, mission branch shifts to "salvage" ending

### E4 — Reactor Bypass
- **Type:** Navigation / Light puzzle
- **Mechanic:** Zero-gravity traversal through irradiated reactor core. Radiation ticks for 2% max HP/second. Three shielded rest points along the route.
- **Estimated time:** 2-3 minutes
- **Fail state:** Death by radiation (respawn at entrance)

## Boss Encounter

### Relay Overseer (Level 22)
- **HP:** 45,000
- **Phases:**
  - **Phase 1 (100-60% HP):** Ranged energy blasts, spawns 2 Scrap Drones every 45 seconds, vulnerable during "System Recalibration" channel (5 sec window)
  - **Phase 2 (60-30% HP):** Activates station defense grid (rotating laser beams across arena), increased attack speed, drones now level 20
  - **Phase 3 (30-0% HP):** Enrage — all attacks deal 50% more damage, no more drones but fires homing missiles (3-missile salvo every 10 seconds)
- **Key mechanic:** Recalibration windows are the only time bonus damage applies; missing them extends the fight significantly
- **Drops:** 1x Overseer's Circuit (quest item), 1x rare-quality weapon (from loot table "relay-weapons"), 350 Astral Credits

## Optional Content / Secrets

### S1 — Crew Quarters (Hidden Area)
- **Access:** Hack a side terminal in the Docking Bay (requires Hacking skill rank 3 or a Bypass Module consumable)
- **Content:** 3 lore datapads (Crew Logs #14, #15, #16 — chronicle the station's last days), 1 supply cache (2x Med Hypos, 50 Astral Credits)
- **Narrative:** Reveals the Overseer was once the station's AI caretaker, corrupted by a Void signal
- **Reward flag:** Discovering all 3 logs unlocks dialogue option with NPC Kael in Act 3

### S2 — Ventilation Shaft Network
- **Access:** Crouch-enter vent in Atrium (partially hidden behind collapsed beam, visible with scanner pulse)
- **Content:** Shortcut connecting Docking Bay to Command Deck (bypasses E2 entirely), contains 1 lore datapad (Engineering Note), 1 rare crafting material (Stabilized Void Shard)
- **Risk:** 2x Vent Crawlers (level 19, ambush in narrow space — limited dodge room)
- **Narrative:** Engineering Note hints at a failsafe code usable during the boss fight

### S3 — Observation Lounge
- **Access:** During E3, after Wave 1, a blast door briefly opens (15-second window). Requires player to notice and choose to leave the defense zone.
- **Content:** Panoramic view of the ice moon (cosmetic screenshot moment), 1 unique cosmetic item (Shattered Relay Hologram — ship decoration), 1 lore datapad
- **Risk:** Leaving the defense zone during waves means terminals take undefended damage

### S4 — Hidden Reactor Cache
- **Access:** During E4, deviate from the marked path to reach a side chamber (requires 4 seconds of extra radiation exposure beyond nearest rest point)
- **Content:** 1x Experimental Reactor Core (epic crafting material, used in 2 endgame recipes), 200 Astral Credits
- **Risk:** Tight HP check — players below 60% HP will likely die from radiation

### S5 — Overseer's Memory Core (Boss Secret)
- **Access:** Use the failsafe code from S2's Engineering Note during the Overseer's Phase 2 Recalibration window (specific input, not prompted)
- **Content:** Skips Phase 3 entirely, Overseer "remembers" its original purpose. Unlocks unique quest reward variant: Overseer's Gratitude (AI companion module) instead of standard weapon drop.
- **Narrative:** Ties into the Void corruption storyline, referenced again in Act 4

## Lore Collectibles

| ID | Name | Location | Part of Set? |
|----|------|----------|--------------|
| L1 | Crew Log #14 | S1 — Crew Quarters | Yes (Shattered Relay set, 5/8) |
| L2 | Crew Log #15 | S1 — Crew Quarters | Yes (Shattered Relay set, 6/8) |
| L3 | Crew Log #16 | S1 — Crew Quarters | Yes (Shattered Relay set, 7/8) |
| L4 | Engineering Note | S2 — Ventilation Shaft | Yes (Shattered Relay set, 8/8) |
| L5 | Final Transmission | Observation Lounge (S3) | No (standalone) |
| L6 | Overseer Protocol | Auto-collected during boss fight | No (standalone) |

## Collectible Progress Notes
- Crew Logs #1-#13 are found in earlier zones (Sectors 5, 6, and 7-A through 7-F)
- Completing the full Shattered Relay set (8/8) awards the achievement "Every Signal Tells a Story" and unlocks a lore codex entry
- L4 (Engineering Note) is required to access secret S5; missing it locks the player out of the alternate boss ending

## Zone Economy

| Activity | Astral Credits | XP | Estimated Time |
|----------|---------------|----|----------------|
| Critical path clear | 500 | 3,200 | 45-60 min |
| Full clear (all secrets) | 1,100 | 4,800 | 90-120 min |
| Boss only (speedrun) | 350 | 1,400 | 8-12 min |
| Repeatable (daily reset) | 250 (reduced) | 1,600 | 30-40 min |
