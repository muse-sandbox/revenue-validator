# RUN MANIFEST — Revenue KB/Validator V1.2 regression A/B run (FLOW-593, Phase B)

- **Дата прогона:** 2026-08-05 (UTC, тайминги в таблице)
- **Модель:** `claude-fable-5` (одна и та же для всех 12 запусков; та же, что в FLOW-579/586), headless `claude -p`
- **Prompt:** `revenue-kb-v1.2/validator_prompt_v1_2.md` V1.2 frozen, sha256 `62a39eb89eede880b977310ac943e6fa73788f6da8daf2e7876dfb90ad818b4a` — байт-в-байт одинаков в обоих плечах (единственная разница входов — блок KNOWLEDGE CONTEXT)
- **KNOWLEDGE CONTEXT (только плечо B):** `knowledge_base.md` + `\n\n---\n\n` + `pattern_cards.md` (V1.2), sha256 `9949e10b34df6c2e67c14dcec30e2f00ef8c175bccc327d2c262e752ddd10df3` (совпадает с V1.2 FREEZE_MANIFEST)
- **Blind-карточки:** `revenue-corpus-prep-v1/holdout-blind/RH-01…06.md` (frozen FLOW-575, не редактировались), sha256 совпали с `BUNDLE_MANIFEST.md` (см. `preflight_report.txt`)
- **Протокол:** `revenue-corpus-prep-v1/EVALUATION_PROTOCOL.md` V1 frozen; пороги §6 не менялись. Это regression rerun фикса C6-класса поверх FLOW-586; порог не пересматривался после просмотра результатов.

## Механика изоляции (одинакова для всех 12 запусков; идентична FLOW-579/586)

```
claude -p --tools "" --strict-mcp-config --mcp-config '{"mcpServers":{}}' \
  --setting-sources "" --model claude-fable-5 --no-session-persistence
```

- инструменты и MCP отключены; настройки/CLAUDE.md/память не загружаются; cwd — пустая
  изолированная директория вне проектов; сессия не сохраняется; web/поиск недоступны;
- вход одним файлом в stdin: `validator_prompt_v1_2.md` с `{EXPERIMENT_CARD}` = blind-карточка;
  в плече B `{KNOWLEDGE_CONTEXT}` = KNOWLEDGE CONTEXT V1.2, в плече A блок
  `<knowledge-context>…</knowledge-context>` удалён целиком;
- 12 независимых процессов, никакого переноса контекста между кейсами и плечами;
- ground truth, arm mapping, комментарии и evaluation-артефакты FLOW-579/586
  в контексты inference не подавались; runner их не читал.

## Машинный линтер (Stage 3)

Детерминированный `revenue-kb-v1.2/linter.py` (frozen, sha256 в V1.2 FREEZE_MANIFEST)
прогнан на всех 12 verbatim-ответах: плечо B — KB-режим, плечо A — `--no-kb-arm`.
JSON-отчёты: `linter/arm-*-RH-0x.json`. Повторный прогон всех 12 дал байт-идентичные
отчёты (детерминизм подтверждён на реальных ответах). Перезапусков inference по
результатам линтера не было (селекции нет; результаты — вход оценки Фазы C).

Итоги: a/RH-01=PASS, a/RH-02=PASS, a/RH-03=PASS, a/RH-04=PASS, a/RH-05=PASS, a/RH-06=FAIL, b/RH-01=PASS, b/RH-02=PASS, b/RH-03=PASS, b/RH-04=PASS, b/RH-05=PASS, b/RH-06=PASS

## Запуски

| Плечо | Кейс | Start (UTC) | End (UTC) | Exit | Linter | Input sha256 | Output sha256 |
|---|---|---|---|---|---|---|---|
| A | RH-01 | 2026-08-05T17:20:41Z | 2026-08-05T17:21:49Z | 0 | PASS | `edfd810c0594a1ae69cbf5bf5b20d057ce25c61dccd6fd786f11d8eda97f3123` | `9b75b216d4522eccfccd84bd4fe218a77d27b5eedee1a0e42c580ffeafd5921a` |
| A | RH-02 | 2026-08-05T17:20:41Z | 2026-08-05T17:21:54Z | 0 | PASS | `e10cdbb40fe05139c7d5ad7ecc651b27511c36103c6250798179f381b389607f` | `c63f071da5562b8d37f41816e6c2bedb50d6e35782eee1bce977258bc2d9d325` |
| A | RH-03 | 2026-08-05T17:20:41Z | 2026-08-05T17:21:34Z | 0 | PASS | `304c3357e8309d282f45cd2e19009ba0da7a706db99557e4ffce5ea322e2877b` | `19d2c5b1a59b752171b4c2f555cb8535a7e1e40762f6fa8dba2f3d8c7c78420a` |
| A | RH-04 | 2026-08-05T17:20:41Z | 2026-08-05T17:21:45Z | 0 | PASS | `9f60ef19e12bdce53882d626bfcf96f97b330c91b58b073571591bd6ad77ff28` | `60e5f9edb08f5cf843ca3cc1876b4226abc2538475ef34261b1c848898c45cc5` |
| A | RH-05 | 2026-08-05T17:20:41Z | 2026-08-05T17:21:25Z | 0 | PASS | `daa04f8ae8a0b004d4c6b0ad9384f3221478dcfc3665ab6ef139bd08682844b6` | `904d9ea1ea256dd1ac6210553e01ac509a2b4d75c801ae9846cea02086c37f75` |
| A | RH-06 | 2026-08-05T17:20:41Z | 2026-08-05T17:21:39Z | 0 | FAIL | `18280b4b15d80edc1248c9c6be002c013db5f6e891be57d27aa8ab12c5fc5dea` | `16a9e66303bce9f6b6f89661eb160aaa10799d451d526e272bc5f7d2f02d11e0` |
| B | RH-01 | 2026-08-05T17:21:25Z | 2026-08-05T17:24:41Z | 0 | PASS | `272df9cc40ae0b838c5599867c94ebb8e489347973eec62e4847f3b9b0693109` | `cff9500a9897c702c8074fc007e96cfea6b80c13478b232e9ae2aa4f17f593a0` |
| B | RH-02 | 2026-08-05T17:21:34Z | 2026-08-05T17:25:35Z | 0 | PASS | `365fa98e7d6b09a59ac96425d55a7d0d49084a330be718f2ad6405fd6c54a40a` | `e8b131931c9c925542b7e77f9eeb81ffb8d876e3fff766a5a505ad01a032ed51` |
| B | RH-03 | 2026-08-05T17:21:39Z | 2026-08-05T17:24:42Z | 0 | PASS | `b6d9dfe509fc7b80a43dded93806f6f04b978d2c453f5f4871886bd02e0c1d71` | `39f55a501ad9013c7810684a9e8bbeb1a4b833e6833f4ddb16496dcc3119bb94` |
| B | RH-04 | 2026-08-05T17:21:45Z | 2026-08-05T17:24:26Z | 0 | PASS | `33de7560d9a9cdf3a1ae76081282583b02c8cd3df5111f64aaf72cadc9f49b20` | `f34a6577870289af2d2f10482f1b5a841f9156083f3ba5c3a0e0d74f6d796867` |
| B | RH-05 | 2026-08-05T17:21:49Z | 2026-08-05T17:23:35Z | 0 | PASS | `04c2ed464a783bf8d1c48477e7968f088018085f5d4fbabb455a0b298bbe982e` | `84b1c3f0a8b9e69354f15437e644f8e93be4a7e55e172d50f1d90c7d145ae910` |
| B | RH-06 | 2026-08-05T17:21:54Z | 2026-08-05T17:25:27Z | 0 | PASS | `daa6c11df16ec8c8952b647b132a6dd25ce3d67f1e63dec33ba34ef1e9f4fe55` | `e44c23c524d16cb6d46f7c70eece2e023e335d6a8e06da0c66c4657e0b6b7ae4` |

Ответы сохранены verbatim: `arm-a/RH-0x.md`, `arm-b/RH-0x.md` — байт-в-байт stdout.

## Blind-пары

`blind-pairs/RH-0x-X.md` / `RH-0x-Y.md`; mapping X/Y↔A/B — по одному случайному биту
(`secrets.randbits(1)`) на кейс, записан в `arm_mapping_sealed.md` (sealed; runner,
оркестратор и судьи не читают его до заморозки pairwise-вердиктов C1–C4, C6).

## Зафиксированные решения

1. Плечо A = промпт с полностью удалённым блоком `<knowledge-context>` (протокол §1
   «блок отсутствует»), без строк-заменителей — как в FLOW-579/586.
2. Runner не загружал содержимое ответов ни в один контекст модели: только хеши,
   структурные проверки и линтер скриптом.
3. Унаследованное ограничение дизайна: verbatim-ответы содержательно маркируют плечо
   (B цитирует source ID T*-**/P-**). Имена файлов пар и порядок плечо не выдают.
4. Linter-фейлы (если есть) не скрываются и не чинятся перезапуском — они входят в
   regression-оценку как есть.
