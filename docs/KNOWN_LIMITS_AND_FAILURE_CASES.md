# OMNIA — Known Limits and Failure Cases

## Purpose

This document records known limits, expected failure cases, and non-goals of OMNIA.

It exists to make the system easier to review, falsify, and correctly interpret.

OMNIA is strongest when it is read as:

```text
a post-hoc structural stability gate for AI outputs
```

OMNIA is weakest when it is misread as:

```text
a truth oracle
a semantic evaluator
a final decision system
a universal hallucination detector
```

The central boundary remains:

```text
measurement != inference != decision
```

---

## Core boundary

OMNIA measures structural behavior.

OMNIA does not infer semantic truth.

OMNIA does not make final decisions.

This means that OMNIA can expose structural fragility without deciding whether an output is true or false.

It also means that OMNIA can fail to detect a semantic error when the output remains structurally admissible.

This is not an implementation accident.

It is the boundary of the system.

---

## Main limitation

The main limitation is:

```text
structural validity != semantic correctness
```

A structurally valid output can be semantically wrong.

A semantically correct output can be structurally fragile.

Therefore, OMNIA must not be used alone as a final evaluator.

It should be used before, beside, or inside a broader evaluation pipeline.

---

## Failure case 1 — Semantic error with stable structure

OMNIA may return `GO` for a semantically wrong answer if the answer is structurally well-formed and stable.

Examples:

```text
Expected answer: 4
Model output:    Final answer: 2.

Expected answer: dog
Model output:    Final answer: wolf.

Expected color: black
Model output:   Final answer: blue.
```

These outputs may be semantically wrong.

But if they satisfy the structural contract and remain stable under tested perturbations, OMNIA may treat them as structurally admissible.

Correct interpretation:

```text
GO = no structural instability detected inside the tested regime
```

Incorrect interpretation:

```text
GO = true
GO = correct
GO = safe
GO = deployable
```

OMNIA does not make those claims.

---

## Failure case 2 — Correct answer with fragile structure

OMNIA may return `RISK` for an answer that is semantically correct but structurally fragile.

Example:

```text
Expected answer: 15
Model output:    Final answer: 15.
```

The answer may be correct.

However, if nearby variants degrade, collapse, become uncertain, or violate the expected contract, OMNIA may flag structural fragility.

Correct interpretation:

```text
RISK = structural degradation detected
```

Incorrect interpretation:

```text
RISK = false
RISK = wrong
RISK = unsafe in every context
```

OMNIA does not make those claims.

---

## Failure case 3 — Overflagging

OMNIA may overflag outputs when the structural proxy is too strict.

Possible causes:

```text
thresholds are too aggressive
similarity metric is too shallow
acceptable variation is treated as degradation
domain-specific wording changes are misread as instability
contract rules are too narrow
perturbations are poorly designed
```

Overflagging means OMNIA may return `RISK` or `STOP` where a downstream evaluator would accept the output.

This is expected in early or conservative gate settings.

Mitigation:

```text
adjust thresholds
improve structural metrics
define better output contracts
test domain-specific perturbations
separate structural variation from structural degradation
preserve failure cases
```

---

## Failure case 4 — Underflagging

OMNIA may underflag outputs when the tested transformations do not expose the instability.

Possible causes:

```text
perturbation set is too weak
metric does not capture the relevant collapse
output is structurally stable but semantically false
surface contract is too permissive
failure mode is outside the tested regime
```

Underflagging means OMNIA may return `GO` even though another evaluator later rejects the output.

This does not invalidate the boundary.

It shows the limit of the tested structural regime.

Mitigation:

```text
expand perturbation families
add stronger contract checks
compare multiple structural metrics
test against real model outputs
record false negatives
separate semantic failures from structural failures
```

---

## Failure case 5 — Metric artifact

A structural signal may be produced by the metric rather than by a meaningful property of the output.

Possible causes:

```text
string similarity bias
length bias
formatting bias
tokenization artifact
threshold artifact
dataset artifact
case construction artifact
```

This is why OMNIA results must be falsified.

A useful reviewer should ask:

```text
Does the result survive a different metric?
Does the result survive threshold changes?
Does the result survive different perturbations?
Does the signal remain when superficial length or formatting effects are controlled?
```

Metric artifacts are not hidden.

They are part of the falsification path.

---

## Failure case 6 — Surface contract weakness

If the surface check is too weak, malformed outputs may pass.

If the surface check is too strict, acceptable outputs may fail.

This affects the gate.

Example of weak contract:

```text
non-empty output = PASS
```

Example of stronger contract:

```text
must contain final answer marker
must satisfy expected schema
must preserve required fields
must remain parseable
must satisfy scalar-only answer when required
```

OMNIA depends on explicit contracts.

Poor contracts produce poor structural readings.

---

## Failure case 7 — Perturbation regime weakness

OMNIA only measures stability under the transformations that are actually tested.

If the perturbation regime is too narrow, failures may remain invisible.

If the perturbation regime is too aggressive, valid variation may be misclassified as instability.

Correct reading:

```text
OMNIA measures stability inside a defined transformation regime.
```

Incorrect reading:

```text
OMNIA proves universal stability.
```

No such universal claim is made.

---

## Failure case 8 — Domain mismatch

A structural metric that works for one domain may not work for another.

Examples:

```text
short arithmetic answers
long natural-language explanations
code patches
logs
security configurations
cryptographic outputs
multi-step reasoning traces
scientific claims
legal text
```

Different domains may require different contracts, perturbations, metrics, and thresholds.

OMNIA should not assume that one proxy works everywhere.

---

## Failure case 9 — Correctness hidden outside structure

Some failures are semantic, factual, legal, ethical, or operational.

They may not appear as structural instability.

Examples:

```text
wrong date
wrong legal interpretation
wrong medical recommendation
wrong citation
wrong identity
wrong causal claim
misleading but well-formed answer
```

OMNIA may not detect these by itself.

These require external evaluators.

Correct pipeline:

```text
OMNIA structural gate
  -> semantic evaluator
  -> domain review
  -> external decision layer
```

---

## Failure case 10 — GO misinterpretation

The most dangerous misuse is interpreting `GO` as final correctness.

GO means:

```text
no structural instability was detected inside the tested regime
```

GO does not mean:

```text
true
correct
complete
safe
approved
deployable
legally valid
scientifically valid
morally acceptable
```

GO is a structural signal only.

The final decision remains external.

---

## Failure case 11 — RISK misinterpretation

RISK means:

```text
measurable structural fragility or degradation was detected
```

RISK does not mean:

```text
the answer is false
the answer is unsafe
the answer must be rejected in every context
the model failed semantically
```

RISK means the output should not proceed blindly.

It should be reviewed, retried, compared, or routed to another layer.

---

## Failure case 12 — STOP misinterpretation

STOP means:

```text
the current diagnostic path reached a structural boundary
```

STOP does not mean:

```text
the whole system failed
the task is impossible
the output is semantically false
all further analysis is forbidden
```

External systems may open a new diagnostic space, change the contract, retry, or escalate.

OMNIA does not decide that action.

---

## Non-goals

OMNIA does not aim to be:

```text
a semantic truth engine
a universal evaluator
a human judgment replacement
a benchmark replacement
a safety certification system
a legal compliance system
a medical evaluator
a production policy engine
a consciousness model
a reasoning engine
```

These are outside the system boundary.

---

## Valid use

OMNIA is validly used when the question is structural.

Examples:

```text
Does the output remain stable under controlled perturbation?
Does the output preserve its expected contract?
Does the structure degrade under nearby transformations?
Does the reasoning trace collapse under reordering?
Does surface validity hide structural fragility?
Does the output remain admissible enough for downstream evaluation?
```

---

## Invalid use

OMNIA is misused when the question is final or semantic.

Examples:

```text
Is the answer true?
Is the answer legally correct?
Is the answer medically safe?
Is the output morally acceptable?
Should this be deployed?
Is the model generally reliable?
```

OMNIA does not answer these questions.

It can only provide structural evidence to an external process.

---

## Reviewer falsification checklist

A reviewer should test whether OMNIA fails under controlled changes.

Useful checks:

```text
[ ] Change thresholds.
[ ] Change perturbations.
[ ] Change similarity metrics.
[ ] Add semantically wrong but structurally stable outputs.
[ ] Add semantically correct but structurally fragile outputs.
[ ] Add domain-specific outputs.
[ ] Test short answers and long explanations separately.
[ ] Check whether RISK is caused by length artifacts.
[ ] Check whether GO hides semantic errors.
[ ] Record both false positives and false negatives.
```

A useful failure does not destroy OMNIA.

It defines the boundary of what OMNIA can and cannot measure.

---

## How limits strengthen the project

Explicit limits make OMNIA stronger.

They prevent false claims.

They make review easier.

They preserve the core separation:

```text
measurement != inference != decision
```

The system is useful only if its boundary is clear.

---

## Summary

Known limits can be reduced to one central rule:

```text
OMNIA measures structural stability.
OMNIA does not decide semantic truth.
```

Therefore:

```text
GO   != true
RISK != false
STOP != global failure
```

The final boundary remains:

```text
measurement != inference != decision
```
