# SPDX-FileCopyrightText: 2026 LibreCode Coop and contributors
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Executable contract for the plugin's own engineering and distribution rules."""

from __future__ import annotations

import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_ci_gate import REQUIRED_JOBS, evaluate  # noqa: E402
from check_commits import validate_message, verified_signature  # noqa: E402
from check_workflows import check  # noqa: E402


class PluginContractTest(unittest.TestCase):
    def test_manifest_and_both_marketplaces_are_consistent(self):
        manifest = json.loads((ROOT / "plugin.json").read_text())
        codex = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
        claude = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        claude_plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
        self.assertEqual(manifest["name"], "librecode-agent-skills")
        self.assertEqual(manifest["version"], "0.1.0")
        self.assertEqual(manifest["repository"], "https://github.com/LibreCodeCoop/agent-skills")
        self.assertEqual(manifest["license"], "AGPL-3.0-or-later")
        self.assertEqual(codex["plugins"][0]["name"], manifest["name"])
        self.assertEqual(codex["plugins"][0]["source"], {"source": "local", "path": "./"})
        self.assertEqual(claude["plugins"][0]["name"], manifest["name"])
        self.assertEqual(claude["plugins"][0]["source"], "./")
        for field in ("name", "description", "author"):
            self.assertEqual(claude_plugin[field], manifest[field])
        self.assertNotIn("version", claude_plugin)
        self.assertNotIn("version", claude["plugins"][0])

    def test_skill_frontmatter_and_bilingual_discovery(self):
        skills = list((ROOT / "skills").glob("*/SKILL.md"))
        self.assertEqual(len(skills), 1)
        for skill in skills:
            text = skill.read_text()
            self.assertTrue(text.startswith("---\n"))
            frontmatter = text.split("---\n", 2)[1]
            self.assertIn("name: " + skill.parent.name, frontmatter)
            self.assertRegex(frontmatter, r"(?m)^description: .{60,}")
            self.assertRegex(frontmatter.lower(), r"criar|inicializar|auditar")
            self.assertIn("bootstrap", frontmatter.lower())
            self.assertIn("references/security-and-supply-chain.md", text)
            for link in re.findall(r"\]\(([^)]+)\)", text):
                target = link.split("#", 1)[0]
                if target and not target.startswith(("https://", "http://")):
                    self.assertTrue((skill.parent / target).resolve().is_relative_to(skill.parent.resolve()), target)
            self.assertIn("AGPL-3.0-or-later", text)

    def test_internal_markdown_links_resolve(self):
        for path in ROOT.rglob("*.md"):
            for value in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                target = value.split("#", 1)[0]
                if not target or target.startswith(("http://", "https://", "mailto:")):
                    continue
                self.assertTrue((path.parent / target).is_file(), (path, target))

    def test_agpl_canonical_and_optional_mit_text(self):
        agpl = (ROOT / "LICENSE").read_bytes()
        self.assertEqual(agpl, (ROOT / "LICENSES/AGPL-3.0-or-later.txt").read_bytes())
        self.assertEqual(agpl, (ROOT / "skills/librecode-project-bootstrap/assets/AGPL-3.0-or-later.txt").read_bytes())
        self.assertIn(b"GNU AFFERO GENERAL PUBLIC LICENSE", agpl)
        self.assertEqual((ROOT / "LICENSES/MIT.txt").read_bytes(), (ROOT / "skills/librecode-project-bootstrap/assets/MIT.txt").read_bytes())

    def test_no_copied_libresign_skills_or_duplicated_rulesets(self):
        self.assertEqual({x.name for x in (ROOT / "skills").iterdir()}, {"librecode-project-bootstrap"})
        self.assertFalse((ROOT / "governance.config.json").exists())
        self.assertIn("LibreCodeCoop/.github", (ROOT / "AGENTS.md").read_text())
        self.assertIn("ZIP", (ROOT / "README.md").read_text())
        self.assertTrue((ROOT / ".github/CODEOWNERS").is_file())
        self.assertIn("@LibreCodeCoop/maintainers", (ROOT / ".github/CODEOWNERS").read_text())
        self.assertTrue((ROOT / "SECURITY.md").is_file())

    def test_public_catalog_excludes_internal_operating_workflows(self):
        readme = (ROOT / "README.md").read_text()
        policy = (ROOT / "references/language-policy.md").read_text()
        admission = (ROOT / "references/skill-catalog.md").read_text()
        self.assertIn("Public scope and language", readme)
        self.assertIn("customer records", readme)
        self.assertIn("separate private repository", policy)
        self.assertIn("Público ou interno", admission)
        self.assertIn("AGPL-3.0-or-later", readme)

    def test_every_source_file_has_spdx_or_narrow_annotation(self):
        annotated = {
            "plugin.json", ".agents/plugins/marketplace.json", ".claude-plugin/plugin.json",
            ".claude-plugin/marketplace.json", "skills/librecode-project-bootstrap/assets/MIT.txt",
            "skills/librecode-project-bootstrap/assets/AGPL-3.0-or-later.txt",
        }
        for path in ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
                continue
            rel = path.relative_to(ROOT).as_posix()
            if rel in {"LICENSE", "LICENSES/MIT.txt", "LICENSES/AGPL-3.0-or-later.txt"} or rel in annotated:
                continue
            if path.suffix == ".pyc":
                continue
            data = path.read_text()
            self.assertIn("SPDX-" + "License-Identifier:", data[:1200], rel)
            self.assertIn("SPDX-FileCopyrightText:", data[:1200], rel)
        reuse = (ROOT / "REUSE.toml").read_text()
        for rel in annotated:
            self.assertIn('"' + rel + '"', reuse)

    def test_workflows_pass_static_policy(self):
        self.assertEqual(check(ROOT), [])
        validate = (ROOT / ".github/workflows/validate.yml").read_text()
        self.assertIn("pull_request:", validate)
        self.assertIn("branches: [main]", validate)
        self.assertNotIn("pull_request_target:", validate)
        self.assertIn("actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1", validate)
        self.assertIn("reuse-action@676e2d560c9a403aa252096d99fcab3e1132b0f5", validate)
        self.assertIn("GITHUB_TOKEN: ${{ github.token }}", validate)
        self.assertIn("--network none", validate)
        needs_line = next(line.strip() for line in validate.splitlines() if line.strip().startswith("needs: ["))
        dependencies = [x.strip() for x in needs_line.split("[", 1)[1].split("]", 1)[0].split(",")]
        self.assertEqual(set(dependencies), set(REQUIRED_JOBS))
        for job in REQUIRED_JOBS:
            self.assertRegex(validate, rf"(?m)^  {re.escape(job)}:\s*$")
        self.assertRegex(validate, r"(?m)^  ci-required:\s*$")
        self.assertIn("if: always()", validate)
        self.assertIn("NEEDS_JSON: ${{ toJSON(needs) }}", validate)


class CommitPolicyTest(unittest.TestCase):
    def test_signed_author_and_conventional_subject(self):
        self.assertEqual(validate_message("Dev Example", "dev@example.test", "feat(skills): add catalog\n\nSigned-off-by: Dev Example <dev@example.test>"), [])
        self.assertTrue(verified_signature({"commit": {"verification": {"verified": True}}}))

    def test_rejects_invalid_subject_dco_or_signature(self):
        self.assertTrue(validate_message("Dev Example", "dev@example.test", "not conventional\n\nSigned-off-by: Dev Example <dev@example.test>"))
        self.assertTrue(validate_message("Dev Example", "dev@example.test", "feat: bad signoff\n\nSigned-off-by: Other <other@example.test>"))
        self.assertFalse(verified_signature({"commit": {"verification": {"verified": False}}}))
        self.assertFalse(verified_signature({}))


class CiGateTest(unittest.TestCase):
    def test_all_required_success_and_allowed_push_skip(self):
        ok = {name: {"result": "success"} for name in REQUIRED_JOBS}
        self.assertEqual(evaluate(ok, "pull_request"), [])
        ok["commit-policy"]["result"] = "skipped"
        self.assertEqual(evaluate(ok, "push"), [])
        self.assertTrue(evaluate(ok, "pull_request"))

    def test_missing_failure_cancellation_and_skips_fail_closed(self):
        base = {name: {"result": "success"} for name in REQUIRED_JOBS}
        for name in REQUIRED_JOBS:
            for result in ("failure", "cancelled", "skipped", "pending", None):
                with self.subTest(name=name, result=result):
                    values = {**base, name: {"result": result}}
                    if name == "commit-policy" and result == "skipped":
                        self.assertTrue(evaluate(values, "pull_request"))
                    else:
                        self.assertTrue(evaluate(values, "pull_request"))
            self.assertTrue(evaluate({k: v for k, v in base.items() if k != name}, "pull_request"))
        self.assertTrue(evaluate(base, "workflow_dispatch"))
        self.assertTrue(evaluate({**base, "untracked-check": {"result": "success"}}, "pull_request"))


if __name__ == "__main__":
    unittest.main()
