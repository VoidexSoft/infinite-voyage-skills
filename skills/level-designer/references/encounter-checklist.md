# Pre-Ship Encounter Checklist

Validate every encounter against this checklist before it goes into a release build.
No encounter should ship without a full pass. Mark each item as PASS, FAIL, or N/A.

---

## 1. Difficulty Verification

- [ ] **Difficulty tier assigned** — Encounter has a clearly labeled tier (Story / Easy / Normal / Hard / Nightmare)
- [ ] **Stat budget verified** — Enemy HP, damage, and armor fall within the tier's stat envelope (see `difficulty-guide.md`)
- [ ] **DPS-to-EHP ratio checked** — Time-to-death for the player at expected gear level is within target range
- [ ] **Difficulty tested at minimum viable gear** — Encounter is completable with the worst reasonable loadout for this progression point
- [ ] **Difficulty tested at maximum expected gear** — Encounter is not trivialized by optimal gear available at this stage
- [ ] **Scaling formula applied** — If adaptive difficulty is active, multipliers produce expected results at each bracket
- [ ] **Outlier damage removed** — No single attack one-shots the player at expected EHP without a telegraph window of at least 1.5 seconds
- [ ] **Healer/support enemy output verified** — Support enemies do not make the encounter unwinnable through attrition

## 2. Reward Balance

- [ ] **XP reward matches tier and duration** — XP per minute is consistent with zone expectations
- [ ] **Loot table reviewed** — Drop rates are within economy parameters (coordinate with economy-designer)
- [ ] **Bonus rewards gated properly** — Optional challenge rewards do not exceed 150% of base reward
- [ ] **No duplicate unique drops** — If a unique item drops here, it does not also drop elsewhere in the zone
- [ ] **Progression unlock verified** — Completing this encounter unlocks exactly the intended areas or quest flags
- [ ] **Currency output within budget** — Gold and crafting materials do not exceed zone currency targets
- [ ] **Reward communicates difficulty** — Harder optional encounters visibly reward more than mandatory ones

## 3. Narrative Hooks

- [ ] **Story context present** — The player understands why this encounter exists in the narrative
- [ ] **Pre-encounter setup exists** — Environmental cues, NPC dialogue, or item descriptions foreshadow the encounter
- [ ] **Post-encounter payoff delivered** — Completing the encounter changes something visible in the world or story
- [ ] **Dialogue triggers tested** — Any mid-combat dialogue fires at the correct health threshold or event
- [ ] **Lore objects placed** — If applicable, discoverable items in the encounter space support the zone narrative
- [ ] **NPC positioning makes sense** — Enemy placement tells a story (guards patrol, ambushers hide, beasts nest)
- [ ] **Dead enemies tell stories** — Corpse placement, battle damage, and environmental destruction are consistent

## 4. Accessibility

- [ ] **Colorblind-safe indicators** — All threat telegraphs use shape and animation in addition to color
- [ ] **Audio cues present** — Major attacks have distinct audio tells, not just visual ones
- [ ] **Subtitle support** — Any combat dialogue or audio narrative is subtitled
- [ ] **Input complexity reasonable** — Required inputs per second do not exceed tier expectations
- [ ] **Assist mode functional** — If the game offers aim assist or auto-dodge, the encounter works with them enabled
- [ ] **Font sizes readable** — Any in-combat UI text meets minimum size requirements
- [ ] **Screen shake optional** — Camera effects can be reduced or disabled without losing gameplay information

## 5. Pacing

- [ ] **Encounter duration within target** — Actual playtime is within 20% of the design estimate
- [ ] **Pre-combat breathing room** — Player has at least 10 seconds of safe space before combat triggers
- [ ] **Post-combat breathing room** — Player has at least 15 seconds before the next threat
- [ ] **No back-to-back high-intensity encounters** — Two consecutive encounters at intensity 8+ are separated by a release moment
- [ ] **Tension curve validated** — This encounter's intensity fits its position in the zone's tension/release cycle
- [ ] **Exploration reward between combats** — Players find at least one discoverable item between mandatory encounters
- [ ] **Pacing tested with real players** — Observed playtime matches intended cadence (see `player-testing-checklist.md`)

## 6. Soft-Lock Prevention

- [ ] **No unwinnable states** — The encounter cannot reach a state where the player cannot win or die
- [ ] **Stuck enemy detection** — If an enemy gets stuck in geometry, a timeout despawns or repositions it
- [ ] **Retreat path available** — The player can flee or reset the encounter if overwhelmed
- [ ] **Checkpoint before encounter** — A save point or checkpoint exists before any encounter lasting over 5 minutes
- [ ] **Door/gate states verified** — Progression gates open correctly on victory and do not re-lock
- [ ] **Resource availability confirmed** — Enough healing items or regeneration exists to sustain the encounter
- [ ] **Respawn logic tested** — Player respawn after death returns them to a valid, playable state
- [ ] **Trigger volumes verified** — Combat triggers activate reliably and do not fail on edge-case player positions

## 7. Combat Variety

- [ ] **Multiple valid strategies** — At least two distinct approaches can defeat the encounter (e.g., stealth, brute force, environmental)
- [ ] **Enemy role diversity** — Encounter includes at least two different enemy roles (tank, DPS, support, ranged, melee)
- [ ] **No identical encounters in same zone** — This encounter composition does not exactly repeat another in the zone
- [ ] **Player build agnostic** — No single player build is required; all major archetypes can succeed
- [ ] **Engagement range variety** — Encounter has both close-range and long-range threat elements
- [ ] **Interactive elements present** — At least one environmental object can be used tactically
- [ ] **Escalation present** — The encounter changes state at least once (reinforcements, phase shift, environmental change)

## 8. Environmental Hazards

- [ ] **Hazards clearly communicated** — Every environmental hazard has a visible and audible warning
- [ ] **Damage values balanced** — Hazard damage is meaningful but not instantly lethal at expected player HP
- [ ] **Player-usable hazards tested** — If hazards can damage enemies, the interaction works correctly
- [ ] **Hazard timing predictable** — Recurring hazards follow a learnable pattern
- [ ] **Safe zones exist** — The encounter arena has at least one position safe from all hazards simultaneously
- [ ] **Hazard interaction with AI verified** — Enemies respond to hazards appropriately (avoid, use, or ignore as designed)
- [ ] **Destructible cover functional** — If cover can be destroyed, it breaks as expected and debris does not block pathing

---

## Sign-Off Requirements

An encounter requires sign-off from the following roles before shipping:

| Role | Validates | Required? |
|------|-----------|-----------|
| Level Designer | Pacing, variety, soft-locks, hazards | Yes |
| Game Balancer | Difficulty, stat budgets, DPS checks | Yes |
| Economy Designer | Rewards, loot tables, currency output | Yes |
| Narrative Designer | Story hooks, dialogue triggers, lore | Yes |
| QA Lead | All functional checks, edge cases | Yes |
| Accessibility Lead | Colorblind, audio, input complexity | Yes |
| Art Lead | Visual clarity, telegraph readability | Recommended |
| Audio Lead | Audio cues, ambient atmosphere | Recommended |

## Quick Reference: Common Failures

| Failure | Symptom | Fix |
|---------|---------|-----|
| Silent one-shot | Player dies with no warning | Add 1.5s telegraph with audio + visual cue |
| Attrition lock | Fight drags past 15 minutes | Cap support enemy healing; add enrage timer |
| Loot vacuum | Encounter drops nothing memorable | Add guaranteed drop from themed loot table |
| Dead zone before boss | 2+ minutes of empty hallway | Add environmental storytelling or minor loot |
| Geometry trap | Enemy or player stuck in wall | Add navmesh checks; add stuck-detection timeout |
| Build wall | Only one player build can win | Add alternative damage vulnerability or bypass |
| Narrative gap | Player does not know why they are fighting | Add pre-encounter NPC hint or environmental setup |

---

## 9. Performance and Technical

- [ ] **Frame rate stable** — Encounter does not cause frame drops below target (30/60 FPS depending on platform)
- [ ] **Spawn system functional** — All enemies spawn at the correct locations and times
- [ ] **Despawn on completion** — Any surviving non-essential enemies despawn or flee after encounter completion
- [ ] **Particle effects bounded** — Environmental effects and ability VFX do not cause GPU spikes
- [ ] **Audio channels managed** — Simultaneous sound effects do not exceed channel limits or cause audio clipping
- [ ] **Physics interactions stable** — Destructible objects, ragdolls, and projectiles behave predictably
- [ ] **Network sync verified** — If multiplayer, all encounter states sync correctly between clients
- [ ] **Memory footprint acceptable** — Encounter does not cause memory spikes that affect adjacent areas

## 10. Multiplayer Considerations (If Applicable)

- [ ] **Scaling for party size** — Enemy HP and count scale appropriately for 1-4 players
- [ ] **No single-player-only mechanics** — All interactive elements work with multiple players present
- [ ] **Reward distribution fair** — Loot and XP distribute correctly among party members
- [ ] **Revive windows exist** — Downed players have adequate time and safety for revival
- [ ] **Role diversity rewarded** — Encounter benefits from having different player builds in the party
- [ ] **Solo completable** — Encounter remains winnable by a solo player at appropriate level

---

## Severity Classification

When a checklist item fails, classify the severity to prioritize fixes:

| Severity | Definition | Example | Action |
|----------|-----------|---------|--------|
| **Blocker** | Encounter is unplayable or causes data loss | Soft-lock, crash, save corruption | Must fix before any build ships |
| **Critical** | Encounter is completable but seriously flawed | One-shot without telegraph, broken rewards | Fix before milestone build |
| **Major** | Noticeable quality issue that affects experience | Poor pacing, missing audio cues, weak variety | Fix before release candidate |
| **Minor** | Polish issue that does not affect core experience | Suboptimal loot balance, slight timing issues | Fix if time allows |
| **Suggestion** | Improvement that would enhance the encounter | Additional environmental interaction | Backlog for future iteration |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Initial | Full checklist established |
| — | — | Update this table as the checklist evolves |
