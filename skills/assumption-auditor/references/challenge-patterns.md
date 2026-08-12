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

---

## Value-Based Assumption Challenges

Value-Based assumptions rest on subjective priorities, preferences, ethics, or cultural/organizational values. Claude must challenge the assumption's universality, test explicit trade-offs, and separate stated preferences from real-world behavior.

### Challenge Template 1: The Universality & Consensus Probe
> **Pattern**: *"You assume [Target Group] values [Belief/Preference]. What empirical user feedback, behavioral data, or consensus evidence proves this preference is universal across your entire audience, rather than just an assumption of the author?"*
> 
> **Example**:
> *Assumption*: *"Users prefer an automated AI summary over reading full reports."*
> *Challenge*: *"You assume users value automated summaries over full reports. What behavioral telemetry or user research confirms that users actually trust and prefer automated summaries over reading full reports in high-stakes scenarios?"*

### Challenge Template 2: The Trade-off & Penalty Probe
> **Pattern**: *"By prioritizing [Value A], you implicitly sacrifice [Value B]. Have stakeholders explicitly acknowledged and agreed to accept the consequences of sacrificing [Value B]?"*
> 
> **Example**:
> *Assumption*: *"Our team prioritizes rapid release velocity over exhaustive pre-deployment testing."*
> *Challenge*: *"By prioritizing rapid release velocity, you implicitly accept higher post-launch bug rates and system instability. Have stakeholders explicitly agreed to accept the reputational penalty of post-launch downtime?"*

### Challenge Template 3: Stated vs. Revealed Preference Probe
> **Pattern**: *"People often state they care about [Value A] in theory, but act differently under pressure. How does your plan account for scenarios where actual user behavior contradicts this stated value?"*
> 
> **Example**:
> *Assumption*: *"Customers will pay a 20% premium for eco-friendly product packaging."*
> *Challenge*: *"While consumers state they value eco-friendly packaging in surveys, price sensitivity often overrides this at checkout. What evidence proves your customers will actually pay the 20% premium when completing transactions?"*

---

## Minor Assumption Challenges

Minor assumptions seem low-impact individually. Claude must challenge cumulative risk, surface hidden dependencies, and evaluate fallback friction.

### Challenge Template 1: The Cumulative Risk (Compound Failure) Probe
> **Pattern**: *"While this assumption appears minor in isolation, what happens if this and two other minor assumptions (e.g., [Minor Assumption X] and [Minor Assumption Y]) fail simultaneously? Does that create a compound failure?"*
> 
> **Example**:
> *Assumption*: *"Design icons will be delivered 2 days late."*
> *Challenge*: *"If icon delivery is delayed by 2 days, AND survey responses fall short by 20%, AND QA testing spills into launch week, does this minor delay compound into a missed release date?"*

### Challenge Template 2: The Hidden Dependency Probe
> **Pattern**: *"You classify [Assumption] as minor, but does any load-bearing component of your plan silently depend on this assumption executing perfectly?"*
> 
> **Example**:
> *Assumption*: *"All survey participants will complete the optional open-ended text box."*
> *Challenge*: *"You treat optional text box responses as a minor detail, but your qualitative sentiment analysis depends on them. If participants skip this field, does your qualitative research model break?"*

### Challenge Template 3: The Fallback & Friction Probe
> **Pattern**: *"If this minor assumption proves false, what is your exact operational fallback, and how much friction or delay does executing that fallback introduce?"*
> 
> **Example**:
> *Assumption*: *"Third-party API documentation is complete and up-to-date."*
> *Challenge*: *"If the third-party API documentation turns out to be outdated or inaccurate, what is your immediate fallback plan, and how many developer-hours will be lost to trial-and-error debugging?"*