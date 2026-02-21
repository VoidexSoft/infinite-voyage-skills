# Narrative Bible

The master narrative reference for all writers and designers working on Infinite Voyage. Every piece of narrative content -- dialogue, codex entries, quest text, environmental storytelling, UI copy -- must align with this document.

---

## World Setting

### The Premise

It is the year 2847. Humanity has colonized the Kepler Sector, a cluster of star systems connected by unstable warp corridors. During routine expansion, survey teams discovered the Remnant -- vast ruins of an ancient civilization that vanished without explanation. The ruins are older than Earth's fossil record. They contain technology that defies known physics. And something inside them is waking up.

The player is a Voyager, part archaeologist, part explorer, part diplomat. Voyagers are licensed by the Concord Authority to enter Remnant sites, catalog findings, and determine whether the ruins are safe for colonization. In practice, Voyagers are the first to face whatever the Remnant left behind.

### The Kepler Sector

The playable universe consists of interconnected star systems, each with distinct character:

- **Core Systems** -- Heavily colonized, politically complex. The Concord Authority governs here. Safe but bureaucratic.
- **Frontier Systems** -- Partially settled, lawless in places. Independent stations, mining operations, and pirate outposts.
- **Deep Reach** -- Uncharted space where the densest Remnant sites are found. Hostile environments, unknown threats.
- **The Silence** -- A region where all signals stop. Ships that enter rarely return. The source of the Remnant mystery.

### Technology Level

Humanity has faster-than-light travel (warp corridors, not free-roaming FTL), energy weapons, basic AI assistants, genetic augmentation, and modular starships. They do not have teleportation, time travel, or true artificial consciousness. Remnant technology is several orders of magnitude beyond human capability and is often incomprehensible -- it works, but nobody knows why.

### The Remnant

The vanished civilization. No one knows what they looked like, what they called themselves, or why they disappeared. Their ruins suggest a culture obsessed with observation -- telescopes the size of moons, sensor arrays that span solar systems, data storage structures holding information about galaxies humanity has never seen. The central mystery: what were they watching, and what did they see that made them leave?

---

## Tone Guide

### Core Tone

**Awe tempered by loneliness.** The universe is beautiful and terrifying in equal measure. The player should feel the wonder of discovery alongside the weight of isolation. This is not grimdark nihilism -- there is hope, warmth, and humor -- but it is grounded in the reality that space is vast and indifferent, and that the things humanity finds out there were not meant for human minds.

### Tone Spectrum

| Context | Tone |
|---------|------|
| Exploration / discovery | Wonder, curiosity, quiet awe |
| NPC interactions (friendly) | Warm, wry, lived-in humor |
| NPC interactions (hostile) | Tense, clipped, pragmatic |
| Remnant encounters | Unsettling, reverent, alien |
| Combat / danger | Urgent, visceral, controlled fear |
| Codex / lore entries | Academic curiosity, restrained excitement |
| Personal moments (crew) | Intimate, vulnerable, real |
| Political / faction conflict | Measured, ideological, morally gray |

### What This Game Sounds Like

- A conversation between two scientists at the edge of the unknown, sharing a flask of coffee, one of them trying not to show how scared they are.
- A documentary narrator who has seen something that changed them and is choosing their words carefully.
- A ship's log written by someone who knows they might not be the one to read it.

### What This Game Does NOT Sound Like

- Generic sci-fi military barking ("Move out, soldier!")
- Juvenile humor or pop-culture references that break immersion
- Pompous fantasy prose ("And lo, the stars did weep...")
- Cynical edgelord nihilism ("Nothing matters anyway")
- Technobabble without emotional grounding

---

## Narrative Themes

### Primary Themes

1. **The Cost of Knowledge** -- Every discovery demands something. Understanding the Remnant changes the people who study them. Is the truth worth what it takes from you?

2. **Connection Across Distance** -- Loneliness is the default state in space. The relationships the player builds -- with crew, with NPCs, even with the echoes of the Remnant -- are the antidote. The game argues that connection is worth the risk of loss.

3. **Legacy and Impermanence** -- The Remnant built wonders that outlasted their creators by millennia. What does humanity build that will last? What should it build? The player's choices are a small answer to a vast question.

### Secondary Themes

4. **Authority vs. Freedom** -- The Concord Authority provides stability but restricts exploration. Frontier independence offers freedom but invites chaos. Neither is wholly right.

5. **The Observer Effect** -- The Remnant were watchers. The player is a watcher. The act of observing changes both the observed and the observer. This theme should manifest mechanically (scanning changes things) and narratively (learning truths changes relationships).

6. **What Makes Us Human** -- In a universe of genetic augmentation, AI assistants, and alien artifacts that alter cognition, the boundaries of "human" are tested. The game does not answer this question; it asks it repeatedly from different angles.

---

## Narrative Pillars

These are inviolable rules for all narrative content:

### 1. Discovery Is the Reward

The best moments in the game are when the player understands something new about the world. Plot twists, lore revelations, character secrets, environmental storytelling -- these are more valuable than any item drop. Design narrative content so that understanding IS the reward.

### 2. No Pure Villains, No Pure Heroes

Every antagonist believes they are right. Every ally has flaws. The player should regularly face situations where the "right" choice is unclear. If a faction or character can be reduced to "evil" without nuance, they need more development.

### 3. The World Existed Before the Player

NPCs have histories, grudges, loves, and routines that predate the player's arrival. The player enters ongoing stories, not stories created for the player. Conversations should reference events the player was not part of. The world should feel lived-in.

### 4. Silence Is a Tool

Not every moment needs dialogue. Let environments speak. Let pauses in conversation carry weight. A ruin with no explanation is more powerful than a ruin with a plaque. Trust the player to feel the absence.

### 5. Consequences Are Remembered

Choices matter, and the world remembers. An NPC spared in Act 1 reappears in Act 3. A faction betrayed closes its doors permanently. The player should feel that their decisions have weight, even small ones. See `references/branching-patterns.md` for implementation patterns.

---

## Point of View Conventions

### Player Character

- The player character (the Voyager) is **not** a blank slate. They have a defined role (licensed Voyager), a general demeanor (curious, competent), and a history (they chose this life). However, their specific personality, moral alignment, and relationships are shaped by player choice.
- Dialogue options represent different facets of the Voyager's personality, not different characters. All options should feel like things the same person could plausibly say.
- The Voyager speaks in **second person** in quest logs and UI text ("You received a transmission from Zara") and in **first person** during dialogue scenes.

### Narrator / UI Voice

- Quest logs, objective text, codex summaries, and tutorial prompts use a **neutral third-person observer** tone. This voice is informative, slightly dry, and never condescending.
- Example: "The signal originated from the Vostok Array, a Remnant observatory in the outer ring of the Callisto system. Zara has marked the coordinates."
- This voice never editorializes, jokes, or expresses emotion. It is a tool, not a character.

### NPC Dialogue

- NPCs speak in **first person** and address the player in **second person**.
- Each NPC has a distinct voice (see `references/character-template.md`). Voice consistency is more important than variety of vocabulary.
- NPCs should never deliver exposition they would not realistically know or care about. A miner talks about mining. A scientist talks about science. If the player needs information outside an NPC's expertise, the NPC should direct them elsewhere.

### Codex Entries

- Written from the perspective of **in-world documents**: research papers, ship logs, intercepted transmissions, field notes.
- Each codex entry should have an implied author with an implied bias. A Concord Authority report and a Frontier smuggler's journal describe the same event differently.
- Codex entries use the tense appropriate to their format (past tense for historical accounts, present tense for field observations).

---

## Tense Conventions

| Content Type | Tense | Example |
|-------------|-------|---------|
| Quest log (active) | Present | "Investigate the signal source at Vostok Array." |
| Quest log (completed) | Past | "You investigated the Vostok Array and recovered Zara's data." |
| Dialogue | Present / context-dependent | "I've been tracking this signal for weeks." |
| Codex (historical) | Past | "The Callisto Accord was signed in 2801." |
| Codex (field notes) | Present | "The crystalline structures emit a low hum at 40 Hz." |
| Combat barks | Present imperative | "Shield failing!" / "Hostiles, bearing north!" |
| Environmental text (signs, terminals) | Present / imperative | "Warning: Atmosphere unstable beyond this point." |
| Cinematic narration | Present | "The door opens. Light floods the chamber." |
| Item descriptions | Present | "A corroded data chip. The Remnant glyphs are still legible." |

---

## Vocabulary and Terminology

### Preferred Terms

| Use This | Not This | Reason |
|----------|----------|--------|
| Voyager | Player, hero, protagonist | In-world term for the player's role |
| Remnant | Ancients, aliens, precursors | Established proper noun |
| Warp corridor | Hyperspace, jump gate | Specific to this universe's FTL |
| The Silence | The void, dark space | Proper noun for the unknown region |
| Concord Authority | The government, the feds | Proper faction name |
| Frontier | The wilds, the border | Established regional term |
| Deep Reach | Deep space, the unknown | Proper regional name |
| Station | Base, outpost (for large) | Consistency in scale terminology |
| Outpost | Station (for small) | Consistency in scale terminology |

### Forbidden Language

- No real-world brand names or contemporary slang
- No Earth-centric idioms unless deliberately used by a character as a quirk (e.g., an NPC who collects Old Earth sayings)
- No profanity beyond mild expletives; characters express anger through intensity, not vulgarity
- No meta-references to game mechanics in dialogue (NPCs do not say "quest" or "level up")

### Remnant Naming Conventions

Remnant sites, artifacts, and phenomena are named by human researchers, not by the Remnant themselves. Names follow academic convention: location-based ("Vostok Array"), descriptor-based ("The Lattice"), or discoverer-based ("Chen's Anomaly"). The Remnant had no known language; their glyphs remain untranslated.

---

## Integration Notes

- **For quest designers:** Every quest must reinforce at least one primary theme. Use the quest template (`references/quest-template.md`) to document which theme a quest serves.
- **For dialogue writers:** Read the character's profile before writing a single line. Voice consistency is reviewed during QA.
- **For level designers:** Environmental storytelling should follow the tone guide. Ruins are awe-inspiring, not horror-game scary. Frontier stations are rough but human, not dystopian.
- **For economy designers:** Reward structures should support the "Discovery Is the Reward" pillar. Lore unlocks and codex entries are first-class rewards alongside gear and currency.
