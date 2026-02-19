# Zone Layout: Derelict Mining Complex — Asteroid K-19

## Overview

An abandoned asteroid mining facility spanning three vertical strata (Upper Docks, Mid-Level Refinery, and Deep Mines). The player enters from the Upper Docks and must descend to the Deep Mines to retrieve the Graviton Lens, a critical quest item. The complex has been overrun by Hive Drones — insectoid machines that have built organic-mechanical nests throughout the facility.

**Level range:** 18-22
**Estimated full completion time:** 50-70 minutes
**Critical path only time:** 30-40 minutes

## Rough Topology

```
UPPER DOCKS (Entry Level)
========================

[Docking Bay A] ---main corridor--- [Central Hub Upper] ---locked(Blue Keycard)--- [Control Tower]
      |                                     |                                           |
      |                                 [Elevator A]                              (overlooks Refinery
      |                                  (requires                                 for scouting)
[Supply Closet]                         power restore)
 (optional loot)

MID-LEVEL REFINERY
========================

                          [Elevator A landing] ---catwalk--- [Refinery Floor]
                                  |                               |
                          [Maintenance Shaft]              [Smelting Chamber]
                           (optional, dangerous,           ---locked(Red Keycard)--- [Foreman's Office]
                            shortcut to Deep Mines)              |                    (Red Keycard is HERE,
                                  |                        [Conveyor Belt              but also contains
                                  |                         Gauntlet]                  Blue Keycard)
                                  |                              |
                                  |                    [Cooling Tunnels]
                                  |                         |
                                  +---- both paths --->  [Elevator B]
                                                         (always operational)

DEEP MINES
========================

[Elevator B landing] ---narrow tunnel--- [Hive Nest Alpha] ---locked(Green Keycard)--- [Graviton Lens Chamber]
        |                                       |                                              |
   [Mining Cart Track]                    [Drone Breeding Pit]                          [BOSS: Hive Queen]
    (optional ride,                        (Green Keycard is                             (must defeat to
     leads to secret                        dropped by Pit                                claim Lens and
     loot cache)                            Guardian mini-boss)                           unlock exit)
                                                  |
                                          [Collapsed Tunnel]
                                           (one-way shortcut
                                            back to Upper Docks
                                            after boss defeat)
```

## Door and Key Inventory

| Door / Gate | Location | Key Required | Key Location | Optional? |
|---|---|---|---|---|
| Control Tower access | Upper Docks | Blue Keycard | Foreman's Office (Mid-Level) | Yes — provides scouting advantage and bonus loot |
| Foreman's Office | Mid-Level Refinery | Red Keycard | Smelting Chamber (dropped by Smelter Bot enemy) | No — required for critical path (contains Blue Keycard + progress route) |
| Graviton Lens Chamber | Deep Mines | Green Keycard | Drone Breeding Pit (dropped by Pit Guardian mini-boss) | No — required to complete zone |
| Maintenance Shaft gate | Mid-Level Refinery | None (always open) | N/A | Yes — dangerous shortcut that skips Conveyor Belt Gauntlet |
| Mining Cart Track | Deep Mines | None (always open) | N/A | Yes — leads to secret loot cache |

## Path Categories

### Critical Path (required)
1. Docking Bay A -> Central Hub Upper
2. Restore power to Elevator A (combat encounter in Central Hub)
3. Elevator A down to Mid-Level Refinery
4. Refinery Floor -> Smelting Chamber (combat, obtain Red Keycard)
5. Unlock Foreman's Office
6. Conveyor Belt Gauntlet OR Maintenance Shaft -> Cooling Tunnels
7. Elevator B down to Deep Mines
8. Hive Nest Alpha -> Drone Breeding Pit (mini-boss, obtain Green Keycard)
9. Unlock Graviton Lens Chamber
10. Defeat Hive Queen boss
11. Claim Graviton Lens, exit via Collapsed Tunnel shortcut

### Optional Branches
- **Supply Closet (Upper Docks):** Minor loot, no enemies. 2 minutes.
- **Control Tower (Upper Docks):** Requires backtracking with Blue Keycard from Mid-Level. Scouting advantage (marks enemies on map for Refinery). Bonus rare loot chest. 5 minutes.
- **Maintenance Shaft (Mid-Level):** Dangerous shortcut — high-level Hive Drones in tight corridors, no cover. Skips Conveyor Belt Gauntlet but is harder. 4 minutes.
- **Mining Cart Track (Deep Mines):** Scripted ride sequence, ends at hidden loot cache with Epic-tier equipment. 3 minutes.

## Encounter Locations (summary)

| Location | Encounter Type | Estimated Difficulty | Duration |
|---|---|---|---|
| Central Hub Upper | Combat (power restore defense) | Medium | 5 min |
| Refinery Floor | Combat (drone patrol) | Medium | 4 min |
| Smelting Chamber | Combat (Smelter Bot + adds) | Medium-Hard | 6 min |
| Conveyor Belt Gauntlet | Environmental/Combat hybrid | Hard | 7 min |
| Maintenance Shaft | Combat (tight quarters) | Hard | 4 min |
| Hive Nest Alpha | Combat (swarm encounter) | Medium | 5 min |
| Drone Breeding Pit | Mini-boss (Pit Guardian) | Hard | 8 min |
| Graviton Lens Chamber | Boss (Hive Queen) | Very Hard | 12 min |
