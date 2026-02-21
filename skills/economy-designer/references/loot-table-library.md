# Loot Table Library

A reference library of loot table patterns. Contains reusable
templates, rarity tier definitions, weighted distribution examples, pity systems,
and seasonal loot mechanics.

---

## Rarity Tier Definitions

All items in Infinite Voyage follow a five-tier rarity system. Each tier has
standardized drop rates, visual indicators, and value expectations.

| Tier | Color | Base Drop Rate | Power Budget | Sell Value (Gold) | Salvage Yield |
|------|-------|----------------|--------------|-------------------|---------------|
| Common | White | 55-70% | 1.0x | 5-20 | 1 Scrap |
| Uncommon | Green | 20-30% | 1.3x | 25-75 | 2 Scraps |
| Rare | Blue | 8-12% | 1.7x | 100-300 | 5 Scraps |
| Epic | Purple | 2-5% | 2.2x | 500-1,500 | 12 Scraps |
| Legendary | Orange | 0.5-2% | 3.0x | 2,000-10,000 | 30 Scraps |

### Power Budget Rule

An item's power budget determines how strong it is relative to its level. A Rare
sword at level 20 deals 1.7x the damage of a Common sword at level 20. This
ensures rarity always feels meaningful without making common items useless.

---

## Pattern 1: Standard Enemy Drop Table

Used for regular overworld enemies. High common rate, no legendary drops.

```json
{
  "loot_table_id": "overworld_enemy_standard",
  "source": "Standard overworld enemies (wolves, bandits, etc.)",
  "rolls": 1,
  "nothing_weight": 30,
  "weighted_drops": [
    {
      "pool": "junk",
      "weight": 35,
      "items": ["torn_cloth", "cracked_bone", "dull_fang"],
      "quantity": { "min": 1, "max": 2 },
      "rarity": "common"
    },
    {
      "pool": "consumable",
      "weight": 20,
      "items": ["minor_health_potion", "minor_mana_potion"],
      "quantity": { "min": 1, "max": 1 },
      "rarity": "common"
    },
    {
      "pool": "currency",
      "weight": 10,
      "items": ["gold"],
      "quantity": { "min": 5, "max": 15 },
      "rarity": "common"
    },
    {
      "pool": "equipment",
      "weight": 5,
      "items": ["level_appropriate_gear"],
      "quantity": { "min": 1, "max": 1 },
      "rarity": "uncommon"
    }
  ],
  "total_weight": 100,
  "notes": "30% chance of no drop. Keeps inventory clean for overworld farming."
}
```

---

## Pattern 2: Dungeon Boss Drop Table

Used for end-of-dungeon bosses. Guaranteed drops plus weighted bonus rolls.

```json
{
  "loot_table_id": "dungeon_boss_tier2",
  "source": "Tier 2 dungeon bosses (level 20-30)",
  "guaranteed_drops": [
    {
      "item": "gold",
      "quantity": { "min": 200, "max": 500 }
    },
    {
      "item": "dungeon_crystal",
      "quantity": { "min": 3, "max": 5 }
    }
  ],
  "bonus_rolls": 2,
  "weighted_drops": [
    {
      "pool": "equipment_uncommon",
      "weight": 45,
      "rarity": "uncommon",
      "items": ["boss_specific_uncommon_set"],
      "quantity": { "min": 1, "max": 1 }
    },
    {
      "pool": "equipment_rare",
      "weight": 30,
      "rarity": "rare",
      "items": ["boss_specific_rare_set"],
      "quantity": { "min": 1, "max": 1 }
    },
    {
      "pool": "equipment_epic",
      "weight": 15,
      "rarity": "epic",
      "items": ["boss_specific_epic_set"],
      "quantity": { "min": 1, "max": 1 }
    },
    {
      "pool": "equipment_legendary",
      "weight": 5,
      "rarity": "legendary",
      "items": ["boss_unique_legendary"],
      "quantity": { "min": 1, "max": 1 }
    },
    {
      "pool": "crafting_materials",
      "weight": 5,
      "rarity": "rare",
      "items": ["boss_essence", "enchanted_shard"],
      "quantity": { "min": 1, "max": 3 }
    }
  ],
  "total_weight": 100,
  "first_clear_bonus": {
    "enabled": true,
    "extra_rolls": 1,
    "guaranteed_rarity_minimum": "rare"
  }
}
```

---

## Pattern 3: World Boss / Raid Boss Table

High-value encounters with group loot distribution.

```json
{
  "loot_table_id": "world_boss_weekly",
  "source": "Weekly world boss encounter",
  "loot_distribution": "personal",
  "lockout": "weekly",
  "guaranteed_drops_per_player": [
    { "item": "gold", "quantity": { "min": 1000, "max": 2000 } },
    { "item": "boss_trophy", "quantity": { "min": 1, "max": 1 } }
  ],
  "personal_rolls": 3,
  "weighted_drops": [
    { "pool": "rare_gear", "weight": 40, "rarity": "rare" },
    { "pool": "epic_gear", "weight": 25, "rarity": "epic" },
    { "pool": "legendary_gear", "weight": 5, "rarity": "legendary" },
    { "pool": "crafting_rare", "weight": 20, "rarity": "rare" },
    { "pool": "mount_fragment", "weight": 10, "rarity": "epic",
      "notes": "Collect 20 fragments to assemble legendary mount" }
  ],
  "total_weight": 100,
  "pity_system": {
    "enabled": true,
    "type": "legendary_guarantee",
    "threshold": 12,
    "description": "After 12 kills without a legendary, next kill guarantees one"
  }
}
```

---

## Pattern 4: Crafting Gathering Node

For resource nodes in the world (mining, herbalism, logging).

```json
{
  "loot_table_id": "iron_ore_node",
  "source": "Iron ore deposits (zones level 15-25)",
  "rolls": 1,
  "guaranteed_drops": [
    { "item": "iron_ore", "quantity": { "min": 2, "max": 4 } }
  ],
  "weighted_drops": [
    { "pool": "bonus_ore", "weight": 60,
      "items": [{ "item": "iron_ore", "quantity": { "min": 1, "max": 2 } }] },
    { "pool": "rare_ore", "weight": 25,
      "items": [{ "item": "silver_ore", "quantity": { "min": 1, "max": 1 } }] },
    { "pool": "gem", "weight": 10,
      "items": [{ "item": "rough_sapphire", "quantity": { "min": 1, "max": 1 } }] },
    { "pool": "rare_gem", "weight": 5,
      "items": [{ "item": "flawless_sapphire", "quantity": { "min": 1, "max": 1 } }] }
  ],
  "total_weight": 100,
  "skill_bonus": {
    "description": "Mining skill level adds bonus quantity",
    "formula": "base_quantity + floor(mining_skill / 25)"
  }
}
```

---

## Pattern 5: Treasure Chest (Tiered)

Chests found in the world scale with zone difficulty.

```json
{
  "loot_table_id": "treasure_chest_tiered",
  "variants": {
    "wooden_chest": {
      "rolls": 2,
      "rarity_cap": "uncommon",
      "gold_range": [10, 50],
      "distribution": { "common": 75, "uncommon": 25 }
    },
    "iron_chest": {
      "rolls": 3,
      "rarity_cap": "rare",
      "gold_range": [50, 200],
      "distribution": { "common": 50, "uncommon": 30, "rare": 20 }
    },
    "gold_chest": {
      "rolls": 3,
      "rarity_cap": "epic",
      "gold_range": [200, 750],
      "distribution": { "uncommon": 40, "rare": 35, "epic": 25 }
    },
    "legendary_chest": {
      "rolls": 4,
      "rarity_cap": "legendary",
      "gold_range": [500, 2000],
      "distribution": { "rare": 40, "epic": 35, "legendary": 25 }
    }
  }
}
```

---

## Pity System Implementations

Pity systems prevent extreme bad luck from ruining player experience. Three
standard implementations:

### Counter-Based Pity

The simplest model. A hidden counter tracks attempts without the target rarity.
When the counter hits the threshold, the next drop is guaranteed.

```json
{
  "pity_system": "counter",
  "target_rarity": "legendary",
  "base_drop_rate": 0.02,
  "hard_pity_threshold": 50,
  "description": "After 50 boss kills without a legendary, kill 51 guarantees one."
  }
```

**Effective drop rate**: With 2% base rate and hard pity at 50, the effective
rate is approximately 2.6% (accounting for pity triggers).

### Escalating Probability Pity

Drop rate increases with each failed attempt, creating a soft pity curve.

```json
{
  "pity_system": "escalating",
  "target_rarity": "epic",
  "base_drop_rate": 0.05,
  "escalation_start": 15,
  "escalation_rate": 0.03,
  "hard_pity_threshold": 30,
  "example_rates": {
    "attempt_1": 0.05,
    "attempt_15": 0.05,
    "attempt_16": 0.08,
    "attempt_20": 0.20,
    "attempt_25": 0.35,
    "attempt_30": 1.00
  }
}
```

### Token Accumulation Pity

Failed rolls award consolation tokens. Tokens can be exchanged for a guaranteed
item once enough are collected.

```json
{
  "pity_system": "token_accumulation",
  "token_name": "echo_shard",
  "tokens_per_failed_roll": 1,
  "tokens_for_guarantee": 40,
  "target_rarity": "legendary",
  "exchange_vendor": "Echo Merchant",
  "notes": "Players always feel progress even on bad luck streaks"
}
```

---

## Guaranteed Drop Mechanics

Some drops should always occur regardless of RNG. Use guaranteed drops for:

| Scenario | Guaranteed Drop | Reason |
|----------|-----------------|--------|
| First dungeon clear | Rare+ item | Rewards exploration, validates effort |
| Quest completion | Specified quest reward | Player earned it through objectives |
| Boss kill (any) | Gold + dungeon currency | Economy floor, ensures time is never wasted |
| Achievement milestone | Cosmetic or title | Celebration of long-term commitment |
| Season first login | Seasonal currency starter | Onboarding into seasonal content |

### Anti-Farming Protection

For guaranteed drops that should only happen once, use lockout flags:

```json
{
  "guaranteed_drop": "ancient_relic",
  "lockout": {
    "type": "per_character",
    "resets": "never",
    "flag": "has_received_ancient_relic"
  }
}
```

---

## Seasonal Loot Tables

Seasonal loot rotates every 60 days with themed content.

```json
{
  "loot_table_id": "winter_festival_2026",
  "season": "Frostbound Festival",
  "duration": "60 days",
  "availability": "Seasonal event zones and activities only",
  "currency": "voyage_tokens",
  "exclusive_drops": [
    {
      "item": "frostbound_cloak",
      "rarity": "epic",
      "type": "cosmetic",
      "source": "Seasonal dungeon boss",
      "drop_rate": 0.10,
      "tradeable": false
    },
    {
      "item": "ice_crystal_mount",
      "rarity": "legendary",
      "type": "cosmetic",
      "source": "Seasonal world boss",
      "drop_rate": 0.02,
      "pity": { "type": "counter", "threshold": 30 },
      "tradeable": false
    }
  ],
  "returning_items": {
    "enabled": true,
    "description": "Previous seasonal items return at reduced rate after 2 seasons",
    "rate_modifier": 0.5
  },
  "post_season": {
    "drops_cease": true,
    "tokens_convert": { "to": "gold", "ratio": "1:2" },
    "items_remain": "Owned items kept permanently"
  }
}
```

---

## Weighted Distribution Calculator

Use this formula to validate any loot table before shipping:

```python
def validate_distribution(table):
    """Validate loot table weights and expected outcomes."""
    total_weight = sum(entry["weight"] for entry in table["weighted_drops"])
    if table.get("nothing_weight"):
        total_weight += table["nothing_weight"]

    results = {}
    for entry in table["weighted_drops"]:
        actual_rate = entry["weight"] / total_weight
        results[entry["pool"]] = {
            "weight": entry["weight"],
            "drop_rate": round(actual_rate, 4),
            "per_100_kills": round(actual_rate * 100, 1)
        }

    # Verify weights sum correctly
    assert total_weight == 100, f"Weights sum to {total_weight}, expected 100"
    return results


def expected_attempts_to_drop(drop_rate, pity_threshold=None):
    """Calculate expected attempts needed for at least one drop."""
    if pity_threshold:
        # With pity, expected attempts is bounded
        expected = sum(
            (1 - drop_rate) ** (k - 1) * drop_rate * k
            for k in range(1, pity_threshold)
        ) + (1 - drop_rate) ** (pity_threshold - 1) * pity_threshold
        return round(expected, 1)
    else:
        # Without pity, geometric distribution
        return round(1 / drop_rate, 1)
```

### Quick Reference: Attempts to Drop

| Drop Rate | Without Pity | With Pity (50) | With Pity (30) |
|-----------|-------------|-----------------|-----------------|
| 50% | 2 | 2.0 | 2.0 |
| 20% | 5 | 5.0 | 5.0 |
| 10% | 10 | 9.8 | 9.5 |
| 5% | 20 | 18.6 | 16.8 |
| 2% | 50 | 36.4 | 25.8 |
| 1% | 100 | 44.4 | 27.5 |
| 0.5% | 200 | 48.5 | 29.3 |

---

## Loot Table Audit Checklist

Run this checklist on every loot table before it goes live:

```
[ ] All weights sum to exactly 100
[ ] No individual item has a drop rate below 0.1% without a pity system
[ ] Guaranteed drops are present for boss encounters
[ ] Gold/currency is included as a floor reward
[ ] Legendary items have pity systems attached
[ ] Seasonal items are flagged with expiration metadata
[ ] Quantity ranges have min <= max
[ ] First-clear bonuses are defined for new content
[ ] No item appears in multiple pools within the same table (prevents double-dipping)
[ ] Drop rates have been validated with 100,000-run simulation
```
