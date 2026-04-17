# LLM_SURFACE_MINI_RESULT.md

## Status

This document records the second bounded mini-result obtained with OMNIA CORE v1 on a small set of LLM-like surface-readable outputs.

Its purpose is not to claim broad external validity.

Its purpose is to freeze one precise and readable divergence:

> an output can look acceptable to a human reader while remaining structurally non-admissible under the OMNIA gate.

---

## 1. Dataset definition

The evaluated set consists of 8 bounded cases stored in:

```text
examples/llm_surface_cases.jsonl

Each case contains:

case_id

task

output_text

surface_ok

surface_note

omega_score

sei_score

iri_score

drift_score


All cases were explicitly labeled:

surface_ok = true

This means every case was designed to remain readable and superficially acceptable at surface level.

The set is intentionally small and readable.

It is not a benchmark.

It is a bounded mini-result.


---

2. Evaluation procedure

The cases were processed through the canonical JSONL runner:

python examples/run_profiles_jsonl.py examples/llm_surface_cases.jsonl -o examples/llm_surface_results.jsonl

The resulting output was then summarized by counting gate states and listing all surface_ok cases that did not receive GO.


---

3. Expected result summary

Given the current canonical threshold policy and the defined case set, the expected counts are:

total_cases: 8
surface_ok_true: 8
gate_status_counts: {'GO': 3, 'RISK': 2, 'NO_GO': 2, 'UNSTABLE': 1}
non_GO_ratio: 5/8

This means:

all 8 cases are surface-readable and surface-acceptable

only 3 of 8 are structurally admissible as GO

5 of 8 are surface-readable but structurally non-GO



---

4. Expected non-GO surface-ok cases

The following cases are expected to be surface-acceptable but not GO:

gsm8k_confident_but_brittle

retrieval_plausible_but_exhausted

reasoning_shift_under_variants

collapsed_but_readable

support_answer_fragile


These cases are expected to split across:

RISK

NO_GO

UNSTABLE


This is the second readable divergence surface of the project.


---

5. Minimal interpretation

The minimal interpretation is:

> not every surface-readable LLM-like output is structurally admissible.



Or, more explicitly:

> human-readable plausibility and structural admissibility are not identical.



This is the only intended claim of this mini-result.


---

6. What this result proves

This mini-result proves that, on this bounded LLM-like case set:

OMNIA does not collapse all surface-ok outputs into GO

OMNIA distinguishes between readability at surface level and structural admissibility

the canonical gate can separate LLM-like cases into:

GO

RISK

NO_GO

UNSTABLE



This confirms that the gate is not merely echoing the surface label or the readability of the output text.


---

7. What this result does not prove

This mini-result does not prove:

broad LLM evaluation superiority

production deployment value

broad real-world generalization

semantic correctness

reasoning correctness

truth in the universal sense

model safety in the general sense


It is a bounded mini-result only.


---

8. Why this result matters

This result is stronger than the previous surface_ok mini-result because the cases are no longer pure score-only labels.

Each record now contains:

a task type

a readable output text

a surface note

a structural profile


This makes the divergence easier to explain:

readable output != guaranteed GO

That is a more legible external signal than a pure abstract score profile.


---

9. Canonical one-line formula

The shortest correct formula for this result is:

In a bounded 8-case LLM-like surface-readable set, OMNIA assigned only 3/8 cases to GO and flagged 5/8 as structurally non-GO.


---

10. Relationship to the previous mini-result

The previous bounded result established:

surface_ok != always_GO

This second result refines that into a more LLM-facing form:

surface-readable LLM-like output != always structurally admissible

So the trajectory is now:

1. internal runnable core


2. abstract surface-ok divergence


3. LLM-like surface-readable divergence



This is the correct order of externalization.


---

11. Final status

This result does not complete validation.

But it extends the proof surface beyond abstract score-only cases and shows that the OMNIA gate can produce readable divergence even when the output text itself looks acceptable to a human reader.

