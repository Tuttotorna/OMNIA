"""
Rebuild all frozen OMNIA mini-result JSONL artifacts.

Run:
  python examples/rebuild_all_results.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


RUNNER = Path("examples/run_profiles_jsonl.py")

JOBS = [
    (
        Path("examples/demo_profiles.jsonl"),
        Path("examples/demo_profiles_results.jsonl"),
    ),
    (
        Path("examples/surface_ok_cases.jsonl"),
        Path("examples/surface_ok_results.jsonl"),
    ),
    (
        Path("examples/llm_surface_cases.jsonl"),
        Path("examples/llm_surface_results.jsonl"),
    ),
    (
        Path("examples/support_response_cases.jsonl"),
        Path("examples/support_response_results.jsonl"),
    ),
]


def run_job(input_path: Path, output_path: Path) -> None:
    if not input_path.exists():
        raise FileNotFoundError(f"Missing input file: {input_path}")

    if not RUNNER.exists():
        raise FileNotFoundError(f"Missing runner file: {RUNNER}")

    cmd = [
        sys.executable,
        str(RUNNER),
        str(input_path),
        "-o",
        str(output_path),
    ]

    subprocess.run(cmd, check=True)


def main() -> int:
    print("-" * 40)
    print("OMNIA REBUILD ALL RESULTS")
    print("-" * 40)

    for input_path, output_path in JOBS:
        print(f"rebuilding: {input_path} -> {output_path}")
        run_job(input_path, output_path)

    print("-" * 40)
    print("all frozen result artifacts rebuilt")
    print("-" * 40)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())