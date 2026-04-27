# OMNIA — External Validation Entry Point

## Purpose

This document defines how an external reader can verify OMNIA without prior context.

No internal knowledge required.

No interpretation required.

Only execution.

---

## What to run

Minimal path:

```bash
pip install -e . -U --no-cache-dir

python examples/collect_real_outputs_v1.py
python examples/evaluate_real_outputs_v1.py
python examples/omnia_structural_gate_v1.py
python examples/train_structural_gate_v2.py
python examples/use_structural_gate_v2.py


---

What you should observe

1. Real outputs are structurally unstable

total  = 60
atomic ≈ 15%
short  ≈ 15%
long   ≈ 70%

Interpretation:

Most outputs are not clean structured answers.


---

2. Structural gate does not pass everything

PASS   ≈ 40%
REVIEW ≈ 45%
REJECT ≈ 15%

Interpretation:

The system does not collapse to trivial acceptance.


---

3. Learned gate reproduces rule-based gate

Delta:
PASS   +1
REVIEW -1
REJECT  0

Interpretation:

The learned model captures the structural boundary.


---

What this proves

Minimal claim:

A structural-only layer can:

- detect malformed outputs
- detect structural drift
- separate outputs into routing categories


---

What this does NOT prove

This does NOT prove:

semantic correctness

factual accuracy

reasoning validity

universal detection



---

Boundary

measurement != inference != decision

OMNIA is a measurement layer only.


---

Reproducibility requirement

A valid claim requires:

dataset

runner

result file


All included in this repository.


---

Final instruction

If the outputs you observe differ significantly:

inspect dataset

inspect runner

inspect environment


The system is deterministic at this scale.


---

One-line takeaway

OMNIA does not decide.

OMNIA filters structure before anything else.


