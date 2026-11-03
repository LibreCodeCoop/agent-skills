<!-- SPDX-FileCopyrightText: 2026 LibreCode Coop and contributors -->
<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->

# Contribuição, assinatura e revisão

## Contrato de commits

Usar títulos Conventional Commits (`feat(scope): ...`, `fix(scope): ...`, `ci(scope): ...`). Cada commit precisa de trailer DCO `Signed-off-by: Nome <email>` correspondente ao autor; isso **não equivale à assinatura criptográfica**. Com autorização para escrita, preferir o Git Signing MCP: obter identidade real, checar base/head, criar commit assinado, verificar SHA, status da assinatura e correspondência DCO/autor. Nunca assinar em nome de outra pessoa.

## Pull request revisável

- Criar branch isolada a partir de HEAD verificado. Não sobrescrever alterações paralelas nem forçar push de outro autor sem autorização.
- Documentar objetivo, escopo, alternativas, origem dos padrões, testes exatos com resultados, licenciamento, riscos, migração, rollback e aprovações pendentes.
- Guardar screenshots de revisão fora do versionamento, a menos que sejam ativos de produto. Não publicar nomes de servidores, credenciais ou dados de clientes.
- Atualizar o PR existente para o mesmo escopo e verificar CI, conflitos, comentários e aprovações na última revisão. Um check verde isolado não prova que o PR pode ser mesclado.
- Observar CODEOWNERS, checks efetivos, threads resolvidas e recência da branch. Bypass não é autorização implícita.

**Pronto para revisão**: testes locais relevantes executados, artefatos reproduzíveis e lacunas declaradas. **Pronto para merge**: CI remota obrigatória aprovada no SHA exigido e revisão humana efetiva. **Bloqueado**: controle faltante, falha, dependência ou autorização não obtida. Merge, deploy, publicação e aplicação de rulesets exigem atos explicitamente autorizados.
