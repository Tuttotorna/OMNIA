from __future__ import annotations

from typing import Any, Dict, List

from omnia.limits import compute_gate_status, compute_limit_triggered, compute_reason_code
from omnia.metrics import compute_drift_score, compute_iri_score, compute_omega_score, compute_sei_score
from omnia.transforms import build_variants


def _extract_text(case: Dict[str, Any]) -> str:
    text = case.get("text", "")
    if not isinstance(text, str):
        raise TypeError(f"case['text'] must be a string, got {type(text).__name__}")
    text = text.strip()
    if not text:
        raise ValueError("case['text'] must be a non-empty string")
    return text


def _extract_variants(case: Dict[str, Any], baseline_text: str) -> List[str]:
    variants = case.get("variants", [])

    if variants is None:
        variants = []

    if not isinstance(variants, list):
        raise TypeError(f"case['variants'] must be a list, got {type(variants).__name__}")

    cleaned: List[str] = []
    for idx, item in enumerate(variants):
        if not isinstance(item, str):
            raise TypeError(
                f"case['variants'][{idx}] must be a string, got {type(item).__name__}"
            )
        item = item.strip()
        if item:
            cleaned.append(item)

    generated = build_variants(baseline_text)
    for item in generated:
        if item not in cleaned:
            cleaned.append(item)

    if baseline_text not in cleaned:
        cleaned.insert(0, baseline_text)

    return cleaned


def run_omnia(case: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(case, dict):
        raise TypeError(f"case must be a dict, got {type(case).__name__}")

    baseline_text = _extract_text(case)
    variants = _extract_variants(case, baseline_text)

    omega_score = compute_omega_score(baseline_text, variants)
    sei_score = compute_sei_score(omega_score=omega_score, variants=variants)
    drift_score = compute_drift_score(baseline_text, variants)
    iri_score = compute_iri_score(omega_score=omega_score, drift_score=drift_score)

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

    reason_code = compute_reason_code(
        omega_score=omega_score,
        sei_score=sei_score,
        iri_score=iri_score,
        drift_score=drift_score,
        limit_triggered=limit_triggered,
        gate_status=gate_status,
    )

    result: Dict[str, Any] = {
        "omega_score": round(float(omega_score), 6),
        "sei_score": round(float(sei_score), 6),
        "iri_score": round(float(iri_score), 6),
        "drift_score": round(float(drift_score), 6),
        "limit_triggered": bool(limit_triggered),
        "gate_status": str(gate_status),
        "reason_code": str(reason_code),
    }

    if "case_id" in case:
        result["case_id"] = case["case_id"]

    return result