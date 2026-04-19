from __future__ import annotations


def compute_limit_triggered(
    omega_score: float,
    sei_score: float,
    iri_score: float,
    drift_score: float,
) -> bool:
    """
    Minimal bounded limit logic for OMNIA core.

    A limit is triggered when structural continuation is no longer
    admissible inside the tested bounded space.
    """
    omega = float(omega_score)
    sei = float(sei_score)
    iri = float(iri_score)
    drift = float(drift_score)

    if omega < 0.35:
        return True
    if sei < 0.25:
        return True
    if iri > 0.75:
        return True
    if drift > 0.80:
        return True

    return False


def compute_gate_status(
    omega_score: float,
    sei_score: float,
    iri_score: float,
    drift_score: float,
    limit_triggered: bool,
) -> str:
    """
    Canonical bounded gate conversion.

    Allowed outputs:
    - GO
    - RISK
    - NO_GO
    - UNSTABLE
    """
    omega = float(omega_score)
    sei = float(sei_score)
    iri = float(iri_score)
    drift = float(drift_score)

    if limit_triggered:
        if omega < 0.20 or iri > 0.90 or drift > 0.90:
            return "UNSTABLE"
        return "NO_GO"

    if omega >= 0.75 and sei >= 0.50 and iri <= 0.40 and drift <= 0.35:
        return "GO"

    return "RISK"


def compute_reason_code(
    omega_score: float,
    sei_score: float,
    iri_score: float,
    drift_score: float,
    limit_triggered: bool,
    gate_status: str,
) -> str:
    """
    Return a bounded machine-readable structural reason.
    """
    omega = float(omega_score)
    sei = float(sei_score)
    iri = float(iri_score)
    drift = float(drift_score)

    if gate_status == "UNSTABLE":
        if drift > 0.90:
            return "profile_collapse"
        if iri > 0.90:
            return "high_iri"
        return "unstable_profile"

    if gate_status == "NO_GO":
        if omega < 0.35:
            return "low_omega"
        if sei < 0.25:
            return "limit_exhaustion"
        if iri > 0.75:
            return "high_iri"
        if drift > 0.80:
            return "high_drift"
        if limit_triggered:
            return "limit_triggered"
        return "no_go_profile"

    if gate_status == "GO":
        return "stable_profile"

    if drift > 0.55:
        return "high_drift"
    if omega < 0.60:
        return "low_omega"
    if iri > 0.45:
        return "high_iri"
    if sei < 0.45:
        return "low_sei"

    return "moderate_fragility"