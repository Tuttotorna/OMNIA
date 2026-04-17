from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


_ALLOWED_GATE_STATUSES = {"GO", "RISK", "NO_GO", "UNSTABLE"}
_ALLOWED_REASON_CODES = {
    "stable",
    "fragile",
    "high_drift",
    "low_extractability",
    "irreversible_loss",
    "limit_reached",
    "collapsed_profile",
}


@dataclass(frozen=True)
class OmniaResult:
    omega_score: float
    sei_score: float
    iri_score: float
    drift_score: float
    limit_triggered: bool
    gate_status: str
    reason_code: str

    def to_dict(self) -> Dict[str, float | bool | str]:
        return {
            "omega_score": self.omega_score,
            "sei_score": self.sei_score,
            "iri_score": self.iri_score,
            "drift_score": self.drift_score,
            "limit_triggered": self.limit_triggered,
            "gate_status": self.gate_status,
            "reason_code": self.reason_code,
        }


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, float(value)))


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


def compute_gate_status(
    omega_score: float,
    sei_score: float,
    iri_score: float,
    drift_score: float,
    limit_triggered: bool,
) -> str:
    if (
        not limit_triggered
        and omega_score >= 0.75
        and sei_score >= 0.70
        and iri_score < 0.25
        and drift_score < 0.25
    ):
        return "GO"

    # UNSTABLE only for genuine collapse-level conditions
    if (
        omega_score < 0.30
        or iri_score >= 0.75
        or (
            limit_triggered
            and omega_score < 0.30
            and (iri_score >= 0.50 or drift_score >= 0.70)
        )
    ):
        return "UNSTABLE"

    # NO_GO for blocking but non-collapsed conditions
    if (
        limit_triggered
        or sei_score < 0.20
        or drift_score >= 0.70
        or iri_score >= 0.50
    ):
        return "NO_GO"

    return "RISK"


def select_reason_code(
    omega_score: float,
    sei_score: float,
    iri_score: float,
    drift_score: float,
    limit_triggered: bool,
    gate_status: str,
) -> str:
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

    if drift_score >= 0.50:
        return "high_drift"
    if sei_score < 0.70:
        return "low_extractability"
    return "fragile"


def evaluate_structural_profile(
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

    if gate_status not in _ALLOWED_GATE_STATUSES:
        raise ValueError(f"Invalid gate_status produced: {gate_status}")

    reason_code = select_reason_code(
        omega_score=omega_score,
        sei_score=sei_score,
        iri_score=iri_score,
        drift_score=drift_score,
        limit_triggered=limit_triggered,
        gate_status=gate_status,
    )

    if reason_code not in _ALLOWED_REASON_CODES:
        raise ValueError(f"Invalid reason_code produced: {reason_code}")

    return OmniaResult(
        omega_score=omega_score,
        sei_score=sei_score,
        iri_score=iri_score,
        drift_score=drift_score,
        limit_triggered=limit_triggered,
        gate_status=gate_status,
        reason_code=reason_code,
    )