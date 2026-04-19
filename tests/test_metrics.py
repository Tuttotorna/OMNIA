from omnia.metrics import (
    compute_drift_score,
    compute_iri_score,
    compute_omega_score,
    compute_sei_score,
)


def test_compute_omega_score_is_bounded() -> None:
    baseline = "The answer is 4."
    variants = ["4", "The answer is 4", "Answer: 4"]

    score = compute_omega_score(baseline, variants)

    assert isinstance(score, float)
    assert 0.0 <= score <= 1.0


def test_compute_omega_score_is_high_for_close_variants() -> None:
    baseline = "The answer is 4."
    variants = ["The answer is 4", "Answer: 4", "4"]

    score = compute_omega_score(baseline, variants)

    assert score > 0.4


def test_compute_drift_score_is_bounded() -> None:
    baseline = "The answer is 4."
    variants = ["4", "The answer is 4", "Answer: 4"]

    score = compute_drift_score(baseline, variants)

    assert isinstance(score, float)
    assert 0.0 <= score <= 1.0


def test_compute_drift_score_matches_omega_complement() -> None:
    baseline = "The answer is 4."
    variants = ["4", "The answer is 4", "Answer: 4"]

    omega = compute_omega_score(baseline, variants)
    drift = compute_drift_score(baseline, variants)

    assert abs(drift - (1.0 - omega)) < 1e-9


def test_compute_sei_score_is_bounded() -> None:
    variants = ["The answer is 4.", "The answer is 4", "Answer: 4", "4"]

    score = compute_sei_score(omega_score=0.7, variants=variants)

    assert isinstance(score, float)
    assert 0.0 <= score <= 1.0


def test_compute_sei_score_increases_with_more_variants() -> None:
    few = ["The answer is 4."]
    many = ["The answer is 4.", "The answer is 4", "Answer: 4", "4"]

    sei_few = compute_sei_score(omega_score=0.7, variants=few)
    sei_many = compute_sei_score(omega_score=0.7, variants=many)

    assert sei_many >= sei_few


def test_compute_iri_score_is_bounded() -> None:
    score = compute_iri_score(omega_score=0.6, drift_score=0.4)

    assert isinstance(score, float)
    assert 0.0 <= score <= 1.0


def test_compute_iri_score_rises_when_omega_is_low_and_drift_is_high() -> None:
    low_quality = compute_iri_score(omega_score=0.2, drift_score=0.8)
    better_quality = compute_iri_score(omega_score=0.8, drift_score=0.2)

    assert low_quality > better_quality


def test_compute_omega_score_returns_zero_for_empty_variants() -> None:
    score = compute_omega_score("The answer is 4.", [])
    assert score == 0.0