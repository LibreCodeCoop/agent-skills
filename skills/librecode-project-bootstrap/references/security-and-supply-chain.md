<!-- SPDX-FileCopyrightText: 2026 LibreCode Coop and contributors -->
<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->

# Segurança e cadeia de suprimentos

Ameaças consideradas conforme o projeto: entradas de PR público, permissões dos jobs, segredos, dependências, autenticação, multiempresa, serviços expostos, migrações e releases. Não introduzir Docker, banco, serviço de segredos, túnel ou permissões administrativas em projetos simples apenas para satisfazer uma checklist.

| Controle | Verificação executável ou aceite |
| --- | --- |
| Referências imutáveis de Actions | Comparar SHA upstream e comentários de versão; executar o verificador de política, Actionlint e Zizmor |
| Privilégios mínimos | Revisar `permissions`, eventos e checkout sem credenciais persistidas; testar caminhos de PR não confiáveis |
| Segredos | Executar Gitleaks ou equivalente no conteúdo e, quando necessário, no histórico Git; remover detalhes privados das evidências públicas |
| Dependências | Instalar via lock; executar `composer audit`, `npm audit`, `pip-audit`/`uv` ou `govulncheck`, conforme stack; registrar dados não verificados |
| Testes de negação | Cobrir input malformado, credencial inválida, ACL e isolamento entre tenants apenas se essas superfícies existirem |
| Containers | `docker build`, validação Compose, smoke real de inicialização, usuário/permissões, persistência e análise de imagem, se o produto de fato usa containers |
| Escopo público | Rejeitar `.env`, chaves, dumps, hosts internos e dados de clientes no repositório/distribuição; usar fixtures sintéticas |
| Release | Validar a revisão exata, checksum, artefato e autorização antes de publicar; CI verde não equivale a permissão de deploy |

## Atualização de dependências

Evitar Dependabot e Renovate atuando sobre o mesmo ecossistema sem separação explícita de responsabilidade. Em `suitecrm-mcp`, Composer e Actions ficam com Dependabot e Docker com Renovate; `akaunting-mcp` adota configuração diferente. Não transformar uma escolha local em obrigação universal. Atualizações major exigem revisão humana; automerge não é autorizado por esta Skill.

## Limites da automação

`audit_project.py` é heurístico e somente leitura. Não certifica segurança do histórico, qualidade das regras de negócio, branch protection remota ou estabilidade operacional. `check_ci_results.py` não publica status no GitHub. Cada recomendação precisa de comando verificável ou aceite humano definido; controles meramente decorativos não servem.
