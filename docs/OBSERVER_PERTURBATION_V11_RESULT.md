# Observer Perturbation Signal Test V11 (Realistic LLM-like Outputs)

## Purpose

V11 evaluates the behavior of ObserverPerturbation on more realistic, LLM-like outputs.

Unlike previous versions, this dataset is less synthetic and closer to actual model responses.

The goal is to compare:

- raw OPI
- corrected OPI

under realistic conditions.

---

## Runner

```text
examples/observer_perturbation_signal_test_v11_llm_outputs.py


---

Result files

results/observer_perturbation_v11_raw_ranked.json
results/observer_perturbation_v11_corrected_ranked.json
results/observer_perturbation_v11_summary.json


---

Dataset

10 stable outputs
10 contradictory / inconsistent outputs

Characteristics:

natural phrasing

no keyword tricks

mixed domains (math, QA, factual, instructions)



---

Summary Results

RAW:

top3:
  precision: 0.667
  recall:    0.2

top5:
  precision: 0.4
  recall:    0.2

top10:
  precision: 0.5
  recall:    0.5


CORRECTED:

top3:
  precision: 1.0
  recall:    0.3

top5:
  precision: 0.8
  recall:    0.4

top10:
  precision: 0.6
  recall:    0.6


---

Key Observation

Corrected signal improves ranking quality:

precision@5:
  raw       = 0.4
  corrected = 0.8

This confirms that V10 improvements generalize beyond synthetic data.


---

Failure Mode (Raw OPI)

Raw OPI still ranks simple, rigid statements too high:

"2 + 2 equals 4."
"The result is 42."

These are:

short

single-sentence

structurally rigid


Result:

false positives in top-k


---

Correction Effect

The correction layer:

penalizes short / single-sentence outputs

This shifts ranking toward:

multi-part inconsistent structures

Example:

"The result is 42. The result is 41."
"The answer is 17. The answer is 18."


---

Interpretation

V11 confirms:

raw OPI → noisy
corrected OPI → useful ranking signal


---

Practical Use

Corrected OPI can be used as:

high-precision triage mechanism

Workflow:

rank outputs
inspect top-k
ignore low-score region


---

Limitations

Still not:

full contradiction detector
complete recall system
semantic truth verifier


---

Correct Claim

The correct claim from V11:

> A simple structural correction applied to ObserverPerturbation significantly improves top-k prioritization on realistic LLM-like outputs compared to raw OPI.




---

Status

V8  → ranking useful (synthetic)
V10 → false positives reduced
V11 → improvement holds on realistic outputs


---

Boundary

measurement != inference != decision

