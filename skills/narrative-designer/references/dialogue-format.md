# Dialogue Format Reference

The complete specification for dialogue data. All dialogue trees must conform to this schema so they can be imported by the dialogue engine, tested in automated pipelines, and localized for international releases.

---

## JSON Schema Overview

Every dialogue exchange is a single JSON file representing one conversation. A conversation is a directed graph of **nodes** (things an NPC says) connected by **responses** (things the player can say). The engine traverses this graph based on player input and game state.

### Top-Level Structure

```json
{
  "dialogue_id": "string (unique identifier)",
  "version": "string (semver, e.g. 1.0.0)",
  "speaker": {
    "id": "string (NPC internal ID)",
    "name": "string (display name)",
    "title": "string (optional role/title)"
  },
  "trigger": {
    "type": "string (interaction | proximity | event | automatic)",
    "conditions": ["array of condition strings"]
  },
  "nodes": [
    { "...node objects (see Node Schema below)" }
  ],
  "metadata": {
    "location": "string (where this dialogue occurs)",
    "quest_context": "string (associated quest ID, if any)",
    "estimated_duration": "string (e.g. 2min)",
    "voice_acted": "boolean",
    "priority": "integer (0-100, for dialogue queue ordering)",
    "tags": ["array of content tags"],
    "writer": "string (author attribution)",
    "last_updated": "string (ISO 8601 date)"
  }
}
```

### Node Schema

Each node represents a single dialogue beat -- one block of NPC speech followed by player response options.

```json
{
  "id": "string (unique within this dialogue)",
  "text": "string (what the NPC says)",
  "speaker_override": "string (optional, if someone other than the primary speaker talks)",
  "speaker_emotion": "string (emotion tag, see Emotion Tags below)",
  "animation": "string (optional animation trigger)",
  "camera": "string (optional camera direction: close_up | medium | wide | over_shoulder)",
  "audio_cue": "string (optional sound effect or music trigger)",
  "conditions": ["array of condition strings required to reach this node"],
  "effects": ["array of effect strings triggered when this node is displayed"],
  "responses": [
    { "...response objects (see Response Schema below)" }
  ],
  "next": "string (optional, auto-advance to this node if no responses)",
  "is_terminal": "boolean (if true, conversation ends after this node)"
}
```

### Response Schema

Each response is one option the player can select.

```json
{
  "id": "string (unique within this node)",
  "text": "string (what the player says)",
  "short_text": "string (optional abbreviated text for UI display if text is long)",
  "tooltip": "string (optional hover text explaining consequences)",
  "tone": "string (tone tag, see Tone Tags below)",
  "next": "string (node ID to advance to)",
  "requirements": ["array of requirement strings the player must meet"],
  "effects": ["array of effect strings triggered when player selects this"],
  "flags_set": ["array of flag strings set by this choice"],
  "hidden": "boolean (if true, option only appears when requirements are met)",
  "skill_check": {
    "skill": "string (skill name)",
    "difficulty": "integer (target number)",
    "success_next": "string (node ID on success)",
    "failure_next": "string (node ID on failure)"
  }
}
```

---

## Tag Systems

### Emotion Tags

Applied to `speaker_emotion` on nodes. These drive facial animation, voice tone selection, and portrait expression in the UI.

| Tag | Description | Animation Set |
|-----|-------------|---------------|
| `neutral` | Default state, conversational | idle_talk |
| `happy` | Genuine positive emotion | smile, gesture_open |
| `amused` | Dry humor, wry satisfaction | smirk, slight_nod |
| `worried` | Concern, anxiety | brow_furrow, glance_away |
| `afraid` | Fear, dread | eyes_wide, step_back |
| `angry` | Frustration, hostility | jaw_clench, lean_forward |
| `sad` | Grief, loss, melancholy | eyes_down, voice_low |
| `determined` | Resolve, conviction | chin_up, steady_gaze |
| `surprised` | Shock, disbelief | eyebrow_raise, step_back |
| `suspicious` | Distrust, wariness | eyes_narrow, arms_cross |
| `reverent` | Awe, spiritual weight | eyes_up, voice_hushed |
| `exhausted` | Physical or emotional fatigue | shoulders_slump, voice_flat |
| `secretive` | Hiding something, conspiratorial | lean_in, voice_low |
| `pleading` | Desperation, begging | hands_open, eyes_wide |

### Tone Tags

Applied to `tone` on player responses. These classify the player's approach and feed into the invisible reactivity system (see `references/branching-patterns.md`).

| Tag | Player Stance | Personality Axis |
|-----|--------------|------------------|
| `empathetic` | Kind, understanding | Compassion + |
| `pragmatic` | Practical, efficient | Pragmatism + |
| `curious` | Inquisitive, probing | Curiosity + |
| `aggressive` | Confrontational, forceful | Aggression + |
| `humorous` | Deflecting with wit | Humor + |
| `cautious` | Risk-averse, careful | Caution + |
| `honest` | Blunt, truthful | Honesty + |
| `deceptive` | Misleading, strategic | Deception + |
| `diplomatic` | Compromise-seeking | Diplomacy + |
| `defiant` | Rebellious, resistant | Defiance + |
| `scholarly` | Analytical, knowledge-focused | Intellect + |
| `dismissive` | Uninterested, cold | Detachment + |

### Condition Strings

Conditions gate node visibility and response availability. Format: `type:identifier:operator:value`.

```
flag:observed_sky_change                    -- Boolean flag is set
quest:starmap_investigation:status:active   -- Quest is in specific state
relationship:zara:>=:50                     -- Relationship score threshold
item:remnant_data_chip:count:>=:1           -- Player has item
skill:engineering:>=:30                     -- Skill level check
location:observatory                        -- Player is at location
time:night                                  -- Time of day
faction:concord_authority:reputation:>=:40  -- Faction standing
stat:health:<=:25                           -- Player stat threshold
dialogue:npc_zara_starmap:completed         -- Previous dialogue was finished
```

### Effect Strings

Effects are triggered when nodes display or responses are selected. Format: `type:target:operation:value`.

```
relationship:zara:+:5                       -- Increase relationship
relationship:zara:-:3                       -- Decrease relationship
flag:set:learned_about_silence              -- Set a boolean flag
flag:clear:zara_suspicious                  -- Clear a boolean flag
quest:starmap_investigation:advance         -- Move quest to next stage
quest:starmap_investigation:fail            -- Fail the quest
item:give:remnant_data_chip:1               -- Give item to player
item:remove:old_star_chart:1                -- Remove item from player
xp:grant:50                                 -- Grant experience points
faction:concord_authority:reputation:+:10   -- Change faction standing
unlock:codex:remnant_observatory_notes      -- Unlock a codex entry
camera:shake:light                          -- Trigger camera effect
audio:play:revelation_sting                 -- Play audio cue
```

---

## Formatting Conventions

### Text Formatting in Dialogue Strings

Dialogue text supports a limited set of inline markup for the engine's rich text renderer:

| Markup | Renders As | Usage |
|--------|-----------|-------|
| `*text*` | *Italic* | Internal thought, emphasis |
| `**text**` | **Bold** | Proper nouns on first mention, key terms |
| `{pause}` | Timed pause (0.5s) | Dramatic beat, hesitation |
| `{pause:1.5}` | Timed pause (custom) | Longer dramatic pauses |
| `{player_name}` | Player's chosen name | Dynamic insertion |
| `{player_title}` | Player's current title | Dynamic insertion |
| `[sfx:sound_id]` | Inline sound effect | Sound plays during text scroll |
| `\n` | Line break | Separate paragraphs within one node |

### Dialogue Writing Rules

1. **Maximum node text length:** 200 characters for standard dialogue, 400 for critical story beats. Players stop reading after two lines on screen.
2. **Maximum responses per node:** 4 visible options. More than 4 overwhelms the UI. Use conditions to filter contextually.
3. **Response text length:** Maximum 80 characters. Responses must be scannable at a glance.
4. **No orphan nodes:** Every node must be reachable from `start`. Run validation before committing.
5. **No dead ends:** Every non-terminal node must have at least one response or a `next` auto-advance.
6. **Terminal nodes must be explicit:** Set `is_terminal: true` on every conversation-ending node.
7. **One idea per node:** Each node conveys one piece of information or one emotional beat. Split multi-topic speech into chained nodes with auto-advance.
8. **Read it aloud:** If dialogue sounds wrong spoken, it is wrong written.

### File Naming Convention

```
dialogue_[speaker_id]_[context].json

Examples:
  dialogue_npc_zara_starmap.json
  dialogue_npc_kael_first_meeting.json
  dialogue_npc_director_voss_debrief.json
  dialogue_generic_merchant_browse.json
```

---

## Localization Notes

### String Extraction

All `text`, `short_text`, and `tooltip` fields in dialogue JSON are extracted into localization tables during the build pipeline. The extraction produces a CSV with columns:

```
dialogue_id, node_id, response_id, field, source_text, context_note, char_limit
```

### Writing for Localization

1. **Avoid idioms** that do not translate. "Bite the bullet" means nothing in Japanese. Use direct language.
2. **Allow for text expansion.** German and French text is typically 20-30% longer than English. UI layouts must accommodate this. Keep source text concise to give translators room.
3. **Gender-neutral language** where possible. If gender is relevant, provide male/female/neutral variants using the tag system: `{player_name:gendered:he|she|they}`.
4. **Context notes are mandatory.** Every string in the localization table must have a `context_note` explaining who is speaking, to whom, and in what emotional state. Translators cannot open the game; they work from spreadsheets.
5. **Do not split sentences across nodes** if the sentence structure might reorder in other languages. Each node should be a complete, self-contained thought.
6. **Placeholder variables** (`{player_name}`, `{item_name}`) must be documented with their possible values and grammatical role so translators can handle declension and articles.
7. **Character limits** must be specified for every string. The UI renderer has fixed text boxes. Overflows are runtime errors.

### Localization ID Format

Every translatable string gets a unique ID generated during extraction:

```
DLG_[dialogue_id]_[node_id]_TEXT
DLG_[dialogue_id]_[node_id]_[response_id]_TEXT
DLG_[dialogue_id]_[node_id]_[response_id]_TOOLTIP
```

---

## Example: Complete Dialogue File

```json
{
  "dialogue_id": "npc_zara_starmap_crisis",
  "version": "1.2.0",
  "speaker": {
    "id": "npc_zara",
    "name": "Zara",
    "title": "Star Cartographer"
  },
  "trigger": {
    "type": "interaction",
    "conditions": ["quest:starmap_investigation:status:active"]
  },
  "nodes": [
    {
      "id": "start",
      "text": "The constellations have shifted again. {pause} Someone is rewriting the sky.",
      "speaker_emotion": "worried",
      "conditions": [],
      "effects": [],
      "responses": [
        {
          "id": "ask_who",
          "text": "Who could do something like that?",
          "tone": "curious",
          "next": "explain_threat",
          "requirements": [],
          "effects": [],
          "flags_set": [],
          "hidden": false
        },
        {
          "id": "shared_knowledge",
          "text": "I noticed it too. My navigation charts are useless now.",
          "tone": "pragmatic",
          "next": "shared_experience",
          "requirements": ["flag:observed_sky_change"],
          "effects": ["relationship:zara:+:5"],
          "flags_set": ["zara_trusts_voyager"],
          "hidden": true
        },
        {
          "id": "dismiss",
          "text": "Stars shift. That is how the universe works.",
          "tone": "dismissive",
          "next": "dismissal",
          "requirements": [],
          "effects": ["relationship:zara:-:3"],
          "flags_set": [],
          "hidden": false
        }
      ]
    },
    {
      "id": "explain_threat",
      "text": "Not a who. A what. {pause} The Remnant observatories in the Deep Reach are activating. They are recalibrating something we cannot see.",
      "speaker_emotion": "afraid",
      "conditions": [],
      "effects": ["unlock:codex:remnant_observatory_notes"],
      "responses": [
        {
          "id": "volunteer",
          "text": "Point me at the nearest one. I will find out what they are doing.",
          "tone": "determined",
          "next": "accept_mission",
          "requirements": [],
          "effects": ["quest:starmap_investigation:advance"],
          "flags_set": ["volunteered_for_observatory"],
          "hidden": false
        },
        {
          "id": "ask_more",
          "text": "How do you know the observatories are responsible?",
          "tone": "scholarly",
          "next": "evidence",
          "requirements": [],
          "effects": [],
          "flags_set": [],
          "hidden": false
        }
      ]
    },
    {
      "id": "shared_experience",
      "text": "You have seen it? {pause} Good. I was starting to think I was losing my mind. The Concord is ignoring my reports.",
      "speaker_emotion": "surprised",
      "conditions": [],
      "effects": ["relationship:zara:+:3"],
      "responses": [
        {
          "id": "offer_help",
          "text": "You are not alone in this. What do you need?",
          "tone": "empathetic",
          "next": "accept_mission",
          "requirements": [],
          "effects": ["quest:starmap_investigation:advance", "relationship:zara:+:5"],
          "flags_set": ["volunteered_for_observatory"],
          "hidden": false
        }
      ]
    },
    {
      "id": "dismissal",
      "text": "If you say so, Voyager. {pause} But when your warp calculations start failing, remember I warned you.",
      "speaker_emotion": "angry",
      "conditions": [],
      "effects": ["flag:set:zara_warning_dismissed"],
      "responses": [],
      "next": null,
      "is_terminal": true
    },
    {
      "id": "evidence",
      "text": "The shift pattern matches the resonance frequency of Remnant sensor arrays. I have twenty years of star charts. This is not natural drift.",
      "speaker_emotion": "determined",
      "conditions": [],
      "effects": [],
      "responses": [
        {
          "id": "convinced",
          "text": "That is good enough for me. Where do I start?",
          "tone": "pragmatic",
          "next": "accept_mission",
          "requirements": [],
          "effects": ["quest:starmap_investigation:advance"],
          "flags_set": ["volunteered_for_observatory"],
          "hidden": false
        },
        {
          "id": "skill_check_verify",
          "text": "[Science] Let me see the resonance data myself.",
          "tone": "scholarly",
          "next": null,
          "requirements": [],
          "effects": [],
          "flags_set": [],
          "hidden": false,
          "skill_check": {
            "skill": "science",
            "difficulty": 40,
            "success_next": "verified",
            "failure_next": "accept_mission"
          }
        }
      ]
    },
    {
      "id": "verified",
      "text": "You... actually understand the data? {pause} I have been explaining this to bureaucrats for months. It is refreshing to talk to someone who reads a spectrograph.",
      "speaker_emotion": "happy",
      "conditions": [],
      "effects": ["relationship:zara:+:10", "xp:grant:25"],
      "responses": [
        {
          "id": "to_mission",
          "text": "The data confirms it. Let us get to work.",
          "tone": "pragmatic",
          "next": "accept_mission",
          "requirements": [],
          "effects": ["quest:starmap_investigation:advance"],
          "flags_set": ["volunteered_for_observatory", "zara_respects_science"],
          "hidden": false
        }
      ]
    },
    {
      "id": "accept_mission",
      "text": "The nearest active observatory is in the Vostok system. I have marked coordinates on your nav console. {pause} Be careful. The last survey team that went out there went silent.",
      "speaker_emotion": "worried",
      "conditions": [],
      "effects": ["flag:set:vostok_coordinates_received"],
      "audio_cue": "ui_quest_update",
      "responses": [],
      "next": null,
      "is_terminal": true
    }
  ],
  "metadata": {
    "location": "observatory",
    "quest_context": "starmap_investigation",
    "estimated_duration": "3min",
    "voice_acted": true,
    "priority": 80,
    "tags": ["main_quest", "remnant", "mystery", "zara_arc"],
    "writer": "narrative_team",
    "last_updated": "2026-02-19"
  }
}
```

---

## Validation Checklist

Before committing any dialogue file, verify:

- [ ] All node IDs are unique within the file
- [ ] All `next` references point to existing node IDs
- [ ] Every non-terminal node has responses or a `next` auto-advance
- [ ] Terminal nodes have `is_terminal: true`
- [ ] No unreachable nodes (every node reachable from `start`)
- [ ] All emotion tags are from the approved list
- [ ] All tone tags are from the approved list
- [ ] Condition and effect strings follow the documented format
- [ ] Node text respects the 200/400 character limit
- [ ] Response text respects the 80 character limit
- [ ] No more than 4 visible responses per node
- [ ] Context notes are present for all translatable strings
- [ ] File name follows `dialogue_[speaker]_[context].json` convention
- [ ] `version` field is incremented if editing an existing file
