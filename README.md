# Assumption Auditor

A Claude Skill that hunts down hidden, unstated assumptions in any plan, argument, essay, or proposal — and forces the user to defend or fix each one before moving forward.

---

## 1. Problem Statement

Most plans, pitches, and arguments fail not because of bad logic, but because of **assumptions nobody questioned**. A business plan might assume demand exists. A research proposal might assume a dataset is unbiased. An essay might assume its audience already agrees with its premise.

People rarely catch their own blind spots — they're too close to their own reasoning. The **Assumption Auditor** skill solves this by acting as a structured, repeatable "outside eye" that systematically extracts and challenges the assumptions buried inside any input text.

---

## 2. What the Skill Does

Given any input (a plan, argument, thesis, pitch, or proposal), the skill:

1. **Extracts** every explicit and implicit assumption the text relies on.
2. **Classifies** each assumption by risk level (e.g., *load-bearing* vs. *minor*).
3. **Challenges** each one with a pointed question or counter-scenario.
4. **Requests a defense** from the user — accept, revise, or discard the assumption.
5. **Outputs a clean audit report** summarizing which assumptions survived, which were fixed, and which remain unresolved.

### Example Flow
```
Input: "We should launch the app in Pakistan first because our target
        users are mostly students."

Extracted Assumptions:
1. Students are the primary revenue source. (Load-bearing)
2. Pakistan has the infrastructure needed for launch. (Load-bearing)
3. Competitors haven't already captured this segment. (Minor)

Challenge for #1:
"If students have low purchasing power, how does this assumption
affect your monetization model? What evidence supports this being
your primary user base?"

→ User responds → assumption marked Defended / Revised / Discarded
→ Final audit report generated
```

---

## 3. Skill Architecture

```
assumption-auditor/
├── SKILL.md                 (required — triggers + instructions)
├── references/
│   ├── assumption-types.md  (taxonomy of assumption categories)
│   └── challenge-patterns.md (question templates by category)
└── assets/
    └── audit-report-template.md
```

**SKILL.md** contains:
- **Description** — when Claude should trigger this skill (e.g., user shares a plan, pitch, proposal, thesis, or asks "audit my assumptions" / "what am I missing here" / "poke holes in this").
- **Instructions** — the step-by-step extraction → classification → challenge → report workflow.
- **Output format** — a consistent audit report structure (see `assets/audit-report-template.md`).

---

## 4. Development Workflow

Following the standard skill-building loop:

1. **Draft** — write the first version of SKILL.md with the core workflow.
2. **Test** — run 8–10 sample inputs (business plans, essays, research proposals, personal decisions) through the skill.
3. **Review** — evaluate outputs together: Are assumptions genuinely load-bearing? Are challenges sharp, not generic?
4. **Iterate** — refine instructions, add assumption categories, tighten output format.
5. **Package** — finalize and export the `.skill` file.

---

## 5. Task Division (Team of 2 — 50/50 Split)

Instead of splitting by "easy vs. hard" role, work is split so each member owns **half of every layer** — both touch the core logic, both touch testing. This keeps effort and learning even.

| Area | Member 1 | Member 2 |
|---|---|---|
| **Core Skill Logic (`SKILL.md`)** | Draft the extraction + classification steps (how assumptions are pulled out and ranked as load-bearing vs. minor) | Draft the challenge-generation + defense-handling steps (how Claude questions each assumption and processes the user's response) |
| **Assumption Taxonomy** | Define assumption categories (factual, value-based, load-bearing, minor) | Write examples for each category to validate the taxonomy makes sense in practice |
| **Reference Content (`challenge-patterns.md`)** | Write challenge/question templates for half the categories | Write challenge/question templates for the other half of categories |
| **Test Cases** | Build 4–5 test cases (e.g., business plans, personal decisions) | Build 4–5 test cases (e.g., research proposals, essays) |
| **Testing & Evaluation** | Run own test cases through the skill, log results | Run own test cases through the skill, log results |
| **Output Formatting (`audit-report-template.md`)** | Co-design the report layout together (joint 30-min session) | Co-design the report layout together (joint 30-min session) |
| **Documentation (README, examples)** | Write half the sections | Write half the sections |
| **Final Review & Packaging** | Joint review of all test outputs, then package `.skill` file together | Joint review of all test outputs, then package `.skill` file together |

> Both members work through the full pipeline (logic → taxonomy → testing → docs) instead of one person owning "hard" parts and the other owning "easy" parts. Swap in actual names once finalized.

---

## 6. Suggested Timeline

| Phase | Duration | Milestone |
|---|---|---|
| Design & Draft | 2–3 days | First working SKILL.md |
| Testing Round 1 | 2 days | 8–10 test cases run, feedback logged |
| Revision | 2 days | Refined logic + templates |
| Testing Round 2 | 1–2 days | Re-run test cases, confirm improvement |
| Packaging & Docs | 1 day | Final `.skill` file + polished README |

---

## 7. Future Improvements

- Add a "confidence score" per assumption based on how much evidence supports it.
- Persistent tracking: log assumptions across multiple sessions to catch contradictions over time.
- Domain-specific challenge sets (technical/research vs. business vs. personal decisions).

---

## 8. Credits

Built by [Member 1 Name] and [Member 2 Name].
