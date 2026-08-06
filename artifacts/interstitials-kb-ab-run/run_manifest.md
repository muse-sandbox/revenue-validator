# RUN MANIFEST — Interstitials KB A/B inference run (FLOW-570)

- **Дата прогона:** 2026-08-04 (08:17–08:23 UTC)
- **Модель:** `claude-fable-5` (одна и та же для всех 8 запусков), Claude Code CLI 2.1.221, headless `claude -p`
- **Prompt:** `combined_validator_prompt.md` V0 frozen, sha256 `43ff7f52b3dc51aefcfe2a1dc596ea54241ff3afe3fa17e838116222df65d612` — байт-в-байт одинаков в обоих плечах, не изменялся
- **Knowledge base (только плечо B):** `knowledge_base.md` sha256 `dc04a072dd84a4ee29dc88059518c0b2d011033c5f841d133ed583d7f0b616c3` + `pattern_cards.md` sha256 `0bd1f2e06b53a53db43c4b821922fa7f183645b7cb0afd18ca6ad3836685e365` (frozen V0, без изменений)
- **Blind-карточки:** `holdout-blind/IH-01.md…IH-04.md`, sha256 совпали с `BUNDLE_MANIFEST.md` корпуса interstitials-corpus-prep (см. Preflight ниже)

## Preflight (пройден)

1. SHA-256 всех 7 файлов frozen KB bundle совпали с `FREEZE_MANIFEST.md` (interstitials-kb-v0).
2. SHA-256 всех 4 blind-карточек совпали с `BUNDLE_MANIFEST.md` корпуса (строки `holdout-blind/IH-0x.md`):
   - `38c58a2a761823105f21493e6518f98e89cfa1d8e2a48585beab43d19f3b6169  IH-01.md`
   - `179cd5ad284ae6c59a4beeb04837c972f86a9bddeceaea359b0a7e9fae573664  IH-02.md`
   - `9381137e3faee6547f15ead3dd609b9749bcb9800e2556c632d2fad2fbfefd6c  IH-03.md`
   - `c7d5494b93cf703a482ab99780b176b1ee93c44efee988b3da2953441f6bc996  IH-04.md`
3. Модель, дата и версия prompt зафиксированы (см. выше).

## Механика изоляции (одинакова для всех 8 запусков)

Каждый запуск — отдельный headless-процесс `claude -p` с чистым контекстом:

```
claude -p --tools "" --strict-mcp-config --mcp-config '{"mcpServers":{}}' \
  --setting-sources "" --model claude-fable-5 --no-session-persistence
```

- инструменты полностью отключены (`--tools ""`);
- MCP-серверы отключены (`--strict-mcp-config` + пустой конфиг);
- пользовательские/проектные настройки, CLAUDE.md и память не загружались (`--setting-sources ""`, cwd — пустая изолированная директория вне каких-либо проектов);
- сессия не сохранялась (`--no-session-persistence`);
- web/поиск недоступны (инструментов нет);
- никакого переноса контекста между кейсами и между плечами: 8 независимых процессов.

Вход подавался в stdin одним файлом: текст `combined_validator_prompt.md`, затем блок
`=== BEGIN/END HYPOTHESIS DOCUMENT ===` с карточкой, затем:

- **плечо A** — строка `Historical product knowledge is not provided.` (блок KNOWLEDGE CONTEXT отсутствует);
- **плечо B** — блок `=== BEGIN/END KNOWLEDGE CONTEXT ===` с полными текстами `knowledge_base.md` и `pattern_cards.md`.

## Запуски

| Плечо | Кейс | Start (UTC) | End (UTC) | Exit | Input sha256 | Output sha256 |
|---|---|---|---|---|---|---|
| A | IH-01 | 2026-08-04T08:17:33Z | 2026-08-04T08:20:22Z | 0 | `b371ac95aabc9be71cdedfee59dc8843cc72d8f4a0fcdbc2b28e541eb09dd348` | `ee73ff77e9d2be35ee301ba2c66f8853fe47c3316e570b2de112fac9016d1695` |
| A | IH-02 | 2026-08-04T08:17:33Z | 2026-08-04T08:20:48Z | 0 | `a6e73329b584ee12421d6b42e27901488854bb8fcdc562dffa3ab5179cbfe2ff` | `f6d6d2e424649c8e1b9bd8fe7ae454554ef78ea68b032b3cf7c5f6a3596d6d1e` |
| A | IH-03 | 2026-08-04T08:17:33Z | 2026-08-04T08:20:43Z | 0 | `c2af0b5c396d0e15b330931656881376615f63ea46c62225114063e6fa84414f` | `d83f7e6fadecd593e32c0cd4ab630c88e3c2a8f8c444a7ddc6c843004729b599` |
| A | IH-04 | 2026-08-04T08:17:33Z | 2026-08-04T08:20:58Z | 0 | `bc97f03a75dc458bebb771e0461587c259208e4fdba47ca94ba8d8ef4adbc3c7` | `19f3cad95d68fbc662dd1b953e3cc15ad9ffe3a9e1dd202d6d3ac61f1ee1913a` |
| B | IH-01 | 2026-08-04T08:17:33Z | 2026-08-04T08:22:38Z | 0 | `e30048d234a9084fdebe36cf34d825ffdb73820f6a1c0e7ae58e4c1b365f00e9` | `7f6d453af4f6160268050c8e4326a68eee6d78e77db062d17a799eebea882108` |
| B | IH-02 | 2026-08-04T08:17:33Z | 2026-08-04T08:22:32Z | 0 | `d0cba26eae40f831ffc3463b9a0878056d69a3782d746116d0ed2e838279567f` | `c5aee1b25ce665b59fd586d0a5ac80589c9966b8aabd867e9da53d47bd8cdcdb` |
| B | IH-03 | 2026-08-04T08:17:33Z | 2026-08-04T08:22:21Z | 0 | `f93feefeaf4e52b1ff1c4e66a3aae38e37f43ca6dd6a5f0eb456e063da810bc3` | `b2d6685e2b142808005fb45b06c39ec378e5a0b2adf126e8a70b0718a8dd534f` |
| B | IH-04 | 2026-08-04T08:17:33Z | 2026-08-04T08:21:58Z | 0 | `ec955d8343d80cec2bb7f94b608b0de3613be7327a3687d1ebbcca3bfd01c63f` | `aaedbb9a544238046664590c45dfa4bd5bd798e81f42e65c58c4cebc4574e4b2` |

Ответы сохранены verbatim: `arm-a/IH-0x.md` и `arm-b/IH-0x.md` — байт-в-байт stdout соответствующего запуска.

## Зафиксированные решения и отклонения

1. **Состав KNOWLEDGE CONTEXT плеча B.** Текст задачи FLOW-570 упоминает только `knowledge_base.md`, однако pre-registered `EVALUATION_PROTOCOL.md` (§1), `FREEZE_MANIFEST.md` и сам `combined_validator_prompt.md` (раздел I.2 и A/B-инвариант) единообразно определяют KNOWLEDGE CONTEXT как `knowledge_base.md` + `pattern_cards.md` (source ID формата `IKB-Pxx` существуют только в pattern_cards). Менять протокол запрещено, поэтому плечо B получило оба файла — по frozen-протоколу.
2. **Строка плеча A.** По требованию задачи во вход плеча A добавлена строка `Historical product knowledge is not provided.` после блока документа. Протокол описывает вход A как «только карточка»; строка не несёт знаний и дублирует правило самого промпта об отсутствующем KNOWLEDGE CONTEXT. Зафиксировано как микро-отклонение от буквы протокола в пользу буквы задачи.
3. **Ограничение blind-ревью (унаследованное от дизайна).** Ответы сохранены verbatim, поэтому содержимое пары само по себе может выдавать плечо (B цитирует source ID `KS-xx`/`IKB-…`; A содержит фразу «Knowledge context не предоставлен…»). Это свойство дизайна эксперимента, не этого прогона; имена файлов пар (`X`/`Y`) признак плеча не содержат.
4. Сравнение содержимого A и B не выполнялось; выполнены только автоматические структурные проверки (наличие проходов 1–3 в каждом ответе) без загрузки текста ответов в контекст оркестратора.

## Definition of Done

- 4/4 кейса обработаны в обоих плечах; всего 8 независимых запусков — да.
- Между плечами отличается только наличие KNOWLEDGE CONTEXT во входе — да (входы собраны конкатенацией одних и тех же frozen-файлов).
- Prompt и KB не менялись (хеши совпадают с FREEZE_MANIFEST) — да.
- Ground truth / outcomes не открывались — да (см. `clean_room_declaration.md`).
- Ответы сохранены verbatim и захешированы — да (таблица выше, `BUNDLE_MANIFEST.md`).
- X/Y-пары рандомизированы — да (по одному биту `/dev/urandom` на кейс; mapping в `arm_mapping_sealed.md`).
