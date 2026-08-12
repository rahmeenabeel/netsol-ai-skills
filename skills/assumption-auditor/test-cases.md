# Test Cases — Person 1

Not part of the skill runtime. For manual testing before/during team review.

## Test Case 1 — Business/Product Plan
"We should launch the app in Pakistan first because our target users are
mostly students. Since students are highly active on social media, we can
rely on organic word-of-mouth instead of paid marketing for our initial
growth. Our freemium model will convert well because students are price-
sensitive and will want to avoid the premium tier's cost."

Intended buried assumptions: price-sensitive ≠ willing to convert at all
(freemium doesn't guarantee conversion just because premium is avoided);
"highly active on social media" assumed to translate directly into
word-of-mouth for *this specific app category*.

## Test Case 2 — Personal Decision
"I'm going to quit my job to freelance full-time starting next month. I've
saved three months of expenses, which should be enough of a cushion. My
current clients already like my work, so I expect they'll keep hiring me
even after I'm not full-time anywhere. Freelancing will also let me finally
have control over my schedule."

Intended buried assumptions: clients liking full-time work translates to
paying freelance rates/keeping the same volume; "control over schedule"
assumes freelance work won't just expand to fill all available time.

## Test Case 3 — Research Proposal
"We propose training a model to detect early signs of burnout using
employee Slack message patterns. Since burnout affects communication style,
changes in message frequency and tone should serve as reliable early
indicators. We'll use six months of historical data from three participating
companies to train the model. This approach avoids the cost and delay of
traditional employee surveys."

Intended buried assumptions: three companies' data generalizes to other
companies/industries (population assumption); communication style changes
are caused by burnout specifically, not other factors (stress, role change,
holidays); employees consented to and are unaware of this monitoring, which
may itself be an unstated ethical assumption.

## Test Case 4 — Essay/Argument
"Remote work should become the permanent default for knowledge workers.
Employees are more productive without office distractions, as shown by
the productivity spikes many companies saw in 2020. It also improves
quality of life by eliminating commutes. Companies that resist this shift
will struggle to retain top talent in the long run."

Intended buried assumptions: 2020 productivity spikes generalize to normal,
non-pandemic conditions (temporal assumption — the context was unusual);
"top talent" is assumed to universally value remote work over other factors
(value-based, treated as fact); commute elimination assumed to matter more
than other lost benefits (e.g., in-person collaboration).

## Test Case 5 — Personal/Health Decision
"I'm going to switch to a plant-based diet to improve my energy levels. A
few friends who made the switch said they felt better within weeks, so I
expect similar results. I'll also save money since meat is the most
expensive part of my grocery bill. Since I'm already a decent cook, the
transition shouldn't be too disruptive."

Intended buried assumptions: friends' self-reported experience generalizes
to this specific person (small, biased sample — classic anecdote-as-evidence
trap); being "a decent cook" assumed to transfer directly to plant-based
cooking specifically, which has different techniques/ingredients.

---

## Test Log (Run 1 — logic drafted, pre-merge with teammate's challenge steps)

| Test Case | Assumptions caught vs. intended | Classification accuracy | Notes |
|---|---|---|---|
| 1 (Business) | 2/2 buried caught | Good, but all 4 landed Load-bearing — check for over-flagging | Value-Based assumption (#1, target user choice) was mislabeled as fact by the input itself; taxonomy caught it correctly |
| 2 (Personal) | 2/2 buried caught | Good | Minor/Load-bearing split felt right |
| 3 (Research) | 3/3 caught incl. ethical one | Strong | Best evidence the checklist surfaces non-obvious assumptions |
| 4 (Essay) | 2/2 intended + found extra | Debatable — commute-vs-collaboration assumption might deserve Load-bearing, not Minor | Flag for team discussion |
| 5 (Health) | 2/2 caught | Good | Clean baseline case, nothing missed or over-flagged |

**Open issues for team review:**
1. Test Case 1 — every assumption landed Load-bearing. Check whether the Step 4 collapse test is too easy to satisfy, or the plan is genuinely that fragile. Added a mitigation note in SKILL.md Step 4 ("Watch for over-flagging") — re-test after teammate's challenge steps are merged in.
2. Test Case 4, assumption #3 (commute vs. collaboration) — ambiguous risk call, worth resolving live with teammate rather than unilaterally.