from __future__ import annotations

import re
from typing import List


def _normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _strip_terminal_punctuation(text: str) -> str:
    return text.rstrip(" .,!?:;")


def _lowercase(text: str) -> str:
    return text.lower()


def _collapse_answer_prefix(text: str) -> str:
    lowered = text.lower().strip()

    prefixes = (
        "answer:",
        "the answer is",
        "final answer:",
        "result:",
    )

    for prefix in prefixes:
        if lowered.startswith(prefix):
            stripped = text[len(prefix):].strip(" \t:-")
            return stripped.strip()

    return text.strip()


def _dedupe_preserve_order(items: List[str]) -> List[str]:
    seen = set()
    out: List[str] = []

    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)

    return out


def build_variants(text: str) -> List[str]:
    """
    Build a minimal deterministic set of bounded structural variants.

    Rules:
    - no semantics
    - no external models
    - no randomness
    - only explicit surface transformations
    """
    if not isinstance(text, str):
        raise TypeError(f"text must be a string, got {type(text).__name__}")

    base = text.strip()
    if not base:
        return []

    variants = [
        base,
        _normalize_whitespace(base),
        _strip_terminal_punctuation(base),
        _lowercase(base),
        _normalize_whitespace(_lowercase(base)),
        _collapse_answer_prefix(base),
        _strip_terminal_punctuation(_collapse_answer_prefix(base)),
        _normalize_whitespace(_collapse_answer_prefix(base)),
    ]

    cleaned = [v.strip() for v in variants if isinstance(v, str) and v.strip()]
    return _dedupe_preserve_order(cleaned)