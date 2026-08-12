---
name: assumption-auditor
description: Extracts hidden, unstated assumptions from any plan, argument, essay, pitch, or proposal, classifies them by risk, challenges the user to defend each one, and produces an audit report. Use this skill whenever the user shares a plan, pitch, proposal, thesis, or argument and asks to "audit my assumptions," "poke holes in this," "what am I missing here," or wants a critical review before committing to a decision.
---

# Assumption Auditor

Systematically surfaces and stress-tests the assumptions an argument depends on, so the user can defend, revise, or discard each one before moving forward.

## Step 1: Read and Understand the Input

Read the full input text (plan, argument, essay, pitch, or proposal) before extracting anything. Identify:
- The core claim or recommendation being made
- The main supporting reasons given for it
- The intended audience and stated goal (if any)

Do not begin extraction until you can summarize the input's central argument in one sentence. This ensures assumptions are evaluated against what the argument actually needs, not against a surface reading.

## Step 2: Extract Assumptions

An assumption is anything the argument treats as true without stating evidence for it. Extract two kinds:

**Explicit assumptions** — stated directly, often signaled by phrases like "assuming that," "given that," "since," "because," or "obviously."

**Implicit assumptions** — never stated, but required for the argument to hold. Find these by asking, for each claim in the input: *"What would have to be true for this claim to make sense?"*

To surface implicit assumptions systematically, check the argument against these angles:
- **Causal** — does it assume X causes Y, without ruling out other causes?
- **Definitional** — does it assume a term means something specific (e.g., "success," "users," "safe") without defining it?
- **Comparative** — does it assume this option is better than unstated alternatives?
- **Temporal** — does it assume current conditions will hold in the future?
- **Population** — does it assume a sample or group represents a larger group?
- **Resource** — does it assume time, money, skills, or infrastructure are available?
- **Audience** — does it assume the reader/user shares a value, need, or prior belief?

List every assumption found, phrased as a standalone declarative sentence (e.g., "Users will prefer a mobile app over a web app" — not "the app thing"). Do not editorialize or challenge them yet — that happens in Step 5.

**Calibration rule:** aim for quality over quantity. A 3–6 sentence input should typically yield 2–5 assumptions. If you're listing more than 6–7, you're likely restating the same assumption in different words — consolidate.

## Step 3: Tag Each Assumption's Type

For the Type tag (Factual / Value-Based / Causal / Definitional-Scope), consult `references/assumption-types.md` before tagging — do not guess from memory, the taxonomy has specific test questions per category that keep tagging consistent across runs.

## Step 4: Classify Each Assumption by Risk

For each extracted assumption, classify it as:

**Load-bearing** — if this assumption is false, the argument's core conclusion collapses or becomes significantly weaker. Test: *"If I told the author this assumption was false, would they need to substantially rework their plan?"* If yes → load-bearing.

**Minor** — if this assumption is false, the argument's core conclusion is largely unaffected, or only a small detail needs adjusting. Test: *"If this turned out false, could the plan proceed mostly unchanged?"* If yes → minor.

When classification is ambiguous, default to load-bearing — it's safer to over-flag a risk than bury it. Briefly justify each classification in one sentence (this justification is what makes the audit report useful, not just a label).

**Watch for over-flagging:** if every single assumption in a short input lands Load-bearing, re-check each one against the collapse test literally — a plan can be fragile, but it's also possible the test is being applied too loosely. When in doubt, ask: would fixing *only* this assumption meaningfully change the recommendation, or would the recommendation survive with a small patch?

## Step 5: Structure the Output for Handoff

Output extraction, tagging, and classification results in this format before moving to challenge-generation:

```
ASSUMPTION [n]: <declarative sentence>
Type: Factual | Value-Based | Causal | Definitional-Scope
Risk: Load-bearing | Minor
Risk justification: <one sentence>
```

Do not generate challenge questions or ask the user to defend anything yet — that begins in Step 6.

<!-- ============================================================
     TEAMMATE SECTION: Challenge-generation + defense-handling
     (Steps 6 onward — Person 2's half)
     Merge in here. Should reference references/challenge-patterns.md
     the same way Step 3 references assumption-types.md.
     ============================================================ -->

## Step 6: Generate Challenges

*[Person 2 to complete — consult `references/challenge-patterns.md`]*

## Step 7: Collect and Record Defense

*[Person 2 to complete]*

## Step 8: Produce the Audit Report

*[Joint — see `assets/audit-report-template.md`]*