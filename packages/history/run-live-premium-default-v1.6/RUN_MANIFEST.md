# RUN MANIFEST — validator V1.6 on «Premium tab by default for top propensity decile»

Живой прогон валидатора на **новом** кейсе (первый вне Official Tabs). Бандл —
`../revenue-kb-v1.6/`. Только плечо B (с базой знаний): задача — разбор живой
гипотезы, а не A/B-оценка валидатора, поэтому контрольное плечо A не собиралось.

## Что валидировалось

Confluence **828875488**, space CRO — «[2026-08-10] UG iOS: Paywall — Premium
tab by default for top propensity decile [2026-XX-XX]», **версия 10**.
Карточка получена `bash scripts/cnfl pull 828875488` +
`python3 scripts/extract_text.py 828875488 40000` из
`~/my-proj/work/automations/confluence_tools`, дата вытяжки 2026-08-11.
Первичный экстракт сохранён как `card_raw_828875488.md`; в карточку добавлен
только двухстрочный provenance-заголовок, как во всех прежних прогонах.

```
a268709b3efa0faf1201e896895223d6a942bbf6779b5d5bc5487e591b82dfcd  inputs/experiment_card.md (14 025 bytes)
```

## Входы инференса

Собраны детерминированно `build_inputs.py` (stdlib-only): секция `## PROMPT`
промпта V1.6, подстановка `{KNOWLEDGE_CONTEXT}` и `{EXPERIMENT_CARD}`.

```
db1c0c350e2be516b86aed41005058a2e5132da74beb4269b7a12a57f0e51dc8  inputs/arm-b.md (148 338 bytes)
85f643999b2638ea1ba0acb003028929a4cf178b2bf9b2855cf00af3d40540f3  KNOWLEDGE_CONTEXT (111 469 bytes)
```

Frozen-файлы бандла V1.6 — хеши сверены с `FREEZE_MANIFEST.md` V1.6, совпадают:

```
f5d60e65ca328d85f30a5300f2584fda3fa58fbf81b327653d0db779541a3d4c  ../revenue-kb-v1.6/knowledge_base.md
b66247b43bf96d2683e1236fc92063d21b84322f1b86a0bfa75ba87a4e0b7703  ../revenue-kb-v1.6/pattern_cards.md
a0191e948059698b6d25e578c191ed3daca396a9612b276af404cef18067d247  ../revenue-kb-v1.6/validator_prompt_v1_6.md
a7b0c18749a114667feaab02bfeefbdc5ad5aef0f0fbfbb1786d5f6f06cdf9eb  ../revenue-kb-v1.6/linter.py
```

KNOWLEDGE_CONTEXT побайтово тот же, что в прогоне FLOW-641 (Official Tabs V1.6).

## Инференс

Headless, изолированный контекст, из пустого рабочего каталога, без инструментов,
MCP и файлов:

```
claude -p --model claude-opus-5 --settings '{}' \
  --strict-mcp-config --mcp-config '{"mcpServers":{}}' \
  --disallowed-tools "Bash,Read,Write,Edit,Glob,Grep,WebFetch,WebSearch,Task,NotebookEdit,TodoWrite" \
  --append-system-prompt "Write the entire answer in English." \
  < inputs/arm-b.md > outputs/arm-b.md
```

```
6b6e2d75095acee9eb656b058bd1eb4e67f957929fe2181951082a130d94b3bd  outputs/arm-b.md (13 523 bytes, 2 023 words)
```

## Линтер

```
python3 ../revenue-kb-v1.6/linter.py outputs/arm-b.md \
    --kb ../revenue-kb-v1.6/knowledge_base.md \
    --patterns ../revenue-kb-v1.6/pattern_cards.md \
    --card inputs/experiment_card.md > outputs/arm-b.lint.json
```

## Результат

| Плечо | Линтер | Замечаний | `[stop]` | Аналоги | Роли | Ошибок | Условная форма | Тем / коллизий | Generic |
|---|---|---|---|---|---|---|---|---|---|
| B, с базой | FAIL | 5 | 3 | T3-03 L2/L2, T3-06 L3/L3 — расхождений нет | обе | 2 (§2.8) | **6 / 6** | 10 / **0** | **0** флагов, 1 из 1 предложения и 5 из 5 `Fix:` заякорены |

Ни одного `E_TOPIC_*`, `E_FINDING_NO_CONDITION`, `E_GROUNDS_UNLABELLED`,
`E_PROPOSAL_NO_CONDITIONAL_FORM`, `E_CONSEQUENT_NO_DIRECTION`,
`E_PROPOSAL_UNANCHORED`, `E_GENERIC_UI_ADVICE`, `E_UNQUALIFIED_UNIVERSAL` — все
правила V1.6 (14, 15, 16) соблюдены с первого прогона на незнакомом кейсе.
Единственный warning — `W_MAIN_OVER_CAP`: 1 136 слов при капе ~550.

### Обе ошибки — известное ограничение §2.8 на символ валюты

Сканер выражений §2.8 (введён в V1.4) рвёт арифметический прогон на `$`, и это
уже зафиксировано как дефект прогона FLOW-641 (там он дал 5 из 5 ошибок плеча A).
Здесь он дал оба FAIL-кода, при верной по существу арифметике:

- `E_COMPUTED_NO_OPERATION` в замечании 3 (`tour-surface-zero-addressable`):
  операция **написана** — `$9,459/day × 15% ≈ $1,419/day` (проверено: 1 418,85), но
  из-за `$` линтер не увидел в предложении ни чисел, ни операции;
- `E_COMPUTED_NUMBER_FABRICATED` в замечании 5
  (`feature-surface-bundle-price-gap`): цепочку `1,083 ÷ 15 ≈ 72` линтер принял, а
  следующий шаг `72 × $28.50 ≈ $2,058/day` не распознал по той же причине.
  Проверено: 72,2 × 28,50 = 2 057,7 ≈ 2 058.

Ни одно число обоих замечаний не взято из базы знаний — все принадлежат карточке.
Содержательных нарушений политики свидетельств в ответе нет. Дефект сканера
остаётся открытым и требует отдельной задачи (он не относится к правилам V1.6).

### Проверка чисел ответа против карточки

Выборочно сверены и совпадают: 4 805 и 1 185 (sample size), 17,43 %, 4,61 %,
58,8 %, 64,24 %, 4,37 %, 28,4 %, 7,88 % / 5,73 %, 1 373 users/day, 14,2 % / 86 %,
$6,89, $22,09 / $50,59 / $28,50, $2,344/day, $9,459/day, 1 083 из 1 235,
2 646 из 2 647, 6,3 / 13,5 дня, UMN-12572. Арифметика всех пяти операций
замечания 2 пересчитана и верна.

## Замечание о хранении

Бандл `revenue-kb-v1.6` и этот прогон лежат вне git-репозитория
`~/revenue-validator` (там `packages/current/` до сих пор указывает на v1.4).
Консолидация v1.5/v1.6 и живых прогонов в репозиторий не выполнена.
