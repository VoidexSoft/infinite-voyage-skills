# Infinite Voyage — Ability Design Notes

Notes from the design meeting on class abilities. Four classes, three abilities each. These need to be organized into a comparison matrix so we can check balance across classes.

## Navigator (balanced generalist)

**Stellar Barrage** — The Navigator's bread-and-butter ranged attack. Fires a burst of plasma bolts dealing moderate damage (base 20) to a single target. 2-turn cooldown, costs 15 energy. Should scale well with Attack stat. Unlocks at level 1 so everyone has it immediately. We want this to be the "always available" damage option.

**Warp Dodge** — Defensive ability. Navigator phase-shifts briefly, gaining 40% dodge for 1 turn. Costs 20 energy, 4-turn cooldown. Unlocks at level 5. No damage component. The idea is that Navigators can survive by being slippery, not tanky. This should be compared against Vanguard's Fortress Mode for effective damage mitigation.

**Astral Surge** — Ultimate ability. Channels cosmic energy for 1 turn, then unleashes a massive AoE blast hitting all enemies for 45 base damage. 8-turn cooldown, costs 50 energy. Unlocks at level 15. This is the Navigator's "clear the room" move. High cost, high reward. Should feel impactful but not overshadow Arcanist's AoE options.

## Vanguard (tank / melee)

**Meteor Strike** — Heavy melee slam. Deals 30 base damage to single target and has a 25% chance to stun for 1 turn. 3-turn cooldown, costs 20 energy. Unlocks at level 1. The stun is the key differentiator — Vanguards control the battlefield. Damage is higher than Stellar Barrage to compensate for melee range.

**Fortress Mode** — Toggle ability (no cooldown but drains 8 energy per turn while active). Reduces all incoming damage by 35% but reduces movement to 0. Unlocks at level 6. This is the Vanguard's "hold the line" identity. Need to compare energy drain vs. Warp Dodge's burst cost — both are defensive but very different in feel.

**Orbital Drop** — Ultimate. Calls down a massive kinetic strike on a target area after a 2-turn delay. Deals 60 base damage in AoE. 10-turn cooldown, costs 45 energy. Unlocks at level 18. The delay is the downside — enemies can move out of the zone. But if it lands, it's the hardest single hit in the game. Compare with Astral Surge (instant but lower damage).

## Arcanist (magic DPS / support hybrid)

**Void Bolt** — Ranged magic attack. Deals 25 base damage and applies a "Void Mark" debuff that increases damage taken by 10% for 2 turns. 2-turn cooldown, costs 18 energy. Unlocks at level 1. The debuff is what makes this special — it's a force multiplier for the whole party. Slightly more expensive than Stellar Barrage to compensate.

**Nebula Shield** — Creates a shield on an ally that absorbs 30 damage. Lasts 3 turns or until broken. 5-turn cooldown, costs 25 energy. Unlocks at level 7. This is the Arcanist's support identity. Unlike Fortress Mode (self only) or Warp Dodge (self only), this can protect anyone. Trade-off: it doesn't reduce damage, it has a cap.

**Supernova** — Ultimate AoE. Detonates all Void Marks on the field, dealing 35 base damage + 15 bonus damage per mark detonated. No cap on marks. 9-turn cooldown, costs 55 energy. Unlocks at level 16. In theory, if Arcanist has been applying Void Marks for several turns, this could deal massive damage. But it requires setup. Compare vs. Astral Surge which is simpler but more reliable.

## Phantom (stealth / burst damage)

**Shadow Strike** — Melee attack from stealth. Deals 22 base damage, but if used from stealth, deals double damage (44 effective). 2-turn cooldown, costs 12 energy. Unlocks at level 1. Cheapest ability in the game energy-wise, but requires stealth positioning to maximize. Without stealth bonus it's actually the weakest starter ability.

**Vanish** — Enters stealth for 2 turns. While stealthed, next attack gets the stealth bonus and Phantom can't be targeted by single-target abilities. 6-turn cooldown, costs 22 energy. Unlocks at level 8. This is the enabler for Shadow Strike's double damage. The cooldown means Phantom can't stay stealthed permanently — there's a window of vulnerability.

**Singularity Blade** — Ultimate. A devastating single-target strike dealing 70 base damage. If used from stealth, also applies a 3-turn bleed for 10 damage per turn (100 total effective damage from stealth). 12-turn cooldown, costs 40 energy. Unlocks at level 20. Highest single-target damage in the game, but ONLY from stealth and ONLY single target. Compare with Orbital Drop (AoE, 60 damage) and Supernova (scaling AoE).
