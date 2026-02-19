# Character Rig Requirements — Infinite Voyage

## Target Platforms
- PC (primary) — Unreal Engine 5.4, high-end rigs
- PlayStation 5 / Xbox Series X — console parity with PC High
- Nintendo Switch 2 — reduced bone count, no cloth sim

## Characters Needing Animation Specs

### 1. Navigator (Player Character)
- Humanoid, medium build, space suit with articulated joints
- Needs full locomotion, zero-G traversal, combat (ranged + melee tool), and 40+ dialogue facial expressions
- Suit has mechanical backpack thrusters — need secondary bone chain for thruster flaps
- Helmet visor retracts — mechanical hinge animation needed

### 2. Voidborn Stalker (Elite Enemy)
- Four-armed insectoid, digitigrade legs, tail with stinger
- Fast, erratic movement — lots of anticipation/snap attacks
- Wings fold/unfold for glide attacks
- Death: exoskeleton cracks and dissolves (blend shape sequence)

### 3. Station Merchant NPC (Friendly)
- Upper body only (behind counter), highly expressive face and hand gestures
- Six fingers per hand (alien species)
- Three eye stalks with independent look-at tracking
- Idle fidgeting animations: polishing merchandise, tapping counter, scratching head-crest

## Rig Constraints

| Parameter | PC / Console | Switch 2 |
|-----------|-------------|----------|
| Max bones (player) | 120 | 65 |
| Max bones (NPC) | 80 | 45 |
| Max bones (enemy) | 90 | 50 |
| IK chains allowed | 4 per character | 2 per character |
| Cloth sim bones | Up to 30 | 0 (baked) |
| Facial blend shapes | 52 (ARKit standard) | 24 (reduced set) |
| Bone naming | UE5 Mannequin standard | Same |
| Root motion | Required for locomotion | Required |

## Animation Pipeline Notes
- All rigs authored in Maya 2025, exported FBX 2020.3
- Skeleton naming must follow `IV_[CharType]_[BoneName]` convention (e.g., `IV_Navigator_Spine01`)
- IK targets: feet (ground contact), hands (weapon/tool grip), head (look-at), tail (Voidborn only)
- Additive animations for breathing, weapon sway, hit reactions
- Blend trees for locomotion (idle > walk > jog > sprint, 8-directional)
- Retarget-ready: all humanoids share a common base skeleton with per-character extension bones
- Frame rate: 30 FPS authored, played back at 60 FPS in engine
- Total animation frame budget per character: Navigator 8,000 frames, Stalker 5,000 frames, Merchant 3,000 frames
