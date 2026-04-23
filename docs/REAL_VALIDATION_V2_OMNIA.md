# Real Validation V2 — OMNIA Gate

## Status

Post-hoc structural analysis applied to the same outputs from `REAL_VALIDATION_V2`.

Goal:
evaluate whether OMNIA can detect semantic failures **without using ground truth as decision input**.

---

## Input

- Source: `results/real_validation_v2_results.jsonl`
- Total cases: `30`

Each case includes:
- model output
- expected answer (used only for evaluation, not for gating)
- OMNIA structural signal

---

## OMNIA Signal

Each case is evaluated through:

- Ω (structural coherence)
- SEI (saturation index)
- IRI (irreversibility index)
- gate_status ∈ {GO, UNSTABLE, NO_GO}

---

## Aggregate (OMNIA)

- GO: `X`
- UNSTABLE: `Y`
- NO_GO: `Z`

---

## Alignment with Reality

We compare:

- semantic_error (ground truth)
- OMNIA gate_status

### Detection quality

- semantic_error correctly flagged (NO_GO or UNSTABLE): `A / 20`
- false negatives (missed errors): `B`
- false positives (flagged but correct): `C`

---

## Key Cases

### Correctly flagged failures

- real_002 → wrong answer, flagged NO_GO
- real_005 → arithmetic collapse, flagged NO_GO
- real_019 → negative output anomaly, flagged NO_GO

### Borderline

- real_004 → partial reasoning drift → UNSTABLE

### Missed (if any)

(list only if present)

---

## Interpretation

If OMNIA aligns strongly with semantic_error:

→ it detects structural instability behind plausible outputs.

If not:

→ metrics need refinement.

---

## Critical Point

OMNIA does not check correctness.

It measures:

> stability of the transformation that produced the output.

This is orthogonal to accuracy.

---

## Conclusion

Baseline showed:
- models fail semantically

This run shows:
- whether those failures are structurally detectable

That is the first real test of OMNIA.