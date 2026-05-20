# Input / Output Contract

This document defines the public shape expected from OMNIA measurements.

The goal is clarity.

A reviewer should understand what entered the engine and what came out.

---

## Input

An OMNIA input may be:

- generated text;
- model output;
- structured trace;
- numeric representation;
- transformed variant;
- trajectory;
- artifact emitted by another repository;
- measurement candidate.

The input should be explicitly named.

---

## Transformation

A transformation may be:

- perturbation;
- rewrite;
- representation shift;
- base change;
- temporal shift;
- observer-frame change;
- controlled variant;
- adversarial or stress condition.

The transformation should be documented.

---

## Measurement

A measurement should specify:

- what property is being measured;
- what metric or signal is emitted;
- what threshold or condition applies, if any;
- what version or protocol generated it.

---

## Output

An output may be:

- score;
- signal;
- flag;
- report;
- JSON artifact;
- JSONL row;
- gate result;
- drift measurement;
- irreversibility measurement;
- stability indicator.

A useful output should include the boundary:

    what this result means
    what this result does not mean

---

## Minimal JSON shape

A minimal measurement artifact can use this shape:

    {{
      "case_id": "stable-case-id",
      "input_ref": "path-or-description",
      "transformation": "declared transformation",
      "measurement": {{}},
      "output": {{}},
      "boundary": "measurement != inference != decision",
      "limitation": "What this result does not prove"
    }}

---

## No silent promotion

A measurement output must not silently become a semantic truth claim.

A score is not a decision.

A signal is not a verdict.

A boundary is part of the output.

