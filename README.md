<!-- SPDX-FileCopyrightText: 2026 LibreCode Coop and contributors -->
<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->

# LibreCode Agent Skills

Catálogo público de Skills reutilizáveis para inicialização, auditoria e manutenção de projetos da LibreCode. O repositório contém um **plugin Git-backed**: as Skills, referências, testes e manifestos fazem parte da mesma unidade de distribuição. O repositório da [LibreSign](https://github.com/LibreSign/agent-skills) foi usado como referência de arquitetura, mas não é uma dependência nem uma cópia deste catálogo.

> **English:** Public LibreCode Coop agent-skills plugin for creating and auditing software projects. Skill discovery metadata includes English and Portuguese. Operational guidance is maintained in Brazilian Portuguese. Follow the requesting user's language when producing answers.

## Catálogo

| Skill | Objetivo |
| --- | --- |
| [librecode-project-bootstrap](skills/librecode-project-bootstrap/SKILL.md) | Inicializar projetos PHP, Python, JavaScript e Go no modo CLI mínimo; orientar outras arquiteturas e auditar projetos existentes sem alterações destrutivas. |

Nova Skill só deve entrar no catálogo se possuir gatilho e resultado distintos dos existentes. Consulte [critérios de admissão](references/skill-catalog.md).

## Instalação e atualização

**Fonte canônica:** `LibreCodeCoop/agent-skills`, instalado como um único plugin por um cliente que suporte marketplaces Git. No Codex com suporte a plugins:

```sh
codex plugin marketplace add LibreCodeCoop/agent-skills
codex plugin marketplace list
codex plugin marketplace upgrade
```

Use o marketplace do cliente para instalar **LibreCode Agent Skills**. A atualização do catálogo **não prova** que a cópia instalada em cache ou o ChatGPT web foi atualizada: confirme a versão do `plugin.json`, a revisão instalada e o acesso à Skill. Para outros clientes, consulte [distribuição](references/distribution.md). Não instale um ZIP avulso em paralelo ao plugin; o pacote isolado pode divergir da fonte Git e de suas referências.

Nenhuma instalação, sincronização, release, deploy ou alteração de regras é disparada automaticamente pela presença desses arquivos.

## Padrões institucionais e idioma

- A fonte de verdade para **governança de repositórios e workflows** é [`LibreCodeCoop/.github`](https://github.com/LibreCodeCoop/.github); este catálogo descreve como aplicar os controles e consultar a política, sem mantê-la em duplicidade.
- Licença padrão de projetos próprios LibreCode: **AGPL-3.0-or-later**. Escolhas alternativas exigem decisão explícita e verificação de compatibilidade; a auditoria preserva licenças existentes.
- **Português brasileiro** é o idioma principal da documentação e dos fluxos internos. Nomes técnicos e identificadores permanecem em inglês; metadados de descoberta e orientações de instalação incluem inglês. A resposta deve usar o idioma do solicitante. [Política de idioma](references/language-policy.md).

## Qualidade e contribuições

```sh
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s skills/librecode-project-bootstrap/scripts/tests -v
python3 skills/librecode-project-bootstrap/scripts/audit_project.py . --strict
python3 scripts/check_workflows.py .
```

A CI também executa `reuse lint`, Actionlint, Zizmor, varredura de segredos, verificação de commits e um agregador que considera falhas, cancelamentos e skips. Testes de comportamento com modelos e integração em projetos de terceiros exigem avaliações adicionais, não substituídas por CI verde. Consulte [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md) e [avaliação do catálogo](references/skill-catalog.md).

Este catálogo não faz deploy nem merge de forma automática.
