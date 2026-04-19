from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List

from omnia import run_omnia


DATASET_PATH = Path("data/support_screening_external_v2.jsonl")
OUTPUT_PATH = Path("examples/support_screening_external_v2_omnia_results.jsonl")


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                items.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on line {line_no} of {path}: {exc}") from exc
    return items


def _normalize_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _strip_politeness(text: str) -> str:
    patterns = [
        r"\bthank you for (contacting us|your message|reaching out)\b[,. ]*",
        r"\bwe understand (your concern|your frustration|how important this is)\b[,. ]*",
        r"\bwe are sorry for the inconvenience\b[,. ]*",
        r"\bwe appreciate your patience\b[,. ]*",
        r"\byour issue is important to us\b[,. ]*",
        r"\band we are here to help\b[,. ]*",
    ]
    out = text
    for pattern in patterns:
        out = re.sub(pattern, "", out, flags=re.IGNORECASE)
    return _normalize_spaces(out.strip(" ,.-"))


def _first_sentence(text: str) -> str:
    parts = re.split(r"(?<=[.!?])\s+", _normalize_spaces(text))
    return parts[0].strip() if parts and parts[0].strip() else _normalize_spaces(text)


def _content_only(text: str) -> str:
    text = _strip_politeness(text)
    text = re.sub(r"\bplease\b", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\bkindly\b", "", text, flags=re.IGNORECASE)
    return _normalize_spaces(text.strip(" ,.-"))


def _compressed(text: str) -> str:
    text = _content_only(text)
    replacements = {
        "your order is currently in transit and should arrive soon": "order in transit",
        "refunds can take a few business days to appear depending on your bank": "refund delay depends on bank",
        "your account has been locked due to unusual activity": "account locked",
        "please reset your password to regain access": "reset password",
        "your shipment may be delayed in transit": "shipment delayed",
        "please allow a little more time and check tracking again soon": "wait and check tracking",
        "your request is being reviewed and we will update you as soon as possible": "request under review",
        "please confirm that your phone number or email is correct and request a new code": "check contact info and request new code",
        "if the issue continues, contact support for manual verification": "contact support for manual verification",
        "please contact support": "contact support",
        "please check again later": "check later",
        "please check tracking again later": "check tracking later",
        "please monitor tracking again later": "monitor tracking later",
    }
    lowered = text.lower()
    for src, dst in replacements.items():
        lowered = lowered.replace(src, dst)
    return _normalize_spaces(lowered)


def _remove_actionability(text: str) -> str:
    out = re.sub(
        r"\b(please|check again soon|check again later|contact support again if it still cannot be found|"
        r"reset your password to regain access|try again|allow a little more time|"
        r"check tracking again soon|check tracking again later|monitor tracking again later|"
        r"contact support for manual verification|contact support if there is still no movement|"
        r"contact support if the issue continues|contact support to check the available options)\b[,. ]*",
        "",
        text,
        flags=re.IGNORECASE,
    )
    return _normalize_spaces(out.strip(" ,.-"))


def _prompt_response_minimal(prompt: str, response: str) -> str:
    return _normalize_spaces(f"{prompt.strip()} {_content_only(response)}")


def build_case(item: Dict[str, Any]) -> Dict[str, Any]:
    prompt = item["prompt"]
    response = item["response"]
    text = _normalize_spaces(response)

    variants = [
        text,
        text.lower(),
        _first_sentence(text),
        _strip_politeness(text),
        _content_only(text),
        _compressed(text),
        _remove_actionability(text),
        _prompt_response_minimal(prompt, text),
    ]

    cleaned: List[str] = []
    seen = set()
    for v in variants:
        v = _normalize_spaces(v)
        if v and v not in seen:
            seen.add(v)
            cleaned.append(v)

    return {
        "case_id": item["case_id"],
        "text": text,
        "variants": cleaned,
    }


def to_result(item: Dict[str, Any]) -> Dict[str, Any]:
    case = build_case(item)
    omnia_result = run_omnia(case)

    return {
        "case_id": item["case_id"],
        "source": item["source"],
        "prompt": item["prompt"],
        "response": item["response"],
        "label": item["label"],
        "omega_score": omnia_result["omega_score"],
        "sei_score": omnia_result["sei_score"],
        "iri_score": omnia_result["iri_score"],
        "drift_score": omnia_result["drift_score"],
        "limit_triggered": omnia_result["limit_triggered"],
        "gate_status": omnia_result["gate_status"],
        "reason_code": omnia_result["reason_code"],
    }


def save_jsonl(path: Path, rows: Iterable[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def summarize(rows: List[Dict[str, Any]]) -> Dict[str, int]:
    summary: Dict[str, int] = {}
    for row in rows:
        gate = row["gate_status"]
        summary[gate] = summary.get(gate, 0) + 1
    return dict(sorted(summary.items()))


def main() -> None:
    items = load_jsonl(DATASET_PATH)
    results = [to_result(item) for item in items]
    save_jsonl(OUTPUT_PATH, results)

    summary = summarize(results)

    print(f"Loaded: {len(items)} cases")
    print(f"Wrote: {OUTPUT_PATH}")
    print("OMNIA gate distribution:")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()