# OMNIA — Minimal Comparative Benchmark

## Goal

Provide a minimal, reproducible comparison between:

- No structural gate (baseline)
- OMNIA Structural Gate V1
- OMNIA Structural Gate V2 (learned)

This is not a leaderboard.

It is a stability comparison under identical data.

---

## Dataset

Same dataset used across all runs:

```text
data/real_structural_dataset_v1.jsonl
(total = 60)

Includes:

QA prompts

arithmetic tasks

code tasks

definition tasks

malformed and noisy outputs



---

Systems Compared

1. Baseline (no gate)

Assumption:

All outputs are valid unless semantically wrong.

No structural filtering applied.


---

2. OMNIA V1 (rule-based gate)

Outputs classified into:

PASS / REVIEW / REJECT

Based on structural signals:

length

digit density

symbol density

malformed score

structural drift heuristics



---

3. OMNIA V2 (learned gate)

Model trained to approximate V1 decisions.

Same input features.

Learns boundary instead of encoding rules.


---

Results Summary

V1 Gate

PASS   = 24
REVIEW = 27
REJECT = 9


---

V2 Gate

PASS   = 25
REVIEW = 26
REJECT = 9

Delta:

PASS   +1
REVIEW -1
REJECT  0


---

Key Comparison Insight

Stability of distribution

Both V1 and V2 converge to nearly identical distributions.

This indicates:

structural boundary is learnable

decision surface is not arbitrary

signal is stable under feature representation



---

Important Control Observation

Baseline (no gate) behavior:

no structural separation

all outputs treated as equivalent candidates


Result:

no routing layer → no structural discrimination


---

Interpretation

OMNIA does not improve correctness.

It introduces structure-aware routing.


---

What this benchmark shows

Confirmed

structural features contain separable signal

rule-based and learned gates converge

instability is not random noise



---

Not confirmed

semantic correctness improvement

general reasoning improvement

truth detection capability



---

Structural Hypothesis (limited)

Given identical inputs:

> Outputs can be partitioned into structurally distinct regimes that are stable under both rule-based and learned classification.




---

Minimal Conclusion

OMNIA is not a model improvement layer.

It is a structural partitioning layer over model outputs.


---

Next extension (optional future work)

compare against other LLM guardrails

add adversarial perturbation benchmark

measure cross-model stability consistency


---

## Perché questo è il passo giusto

Perché adesso hai:

- DOI reale
- dataset reale
- gate V1/V2
- observer perturbation signal

