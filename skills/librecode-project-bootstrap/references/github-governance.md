<!-- SPDX-FileCopyrightText: 2026 LibreCode Coop and contributors -->
<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->

# Governança GitHub e distribuição de workflows

Fontes vigentes: [configuração declarativa](https://github.com/LibreCodeCoop/.github/blob/main/governance.config.json), [governança](https://github.com/LibreCodeCoop/.github/blob/main/docs/repository-governance.md), [sincronização entre repositórios](https://github.com/LibreCodeCoop/.github/blob/main/docs/cross-repository-automation.md) e [política de atualizações](https://github.com/LibreCodeCoop/.github/blob/main/docs/dependency-update-policy.md).

## Autoridade e aplicação

- `LibreCodeCoop/.github` define as políticas e o catálogo de workflows. Seu motor `github-governance` calcula o plano e aplica as regras somente em execução separadamente autorizada; merge de JSON **não aplica** rulesets automaticamente.
- `protected-branches` é a política desejada para repositórios públicos e ativos elegíveis: revisão, Code Owner quando efetivo, conversas resolvidas e proteção contra exclusão/force push nas branches padrão e `stable*`. **Consultar o ruleset remoto** antes de afirmar que foi aplicado.
- `organization-config-ci` é específico de `.github` e `governance-ci` do projeto de governança. Não os descreva como requeridos por todos os consumidores.
- A política `required-ci-gate` observada para `release-tool` e `nextcloud-docker-development` está **desabilitada** até prova de um agregador real. Não a habilite apenas porque existe um job com o nome esperado.
- Aplicação controlada: obter plano read-only, revisar diferença, solicitar aprovação do ambiente protegido, aplicar somente a destino explicitamente autorizado e verificar rulesets remotos/drift.

## Contrato de `ci-required`

1. Enumerar todos os checks obrigatórios, matrizes, skips admissíveis e o SHA esperado.
2. Em um workflow único, usar `needs` para todos os jobs obrigatórios e `if: always()`. Inspecionar resultados concretos: `failure`, `cancelled`, ausência e `skipped` inesperado bloqueiam.
3. `needs` **não reúne workflows independentes**. Quando checks estão em várias execuções, criar coordenador que consulte as check suites correspondentes ao mesmo SHA; não fabricar um status verde.
4. Testar sucesso, falha, cancelamento, ausência, skips, reruns, mudanças no conjunto de jobs, matrizes e PRs de fork. Validar o check na revisão exigida pelo ruleset.
5. Alterar ruleset somente após comprovar o produtor e obter autorização separada. `scripts/check_ci_results.py` é apenas ferramenta de avaliação local, não publica check algum.

## Adoção dos templates institucionais

- Escolher somente arquivos aplicáveis em [`workflow-templates/`](https://github.com/LibreCodeCoop/.github/tree/main/workflow-templates). Um template Psalm/Nextcloud não é genericamente adequado a qualquer PHP; não há template institucional universal Python/Go presumido.
- Seguir sincronização com PR, `.github/actions-lock.txt`, autenticação aprovada e `*.patch` versionados para alterações locais. Divergências não autorizam sobrescrita.
- Usar referências `uses:` externas com SHA **completo de 40 caracteres**, comentário de versão upstream autêntico e `actions/checkout` com `persist-credentials: false`. Preferir permissões `contents: read`, escrita apenas no job que efetivamente exigir.
- Executar o verificador institucional ou equivalente, Actionlint e Zizmor. Pin de containers por digest quando apropriado.
- Evitar `pull_request_target` executando código não confiável com token de escrita, autoaprovação e automerge de mudanças não revisadas. CODEOWNERS de `.github` **não é herdado** pelo consumidor; definir responsáveis reais.
- Evitar filtros de caminhos que removam um check marcado como obrigatório para determinados PRs.
