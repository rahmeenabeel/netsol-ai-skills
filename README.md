# Assumption Auditor

A Claude Agent Skill that hunts down hidden, unstated assumptions in any plan, argument, essay, or proposal — and forces the user to defend or fix each one before moving forward.

---

## 1. Problem Statement

Most plans, pitches, research proposals, and essays fail not because of bad logic, but because of **assumptions nobody questioned**. A business plan might assume immediate user demand. A research proposal might assume an urban hospital dataset generalizes to rural clinics. A policy essay might assume objective definitions of fairness exist.

People rarely catch their own blind spots—they are too close to their own reasoning. The **Assumption Auditor** skill solves this by acting as a structured, repeatable "outside eye" that systematically extracts, classifies, and unflinchingly challenges the assumptions buried inside any input text.

---

## 2. What the Skill Does

Given any input (a plan, research proposal, thesis, pitch, or essay), the skill executes a 5-step auditing pipeline:

1. **Extracts** every explicit and implicit assumption the text relies on.
2. **Classifies** each assumption by risk level (`Load-Bearing` vs. `Minor`) and category (`Factual` vs. `Value-Based`).
3. **Challenges** each one using **Dual-Angle Stress Testing** (Evidence Angle or Counter-Scenario Angle) and category-specific question templates.
4. **Evaluates User Defenses** against strict resolution criteria (`[DEFENDED]`, `[REVISED]`, `[DISCARDED]`), pushing back on vague rhetoric.
5. **Outputs a Clean Audit Report** summarizing which assumptions survived, which were revised, and which downstream features break from discarded assumptions.

---

## 3. Skill Architecture & File Tree

```
skills/assumption-auditor/
├── SKILL.md                 (core skill instructions & workflow)
├── references/
│   ├── assumption-types.md  (taxonomy definitions & practical examples)
│   └── challenge-patterns.md (challenge templates per category)
├── assets/
│   └── audit-report-template.md (standardized audit report layout)
└── tests/
    ├── test-research-proposal-1.md (Medical AI / Edge ML proposal)
    ├── test-research-proposal-2.md (Crypto / IoT consensus proposal)
    ├── test-essay-1.md             (AI hiring audit policy essay)
    ├── test-essay-2.md             (Remote work innovation essay)
    └── test-execution-log.md       (test execution & evaluation log)
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
