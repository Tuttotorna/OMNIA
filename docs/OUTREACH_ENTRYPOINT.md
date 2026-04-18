# OUTREACH_ENTRYPOINT.md

OMNIA is a post-hoc structural measurement core for detecting when outputs that pass a naive baseline should still not be passed forward unchanged.

The current public entry point is:

```text
docs/FIRST_PUBLIC_CASE.md

The first bounded public case shows this:

baseline_forwarded_count: 8
post_gate_forwarded_count: 0
outcome_changed_count: 8
delta_forwarded: 8

In other words:

baseline_pass != safe_to_pass_forward

This is not a broad benchmark claim. It is one bounded operational case showing that a naive pass condition is not enough once structural admissibility is measured.

Fastest reproducible command:

python examples/omnia_inevitability_case_v0/rebuild_and_analyze_case.py

Repository:

https://github.com/Tuttotorna/OMNIA