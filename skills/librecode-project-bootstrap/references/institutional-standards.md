<!-- SPDX-FileCopyrightText: 2026 LibreCode Coop and contributors -->
<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->

# Matriz de decisões de engenharia

Registro de 2026-11-03. A fonte de verdade das regras organizacionais é [`LibreCodeCoop/.github`](https://github.com/LibreCodeCoop/.github). **Política desejada, implementação no código e aplicação efetiva no GitHub são estados diferentes.** Esta é uma proposta de baseline técnico baseada em evidências, não um ruleset universal automaticamente promulgado.

**Obrigatório:** definido em governança aplicável ou necessário para commits desta Skill. **Recomendado:** prática bem evidenciada, porém não universalmente imposta. **Condicional:** depende de linguagem, risco ou distribuição. **Específico:** não transportar automaticamente a outro produto.

| Controle | Classificação | Evidência de adoção | Comprovação exigida |
| --- | --- | --- | --- |
| PR revisado, aprovação, conversas resolvidas e proteção da branch | Obrigatório quando o ruleset for aplicável | `governance.config.json` define `protected-branches` para repositórios públicos elegíveis | Consultar ruleset **remoto** e revisão real |
| CODEOWNERS efetivo | Condicional à governança e responsáveis reais | `.github` mantém CODEOWNERS; `profile_fields` tem mapeamento específico | Conferir regras e mantenedores com permissão; não há herança automática |
| Conventional Commits e DCO | Obrigatório nos commits produzidos pela Skill | `suitecrm-mcp`, `akaunting-mcp` e CI de governança | Validar cada commit e trailer de autoria |
| Assinatura criptográfica | Obrigatório nas alterações remotas autorizadas pela Skill | `akaunting-mcp/AGENTS.md`; Git Signing MCP | Verificar commit no GitHub e DCO separadamente |
| Actions com SHA completo e versão upstream | Obrigatório nos novos workflows LibreCode | `.github/scripts/check_workflow_policy.py`, `nextcloud-docker` PR #85 | Executar verificador, Actionlint e Zizmor; comparar SHA |
| Privilégios mínimos e checkout seguro | Obrigatório nos novos workflows | `.github` checker, CI dos MCPs | `permissions` por job e `persist-credentials: false` |
| Agregador `ci-required` | Condicional à adoção explícita | `required-ci-gate` da governança atualmente desabilitado nos consumidores nomeados | Observar **todos** os jobs reais do SHA correto, falha/cancelamento/skip/ausência |
| Lint, análise estática, formatação e testes de comportamento | Recomendado; ferramentas condicionais | PHPUnit/PHPStan/CS Fixer nos MCPs, Behat/Playwright em NFSe, Bats no Docker | Executar comandos e verificar negativos/integrados relevantes |
| Locks, instalação reprodutível e auditoria | Condicional às dependências | Composer e npm nos exemplos | Executar instalação com lock e auditoria nativa |
| Imagens imutáveis, permissões e smoke | Condicional a containers | `suitecrm-mcp`, `nextcloud-docker` | Build, smoke, usuário, volumes e scan quando aplicável |
| REUSE, SPDX e licença integral | Padrão proposto para novos repositórios; obrigatório se REUSE adotado | Workflow `reuse.yml` do catálogo e apps LibreCode | `reuse lint` real e revisão de direitos |
| AGPL-3.0-or-later como **padrão** de novos projetos LibreCode | Padrão institucional confirmado pelo responsável; não proibição geral de outras licenças | Licenças dos repositórios analisados e decisão institucional de 03/11/2026 | Licença canônica por padrão; exceções explícitas justificadas; preservar existentes |
| README, contribuição, segurança e escopo público | Recomendado; profundidade condicional | MCPs e módulos com políticas próprias | Configuração, exemplos e reportes privados verdadeiros |
| Scan de segredos e distribuição | Condicional a exposição pública e sensibilidade | `akaunting-mcp` possui Gitleaks e verificação de escopo | Testes de scanner no histórico/árvore e dados sintéticos |
| Release e branches estáveis | Condicional à estratégia de distribuição | `.github/docs/release-workflow-architecture.md`, LibreSign | Artefato de commit correto e autorização separada |
| Cenários fiscais, multiempresa e APIs Nextcloud | Específico de produto | `akaunting-nfse`, LibreSign, profile_fields | Transferir a disciplina de contratos, não as dependências/ambientes |

## Interpretação e limites

1. `ci-required` não pode ser um check fictício. Um status verde que ignore uma matriz ou workflow obrigatório é um erro de governança.
2. Templates Nextcloud/Psalm não são fluxos genéricos PHP. Python, Go e outras linguagens podem exigir adaptação tecnicamente justificada e revisada.
3. DCO e assinatura criptográfica são independentes. Assinatura de commit não substitui revisão humana nem autorização de escrita.
4. Um teste de smoke não comprova cobertura, integridade, licenciamento ou prontidão de produção. Use `PASS`, `FAIL`, `UNKNOWN` e `N/A` com evidência.
5. O auditor local não consegue certificar GitHub remoto: regras efetivas, check suites, SHA e permissões precisam de consulta externa.

Para URLs diretas, exceções e nível de adoção, veja [evidence-ledger.md](evidence-ledger.md).
