# OMNIA v1.0 — Structural Measurement Engine

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19488048.svg)](https://doi.org/10.5281/zenodo.19488048)

**Author:** Massimiliano Brighindi  
**Project:** MB-X.01

---

## What OMNIA does

OMNIA is a post-hoc structural measurement engine.

It does not generate answers.  
It does not interpret semantics.  
It does not make decisions.

It measures whether an output remains structurally admissible under controlled variation.

```text
Structural truth = invariance under transformation

If an output stays coherent under transformation, structure holds.
If it drifts, exhausts itself, or collapses, OMNIA measures that failure.


---

Core claim

surface-readable output != always structurally admissible

That is the entire point.

A system can produce output that looks correct, fluent, and acceptable, while the underlying structure is already weak.

OMNIA is designed to detect that gap.


---

Architectural boundary

measurement != inference != decision

OMNIA performs measurement only.

It does not:

replace a model

infer intent

interpret meaning

make final decisions


It emits structural signals that an external layer may use.


---

What OMNIA returns

Main outputs include:

omega_score → structural coherence

drift_score → instability under variation

iri_score → irreversibility

sei_score → remaining structural extractability

gate_status → admissibility class


Gate classes:

GO

RISK

NO_GO

UNSTABLE


Interpretation:

GO = structurally admissible

RISK = readable but fragile

NO_GO = readable but not structurally admissible

UNSTABLE = collapse detected



---

Verified status

The repository has been executed end-to-end in a fresh Colab runtime.

Verified:

clone: OK

install: OK

import: OK

tests: OK

smoke example: OK

frozen artifact rebuild: OK

analyzers: OK


Test result:

47 passed

So this is not documentation-only.
The repo runs.


---

Smoke result

Verified smoke execution:

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

Meaning:

OMNIA core executed correctly

the case was not saturated

the output was classified as RISK

the dominant failure signal was high_drift



---

Main result

Current frozen mini-suite summary:

Dataset	Total	GO	RISK	NO_GO	UNSTABLE	non_GO	Ratio

Surface OK	8	3	2	2	1	5	5/8
LLM Surface	8	3	2	2	1	5	5/8
Support Responses	8	3	2	2	1	5	5/8
RAG Answers	8	3	2	2	1	5	5/8


So the strongest current public statement is:

In the current frozen mini-suite, 5 out of 8 surface-readable outputs are not GO.

This is the value of the repository.

Not that OMNIA writes better outputs.
Not that OMNIA knows truth in the semantic sense.

But this:

OMNIA separates surface readability from structural admissibility.


---

Why it matters

Most evaluation pipelines still confuse these layers:

readable output

correct-looking output

structurally stable output


They are not the same thing.

An output can look fine and still be structurally weak.

If a system cannot detect that difference, it is exposed to silent failure.

OMNIA is built to operate there.


---

Quick start

Clone:

git clone https://github.com/Tuttotorna/OMNIA.git
cd OMNIA

Install:

pip install -e .

Run tests:

pytest -q

Run smoke example:

python examples/quick_omnia_test.py

Run full frozen rebuild + analysis:

python examples/rebuild_and_analyze_all.py


---

Minimal formula

Output can look fine.
Structure can still fail.
OMNIA measures that failure.
measurement != inference != decision


---

Scope

What is justified now:

the engine runs

the tests pass

the examples run

the frozen suite is reproducible

the admissibility split is measurable


What is not justified now:

universal claims

benchmark supremacy claims

claims that OMNIA solves hallucinations in general

claims that OMNIA replaces reasoning or decision systems


The strength of the project is not hype.
It is boundary discipline.


---

Contact

Massimiliano Brighindi
MB-X.01

GitHub:
https://github.com/Tuttotorna/OMNIA

DOI:
10.5281/zenodo.19488048