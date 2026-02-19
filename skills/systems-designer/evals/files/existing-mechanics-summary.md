# Infinite Voyage — Existing Mechanics Summary

This document summarizes all currently designed and implemented game systems in Infinite Voyage. Use this as context when designing new mechanics or analyzing system interactions.

---

## 1. Combat System

### Melee Combat
- Light attacks (fast, low damage, low stamina cost)
- Heavy attacks (slow, high damage, high stamina cost, can stagger)
- Dodge roll (i-frames, stamina cost, directional)
- Block/parry (shield-based, timing-dependent parry window of 0.2s)
- Stagger mechanic: enemies have a stagger bar that fills from heavy attacks and parries

### Ranged Combat
- Energy weapons: hitscan, consume Energy Cells
- Projectile weapons: travel time, consume Ammo
- Overheating mechanic: sustained fire builds heat; overheated weapons lock for 3s
- Aim assist: slight magnetism at close-medium range, none at long range

### Status Effects
- **Burn:** DoT, 5 damage/s for 8s, stacks up to 3 times
- **Freeze:** Slows movement by 40% for 6s; at 3 stacks, hard-freezes for 2s
- **Shock:** Chains to nearby enemies within 5m, damage splits per jump
- **Void Corruption:** Reduces healing received by 50% for 10s
- **Bleed:** DoT, 3 damage/s for 12s, movement increases bleed damage

## 2. Movement & Traversal

- Walking, sprinting (costs stamina), crouching, sliding
- Jetpack: short vertical boost, limited fuel that regenerates
- Grapple hook: swing traversal, attaches to designated anchor points
- Zero-G movement: in space segments, 6-DOF movement with inertia
- Fast travel: unlockable warp beacons at discovered locations

## 3. Stamina System

- Max stamina: 100 (base), scales with Endurance attribute
- Regeneration: 15/s after 1.5s of no stamina use
- Costs: Sprint (10/s), Dodge (25), Light attack (10), Heavy attack (30), Block (5/s while blocking), Parry attempt (15)
- Stamina break: at 0 stamina, player is vulnerable for 1s (cannot dodge or block)
- Currently NO regen-while-acting mechanic. Full stop on regen during any stamina-consuming action

## 4. Progression System

### Experience & Leveling
- XP gained from: combat kills, quest completion, exploration discoveries, crafting
- Level cap: 50
- Each level grants 3 attribute points and 1 skill point

### Attributes
- **Might:** Melee damage, stagger damage, carry weight
- **Precision:** Ranged damage, crit chance, aim assist range
- **Endurance:** Max stamina, stamina regen, max HP
- **Intellect:** Ability damage, cooldown reduction, scan range
- **Resolve:** Status effect resistance, shield strength, dialogue options

### Skill Trees
- Four trees: Vanguard (melee), Sharpshooter (ranged), Technomancer (abilities), Explorer (traversal/utility)
- Each tree has 20 nodes, branching paths
- Ultimate ability unlocked at tree depth 15

## 5. Economy

### Currencies
- **Credits:** Primary currency, earned from quests, loot sales, bounties
- **Void Shards:** Rare currency from elite enemies and Rift events, used for high-tier crafting
- **Reputation Tokens:** Faction-specific, earned through faction missions

### Vendors
- General vendor: basic supplies, ammo, consumables
- Faction vendors: unique gear locked behind reputation thresholds
- Black market: rare items, rotating stock, higher prices

## 6. Crafting System

- Workbench-based: must be at a crafting station
- Recipe discovery: found via exploration, quest rewards, or experimentation
- Material tiers: Common, Uncommon, Rare, Exotic
- Gear can be upgraded up to +5 at a workbench (costs escalate per tier)
- Consumable crafting: health packs, stamina boosters, elemental grenades
- Mod crafting: attach mods to weapons/armor for stat bonuses or effects

## 7. Inventory & Equipment

- Weight-based inventory (carry capacity from Might attribute)
- Equipment slots: Helmet, Chest, Legs, Boots, Weapon 1, Weapon 2, Shield/Gadget, 3 Accessory slots
- Gear rarity: Common (white), Uncommon (green), Rare (blue), Epic (purple), Legendary (orange)
- Set bonuses: wearing 2/3/4 pieces of a set grants escalating bonuses
- Quick-use bar: 4 consumable slots accessible during combat

## 8. Ability System

- Each player has 4 ability slots (mapped to inputs)
- Abilities unlocked from skill trees
- Each ability has: cast time, cooldown, resource cost (stamina or energy), effect
- Ability synergies: certain abilities combo (e.g., Freeze + Shatter = AoE ice explosion)
- Ultimate abilities: long cooldown (120s), high impact, unlocked deep in skill trees

## 9. Ship Systems (Hub & Travel)

- Player ship serves as hub: storage, crafting stations, crew quarters
- Ship upgrades: engine (travel speed), hull (durability), scanner (discovery range), cargo (storage)
- Star map navigation: select destination, travel time based on distance and engine level
- Ship combat: separate system, turret-based, not yet fully designed

## 10. Narrative & Quest System

- Main storyline: 40+ hour campaign across 8 star systems
- Side quests: faction missions, bounties, exploration tasks, crew personal quests
- Dialogue system: branching choices influenced by Resolve attribute
- Lore fragments: collectible text/audio logs that fill in world history
- Reputation system: 5 factions, actions affect standing, unlocks faction content

## 11. Multiplayer

- 2-4 player co-op for all content
- Shared world, instanced loot
- Difficulty scales with player count (+50% enemy HP per additional player)
- Revive mechanic: downed players can be revived within 15s
- No friendly fire in co-op
- PvP: dedicated arenas, separate from PvE, gear normalized to prevent power gaps
