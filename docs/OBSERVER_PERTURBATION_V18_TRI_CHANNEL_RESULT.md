# OMNIA — V18 Tri-Channel Structural Triage

## Purpose

V18 introduces a structural triage model that separates failure modes into **independent channels** instead of relying on a single global score.

Goal:

> determine whether structural failures are better captured by decomposition rather than aggregation.

---

## Core Idea

A single suspicion score mixes fundamentally different phenomena.

V18 splits structural degradation into three disjoint categories:

```text
1. atomic malformed
2. short malformed
3. long incoherent

Each channel captures a different structural failure regime.


---

Channels

1. Atomic Malformed

Definition:

empty outputs

near-empty outputs

single-token or minimal-token degeneration


Examples:

VEPSEINET
leukdd1g9Aef
inorganization

Interpretation:

> structure collapses at the token level.




---

2. Short Malformed

Definition:

short outputs (2–8 tokens)

partially structured but broken

symbolic or numeric inconsistencies


Examples:

6 * 16 * 11* 9) *
15 numbers! (Courp 0!
1532” cut. S

Interpretation:

> structure exists but is locally corrupted.




---

3. Long Incoherent

Definition:

longer outputs

multiple sentences or extended sequences

global inconsistency or semantic drift


Examples:

numeric sequences without coherence
multi-sentence contradictory fragments
pseudo-reasoning chains

Interpretation:

> structure exists but collapses across span.




---

Key Result

V18 shows that:

different structural failures occupy different regions
and cannot be reliably captured by a single scalar score


---

Comparison with Previous Versions

V14 / V15

single corrected_opi score

dominated by short malformed outputs

poor sensitivity to long incoherence


V16 / V17

introduced multiple channels

but had overlap and classification ambiguity


V18

disjoint channel assignment

clean separation of regimes

interpretable output



---

Interpretation

Correct interpretation:

> OMNIA should not output a single "suspicion score".



Instead:

> OMNIA should output a multi-channel structural diagnostic.




---

Valid Claim

> Structural degradation in LLM outputs is not a single phenomenon.
It decomposes into distinct regimes that require separate measurement channels.




---

Non-Claims

OMNIA does NOT:

detect semantic truth

guarantee completeness of detection

replace evaluation pipelines

act as a final decision system



---

Value

V18 provides:

clearer interpretability

separation of failure modes

improved diagnostic utility

a path toward structured output triage systems



---

Conclusion

V18 is the first version where:

structure failure ≠ single scalar
structure failure = multi-channel space

This is a conceptual shift, not just an incremental improvement.


---

Next Direction

Possible extensions:

calibration between channels

cross-channel interaction signals

integration into gating systems

real-world pipeline testing


