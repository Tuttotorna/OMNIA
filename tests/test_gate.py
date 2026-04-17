from omnia.gate import evaluate_structural_profile


def test_go_case() -> None:
    result = evaluate_structural_profile(
        omega_score=0.84,
        sei_score=0.77,
        iri_score=0.12,
        drift_score=0.15,
    )

    assert result.limit_triggered is False
    assert result.gate_status == "GO"
    assert result.reason_code == "stable"


def test_risk_case() -> None:
    result = evaluate_structural_profile(
        omega_score=0.58,
        sei_score=0.55,
        iri_score=0.31,
        drift_score=0.57,
    )

    assert result.limit_triggered is False
    assert result.gate_status == "RISK"
    assert result.reason_code == "high_drift"


def test_no_go_case() -> None:
    result = evaluate_structural_profile(
        omega_score=0.43,
        sei_score=0.16,
        iri_score=0.44,
        drift_score=0.49,
    )

    assert result.limit_triggered is True
    assert result.gate_status == "NO_GO"
    assert result.reason_code == "limit_reached"


def test_unstable_case() -> None:
    result = evaluate_structural_profile(
        omega_score=0.18,
        sei_score=0.09,
        iri_score=0.87,
        drift_score=0.82,
    )

    assert result.limit_triggered is True
    assert result.gate_status == "UNSTABLE"
    assert result.reason_code == "collapsed_profile"