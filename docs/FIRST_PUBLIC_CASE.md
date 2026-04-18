# FIRST_PUBLIC_CASE

## Status

This document defines the first public-facing case for OMNIA CORE v1.

Its purpose is simple:

> show one bounded, readable, externally legible result with an explicit operational delta.

Not the whole architecture.
Not the whole ecosystem.
Not every mini-result.

One case.
One claim.
One before/after change.

---

## Core public claim

The first public claim is:

> outputs that pass a naive baseline are not always safe to pass forward unchanged.

In OMNIA terms:

```text
baseline_pass != safe_to_pass_forward

This is the first public-facing claim because it is:

small

readable

falsifiable

operationally relevant



---

Chosen public case

The chosen public case is:

examples/omnia_inevitability_case_v0/

This directory contains the first bounded end-to-end inevitability case.

Its core files are:

baseline_results.jsonl

omnia_scores.jsonl

gate_actions.jsonl

final_results.jsonl

metrics.md

analyze_case.py


This is the canonical first public case of the repository.


---

Why this case was chosen

Earlier mini-results proved readable divergence.

That was useful, but still incomplete.

This case was chosen because it adds the missing layer:

baseline
-> OMNIA measurement
-> external gate action
-> changed operational outcome

This makes the project easier to understand externally.

It is no longer only:

readable output vs structural admissibility


It is now:

naive pass vs gated intervention


That is the first real necessity surface.


---

Public result summary

For this bounded 8-case inevitability set:

baseline_accept_count = 8
baseline_forwarded_count = 8
post_gate_forwarded_count = 0
outcome_changed_count = 8
delta_forwarded = 8

Frozen gate distribution:

GO = 0
RISK = 4
NO_GO = 3
UNSTABLE = 1

Frozen action split:

flagged_for_review = 4
blocked_and_escalated = 4

This means:

the naive baseline forwards all 8 cases

the OMNIA-attached gate prevents unchanged forwarding in all 8 cases

4 cases are redirected to review

4 cases are redirected to escalation


This is the first public operational delta.


---

Public interpretation

The intended public interpretation is minimal:

> a naive baseline can pass every case, while an OMNIA-attached gate can still prevent unsafe unchanged forwarding.



Or more directly:

> passing a baseline is not the same as being safe to pass forward.



Nothing larger is needed for the first public case.


---

What this case proves

This case proves that OMNIA can already do one public-facing operational thing:

receive a bounded case set that passes a naive baseline

separate those cases by structural admissibility

support different downstream actions

change the operational path


This shows that OMNIA is not merely a descriptive layer.

That is enough for a first public case.


---

What this case does not prove

This case does not prove:

broad benchmark superiority

production readiness

semantic correctness

universal truth claims

broad safety claims

large-scale deployment value


It is one bounded public case only.


---

Canonical public formula

The shortest correct public formula is:

In a bounded 8-case inevitability set, the naive baseline forwards 8/8 cases, while the OMNIA-attached gate forwards 0/8 unchanged, producing a full operational delta of 8.


---

Public-facing run commands

Analyze the bounded inevitability case:

python examples/omnia_inevitability_case_v0/analyze_case.py

Rebuild the broader frozen result surface:

python examples/rebuild_and_analyze_all.py

Inspect the core public case files directly:

examples/omnia_inevitability_case_v0/baseline_results.jsonl
examples/omnia_inevitability_case_v0/omnia_scores.jsonl
examples/omnia_inevitability_case_v0/gate_actions.jsonl
examples/omnia_inevitability_case_v0/final_results.jsonl
examples/omnia_inevitability_case_v0/metrics.md


---

Repository rule after this point

This file defines the primary external-facing case.

From this point forward, OMNIA should not present all mini-results equally in public-facing contexts.

The first default external reference should be:

OMNIA Inevitability Case v0

Other result layers remain useful inside the repository, but this one is the main public entry point.


---

Final rule

Do not expand public-facing communication by adding more equal-priority cases.

Use one main case first.

That case is now frozen here.