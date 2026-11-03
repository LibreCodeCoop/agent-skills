#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 LibreCode Coop and contributors
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Verify actionable workflow policy with the bundled Skill audit engine."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE / "skills/librecode-project-bootstrap/scripts"))
from audit_project import inspect_workflow  # noqa: E402


def check(root: Path) -> list[str]:
    errors = []
    workflows = sorted((root / ".github/workflows").glob("*.yml"))
    workflows += sorted((root / ".github/workflows").glob("*.yaml"))
    if not workflows:
        return ["no workflows found"]
    for path in workflows:
        errors.extend(f"{f.evidence}: {f.message}" for f in inspect_workflow(path, root) if f.status == "FAIL")
        text = path.read_text(encoding="utf-8")
        if "permissions:" not in text or "contents: read" not in text:
            errors.append(f"{path.name}: missing explicit least-privilege contents: read")
        if "pull_request_target:" in text:
            errors.append(f"{path.name}: pull_request_target needs separate security review")
    return errors


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("root", nargs="?", type=Path, default=BASE)
    args = p.parse_args()
    findings = check(args.root.resolve())
    if findings:
        print("\n".join(findings), file=sys.stderr)
        return 1
    print("Workflow policy checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
