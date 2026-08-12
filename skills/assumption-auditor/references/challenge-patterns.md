# Challenge Patterns

Each assumption gets challenged using the template(s) matching its Type and Risk level. Templates are questions — fill in the bracketed parts with specifics from the actual assumption, never leave them generic. A challenge that could apply to any assumption in any input is a failed challenge; rewrite it until it only makes sense for *this* assumption.

When an assumption is both a specific Type AND Load-bearing, combine one Type-specific template with one Load-bearing template into a single, non-repetitive challenge rather than stacking separate questions back-to-back. Prioritize specificity over template-completeness — a sharp two-sentence challenge beats four generic questions stapled together.

---

## Factual Assumption Challenges

Use when Type = Factual. Goal: force the user to name real evidence, not just restate confidence.

**Evidence-source template:**
> "What specific evidence — data, a study, past experience, a source — supports [assumption] being true for [the specific case in the input, not the general case]?"

**Base-rate template:**
> "[Assumption] — is this true in general, or specifically true for [the exact population/context named in the input]? What's the gap between those two?"

**Recency/staleness template:**
> "When was this last verified? Is there a chance [assumption] was true before but has since changed?"

**Counter-evidence template:**
> "What would you expect to see if [assumption] were actually false? Have you looked for that?"

*Example applied:*
Assumption: "70% of our target users own smartphones."
> "What specific evidence — a survey, market report, or comparable product's data — supports 70% smartphone ownership specifically among *your* target segment in *this* market, rather than the general population?"

---

## Load-Bearing Assumption Challenges

Use when Risk = Load-bearing, regardless of Type (stack with the Type-specific template above).

**Collapse-test template:**
> "If [assumption] turned out to be false, what specifically in your plan would need to change? Walk through it — does the whole approach need rethinking, or just one part?"

**Single-point-of-failure template:**
> "Is [assumption] doing more work than any other claim in this argument? What else in your plan depends on it being true?"

**Pre-mortem template:**
> "Imagine this plan failed in six months. Looking back, is [assumption] the most likely reason why? If not this one, which assumption would you flag instead?"

**De-risking template:**
> "Is there a cheaper or faster way to test [assumption] before committing fully to a plan that depends on it?"

*Example applied:*
Assumption: "Students are the primary revenue source." (Load-bearing)
> "If it turns out students aren't your primary revenue source, does your entire monetization model need to change, or just your marketing targeting? What's the cheapest way to test this assumption before you build around it?"

<!-- ============================================================
     TEAMMATE SECTION: Value-Based, Causal, Definitional/Scope
     challenge templates — Person 2 to append below.
     Follow the same format: template name, one-line goal,
     3-4 bracketed question templates, one worked example.
     ============================================================ -->