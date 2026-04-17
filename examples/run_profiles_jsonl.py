from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from omnia import evaluate_structural_profile


REQUIRED_FIELDS = (
    "omega_score",
    "sei_score",
    "iri_score",
    "drift_score",
)


def validate_record(record: dict[str, Any], line_number: int) -> None:
    missing = [field for field in REQUIRED_FIELDS if field not in record]
    if missing:
        missing_str = ", ".join(missing)
        raise ValueError(
            f"Line {line_number}: missing required fields: {missing_str}"
        )


def enrich_record(record: dict[str, Any]) -> dict[str, Any]:
    result = evaluate_structural_profile(
        omega_score=record["omega_score"],
        sei_score=record["sei_score"],
        iri_score=record["iri_score"],
        drift_score=record["drift_score"],
    )

    return {
        **record,
        **result.to_dict(),
    }


def process_jsonl(input_path: Path, output_path: Path | None = None) -> int:
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    output_stream = None
    should_close = False

    try:
        if output_path is None:
            output_stream = sys.stdout
        else:
            output_stream = output_path.open("w", encoding="utf-8")
            should_close = True

        with input_path.open("r", encoding="utf-8") as infile:
            for line_number, raw_line in enumerate(infile, start=1):
                stripped = raw_line.strip()

                if not stripped:
                    continue

                try:
                    record = json.loads(stripped)
                except json.JSONDecodeError as exc:
                    raise ValueError(
                        f"Line {line_number}: invalid JSON: {exc.msg}"
                    ) from exc

                if not isinstance(record, dict):
                    raise ValueError(
                        f"Line {line_number}: JSON record must be an object"
                    )

                validate_record(record, line_number)
                enriched = enrich_record(record)

                output_stream.write(json.dumps(enriched) + "\n")

        return 0

    finally:
        if should_close and output_stream is not None:
            output_stream.close()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run OMNIA CORE v1 on JSONL structural profiles."
    )
    parser.add_argument(
        "input",
        type=Path,
        help="Path to input JSONL file.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Optional path to output JSONL file. Defaults to stdout.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        return process_jsonl(args.input, args.output)
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())