# Decision Object Validator Demo

## Status

This is a constructed demonstration of the prototype tool.

It does not prove OMNIA.

It does not prove new mathematics.

It only shows how the validator detects decision-object failure.

## Demo field

Input file:

demo_decisions.csv

Object used for decision:

risk_score

Decision:

action

Hidden/context fields:

segment, exposure

## Expected result

The demo contains exact decision-object collisions:

risk_score = 72

action = block / approve

and:

risk_score = 85

action = urgent_patch / defer_patch

Therefore:

D cannot factor through pi

on the observed demo data.

## Run

From the repository root:

python field-tools/TOOLS/decision_object_validator.py \
  --input field-tools/EXAMPLES/DECISION-OBJECT-VALIDATOR-DEMO/demo_decisions.csv \
  --object-column risk_score \
  --decision-column action \
  --id-column case_id \
  --hidden-columns segment,exposure \
  --bucket-width 10 \
  --outdir field-tools/EXAMPLES/DECISION-OBJECT-VALIDATOR-DEMO/output

## Generated output

The committed demo output is in:

field-tools/EXAMPLES/DECISION-OBJECT-VALIDATOR-DEMO/output/
