# FLOW-546 — Clean-room declaration

Дата прогона: 2026-08-04. Оркестратор: Claude Code (модель `claude-fable-5`), новый контекст, созданный только из текста задачи FLOW-546.

## Вход

- Единственный использованный вход — clean bundle по точному пути из задачи:
  `/Users/elzira/Documents/Codex/2026-08-03/users-elzira-obsidian-ug-ai-infrastructure/outputs/flow546-clean-input`
- Перед прогоном выполнен preflight: состав bundle (4 файла `validator-v0/`, 8 файлов `prelaunch-pack/HX-01…HX-08`, `BUNDLE_MANIFEST.md`) проверен листингом только внутри bundle; SHA-256 всех 12 файлов пересчитаны и совпали с `BUNDLE_MANIFEST.md`; frozen-хеши `validator_v0_prompt.md` / `validator_v0_spec.md` / `validator_v0_criteria.md` совпали с `validator_v0_freeze.md`.

## Изоляция inference-запусков

- Каждая карточка HX-01…HX-08 обработана отдельным изолированным headless-процессом `claude -p` (скрипт `analysis_scripts/flow546_blind_run.sh`):
  - новый чистый контекст (отдельная сессия на карточку, пустая рабочая директория вне репозитория — без CLAUDE.md, хуков и памяти);
  - system prompt = неизменённый `validator_v0_prompt.md`, переданный файлом (`--system-prompt-file`);
  - единственный project input = одна HX-карточка, переданная verbatim через stdin;
  - все инструменты отключены (`--tools ""`), MCP-серверы отключены (`--strict-mcp-config` с пустым конфигом) — поиск и внешние источники недоступны процессу физически;
  - процессы не имели доступа к ответам и содержимому других карточек.
- Ответы сохранены verbatim (поле `result` JSON-ответа CLI, байт-в-байт через `jq -j`) в `output/flow546/blind_outputs/HX-0N.md` и захешированы SHA-256.

## Что НЕ делалось

- Ground truth, mapping, registry, warehouse facts, outcome-классы, исходные документы гипотез и их Results/Decision — не искались и не открывались.
- HX-ID и фразы карточек не искались в файловой системе, Linear, Confluence или интернете.
- Другие Linear-задачи (кроме самой FLOW-546 и её описания/комментариев), Obsidian, Confluence, интернет, git-ветки других задач — не открывались.
- `validator_v0_prompt.md`, `validator_v0_spec.md`, `validator_v0_criteria.md`, `validator_v0_freeze.md` и HX-карточки не изменялись (bundle read-only; хеши на входе совпали с манифестом).
- Рекомендации валидатора с исходами не сравнивались; никакая оценка качества не проводилась (задача — только inference).
- Оркестратор не читал содержимое HX-карточек в свой контекст: карточки передавались subprocess-ам напрямую из файлов; из ответов для summary извлекались только строки «Рекомендация + уверенность».

## Отклонения

- Вне bundle оркестратором читались только: текст задачи FLOW-546 (Linear), служебные файлы worktree (CLAUDE.md репозитория, preflight-скрипты) и создаваемые артефакты `output/flow546/`. На вход валидатора ничего из этого не попадало.

Run признаётся валидным: нарушений clean-room не зафиксировано.
