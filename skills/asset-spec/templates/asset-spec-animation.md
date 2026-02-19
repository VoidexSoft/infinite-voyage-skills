# Animation Asset Specification

> Fill in all fields below. Replace bracketed placeholders with actual values.
> Delete any sections that do not apply, but document why they were removed.
> Reference: `references/animation-naming-conventions.md`, `references/polygon-budgets.md`

---

## Overview

| Field | Value |
|-------|-------|
| **Asset Name** | [e.g., `anim_warrior_combat_set`] |
| **Character / Object** | [e.g., Warrior (Player Character)] |
| **Asset Type** | Animation Set |
| **Animation Count** | [e.g., 22 clips] |
| **Priority** | [Critical Path / High / Medium / Low] |
| **Owner** | [Animator name] |
| **Target Completion** | [YYYY-MM-DD] |
| **Deliverable Format** | [FBX with embedded animations / Separate FBX per clip] |

---

## Target Character / Object

| Parameter | Value |
|-----------|-------|
| **Character asset** | [Link to character spec or asset name] |
| **Rig type** | [Humanoid / Quadruped / Custom / Mechanical] |
| **Skeleton** | [Engine standard humanoid / Custom -- specify] |
| **Bone count** | [e.g., 45] |
| **Frame rate** | [e.g., 30 FPS] |
| **Playback rate** | [e.g., Engine runs at 60 FPS; animations authored at 30 FPS] |

---

## Animation List

### Locomotion

| # | Clip Name | Frames | Duration | Loop | Root Motion | Priority | Notes |
|---|-----------|--------|----------|------|-------------|----------|-------|
| 1 | [e.g., `char_warrior_idle`] | [90] | [3.0s] | [Yes] | [No] | [Critical] | [Subtle breathing, weight shift] |
| 2 | [e.g., `char_warrior_walk_fwd`] | [40] | [1.33s] | [Yes] | [Yes] | [Critical] | [1.4 m/s speed] |
| 3 | [e.g., `char_warrior_run_fwd`] | [24] | [0.8s] | [Yes] | [Yes] | [Critical] | [3.5 m/s speed] |
| 4 | | | | | | | |
| 5 | | | | | | | |

### Combat

| # | Clip Name | Frames | Duration | Loop | Root Motion | Damage Window | Priority | Notes |
|---|-----------|--------|----------|------|-------------|---------------|----------|-------|
| 1 | [e.g., `char_warrior_attack_light_01`] | [20] | [0.67s] | [No] | [Yes] | [Fr 8-14] | [Critical] | [Quick slash] |
| 2 | [e.g., `char_warrior_attack_heavy`] | [40] | [1.33s] | [No] | [Yes] | [Fr 20-30] | [Critical] | [Wind-up + impact] |
| 3 | [e.g., `char_warrior_hit_front`] | [15] | [0.5s] | [No] | [No] | [N/A] | [Critical] | [Stagger reaction] |
| 4 | [e.g., `char_warrior_death_01`] | [60] | [2.0s] | [No] | [Yes] | [N/A] | [Critical] | [Fall forward] |
| 5 | | | | | | | | |

### Abilities / Casting

| # | Clip Name | Frames | Duration | Loop | Root Motion | Priority | Notes |
|---|-----------|--------|----------|------|-------------|----------|-------|
| 1 | [e.g., `char_warrior_cast_start`] | [15] | [0.5s] | [No] | [No] | [High] | [Arms raise, gather energy] |
| 2 | [e.g., `char_warrior_cast_loop`] | [30] | [1.0s] | [Yes] | [No] | [High] | [Channeling hold] |
| 3 | [e.g., `char_warrior_cast_end`] | [12] | [0.4s] | [No] | [No] | [High] | [Release energy] |
| 4 | | | | | | | |

### Interaction

| # | Clip Name | Frames | Duration | Loop | Priority | Notes |
|---|-----------|--------|----------|------|----------|-------|
| 1 | [e.g., `char_warrior_interact`] | [30] | [1.0s] | [No] | [Medium] | [Generic button press] |
| 2 | [e.g., `char_warrior_pickup`] | [25] | [0.83s] | [No] | [Medium] | [Bend and grab] |
| 3 | | | | | | |

### Emotes / Social

| # | Clip Name | Frames | Duration | Loop | Priority | Notes |
|---|-----------|--------|----------|------|----------|-------|
| 1 | [e.g., `char_warrior_emote_wave`] | [50] | [1.67s] | [No] | [Low] | [Friendly wave] |
| 2 | | | | | | |

### Total Animation Summary

| Category | Clip Count | Total Frames | Total Duration |
|----------|-----------|--------------|----------------|
| Locomotion | [e.g., 18] | [e.g., 650] | [e.g., 21.7s] |
| Combat | [e.g., 22] | [e.g., 580] | [e.g., 19.3s] |
| Abilities | [e.g., 8] | [e.g., 237] | [e.g., 7.9s] |
| Interaction | [e.g., 6] | [e.g., 165] | [e.g., 5.5s] |
| Emotes | [e.g., 4] | [e.g., 205] | [e.g., 6.8s] |
| **Total** | **[e.g., 58]** | **[e.g., 1,837]** | **[e.g., 61.2s]** |

---

## Blend Requirements

### Blend Tree Definitions

| Blend Tree | Type | Parameters | Clips Involved |
|------------|------|------------|----------------|
| [e.g., `BT_Locomotion_Ground`] | [2D Freeform] | [MoveX, MoveY] | [idle, walk_fwd/bwd/l/r, run_fwd] |
| [e.g., `BT_Combat_DirectionalHit`] | [2D Simple] | [HitDirection] | [hit_front, hit_back, hit_left, hit_right] |
| [e.g., `BT_Idle_Random`] | [1D Random] | [IdleVariant] | [idle, idle_bored, idle_alert] |

### Cross-Fade Transitions

| From State | To State | Blend Duration | Type | Notes |
|------------|----------|---------------|------|-------|
| [Idle] | [Walk] | [0.2s] | [Linear] | [Smooth start] |
| [Walk] | [Run] | [0.15s] | [Linear] | [Speed-driven] |
| [Any Locomotion] | [Attack] | [0.1s] | [Linear] | [Responsive combat entry] |
| [Attack] | [Idle] | [0.25s] | [Linear] | [Recovery feel] |
| [Any] | [Hit] | [0.05s] | [Linear] | [Instant interrupt] |
| [Any] | [Death] | [0.1s] | [Linear] | [Quick transition] |

### Additive Layers

| Layer | Base Clip | Additive Clip | Body Mask | Notes |
|-------|-----------|---------------|-----------|-------|
| [e.g., Breathing] | [Idle T-pose] | [Breathing cycle] | [Upper body] | [Always active, low weight 0.3] |
| [e.g., Aim offset] | [Idle] | [Aim up/down/left/right] | [Spine + arms] | [Driven by aim direction] |
| [e.g., Head look] | [Idle] | [Head turn targets] | [Head + neck] | [IK-driven look-at] |

---

## Root Motion Specifications

| Clip | Root Bone Translation | Root Bone Rotation | Speed (m/s) | Notes |
|------|----------------------|-------------------|-------------|-------|
| [walk_fwd] | [Forward: Yes] | [No] | [1.4] | [Constant velocity] |
| [run_fwd] | [Forward: Yes] | [No] | [3.5] | [Constant velocity] |
| [dodge_left] | [Left: Yes] | [No] | [5.0 burst] | [Non-linear, decelerates] |
| [attack_light] | [Forward: slight] | [No] | [0.5 burst] | [Lunge on contact frame] |
| [attack_heavy] | [Forward: Yes] | [No] | [1.0 burst] | [Wind-up pulls back, strike lunges] |
| [knockdown] | [Back + Down] | [Yes -- fall rotation] | [varies] | [Physics takes over at end] |

### Root Motion Rules
- Root bone must be at ground level (Y=0 at feet contact)
- Forward motion must match expected gameplay speed exactly
- Rotation root motion only for specific clips (180 turns, knockdowns)
- Root motion is disabled when physics/ragdoll takes over

---

## IK Requirements

| IK System | Type | Target | Weight | Notes |
|-----------|------|--------|--------|-------|
| [Foot IK] | [Two-bone] | [Ground contact points] | [1.0 on flat, blend on slopes] | [Prevent foot sliding, adapt to terrain] |
| [Hand IK] | [Two-bone] | [Weapon grip / interact point] | [1.0 during grip] | [Ensure hand meets weapon handle] |
| [Head Look-At] | [Multi-bone chain] | [Camera direction / NPC target] | [0.5-1.0 based on context] | [Spine + neck + head chain] |
| [Aim IK] | [Multi-bone chain] | [Aim target] | [0-1.0 when aiming] | [Upper body follows aim direction] |

### IK Disable Windows
- Disable foot IK during: jump, dodge, knockdown, death
- Disable hand IK during: casting, unarmed idle, emotes
- Disable look-at during: death, heavy hit reaction, cutscene override

---

## Event Markers

Every animation must include the required event markers from `references/animation-naming-conventions.md`.

### Locomotion Events

| Clip | Event | Frame | Purpose |
|------|-------|-------|---------|
| [walk_fwd] | `OnFootstepLeft` | [Frame 10] | [Trigger left footstep SFX] |
| [walk_fwd] | `OnFootstepRight` | [Frame 30] | [Trigger right footstep SFX] |
| [run_fwd] | `OnFootstepLeft` | [Frame 6] | [Trigger left footstep SFX] |
| [run_fwd] | `OnFootstepRight` | [Frame 18] | [Trigger right footstep SFX] |

### Combat Events

| Clip | Event | Frame | Purpose |
|------|-------|-------|---------|
| [attack_light_01] | `OnAttackDamageStart` | [Frame 8] | [Enable hitbox] |
| [attack_light_01] | `OnAttackDamageEnd` | [Frame 14] | [Disable hitbox] |
| [attack_light_01] | `OnAttackCancel` | [Frame 16] | [Allow combo input] |
| [attack_light_01] | `OnWeaponTrailStart` | [Frame 6] | [Start weapon VFX trail] |
| [attack_light_01] | `OnWeaponTrailEnd` | [Frame 16] | [Stop weapon VFX trail] |
| [attack_light_01] | `OnSoundPlay` | [Frame 5] | [Swing whoosh SFX] |

### Generic Events

| Clip | Event | Frame | Purpose |
|------|-------|-------|---------|
| [All combat clips] | `OnAnimationEnd` | [Last frame] | [Signal state machine: animation complete] |
| [cast_end] | `OnCastRelease` | [Frame 8] | [Spawn projectile / trigger ability] |
| [death] | `OnRagdollActivate` | [Frame 50] | [Switch to ragdoll physics] |

---

## State Machine Diagram

Describe the expected state machine structure for this animation set.

```
[Entry] --> IdleRelaxed
  IdleRelaxed --> SM_Locomotion (MoveSpeed > 0.1)
  IdleRelaxed --> SM_Combat (Attack input)
  IdleRelaxed --> SM_Abilities (Ability input)
  IdleRelaxed --> SM_Interaction (Interact input)

SM_Locomotion:
  Walk <-> Run (MoveSpeed threshold)
  Walk/Run --> Dodge (Dodge input)
  Walk/Run --> Jump (Jump input)

SM_Combat:
  AttackLight01 --> AttackCombo02 (combo input in cancel window)
  AttackCombo02 --> AttackCombo03 (combo input in cancel window)
  Any --> HitReaction (damage received)
  Any --> Death (health <= 0)

SM_Abilities:
  CastStart --> CastLoop (hold)
  CastLoop --> CastEnd (release)
```

---

## Approval Criteria

### Blocking Gate
- [ ] Key poses hit correct positions (start, peak, recovery)
- [ ] Timing feels responsive (attacks connect when expected)
- [ ] Weight and momentum are believable
- [ ] Silhouette communicates action clearly

### Polish Gate
- [ ] Curves are smooth (no pops, hitches, or linear segments)
- [ ] Follow-through and overlapping action present
- [ ] Root motion distances match gameplay design values
- [ ] Blend transitions are seamless at specified durations

### Integration Gate
- [ ] All event markers placed at correct frames
- [ ] All clips export without errors in target format
- [ ] Naming follows `references/animation-naming-conventions.md`
- [ ] State machine transitions work in-engine
- [ ] IK systems interact correctly with animations
- [ ] Frame timing verified against spec (duration matches)

---

## Delivery Checklist

- [ ] All animation clips exported (FBX per clip or combined)
- [ ] Event markers embedded in clips
- [ ] Animation controller / state machine file (if applicable)
- [ ] Blend tree configurations documented
- [ ] Root motion values documented (speed per clip)
- [ ] IK settings documented
- [ ] Test video of all animations playing in sequence
- [ ] This spec document updated with final frame counts

---

## Timeline

| Milestone | Date | Sign-off |
|-----------|------|----------|
| Blocking pass complete | [YYYY-MM-DD] | [Anim Lead] |
| Spline / polish pass | [YYYY-MM-DD] | [Anim Lead] |
| Event markers + root motion | [YYYY-MM-DD] | [Anim Lead + Gameplay] |
| Engine integration verified | [YYYY-MM-DD] | [Tech Art + Gameplay] |
| Final delivery | [YYYY-MM-DD] | [Anim Lead] |

---

## Dependencies

### Inputs
- [ ] Rigged character mesh (approved rig with correct bone count)
- [ ] Gameplay design values (movement speeds, attack timings, combo windows)
- [ ] State machine design (which states connect to which)
- [ ] VFX timing requirements (when do effects trigger?)
- [ ] Audio timing requirements (when do sounds play?)

### Outputs
- [ ] Gameplay systems (combat, movement depend on animation timing)
- [ ] VFX system (particle spawns depend on event markers)
- [ ] Audio system (sound triggers depend on event markers)
- [ ] AI system (enemy behavior depends on animation durations)
- [ ] UI system (ability cooldowns may reference animation length)

---
