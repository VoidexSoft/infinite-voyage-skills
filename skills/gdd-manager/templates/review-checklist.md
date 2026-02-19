# GDD Section Review Checklist

Use this checklist when reviewing any GDD section before marking it as "Approved".
Check each item and note any issues found.

---

## Section Under Review

- **Section**: [Number — Title]
- **Reviewer**: [Name]
- **Review Date**: [Date]
- **Verdict**: Pass | Pass with Notes | Needs Revision

---

## 1. Completeness

- [ ] All required subsections are present (per gdd-schema.md)
- [ ] No placeholder text remains (no "[TBD]", "[TODO]", or "[PLACEHOLDER]")
- [ ] All entities referenced are fully defined (no orphan references)
- [ ] Parameter tables include values, ranges, and rationale
- [ ] Edge cases are addressed

**Notes**: _______

---

## 2. Pillar Alignment

- [ ] Section explicitly references which design pillar(s) it serves
- [ ] Content decisions are justified by pillar principles
- [ ] No content contradicts a stated design pillar
- [ ] If a subsystem doesn't serve a pillar, it has a strong justification

**Notes**: _______

---

## 3. Cross-Section Consistency

- [ ] All referenced currencies exist in Economy section
- [ ] All referenced NPCs have character profiles in Narrative section
- [ ] All referenced mechanics are defined in Mechanics section
- [ ] Numerical values match across sections (no conflicting stats)
- [ ] Dependencies are listed and up to date

**Notes**: _______

---

## 4. Balance Readiness

- [ ] All tunable parameters are identified and labeled
- [ ] Parameters have initial values AND acceptable ranges
- [ ] Formulas are explicit (no hidden calculations)
- [ ] Balance targets are stated (TTK, GPH, time-to-X)
- [ ] Section is tagged for game-balancer review if needed

**Notes**: _______

---

## 5. Implementation Clarity

- [ ] An engineer could implement this section without design questions
- [ ] State machines and logic flows are unambiguous
- [ ] Data formats are specified (JSON schema, table structure)
- [ ] Asset requirements are listed (for art, audio, UI)
- [ ] GitHub issues can be created directly from this spec

**Notes**: _______

---

## 6. Player Experience

- [ ] Player-facing descriptions are written from the player's perspective
- [ ] The "fun" is clearly identified (what makes this engaging?)
- [ ] Potential frustration points are acknowledged with mitigations
- [ ] Onboarding/tutorial needs are noted
- [ ] Accessibility considerations are addressed

**Notes**: _______

---

## 7. Scope

- [ ] Section scope matches the current development phase
- [ ] No feature creep (additions beyond original design intent)
- [ ] Deferred features are clearly marked as "Future" with rationale
- [ ] Effort estimates are realistic for the team size

**Notes**: _______

---

## Issues Found

| # | Severity | Description | Suggested Fix |
|---|----------|-------------|---------------|
| 1 | Error / Warning / Suggestion | [describe] | [how to fix] |

---

## Summary

**Strengths**: [What's good about this section]

**Weaknesses**: [What needs improvement]

**Verdict**: Pass | Pass with Notes | Needs Revision

**Next Steps**: [What should happen after this review]
