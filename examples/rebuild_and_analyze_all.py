"""
Rebuild and analyze all frozen OMNIA mini-result artifacts.

Run:
  python examples/rebuild_and_analyze_all.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


PYTHON = sys.executable

REBUILD_SCRIPT = Path("examples/rebuild_all_results.py")
GENERIC_ANALYZER = Path("examples/analyze_results.py")
SURFACE_OK_ANALYZER = Path("examples/analyze_surface_ok_results.py")
LLM_ANALYZER = Path("examples/analyze_llm_surface_results.py")
SUPPORT_ANALYZER = Path("examples/analyze_support_response_results.py")
RAG_ANALYZER = Path("examples/analyze_rag_answer_results.py")

RESULT_FILES = [
    Path("examples/demo_profiles_results.jsonl"),
    Path("examples/surface_ok_results.jsonl"),
    Path("examples/llm_surface_results.jsonl"),
    Path("examples/support_response_results.jsonl"),
    Path("examples/rag_answer_results.jsonl"),
]


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def ensure_exists(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path}")


def main() -> int:
    ensure_exists(REBUILD_SCRIPT)
    ensure_exists(GENERIC_ANALYZER)
    ensure_exists(SURFACE_OK_ANALYZER)
    ensure_exists(LLM_ANALYZER)
    ensure_exists(SUPPORT_ANALYZER)
    ensure_exists(RAG_ANALYZER)

    print("=" * 48)
    print("OMNIA REBUILD AND ANALYZE ALL")
    print("=" * 48)

    print("\n[1/4] Rebuilding frozen result artifacts")
    run([PYTHON, str(REBUILD_SCRIPT)])

    print("\n[2/4] Verifying rebuilt result files")
    for result_file in RESULT_FILES:
        ensure_exists(result_file)
        print(f"- ok: {result_file}")

    print("\n[3/4] Running generic analyzer on all frozen results")
    for result_file in RESULT_FILES:
        print("-" * 48)
        print(f"ANALYZING: {result_file}")
        print("-" * 48)
        run([PYTHON, str(GENERIC_ANALYZER), "--input", str(result_file)])

    print("\n[4/4] Running domain-specific analyzers")

    print("-" * 48)
    print("ANALYZING: examples/surface_ok_results.jsonl (surface-ok-specific)")
    print("-" * 48)
    run([PYTHON, str(SURFACE_OK_ANALYZER)])

    print("-" * 48)
    print("ANALYZING: examples/llm_surface_results.jsonl (LLM-specific)")
    print("-" * 48)
    run([PYTHON, str(LLM_ANALYZER)])

    print("-" * 48)
    print("ANALYZING: examples/support_response_results.jsonl (support-specific)")
    print("-" * 48)
    run([PYTHON, str(SUPPORT_ANALYZER)])

    print("-" * 48)
    print("ANALYZING: examples/rag_answer_results.jsonl (RAG-specific)")
    print("-" * 48)
    run([PYTHON, str(RAG_ANALYZER)])

    print("=" * 48)
    print("DONE: all frozen result artifacts rebuilt and analyzed")
    print("=" * 48)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())