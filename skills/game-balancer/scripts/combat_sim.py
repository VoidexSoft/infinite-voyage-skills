#!/usr/bin/env python3
"""
Monte Carlo combat simulator for game balancing.

Simulates combat encounters between attacker and defender with configurable
stats, abilities, armor formulas, critical hits, and dodge mechanics.

Outputs win rates, average time-to-kill, and damage statistics.
"""

import argparse
import json
import random
from pathlib import Path
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass


@dataclass
class CombatStats:
    """Container for combat statistics."""
    health: float
    attack_power: float
    armor: float
    critical_chance: float = 0.0
    critical_multiplier: float = 1.5
    dodge_chance: float = 0.0


@dataclass
class Ability:
    """Combat ability definition."""
    name: str
    cooldown: int  # turns
    damage_multiplier: float
    hit_chance: float = 1.0


class CombatSimulator:
    """Simulates combat encounters."""

    def __init__(
        self,
        attacker_stats: CombatStats,
        defender_stats: CombatStats,
        attacker_abilities: List[Ability] = None,
        defender_abilities: List[Ability] = None,
        armor_formula: str = 'flat',
        armor_value: float = 0.0,
        max_turns: int = 1000
    ):
        """
        Initialize combat simulator.

        Args:
            attacker_stats: Attacker's combat stats
            defender_stats: Defender's combat stats
            attacker_abilities: List of attacker abilities
            defender_abilities: List of defender abilities
            armor_formula: 'flat' (reduction) or 'percent' (reduction)
            armor_value: Armor damage reduction value
            max_turns: Maximum turns before combat ends (draw)
        """
        self.attacker_stats = attacker_stats
        self.defender_stats = defender_stats
        self.attacker_abilities = attacker_abilities or []
        self.defender_abilities = defender_abilities or []
        self.armor_formula = armor_formula
        self.armor_value = armor_value
        self.max_turns = max_turns

    def calculate_damage(self, attacker: CombatStats, defender: CombatStats) -> float:
        """
        Calculate damage with armor reduction.

        Args:
            attacker: Attacking combatant
            defender: Defending combatant

        Returns:
            Damage dealt after armor
        """
        base_damage = attacker.attack_power

        # Check critical hit
        if random.random() < attacker.critical_chance:
            base_damage *= attacker.critical_multiplier

        # Apply armor
        if self.armor_formula == 'flat':
            damage = max(1, base_damage - self.armor_value)
        elif self.armor_formula == 'percent':
            damage = base_damage * (1 - self.armor_value / 100)
        else:
            damage = base_damage

        return damage

    def can_hit(self, combatant: CombatStats, ability: Ability = None) -> bool:
        """
        Check if attack hits (dodge + ability hit chance).

        Args:
            combatant: Attacking combatant
            ability: Optional ability being used

        Returns:
            True if attack hits
        """
        # Check dodge
        if random.random() < combatant.dodge_chance:
            return False

        # Check ability hit chance
        if ability and random.random() > ability.hit_chance:
            return False

        return True

    def get_next_action(
        self,
        abilities: List[Ability],
        cooldowns: Dict[str, int]
    ) -> Ability:
        """
        Get next ability to use (or None for basic attack).

        Args:
            abilities: Available abilities
            cooldowns: Current cooldown timers

        Returns:
            Ability to use or None for basic attack
        """
        available = [a for a in abilities if cooldowns.get(a.name, 0) <= 0]
        if available:
            return random.choice(available)
        return None

    def simulate_combat(self) -> Tuple[str, int, float, float]:
        """
        Simulate a single combat encounter.

        Returns:
            Tuple of (winner, turns_taken, attacker_damage_dealt, defender_damage_dealt)
        """
        attacker_hp = self.attacker_stats.health
        defender_hp = self.defender_stats.health

        attacker_cooldowns = {a.name: 0 for a in self.attacker_abilities}
        defender_cooldowns = {a.name: 0 for a in self.defender_abilities}

        attacker_damage_dealt = 0.0
        defender_damage_dealt = 0.0
        turns = 0

        while attacker_hp > 0 and defender_hp > 0 and turns < self.max_turns:
            turns += 1

            # Attacker turn
            ability = self.get_next_action(self.attacker_abilities, attacker_cooldowns)
            if self.can_hit(self.attacker_stats, ability):
                damage_multiplier = ability.damage_multiplier if ability else 1.0
                damage = self.calculate_damage(self.attacker_stats, self.defender_stats)
                damage *= damage_multiplier
                defender_hp -= damage
                attacker_damage_dealt += damage

                # Set cooldown
                if ability:
                    attacker_cooldowns[ability.name] = ability.cooldown

            # Defender turn
            ability = self.get_next_action(self.defender_abilities, defender_cooldowns)
            if self.can_hit(self.defender_stats, ability) and defender_hp > 0:
                damage_multiplier = ability.damage_multiplier if ability else 1.0
                damage = self.calculate_damage(self.defender_stats, self.attacker_stats)
                damage *= damage_multiplier
                attacker_hp -= damage
                defender_damage_dealt += damage

                # Set cooldown
                if ability:
                    defender_cooldowns[ability.name] = ability.cooldown

            # Decrease cooldowns
            for key in attacker_cooldowns:
                if attacker_cooldowns[key] > 0:
                    attacker_cooldowns[key] -= 1

            for key in defender_cooldowns:
                if defender_cooldowns[key] > 0:
                    defender_cooldowns[key] -= 1

        # Determine winner
        if attacker_hp > 0:
            winner = 'attacker'
        elif defender_hp > 0:
            winner = 'defender'
        else:
            winner = 'draw'

        return winner, turns, attacker_damage_dealt, defender_damage_dealt

    def run_simulations(self, num_simulations: int) -> Dict[str, Any]:
        """
        Run multiple combat simulations.

        Args:
            num_simulations: Number of simulations to run

        Returns:
            Dictionary with aggregated statistics
        """
        results = {
            'attacker_wins': 0,
            'defender_wins': 0,
            'draws': 0,
            'total_turns': [],
            'attacker_damage': [],
            'defender_damage': [],
        }

        for _ in range(num_simulations):
            winner, turns, att_dmg, def_dmg = self.simulate_combat()

            if winner == 'attacker':
                results['attacker_wins'] += 1
                results['attacker_damage'].append(att_dmg)
            elif winner == 'defender':
                results['defender_wins'] += 1
                results['defender_damage'].append(def_dmg)
            else:
                results['draws'] += 1

            results['total_turns'].append(turns)

        # Calculate statistics
        stats = {
            'simulations': num_simulations,
            'attacker_win_rate': results['attacker_wins'] / num_simulations,
            'defender_win_rate': results['defender_wins'] / num_simulations,
            'draw_rate': results['draws'] / num_simulations,
            'average_turns': sum(results['total_turns']) / len(results['total_turns']),
            'avg_attacker_damage': (
                sum(results['attacker_damage']) / len(results['attacker_damage'])
                if results['attacker_damage'] else 0
            ),
            'avg_defender_damage': (
                sum(results['defender_damage']) / len(results['defender_damage'])
                if results['defender_damage'] else 0
            ),
            'turns_min': min(results['total_turns']),
            'turns_max': max(results['total_turns']),
        }

        return stats


def load_config(config_path: Path) -> Dict[str, Any]:
    """Load combat configuration from JSON."""
    with open(config_path, 'r') as f:
        return json.load(f)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description='Monte Carlo combat simulator')
    parser.add_argument(
        '--config',
        type=Path,
        required=True,
        help='Combat configuration JSON file'
    )
    parser.add_argument(
        '--simulations',
        type=int,
        default=1000,
        help='Number of simulations to run'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path('combat_results.json'),
        help='Output path for results JSON'
    )

    args = parser.parse_args()

    # Load configuration
    config = load_config(args.config)

    # Create combatant stats
    attacker_config = config.get('attacker', {})
    defender_config = config.get('defender', {})

    attacker_stats = CombatStats(
        health=attacker_config.get('health', 100),
        attack_power=attacker_config.get('attack_power', 10),
        armor=attacker_config.get('armor', 0),
        critical_chance=attacker_config.get('critical_chance', 0.1),
        critical_multiplier=attacker_config.get('critical_multiplier', 1.5),
        dodge_chance=attacker_config.get('dodge_chance', 0),
    )

    defender_stats = CombatStats(
        health=defender_config.get('health', 100),
        attack_power=defender_config.get('attack_power', 10),
        armor=defender_config.get('armor', 0),
        critical_chance=defender_config.get('critical_chance', 0.1),
        critical_multiplier=defender_config.get('critical_multiplier', 1.5),
        dodge_chance=defender_config.get('dodge_chance', 0),
    )

    # Create abilities
    attacker_abilities = [
        Ability(
            name=a.get('name', f'ability_{i}'),
            cooldown=a.get('cooldown', 3),
            damage_multiplier=a.get('damage_multiplier', 1.5),
            hit_chance=a.get('hit_chance', 1.0),
        )
        for i, a in enumerate(attacker_config.get('abilities', []))
    ]

    defender_abilities = [
        Ability(
            name=a.get('name', f'ability_{i}'),
            cooldown=a.get('cooldown', 3),
            damage_multiplier=a.get('damage_multiplier', 1.5),
            hit_chance=a.get('hit_chance', 1.0),
        )
        for i, a in enumerate(defender_config.get('abilities', []))
    ]

    # Create simulator
    sim = CombatSimulator(
        attacker_stats=attacker_stats,
        defender_stats=defender_stats,
        attacker_abilities=attacker_abilities,
        defender_abilities=defender_abilities,
        armor_formula=config.get('armor_formula', 'flat'),
        armor_value=config.get('armor_value', 0),
        max_turns=config.get('max_turns', 1000),
    )

    # Run simulations
    print(f"Running {args.simulations} combat simulations...")
    results = sim.run_simulations(args.simulations)

    # Save results
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\nCombat Results:")
    print(f"  Attacker win rate: {results['attacker_win_rate']:.2%}")
    print(f"  Defender win rate: {results['defender_win_rate']:.2%}")
    print(f"  Draw rate: {results['draw_rate']:.2%}")
    print(f"  Average turns: {results['average_turns']:.1f}")
    print(f"  Avg attacker damage: {results['avg_attacker_damage']:.1f}")
    print(f"  Avg defender damage: {results['avg_defender_damage']:.1f}")
    print(f"\nSaved results to: {args.output}")


if __name__ == '__main__':
    main()
