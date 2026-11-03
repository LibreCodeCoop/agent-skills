<!-- SPDX-FileCopyrightText: 2026 LibreCode Coop and contributors -->
<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->

# Perfis de qualidade por linguagem

Os comandos abaixo são **candidatos**, a selecionar conforme o projeto e executar. Não adicionar ferramentas que não rodam nem configuração decorativa. Um CLI mínimo sem dependências precisa de testes funcionais e negativos; isso não equivale à cobertura exigida para um serviço em produção.

| Plataforma | Estrutura nativa | Testes, análise e estilo | Dependências |
| --- | --- | --- | --- |
| PHP | `composer.json`, PSR-4 e versão suportada | `php -l`, PHPUnit/Pest; PHPStan **ou** Psalm; PHP-CS-Fixer e testes de integração conforme o produto | `composer validate`, lock quando apropriado e `composer audit` |
| Python | `pyproject.toml`, `src/` e runtime | `compileall`, `unittest`/pytest, Ruff e análise de tipos quando relevante, testes de integração | pip/uv, lock conforme distribuição, `pip-audit` |
| TypeScript | `package.json`, `tsconfig.json`, engines | `npm ci`, lint, `tsc --noEmit`, testes, build; Playwright se existe UI | Lock e `npm audit` |
| JavaScript | Runtime Node e módulo definidos | `node --test`, ESLint/formatter conforme tamanho, typecheck opcional | `npm ci` e `npm audit` se há dependências |
| Go | `go.mod` e versão mínima | `gofmt`, `go vet ./...`, `go test ./...`, `-race` se pertinente | `go mod verify`, `govulncheck` |
| Shell/containers | Somente se o produto precisar | ShellCheck, Bats, build, Compose, smoke e scan de imagem | Digest e versões reproduzíveis |
| Outras | Manifest idiomático da plataforma | Formatador, análise, unit/integration/negative tests reais | Pin e auditoria compatíveis |

## Escolha pelo contexto

- **Bibliotecas:** testar a menor versão suportada de runtime/dependências e a mais nova quando viável.
- **Serviços:** adicionar testes de autorização, erros, prontidão, endpoints e migrações seguras.
- **Plugins:** respeitar framework hospedeiro e matriz de compatibilidade; não importar versões Nextcloud para um projeto genérico.
- **Interfaces sensíveis:** cobrir negação, isolamento de tenants, input malformado e falhas transacionais com dados sintéticos.
- **Containers:** testar efetivamente build, usuário, volume, inicialização, arquiteturas relevantes e vulnerabilidades; não criar Docker para biblioteca que não precisa.
- **CI:** orquestrar comandos já testados nos gerenciadores (`composer check`, `npm run check`, `go test`) em vez de grandes scripts shell duplicados.

O auxiliar CLI executável aceita `php`, `python`, `javascript`, `go`. Exemplo com licença padrão:

```sh
python3 scripts/bootstrap.py --name demo --language python --runtime 3.12 --kind cli --distribution source --copyright 'LibreCode Coop and contributors' --destination /tmp/demo
```

TypeScript e outros tipos de aplicação requerem definição real de build/testes pelo agente; não entregar gerador incompleto como projeto pronto. Sempre registrar a ausência de análise estática, auditoria de vulnerabilidades ou testes de integração não executados.
