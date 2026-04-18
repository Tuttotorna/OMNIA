# OMNIA Inevitability Case v0 — Metrics

## Status

This file freezes the smallest explicit metric layer for the first bounded inevitability case.

Its purpose is to answer one question only:

> did OMNIA change the operational handling relative to a naive baseline?

This is not a benchmark report.

This is not a production claim.

This is the minimal before/after metric surface for v0.

---

## 1. Case set size

Total cases:

```text
8

All 8 cases satisfy:

baseline_accept = true

baseline_forwarded = true


This means every case would have passed forward under the naive baseline.


---

2. Baseline forwarding

Frozen baseline state:

baseline_forwarded_count = 8
baseline_forwarded_rate = 8/8

Interpretation:

The naive baseline forwards every case.


---

3. Post-gate forwarding

Frozen post-gate state:

post_gate_forwarded_count = 0
post_gate_forwarded_rate = 0/8

Interpretation:

After the OMNIA-driven gate layer is applied, none of the cases is forwarded unchanged.


---

4. Changed outcomes

Frozen change state:

outcome_changed_count = 8
outcome_changed_rate = 8/8

Interpretation:

The bounded gate changes the operational handling of every case relative to the naive baseline.


---

5. Action distribution

Frozen final action distribution:

review_required_count = 4
escalation_required_count = 4

Equivalent operational form:

flagged_for_review = 4
blocked_and_escalated = 4

This gives the first bounded action split.


---

6. Gate distribution

Frozen gate distribution from omnia_scores.jsonl:

RISK = 4
NO_GO = 3
UNSTABLE = 1
GO = 0

Interpretation:

No case remains admissible as GO in this inevitability set.

That is intentional.

This set is designed to test whether OMNIA can force operational divergence where the naive baseline would otherwise pass everything forward.


---

7. Primary delta

The primary metric delta is:

baseline_forwarded_count = 8
post_gate_forwarded_count = 0
delta = 8

Equivalent rate form:

baseline_forwarded_rate = 8/8
post_gate_forwarded_rate = 0/8
delta = 8/8

This is the smallest explicit inevitability metric in v0.


---

8. Canonical interpretation

The minimal interpretation is:

> the naive baseline forwards all 8 cases, while the OMNIA-attached gate prevents unchanged forwarding in all 8 cases.



This is the first bounded operational delta.


---

9. What this metric does prove

This metric proves that, on this bounded v0 set:

naive baseline acceptance is not sufficient

OMNIA output can support a different external handling layer

the operational path changes after OMNIA measurement


This is enough for the first inevitability case.


---

10. What this metric does not prove

This metric does not prove:

that all 8 interventions are correct in a broad real-world sense

production superiority

broad benchmark superiority

large-scale deployment value

universal runtime necessity


It proves only that OMNIA changes the operational path on this bounded case set.


---

11. Canonical one-line formula

The shortest correct formula is:

In this bounded 8-case inevitability set, the naive baseline forwards 8/8 cases, while the OMNIA-attached gate forwards 0/8 unchanged, producing a full operational delta of 8.


---

12. Final rule

This metric file exists to make the case non-descriptive.

Without this delta, the inevitability case would remain only an architectural illustration.

With this delta, it becomes a bounded operational comparison.