# RUN MANIFEST — validator V1.6 on Official Tabs micro-demo (FLOW-641)

Повторный прогон **того же** живого кейса, что FLOW-617 (V1.2), FLOW-624
(V1.3), FLOW-631 (V1.3 run 2), FLOW-632 (V1.4) и FLOW-629 (V1.5). Бандл —
`../revenue-kb-v1.6/`. Оба плеча, изолированный контекст.

## Что валидировалось

Confluence **815603314**, space CRO — «2026-07-13 UG App Official Tabs feature
micro-demo in first session», **версия 51**. Карточка эксперимента взята
**побайтово** из прогона V1.2 (`../trial-run-815603314/inputs/arm-a.md`) — тот
же источник, что в V1.3, V1.4 и V1.5. Свежий `cnfl pull` не делался:
единственная переменная относительно V1.5 — версия бандла (плюс вариативность
модели).

```
5966bfe315a63e52b6c3f8c7db488eb7b92925c5a9f8aafee745d368997783af  inputs/experiment_card.md (20 206 bytes)
```

Проверено `cmp`: файл **байт-в-байт** равен
`../trial-run-815603314-v1.5/inputs/experiment_card.md`.

## Входы инференса

Собраны детерминированно `build_inputs.py` (stdlib-only): секция `## PROMPT`
промпта V1.6, подстановка `{KNOWLEDGE_CONTEXT}` и `{EXPERIMENT_CARD}`. Плечо A
получает тот же текст с пустым блоком `<knowledge-context>`.

```
8431a7b4163a2b1f5cec4fc47dc7c35ff0d5d5b5745ac107a4e855d83b1cb861  inputs/arm-a.md (43 050 bytes)
f98122916bf8bc882c91a66057ce0a617b41e2144f37e9bd1a35fd67a502f4b5  inputs/arm-b.md (154 519 bytes)
85f643999b2638ea1ba0acb003028929a4cf178b2bf9b2855cf00af3d40540f3  KNOWLEDGE_CONTEXT (111 469 bytes)
```

Использованные frozen-файлы бандла V1.6:

```
f5d60e65ca328d85f30a5300f2584fda3fa58fbf81b327653d0db779541a3d4c  ../revenue-kb-v1.6/knowledge_base.md
b66247b43bf96d2683e1236fc92063d21b84322f1b86a0bfa75ba87a4e0b7703  ../revenue-kb-v1.6/pattern_cards.md
a0191e948059698b6d25e578c191ed3daca396a9612b276af404cef18067d247  ../revenue-kb-v1.6/validator_prompt_v1_6.md
a7b0c18749a114667feaab02bfeefbdc5ad5aef0f0fbfbb1786d5f6f06cdf9eb  ../revenue-kb-v1.6/linter.py
```

`pattern_cards.md` — тот же хеш, что в манифестах V1.2/V1.3/V1.4/V1.5.
KNOWLEDGE_CONTEXT вырос с 98 281 до 111 469 байт (+§1.13, +§2.10, +§2.11,
+§2.12): объёмы разделов ответа с V1.5 напрямую несопоставимы.

## Инференс

Headless, изолированный контекст, из пустого рабочего каталога, без
инструментов, MCP и файлов:

```
claude -p --model claude-opus-5 --settings '{}' \
  --strict-mcp-config --mcp-config '{"mcpServers":{}}' \
  --disallowed-tools "Bash,Read,Write,Edit,Glob,Grep,WebFetch,WebSearch,Task,NotebookEdit,TodoWrite" \
  --append-system-prompt "Write the entire answer in English." \
  < inputs/arm-<X>.md > outputs/arm-<X>.md
```

## Линтер

```
python3 ../revenue-kb-v1.6/linter.py outputs/arm-a.md \
    --kb ../revenue-kb-v1.6/knowledge_base.md \
    --patterns ../revenue-kb-v1.6/pattern_cards.md \
    --card inputs/experiment_card.md --no-kb-arm   > outputs/arm-a.lint.json
python3 ../revenue-kb-v1.6/linter.py outputs/arm-b.md \
    --kb ../revenue-kb-v1.6/knowledge_base.md \
    --patterns ../revenue-kb-v1.6/pattern_cards.md \
    --card inputs/experiment_card.md               > outputs/arm-b.lint.json
```

## Результат

| Плечо | Линтер | Замечаний | `[stop]` | Ранг FD7 | Роли | Ошибок | Условная форма | Тем / коллизий | Generic |
|---|---|---|---|---|---|---|---|---|---|
| A, без базы | FAIL | 6 | 3 | корректен | обе | 5 (§2.8, все на одной паре утверждений) | **6 / 6** | 11 / **0** | **0** флагов, 6 из 6 `Fix:` заякорены |
| B, с базой | FAIL | 4 | 3 | корректен | обе | **1** (`E_COMPUTED_SOURCE_ID`) | **6 / 6** | 9 / **0** | **0** флагов, 2 из 2 предложений и 4 из 4 `Fix:` заякорены |

Ни одного `E_TOPIC_MISSING`, `E_TOPIC_MALFORMED`, `E_DUPLICATE_TOPIC`,
`E_FINDING_NO_CONDITION`, `E_GROUNDS_UNLABELLED`,
`E_PROPOSAL_NO_CONDITIONAL_FORM`, `E_CONSEQUENT_NO_DIRECTION`,
`E_PROPOSAL_UNANCHORED` и `E_GENERIC_UI_ADVICE` — то есть **все девять новых
правил соблюдены обоими плечами с первого прогона**. Единственный warning в
обоих плечах — `W_MAIN_OVER_CAP` (1 036 и 1 289 слов при капе ~550);
`W_TOPIC_RESTATED_IN_APPENDIX` и `W_FIX_UNANCHORED` не сработали ни разу.

Аналоги плеча B: T2-07 заявлен L2 и вычисляется L2, T1-07 заявлен L3 и
вычисляется L3 — расхождений нет; `evidence is mixed` присутствует с обеими
границами переноса.

### Единственная ошибка плеча B

`E_COMPUTED_SOURCE_ID`: в `[computed]`-замечании про разбавление
(`chords-branch-dilution-readout`) внутри слота `Fix:` осталась ссылка `(P-11)`.
По §2.8 CC3 вычисление над числами карточки не несёт source ID. Ошибка
нотационная: ни одно число замечания из базы не взято — все 78%, 27%, 57%, 22%
принадлежат карточке.

### Пять ошибок плеча A

Все пять — §2.8, и все на двух утверждениях:

- `-0.9 pp` в слоте `Consequence:` первого замечания — величина, которую
  карточка не называет и которую показанная арифметика не выводит;
- `$0.77 − $0.66 = $0.11`, `38 147 × $0.11 ≈ $4 196` — здесь операция **показана
  и верна**, но сканер выражений §2.8 (V1.4) рвёт арифметический прогон на
  символе валюты `$`, поэтому читает `0.11` и `4 196` как невыведенные. Это
  ограничение §2.8, а не §2.10–§2.12; V1.6 его не трогала и чинить его надо
  отдельной задачей.

### Регрессия на реальных ответах V1.5

`analysis_scripts/FLOW-641/regression_v1_5_answers.py` прогоняет линтер V1.6 по
замороженным ответам V1.5 и сверяет с отчётами, которые сохранил тот прогон:

| Плечо | Сохранено V1.5 | Осталось под V1.6 | Добавилось |
|---|---|---|---|
| A | `E_FINDING_MECHANISM_UNGROUNDED`, `E_UNQUALIFIED_UNIVERSAL` | обе | `E_FINDING_NO_CONDITION`, `E_GROUNDS_UNLABELLED`, `E_TOPIC_MISSING` |
| B | `E_COMPUTED_NUMBER_FABRICATED` | она | `E_FINDING_NO_CONDITION`, `E_GROUNDS_UNLABELLED`, `E_PROPOSAL_NO_CONDITIONAL_FORM`, `E_TOPIC_MISSING` |

Ни один прежний код и ни один warning не потерян; всё добавленное — коды V1.6.
`conditional_form` у обоих ответов V1.5 — **0 / 7** и **0 / 8**.

Разбор по продуктовой рубрике — `rubric_run.md`.

