# Case Template

## Case title

`[field] — [decision] — [object used]`

---

## 1. Context

Describe the decision environment without theory or rhetoric.

---

## 2. Decision D

What decision is being made?

Example:

- deploy model A or B;
- patch vulnerability X before Y;
- roll out variant B;
- choose treatment;
- rank systems;
- approve release;
- allocate budget.

---

## 3. Object used pi

What object is used to make the decision?

Example:

- aggregate conversion rate;
- benchmark score;
- KPI;
- risk score;
- leaderboard rank;
- model output;
- representation;
- average value.

---

## 4. Accessible field Omega

What field is being reduced by the object?

Include the relevant structure:

- segments;
- conditions;
- populations;
- deployment environments;
- costs;
- constraints;
- causal variables;
- hidden dependencies;
- transformation family.

---

## 5. Collapse

Show the collapse.

Find or construct:

`pi(omega1) = pi(omega2)`

or practical equivalence:

`pi(omega1) approximately equals pi(omega2)`

---

## 6. Decision divergence

Show that the collapsed states require different decisions.

`D(omega1) != D(omega2)`

---

## 7. Audit conclusion

If collapse and decision divergence are present:

`pi` cannot ground `D`.

The decision is being made on the wrong object.

---

## 8. Correction

Define the corrected object.

Examples:

- stratified metric;
- decision-specific benchmark;
- deployment-conditioned score;
- causal model;
- richer field;
- transformation-stability score;
- risk vector instead of scalar.

---

## 9. Result

What changes?

- decision changed;
- decision suspended;
- additional data required;
- ranking invalidated;
- deployment blocked;
- gate passed only within scope;
- management action corrected.

---

## 10. Final sentence

Correct answers to the wrong object are not solutions.\n