<!-- SPDX-FileCopyrightText: 2026 LibreCode Coop and contributors -->
<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->

# Critérios de admissão e revisão de Skills

O catálogo deve conter o **menor conjunto suficiente de fluxos distintos**, não uma coleção arbitrária de papéis ou linguagens. Antes de criar uma Skill, verifique se o novo caso pode ser resolvido por uma referência ou modo em uma existente. Compare o gatilho, a saída esperada e as permissões. Skills concorrentes com gatilhos idênticos devem ser combinadas ou ter descrições mais precisas.

Para admitir uma nova Skill, apresente um exemplo positivo de ativação, um caso próximo que deve ser roteado para outra Skill, o critério de autorização, os testes automatizados de recursos e um experimento com uso real. As verificações estruturais não demonstram que um modelo agirá corretamente diante de texto malicioso; esse risco exige avaliações comportamentais com credenciais desabilitadas e supervisão humana.

A Skill atual `librecode-project-bootstrap` trata **criação inicial e auditoria institucional de configuração**. Ela não substitui code review de uma mudança pontual, investigação de um incidente de CI ou tratamento confidencial de advisories; esses gatilhos e saídas são distintos e não justificam cópia das Skills da LibreSign.
