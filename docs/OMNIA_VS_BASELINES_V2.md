# OMNIA vs Baselines V2

## Results

| Method | TP | FN | FP | TN | Precision | Recall |
|---|---:|---:|---:|---:|---:|---:|
| OMNIA V7 | 10 | 0 | 0 | 6 | 1.000 | 1.000 |
| Baseline Simple V1 | 0 | 10 | 0 | 6 | 0.000 | 0.000 |
| Baseline Majority V2 | 5 | 5 | 1 | 5 | 0.833 | 0.500 |

## Interpretation

OMNIA V7 outperforms both baselines on this controlled validation set.

The non-trivial baseline improves over the trivial baseline, but still misses half of the observed errors and introduces one false positive.

OMNIA V7 detects all observed errors and blocks no correct outputs.

## Status

Still minimal validation.

More datasets and stronger models required.