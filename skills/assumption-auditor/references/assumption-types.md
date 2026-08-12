# Assumption Taxonomy & Types

This document outlines the standard taxonomy used by the Assumption Auditor skill to categorize assumptions pulled from input texts. 

- **Definitions**: Authored by Member 1.
- **Practical Examples**: Authored by Member 2.

---

## 1. Factual Assumptions

### Definition (Member 1)
Assumptions rooted in verifiable, empirical statements about data, metrics, technical capabilities, historical events, or real-world conditions.

### Practical Examples (Member 2)
1. **Technical Capability**: *"Our backend framework will handle 10,000 concurrent WebSocket connections per instance without exceeding 50ms latency."*
2. **Market/Demographic Reality**: *"Over 70% of university students in targeted urban centers have continuous 4G mobile data access."*
3. **Data Availability**: *"The open-source healthcare dataset includes complete, uncorrupted clinical logs spanning 2018 to 2024."*

---

## 2. Value-Based Assumptions

### Definition (Member 1)
Implicit or explicit beliefs regarding human preferences, ethics, subjective priorities, organizational values, or user desires.

### Practical Examples (Member 2)
1. **User Preference**: *"Users prefer a minimalist, automated workflow over manual granular controls, even if automation occasionally misclassifies items."*
2. **Academic/Research Values**: *"Academic reviewers prioritize novel algorithmic architecture over thorough baseline benchmark comparisons."*
3. **Organizational Priority**: *"Clients will choose a vendor offering faster 24-hour turnaround over a vendor offering higher analytical precision at a slower pace."*

---

## 3. Load-Bearing Assumptions

### Definition (Member 1)
High-impact, foundational assumptions upon which the entire argument, business model, or thesis rests. If a load-bearing assumption proves false, the entire proposal collapses.

### Practical Examples (Member 2)
1. **Research Proposal**: *"The synthetic training dataset accurately mirrors real-world distribution shifts encountered during live deployment."* (If false: the entire algorithm fails in production, invalidating the research hypothesis).
2. **Business Pitch**: *"Local regulatory authorities will classify our peer-to-peer platform as an information service rather than a financial broker."* (If false: the service becomes legally prohibited overnight).
3. **Policy Essay**: *"Increasing penalties for non-compliance will deter corporate carbon emissions more effectively than offering tax subsidies."* (If false: the recommended policy framework produces the opposite intended outcome).

---

## 4. Minor Assumptions

### Definition (Member 1)
Low-impact, tactical, or secondary assumptions. If proven false, they require minor tweaks, minor budget reallocations, or small schedule adjustments, but do not threaten the overall viability of the project.

### Practical Examples (Member 2)
1. **Operational Schedule**: *"The design team will finalize branding icons and typography selections by the end of Sprint 1."* (If false: placeholder icons can be used without delaying backend development).
2. **Survey Response Rate**: *"At least 15% of survey respondents will fill out the optional open-ended feedback box."* (If false: quantitative survey data remains completely usable).
3. **Tooling Selection**: *"Developers will prefer using Git CLI over graphical UI tools like GitHub Desktop during code reviews."* (If false: workflow efficiency changes slightly, but deliverables remain unaffected).
