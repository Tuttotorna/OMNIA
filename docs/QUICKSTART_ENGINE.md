# Quickstart Engine

This document gives the fastest path to seeing OMNIA as a core measurement engine.

The public mental model is:

    input -> transformation -> measurement -> output -> boundary

---

## Clean install

    git clone https://github.com/Tuttotorna/OMNIA.git
    cd OMNIA
    python -m pip install -e .
    pytest

---

## What to look for

After installation and tests, look for the smallest available example or smoke test.

The point is not to prove the whole theory.

The point is to identify:

    What is the input?
    What transformation is applied?
    What is measured?
    What output is produced?
    What boundary is declared?

---

## Expected engine behavior

A good OMNIA engine path should produce an output that can be read as a measurement artifact.

It should not silently become:

    semantic judgment
    final decision
    truth certificate
    model intelligence claim

---

## Public compression

    OMNIA measures structural behavior.
    It does not infer meaning.
    It does not decide truth.

