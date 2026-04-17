from omnia import evaluate_structural_profile


def test_clean_admissible_profile() -> None:
    result = evaluate_structural_profile(
        omega_score=0.84,
        sei_score=0.77,
        iri_score=0.12,
        drift_score=0.15,
    )

    assert result.gate_status == "GO"
    assert result.reason_code == "stable"
    assert result.limit_triggered is False


def test_surface_ok_but_fragile_profile() -> None:
    result = evaluate_structural_profile(
        omega_score=0.58,
        sei_score=0.55,
        iri_score=0.31,
        drift_score=0.57,
    )

    assert result.gate_status == "RISK"
    assert result.reason_code == "high_drift"
    assert result.limit_triggered is False


def test_continuation_not_admissible_profile() -> None:
    result = evaluate_structural_profile(
        omega_score=0.43,
        sei_score=0.16,
        iri_score=0.44,
        drift_score=0.49,
    )

    assert result.gate_status == "NO_GO"
    assert result.reason_code == "limit_reached"
    assert result.limit_triggered is True


def test_collapsed_profile() -> None:
    result = evaluate_structural_profile(
        omega_score=0.18,
        sei_score=0.09,
        iri_score=0.87,
        drift_score=0.82,
    )

    assert result.gate_status == "UNSTABLE"
    assert result.reason_code == "collapsed_profile"
    assert result.limit_triggered is True


def test_high_drift_block_profile() -> None:
    result = evaluate_structural_profile(
        omega_score=0.47,
        sei_score=0.45,
        iri_score=0.28,
        drift_score=0.74,
    )

    assert result.gate_status == "NO_GO"
    assert result.reason_code == "high_drift"
    assert result.limit_triggered is False


def test_extractability_exhausted_profile() -> None:
    result = evaluate_structural_profile(
        omega_score=0.52,
        sei_score=0.12,
        iri_score=0.33,
        drift_score=0.34,
    )

    assert result.gate_status == "NO_GO"
    assert result.reason_code == "limit_reached"
    assert result.limit_triggered is True