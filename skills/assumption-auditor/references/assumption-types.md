# Assumption Taxonomy

Every extracted assumption gets tagged with one of these four types. If an assumption seems to fit two categories, pick the one that's more central to *why* the assumption matters — don't dual-tag.

## 1. Factual
A claim about how the world currently is (or was, or will be) — verifiable in principle, even if no evidence is given here.

- *"70% of our target users own smartphones."*
- *"This dataset was collected without demographic bias."*

Test: Could you, in principle, go check this against reality (a study, a survey, a record)? If yes → Factual.

### Practical Examples
1. **Technical Capability**: *"Our backend framework will handle 10,000 concurrent WebSocket connections per instance without exceeding 50ms latency."*
2. **Market/Demographic Reality**: *"Over 70% of university students in targeted urban centers have continuous 4G mobile data access."*
3. **Data Availability**: *"The open-source healthcare dataset includes complete, uncorrupted clinical logs spanning 2018 to 2024."*

## 2. Value-Based
A claim about what matters, what's desirable, or what's the "right" priority — not verifiable by checking facts, only defensible by argument.

- *"Growth should be prioritized over profitability in year one."*
- *"Students deserve cheaper access than working professionals."*

Test: Could two reasonable people disagree even if they agreed on all the facts? If yes → Value-Based.

### Practical Examples
1. **User Preference**: *"Users prefer a minimalist, automated workflow over manual granular controls, even if automation occasionally misclassifies items."*
2. **Academic/Research Values**: *"Academic reviewers prioritize novel algorithmic architecture over thorough baseline benchmark comparisons."*
3. **Organizational Priority**: *"Clients will choose a vendor offering faster 24-hour turnaround over a vendor offering higher analytical precision at a slower pace."*

## 3. Causal
A claim that one thing leads to, enables, or prevents another — a mechanism, not just a correlation.

- *"Lower prices will drive higher adoption among students."*
- *"Faster onboarding reduces churn."*

Test: Does the assumption link an action/condition to an effect? If yes → Causal. (Causal assumptions are often also technically Factual/checkable — tag as Causal when the mechanism itself is the load-bearing part, not just the standalone fact.)

## 4. Definitional / Scope
A claim that silently defines a term, boundary, or category the rest of the argument depends on.

- *"Our 'users' means people who complete onboarding, not just downloads."*
- *"'Launch' means available in-app, not marketing-ready."*

Test: Does the argument depend on a word or boundary meaning one specific thing, when it could reasonably mean something else? If yes → Definitional/Scope.

---

**Load-bearing vs. Minor is a separate, orthogonal axis** (see SKILL.md Step 4) — every assumption gets both a Type (one of the four above) AND a Risk level (Load-bearing/Minor). An assumption can be Factual + Minor, or Value-Based + Load-bearing, etc. Don't conflate "factual" with "high risk" — value-based assumptions are often the most load-bearing and hardest to challenge.

### Load-Bearing Examples
1. **Research Proposal**: *"The synthetic training dataset accurately mirrors real-world distribution shifts encountered during live deployment."* (If false: the entire algorithm fails in production, invalidating the research hypothesis).
2. **Business Pitch**: *"Local regulatory authorities will classify our peer-to-peer platform as an information service rather than a financial broker."* (If false: the service becomes legally prohibited overnight).
3. **Policy Essay**: *"Increasing penalties for non-compliance will deter corporate carbon emissions more effectively than offering tax subsidies."* (If false: the recommended policy framework produces the opposite intended outcome).

### Minor Examples
1. **Operational Schedule**: *"The design team will finalize branding icons and typography selections by the end of Sprint 1."* (If false: placeholder icons can be used without delaying backend development).
2. **Survey Response Rate**: *"At least 15% of survey respondents will fill out the optional open-ended feedback box."* (If false: quantitative survey data remains completely usable).
3. **Tooling Selection**: *"Developers will prefer using Git CLI over graphical UI tools like GitHub Desktop during code reviews."* (If false: workflow efficiency changes slightly, but deliverables remain unaffected).

## Quick Reference Table

| Type | One-line test | Example |
|---|---|---|
| Factual | Could you check this against reality? | "Users own smartphones" |
| Value-Based | Could reasonable people disagree despite agreeing on facts? | "Growth > profitability" |
| Causal | Does it link an action to an effect? | "Lower price → higher adoption" |
| Definitional/Scope | Does it silently define a term/boundary? | "'Users' = onboarded, not downloads" |