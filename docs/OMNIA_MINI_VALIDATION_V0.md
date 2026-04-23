# OMNIA Mini Validation v0

This document records the first executable mini-validation result obtained from the public OMNIA repository.

It is not yet a full comparative validation against external baselines.
It is a reproducible internal result showing that surface acceptability and structural admissibility can diverge.

---

## Run status

The repository was cloned and installed successfully.

Validation checks passed:

- import omnia: OK
- pytest: 47 passed

The following files were present and used:

- `examples/llm_surface_cases.jsonl`
- `examples/llm_surface_results.jsonl`
- `examples/omnia_vs_baseline.py`

---

## Executed script

```bash
python examples/omnia_vs_baseline.py


---

Output summary

Cases loaded: 8
Results loaded: 8

Fields found

case_id

task

output_text

surface_ok

surface_note

omega_score

sei_score

iri_score

drift_score

limit_triggered

gate_status

reason_code


Gate status counts

GO: 3 (0.375)

RISK: 2 (0.250)

NO_GO: 2 (0.250)

UNSTABLE: 1 (0.125)


Non-GO ratio

Non-GO cases = RISK + NO_GO + UNSTABLE = 5

non_go_ratio = 5 / 8 = 0.625

So, in this mini-set:

total cases: 8

GO cases: 3

non-GO cases: 5

non-GO ratio: 62.5%



---

Key observation

This run shows that outputs can remain superficially acceptable while being structurally risky, inadmissible, or unstable.

This is the core distinction OMNIA is trying to expose:

surface readability != structural admissibility


---

Representative cases

1) Surface-readable but unstable

case_id: collapsed_but_readable

surface_ok: true

gate_status: UNSTABLE

reason_code: collapsed_profile


Interpretation:

A response may remain readable at surface level while its structural profile is already collapsed.

2) Plausible but structurally exhausted

case_id: retrieval_plausible_but_exhausted

surface_ok: true

limit_triggered: true

gate_status: NO_GO

reason_code: limit_reached


Interpretation:

A response may appear plausible while having already exhausted its structural admissibility.

3) Confident but brittle

case_id: gsm8k_confident_but_brittle

surface_ok: true

gate_status: RISK

reason_code: high_drift


Interpretation:

Confidence and readability do not guarantee structural stability.


---

Current conclusion

This result is sufficient to support the following claim:

> OMNIA can operationally separate surface acceptability from structural admissibility in a reproducible executable setting.



This result is not yet sufficient to support the stronger claim:

> OMNIA systematically outperforms standard baselines.



That stronger claim requires a direct quantitative comparison.


---

Next step

The next required step is to compute a minimal direct comparison:

baseline = surface_ok

OMNIA = gate_status


This will quantify how many cases pass the surface baseline but are still flagged by OMNIA as:

RISK

NO_GO

UNSTABLE


That comparison will produce the first compact public evidence table.

