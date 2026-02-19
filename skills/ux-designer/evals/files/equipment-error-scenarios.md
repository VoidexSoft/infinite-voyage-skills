# Equipment Screen Error Scenarios — Infinite Voyage

These are the 6 error/edge-case scenarios that the UX designer must define complete UI states for on the item equipment screen.

---

## Scenario 1: Equipping an Item That Exceeds Power Capacity

**Context:** The player's exosuit has a power capacity rating (e.g., 100 units). Some high-tier equipment has a power draw. The player tries to equip a Quantum Shield Generator (power draw: 35) when only 20 units of capacity remain.

**Questions to resolve:**
- What message is displayed?
- Can the player still force-equip (with a penalty)?
- What visual indicator shows power is exceeded?
- Does the UI suggest which item to unequip to make room?

---

## Scenario 2: Equipping a Class-Restricted Item

**Context:** The player is a Navigator class and attempts to equip a "Vanguard Assault Chassis" that is restricted to the Vanguard class only.

**Questions to resolve:**
- When is the restriction communicated — before or after the equip attempt?
- Is the item grayed out in the list, or selectable but blocked on confirm?
- What message explains the restriction?
- Does the UI suggest an equivalent item for the player's class?

---

## Scenario 3: Equipping an Item While in Combat

**Context:** The player opens the equipment screen during active combat (the game allows pausing in single-player but not in co-op). In co-op mode, the game continues while the menu is open. The player tries to swap their primary weapon mid-fight.

**Questions to resolve:**
- Is equipment swapping allowed during combat at all?
- If allowed, is there a swap cooldown or animation?
- What happens to enemies targeting the player during the swap?
- What feedback tells the player the swap completed (or failed)?
- How does this differ between single-player (paused) and co-op (real-time)?

---

## Scenario 4: Equipping a Damaged / Broken Item

**Context:** The player's Photon Lance has 0 durability (broken). They unequip it for repairs but then try to re-equip it before repairing.

**Questions to resolve:**
- Can a broken item be equipped at all?
- If yes, what are the stat penalties and how are they displayed?
- What warning is shown when trying to equip a broken item?
- Is there a quick-repair option from the equip confirmation dialog?
- How does the item appear visually in the equipment slot (cracked icon, red overlay)?

---

## Scenario 5: Inventory Full When Unequipping

**Context:** The player has 60/60 inventory slots full. They try to unequip their current helmet to swap it for a new one. The unequipped helmet has nowhere to go.

**Questions to resolve:**
- Is the swap handled atomically (old item and new item swap slots directly)?
- If not atomic, what error message appears for full inventory?
- Does the UI suggest salvaging or dropping an item to make room?
- Can the player salvage directly from the equipment screen without navigating to inventory?
- What happens if the player tries to unequip without a replacement (just removing gear)?

---

## Scenario 6: Network Timeout During Equipment Change (Co-op)

**Context:** In co-op mode, equipment changes are synced to the server. The player confirms an equipment swap but the network request times out after 5 seconds.

**Questions to resolve:**
- What loading/pending state is shown while waiting for server confirmation?
- After timeout, is the item rolled back to its previous state?
- What error message is displayed?
- Can the player retry the action, and how?
- Are other equipment actions blocked during the pending state?
- How is the player's avatar shown to teammates during the pending state?
