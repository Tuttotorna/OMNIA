File: docs/LABELING_POLICY.md

# OMNIA - Labeling Policy

## Purpose

This document defines the labeling policy for the first external validation pass of OMNIA core.

Its purpose is to freeze the acceptability labeling rule before final scoring.

The dataset must not be labeled opportunistically after observing OMNIA results.

---

## Labeling role

The first external validation task is:

> support-response screening

Therefore, the label attached to each item must answer only one bounded operational question:

> should this response be allowed to pass forward?

This is the only labeling question.

It is not a universal truth judgment.
It is not a semantic perfection score.
It is not a general quality rating.

It is a bounded pass-forward acceptability decision.

---

## Label space

Each item must receive exactly one label:

- `PASS`
- `FAIL`

### `PASS`
The response is operationally acceptable to pass forward inside the bounded support task.

### `FAIL`
The response should not be allowed to pass forward inside the bounded support task.

---

## Canonical labeling question

For every item, the annotator must answer:

> if this response appeared in a bounded support workflow, should it be allowed to pass forward?

This is the canonical labeling question.

No alternative hidden question may be substituted during annotation.

---

## PASS criteria

A response should be labeled `PASS` only if it is operationally acceptable to pass forward.

Typical properties of a `PASS` item:

- non-empty
- readable
- support-like in form
- not obviously corrupted
- not obviously repetitive junk
- not materially misleading in a way that makes pass-forward unacceptable
- not structurally degraded enough to make operational pass unacceptable

A `PASS` label does not mean the response is perfect.
It means it is acceptable to pass forward under the bounded task.

---

## FAIL criteria

A response should be labeled `FAIL` if it should not pass forward in the bounded support setting.

Typical properties of a `FAIL` item:

- empty or near-empty
- visibly corrupted
- junk-like or repetitive in a materially unacceptable way
- placeholder-like instead of operationally usable
- misleading or operationally unsafe to pass forward
- superficially polite but materially unfit
- structurally weak enough that pass-forward is unacceptable

A `FAIL` label means the response should not be allowed through the bounded workflow.

---

## Borderline rule

Borderline cases are expected.

For borderline items, the annotator must still choose one label.

Decision rule for borderline cases:

```text
when in doubt, ask whether passing the response forward would be operationally acceptable without hidden rescue context

If the answer is no, label FAIL.

If the answer is yes, label PASS.

This rule prevents indefinite ambiguity.


---

No hidden rescue rule

The annotator must not assume missing hidden context that is not present in the item.

If a response would only become acceptable after adding unavailable context, editing, or repair, it should not be labeled PASS.

The item must be judged as it exists in the frozen dataset.


---

Single-question discipline

The annotator must not silently replace the canonical question with other questions such as:

is this polite?

is this grammatical?

is this probably true?

is this helpful in theory?

is this semantically rich?

would a generous human forgive it?


Those are not the labeling objective.

The only objective is bounded pass-forward acceptability.


---

Consistency rule

The same standard must be applied to all items.

In particular:

superficially readable but operationally weak items must be judged by the same rule every time

empty-template items must be judged consistently

repetitive or degraded outputs must be judged consistently

acceptable but minimal outputs must be judged consistently


Consistency is more important than stylistic preference.


---

Annotator model

For the first validation pass, a single frozen annotator policy is acceptable if:

the dataset remains bounded

the labeling question is explicit

the criteria are written in advance

labels are frozen before final scoring


Multi-annotator adjudication may be added later, but is not required for the first bounded pass.


---

Freeze rule

Once the dataset is frozen and labeling is complete:

labels may not be changed

criteria may not be reinterpreted

borderline items may not be relabeled after observing OMNIA results


If labels must change materially, a new versioned dataset must be created.

No silent mutation is allowed.


---

Versioning rule

The labeling policy is tied to the dataset version.

Example:

dataset: support_screening_external_v1.jsonl
labeling policy: labeling_policy_v1

If the policy changes materially, the version must change.


---

What this labeling does not claim

This labeling policy does not claim:

universal truth judgment

semantic finality

production certification

legal or safety certification

domain-complete customer-support evaluation


It defines only the bounded label needed for the first OMNIA external validation pass.


---

Minimal labeling summary

question: should this response be allowed to pass forward?
label space: PASS / FAIL
PASS = operationally acceptable to pass
FAIL = should not pass
borderline rule = decide based on pass-forward acceptability without hidden rescue context
freeze rule = no relabeling after observing results


---

Canonical labeling sentence

The first OMNIA external validation labels each support-style response only by bounded pass-forward acceptability, using a frozen PASS/FAIL policy and no hidden rescue assumptions.