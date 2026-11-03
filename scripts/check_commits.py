#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 LibreCode Coop and contributors
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Enforce Conventional Commits, author-matching DCO and GitHub verified signatures."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from urllib import request

CONVENTIONAL = re.compile(
    r"^(?:build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)"
    r"(?:\([a-z0-9_.-]+\))?!?: [^\s].{2,}$"
)


def validate_message(author: str, email: str, message: str) -> list[str]:
    header = message.splitlines()[0] if message.splitlines() else ""
    failures = []
    if not CONVENTIONAL.fullmatch(header):
        failures.append("missing Conventional Commit subject")
    trailers = re.findall(r"(?im)^Signed-off-by:\s*(.+?)\s*<([^<>\s]+)>\s*$", message)
    if (author, email) not in trailers:
        failures.append("missing author-matching DCO Signed-off-by trailer")
    return failures


def verified_signature(commit_payload: dict) -> bool:
    return commit_payload.get("commit", {}).get("verification", {}).get("verified") is True


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True, help="Trusted base commit SHA")
    parser.add_argument("--head", required=True, help="Pull request head commit SHA")
    args = parser.parse_args()
    for value in (args.base, args.head):
        if re.fullmatch(r"[a-f0-9]{40}", value) is None:
            parser.error("base/head must be full 40-character commit SHAs")
    token = os.getenv("GITHUB_TOKEN", "")
    repository = os.getenv("GITHUB_REPOSITORY", "")
    if not token or re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository) is None:
        parser.error("GITHUB_TOKEN and GITHUB_REPOSITORY are required for GitHub signature verification")
    commits = git("rev-list", "--no-merges", f"{args.base}..{args.head}").splitlines()
    if not commits:
        print("No non-merge commits in PR", file=sys.stderr)
        return 1
    failures = []
    for sha in commits:
        author, email, *body = git("show", "-s", "--format=%an%n%ae%n%B", sha).splitlines()
        failures.extend(f"{sha[:12]}: {e}" for e in validate_message(author, email, "\n".join(body)))
        req = request.Request(
            f"https://api.github.com/repos/{repository}/commits/{sha}",
            headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json", "User-Agent": "librecode-agent-skills"},
        )
        try:
            with request.urlopen(req, timeout=15) as resp:
                commit = json.load(resp)
            if not verified_signature(commit):
                failures.append(f"{sha[:12]}: GitHub does not verify cryptographic commit signature")
        except (OSError, ValueError) as exc:
            failures.append(f"{sha[:12]}: signature check unavailable: {type(exc).__name__}")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"Conventional Commits, DCO and verified signatures: {len(commits)} commit(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
