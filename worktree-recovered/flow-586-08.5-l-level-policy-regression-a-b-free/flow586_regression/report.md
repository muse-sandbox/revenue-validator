# FLOW-586 — Исправление L-level policy и regression A/B перед freeze Validator V1

Дата: 2026-08-05. Regression gate после FLOW-580, перед FLOW-581. Пороги FLOW-579 не
пересматривались, исходный `NO` FLOW-579 не переименовывался.

## Вердикт

# `GATE: FAIL`

- **Спеццель регрессии достигнута:** дефект FLOW-579 (инфляция уровня близости: claimed L2
  при осях L3 в RH-05/T3-05) **исправлен generic-фиксом и не воспроизводится** — computed
  L-level совпадает с осями во всех 20 analog-карточках всех 6 кейсов B (машинный линтер
  12/12 PASS + независимый ручной пересчёт evaluator'а); в RH-05 T3-05 теперь честный L3,
  при пустом L1/L2 выдано обязательное «no direct analogs».
- **Причина FAIL:** новое, не связанное со старым дефектом **1 формальное C6-нарушение** у
  плеча B в RH-04 — прозаическая фраза «Wrapper changes without offer changes have not
  lifted purchases in this corpus» (овергенерализация P-10/T1-09 на весь класс wrapper-изменений,
  противоречащая корпусному факту T1-07 var2 iOS +26.5%, который ответ сам же цитирует и
  карантинирует). Подтверждено адверсариальной верификацией ДО вскрытия GT: формальное,
  wording-level; вердикт/прогноз/рекомендации ответа на фразе не строятся. Frozen-протокол
  §6.5 требует C6=0 и формальные/содержательные нарушения не различает.
- **FLOW-581 не разблокируется.** Очередь остановлена.

## Способ исправления (рекомендация для следующей итерации)

Минимальный V1.2 (generic, без подгонки под RH-04):
1. уточнить заголовок паттерна P-10 — тело говорит о message/creative-персонализации при
   неизменном оффере, заголовок «…not only the wrapper» шире тела и провоцирует
   овергенерализацию;
2. расширить линтер/промпт запретом бес-квалификаторных корпусных универсалий в прозе
   («X have not/never/always … in this corpus» без явного скоупа и контрпримеров);
3. повторный regression-прогон по тому же frozen-протоколу.
KB не отбрасывать: содержательная картина второй раз подряд эквивалентна сильному YES по
6/7 условий.

## Результаты прогона (сводка)

| Условие §6 протокола | Порог | Факт | Статус |
|---|---|---|---|
| 1. B предпочтён (C4) | ≥4/6 | 6/6 (5 уверенно, RH-05 с небольшим перевесом) | ✅ |
| 2. C1 source-grounded insight | ≥4/6 вкл. страту 2/3 | 6/6 | ✅ |
| 3. Материальное изменение | ≥1 | 6/6 | ✅ |
| 4. Галлюцинации B (C2) | =0 | 0 | ✅ |
| 5. Unsupported transfers B (C6) | =0 | 1 (формальное, RH-04, проза) | ❌ |
| 6. False blockers B ≤ A | ≤ | 0 ≤ 0 | ✅ |
| 7. Review ≤10 мин | все | pending human → shadow pilot FLOW-566 | ⏳ |

| Решающее правило FLOW-586 | Факт | Статус |
|---|---|---|
| Integrity и clean-room валидны | 22/22 + 19/19 + 53/53 хешей OK, mtime-порядок фаз соблюдён | ✅ |
| Computed L-level совпадает с осями 6/6 | 20/20 карточек (линтер + ручной пересчёт) | ✅ |
| Unsupported transfers = 0 | 1 (RH-04, формальное) | ❌ |
| Hallucinated lessons = 0 | 0 | ✅ |
| False blockers B ≤ A | 0 ≤ 0 | ✅ |
| «no direct analogs» при пустом L1/L2 | сработало (RH-05) | ✅ |
| Старый дефект RH-05 не воспроизводится | не воспроизведён ни в одной карточке | ✅ |

C5 outcome alignment (после вскрытия GT): **B 6 : A 0** (как в FLOW-579), с дословными
попаданиями (RH-02 «inconclusive as designed» при факте p=0.06; RH-02 trial-quality −43.3%
при прецеденте −45%; RH-05 payment-mix shift и «monitor Charge→Cancel» дословно в решении
команды).

## Preconditions (проверены до начала)

- FLOW-580 доставлен: Evidence Policy V1 заморожена (`revenue-evidence-policy-v1/`, хеши
  совпадают), decision matrix L1/L2/L3 присутствует. Статус в Linear не переводился (перевод
  статусов — за пользователем), выполнение подтверждено комментарием о DoD и frozen-бандлом.
- Frozen-бандлы FLOW-575/578/579 не редактировались: 77/77 SHA-256 OK (перепроверялись
  трижды: до Фазы A, после Фазы A, в Фазе C).
- FLOW-584 = PASS (отчёт аудита).

## Фазы (изолированные контексты)

- **Фаза A (builder-субагент):** собран и заморожен `revenue-kb-v1.1/` (22 файла,
  FREEZE_MANIFEST): детерминированная формализация L1/L2/L3 из осей (KB §2.2, разрешения
  неоднозначностей R1–R5 в сторону более низкого уровня), строгий YAML-формат analog-карточки
  (все 10 осей + segment_monetization_state/money_chain_link/platform), stdlib-линтер с 6 hard
  errors (инфляция уровня, пустой not_transferable, несуществующий source ID, непарсируемая
  карточка, отсутствие «no direct analogs», отсутствие секции side-effects), обязательная
  секция «Non-monetization effects to instrument» (обе стороны + stop-rules), 25 selftest-тестов,
  детерминизм подтверждён двойным прогоном. Builder знал тип ошибки, текстов RH-кейсов не видел.
  pattern_cards.md и evidence_policy* — байт-в-байт копии. KNOWLEDGE_CONTEXT V1.1:
  `ae980e46…`, 58 094 bytes.
- **Фаза B (clean runner):** `revenue-kb-v1.1-regression-run/` — 12 изолированных headless
  `claude -p` (claude-fable-5, без инструментов/MCP/настроек/сессий; та же механика, что
  FLOW-579), preflight 28/28 OK, exit 0 у всех 12, линтер PASS 12/12 с повторным
  байт-идентичным прогоном (детерминизм на реальных ответах), blind-пары + sealed mapping,
  run_manifest + BUNDLE_MANIFEST (53 файла). Ground truth / mapping / артефакты FLOW-579 в
  контексты inference не подавались. Инцидент: первый запуск скрипта умер на Stage 2 (фоновый
  процесс runner-субагента был убит при завершении его хода) — ни один inference не завершился,
  ответы не генерировались и не читались; второй запуск (из контекста оркестратора, только
  манифест-уровневые данные) чистый.
- **Фаза C (судьи + верификатор + evaluator):** 6 независимых слепых судей (по одному на кейс,
  порядок чтения зафиксирован случайными битами до запуска), scorecard'ы заморожены
  (`ac80e218…`) ДО адверсариальной верификации C6-флага RH-04 и ДО вскрытия mapping/GT.
  Mapping совпал с содержательными догадками судей 6/6 (неполнота слепоты — унаследованное
  задекларированное свойство). Evaluator: integrity, C5, false blockers, L3/RH-05-аудит,
  метрики, вердикт.

## Артефакты

Канонические бандлы (рядом с `revenue-kb-v1/`):
- `~/Documents/Codex/2026-08-03/users-elzira-obsidian-ug-ai-infrastructure/outputs/revenue-kb-v1.1/`
- `…/outputs/revenue-kb-v1.1-regression-run/`
- `…/outputs/revenue-kb-v1.1-regression-evaluation/` (case_scorecards, metrics,
  l3_and_rh05_audit, final_verdict, errors_and_limitations, c6_verification_rh04,
  blind_pairwise_scorecards + freeze, judges/, BUNDLE_MANIFEST)

Скрипты (этот репозиторий): `analysis_scripts/20260805_flow586_verify_frozen_bundles.py`,
`analysis_scripts/20260805_flow586_regression_ab_run.py`.

## Ограничение интерпретации

Повтор на том же holdout — regression test исправления, а не независимая оценка общей
продуктовой пользы; генерализация — shadow pilot (FLOW-566) и следующий новый holdout.
C7 (human review ≤10 мин) агентной оценкой не закрывается — pending.
