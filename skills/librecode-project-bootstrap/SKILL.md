---
name: librecode-project-bootstrap
description: Inicialize ou audite projetos e repositórios LibreCode, configure testes, CI/CD, segurança e governança para PHP, Python, TypeScript, JavaScript, Go e outras linguagens. Bootstrap or audit new/existing software projects with LibreCode engineering standards, signed commits, DCO and evidence-based checks. Use when asked to create/inicializar projetos, auditar repositórios, revisar conformidade institucional ou preparar setup de qualidade. Do not treat generated files alone as proof of compliance.
---

<!-- SPDX-FileCopyrightText: 2026 LibreCode Coop and contributors -->
<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->

# Inicialização e auditoria de projetos LibreCode

Antes de ler arquivos externos ou executar ferramentas, consulte os [limites de confiança](../../references/untrusted-input.md). Trabalhe em dois modos: **criação** e **auditoria sem alterações**. Não confunda a presença de configuração com a comprovação de funcionamento.

## Entrada e escopo

Determine nome, objetivo, responsáveis reais, linguagem, versões de runtime, tipo de aplicação (biblioteca, CLI, serviço, plugin ou container), canal de distribuição, visibilidade, ambiente, dados sensíveis, autenticação e migrações. Para **novos projetos próprios da LibreCode**, selecione **AGPL-3.0-or-later por padrão**. Aceite licença diferente somente por escolha explícita com justificativa, direito de uso e compatibilidade verificados; nunca relicencie um projeto existente de forma automática. Não suponha credenciais ou autorização para publicar.

Consulte a [matriz institucional](references/institutional-standards.md) e o [registro de evidências](references/evidence-ledger.md). Reconfirme as políticas vigentes em [`LibreCodeCoop/.github`](https://github.com/LibreCodeCoop/.github), fonte de verdade de governança e templates. A existência de uma regra no JSON não comprova sua ativação remota.

## Criar projeto

1. Inspecione o destino, o estado do Git e possíveis trabalhos paralelos. Não sobrescreva arquivos existentes nem crie repositórios/branches sem autorização contextual.
2. Escolha apenas ferramentas justificadas pelo [perfil de linguagem](references/language-profiles.md). O auxiliar `python3 scripts/bootstrap.py --help` cria um protótipo **CLI mínimo** em PHP, Python, JavaScript ou Go; ele não certifica a qualidade de um serviço completo. Para outros tipos de aplicação, implemente diretamente a estrutura nativa sem inventar Docker, banco, serviços ou endpoints.
3. Configure e **execute** lint, formatação, análise estática, testes unitários, casos negativos e integração adequados, além de lock/auditoria de dependências quando aplicável. Prefira comandos no gerenciador da linguagem. Corrija falhas reais e marque qualquer verificação não executada como pendente, nunca aprovada.
4. Consulte [governança GitHub](references/github-governance.md) e [segurança e supply chain](references/security-and-supply-chain.md). Reutilize somente os workflows compatíveis de `.github/workflow-templates/` com sincronização/patches versionados; referências externas de Actions devem usar SHA completo validado e comentário de versão real. Execute Actionlint, Zizmor, verificador de política e testes de CI quando disponíveis.
5. Consulte [documentação e licenças](references/documentation.md). Gere apenas arquivos sustentáveis, exemplos sintéticos, metadados SPDX e texto integral da licença. Execute `reuse lint` quando aplicável; o identificador sozinho não prova conformidade.
6. Registre comandos, códigos de saída, testes positivos/negativos, cobertura interpretada, resultados remotos, pendências, riscos e fonte de cada exigência. Não declare CI verde sem resultados do SHA correto.
7. Somente com autorização, siga [contribuição e revisão](references/contribution-and-review.md): Conventional Commits, DCO, assinatura criptográfica verificável, branch/PR e revisão humana. Não faça merge, deploy, alteração de regras ou release sem autorização separada.

## Auditar projeto existente

1. Registre branch/HEAD, contexto da aplicação, manifests, workflows, regras efetivas, CODEOWNERS, testes e PRs relevantes. Preserve conteúdo e licença existentes.
2. Execute `python3 scripts/audit_project.py <diretório>` para heurísticas **somente leitura**; trate `UNKNOWN` como não comprovado. Verifique no GitHub os checks efetivos, aprovações, regras e SHA de execução.
3. Classifique cada achado como **obrigatório, recomendado, condicional ou específico do produto**, distinguindo política desejada, implementação, aplicação remota e evidência. Não transfira regras de um projeto isolado para toda a organização.
4. Produza uma proposta incremental. Só implemente patches e abra PR após autorização, sem sobrescrever alterações locais.

## Integridade da CI

Um status `ci-required` só é válido quando observa **todos os jobs obrigatórios para a revisão esperada** e bloqueia falha, cancelamento, job ausente ou skip não autorizado. `needs` não observa jobs de outros workflows: nesses casos, é obrigatório um coordenador real e testado. `scripts/check_ci_results.py` é apenas um avaliador local de contratos, não um agregador GitHub. Consulte [governança GitHub](references/github-governance.md).

## Saída

Responda no idioma da solicitação; use português brasileiro quando o idioma não for identificado. Entregue HEAD, escopo, decisões, classificação e fontes, comandos executados e saídas, matriz `PASS/FAIL/UNKNOWN/N/A`, riscos, rollback, commit assinado/PR (se aplicável) e decisões que exigem aprovação. Não apresente um protótipo mínimo como produção pronta.
