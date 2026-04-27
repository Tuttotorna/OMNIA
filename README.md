# OMNIA — Structural Measurement Core

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19739481.svg)](https://doi.org/10.5281/zenodo.19739481)

**Author:** Massimiliano Brighindi  
**Contact:** brighissimo@gmail.com

---

## What OMNIA is

OMNIA is a structural measurement core.

It does not judge meaning.  
It does not replace reasoning.  
It does not declare truth.

OMNIA measures whether an output remains structurally admissible under controlled transformations, constraints, or observer perturbations.

In one sentence:

> OMNIA measures how much structure survives when form, constraints, or nearby representation changes.

---

## Core Boundary

```text
structural validity != semantic correctness

OMNIA measures structural validity.

It does not measure semantic truth.

This boundary is intentional.

OMNIA is not:

a truth oracle

a semantic evaluator

a final decision system

a contradiction detector by itself



---

Non-Negotiable Rule

measurement != inference != decision

OMNIA stays inside the measurement layer.

That is what keeps it clean.


---

What OMNIA detects

OMNIA is strongest when failures are structural:

incomplete outputs

malformed answers

format violations

expression instead of final answer

unstable output under variation

structurally hollow responses

mismatch between requested output contract and produced output

instability under observer perturbation

atomic collapse

short malformed output

long incoherent drift


Examples:

"5 * 3 ="          -> incomplete
"5 * 3 = 15"      -> not final-only
"blue"            -> incomplete if expected contract is "blue key"
long explanation  -> invalid if scalar answer required
"LDL"             -> atomic malformed output


---

What OMNIA does not detect

OMNIA does not detect pure semantic errors when the answer is structurally well-formed.

Examples:

"2" instead of "4"
"wolf" instead of "dog"
"blue" instead of "black"

These answers may be wrong, but structurally valid.

OMNIA may return:

GO

This is not a bug.

It is the boundary of the system.


---

Correct System Role

The correct pipeline is:

LLM -> OMNIA -> Semantic Evaluator -> Decision

OMNIA removes structurally invalid, unstable, incomplete, collapsed, or malformed outputs before semantic evaluation or operational decision.


---

Minimal External Signal

OMNIA includes a minimal reproducible signal test for observer-induced structural instability.

Runner:

examples/observer_perturbation_signal_test.py

Document:

docs/OBSERVER_PERTURBATION_RESULT.md

Result summary:

Stable avg OPI:      ~0.0016
Unstable avg OPI:    ~0.0062

Stable avg ratio:    ~0.089
Unstable avg ratio:  ~0.284

Interpretation:

> Internally unstable outputs change more under observer perturbation than stable outputs.



This is not a universal proof.

It is a minimal reproducible signal showing that a real OMNIA lens can separate stable from unstable structures under controlled conditions.


---

Observer Perturbation — Validation Path

This section summarizes the empirical validation path of the ObserverPerturbation signal.

The goal is not to claim universal correctness.

The goal is to show:

where the signal fails

why it fails

how it can be improved

whether the improvement generalizes



---

V6 — Failure on Realistic Classification

V6 tested raw ObserverPerturbation on realistic labeled outputs.

Result:

OMNIA:
  TP: 4
  FP: 5
  TN: 5
  FN: 6

Baseline:
  TP: 9
  FP: 1
  TN: 9
  FN: 1

Conclusion:

raw OPI is not a reliable classifier

The simple baseline outperformed OMNIA.

This failure is important because it defines the limit of the raw signal.

Files:

examples/observer_perturbation_signal_test_v6_real_labeled.py
results/observer_perturbation_v6_summary.json


---

V7 — Keyword-Free Signal

V7 removed obvious lexical cues.

Result:

OMNIA:
  TP: 5
  FP: 5
  TN: 5
  FN: 5

Baseline:
  TP: 0
  FP: 0
  TN: 10
  FN: 10

Conclusion:

baseline collapses
OMNIA retains partial signal

This shows that ObserverPerturbation is not reducible to simple keyword detection.

Files:

examples/observer_perturbation_signal_test_v7_keyword_free.py
results/observer_perturbation_v7_summary.json
docs/OBSERVER_PERTURBATION_V7_RESULT.md


---

V8 — Ranking Signal

V8 tested whether OPI works better as a ranking mechanism than as a binary classifier.

Result:

precision@3  = 0.6667
precision@5  = 0.8
precision@10 = 0.5

Mean separation failed:

stable_mean_opi        = 0.017268491609918033
contradictory_mean_opi = 0.015723120024641747

Conclusion:

classification -> weak
ranking        -> useful

Files:

examples/observer_perturbation_signal_test_v8_ranking.py
results/observer_perturbation_v8_summary.json
results/observer_perturbation_v8_ranked.json
docs/OBSERVER_PERTURBATION_V8_RESULT.md


---

V9 — False Positive Analysis

V9 analyzed why stable cases ranked too high.

Key discovery:

short, rigid structures can produce high raw OPI

Example false positive:

"2 + 2 equals 4."

Conclusion:

OPI can confuse structural rigidity with contradiction-like instability

This explains the V8 false positives.

Files:

examples/observer_perturbation_signal_test_v9_false_positive_analysis.py
results/observer_perturbation_v9_ranked.json
results/observer_perturbation_v9_analysis.json


---

V10 — Corrected Signal

V10 introduced a simple correction:

corrected_opi = raw_opi × length_factor × structure_factor × duplication_factor

Purpose:

penalize short outputs

penalize single-sentence outputs

reduce rigid false positives


Result:

top3:
  precision: 1.0
  recall:    0.3

top5:
  precision: 1.0
  recall:    0.5

top10:
  precision: 0.6
  recall:    0.6

Comparison:

V8 precision@5  = 0.8
V10 precision@5 = 1.0

Conclusion:

false positives significantly reduced
ranking quality improved

Files:

examples/observer_perturbation_signal_test_v10_corrected.py
results/observer_perturbation_v10_summary.json
results/observer_perturbation_v10_ranked.json
docs/OBSERVER_PERTURBATION_V10_RESULT.md


---

V11 — Realistic LLM-like Outputs

V11 tested whether the correction generalizes beyond the synthetic V7/V8 setup.

Result:

RAW:

top3:
  precision: 0.6667
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

Key result:

RAW precision@5       = 0.4
CORRECTED precision@5 = 0.8

Conclusion:

corrected OPI improves top-k prioritization on realistic LLM-like outputs

Files:

examples/observer_perturbation_signal_test_v11_llm_outputs.py
results/observer_perturbation_v11_raw_ranked.json
results/observer_perturbation_v11_corrected_ranked.json
results/observer_perturbation_v11_summary.json
docs/OBSERVER_PERTURBATION_V11_RESULT.md


---

V14 — Real Local-Model Outputs

V14 applied OMNIA to real outputs generated by a local model.

Dataset:

data/real_llm_outputs_v14_local_flan_t5_small.jsonl

Runner:

examples/observer_perturbation_real_outputs_v14.py

Result:

corrected_opi surfaces several structurally degraded generations
in the top-ranked subset

Boundary:

does not capture all malformed outputs

Conclusion:

corrected_opi is useful as a degradation triage signal,
not as a complete detector

Document:

docs/OBSERVER_PERTURBATION_V14_REAL_OUTPUTS_RESULT.md


---

V18 — Tri-Channel Structural Diagnostic

V18 is the key conceptual result.

A single suspicion score was not sufficient.

Structural failure separated into three regimes:

1. atomic malformed
2. short malformed
3. long incoherent

Files:

examples/observer_perturbation_real_outputs_v18_tri_channel.py
results/observer_perturbation_v18_tri_channel_summary.json
docs/OBSERVER_PERTURBATION_V18_TRI_CHANNEL_RESULT.md
docs/OMNIA_V18_FINAL_POSITION.md

Conclusion:

structural failure is not one-dimensional

Correct claim:

> OMNIA can decompose structural failure into distinct regimes. Mapping these regimes into a stable decision gate requires larger-scale calibration and cannot be reliably achieved by small manual threshold tuning alone.




---

Tri-Channel Dataset Validation

OMNIA includes a synthetic structural dataset to validate the tri-channel decomposition.

Generator:

examples/generate_structural_dataset_v1.py

Dataset:

data/structural_dataset_v1.jsonl

Evaluator:

examples/evaluate_tri_channel_dataset_v1.py

Result:

total = 300

atomic -> { atomic: 74, short: 0,  long: 0 }
short  -> { atomic: 30, short: 41, long: 0 }
long   -> { atomic: 0,  short: 12, long: 61 }
good   -> { atomic: 0,  short: 82, long: 0 }

structural accuracy excluding good:
176 / 218 = 0.8073

Interpretation:

atomic detection -> very strong
long detection   -> strong
short regime     -> ambiguous

Document:

docs/TRI_CHANNEL_DATASET_V1_RESULT.md


---

Tri-Channel Classifier V1

A simple learned classifier was trained on the structural dataset.

Trainer:

examples/train_tri_channel_classifier_v1.py

Result:

precision = 1.00
recall    = 1.00
f1-score  = 1.00
accuracy  = 1.00

Feature importance:

length           -> 0.4573
digit_density    -> 0.2724
symbol_density   -> 0.2452
malformed        -> 0.0251

Correct claim:

On a controlled synthetic structural dataset,
tri-channel regimes are perfectly separable using simple structural features.

Boundary:

synthetic success is not proof of real-world performance

Document:

docs/TRI_CHANNEL_CLASSIFIER_V1_RESULT.md


---

Real Output Structural Analysis

OMNIA was tested on real outputs generated by a local model.

Collector:

examples/collect_real_outputs_v1.py

Dataset:

data/real_structural_dataset_v1.jsonl

Evaluator:

examples/evaluate_real_outputs_v1.py

Result:

total  = 60
atomic = 9  (15%)
short  = 9  (15%)
long   = 42 (70%)

Interpretation:

flan-t5-small produces mostly long incoherent structural drift

Document:

docs/REAL_STRUCTURAL_ANALYSIS_V1.md


---

Structural Gate

OMNIA now includes a minimal structural intervention layer.

This is the transition from:

structural observation -> structural intervention

Gate outputs:

PASS
REVIEW
REJECT

These are not final truth decisions.

They are structural routing states.


---

Structural Gate V1 — Rule-Based

Runner:

examples/omnia_structural_gate_v1.py

Result:

total = 60

PASS   = 24 (40.0%)
REVIEW = 28 (46.7%)
REJECT = 8  (13.3%)

Interpretation:

the gate does not pass everything
the gate does not reject everything
the gate routes almost half of real outputs to REVIEW
atomic collapse is rejected
long drift is partially captured

Document:

docs/OMNIA_STRUCTURAL_GATE_V1_RESULT.md


---

Structural Gate V2 — Learned Gate

V2 trains a learned classifier to replicate and smooth the V1 gate behavior.

Trainer:

examples/train_structural_gate_v2.py

Runner:

examples/use_structural_gate_v2.py

Report:

results/structural_gate_v2_report.json
results/omnia_structural_gate_v2.json

Result:

V1:
PASS   = 24
REVIEW = 27
REJECT = 9

V2:
PASS   = 25
REVIEW = 26
REJECT = 9

Delta:
PASS   +1
REVIEW -1
REJECT  0

Training report:

accuracy = 0.94

Correct interpretation:

V2 learns the V1 structural gate behavior with high fidelity
and slightly smooths the decision boundary

Boundary:

V2 is not yet an independently discovered decision system.
It is a learned approximation of the V1 rule-based structural gate.

Do not commit the generated binary model unless needed:

models/structural_gate_v2.pkl

It can be regenerated by running:

python examples/train_structural_gate_v2.py


---

Current Empirical Status

OMNIA has been tested across several controlled validation stages.

Structural Gate V7

Initial gate on controlled QA, reasoning, and RAG cases.

Result:

TP: 10
FN: 0
FP: 0
TN: 6

V7 performed well on the initial small dataset.


---

Harder Dataset

A harder dataset exposed a failure:

V7 recall collapsed to 0.25

This showed that the early gate was too shallow.


---

Structural Gate V8

V8 added structural mismatch detection.

Result on harder data:

TP: 11
FN: 1
FP: 0
TN: 8
Recall:    0.917
Precision: 1.000


---

Structural Completeness V9

V9 added structural completeness detection:

final-answer enforcement

expression detection

answer completeness / granularity check


Result:

TP: 12
FN: 0
FP: 0
TN: 8
Recall:    1.000
Precision: 1.000

This closed the observed V8 failure modes.


---

External Attack Slice

A separate synthetic attack set tested whether V9 generalized beyond the previous dataset.

Result:

TP: 9
FN: 0
FP: 0
TN: 11
Recall:    1.000
Precision: 1.000

This is evidence of cross-pattern robustness, not universal validity.


---

GSM8K-style / GSM8K Real Slices

OMNIA was also tested on arithmetic reasoning slices.

On GSM8K-style and real GSM8K slices, V9 correctly rejected structurally invalid or wrong numeric outputs.

However, some runs were highly imbalanced because the tested model produced very few correct answers.

Therefore these runs show failure detection capability, but are not sufficient as full positive-selectivity proof.


---

Scope Boundary

Read:

docs/OMNIA_SCOPE_BOUNDARY_V1.md

Core conclusion:

> OMNIA is not a universal error detector.
OMNIA is a structural filter layer.




---

Where OMNIA is useful

OMNIA is useful when systems require:

structured outputs

final-only answers

JSON or schema compliance

stable behavior under variation

post-hoc output review

pre-deployment structural gates

detection of hollow or malformed responses

observer-perturbation analysis

top-k triage of structurally suspicious outputs

structural routing: PASS / REVIEW / REJECT


OMNIA is especially relevant where an answer may look acceptable but fail structurally.


---

Where OMNIA is not sufficient

OMNIA is not sufficient for:

pure QA correctness

truth verification

semantic reasoning validation

factuality checking

final operational decisions

production contradiction detection by itself


These require a semantic evaluator, another model, ground truth, or human review.


---

Canonical Outputs

OMNIA produces bounded structural diagnostics such as:

omega_score
sei_score
iri_score
drift_score
limit_triggered
gate_status
reason_code
opi
corrected_opi
atomic_score
short_score
long_score

Typical gate values:

GO
RISK
NO_GO
UNSTABLE
PASS
REVIEW
REJECT

These are measurement or routing outputs.

They are not final truth decisions.


---

Minimal Example Output

{
  "omega_score": 0.594462,
  "sei_score": 0.67557,
  "iri_score": 0.405538,
  "drift_score": 0.405538,
  "limit_triggered": false,
  "gate_status": "RISK",
  "reason_code": "low_omega"
}

Interpretation:

> The output is readable, but structurally weak enough to justify review.




---

Repository Structure

omnia/      -> structural measurement logic
examples/   -> validation datasets and runners
data/       -> frozen datasets
results/    -> frozen experimental outputs
docs/       -> reports, scope, validation notes
tests/      -> core behavior tests


---

Key Documents

docs/OMNIA_SCOPE_BOUNDARY_V1.md
docs/OBSERVER_PERTURBATION_RESULT.md
docs/OBSERVER_PERTURBATION_V7_RESULT.md
docs/OBSERVER_PERTURBATION_V8_RESULT.md
docs/OBSERVER_PERTURBATION_V10_RESULT.md
docs/OBSERVER_PERTURBATION_V11_RESULT.md
docs/OBSERVER_PERTURBATION_V14_REAL_OUTPUTS_RESULT.md
docs/OBSERVER_PERTURBATION_V18_TRI_CHANNEL_RESULT.md
docs/OMNIA_V18_FINAL_POSITION.md
docs/TRI_CHANNEL_DATASET_V1_RESULT.md
docs/TRI_CHANNEL_CLASSIFIER_V1_RESULT.md
docs/REAL_STRUCTURAL_ANALYSIS_V1.md
docs/OMNIA_STRUCTURAL_GATE_V1_RESULT.md
docs/REAL_VALIDATION_V9_STRUCTURAL_COMPLETENESS.md
docs/REAL_VALIDATION_V9_EXTERNAL_ATTACK.md
docs/REAL_VALIDATION_V9_GSM8K_SLICE.md
docs/REAL_VALIDATION_V9_GSM8K_REAL.md
docs/OMNIA_V8_FAILURE_ANALYSIS.md
docs/FOCUSED_PROOF.md


---

Installation

From repository root:

pip install -e . -U --no-cache-dir


---

Smoke Test

python examples/quick_omnia_test.py

Expected ending:

OK: OMNIA core executed


---

Observer Perturbation Tests

Minimal signal:

python examples/observer_perturbation_signal_test.py

Corrected realistic test:

python examples/observer_perturbation_signal_test_v11_llm_outputs.py

Expected V11 direction:

corrected precision@5 > raw precision@5

Observed:

RAW precision@5       = 0.4
CORRECTED precision@5 = 0.8


---

Tri-Channel / Gate Tests

Generate synthetic structural dataset:

python examples/generate_structural_dataset_v1.py

Evaluate tri-channel dataset:

python examples/evaluate_tri_channel_dataset_v1.py

Train tri-channel classifier:

python examples/train_tri_channel_classifier_v1.py

Collect real local-model outputs:

python examples/collect_real_outputs_v1.py

Evaluate real outputs:

python examples/evaluate_real_outputs_v1.py

Run rule-based structural gate:

python examples/omnia_structural_gate_v1.py

Train learned structural gate:

python examples/train_structural_gate_v2.py

Run learned structural gate:

python examples/use_structural_gate_v2.py


---

Tests

pytest -q tests

Recent verified run:

47 passed

This proves software consistency only.

It is not external scientific validation by itself.


---

Reproducibility Rule

An OMNIA claim is valid only if it includes:

frozen dataset

frozen runner

frozen result file

explicit metric interpretation

clear scope boundary


Without reproducibility, the claim is not evidence.


---

Current Public Claim

The correct public claim is narrow:

> OMNIA is a bounded structural measurement core. It detects structural invalidity, incompleteness, drift, malformed outputs, observer-perturbation instability, and structural failure regimes. It does not detect semantic truth. Current results show strong behavior on controlled structural validation tasks, while pure semantic QA remains outside its standalone scope. ObserverPerturbation is best treated as a triage/ranking signal, not a final contradiction detector. The structural gate is an intervention layer for routing outputs to PASS / REVIEW / REJECT, not a final decision system.




---

One-Line Definition

OMNIA measures how much structure survives when form, constraints, or observer framing changes.


---

Final Boundary

OMNIA is strongest when it stays inside its real role:

structural measurement only

No hidden semantics.
No truth oracle.
No decision theater.
No claims beyond evidence.


---

License

MIT License