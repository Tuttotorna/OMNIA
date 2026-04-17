from __future__ import annotations

from dataclasses import dataclass, asdict
import json


@dataclass
class OmniaResult:
    omega_score: float
    sei_score: float
    iri_score: float
    drift_score: float
    limit_triggered: bool
    gate_status: str
    reason_code: str


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, value))


def compute_limit_triggered(
    omega_score: float,
    sei_score: float,
    iri_score: float,
    drift_score: float,
) -> bool:
    exhaustion_boundary = sei_score < 0.20
    critical_irreversible_loss = iri_score >= 0.75
    collapse_tendency = (
        omega_score < 0.30
        and (
            drift_score >= 0.70
            or iri_score >= 0.50
            or sei_score < 0.40
        )
    )
    explicit_collapse_profile = (
        omega_score < 0.30 and drift_score >= 0.70 and iri_score >= 0.50
    )
    return (
        exhaustion_boundary
        or critical_irreversible_loss
        or collapse_tendency
        or explicit_collapse_profile
    )


def select_reason_code(
    omega_score: float,
    sei_score: float,
    iri_score: float,
    drift_score: float,
    limit_triggered: bool,
    gate_status: str,
) -> str:
    # Severity priority:
    # collapsed_profile > limit_reached > irreversible_loss
    # > high_drift > low_extractability > fragile > stable

    if gate_status == "GO":
        return "stable"

    if gate_status == "UNSTABLE":
        if omega_score < 0.30 and drift_score >= 0.70 and iri_score >= 0.50:
            return "collapsed_profile"
        if iri_score >= 0.75:
            return "irreversible_loss"
        if limit_triggered:
            return "limit_reached"
        return "collapsed_profile"

    if gate_status == "NO_GO":
        if limit_triggered:
            if omega_score < 0.30 and drift_score >= 0.70 and iri_score >= 0.50:
                return "collapsed_profile"
            if iri_score >= 0.75:
                return "irreversible_loss"
            return "limit_reached"
        if iri_score >= 0.50:
            return "irreversible_loss"
        if drift_score >= 0.70:
            return "high_drift"
        return "low_extractability"

    # gate_status == "RISK"
    if drift_score >= 0.50:
        return "high_drift"
    if sei_score < 0.70:
        return "low_extractability"
    return "fragile"


def compute_gate_status(
    omega_score: float,
    sei_score: float,
    iri_score: float,
    drift_score: float,
    limit_triggered: bool,
) -> str:
    # GO
    if (
        not limit_triggered
        and omega_score >= 0.75
        and sei_score >= 0.70
        and iri_score < 0.25
        and drift_score < 0.25
    ):
        return "GO"

    # UNSTABLE has strongest priority
    if (
        omega_score < 0.30
        or iri_score >= 0.75
        or (drift_score >= 0.70 and omega_score < 0.50)
        or (
            limit_triggered
            and omega_score < 0.30
            and (iri_score >= 0.50 or drift_score >= 0.70)
        )
    ):
        return "UNSTABLE"

    # NO_GO
    if (
        limit_triggered
        or sei_score < 0.20
        or drift_score >= 0.70
        or iri_score >= 0.50
    ):
        return "NO_GO"

    # Otherwise admissible but weakened
    return "RISK"


def evaluate_case(
    omega_score: float,
    sei_score: float,
    iri_score: float,
    drift_score: float,
) -> OmniaResult:
    omega_score = clamp01(omega_score)
    sei_score = clamp01(sei_score)
    iri_score = clamp01(iri_score)
    drift_score = clamp01(drift_score)

    limit_triggered = compute_limit_triggered(
        omega_score=omega_score,
        sei_score=sei_score,
        iri_score=iri_score,
        drift_score=drift_score,
    )

    gate_status = compute_gate_status(
        omega_score=omega_score,
        sei_score=sei_score,
        iri_score=iri_score,
        drift_score=drift_score,
        limit_triggered=limit_triggered,
    )

    reason_code = select_reason_code(
        omega_score=omega_score,
        sei_score=sei_score,
        iri_score=iri_score,
        drift_score=drift_score,
        limit_triggered=limit_triggered,
        gate_status=gate_status,
    )

    return OmniaResult(
        omega_score=omega_score,
        sei_score=sei_score,
        iri_score=iri_score,
        drift_score=drift_score,
        limit_triggered=limit_triggered,
        gate_status=gate_status,
        reason_code=reason_code,
    )


def main() -> None:
    # Minimal bounded demo profile:
    # superficially acceptable but structurally weakened
    result = evaluate_case(
        omega_score=0.58,
        sei_score=0.55,
        iri_score=0.31,
        drift_score=0.57,
    )

    print("OMNIA CORE v1 quick smoke test")
    print(json.dumps(asdict(result), indent=2))
    print("OK: OMNIA core executed")


if __name__ == "__main__":
    main()