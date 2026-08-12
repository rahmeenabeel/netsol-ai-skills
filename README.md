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

```text
Input: "We should launch the app in Pakistan first because our target users are mostly students."

Extracted Assumptions:
1. Students are the primary revenue source. (Load-bearing)
2. Pakistan has the infrastructure needed for launch. (Load-bearing)
3. Competitors haven't already captured this segment. (Minor)

Challenge for #1:
"If students have low purchasing power, how does this assumption affect your monetization model? What evidence supports this being your primary user base?"

→ User responds → assumption marked Defended / Revised / Discarded
→ Final audit report generated
```

---

## 3. Skill Architecture & File Tree

```text
skills/assumption-auditor/
├── SKILL.md (core skill instructions & workflow)
├── references/
│ ├── assumption-types.md (taxonomy definitions & practical examples)
│ └── challenge-patterns.md (challenge templates per category)
├── assets/
│ └── audit-report-template.md (standardized audit report layout)
└── tests/
    ├── test-research-proposal-1.md (Medical AI / Edge ML proposal)
    ├── test-research-proposal-2.md (Crypto / IoT consensus proposal)
    ├── test-essay-1.md (AI hiring audit policy essay)
    ├── test-essay-2.md (Remote work innovation essay)
    └── test-execution-log.md (test execution & evaluation log)
```

---

## 4. Usage & Trigger Guide

### Skill Triggers

Claude automatically activates this skill when a user:
- Shares a plan, proposal, pitch, research abstract, or essay.
- Uses prompt phrases like:
  - *"Audit my assumptions in this proposal."*
  - *"What am I missing here?"*
  - *"Poke holes in this argument."*
  - *"Check this plan for hidden assumptions."*

---

## 5. Team Task Division (50/50 Vertical Slice)

This project was co-developed by a 2-person team at Netsol Technologies. To ensure equal learning, work was split vertically so both members owned half of every layer (logic, taxonomy, templates, testing, and docs):

| Area | Team Member 1 | Team Member 2 (Rahmeen) |
|---|---|---|
| **Core Logic (`SKILL.md`)** | Extraction & Classification Logic (Step 1 & 2) | Challenge Generation & Defense Handling Logic (Step 3 & 4) |
| **Taxonomy (`assumption-types.md`)** | Category Definitions (Factual, Value-Based, Load-Bearing, Minor) | Practical Examples across multiple domains for each category |
| **Challenge Patterns (`challenge-patterns.md`)** | Factual & Load-Bearing Question Templates | Value-Based & Minor Question Templates |
| **Test Suite (`tests/`)** | Business Plans & Personal Decision Test Cases | Research Proposals & Policy/Societal Essay Test Cases |
| **Testing & Evaluation** | Test Run Execution & Log (Member 1 suite) | Test Run Execution & Log (`test-execution-log.md`) |
| **Report Layout (`audit-report-template.md`)** | Joint Co-design | Joint Co-design |
| **Documentation & Packaging** | README Architecture & Core Sections | README Usage, Triggers, & Member 2 Contributions |

---

## 6. Credits & Internship Context

Developed as part of the AI/ML Internship Program at **Netsol Technologies**. Inspired by the *"Minimum Viable Engineering"* agent skill design methodology.
