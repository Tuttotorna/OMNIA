# SURFACE_OK_MINI_RESULT.md

## Status

This document records the first bounded mini-result obtained with OMNIA CORE v1 on a small `surface_ok` case set.

Its purpose is not to claim broad external validity.

Its purpose is to freeze one precise and readable divergence:

> surface acceptability does not imply structural admissibility.

---

## 1. Dataset definition

The evaluated set consists of 8 bounded cases stored in:

```text
examples/surface_ok_cases.jsonl

All cases were explicitly labeled:

surface_ok = true

This means that, by construction, every case appears acceptable at surface level.

The set is intentionally small and readable.

It is not a benchmark.

It is a bounded mini-result.


---

2. Evaluation procedure

The cases were processed through the canonical JSONL runner:

python examples/run_profiles_jsonl.py examples/surface_ok_cases.jsonl -o examples/surface_ok_results.jsonl

The resulting output was then summarized by counting gate states and listing all surface_ok cases that did not receive GO.


---

3. Result summary

Observed counts:

total_cases: 8
surface_ok_true: 8
gate_status_counts: {'GO': 3, 'RISK': 2, 'NO_GO': 2, 'UNSTABLE': 1}
non_GO_ratio: 5/8

This means:

all 8 cases were surface-acceptable

only 3 of 8 were structurally admissible as GO

5 of 8 were surface-acceptable but structurally non-GO



---

4. Non-GO surface-ok cases

The following cases were surface-acceptable but did not receive GO:

llm_reasoning_surface_ok_but_fragile

llm_confident_but_exhausted

llm_high_drift_block

llm_collapsed_profile

retrieval_answer_fragile


These cases split across:

RISK

NO_GO

UNSTABLE


This is the first readable divergence surface.


---

5. Minimal interpretation

The minimal interpretation is:

> not every surface-ok output is structurally admissible.



Or equivalently:

> surface readability and structural admissibility are not identical.



This is the only intended claim of this mini-result.


---

6. What this result does prove

This mini-result proves that, on this bounded case set:

OMNIA does not collapse all surface-ok cases into GO

OMNIA distinguishes between surface acceptability and structural admissibility

the canonical gate can separate bounded cases into GO, RISK, NO_GO, and UNSTABLE


This confirms that the gate is not merely echoing the surface label.


---

7. What this result does not prove

This mini-result does not prove:

broad real-world generalization

superiority over external baselines

production value

semantic correctness

task-level correctness

broad safety claims


It is a bounded mini-result only.


---

8. Why this result matters

This result is the first small external-facing fracture in the project.

Before this point, the core was:

documented

runnable

testable

internally coherent


After this point, the core also has one small demonstrable divergence:

surface_ok != always_GO

That is the first legible external signal.


---

9. Canonical one-line formula

The shortest correct formula for this result is:

In a bounded 8-case surface-ok set, OMNIA assigned only 3/8 cases to GO and flagged 5/8 as structurally non-GO.


---

10. Final status

This result does not complete validation.

But it does end the phase in which OMNIA had only internal architecture and no readable external-facing divergence at all.

