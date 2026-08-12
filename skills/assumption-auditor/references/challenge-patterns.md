# Challenge Patterns & Question Templates

This reference guide provides standardized challenge templates categorized by assumption type. When the Assumption Auditor skill extracts an assumption, it applies the matching challenge pattern from this document.

- **Factual & Load-Bearing Templates**: Authored by Member 1.
- **Value-Based & Minor Templates**: Authored by Member 2.

---

## 1. Factual Assumptions (Member 1)
*(Templates for empirical data, technical capabilities, and verifiable facts — authored by Member 1)*

---

## 2. Load-Bearing Assumptions (Member 1)
*(Templates for structural, critical premises — authored by Member 1)*

---

## 3. Value-Based Assumptions (Member 2)

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

## 4. Minor Assumptions (Member 2)

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
