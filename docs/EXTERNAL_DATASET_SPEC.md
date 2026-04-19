# OMNIA - External Dataset Specification

## Purpose

This document defines the dataset specification for the first external validation pass of OMNIA core.

Its purpose is to freeze the structure of the evaluation set before scoring.

This prevents post-hoc dataset shaping after seeing results.

---

## Dataset role

The dataset is used only for the first bounded external validation task:

> support-response screening

The dataset must allow comparison between:

- baseline alone
- baseline + OMNIA

on the same frozen set of support-style responses.

---

## Dataset type

The dataset must be a frozen JSONL file.

Each line must represent one support-style response item.

The dataset is bounded and task-specific.
It is not intended as a general-purpose language benchmark.

---

## Data source

The dataset must be external to OMNIA's descriptive documents and internal self-explanatory material.

Allowed sources include:

- publicly available support-response datasets
- externally sourced support-style response corpora
- manually assembled support-style response sets derived from external prompts and outputs
- synthetic support-style outputs only if explicitly marked and generated under frozen rules

Preferred order:

1. public external source
2. externally sourced manually frozen set
3. synthetic bounded set under frozen protocol

The source used must be declared explicitly.

---

## Inclusion criteria

A case may be included only if all of the following are true:

1. it is a support-style response or clearly support-like operational reply
2. it is short enough to remain bounded and readable
3. it can be labeled for pass-forward acceptability
4. it is self-contained enough to evaluate without hidden context
5. it is stored in the frozen JSONL format defined below

Examples of admissible cases:

- order-status replies
- refund replies
- account-access replies
- shipping-delay replies
- generic customer-support responses
- templated support answers
- apparently polite but structurally weak support responses

---

## Exclusion criteria

A case must be excluded if any of the following are true:

- it requires deep hidden context unavailable in the item
- it depends on external attachments or long thread history
- it is too long to remain operationally bounded
- it is not support-style
- it cannot be labeled consistently for acceptability
- it was added after final scoring criteria were already observed
- it is duplicated or near-duplicated without explicit reason

---

## Dataset size

Target size for the first validation pass:

```text
50 to 200 items

This range is large enough to avoid toy-level triviality and small enough to remain manually auditable.

Preferred initial target:

100 items


---

Balance requirement

The dataset should contain a meaningful mix of:

acceptable support responses

unacceptable but superficially plausible responses

clearly weak or fragile responses

borderline cases


The goal is not class balance for its own sake.

The goal is to test whether OMNIA detects silent fragility better than the baseline.


---

Label definition

Each item must carry one bounded acceptability label.

Canonical label field:

label

Allowed values:

PASS

FAIL


PASS

The response is operationally acceptable to pass forward inside the bounded task.

FAIL

The response should not pass forward inside the bounded task.

This label is not a universal truth label. It is a bounded operational acceptability label.


---

Labeling question

Each item must be labeled by answering only this question:

> should this response be allowed to pass forward?



This keeps the label aligned with the validation task.


---

JSONL schema

Each line in the dataset must be a JSON object with at least these fields:

case_id

source

prompt

response

label


Recommended schema:

{
  "case_id": "support-001",
  "source": "external_public" ,
  "prompt": "My order still has not arrived. Where is it?",
  "response": "Your order is currently in transit and should arrive soon.",
  "label": "PASS"
}

Additional optional metadata may be included, such as:

topic

subtype

notes

split

source_url

generation_protocol


But the canonical minimum fields remain fixed.


---

Source field

Canonical source values may include:

external_public

external_manual

synthetic_frozen


This field is required because the origin of the item must remain inspectable.


---

Synthetic data rule

Synthetic data is allowed only under strict conditions.

If synthetic data is used:

it must be explicitly marked as synthetic

the generation protocol must be frozen and documented

the set must be fixed before scoring

the same protocol must be reproducible


Synthetic data must not be passed off as external public data.


---

Freeze rule

Once the evaluation set is declared frozen:

no items may be added

no items may be removed

no labels may be changed

no source metadata may be altered


unless a new versioned dataset is explicitly created.

This rule is mandatory.


---

Versioning rule

The dataset must be versioned.

Example:

support_screening_external_v1.jsonl

If the set changes materially, the version must change.

No silent mutation is allowed.


---

Duplicate control

The dataset must be checked for:

exact duplicates

near-duplicates

template clones that trivialize evaluation


Duplicate-heavy sets distort the validation.

If duplicates are intentionally kept, this must be documented.


---

Labeling procedure

The labeling procedure must be declared before final scoring.

Allowed options:

single frozen annotator with explicit written criteria

multiple annotators with adjudication

externally sourced label set if already available


The first validation pass may use a single frozen labeling policy if the policy is explicit and the dataset is small.


---

Acceptability criteria

A response may be labeled PASS only if it is operationally acceptable inside the bounded support task.

A response should be labeled FAIL if it is:

structurally weak in a way that makes pass-forward unacceptable

misleading

empty or near-empty in operational value

obviously repetitive or degraded

operationally unsafe to pass in the bounded setting

superficially polite but materially unfit


These criteria must be applied consistently.


---

What this dataset is not

This dataset is not:

a universal language benchmark

a reasoning benchmark

a semantic truth benchmark

a safety benchmark in the broad sense

a production certification artifact


It is only a bounded dataset for the first external OMNIA validation pass.


---

Minimal dataset summary

task: support-response screening
format: frozen JSONL
size target: 50 to 200 items
preferred size: 100 items
label space: PASS / FAIL
unit: one support-style response item
freeze rule: no mutation after final dataset freeze


---

Canonical dataset sentence

The first external OMNIA validation dataset must be a frozen, bounded, support-style JSONL set labeled for pass-forward acceptability.