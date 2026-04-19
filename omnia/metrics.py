from __future__ import annotations

from collections import Counter
from typing import Iterable, List


def _clip01(x: float) -> float:
    if x < 0.0:
        return 0.0
    if x > 1.0:
        return 1.0
    return x


def _safe_mean(values: Iterable[float]) -> float:
    vals = [float(v) for v in values]
    if not vals:
        return 0.0
    return sum(vals) / float(len(vals))


def _char_counter(text: str) -> Counter:
    return Counter(text)


def _jaccard_chars(a: str, b: str) -> float:
    sa = set(a)
    sb = set(b)
    union = sa | sb
    if not union:
        return 1.0
    return len(sa & sb) / float(len(union))


def _length_similarity(a: str, b: str) -> float:
    max_len = max(len(a), len(b))
    if max_len == 0:
        return 1.0
    return 1.0 - (abs(len(a) - len(b)) / float(max_len))


def _multiset_overlap(a: str, b: str) -> float:
    ca = _char_counter(a)
    cb = _char_counter(b)

    total_a = sum(ca.values())
    total_b = sum(cb.values())

    if total_a == 0 and total_b == 0:
        return 1.0

    overlap = 0
    for ch in set(ca) | set(cb):
        overlap += min(ca.get(ch, 0), cb.get(ch, 0))

    denom = max(total_a, total_b)
    if denom == 0:
        return 1.0
    return overlap / float(denom)


def _pair_similarity(a: str, b: str) -> float:
    scores = [
        _jaccard_chars(a, b),
        _length_similarity(a, b),
        _multiset_overlap(a, b),
    ]
    return _clip01(_safe_mean(scores))


def compute_omega_score(baseline_text: str, variants: List[str]) -> float:
    if not isinstance(baseline_text, str):
        raise TypeError("baseline_text must be a string")
    if not isinstance(variants, list):
        raise TypeError("variants must be a list")

    cleaned = [v for v in variants if isinstance(v, str) and v.strip()]
    if not cleaned:
        return 0.0

    sims = [_pair_similarity(baseline_text, variant) for variant in cleaned]
    return _clip01(_safe_mean(sims))


def compute_drift_score(baseline_text: str, variants: List[str]) -> float:
    omega = compute_omega_score(baseline_text, variants)
    return _clip01(1.0 - omega)


def compute_sei_score(omega_score: float, variants: List[str]) -> float:
    if not isinstance(variants, list):
        raise TypeError("variants must be a list")

    cleaned = [v for v in variants if isinstance(v, str) and v.strip()]
    n = len(cleaned)

    diversity_bonus = min(max(n - 1, 0), 4) / 4.0
    score = 0.8 * float(omega_score) + 0.2 * diversity_bonus
    return _clip01(score)


def compute_iri_score(omega_score: float, drift_score: float) -> float:
    omega_penalty = 1.0 - float(omega_score)
    score = 0.5 * float(drift_score) + 0.5 * omega_penalty
    return _clip01(score)