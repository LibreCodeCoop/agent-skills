<!-- SPDX-FileCopyrightText: 2026 LibreCode Coop and contributors -->
<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->

# Distribuição Git-backed

O repositório **LibreCodeCoop/agent-skills** é a única fonte de verdade do plugin. Os manifestos `plugin.json`, `.agents/plugins/marketplace.json`, `.claude-plugin/plugin.json` e `.claude-plugin/marketplace.json` se referem ao mesmo plugin e são testados juntos. Versões publicadas são associadas a commits revisados e verificáveis. Nunca atualize a cópia instalada como forma de desenvolver o plugin.

Um cliente com suporte a marketplace Git pode adicionar `LibreCodeCoop/agent-skills` e instalar o plugin completo. Na versão de Codex que implementa `codex plugin marketplace add`, `list` e `upgrade`, o upgrade atualiza o catálogo disponível; não garante recarregamento de uma instalação em cache nem atualização do ChatGPT web. Verifique a revisão instalada, reinicie a sessão ou reinstale conforme a plataforma. Outros clientes podem não oferecer instalação por URL: use os meios oficiais do produto, sem afirmar suporte inexistente.

As Skills deste catálogo devem ser instaláveis apenas pelo plugin completo; dependências compartilhadas precisam permanecer no repositório. Um `skill.zip` de uma única Skill é um **snapshot manual separado**, não o fluxo institucional padrão. Não publique releases, tags, pacotes ou alterações automáticas sem autorização.
