# FREEZE MANIFEST — Revenue Knowledge Base V1 (FLOW-578)

Дата freeze: **2026-08-04**. После этой даты файлы бандла не меняются;
любое изменение — новая версия KB с новым манифестом и новым прогоном
протокола. Хеши считаются по байтам файлов (SHA-256).

## Состав KNOWLEDGE CONTEXT плеча B (зафиксировано)

Конкатенация ровно двух файлов в порядке:
`knowledge_base.md` + разделитель `\n\n---\n\n` + `pattern_cards.md`.

```
76da36323b75c48c39ca25af43d279ab2144eb0a07d5c189361089e22fe08f8d  KNOWLEDGE_CONTEXT (50 415 bytes)
```

Плечо A получает тот же промпт без KNOWLEDGE CONTEXT. Любое другое включение
файлов во вход инференса — нарушение протокола.

## Frozen combined validator prompt V1

```
c464680baf9c53c5226421b3ee344770fe79a442e31fceff0f40f0988dc89e1b  validator_prompt_v1.md
```

Написан clean-room (без чтения V0-бандла); идентичен для плеч A/B.

## SHA-256 файлов бандла

```
4ca6e0b4d02c199ee8fe4269fa615c9268bd4cfa66f81811a61d6d400ba775af  README.md
996430747aae1f478d3ad4c51764669b2af79111ef4506b1c666cab98c0efe15  corpus/20260804_flow578_kb_leakage_scan_and_freeze.py
09153074ed5183d1a27590cff2d459547d9840b8bafa3488fc6ba433784fe5cd  corpus/20260804_flow578_sanitize_inventory_crossrefs.py
d4f176462f5f57679ca0eb06145ba3859958f5af4bebc5da7f7884f11a9c5bde  corpus/20260804_flow578_strip_holdout_from_inventory.py
f69b930aa2a6740e3c6af792cd7f1b6579ee6192ca57a8c8959eb61175497d8d  corpus/inventory_cleaned.yaml
1a159f9f20f1c24afcf8aafe3409b1b8f7facd982d471c12242e1001df62d7f3  corpus/summary_table_cleaned.md
f631d5d16d55b6ed90d657099f36dc2b919d3669a15a54c2d13d96e0c202bbe2  knowledge_base.md
a3f3b7ac9cb0991a29558dee28054c926a0d065018b2e27f9ff5a270e75c04a0  pattern_cards.md
c464680baf9c53c5226421b3ee344770fe79a442e31fceff0f40f0988dc89e1b  validator_prompt_v1.md
```

`FREEZE_MANIFEST.md` в список не входит (самоссылка).

## Provenance (вход и его версии)

- Вход: inventory FLOW-577 **V0.1** (24 кейса, сверка с Confluence
  2026-08-04), каталог
  `flow-577-04-revenue-flow-2/output/flow577_revenue_inventory/`.
- Из входа до чтения удалены 6 holdout-записей и зачищены кросс-ссылки —
  скрипты в `corpus/`, порядок описан в `README.md` § «Исключение нового
  holdout». Очищенный вход заморожен как `corpus/inventory_cleaned.yaml`
  (18 кейсов).
- Модель близости: FLOW-574 (relevance model V0, L1–L3).
- Карта flow: FLOW-576 (Revenue User Flow V0, S0–S9).
- Уроки ex-holdout Interstitials-кейсов IH-01…04 включены через записи
  T1-07…T1-10 входного inventory (источник разметки — GT-карточки FLOW-571,
  через FLOW-577; бандлы `interstitials-*` builder'ом не читались).

## Leakage-скан (2026-08-04, скрипт
`corpus/20260804_flow578_kb_leakage_scan_and_freeze.py`)

Проверка всех файлов бандла на идентификаторы исключённых holdout-кейсов
(ключи записей, pageId, AB id как отдельные токены, Jira-ключи, биграммы
названий):

| Файл | Вердикт |
|---|---|
| `knowledge_base.md` | **PASS** (0 упоминаний) |
| `pattern_cards.md` | **PASS** (0 упоминаний) |
| `validator_prompt_v1.md` | **PASS** (0 упоминаний) |
| `corpus/inventory_cleaned.yaml` | **PASS** (0 упоминаний) |
| `corpus/summary_table_cleaned.md` | **PASS** (0 упоминаний) |
| `README.md` | ожидаемые: перечисление ключей исключаемых записей в инструкции (без названий/исходов) |
| `corpus/*.py` | ожидаемые: скрипты реализуют исключение и по необходимости содержат сам чёрный список |

Итог: **PASS** — весь контент, доступный inference-агенту как вход
(KNOWLEDGE CONTEXT + промпт), и все данные корпуса свободны от
идентификаторов и пересказов holdout-кейсов. Провенанс-файлы содержат только
сам чёрный список (это инструмент исключения, не знание об исходах); каталог
`corpus/` для inference-агента запрещён (см. README, таблица доступа).

## Дисклозы

См. `README.md` § «Дисклозы»: builder видел однострочные классы исходов
holdout в Linear-комментарии FLOW-575 (bootstrap-неизбежность, кейсы
полностью исключены из KB) и 5 строк парафраз при зачистке кросс-ссылок
(вычищены; соответствующие утверждения KB опираются на собственные страницы
разрешённых кейсов).
