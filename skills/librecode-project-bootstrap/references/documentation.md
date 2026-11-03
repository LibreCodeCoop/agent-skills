<!-- SPDX-FileCopyrightText: 2026 LibreCode Coop and contributors -->
<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->

# Documentação e licenciamento

Criar somente o material pertinente ao produto, mantendo instruções que sejam executáveis. Preferir português brasileiro como idioma de manutenção e oferecer uma introdução em inglês para colaboradores externos quando útil.

| Documento | Critério de inclusão e aceite |
| --- | --- |
| README | Padrão: objetivo, instalação, runtime, comandos que realmente passam, suporte e licença |
| CONTRIBUTING | Projetos colaborativos: DCO, Conventional Commits, revisão e comandos reais de desenvolvimento |
| SECURITY | Repositórios públicos ou sensíveis: canal privado verdadeiro, escopo e sem SLA inventado |
| LICENSES/SPDX/REUSE | Texto integral canônico, atribuição adequada; executar `reuse lint`, não apenas verificar presença |
| Arquitetura | Múltiplos serviços ou limites de confiança relevantes, sem diagrama especulativo |
| Desenvolvimento | Setup, fixtures e validação com passos reproduzíveis quando não forem óbvios |
| Operações | Aplicações implantadas: variáveis, segredos, saúde, backup, rollback e limites entre código/deploy |
| CHANGELOG | Releases públicos: registrar versões lançadas, nunca histórico fictício |
| Exemplos/API | APIs/bibliotecas: exemplos funcionais com dados sintéticos |

## Licenças

Para um **novo projeto próprio da LibreCode**, escolher `AGPL-3.0-or-later` por padrão, com o texto integral e identificadores coerentes. Outra licença pode ser solicitada explicitamente se houver justificativa, direitos apropriados e compatibilidade com dependências e distribuição. Essa preferência não é, por si só, uma regra GitHub automaticamente aplicada. Uma auditoria não pode substituir a licença de um projeto existente. Não gerar texto de licença incompleto a partir de um SPDX ID.

Arquivos que aceitam comentários recebem `SPDX-FileCopyrightText` e `SPDX-License-Identifier`; JSON e binários exigem anotação REUSE ou arquivos `.license` específicos. O conteúdo de uma licença da FSF não deve receber automaticamente copyright do gerador. Validar com `reuse lint`.

## Evitar documentação transitória

Não versionar relatórios temporários, logs de incidentes, screenshots de revisão, dumps ou planos por PR que pertencem à descrição do PR ou workspace privado. Atualizar documentos permanentes de comportamento e aceitar evolução incremental. Remover endereços, hostnames internos e identificadores de clientes de exemplos públicos.
