# Ability Power Budget -- Infinite Voyage

## Power Budget Formula

Every ability in Infinite Voyage must fit within a **power budget** calculated from
its level tier and role slot. The total power score of an ability must not exceed its
allocated budget, or it risks crowding out alternatives and collapsing build diversity.

```
Power Budget = BaseBudget(tier) + RoleBonus(role) + SlotModifier(slot)
```

### Base Budget by Tier

| Tier | Level Range | Base Budget |
|------|-------------|-------------|
| T1   | 1-10        | 100         |
| T2   | 11-20       | 180         |
| T3   | 21-35       | 280         |
| T4   | 36-50       | 400         |

### Role Bonus

| Role       | Bonus |
|------------|-------|
| DPS        | +20   |
| Tank       | +10   |
| Support    | +15   |
| Hybrid     | +0    |

### Slot Modifier

| Slot       | Modifier |
|------------|----------|
| Primary    | +30      |
| Secondary  | +15      |
| Utility    | +0       |
| Ultimate   | +60      |

## Component Weight Table

Each component of an ability contributes to its total power score:

| Component              | Weight Formula                          | Notes                              |
|------------------------|-----------------------------------------|------------------------------------|
| Base Damage            | damage / 10                             | Raw damage value divided by 10     |
| Damage over Time (DoT) | (tick_damage * ticks) / 12             | Total DoT divided by 12            |
| Healing                | heal_amount / 8                         | Healing is weighted higher          |
| Shield Grant           | shield_amount / 9                       | Slightly less than healing          |
| Crowd Control (stun)   | stun_duration * 25                      | 1s stun = 25 power                 |
| Crowd Control (slow)   | slow_pct * slow_duration * 15           | e.g., 0.4 * 3s * 15 = 18          |
| AoE Multiplier         | power_so_far * (targets - 1) * 0.3     | Each extra target adds 30% power   |
| Range Bonus            | +5 per 5m beyond 10m base              | Melee abilities get no bonus        |
| Cooldown Reduction     | -2 per second of cooldown above 8s     | Long CDs reduce power score         |
| Resource Cost          | -1 per 10 energy cost above 30         | High cost reduces power score       |

## Ability Under Review

**Ability Name:** Singularity Collapse
**Class:** Voidwalker (DPS)
**Tier:** T3 (Level 28)
**Slot:** Primary

### Stats

- Base Damage: 480
- DoT: 60 damage per tick, 5 ticks (300 total)
- Stun: 1.2 seconds
- AoE: hits up to 3 targets
- Range: 20m
- Cooldown: 10 seconds
- Energy Cost: 55

### Calculated Budget

```
Base Budget (T3):        280
Role Bonus (DPS):        +20
Slot Modifier (Primary): +30
-------------------------------
Total Budget:            330
```

### Task

Calculate the total power score of Singularity Collapse using the component weight
table above. Determine whether it is within budget, over budget, or under budget.
If over budget, recommend which components to reduce and by how much. If under budget
by more than 15%, flag it as potentially underwhelming.
