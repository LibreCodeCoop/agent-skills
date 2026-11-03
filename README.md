<!-- SPDX-FileCopyrightText: 2026 LibreCode Coop and contributors -->
<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->

# LibreCode Agent Skills

**Public, Git-backed agent workflows for open-source software engineering.** This repository contains reusable skills, references, tests, and marketplace manifests as one installable plugin. The [LibreSign Agent Skills](https://github.com/LibreSign/agent-skills) repository informed its architecture but is neither copied nor required.

> **Português:** este repositório é dedicado a Skills públicas de engenharia e projetos de software livre. Processos administrativos, comerciais e operacionais privados da LibreCode têm um catálogo interno separado, com acesso restrito.

## Public scope and language

Public skills cover project creation, open-source collaboration, testing, reproducibility, security, repository governance, and non-destructive audits. **Never include internal business processes, customer records, credentials, private infrastructure identifiers, or proprietary operating procedures in this public plugin.** Keeping text in Portuguese does not make it private; visibility is a content and access-control decision.

English is preferred for **new public-facing instructions** to support international contributors. Skills retain bilingual discovery keywords, may respond in the user's language, and must preserve one authoritative engineering contract. The existing project-bootstrap Skill retains its reviewed Portuguese detailed instructions pending a behavior-verified translation; it is not a second language-specific Skill. See [language policy](references/language-policy.md).

## Skills across LibreCode catalogs

| Catalog | Skill | What it helps with | Availability |
| --- | --- | --- | --- |
| **[Public (this repository)](https://github.com/LibreCodeCoop/agent-skills)** | [librecode-project-bootstrap](skills/librecode-project-bootstrap/SKILL.md) | Creating and reviewing open-source projects with consistent quality, security, and collaboration practices. | Under review in [PR #1](https://github.com/LibreCodeCoop/agent-skills/pull/1) |
| **[Private internal](https://github.com/LibreCodeCoop/agent-skills-internal)** | No operational skills yet | Future commercial, administrative, and cooperative workflows for authorized LibreCode members. | Catalog in preparation; restricted access |

The internal repository is accessible only to authorized collaborators. Listing it here does not grant access or expose its contents. **Skills under review are not yet published as installed plugins.**

Admit additional public Skills only when their trigger, output, and permission boundary are distinct. See [catalog admission](references/skill-catalog.md).

## Install and update from Git

**Canonical source:** `LibreCodeCoop/agent-skills`. For compatible Codex clients:

```sh
codex plugin marketplace add LibreCodeCoop/agent-skills
codex plugin marketplace list
codex plugin marketplace upgrade
```

Install the complete **LibreCode Agent Skills** plugin through the supported marketplace. A marketplace refresh does **not** guarantee that cached plugin installations or ChatGPT web were updated. Verify the installed commit, version and available Skills. Other clients may require a different supported installation path; see [distribution](references/distribution.md). Do not install independent single-Skill ZIP snapshots alongside the Git-backed plugin.

## Engineering rules and licensing

The authoritative GitHub governance policy and shared workflow catalog live at [LibreCodeCoop/.github](https://github.com/LibreCodeCoop/.github). This plugin references those sources instead of copying their policy state. New LibreCode-owned projects default to **AGPL-3.0-or-later**. Alternative licenses require an explicit compatible decision; existing projects are not silently relicensed.

## Verification

```sh
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s skills/librecode-project-bootstrap/scripts/tests -v
python3 skills/librecode-project-bootstrap/scripts/audit_project.py . --strict
python3 scripts/check_workflows.py .
```

GitHub CI additionally runs REUSE, Actionlint, Zizmor, secret scanning, signed-commit/DCO validation and an actual fail-closed `ci-required` aggregator. CI passing does not prove product readiness or effective branch protection. Review [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), and [catalog admission](references/skill-catalog.md). No automatic merge, deploy, ruleset apply, or release.
