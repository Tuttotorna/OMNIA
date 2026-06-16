# Structural Stability Audit

## One-line claim

An output that is correct in one form is not necessarily stable under controlled transformations.

---

## Purpose

This audit tests whether a structure remains compatible under admissible transformations.

It does not decide truth.

It does not decide meaning.

It does not replace domain judgement.

It measures whether structural relations survive transformation.

---

## Definitions

Let:

`X` = object, output, response, model result, structure, document, or representation

`F` = family of admissible transformations

`T_f(X)` = transformed version of `X` under transformation `f in F`

`C(X, T_f(X))` = compatibility relation or score between original and transformed structures

The audit asks:

Does `X` remain structurally compatible under the relevant transformation family `F`?

---

## Examples of transformations

- paraphrase;
- prompt variation;
- format change;
- representation change;
- scale change;
- order change;
- base change;
- translation;
- perturbation;
- segmentation;
- environment change;
- observer-frame change.

---

## Audit questions

1. What structure is being tested?
2. What transformations are admissible?
3. What relations must remain stable?
4. Which transformations break compatibility?
5. Are the breaks acceptable, expected, or critical?
6. Does the output remain usable inside the target scope?

---

## Verdicts

| Verdict | Meaning |
|---|---|
| `STABLE_WITHIN_SCOPE` | The structure remains compatible under the tested transformations. |
| `FRAGILE` | The structure changes materially under relevant transformations. |
| `RUPTURE` | Core relations break under transformation. |
| `INSUFFICIENT_TRANSFORMATIONS` | The tested transformations are too weak to support a stability claim. |
| `OUT_OF_SCOPE` | The tested transformations do not match the target use. |

---

## Boundary

This audit can show instability.

It cannot prove absolute truth.

A structure can be stable and still wrong.

A structure can be locally correct and structurally fragile.

---

## Final statement

Correct once does not mean stable.\n