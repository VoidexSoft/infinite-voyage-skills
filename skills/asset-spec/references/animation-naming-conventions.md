# Animation Naming Conventions

This document defines the standard naming conventions for all animation assets in
game development. Consistent naming ensures animations integrate cleanly with state
machines, blend trees, and scripted events across the project.

---

## Prefix System

Every animation clip name begins with a category prefix that identifies its domain.
Prefixes use lowercase with an underscore separator.

| Prefix | Domain | Description |
|--------|--------|-------------|
| `char_` | Character | Player characters, NPCs, enemies, companions |
| `env_` | Environment | Doors, elevators, traps, destructibles, moving platforms |
| `ui_` | User Interface | Menu transitions, icon animations, HUD elements |
| `fx_` | Visual Effects | Particle triggers, mesh deformations, VFX helper bones |
| `cam_` | Camera | Cutscene cameras, shakes, transitions |
| `veh_` | Vehicle | Mounts, ships, vehicles |
| `prop_` | Props | Animated props not attached to a character or environment |

---

## Full Naming Pattern

```
[prefix]_[subject]_[action]_[variant]_[direction]

Examples:
  char_warrior_idle_relaxed
  char_warrior_run_forward
  char_warrior_attack_light_01
  env_door_open_slow
  ui_button_press_confirm
  fx_fire_loop_medium
```

### Naming Rules

1. **All lowercase** -- No capital letters anywhere in clip names
2. **Underscores only** -- No spaces, hyphens, or camelCase
3. **No special characters** -- Letters, numbers, and underscores only
4. **Numbered variants** -- Use two-digit suffixes: `_01`, `_02`, `_03`
5. **No version numbers in clip names** -- Versioning lives in source control, not the clip
6. **Max 64 characters** -- Keep names descriptive but concise
7. **English only** -- All names in English regardless of localization

---

## Subject Naming

The subject identifies what is being animated. Use the asset's canonical short name.

### Character Subjects

| Subject | Character |
|---------|-----------|
| `warrior` | Player warrior class |
| `mage` | Player mage class |
| `rogue` | Player rogue class |
| `healer` | Player healer class |
| `npc_merchant` | Merchant NPC |
| `npc_questgiver` | Quest giver NPC |
| `npc_guard` | Guard NPC |
| `npc_villager` | Generic villager |
| `enemy_skeleton` | Skeleton enemy type |
| `enemy_golem` | Golem enemy type |
| `enemy_dragon` | Dragon enemy type |
| `boss_lich` | Lich boss |
| `boss_titan` | Titan boss |
| `companion_wolf` | Wolf companion |

### Environment Subjects

| Subject | Element |
|---------|---------|
| `door` | Standard door |
| `gate` | Large gate or portcullis |
| `chest` | Treasure chest |
| `lever` | Lever / switch |
| `platform` | Moving platform |
| `bridge` | Drawbridge or extending bridge |
| `trap_spike` | Spike trap |
| `trap_arrow` | Arrow trap |
| `crystal` | Interactive crystal |
| `portal` | Teleport portal |

---

## Action Naming

Actions describe what the subject is doing. Use consistent verbs across all asset types.

### Locomotion Actions

| Action | Description | Typical Duration |
|--------|-------------|------------------|
| `idle` | Standing still, neutral pose | 2-4 sec loop |
| `idle_[mood]` | Idle with personality (bored, alert, tired) | 3-5 sec loop |
| `walk` | Standard walking pace | 0.8-1.2 sec loop |
| `run` | Standard running pace | 0.6-1.0 sec loop |
| `sprint` | Maximum speed movement | 0.5-0.8 sec loop |
| `crouch_idle` | Crouched stationary | 2-3 sec loop |
| `crouch_walk` | Crouched movement | 1.0-1.5 sec loop |
| `jump_start` | Jump launch from ground | 0.2-0.4 sec |
| `jump_loop` | Airborne loop | 0.5-1.0 sec loop |
| `jump_land` | Landing from jump | 0.2-0.5 sec |
| `fall_loop` | Falling (longer than jump) | 0.5-1.0 sec loop |
| `fall_land` | Hard landing from fall | 0.3-0.6 sec |
| `dodge` | Evasive dodge | 0.4-0.8 sec |
| `turn_left` | In-place 90-degree turn left | 0.3-0.5 sec |
| `turn_right` | In-place 90-degree turn right | 0.3-0.5 sec |
| `turn_180` | In-place 180-degree turn | 0.5-0.8 sec |

### Combat Actions

| Action | Description | Typical Duration |
|--------|-------------|------------------|
| `attack_light` | Fast, low-damage attack | 0.4-0.8 sec |
| `attack_heavy` | Slow, high-damage attack | 0.8-1.5 sec |
| `attack_combo_[N]` | Combo chain hit N (01, 02, 03) | 0.4-1.0 sec |
| `attack_special` | Class-specific special attack | 0.8-2.0 sec |
| `attack_ranged` | Ranged weapon attack | 0.6-1.2 sec |
| `block_start` | Raise shield / guard | 0.2-0.4 sec |
| `block_loop` | Holding block | Loop |
| `block_end` | Lower shield / guard | 0.2-0.4 sec |
| `block_hit` | Impact while blocking | 0.3-0.6 sec |
| `parry` | Timed parry animation | 0.3-0.5 sec |
| `hit_front` | Damage reaction from front | 0.3-0.6 sec |
| `hit_back` | Damage reaction from behind | 0.3-0.6 sec |
| `hit_left` | Damage reaction from left | 0.3-0.6 sec |
| `hit_right` | Damage reaction from right | 0.3-0.6 sec |
| `hit_heavy` | Heavy stagger reaction | 0.5-1.0 sec |
| `knockdown` | Knocked to ground | 0.5-1.0 sec |
| `getup` | Getting up from ground | 0.5-1.0 sec |
| `death` | Death animation | 1.0-3.0 sec |
| `death_[variant]` | Death variant (01, 02, ragdoll) | 1.0-3.0 sec |

### Ability / Cast Actions

| Action | Description | Typical Duration |
|--------|-------------|------------------|
| `cast_start` | Begin casting animation | 0.3-0.8 sec |
| `cast_loop` | Channeling loop | Loop |
| `cast_end` | Release / finish cast | 0.3-0.8 sec |
| `cast_[spell]` | Specific spell cast (fireball, heal) | 0.5-2.0 sec |
| `summon` | Summoning animation | 1.0-3.0 sec |
| `buff` | Self-buff animation | 0.5-1.5 sec |

### Interaction Actions

| Action | Description | Typical Duration |
|--------|-------------|------------------|
| `interact` | Generic interaction (press button, pull lever) | 0.5-1.5 sec |
| `pickup` | Pick up item from ground | 0.5-1.0 sec |
| `open` | Open container / door | 0.5-1.5 sec |
| `close` | Close container / door | 0.5-1.5 sec |
| `sit_start` | Sit down | 0.5-1.0 sec |
| `sit_loop` | Sitting idle | 2-4 sec loop |
| `sit_end` | Stand up from sitting | 0.5-1.0 sec |
| `talk` | Generic talking gesture | 1.0-3.0 sec |
| `emote_[name]` | Emote animation (wave, cheer, bow) | 1.0-4.0 sec |

---

## Direction and Variant Suffixes

When an action has directional or variant forms, append a suffix.

### Directional Suffixes

| Suffix | Meaning |
|--------|---------|
| `_forward` or `_fwd` | Forward direction |
| `_backward` or `_bwd` | Backward direction |
| `_left` or `_l` | Left direction |
| `_right` or `_r` | Right direction |
| `_up` | Upward |
| `_down` | Downward |

### Variant Suffixes

| Suffix | Meaning |
|--------|---------|
| `_01`, `_02`, `_03` | Numbered variation |
| `_loop` | Looping animation |
| `_start` | Transition into state |
| `_end` | Transition out of state |
| `_additive` | Additive blend layer |

---

## State Machine Naming

Animator controller states and layers follow a related but distinct convention.

### Layer Naming

```
[Domain]_[System]

Examples:
  Base_Locomotion
  Upper_Combat
  Full_Override
  Face_Expressions
  Additive_Breathing
```

### State Naming

States within a state machine use PascalCase to distinguish them from clip names.

```
[Action][Context]

Examples:
  IdleRelaxed
  RunForward
  AttackLightCombo01
  DeathFallback
  CastFireball
```

### Sub-State Machine Naming

```
SM_[Category]

Examples:
  SM_Locomotion
  SM_Combat
  SM_Interaction
  SM_Dialogue
```

### Transition Naming

Transitions are named automatically by most engines, but when named manually:

```
[FromState]_to_[ToState]

Examples:
  IdleRelaxed_to_RunForward
  AttackLight_to_IdleRelaxed
  CastStart_to_CastLoop
```

---

## Blend Tree Conventions

### Blend Tree Naming

```
BT_[Domain]_[Purpose]

Examples:
  BT_Locomotion_Ground
  BT_Locomotion_Strafe
  BT_Combat_DirectionalHit
  BT_Idle_Random
```

### Blend Parameters

| Parameter | Type | Range | Use |
|-----------|------|-------|-----|
| `MoveSpeed` | Float | 0.0 - 1.0 | Walk/run blend |
| `MoveX` | Float | -1.0 - 1.0 | Strafe left/right |
| `MoveY` | Float | -1.0 - 1.0 | Forward/backward |
| `TurnAngle` | Float | -180 - 180 | Turn direction |
| `AimVertical` | Float | -1.0 - 1.0 | Look up/down |
| `AimHorizontal` | Float | -1.0 - 1.0 | Look left/right |
| `HitDirection` | Float | 0 - 360 | Damage direction |
| `IdleVariant` | Int | 0 - N | Random idle selection |

---

## Animation Event Markers

Animation events are callbacks triggered at specific frames. Use consistent naming
for event function calls.

### Event Naming Convention

```
On[Action][Detail]

Examples:
  OnFootstepLeft
  OnFootstepRight
  OnAttackDamageStart
  OnAttackDamageEnd
  OnCastRelease
  OnSoundPlay
  OnVFXSpawn
  OnWeaponTrailStart
  OnWeaponTrailEnd
  OnRagdollActivate
  OnIKEnable
  OnIKDisable
```

### Standard Event Markers

Every combat animation must include these markers:

| Event | Frame Placement | Purpose |
|-------|----------------|---------|
| `OnAttackDamageStart` | First frame of damage window | Enable hitbox |
| `OnAttackDamageEnd` | Last frame of damage window | Disable hitbox |
| `OnAttackCancel` | Frame where combo input opens | Allow chain input |
| `OnAnimationEnd` | Final meaningful frame | Signal completion to state machine |

Every locomotion animation must include:

| Event | Frame Placement | Purpose |
|-------|----------------|---------|
| `OnFootstepLeft` | Left foot contact frame | Trigger footstep SFX |
| `OnFootstepRight` | Right foot contact frame | Trigger footstep SFX |

---

## Example Animation List: RPG Warrior Character

Complete animation list for the Warrior player character.

### Locomotion (18 clips)

| Clip Name | Frames | Loop | Root Motion |
|-----------|--------|------|-------------|
| `char_warrior_idle` | 90 | Yes | No |
| `char_warrior_idle_bored` | 120 | Yes | No |
| `char_warrior_idle_alert` | 90 | Yes | No |
| `char_warrior_walk_fwd` | 40 | Yes | Yes |
| `char_warrior_walk_bwd` | 45 | Yes | Yes |
| `char_warrior_walk_left` | 40 | Yes | Yes |
| `char_warrior_walk_right` | 40 | Yes | Yes |
| `char_warrior_run_fwd` | 24 | Yes | Yes |
| `char_warrior_run_bwd` | 28 | Yes | Yes |
| `char_warrior_sprint_fwd` | 20 | Yes | Yes |
| `char_warrior_crouch_idle` | 60 | Yes | No |
| `char_warrior_crouch_walk_fwd` | 45 | Yes | Yes |
| `char_warrior_jump_start` | 10 | No | Yes |
| `char_warrior_jump_loop` | 20 | Yes | No |
| `char_warrior_jump_land` | 12 | No | No |
| `char_warrior_dodge_left` | 18 | No | Yes |
| `char_warrior_dodge_right` | 18 | No | Yes |
| `char_warrior_dodge_bwd` | 20 | No | Yes |

### Combat (22 clips)

| Clip Name | Frames | Loop | Root Motion |
|-----------|--------|------|-------------|
| `char_warrior_attack_light_01` | 20 | No | Yes |
| `char_warrior_attack_light_02` | 22 | No | Yes |
| `char_warrior_attack_light_03` | 24 | No | Yes |
| `char_warrior_attack_heavy` | 40 | No | Yes |
| `char_warrior_attack_combo_01` | 18 | No | Yes |
| `char_warrior_attack_combo_02` | 22 | No | Yes |
| `char_warrior_attack_combo_03` | 30 | No | Yes |
| `char_warrior_attack_special` | 50 | No | Yes |
| `char_warrior_block_start` | 8 | No | No |
| `char_warrior_block_loop` | 30 | Yes | No |
| `char_warrior_block_end` | 10 | No | No |
| `char_warrior_block_hit` | 15 | No | No |
| `char_warrior_parry` | 12 | No | No |
| `char_warrior_hit_front` | 15 | No | No |
| `char_warrior_hit_back` | 15 | No | No |
| `char_warrior_hit_left` | 12 | No | No |
| `char_warrior_hit_right` | 12 | No | No |
| `char_warrior_hit_heavy` | 25 | No | Yes |
| `char_warrior_knockdown` | 30 | No | Yes |
| `char_warrior_getup` | 28 | No | Yes |
| `char_warrior_death_01` | 60 | No | Yes |
| `char_warrior_death_02` | 55 | No | Yes |

### Abilities (8 clips)

| Clip Name | Frames | Loop | Root Motion |
|-----------|--------|------|-------------|
| `char_warrior_cast_start` | 15 | No | No |
| `char_warrior_cast_loop` | 30 | Yes | No |
| `char_warrior_cast_end` | 12 | No | No |
| `char_warrior_cast_battlecry` | 40 | No | No |
| `char_warrior_cast_groundslam` | 45 | No | Yes |
| `char_warrior_cast_shieldcharge` | 30 | No | Yes |
| `char_warrior_buff` | 35 | No | No |
| `char_warrior_summon` | 60 | No | No |

### Interaction (10 clips)

| Clip Name | Frames | Loop | Root Motion |
|-----------|--------|------|-------------|
| `char_warrior_interact` | 30 | No | No |
| `char_warrior_pickup` | 25 | No | No |
| `char_warrior_open` | 30 | No | No |
| `char_warrior_sit_start` | 25 | No | No |
| `char_warrior_sit_loop` | 90 | Yes | No |
| `char_warrior_sit_end` | 25 | No | No |
| `char_warrior_talk` | 60 | Yes | No |
| `char_warrior_emote_wave` | 50 | No | No |
| `char_warrior_emote_cheer` | 60 | No | No |
| `char_warrior_emote_bow` | 45 | No | No |

**Total: 58 animation clips for Warrior character**

---

## File Organization

```
animations/
  characters/
    warrior/
      locomotion/
        char_warrior_idle.fbx
        char_warrior_walk_fwd.fbx
        ...
      combat/
        char_warrior_attack_light_01.fbx
        ...
      abilities/
        char_warrior_cast_start.fbx
        ...
      interaction/
        char_warrior_interact.fbx
        ...
  environment/
    doors/
      env_door_open_slow.fbx
      ...
  ui/
    ...
  fx/
    ...
```

---

*Last updated for production pipeline. Naming conventions are
mandatory for all animation deliverables.*
