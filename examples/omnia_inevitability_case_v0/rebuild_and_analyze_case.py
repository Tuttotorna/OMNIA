"""
Rebuild and analyze OMNIA inevitability case v0.

Run:
    python examples/omnia_inevitability_case_v0/rebuild_and_analyze_case.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


BASE_DIR = Path("examples/omnia_inevitability_case_v0")

REBUILD_SCRIPT = BASE_DIR / "rebuild_case_outputs.py"
ANALYZE_SCRIPT = BASE_DIR / "analyze_case.py"

REQUIRED_FILES = [
    BASE_DIR / "README.md",
    BASE_DIR / "baseline_results.jsonl",
    BASE_DIR / "omnia_scores.jsonl",
    BASE_DIR / "metrics.md",
]


def ensure_exists(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path}")


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def main() -> int:
    for path in REQUIRED_FILES:
        ensure_exists(path)

    ensure_exists(REBUILD_SCRIPT)
    ensure_exists(ANALYZE_SCRIPT)

    print("=" * 56)
    print("OMNIA INEVITABILITY CASE V0 - REBUILD AND ANALYZE")
    print("=" * 56)

    print("\n[1/3] Rebuilding derived artifacts")
    run([sys.executable, str(REBUILD_SCRIPT)])

    print("\n[2/3] Verifying derived artifacts")
    ensure_exists(BASE_DIR / "gate_actions.jsonl")
    ensure_exists(BASE_DIR / "final_results.jsonl")
    print(f"- ok: {BASE_DIR / 'gate_actions.jsonl'}")
    print(f"- ok: {BASE_DIR / 'final_results.jsonl'}")

    print("\n[3/3] Running case analysis")
    run([sys.executable, str(ANALYZE_SCRIPT)])

    print("=" * 56)
    print("DONE: inevitability case rebuilt and analyzed")
    print("=" * 56)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())