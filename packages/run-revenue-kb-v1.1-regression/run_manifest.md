# RUN MANIFEST — Revenue KB/Validator V1.1 regression A/B run (FLOW-586, Phase B)

- **Дата прогона:** 2026-08-05 (UTC, тайминги в таблице)
- **Модель:** `claude-fable-5` (одна и та же для всех 12 запусков; та же, что в FLOW-579), headless `claude -p`
- **Prompt:** `revenue-kb-v1.1/validator_prompt_v1_1.md` V1.1 frozen, sha256 `bb2296b6a98d16f4eee2f33bff9707c5c6248ab8f322f982c7885bcbd93cf380` — байт-в-байт одинаков в обоих плечах (единственная разница входов — блок KNOWLEDGE CONTEXT)
- **KNOWLEDGE CONTEXT (только плечо B):** `knowledge_base.md` + `\n\n---\n\n` + `pattern_cards.md` (V1.1), sha256 `ae980e466379392e751e714c2abe2566a76f3c3880c8437ffd6a3b62ac6b91df` (совпадает с V1.1 FREEZE_MANIFEST)
- **Blind-карточки:** `revenue-corpus-prep-v1/holdout-blind/RH-01…06.md` (frozen FLOW-575, не редактировались), sha256 совпали с `BUNDLE_MANIFEST.md` (см. `preflight_report.txt`)
- **Протокол:** `revenue-corpus-prep-v1/EVALUATION_PROTOCOL.md` V1 frozen; пороги §6 не менялись. Это regression rerun по policy §7 (evidence_policy) после формального NO FLOW-579.

## Механика изоляции (одинакова для всех 12 запусков; идентична FLOW-579)

```
claude -p --tools "" --strict-mcp-config --mcp-config '{"mcpServers":{}}' \
  --setting-sources "" --model claude-fable-5 --no-session-persistence
```

- инструменты и MCP отключены; настройки/CLAUDE.md/память не загружаются; cwd — пустая
  изолированная директория вне проектов; сессия не сохраняется; web/поиск недоступны;
- вход одним файлом в stdin: `validator_prompt_v1_1.md` с `{EXPERIMENT_CARD}` = blind-карточка;
  в плече B `{KNOWLEDGE_CONTEXT}` = KNOWLEDGE CONTEXT V1.1, в плече A блок
  `<knowledge-context>…</knowledge-context>` удалён целиком;
- 12 независимых процессов, никакого переноса контекста между кейсами и плечами;
- ground truth, arm mapping FLOW-579, комментарии FLOW-579 и evaluation-артефакты
  в контексты inference не подавались; runner их не читал.

## Машинный линтер (Stage 3)

Детерминированный `revenue-kb-v1.1/linter.py` (frozen, sha256 в V1.1 FREEZE_MANIFEST)
прогнан на всех 12 verbatim-ответах: плечо B — KB-режим, плечо A — `--no-kb-arm`.
JSON-отчёты: `linter/arm-*-RH-0x.json`. Повторный прогон всех 12 дал байт-идентичные
отчёты (детерминизм подтверждён на реальных ответах). Перезапусков inference по
результатам линтера не было (селекции нет; результаты — вход оценки Фазы C).

Итоги: a/RH-01=PASS, a/RH-02=PASS, a/RH-03=PASS, a/RH-04=PASS, a/RH-05=PASS, a/RH-06=PASS, b/RH-01=PASS, b/RH-02=PASS, b/RH-03=PASS, b/RH-04=PASS, b/RH-05=PASS, b/RH-06=PASS

## Запуски

| Плечо | Кейс | Start (UTC) | End (UTC) | Exit | Linter | Input sha256 | Output sha256 |
|---|---|---|---|---|---|---|---|
| A | RH-01 | 2026-08-05T08:25:59Z | 2026-08-05T08:26:56Z | 0 | PASS | `970326897a4fdfb5c236db32c854c89ea0cefe1d53f387090bb2aff5b30df2c8` | `6e981bc182c13d947f5b83d5b9499654a8f0e30df67356acc56bf9bbc6b6fa05` |
| A | RH-02 | 2026-08-05T08:25:59Z | 2026-08-05T08:26:34Z | 0 | PASS | `4f9dc56e6be662a3dc0cd41b84c5390124acddecb18ea835d018ec11b8b61053` | `1ed7bb3fa8d70562f847fd4da0af916092676fd9e6fab732c1be682c8b83b664` |
| A | RH-03 | 2026-08-05T08:25:59Z | 2026-08-05T08:26:54Z | 0 | PASS | `9928fc1f1f2608c33a2d925764c14343070cb31ff2bc9b589e834f32de402e4d` | `5af068e0e8ef51bb4d060a19ad26be310da035c5e48410a41fa9b53c20e901a5` |
| A | RH-04 | 2026-08-05T08:25:59Z | 2026-08-05T08:26:54Z | 0 | PASS | `c44e2ab86a5e237a7fd2ae358fc836821b262334f41783ea37e197e806eddc9e` | `7c72aa31a80f13a8694e9822e4d5eeec923bb1e4b4fc08052e55490a8fcd4eee` |
| A | RH-05 | 2026-08-05T08:25:59Z | 2026-08-05T08:26:44Z | 0 | PASS | `c5af67e3fa0ed2e1377b5ce624f7dfcdd3e06e935efc0a361af6f87f5eb091c4` | `cf5e9c8c943e5f5ad99acd9a7e915b8c6b5ec8f85a3186e8809383a2847b4cf9` |
| A | RH-06 | 2026-08-05T08:25:59Z | 2026-08-05T08:26:48Z | 0 | PASS | `6eba8935c4b33e0e7fba942c3397fc74db1210cef13ef8e6e5e0bf9c3603a9a3` | `7c2e792b7be6359aa5515d0e793928300a0500d598862301a6f83d82504732dd` |
| B | RH-01 | 2026-08-05T08:26:34Z | 2026-08-05T08:29:43Z | 0 | PASS | `27f999f8358312747bdac1ff30171856d4a97bd734bcdbe88a50cc76c6993e50` | `ef821fededed4bbdd8e947b56cc4afe4894b3f24cfb0bc747e9b7cf904b80a4e` |
| B | RH-02 | 2026-08-05T08:26:44Z | 2026-08-05T08:28:55Z | 0 | PASS | `7d16fa7d4399fccba0a9e229c28b2cb369f0db5818534c765c712784483a4f2a` | `92e343f676c383f5e1fab2dfc255a748563a4b7e0d9b3ea30efb7862bc95fb65` |
| B | RH-03 | 2026-08-05T08:26:48Z | 2026-08-05T08:30:09Z | 0 | PASS | `3d3abf2e572c0df67f9c49ef804732f44772013cb9e14d37daeb2d949c8951bc` | `110558c25702aa101e721b745a6db6701c2bd09dc5d32ea8cf0d76d192aaa076` |
| B | RH-04 | 2026-08-05T08:26:54Z | 2026-08-05T08:29:55Z | 0 | PASS | `c903e41e50cdc2020016f2e68fa70d94593950b1abd9502deb03ed11135496c7` | `cdcae594ea0b89d77a98f3e1076dbea3c5e2784598e2eb94b215d2233541073f` |
| B | RH-05 | 2026-08-05T08:26:54Z | 2026-08-05T08:28:31Z | 0 | PASS | `42d222b286e6e24d2b95b615d6cd6f3412db997b2c2c6e9ba7687ed94509d763` | `c78e56a92fe66f2db95603c539e5c33692d60dbb35634fabc5e515dec2fc0ac2` |
| B | RH-06 | 2026-08-05T08:26:56Z | 2026-08-05T08:30:08Z | 0 | PASS | `de1a32c612304794019e04171ca07a8311c7fc1a5368d2570c3f4e292b61f3a6` | `0140ae60de285f3cf92aaa4d367b906d0526e27b3a17a0a52b2753b348c37744` |

Ответы сохранены verbatim: `arm-a/RH-0x.md`, `arm-b/RH-0x.md` — байт-в-байт stdout.

## Blind-пары

`blind-pairs/RH-0x-X.md` / `RH-0x-Y.md`; mapping X/Y↔A/B — по одному случайному биту
(`secrets.randbits(1)`) на кейс, записан в `arm_mapping_sealed.md` (sealed; runner,
оркестратор и судьи не читают его до заморозки pairwise-вердиктов C1–C4, C6).

## Зафиксированные решения

1. Плечо A = промпт с полностью удалённым блоком `<knowledge-context>` (протокол §1
   «блок отсутствует»), без строк-заменителей — как в FLOW-579.
2. Runner не загружал содержимое ответов в свой контекст: только хеши, структурные
   проверки и линтер скриптом.
3. Унаследованное ограничение дизайна: verbatim-ответы содержательно маркируют плечо
   (B цитирует source ID T*-**/P-**). Имена файлов пар и порядок плечо не выдают.
4. Linter-фейлы (если есть) не скрываются и не чинятся перезапуском — они входят в
   regression-оценку как есть.
