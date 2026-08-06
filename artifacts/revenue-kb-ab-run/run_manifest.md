# RUN MANIFEST — Revenue KB V1 A/B inference run (FLOW-579)

- **Дата прогона:** 2026-08-04 (UTC, тайминги в таблице)
- **Модель:** `claude-fable-5` (одна и та же для всех 12 запусков), Claude Code CLI 2.1.221, headless `claude -p`
- **Prompt:** `revenue-kb-v1/validator_prompt_v1.md` V1 frozen, sha256 `c464680baf9c53c5226421b3ee344770fe79a442e31fceff0f40f0988dc89e1b` — байт-в-байт одинаков в обоих плечах (единственная разница входов — блок KNOWLEDGE CONTEXT)
- **KNOWLEDGE CONTEXT (только плечо B):** `knowledge_base.md` + `\n\n---\n\n` + `pattern_cards.md`, sha256 `76da36323b75c48c39ca25af43d279ab2144eb0a07d5c189361089e22fe08f8d` (совпадает с FREEZE_MANIFEST)
- **Blind-карточки:** `revenue-corpus-prep-v1/holdout-blind/RH-01…06.md`, sha256 совпали с `BUNDLE_MANIFEST.md` (см. `preflight_report.txt`)

## Механика изоляции (одинакова для всех 12 запусков)

Каждый запуск — отдельный headless-процесс с чистым контекстом:

```
claude -p --tools "" --strict-mcp-config --mcp-config '{"mcpServers":{}}' \
  --setting-sources "" --model claude-fable-5 --no-session-persistence
```

- инструменты и MCP отключены; настройки/CLAUDE.md/память не загружаются; cwd — пустая
  изолированная директория вне проектов; сессия не сохраняется; web/поиск недоступны;
- вход подавался одним файлом в stdin: текст `validator_prompt_v1.md`, в котором
  `{EXPERIMENT_CARD}` заменён на blind-карточку; в плече B `{KNOWLEDGE_CONTEXT}` заменён на
  KNOWLEDGE CONTEXT, в плече A блок `<knowledge-context>…</knowledge-context>` удалён целиком
  (протокол §1: «блок отсутствует»; строка промпта «If the block above is empty or absent…»
  сохранена);
- 12 независимых процессов, никакого переноса контекста между кейсами и плечами.

## Запуски

| Плечо | Кейс | Start (UTC) | End (UTC) | Exit | Input sha256 | Output sha256 |
|---|---|---|---|---|---|---|
| A | RH-01 | 2026-08-04T17:49:53Z | 2026-08-04T17:51:09Z | 0 | `bf68405d277b8965a160a030bb3c4ea96b872b3f144706707f42dd48bcf36674` | `94e66edd1b90b13a5c8b52ad94ed10b8f76bc5ba41146b774065c45dbaba75ae` |
| A | RH-02 | 2026-08-04T17:49:53Z | 2026-08-04T17:50:37Z | 0 | `2c0b4e4200389cd33a19f6e2110dbaf6bd85fc775cfcefc88eb393073b6d14a8` | `d7210656db86ae8f332b362025b17858748fa806ac72a010575f3728833f4c9b` |
| A | RH-03 | 2026-08-04T17:49:53Z | 2026-08-04T17:50:41Z | 0 | `a5833ffd1cd0a45a533cdb04e1b93f9e207aae31a304c6cf8e2206838afa4f23` | `316c27969d214e7d9e78ce20dc033397cf6d3ee85c4375c8374894b258e05de4` |
| A | RH-04 | 2026-08-04T17:49:53Z | 2026-08-04T17:50:42Z | 0 | `1ec1ed613971bc766d8f47d1b126608dd0e4f8cb387addc600c1ccccb96bc9e3` | `cbd699c26202d76e8da087f21557c1431498d34267e71d40b2a8b16ce06bdf48` |
| A | RH-05 | 2026-08-04T17:49:53Z | 2026-08-04T17:50:33Z | 0 | `d266825fb1529612b690af4fd3d2fdfc01eafb9a9160e28760ab73843b7d2ae0` | `f290e68c2929895a38ad1e11f18f4a070ab798d133ca3378854fd62b12c3bba6` |
| A | RH-06 | 2026-08-04T17:49:53Z | 2026-08-04T17:50:34Z | 0 | `13877a88aa4f0e05ebb5fa724866bd442e49c6b64977ff55a3458df616a089d4` | `fec290fa8fef8e8af13428cd8dbaea59767aa9c0e1f90b3b53157bf1e5bef100` |
| B | RH-01 | 2026-08-04T17:50:33Z | 2026-08-04T17:52:43Z | 0 | `630bccec2fc5d05b7bad36b90f0d9c780a661b4286b93782e27c19c42f3301de` | `502b700b6ce5b3cafe860c35e8e0456e430b2d185f0462898e955c7349d6b787` |
| B | RH-02 | 2026-08-04T17:50:34Z | 2026-08-04T17:52:05Z | 0 | `3630eaf4e72eea449a8fbb5b2f9ddb6e3cb6c9cfce1827ed749624d5a087162e` | `50a3a6ab40249285f460082b3a79e5a835c37dec16c6f990e729bdc054ff5f79` |
| B | RH-03 | 2026-08-04T17:50:37Z | 2026-08-04T17:52:17Z | 0 | `d42103ed83ab89067a86266d3ada5b5d866efcd7017c3efa8f47e75fb73e027a` | `cad25be656b8bec488f0bf69f2b2ad6a5ef6c48d613b9175795132bbb4f1564f` |
| B | RH-04 | 2026-08-04T17:50:41Z | 2026-08-04T17:52:19Z | 0 | `d6cdf5a389ec56d008b10fdaa2e315886b8f205b9fbd8c7a3cc5a046fb679eca` | `21f5e6e9d4420b049fff5905e5e7426fcc7439c061779dab92ece7b2e2ad0e4a` |
| B | RH-05 | 2026-08-04T17:50:42Z | 2026-08-04T17:52:04Z | 0 | `138d2e7d06df9f381b37e9cb5990509c4a67c1b3c6e3499fc28e3a5e62eba8f8` | `0f13f41dbce6c722e217c71d7332d18614d838c4e613a31e025e092205bf4e2a` |
| B | RH-06 | 2026-08-04T17:51:09Z | 2026-08-04T17:52:55Z | 0 | `562d5dba1bc083cf2860ef40512f0f57b03d65b67dcc419d88aee934ad52d273` | `26b7147abd8e266225699cfb3ec9375a3d0672b2b321407687d8d946004fd97b` |

Ответы сохранены verbatim: `arm-a/RH-0x.md`, `arm-b/RH-0x.md` — байт-в-байт stdout.

## Blind-пары

`blind-pairs/RH-0x-X.md` / `RH-0x-Y.md`; mapping X/Y↔A/B — по одному случайному биту
(`secrets.randbits(1)`) на кейс, записан в `arm_mapping_sealed.md` (sealed; оркестратор и
судьи не читают его до заморозки pairwise-вердиктов C1–C4, C6).

## Зафиксированные решения

1. Плечо A = промпт с полностью удалённым блоком `<knowledge-context>` (протокол §1 «блок
   отсутствует»), без добавления каких-либо строк-заменителей (микро-отклонение FLOW-570
   «Historical product knowledge is not provided.» НЕ воспроизводится — в V1-промпте есть
   явное правило про отсутствующий блок).
2. Оркестратор не загружал содержимое ответов в свой контекст: только хеши и структурные
   проверки скриптом.
3. Унаследованное ограничение дизайна: verbatim-ответы содержательно маркируют плечо
   (B цитирует source ID T*-**/P-**). Имена файлов пар и порядок плечо не выдают.
