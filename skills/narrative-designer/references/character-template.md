# Character Profile Template

A complete template for designing characters in Infinite Voyage. Every named NPC -- from major story figures to recurring merchants -- should have a profile document. The depth of the profile scales with the character's importance, but even minor characters benefit from having their core motivations defined.

---

## Profile Depth Guidelines

| Character Tier | Examples | Required Sections |
|---------------|---------|-------------------|
| **Tier 1: Major** | Crew members, main antagonists, central quest givers | All sections, fully detailed |
| **Tier 2: Supporting** | Faction leaders, recurring NPCs, side quest anchors | Identity, Personality, Voice, Relationships, Gameplay Function |
| **Tier 3: Minor** | One-off quest NPCs, named merchants, ambient characters | Identity, Personality (core trait + flaw), Voice (speech pattern + 2 example lines), Gameplay Function |
| **Tier 4: Generic** | Unnamed guards, random colonists, ambient crowd | Not profiled individually; covered by faction/location voice guides |

---

## Template

### Identity

```markdown
# Character: [Display Name]

## Identity

- **Full Name:** [Complete name including titles, aliases, call signs]
- **Character ID:** [Internal ID: npc_firstname_lastname]
- **Role:** [Their function in the game world, not their gameplay function]
- **Species/Origin:** [Human, augmented, etc. -- homeworld or station of origin]
- **Age:** [Approximate age, or age range if ambiguous]
- **Pronouns:** [For dialogue systems and localization]
- **Affiliation:** [Faction, organization, or independent]
- **First Appearance:** [Quest ID or location where the player first encounters them]
```

### Personality

```markdown
## Personality

- **Core Trait:** [The single defining characteristic -- if you could only describe them in one word, what would it be?]
- **Flaw:** [What makes them fallible and relatable? This should create conflict.]
- **Want:** [What they consciously pursue -- their stated goal]
- **Need:** [What they actually need but may not recognize -- their deeper truth]
- **Fear:** [What drives their worst decisions -- the thing they will do anything to avoid]
- **Coping Mechanism:** [How they handle stress -- humor, withdrawal, control, denial, overwork?]
- **Moral Alignment:** [Not D&D alignment. Where do they sit on the game's moral spectrums? What lines will they not cross? What lines have they already crossed?]

### Personality in Practice

| Situation | Behavior |
|-----------|----------|
| Under pressure | [How they act when things go wrong] |
| When they trust someone | [How their guard drops] |
| When they are lied to | [How they react to betrayal] |
| When they are proven wrong | [Can they admit fault?] |
| Alone and unobserved | [What do they do when no one is watching?] |
```

### Backstory

```markdown
## Backstory

### Before the Game
[2-4 paragraphs covering their life before the player meets them. Focus on:
- Where they came from (origin, upbringing)
- The defining moment that made them who they are
- How they arrived at their current situation
- What they have lost or sacrificed]

### The Wound
[Every compelling character carries a wound -- an unresolved trauma or loss that
shapes their present behavior. What is this character's wound? How does it manifest
in their daily life? The player may or may not learn about the wound; it exists to
inform how the character is written, even when it is never stated directly.]

### Secrets
[What does this character know that they are not telling? List 1-3 secrets, ranked
by severity. Secrets may be revealed through quests, relationship progression, or
never at all.]

1. **[Secret Name]** -- [Description. Who else knows? What would happen if it came out?]
```

### Motivations

```markdown
## Motivations

### Primary Drive
[The engine that moves this character forward. What do they wake up for? What keeps
them going when things are hard?]

### Relationship to the Remnant
[Every character in Infinite Voyage has an opinion about the Remnant -- the central
mystery of the game. What is this character's stance? Curiosity? Fear? Exploitation?
Reverence? Indifference?]

### Relationship to Authority
[Where does this character stand on the Concord Authority vs. Frontier independence
spectrum? Why?]

### What They Would Do for the Player
[Under what circumstances would this character help the player? What would they
refuse to do? Where is their line?]

### What They Would Do Against the Player
[Under what circumstances would this character oppose the player? What would push
them into antagonism?]
```

### Relationships

```markdown
## Relationships

| Character | Relationship | Dynamic | Evolution |
|-----------|-------------|---------|-----------|
| [NPC Name] | [Nature: ally, rival, mentor, etc.] | [The texture of the relationship: respectful disagreement, unspoken love, grudging tolerance] | [How this relationship can change based on player actions or story progression] |
| The Voyager (Player) | [Initial stance] | [How they view the player at first meeting] | [How the relationship can develop -- best case, worst case, and most likely case] |
```

### Voice

```markdown
## Voice

- **Speech Pattern:** [Formal / casual / poetic / clipped / rambling / precise]
- **Vocabulary Level:** [Educated / simple / technical / archaic / mixed]
- **Sentence Structure:** [Short and direct / long and winding / questions / declarative]
- **Verbal Tics:** [Catchphrases, filler words, habits, things they repeat when nervous]
- **Accent/Dialect Notes:** [If applicable -- region of origin affects speech]
- **What They Never Say:** [Words or topics this character avoids -- can be revealing]
- **Humor Style:** [Dry / slapstick / dark / none / self-deprecating / deadpan]

### Example Lines

Write 6 lines that capture this character's voice across emotional states:

- **Neutral:** "[A line of ordinary conversation]"
- **Happy:** "[A line expressing genuine joy or satisfaction]"
- **Angry:** "[A line expressing frustration or hostility]"
- **Afraid:** "[A line when they are scared or threatened]"
- **Vulnerable:** "[A line when their guard is down]"
- **Under Pressure:** "[A line in a crisis or combat situation]"

### Voice Don'ts

[List 2-3 things this character would NEVER say or ways they would NEVER speak.
This is often more useful than "voice dos" for maintaining consistency.]

- They would never: [example]
- They would never: [example]
```

### Character Arc

```markdown
## Arc

- **State at Introduction:** [Who is this character when the player first meets them? What is their emotional and situational starting point?]
- **Catalyst:** [What event or relationship changes them? This may be player-driven.]
- **Midpoint Shift:** [How have they changed halfway through their arc?]
- **Crisis:** [The moment that tests their transformation -- do they revert or grow?]
- **Resolution:** [Who do they become? Describe the best, worst, and neutral outcomes.]
- **Player Influence:** [How specifically can the player affect this arc? Which choices matter?]

### Arc Variations

| Player Approach | Arc Outcome | Final State |
|----------------|-------------|-------------|
| [Supportive/empathetic] | [Best-case arc] | [Who they become at their best] |
| [Neutral/pragmatic] | [Default arc] | [Who they become without intervention] |
| [Hostile/dismissive] | [Worst-case arc] | [Who they become when abandoned or opposed] |
```

### Visual Description

```markdown
## Visual Description

### Physical Appearance
[2-3 sentences describing what the player sees. Focus on the details that make this
character visually distinct and memorable. What would an artist need to know?]

### Distinguishing Features
[1-3 features that make this character immediately recognizable in a crowd.
A scar, a specific garment, an unusual posture, a piece of technology.]

### Body Language
[How this character carries themselves. Posture, gestures, eye contact habits.
This informs animation and signals personality before the character speaks.]

### Wardrobe
[What they wear and why. Clothing communicates status, faction, personality,
and history. Note any items that change over the course of their arc.]

### Art Direction Notes
[Specific guidance for character artists: color palette, visual motifs, references
to existing art or characters in other media that capture the intended feel.]
```

### Gameplay Function

```markdown
## Gameplay Function

- **Services:** [Shop, quest giver, trainer, crafting, information broker, crew role]
- **Primary Location:** [Where the player finds them most of the time]
- **Schedule:** [Do they move around? Day/night differences? Quest-dependent relocation?]
- **Combat Role:** [If a companion: tank, support, DPS, etc. If an enemy: threat type]
- **Unique Mechanic:** [Does this character introduce or embody a unique game mechanic?]
- **Inventory:** [If a merchant: what do they sell? How does their stock change?]
- **Quest Involvement:** [List all quests this character appears in, with role]

| Quest ID | Role | Importance |
|----------|------|-----------|
| [quest_id] | [Giver / Ally / Antagonist / Cameo] | [Critical / Supporting / Flavor] |
```

---

## Example: Fully Profiled Character

```markdown
# Character: Zara Osei

## Identity

- **Full Name:** Dr. Zara Osei, Star Cartographer First Class
- **Character ID:** npc_zara_osei
- **Role:** Leading expert on stellar cartography and Remnant observatory systems
- **Species/Origin:** Human, born on Meridian Station (Core Systems)
- **Age:** 42
- **Pronouns:** She/her
- **Affiliation:** Independent researcher, formerly Concord Authority Science Division
- **First Appearance:** quest_first_voyage (tutorial), observatory deck on Waypoint Station Cygnus

## Personality

- **Core Trait:** Relentless curiosity -- she cannot leave a question unanswered
- **Flaw:** She prioritizes knowledge over safety, both her own and others'
- **Want:** To understand what the Remnant were watching -- to decode the sky
- **Need:** To accept that some answers are not worth the cost of finding them
- **Fear:** Irrelevance -- that she will spend her life studying and never understand
- **Coping Mechanism:** Overwork. When stressed, she retreats into data, charts, and calculations. She stops eating, stops sleeping, and stops talking to people.
- **Moral Alignment:** Believes knowledge should be free and unrestricted. Distrusts the Concord Authority's information control policies. Will bend rules but not betray individuals. Has not yet faced a situation where knowledge directly caused harm -- when she does, it will break her.

### Personality in Practice

| Situation | Behavior |
|-----------|----------|
| Under pressure | Becomes hyper-focused, speaks faster, starts citing data |
| When she trusts someone | Shares half-formed theories, asks for their opinion, makes dry jokes |
| When she is lied to | Goes quiet, then coldly dismantles the lie with evidence |
| When she is proven wrong | Genuinely excited -- a wrong theory means a better one exists |
| Alone and unobserved | Talks to her star charts. Hums the same melody she cannot identify. |

## Backstory

### Before the Game
Zara grew up on Meridian Station, a Concord Authority administrative hub. Her
parents were both civil servants -- reliable, cautious, deeply boring by her
account. She showed aptitude for mathematics early and won a scholarship to the
Concord Science Academy, where she specialized in astrometric analysis.

For fifteen years she worked in the Concord Authority Science Division, mapping
warp corridor stability and cataloging stellar drift. It was important work. It
was also, by her account, "watching paint dry across a hundred light-years." She
was competent, respected, and profoundly unsatisfied.

Everything changed when Survey Team Epsilon discovered the first Remnant observatory
in the Deep Reach. Zara was assigned to analyze its star charts -- charts that
depicted constellations from positions no human telescope could reach. She became
obsessed. When the Concord Authority classified her findings and reassigned her to
routine corridor mapping, she resigned.

She now works independently from Waypoint Station Cygnus, selling navigational
data to fund her real work: decoding the Remnant's observations.

### The Wound
Her younger brother, Kofi, was a survey pilot. He volunteered for a Deep Reach
mission based on coordinates Zara provided from her early Remnant research. His
ship was lost. The Concord Authority ruled it an equipment failure. Zara believes
the coordinates led him somewhere dangerous -- that her research killed him. She
has never said this aloud. She honors him by continuing the work, telling herself
that understanding the danger will prevent future losses. She is not sure she
believes this.

### Secrets

1. **Kofi's coordinates** -- The coordinates she gave her brother point to a
   location inside The Silence. She has never reported this to anyone. She is
   terrified of what it means.

2. **Concord Authority data** -- She copied classified files when she resigned.
   Her independent research is built on stolen data. If the Authority found out,
   she would be arrested.

3. **The melody** -- The song she hums is not from any human composition. She
   first heard it in the resonance patterns of the Remnant observatory data.
   She does not consciously know this.

## Motivations

### Primary Drive
Understanding the Remnant's purpose. Not just what they built, but why. She
believes the answer is in the stars they were watching.

### Relationship to the Remnant
Reverence bordering on obsession. She views the Remnant as the greatest
scientists who ever existed -- peers she will never meet. She does not fear
their technology; she respects it. This lack of fear may be her undoing.

### Relationship to Authority
Distrustful. She believes the Concord Authority prioritizes control over
knowledge. She left their service and does not regret it, but she also
understands why they operate the way they do -- she just disagrees.

### What She Would Do for the Player
Share her research freely if the player shows genuine interest. Provide
coordinates, analysis, and context for any Remnant site. Risk her safety
to accompany the player to a significant discovery. Argue passionately on
the player's behalf if they support open research.

### What She Would Do Against the Player
If the player shuts down a Remnant observatory or destroys research data,
Zara will oppose them. She will not become violent, but she will withdraw
cooperation, share information with the player's rivals, and potentially
sabotage future missions that she believes threaten irreplaceable knowledge.

## Relationships

| Character | Relationship | Dynamic | Evolution |
|-----------|-------------|---------|-----------|
| Director Voss | Former superior | Mutual respect poisoned by institutional disagreement | Can become allied if Voss is pushed toward reform |
| Dr. Okafor (deceased) | Colleague, friend | Okafor encouraged Zara's obsession; her death is a mirror | Learning about Okafor's fate forces Zara to confront her own path |
| Kofi Osei (missing) | Brother | Unresolved grief and guilt | Discovering Kofi's fate is Zara's crew quest climax |
| The Voyager (Player) | Professional interest | Sees the player as a capable tool at first | Can become genuine friendship, or bitter disappointment |

## Voice

- **Speech Pattern:** Precise, rapid when excited, clipped when annoyed
- **Vocabulary Level:** Highly educated, scientific terminology used naturally (not to impress)
- **Sentence Structure:** Declarative statements. She states things as facts, then supports them. Rarely asks questions -- she makes observations and waits for responses.
- **Verbal Tics:** "Look at this" (when showing data), "That is not nothing" (when finding a clue), slight pause before saying anything emotional
- **Accent/Dialect Notes:** Meridian Core accent -- crisp vowels, no contractions when formal
- **What She Never Says:** "I don't know" -- she says "I don't know yet" or "The data is insufficient." She never admits permanent ignorance.
- **Humor Style:** Dry, understated, often mathematical ("The odds of that being coincidence are roughly the odds of a star forming in my coffee cup.")

### Example Lines

- **Neutral:** "The stellar drift in sector seven is three degrees off predicted. That is worth investigating."
- **Happy:** "Do you see this? The resonance pattern matches. Twenty years of data and it finally matches."
- **Angry:** "You destroyed it. You walked into a structure older than our entire civilization and you turned it off like a light switch."
- **Afraid:** "The signal is coming from inside The Silence. {pause} Kofi's last known coordinates were inside The Silence."
- **Vulnerable:** "I keep thinking... if I had not given him those coordinates. If I had just waited for more data."
- **Under Pressure:** "The power core is destabilizing. We have eight minutes. I need three of them -- give me three minutes with the array."

### Voice Don'ts

- She would never use slang or casual contractions in professional contexts
- She would never dismiss data without examining it, no matter the source
- She would never shout -- her anger is cold, precise, and devastating

## Arc

- **State at Introduction:** Brilliant, isolated, obsessed. She has been working alone for years and has forgotten what collaboration feels like.
- **Catalyst:** The player's arrival -- someone who actually goes where her data points. For the first time, her theories can be tested.
- **Midpoint Shift:** She begins to care about the player as a person, not just a research asset. She starts sharing personal details. She is also getting closer to answers that frighten her.
- **Crisis:** The discovery of what happened to Kofi. She must choose between continuing her research (which may lead to the same fate) or stopping.
- **Resolution:** Best case: she finds a way to honor Kofi while continuing safely. Worst case: she pushes too far and pays the price. Default: she retreats, unresolved.
- **Player Influence:** The player's choices about Remnant technology directly shape her arc. Supporting her research strengthens her resolve (for good or ill). Destroying research breaks her trust. Finding Kofi's fate is the turning point.

### Arc Variations

| Player Approach | Arc Outcome | Final State |
|----------------|-------------|-------------|
| Supportive, pro-research | Zara pushes further, makes a breakthrough, confronts the cost | Pioneer who changes humanity's understanding, scarred but fulfilled |
| Neutral, balanced | Zara continues at her own pace, resolution deferred | Still searching, but no longer alone |
| Hostile, anti-research | Zara loses faith, withdraws from the player, works alone | Isolated again, potentially reckless without the player's moderating influence |

## Visual Description

### Physical Appearance
A tall woman with dark brown skin and close-cropped silver hair (premature --
she was dark-haired in her twenties). Sharp features, high cheekbones, eyes that
focus on things other people cannot see. Lean build from forgetting to eat.

### Distinguishing Features
- Silver hair against dark skin -- immediately recognizable
- Always carries a portable star chart projector on her left wrist
- A small scar on her right hand from a lab accident she refuses to discuss

### Body Language
Economical movement. She does not fidget. When she looks at something, she gives
it her full attention. Her stillness can be intimidating. When excited, the
stillness breaks -- she gestures rapidly and moves toward whatever caught her
interest without social awareness.

### Wardrobe
Practical research wear: fitted dark jacket over a high-collared shirt, cargo
pants with tool loops, magnetic boots. Everything chosen for function. One
personal touch: a woven bracelet in green and gold, Kofi's colors.

### Art Direction Notes
Color palette: deep indigo, silver, warm brown. She should feel like a contrast
to the cold environments she works in -- warm skin tones against blue-lit
observatories. Visual motif: stars and constellations subtly integrated into
clothing patterns or jewelry. Reference: Danai Gurira's intensity, Ruth Negga's
stillness.

## Gameplay Function

- **Services:** Quest giver (main quest, crew quest), star chart vendor, Remnant data analysis
- **Primary Location:** Observatory deck, Waypoint Station Cygnus (Acts 1-2); Player's ship (Act 3 if recruited)
- **Schedule:** Day: observatory deck working on charts. Evening: mess hall or player's ship. Night: observatory deck (she does not sleep much).
- **Combat Role:** Not a combatant. If present during combat encounters, she provides scan data (enemy weakness identification) as a support passive.
- **Unique Mechanic:** "Star Reading" -- Zara can analyze Remnant navigation data to reveal hidden locations on the star map. This ability improves as the player's relationship with her deepens.
- **Inventory:** Sells star charts (reveal map regions), navigation algorithms (warp efficiency upgrades), and Remnant data fragments (lore items).

| Quest ID | Role | Importance |
|----------|------|-----------|
| quest_first_voyage | Tutorial NPC (brief) | Supporting |
| quest_silent_observatory | Quest giver, remote support | Critical |
| quest_zara_stargazer (crew quest) | Primary subject | Critical |
| quest_deep_reach_mapping | Quest giver | Supporting |
| quest_the_silence | Companion, key participant | Critical |
```

---

## Quick Reference Checklist

Before submitting a character profile for review:

- [ ] Character ID follows `npc_firstname_lastname` convention
- [ ] Profile depth matches character tier
- [ ] Core trait and flaw create potential for internal conflict
- [ ] Want and need are distinct (want is external, need is internal)
- [ ] Backstory explains present behavior without over-explaining
- [ ] At least one secret exists for Tier 1 and Tier 2 characters
- [ ] Voice is distinct -- example lines could not be spoken by another character
- [ ] Voice don'ts are specified (prevents voice drift during production)
- [ ] Relationship to the Remnant is defined (ties character to central theme)
- [ ] Arc variations cover supportive, neutral, and hostile player approaches
- [ ] Visual description includes distinguishing features and art direction notes
- [ ] Gameplay function is documented with quest involvement table
- [ ] All referenced quest IDs exist or are flagged as planned
