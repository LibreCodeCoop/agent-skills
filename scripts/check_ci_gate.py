#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 LibreCode Coop and contributors
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Fail closed on every mandatory job result of ONE GitHub Actions workflow.

This script does not query other workflow runs or publish checks. GitHub's
`needs` graph and the commit-specific workflow run determine the scope.
"""

from __future__ import annotations

import json
import os
import sys

REQUIRED_JOBS = (
    "package", "reuse", "workflow-policy", "actionlint", "zizmor", "secrets", "commit-policy"
)


def evaluate(needs: dict[str, dict], event: str) -> list[str]:
    if event not in {"push", "pull_request"}:
        return [f"unsupported event {event!r}"]
    errors = []
    for name in REQUIRED_JOBS:
        result = needs.get(name, {}).get("result")
        if result == "success":
            continue
        if name == "commit-policy" and event == "push" and result == "skipped":
            continue
        errors.append(f"{name}: expected success, got {result!r}")
    unknown = set(needs) - set(REQUIRED_JOBS)
    if unknown:
        errors.append(f"untracked dependencies: {', '.join(sorted(unknown))}")
    return errors


def main() -> int:
    try:
        needs = json.loads(os.environ["NEEDS_JSON"])
        event = os.environ["GITHUB_EVENT_NAME"]
        if not isinstance(needs, dict):
            raise ValueError("needs is not a JSON object")
        errors = evaluate(needs, event)
    except (KeyError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"invalid CI result inputs: {exc}", file=sys.stderr)
        return 1
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("All mandatory checks for this workflow run succeeded.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
