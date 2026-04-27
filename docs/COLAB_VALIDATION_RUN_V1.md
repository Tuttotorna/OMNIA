# Colab Validation Run V1

## Purpose

This document records a reproducible Google Colab validation run for OMNIA.

The goal is to verify that the repository can be cloned, installed, tested, and executed end-to-end in a clean Colab environment.

This is not a universal scientific proof.

It is a reproducibility check.

---

## Repository

```text
https://github.com/Tuttotorna/OMNIA.git

Branch:

main


---

Environment

Execution environment:

Google Colab
Python 3.12
Editable install

Install command:

pip install -e . -U --no-cache-dir

Test command:

pytest -q tests


---

Validation Steps

The Colab run executed the following steps:

1. Clone repository
2. Install OMNIA in editable mode
3. Install pytest
4. Verify import from repository root
5. Run pytest
6. Run quick smoke test
7. Run Observer Perturbation V11
8. Generate synthetic structural dataset
9. Evaluate tri-channel dataset
10. Collect real local-model outputs
11. Evaluate real structural outputs
12. Run Structural Gate V1
13. Train Structural Gate V2
14. Run Structural Gate V2


---

Core Software Check

Command:

pytest -q tests

Result:

47 passed in 0.18s

Interpretation:

Core software tests pass.

Boundary:

This proves software consistency only.
It is not external scientific validation by itself.


---

Smoke Test

Command:

python examples/quick_omnia_test.py

Result:

{
  "case_id": "quick-smoke-001",
  "drift_score": 0.405538,
  "gate_status": "RISK",
  "iri_score": 0.405538,
  "limit_triggered": false,
  "omega_score": 0.594462,
  "reason_code": "high_drift",
  "sei_score": 0.67557
}

Expected ending:

OK: OMNIA core executed

Observed:

OK: OMNIA core executed

Interpretation:

The OMNIA core executes successfully in Colab.


---

Observer Perturbation V11

Command:

python examples/observer_perturbation_signal_test_v11_llm_outputs.py

Result:

{
  "raw": {
    "top3": {
      "tp": 2,
      "precision": 0.6666666666666666,
      "recall": 0.2
    },
    "top5": {
      "tp": 2,
      "precision": 0.4,
      "recall": 0.2
    },
    "top10": {
      "tp": 5,
      "precision": 0.5,
      "recall": 0.5
    }
  },
  "corrected": {
    "top3": {
      "tp": 3,
      "precision": 1.0,
      "recall": 0.3
    },
    "top5": {
      "tp": 4,
      "precision": 0.8,
      "recall": 0.4
    },
    "top10": {
      "tp": 6,
      "precision": 0.6,
      "recall": 0.6
    }
  }
}

Key comparison:

RAW precision@5       = 0.4
CORRECTED precision@5 = 0.8

Interpretation:

The corrected ObserverPerturbation score improves top-k prioritization over raw OPI on the V11 realistic LLM-like output slice.

Boundary:

This supports corrected OPI as a triage/ranking signal.
It does not prove universal contradiction detection.


---

Synthetic Structural Dataset Generation

Command:

python examples/generate_structural_dataset_v1.py

Result:

Saved: data/structural_dataset_v1.jsonl
Total: 300
Counts: {'good': 82, 'atomic': 74, 'long': 73, 'short': 71}

Interpretation:

The synthetic structural dataset is generated successfully.


---

Tri-Channel Dataset Evaluation

Command:

python examples/evaluate_tri_channel_dataset_v1.py

Result:

=== CONFUSION MATRIX ===
atomic -> {'atomic': 74, 'short': 0, 'long': 0}
short -> {'atomic': 30, 'short': 41, 'long': 0}
long -> {'atomic': 0, 'short': 12, 'long': 61}
good -> {'atomic': 0, 'short': 82, 'long': 0}

=== STRUCTURAL ACCURACY EXCLUDING GOOD ===
176 / 218 = 0.8073394495412844

Saved: results/tri_channel_dataset_v1_summary.json

Interpretation:

The tri-channel diagnostic separates atomic, short, and long structural failure regimes with 0.8073 structural accuracy when excluding good cases.

Observed pattern:

atomic detection -> strong
long detection   -> strong
short regime     -> ambiguous

Boundary:

The short regime remains less cleanly separable than atomic and long regimes.


---

Real Local-Model Output Collection

Command:

python examples/collect_real_outputs_v1.py

Result:

Saved: data/real_structural_dataset_v1.jsonl
Total rows: 60

Interpretation:

The repo successfully collected real local-model outputs in Colab.

Note:

The collected outputs depend on the local generation run.
Exact downstream counts may vary when this dataset is regenerated.


---

Real Structural Analysis V1

Command:

python examples/evaluate_real_outputs_v1.py

Result:

{
  "total": 60,
  "counts": {
    "atomic": 9,
    "short": 9,
    "long": 42
  },
  "ratios": {
    "atomic": 0.15,
    "short": 0.15,
    "long": 0.7
  }
}

Interpretation:

The collected local-model outputs are mostly classified as long incoherent structural drift.

Observed distribution:

atomic = 9  (15%)
short  = 9  (15%)
long   = 42 (70%)


---

Structural Gate V1

Command:

python examples/omnia_structural_gate_v1.py

Result:

{
  "total": 60,
  "gate_counts": {
    "PASS": 19,
    "REVIEW": 32,
    "REJECT": 9
  },
  "gate_ratios": {
    "PASS": 0.31666666666666665,
    "REVIEW": 0.5333333333333333,
    "REJECT": 0.15
  },
  "class_counts": {
    "atomic": 9,
    "short": 9,
    "long": 42
  },
  "class_ratios": {
    "atomic": 0.15,
    "short": 0.15,
    "long": 0.7
  }
}

Interpretation:

The structural gate does not pass everything and does not reject everything.
It routes a majority of the generated real outputs to REVIEW or REJECT.

Observed gate distribution:

PASS   = 19 (31.7%)
REVIEW = 32 (53.3%)
REJECT = 9  (15.0%)

Boundary:

These are structural routing states.
They are not final truth decisions.


---

Structural Gate V2 Training

Command:

python examples/train_structural_gate_v2.py

Result:

Model saved: models/structural_gate_v2.pkl
Report saved: results/structural_gate_v2_report.json

              precision    recall  f1-score   support

        PASS       0.83      0.83      0.83         6
      REJECT       0.75      1.00      0.86         3
      REVIEW       1.00      0.89      0.94         9

    accuracy                           0.89        18
   macro avg       0.86      0.91      0.88        18
weighted avg       0.90      0.89      0.89        18

Interpretation:

The learned gate approximates the rule-based gate behavior on this generated dataset.

Boundary:

V2 is not an independently validated decision system.
It is a learned approximation of the V1 structural gate.


---

Structural Gate V2 Execution

Command:

python examples/use_structural_gate_v2.py

Result:

{
  "total": 60,
  "counts": {
    "PASS": 19,
    "REVIEW": 31,
    "REJECT": 10
  },
  "ratios": {
    "PASS": 0.31666666666666665,
    "REVIEW": 0.5166666666666667,
    "REJECT": 0.16666666666666666
  }
}

Interpretation:

The learned gate produces a distribution close to the V1 gate.

Comparison:

V1:
PASS   = 19
REVIEW = 32
REJECT = 9

V2:
PASS   = 19
REVIEW = 31
REJECT = 10

Delta:

PASS    0
REVIEW -1
REJECT +1


---

Important Dependency Note

Some scripts require generated datasets.

The following evaluators fail if their input datasets do not exist yet:

examples/evaluate_tri_channel_dataset_v1.py
examples/omnia_structural_gate_v1.py
examples/evaluate_real_outputs_v1.py
examples/train_structural_gate_v2.py
examples/use_structural_gate_v2.py

Required generation order:

python examples/generate_structural_dataset_v1.py
python examples/evaluate_tri_channel_dataset_v1.py

python examples/collect_real_outputs_v1.py
python examples/evaluate_real_outputs_v1.py
python examples/omnia_structural_gate_v1.py
python examples/train_structural_gate_v2.py
python examples/use_structural_gate_v2.py


---

Final Colab Validation Result

The Colab validation run confirms:

clone/install/test path                 -> OK
core software tests                     -> OK
quick OMNIA execution                   -> OK
corrected OPI V11 ranking improvement   -> OK
synthetic structural dataset generation -> OK
tri-channel structural evaluation       -> OK
real local-model output collection      -> OK
real structural analysis                -> OK
structural gate V1                      -> OK
structural gate V2 training/execution   -> OK


---

Correct Claim Supported by This Run

This run supports the following limited claim:

OMNIA can be reproduced in a clean Colab environment and can execute its current structural measurement, observer perturbation, tri-channel diagnostic, and structural gate workflows.

This run does not prove:

semantic truth detection
universal contradiction detection
final decision correctness
production reliability


---

Final Boundary

measurement != inference != decision

This Colab run validates reproducible execution and structural routing behavior.

It does not change the scope boundary of OMNIA.