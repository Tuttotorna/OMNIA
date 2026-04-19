# OMNIA - Gate Mapping Specification

## Purpose

This document defines the frozen operational mapping from OMNIA gate outputs to external validation actions.

Its purpose is to remove ambiguity from the combined condition:

```text
baseline + OMNIA

Without a frozen mapping, OMNIA gate outputs cannot be compared fairly against the baseline.


---

Validation role

OMNIA produces bounded gate outputs:

GO

RISK

NO_GO

UNSTABLE


The external validation, however, requires operational outcomes:

PASS

REVIEW

BLOCK


This document freezes the mapping between the two layers.


---

Canonical mapping

For the first external validation pass, the canonical mapping is:

GO -> PASS
RISK -> REVIEW
NO_GO -> BLOCK
UNSTABLE -> BLOCK

This is the default frozen mapping for version 1.


---

Meaning of each mapping

GO -> PASS

A structurally admissible case is allowed to pass forward.

RISK -> REVIEW

A structurally fragile or elevated-drift case is not auto-blocked, but must not be treated as clean pass-through. It is routed to review.

NO_GO -> BLOCK

A structurally non-admissible case is blocked.

UNSTABLE -> BLOCK

A structurally degraded or collapsed case is blocked.


---

Design principle

This mapping is intentionally conservative but not maximal.

It does not treat RISK as automatic block.

That choice is deliberate.

The first external validation is not meant to prove that OMNIA can block everything suspicious. It is meant to test whether OMNIA can reduce false accepts without making the system operationally useless.

Mapping RISK to REVIEW preserves that distinction.


---

Combined evaluation logic

Under the combined condition:

baseline + OMNIA

the final action is determined as follows:

1. baseline produces PASS, REVIEW, or BLOCK


2. OMNIA produces GO, RISK, NO_GO, or UNSTABLE


3. OMNIA gate output is converted using the frozen gate mapping


4. final operational outcome is the stricter of the two outcomes



Operational severity order:

PASS < REVIEW < BLOCK

Examples:

baseline = PASS, OMNIA = GO -> final = PASS

baseline = PASS, OMNIA = RISK -> final = REVIEW

baseline = PASS, OMNIA = NO_GO -> final = BLOCK

baseline = REVIEW, OMNIA = GO -> final = REVIEW

baseline = BLOCK, OMNIA = GO -> final = BLOCK


This ensures OMNIA does not weaken the baseline. It can only preserve or tighten the decision surface.


---

Why this mapping is acceptable

This mapping is acceptable because it is:

explicit

bounded

reproducible

operationally legible

aligned with OMNIA's non-decision role


It does not turn OMNIA into an autonomous decision-maker. It defines only how OMNIA's bounded outputs affect an external bounded screening workflow.


---

What this mapping does not claim

This mapping does not claim:

universal correctness

optimal operational policy

production-ready escalation logic

semantic adjudication

safety certification


It is only the frozen mapping for the first OMNIA external validation pass.


---

Freeze rule

Once evaluation begins:

the gate mapping may not change

the severity order may not change

the final-action combination rule may not change


If any of these change, a new mapping version must be declared.

No silent mutation is allowed.


---

Versioning rule

The mapping must be versioned.

Example:

omnia_gate_mapping_v1

If the mapping changes materially, the version must change.


---

Minimal mapping summary

OMNIA outputs: GO / RISK / NO_GO / UNSTABLE
Operational outputs: PASS / REVIEW / BLOCK

Frozen mapping:
GO -> PASS
RISK -> REVIEW
NO_GO -> BLOCK
UNSTABLE -> BLOCK

Final combined outcome:
take the stricter result between baseline and mapped OMNIA output


---

Canonical mapping sentence

For the first OMNIA external validation pass, OMNIA gate outputs are frozen into a conservative operational mapping where GO passes, RISK triggers review, and NO_GO or UNSTABLE block.