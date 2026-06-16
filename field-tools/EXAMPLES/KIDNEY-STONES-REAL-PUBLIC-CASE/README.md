# Kidney Stone Treatment — Real Public Decision-Validity Case

## Status

This is a real public case application.

It does not prove OMNIA.

It does not prove a new mathematical theory.

It is not medical advice.

It is not a claim about current clinical practice.

It does not validate the entire framework.

It shows one specific decision-validity failure:

**aggregate treatment success rate is the wrong object for a stone-size-conditioned treatment decision.**

---

## Source status

The data are a historical clinical dataset commonly used as a canonical example of Simpson's paradox.

The data are reported from:

- Charig C.R., Webb D.R., Payne S.R., Wickham J.E. Comparison of treatment of renal calculi by open surgery, percutaneous nephrolithotomy, and extracorporeal shockwave lithotripsy. British Medical Journal. 1986;292:879-882.
- Julious S.A., Mullee M.A. Confounding and Simpson's paradox. BMJ. 1994;309:1480-1481.
- Bonovas S., Piovani D. Simpson's Paradox in Clinical Research: A Cautionary Tale. Journal of Clinical Medicine. 2023;12(4):1633.

---

## Definitions

`Omega` = stone-size-conditioned treatment field

`pi` = aggregate treatment success rate ignoring stone size

`D` = stone-size-conditioned treatment choice by highest observed success rate

---

## Field data

| stone_size | treatment | successes | total | failures | success_rate |
| --- | --- | --- | --- | --- | --- |
| small | A | 81 | 87 | 6 | 0.931034 |
| small | B | 234 | 270 | 36 | 0.866667 |
| large | A | 192 | 263 | 71 | 0.730038 |
| large | B | 55 | 80 | 25 | 0.6875 |

---

## Aggregate projection pi

| treatment | successes | total | failures | success_rate |
| --- | --- | --- | --- | --- |
| A | 273 | 350 | 77 | 0.78 |
| B | 289 | 350 | 61 | 0.825714 |

Decision from aggregate `pi`:

`Treatment B`

---

## Stone-size-conditioned decision D

| stone_size | chosen_treatment | success_rate | successes | total |
| --- | --- | --- | --- | --- |
| large | A | 0.730038 | 192 | 263 |
| small | A | 0.931034 | 81 | 87 |

Decision from conditioned field `Omega`:

{
  "large": "A",
  "small": "A"
}

---

## Conflict

The aggregate projection recommends:

`Treatment B`

The stone-size-conditioned field recommends:

`Treatment A`

for both stone-size groups.

Therefore:

`aggregate_vs_stratified_conflict = True`

---

## Decision-validity conclusion

The aggregate success rate is not false as an aggregate.

It is invalid for the stone-size-conditioned treatment decision because it removes the conditioning field that changes the decision object.

Therefore:

**aggregate treatment success rate is the wrong object for a stone-size-conditioned treatment decision.**

---

## Boundary

This case does not claim that Treatment A or Treatment B should be used in present-day clinical practice.

It only shows that a decision based on aggregate treatment success rate can be invalid when the relevant decision requires conditioning on stone size.

---

## Public sentence

Correct answers to the wrong object are not solutions.

---

## Files

- `stone_size_conditioned_field.csv`
- `aggregate_projection_pi.csv`
- `stone_size_conditioned_decision_D.csv`
- `verdict.json`
- `reproduce.py`
