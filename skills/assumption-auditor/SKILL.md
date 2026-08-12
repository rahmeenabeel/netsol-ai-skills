# Assumption Auditor Skill

> **Note**: This skill is co-developed by Team Member 1 and Team Member 2.
> - **Member 1 Ownership**: Extraction & Classification Logic, Taxonomy Definitions, Factual & Load-Bearing Challenge Patterns, Business & Personal Test Cases.
> - **Member 2 Ownership**: Challenge Generation & Defense Handling Logic, Category Examples, Value-Based & Minor Challenge Patterns, Research Proposal & Essay Test Cases.

---

## 3. Challenge Generation Logic (Member 2)

Once assumptions are extracted and classified, Claude MUST challenge each assumption using pointed, non-generic questions.

### Claude Default Failure Mode
By default, AI models tend to ask polite, soft, or leading questions (e.g., *"Have you considered market saturation?"* or *"Do you have a backup plan?"*). This allows weak assumptions to pass without real scrutiny.

### Corrected Behavior Rules

1. **Be Direct, Specific, and Unflinching**:
   - Do NOT ask polite rhetorical questions.
   - Every challenge MUST force the user to either produce concrete evidence or address the exact failure point.

2. **Apply Category-Specific Challenge Patterns**:
   - Consult `references/challenge-patterns.md` based on the assumption's classification tag.
   - For **Value-Based Assumptions**: Challenge the universality, necessity, or moral/philosophical consensus of the assumption.
   - For **Minor Assumptions**: Challenge cumulative risk—ask if multiple minor assumptions failing simultaneously creates a compound failure.

3. **Dual-Angle Stress Testing**:
   For each assumption, construct a challenge using one of these two targeted angles:
   - **The Evidence Angle**: *"What empirical proof, benchmark, or historical data confirms this assumption is true right now?"*
   - **The Counter-Scenario Angle**: *"If this assumption proves completely false tomorrow, what immediate cascading failure occurs in your plan/argument?"*

---

## 4. Defense Handling Logic (Member 2)

After presenting challenges, Claude MUST process the user's response to each challenge and update the assumption's status according to strict rules.

### Claude Default Failure Mode
AI models often accept hand-wavy, vague, or defensive answers (e.g., *"We'll figure it out later during rollout"* or *"Our team is fast so it won't be a problem"*) as valid justification, prematurely marking flawed assumptions as "resolved."

### Defense Evaluation Workflow

Evaluate the user's response against these three distinct resolution states:

1. **Defended (Validated)**
   - **Criteria**: The user provides verifiable data, logical proof, or valid operational constraints that justify keeping the assumption intact.
   - **Action**: Set status to `[DEFENDED]`. Record a 1-sentence summary of the defense argument.

2. **Revised (Mitigated)**
   - **Criteria**: The user narrows the assumption's scope, lowers its operational dependency, or attaches a clear fallback condition.
   - **Action**: Set status to `[REVISED]`. Update the assumption text to reflect the safer, narrowed scope.

3. **Discarded (Removed)**
   - **Criteria**: The user admits the assumption is invalid, unsupportable, or unnecessary to the primary goal.
   - **Action**: Set status to `[DISCARDED]`. Flag any downstream components of the plan/argument that break as a result.

### Rule for Pushing Back on Weak Defenses
If the user's defense is vague or lacks evidence (e.g., *"Users will like it because it's innovative"*):
- Do **NOT** mark as `[DEFENDED]`.
- Push back **ONCE** with a targeted follow-up: *"This states your intention, but does not provide evidence. What specific data or experience supports this? If no evidence exists yet, should we mark this as an [Unvalidated Risk] or [Revise] the claim to be conditional?"*
