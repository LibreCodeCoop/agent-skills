<!-- SPDX-FileCopyrightText: 2026 LibreCode Coop and contributors -->
<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->

# Contribuindo

Use uma branch curta e um PR revisável. Cada commit deve conter título Conventional Commits, trailer DCO `Signed-off-by` com identidade real e assinatura criptográfica verificada no GitHub. O serviço Git Signing MCP é o mecanismo preferencial para commits autorizados por agentes. Revisões, CODEOWNERS e conversas resolvidas seguem a política de `LibreCodeCoop/.github` aplicada ao repositório; sem merge ou auto-merge silencioso.

Leia [critérios do catálogo](references/skill-catalog.md) e [limites de confiança](references/untrusted-input.md). Use dados sintéticos. Alterações em texto de instrução exigem testes de conteúdo e exemplos de ativação correta/incorreta, não apenas um arquivo bem formatado. Criação de uma Skill nova requer justificativa de não sobreposição e testes de recursos auxiliares executados.

## Comandos locais

```sh
python3 -m compileall -q scripts tests skills
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s skills/librecode-project-bootstrap/scripts/tests -v
python3 scripts/check_workflows.py .
python3 skills/librecode-project-bootstrap/scripts/audit_project.py . --strict
reuse lint
```

Instale Actionlint e Zizmor em versões verificadas para executar as verificações adicionais. O catálogo usa somente a biblioteca padrão do Python 3.12+ em seus validadores e não requer Docker, banco ou uma instalação de desenvolvimento completa. A execução de varredura de segredos por imagem imutável acontece na CI.

A geração de um ZIP de Skill avulsa não é canal institucional de atualização. Não edite manualmente arquivos de uma instalação em cache e considere a revisão exata do repositório ao testar mudanças.
