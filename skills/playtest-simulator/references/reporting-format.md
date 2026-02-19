# Playtest Report Format Template

Standard format for all virtual playtest reports in Infinite Voyage. This template ensures
consistent, actionable reports that design teams can quickly parse, prioritize, and act on.

---

## Report Structure Overview

Every playtest report follows this structure:

1. Header and Metadata
2. Executive Summary
3. Archetype Findings
4. Issue Severity Matrix
5. Recommendation Priority Table
6. Data Tables and Evidence
7. Methodology Section
8. Appendices

---

## Section 1: Header and Metadata

```markdown
# Playtest Report: [Content Name]

| Field              | Value                                         |
|--------------------|-----------------------------------------------|
| Report ID          | PT-[YYYY]-[NNN] (e.g., PT-2026-014)          |
| Date               | [ISO date]                                    |
| Content Tested     | [Specific mechanic, quest, zone, or system]   |
| Content Version    | [GDD section reference or commit hash]        |
| Archetypes Tested  | [List of archetypes simulated]                |
| Scenario Used      | [Reference to simulation-scenarios.md]        |
| Tested By          | [Simulator operator name or "AI Simulation"]  |
| Status             | [Draft / Review / Final]                      |
| Related Reports    | [Links to prior reports on same content]      |
```

### Naming Conventions
- Report IDs are sequential within a year: PT-2026-001, PT-2026-002, etc.
- Content names match GDD section names exactly for traceability
- Version references point to the exact design state that was tested

---

## Section 2: Executive Summary

The executive summary is the most-read section. It must stand alone and communicate
the key findings in under 60 seconds of reading time.

```markdown
## Executive Summary

**Overall Assessment:** [GREEN / YELLOW / RED]

[2-3 sentences summarizing the most important findings. Lead with the single most
critical finding. Include whether the content is ready for implementation, needs
revision, or requires major rework.]

**Top Finding:** [One sentence describing the most impactful discovery]

**Archetype Most at Risk:** [Which player type had the worst experience and why]

**Recommended Action:** [Ship as-is / Revise and retest / Major redesign needed]
```

### Assessment Criteria

| Rating | Meaning                                                         |
|--------|-----------------------------------------------------------------|
| GREEN  | No critical issues. Minor issues only. Ready for implementation |
| YELLOW | Major issues found but fixable. Revise and retest               |
| RED    | Critical issues or fundamental design problems. Redesign needed |

---

## Section 3: Archetype Findings

Present findings for each tested archetype. Use the following template per archetype.

```markdown
## Archetype Findings

### [Archetype Name] Experience

**Overall Satisfaction:** [1-5 scale] [one-word summary: Excellent/Good/Mixed/Poor/Failed]

**Walkthrough Summary:**
[3-5 sentences describing the archetype's journey through the content, focusing on
key decisions, emotional beats, and friction points.]

**Highlight Moments:**
- [Positive moment 1: what worked well for this archetype]
- [Positive moment 2]

**Friction Points:**
- [Friction 1: what caused frustration, confusion, or boredom]
- [Friction 2]

**Would They Return?** [Yes / Probably / Unlikely / No] — [brief reason]

**Time Spent:** [estimated duration for this archetype to complete the content]

**Unique Findings:**
[Anything this archetype specifically discovered that others would not —
exploits for Optimizer, hidden content for Explorer, group issues for Socializer, etc.]
```

### Satisfaction Scale Reference

| Score | Label     | Meaning                                                |
|-------|-----------|--------------------------------------------------------|
| 5     | Excellent | Content is a highlight; archetype would recommend it   |
| 4     | Good      | Enjoyable with minor issues; would replay              |
| 3     | Mixed     | Some good, some bad; might skip on replay              |
| 2     | Poor      | Mostly frustrating or boring; would avoid              |
| 1     | Failed    | Content is broken, incomprehensible, or hostile        |

---

## Section 4: Issue Severity Matrix

All issues found across all archetypes, deduplicated and classified.

```markdown
## Issue Severity Matrix

### Critical Issues (P0) — Must fix before implementation

| ID     | Issue                | Found By      | Description                        | Impact          |
|--------|----------------------|---------------|------------------------------------|-----------------|
| ISS-01 | [Short name]         | [Archetype]   | [Detailed description]             | [Who is affected and how] |

### Major Issues (P1) — Fix in next revision

| ID     | Issue                | Found By      | Description                        | Impact          |
|--------|----------------------|---------------|------------------------------------|-----------------|
| ISS-02 | [Short name]         | [Archetype]   | [Detailed description]             | [Who is affected and how] |

### Minor Issues (P2) — Fix when convenient

| ID     | Issue                | Found By      | Description                        | Impact          |
|--------|----------------------|---------------|------------------------------------|-----------------|
| ISS-03 | [Short name]         | [Archetype]   | [Detailed description]             | [Who is affected and how] |

### Observations (P3) — No fix needed, but worth noting

| ID     | Observation          | Found By      | Description                        | Relevance       |
|--------|----------------------|---------------|------------------------------------|-----------------|
| OBS-01 | [Short name]         | [Archetype]   | [Detailed description]             | [Why it matters]|
```

### Severity Definitions

| Priority | Name      | Criteria                                                  | SLA          |
|----------|-----------|-----------------------------------------------------------|--------------|
| P0       | Critical  | Blocks progress, breaks systems, ruins core experience    | Before ship  |
| P1       | Major     | Significantly degrades experience for one or more archetypes | Next revision |
| P2       | Minor     | Noticeable but does not block or significantly harm       | Backlog      |
| P3       | Observe   | Design notes, edge cases, or subjective preferences       | Track only   |

### Issue Counting Summary

Include a count at the bottom of the matrix:

```
Total Issues: [N]
  Critical (P0): [n]
  Major (P1):    [n]
  Minor (P2):    [n]
  Observations:  [n]
```

---

## Section 5: Recommendation Priority Table

Concrete, actionable fixes for every issue, assigned to the appropriate skill.

```markdown
## Recommendations

| Issue ID | Recommendation              | Assigned Skill      | Effort    | Priority | Dependencies      |
|----------|-----------------------------|---------------------|-----------|----------|-------------------|
| ISS-01   | [Specific fix description]  | [skill name]        | [S/M/L]   | P0       | [other issues]    |
| ISS-02   | [Specific fix description]  | [skill name]        | [S/M/L]   | P1       | None              |
```

### Effort Sizing

| Size | Meaning                                         | Typical Time    |
|------|-------------------------------------------------|-----------------|
| S    | Small tweak: number change, text edit, flag flip | Under 1 hour    |
| M    | Medium change: new logic, new content, rework    | 1-4 hours       |
| L    | Large change: system redesign, major rework      | 4+ hours        |

### Skill Assignment Guide

| Issue Type             | Assigned Skill          |
|------------------------|-------------------------|
| Stat balance           | game-balancer           |
| Narrative/dialogue     | narrative-designer      |
| Level layout/flow      | level-designer          |
| Economy/pricing        | economy-designer        |
| System mechanics       | systems-designer        |
| Data/spreadsheet       | data-modeler            |
| Bug/implementation     | github-gamedev          |
| Multiple skills        | List all, note primary  |

---

## Section 6: Data Tables and Evidence

Supporting data that backs up the findings. Include tables, calculations, and
specific examples.

```markdown
## Data and Evidence

### Combat Data (if applicable)

| Encounter        | Archetype   | TTK (sec) | Deaths | Damage Taken | Potions Used | Satisfaction |
|------------------|-------------|-----------|--------|--------------|--------------|--------------|
| [Encounter name] | Optimizer   | [value]   | [n]    | [value]      | [n]          | [1-5]        |
| [Encounter name] | Casual      | [value]   | [n]    | [value]      | [n]          | [1-5]        |

### Economy Data (if applicable)

| Activity              | Gold Earned | Gold Spent | Net Flow | Time (min) | Gold/Hour |
|-----------------------|-------------|------------|----------|------------|-----------|
| [Activity name]       | [value]     | [value]    | [+/-]    | [value]    | [value]   |

### Progression Data (if applicable)

| Milestone             | Archetype   | Time to Reach | Level at Reach | On Target? |
|-----------------------|-------------|---------------|----------------|------------|
| [Milestone name]      | Casual      | [value]       | [level]        | [Y/N]      |

### Exploit Evidence (if applicable)

| Exploit               | Steps to Reproduce      | Severity | Reproducible? | Net Gain    |
|-----------------------|-------------------------|----------|---------------|-------------|
| [Exploit name]        | 1. [step] 2. [step] ... | [P0-P2]  | [Always/Sometimes] | [value] |
```

### Evidence Guidelines
- Include specific numbers, not vague descriptions
- Show calculations for balance claims (e.g., "DPS is 15% above target because...")
- Reference exact design values from the GDD or data tables
- Screenshots or step-by-step reproduction for exploits

---

## Section 7: Methodology

Document how the simulation was conducted for reproducibility.

```markdown
## Methodology

### Simulation Parameters

| Parameter             | Value                                     |
|-----------------------|-------------------------------------------|
| Scenario Template     | [Reference to simulation-scenarios.md]    |
| Player Level Range    | [Starting level - ending level]           |
| Gear Assumptions      | [Gear state description]                  |
| Knowledge Level       | [First play / Experienced / Expert]       |
| Difficulty Setting    | [Easy / Normal / Hard]                    |
| Session Length Model   | [Duration and pattern]                    |
| RNG Assumptions       | [Average luck / Best case / Worst case]   |

### Archetype Methodology

For each archetype, describe the decision-making framework used:

- **[Archetype]:** [1-2 sentences on how decisions were made for this archetype.
  Reference player-archetypes.md for the full profile used.]

### Limitations

[List known limitations of this simulation. Examples:]
- Virtual simulation cannot capture "feel" — controller feedback, animation quality
- Multiplayer dynamics were modeled but not truly simulated
- RNG outcomes were assumed average; extreme luck scenarios not tested
- Emotional engagement is estimated, not measured
```

---

## Section 8: Appendices

Optional additional material.

```markdown
## Appendices

### Appendix A: Full Archetype Walkthroughs
[Detailed step-by-step walkthroughs if not included in the main body]

### Appendix B: Raw Data
[Complete data sets, calculation spreadsheets, or extended tables]

### Appendix C: Comparison to Previous Reports
[If this content was tested before, compare findings to see what improved or regressed]

### Appendix D: Open Questions
[Questions that arose during simulation that need human designer input]
```

---

## Report Checklist

Before marking a report as complete, verify:

- [ ] Header metadata is fully populated
- [ ] Executive summary can be understood without reading the full report
- [ ] Every archetype tested has a findings section
- [ ] All issues have severity classifications
- [ ] All issues have recommendations with skill assignments
- [ ] Data tables include specific numbers, not vague descriptions
- [ ] Methodology section documents all assumptions
- [ ] Limitations are honestly stated
- [ ] Issue IDs are unique and sequential within the report
- [ ] Related reports are cross-referenced
- [ ] Report status is set correctly (Draft/Review/Final)

---

## Distribution

After completion, the report should be routed to:

| Recipient             | Reason                                        |
|-----------------------|-----------------------------------------------|
| game-balancer         | All balance flags and stat issues              |
| narrative-designer    | All narrative flags and pacing issues          |
| level-designer        | All layout and flow issues                     |
| systems-designer      | All mechanic and system issues                 |
| economy-designer      | All economy and pricing issues                 |
| github-gamedev        | All bugs and implementation tasks              |
| Project lead          | Executive summary and critical issues          |
