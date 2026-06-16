# Decision-Validity Audit Sheet

Use this sheet for any metric, KPI, benchmark, model score, aggregate, representation, or classification used to support a decision.

---

## 1. Decision

What decision is being made?

`D =`

---

## 2. Object used

What object is used to make the decision?

Examples: metric, benchmark, KPI, score, aggregate, model output, representation, ranking, classification.

`pi =`

---

## 3. Field reduced

What system, field, population, process, or generative structure is being reduced?

`Omega =`

---

## 4. Required distinctions

Which distinctions must the decision preserve?

List the differences that would require different decisions.

- Distinction 1:
- Distinction 2:
- Distinction 3:

---

## 5. Collapse test

Can two different states become identical or indistinguishable under the object used?

`pi(omega1) = pi(omega2)`

- Yes
- No
- Unknown

Describe:

---

## 6. Decision divergence

If two states collapse under `pi`, do they require different decisions?

`D(omega1) != D(omega2)`

- Yes
- No
- Unknown

Describe:

---

## 7. Verdict

Choose one:

- `VALID_WITHIN_SCOPE`
- `INVALID_OBJECT`
- `INSUFFICIENT_FIELD`
- `OUT_OF_SCOPE`
- `REQUIRES_REVIEW`

---

## 8. Correction

What object, field, stratification, measurement, or additional distinction is required?

---

## 9. Result

What decision changes after correction?

---

## 10. Minimal conclusion

The decision is / is not validly founded on the object used because:\n