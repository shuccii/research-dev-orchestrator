#!/usr/bin/env python3
"""Validate the portable task-result contract without third-party dependencies."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED = {
    "status": str,
    "summary": str,
    "artifacts": list,
    "evidence": list,
    "risks": list,
    "next_actions": list,
    "verification": dict,
}
STATUSES = {"completed", "needs_revision", "blocked", "awaiting_approval"}


def fail(message: str) -> None:
    print(f"Invalid task result: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_task_result.py path/to/result.json")

    result_path = Path(sys.argv[1])
    try:
        data = json.loads(result_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(str(exc))

    if not isinstance(data, dict):
        fail("root must be an object")
    for key, expected_type in REQUIRED.items():
        if key not in data:
            fail(f"missing '{key}'")
        if not isinstance(data[key], expected_type):
            fail(f"'{key}' must be {expected_type.__name__}")
    if data["status"] not in STATUSES:
        fail("status is not a supported value")
    if not data["summary"].strip():
        fail("summary must not be empty")

    verification = data["verification"]
    for key in ("execution", "validity"):
        if not isinstance(verification.get(key), str) or not verification[key].strip():
            fail(f"verification.{key} must be a non-empty string")

    print(f"Valid task result: {result_path}")


if __name__ == "__main__":
    main()
