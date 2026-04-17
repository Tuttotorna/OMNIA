# QUICKSTART.md

## OMNIA CORE v1 — Quickstart

This document shows the shortest path to run OMNIA CORE v1.

It covers only three things:

1. installation
2. smoke test
3. batch JSONL demo

Nothing else is required for a first valid run.

---

## 1. Install

From the repository root:

```bash
pip install -e . -U

Optional import check:

python -c "from omnia import evaluate_structural_profile; print('OK import omnia')"


---

2. Run the quick smoke test

python examples/quick_omnia_test.py

Expected result:

the script executes without error

a canonical OMNIA result object is printed

the output includes:

omega_score

sei_score

iri_score

drift_score

limit_triggered

gate_status

reason_code



Example output pattern:

{
  "omega_score": 0.58,
  "sei_score": 0.55,
  "iri_score": 0.31,
  "drift_score": 0.57,
  "limit_triggered": false,
  "gate_status": "RISK",
  "reason_code": "high_drift"
}


---

3. Run the batch JSONL demo

Use the canonical demo input:

python examples/run_profiles_jsonl.py examples/demo_profiles.jsonl

This prints one enriched JSON object per line to stdout.

Each output line preserves the original input fields and adds the canonical OMNIA result fields.


---

4. Save the batch output to file

python examples/run_profiles_jsonl.py examples/demo_profiles.jsonl -o examples/results.jsonl

This writes the enriched results to:

examples/results.jsonl


---

5. Run the tests

Run the core gate tests:

pytest tests/test_gate.py

Run the canonical demo profile tests:

pytest tests/test_demo_profiles.py

Run the import test:

pytest tests/test_import.py

Or run the full test suite:

pytest


---

6. Expected input format

The JSONL runner expects one JSON object per line with at least these four fields:

omega_score

sei_score

iri_score

drift_score


Minimal example:

{"omega_score":0.84,"sei_score":0.77,"iri_score":0.12,"drift_score":0.15}
{"omega_score":0.58,"sei_score":0.55,"iri_score":0.31,"drift_score":0.57}

Additional fields are allowed and will be preserved in the output.


---

7. Expected output format

For each input record, OMNIA emits the canonical structural result fields:

omega_score

sei_score

iri_score

drift_score

limit_triggered

gate_status

reason_code


Example enriched output:

{
  "case_id": "surface_ok_but_fragile",
  "omega_score": 0.58,
  "sei_score": 0.55,
  "iri_score": 0.31,
  "drift_score": 0.57,
  "limit_triggered": false,
  "gate_status": "RISK",
  "reason_code": "high_drift"
}


---

8. What this quickstart proves

A successful quickstart proves only that:

the package installs

the canonical core imports

the gate logic executes

the output schema is serializable

batch JSONL processing works


It does not prove broad external validity.

It proves that OMNIA CORE v1 runs correctly in its minimal canonical form.


---

9. Shortest operational summary

install
-> run quick smoke test
-> run JSONL batch demo
-> inspect GO / RISK / NO_GO / UNSTABLE outputs

That is the shortest valid path through OMNIA CORE v1.

