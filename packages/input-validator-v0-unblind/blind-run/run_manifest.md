# FLOW-546 — Blind run manifest

- **Дата прогона:** 2026-08-03 17:05–17:23 UTC (2026-08-04 00:05–00:23 локально, UTC+7)
- **Модель:** `claude-fable-5` (пиновано `--model claude-fable-5`; подтверждено полем `modelUsage` каждого ответа CLI)
- **Валидатор:** Validator V0, frozen 2026-08-03
- **Bundle:** `/Users/elzira/Documents/Codex/2026-08-03/users-elzira-obsidian-ug-ai-infrastructure/outputs/flow546-clean-input`
- **Runner:** `analysis_scripts/flow546_blind_run.sh` — на карточку отдельный изолированный headless-процесс `claude -p`: пустая рабочая директория вне репозитория, system prompt = verbatim `validator_v0_prompt.md` (`--system-prompt-file`), user input = verbatim одна HX-карточка (stdin), `--tools ""` (все инструменты отключены), `--strict-mcp-config` с пустым MCP-конфигом, `--output-format json`. Ответ сохранён байт-в-байт из поля `result` (`jq -j`). Каждый запуск — один turn, `stop_reason=end_turn`, `is_error=false`.

## Frozen Validator V0 (SHA-256, пересчитаны перед прогоном, совпали с `BUNDLE_MANIFEST.md` и `validator_v0_freeze.md`)

```text
61b2ee469049b1239705e3b4f4e5e30fb8043da10d126952fc90a0584e64b330  validator-v0/validator_v0_prompt.md   (использован как system prompt)
e485967eee82c67056bf2408a71087ed35ac6978d9bac3d77277c9c9467e3803  validator-v0/validator_v0_spec.md
371ba35f72d7529e671559e6441ca8f2aac9a8f1aec3104399ebcad643545698  validator-v0/validator_v0_criteria.md
02fa800a49adeb14b858adee3182493c0a12731813dd06cbe09d0740a03afe29  validator-v0/validator_v0_freeze.md
```

Примечание: `validator_v0_example.md` (хеш в freeze: `1ef4a34d…`) в clean bundle отсутствует намеренно и в прогоне не использовался; состав bundle соответствует заданию (ровно 4 файла `validator-v0/` + 8 карточек).

## Запуски (все входные SHA-256 совпали с `BUNDLE_MANIFEST.md`)

| Карточка | Начало (UTC) | Конец (UTC) | Длит., с | API duration_ms | Session id | Input SHA-256 | Output SHA-256 |
|---|---|---|---|---|---|---|---|
| HX-01 | 2026-08-03T17:05:05Z | 2026-08-03T17:07:36Z | 151 | 149340 | f7f7d948-25cf-4e9f-9634-04b56f17213c | `18fdea828da62494797a742dc55282f3dd18017d9d98fb4fde32189236ccf257` | `9d70f0696366722f0950b1d7b6744b13fc1cea8a5010b28a07934ee2d5267359` |
| HX-02 | 2026-08-03T17:07:36Z | 2026-08-03T17:09:33Z | 117 | 115056 | 6fc5464a-a8b8-4c5f-8666-3b7234f755e1 | `9f73f19c2a1216f7e601f6302d58021199c32d1270944b2aa8fedf561a473e1b` | `544225df05f1e58bd40b7eade25205252b44465af257d91ab503fee987815eb2` |
| HX-03 | 2026-08-03T17:09:33Z | 2026-08-03T17:11:41Z | 128 | 126656 | 61d264e2-51b5-4736-8c3e-02aa90507842 | `a459012b3a9bfd619577b5019902de0ed87c45bd8d05410c78270247deab4a2c` | `8997acc282a5e57d318958fc447d73003cea3502928e42a5da066e260c4f7d60` |
| HX-04 | 2026-08-03T17:11:41Z | 2026-08-03T17:13:42Z | 121 | 120207 | c3560be1-04f4-433a-94bf-b2c5a74609a4 | `925680ae8648bb0ebcb061616ab0c50c44e3f07197ca87f930e7eae3d8a091aa` | `a79f8f611ab0fad4e7affb12fdb19c97d18d418b8ea28730a7948fae686953ba` |
| HX-05 | 2026-08-03T17:13:42Z | 2026-08-03T17:16:32Z | 170 | 167519 | 864a4cfc-621a-4d80-9d1f-9fb954d91cce | `d06d68b9a200938c1f325d41bd1345d1a9e094ee372e774e06c0056a7637fbbd` | `9bbbc0de41ee9f3bd492f2e687137897e7ba4d13b6e423ca416e2e62fe56cec3` |
| HX-06 | 2026-08-03T17:16:32Z | 2026-08-03T17:18:39Z | 127 | 100649 | 2e103bb7-2d2d-4c96-a5ac-a8ff4ae02bc6 | `71a7d865ecaa5324f4c626d4d10a1dddd1e37424489ec072386e42bc9a5145b2` | `79be7ed68921f920569621804b299862d2cc43eaf4e764857099c318cb6a132c` |
| HX-07 | 2026-08-03T17:18:39Z | 2026-08-03T17:21:17Z | 158 | 157125 | 42389f45-7cca-46cf-8f41-ffe5bec226ee | `3f584939369af6b8a4801d6331bc030d657ea459dcda2666b39690242b1874fc` | `87ba6e85b195e9262099bec62adb6b573f29b5f4541233fe42d9bd2ee62619b3` |
| HX-08 | 2026-08-03T17:21:17Z | 2026-08-03T17:23:19Z | 122 | 117157 | a53695f4-4ff4-4f5f-a6f6-19cbaaba8e65 | `b9bc250d3db513c3fa6a4ed02b6a00fefc871c9689c38c898dff48e125dafa38` | `95f79c505228236c7608aa9f3e3df19676ad6693ce16bd0a03e711ae5af02e37` |

Суммарное время обработки: 1094 с (~18,2 мин), последовательно, 8/8 успешно.

- Output SHA-256 — хеши файлов `output/flow546/blind_outputs/HX-0N.md` (verbatim-ответы валидатора).
- Wall-clock длительность — время subprocess-а целиком; `duration_ms` — из JSON-ответа CLI.
- Prompt, spec, criteria, freeze и карточки не изменялись (входные хеши совпали до и во время прогона).
