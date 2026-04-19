from omnia.limits import (
    compute_gate_status,
    compute_limit_triggered,
    compute_reason_code,
)


def test_compute_limit_triggered_false_for_stable_profile() -> None:
    triggered = compute_limit_triggered(
        omega_score=0.82,
        sei_score=0.71,
        iri_score=0.18,
        drift_score=0.22,
    )

    assert triggered is False


def test_compute_limit_triggered_true_for_low_omega() -> None:
    triggered = compute_limit_triggered(
        omega_score=0.20,
        sei_score=0.60,
        iri_score=0.30,
        drift_score=0.40,
    )

    assert triggered is True


def test_compute_limit_triggered_true_for_low_sei() -> None:
    triggered = compute_limit_triggered(
        omega_score=0.60,
        sei_score=0.10,
        iri_score=0.30,
        drift_score=0.40,
    )

    assert triggered is True


def test_compute_limit_triggered_true_for_high_iri() -> None:
    triggered = compute_limit_triggered(
        omega_score=0.60,
        sei_score=0.60,
        iri_score=0.90,
        drift_score=0.40,
    )

    assert triggered is True


def test_compute_limit_triggered_true_for_high_drift() -> None:
    triggered = compute_limit_triggered(
        omega_score=0.60,
        sei_score=0.60,
        iri_score=0.30,
        drift_score=0.95,
    )

    assert triggered is True


def test_compute_gate_status_go_for_stable_profile() -> None:
    status = compute_gate_status(
        omega_score=0.85,
        sei_score=0.65,
        iri_score=0.20,
        drift_score=0.20,
        limit_triggered=False,
    )

    assert status == "GO"


def test_compute_gate_status_risk_for_non_limit_but_not_go_profile() -> None:
    status = compute_gate_status(
        omega_score=0.58,
        sei_score=0.50,
        iri_score=0.32,
        drift_score=0.57,
        limit_triggered=False,
    )

    assert status == "RISK"


def test_compute_gate_status_no_go_when_limit_triggered() -> None:
    status = compute_gate_status(
        omega_score=0.30,
        sei_score=0.40,
        iri_score=0.60,
        drift_score=0.50,
        limit_triggered=True,
    )

    assert status == "NO_GO"


def test_compute_gate_status_unstable_for_extreme_profile() -> None:
    status = compute_gate_status(
        omega_score=0.10,
        sei_score=0.10,
        iri_score=0.95,
        drift_score=0.95,
        limit_triggered=True,
    )

    assert status == "UNSTABLE"


def test_compute_reason_code_stable_profile() -> None:
    code = compute_reason_code(
        omega_score=0.85,
        sei_score=0.65,
        iri_score=0.20,
        drift_score=0.20,
        limit_triggered=False,
        gate_status="GO",
    )

    assert code == "stable_profile"


def test_compute_reason_code_high_drift_for_risk() -> None:
    code = compute_reason_code(
        omega_score=0.58,
        sei_score=0.55,
        iri_score=0.31,
        drift_score=0.57,
        limit_triggered=False,
        gate_status="RISK",
    )

    assert code == "high_drift"


def test_compute_reason_code_low_omega_for_no_go() -> None:
    code = compute_reason_code(
        omega_score=0.20,
        sei_score=0.40,
        iri_score=0.50,
        drift_score=0.40,
        limit_triggered=True,
        gate_status="NO_GO",
    )

    assert code == "low_omega"


def test_compute_reason_code_profile_collapse_for_unstable() -> None:
    code = compute_reason_code(
        omega_score=0.10,
        sei_score=0.10,
        iri_score=0.80,
        drift_score=0.95,
        limit_triggered=True,
        gate_status="UNSTABLE",
    )

    assert code == "profile_collapse"