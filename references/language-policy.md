<!-- SPDX-FileCopyrightText: 2026 LibreCode Coop and contributors -->
<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->

# Language and visibility policy

**Classify by audience and disclosure risk first; choose language second.** This public repository contains only reusable open-source software engineering processes. LibreCode commercial, administrative and internal operational workflows belong in a separate private repository, not here, regardless of whether they are written in English or Portuguese.

## Public catalog

- **English preferred** for new publicly distributed Skills and onboarding documentation; contributors may submit Brazilian Portuguese proposals and translations.
- Keep technical names, identifiers, paths and API concepts stable. Use both English and Portuguese activation keywords in `SKILL.md` metadata when they help discovery.
- Respond in the user's language and do not change engineering or approval standards according to language.
- Retain one normative workflow per Skill. Where more than one translation exists, make the canonical text explicit, review semantic equivalence and test the same positive/negative behavioral cases.
- The existing `librecode-project-bootstrap` has bilingual discovery metadata and Portuguese operational guidance. Translate only with maintainers' review and validation against the current test suite; do not ship an unrelated duplicate English Skill solely for translation.

## Internal catalog

- Portuguese (Brazil) is the primary language for working instructions and operational documentation; English names remain acceptable for technical interoperability.
- Private workflow text must remain in the private catalog and must not be synchronized to public branches, public CI artifacts, online evaluations or examples.
- Private visibility is not a permission to commit passwords, customer records, sensitive commercial data, production fixtures or personal information.

## Português resumido

Separe as Skills por finalidade e necessidade de sigilo, não pelo idioma. O catálogo público prioriza acessibilidade internacional; o catálogo privado prioriza revisão clara em português pelos cooperados. Metadados bilíngues não substituem testes de ativação nem autorizam duas fontes independentes de regras.
