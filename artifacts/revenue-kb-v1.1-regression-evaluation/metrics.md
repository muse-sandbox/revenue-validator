# METRICS — Revenue KB/Validator V1.1 regression A/B (FLOW-586)

Дата: 2026-08-05. Протокол: frozen `revenue-corpus-prep-v1/EVALUATION_PROTOCOL.md` (V1);
пороги §6 не менялись. Слепые вердикты: `blind_pairwise_scorecards.md` (sha256
`ac80e218d8bcfe4ad10fd15fd1d01a47827c590284f1bd8c85915801cce8d343`, заморожены
2026-08-05T08:35:24Z — до C6-верификации, вскрытия mapping и GT). C5/false blockers:
`case_scorecards.md` (unblind). C6-счёт: слепые scorecard'ы + адверсариальная верификация
`c6_verification_rh04.md` (до вскрытия; RH-04: 1 формальное, wording-level).

## Таблица 1 — условия протокола §6 (YES-гейт пользы KB)

| # | Условие | Порог | Факт | Статус |
|---|---|---|---|---|
| 1 | B предпочтён по C4 | ≥4/6 (tie не в счёт B) | **6/6** (5 «уверенно», RH-05 «с небольшим перевесом») | ✅ |
| 2 | C1 source-grounded insight у B | ≥4/6, вкл. ≥1 кейс страты 2/3 | **6/6**, вкл. оба кейса страты 2 и оба страты 3 | ✅ |
| 3 | B существенно меняет решение против A | ≥1 кейс | **6/6** (MATERIAL_DELTA во всех) | ✅ |
| 4 | Hallucinated lessons (C2) у B | = 0 | **0** (цитаты сверены судьями с KB, 12/12 ответов чисты) | ✅ |
| 5 | Unsupported transfers (C6) у B | = 0 | **1** — RH-04-B, овергенерализация класса «Wrapper changes … have not lifted purchases in this corpus» (P-10/T1-09); формальное, wording-level, подтверждено до вскрытия | ❌ |
| 6 | False blockers B ≤ A | ≤ | **0 ≤ 0** | ✅ |
| 7 | Human review ≤10 мин/кейс | все | по объёму пар да (1 604–2 215 слов ≈ 8–11 мин); человеком не подтверждено — **pending → FLOW-566** | ⏳ |

Формальный вердикт по §6: **`NO`** — невыполнение условия 5 (как и в FLOW-579; пороги после
открытия holdout не меняются; «NO с оговорками» зарезервировано за провалом только условия 7).

## Таблица 2 — решающее правило FLOW-586 (regression gate)

| # | Условие regression-гейта | Факт | Статус |
|---|---|---|---|
| 1 | Integrity / clean-room валидны | KB V1.1 22/22 хешей OK (+ KNOWLEDGE_CONTEXT concat 58 094 B OK); corpus-prep 19/19 OK (blind-карточки + GT); regression-run 53/53 OK (judge_instructions.md = задокументированный sha `5be60f57…`, записан до запуска судей); слепые scorecard'ы = freeze-хеш; mtime-порядок freeze (15:35:24) → c6-верификация (15:43:33) → unblind-файлы; isolation per `run_manifest.md` (12 изолированных headless-процессов, tools/MCP off, GT/mapping не подавались) | ✅ |
| 2 | Computed L-level совпадает с осями 6/6 | Линтер 12/12 PASS; во всех 20 analog-карточках B claimed == computed; ручная сверка всех 20 по §2.2 evaluator'ом — совпадение (см. `l3_and_rh05_audit.md`) | ✅ |
| 3 | Unsupported transfers = 0 | **1** (RH-04-B, формальное wording-level; вердикт/прогноз/рекомендации ответа на фразе не строятся — но frozen-правило формальных/содержательных не различает) | ❌ |
| 4 | Hallucinated lessons = 0 | 0 | ✅ |
| 5 | False blockers B ≤ A | 0 ≤ 0 | ✅ |
| 6 | `no direct analogs` при пустом L1/L2 | Единственный кейс B с пустым L1/L2 — RH-05: явная строка «no direct analogs» присутствует (линтер-нормой enforced; фикстура `answer_fail_missing_no_direct` в selftest) | ✅ |
| 7 | Старый дефект RH-05 (claimed > computed) не воспроизводится | Не воспроизведён: RH-05-B T3-05 claimed L3 = computed L3 (в FLOW-579 было claimed L2 при computed L3); ни одна из 20 карточек не завышает уровень | ✅ |

**Итог regression-гейта: `GATE: FAIL`** (целостность цела; провалено ровно условие 3).

## C5 и вне-гейтовые метрики (unblind)

- **C5 outcome alignment: B 6 · A 0 · tie 0** (в FLOW-579 тоже 6:0). Оговорки: RH-04 — точечный
  численный прогноз A ближе (−10..+15% vs факт), перевес B по механизмам (attention≠intent —
  дословно в GT-вердикте; демоция Spotify; anti-personalization-фрейминг); RH-05 — вердикт A
  («launch with changes») ближе к фактическому успеху, перевес B по механизму (payment-mix
  shift, strongest in C — дословно подтверждён) и цене победы («monitor Charge→Cancel» —
  дословно решение команды).
- **False blockers: A 0, B 0.** Блокирующие вердикты: RH-03 B, RH-05 B (исход — успех, причины
  блокировки подтвердились как реальные дефекты дизайна/реализовавшиеся guardrail-риски → не
  false blockers по §5), RH-06 A+B (исход — fail, блокировка оправдана).
- Дословные попадания B в фактические исходы: trial-quality collapse −43.3% при прецеденте
  −45% (RH-02); «attention inflation, not intent» (RH-04 ↔ вердикт страницы); payment-mix
  shift + «monitor Charge→Cancel» (RH-05); якорная роль удалённого instant / substitution-not-
  migration (RH-06 ↔ takeaway страницы); low-intent re-trials + cancel-спайк (RH-01).

## Стратная таблица

| Страта | Кейсы | C4 (B) | C1 (B) | C5 (B) | C2/C6 у B | Комментарий |
|---|---|---|---|---|---|---|
| 1 — тот же слой (App interstitial) | RH-01, RH-02 | 2/2 | 2/2 (L1/L2 якорной семьи) | 2/2 | 0 / 0 | Почти точное попадание величины прецедента (−45% vs −43.3%); cancel-спайк и inconclusive-read предсказаны |
| 2 — тот же этап, другая поверхность | RH-03, RH-04 | 2/2 | 2/2 (L1 прецедент + L2/L3 warnings) | 2/2 | 0 / **1 формальное** (RH-04) | Механизмы (Total-null + scenario-funnel; attention≠intent; демоция оффера) подтверждены GT; единственный сбой — прозовая овергенерализация класса, НЕ карточная |
| 3 — та же метрика, другой flow | RH-05, RH-06 | 2/2 | 2/2 (в RH-06 web-источники законно L1; в RH-05 честный L3 + «no direct analogs») | 2/2 | 0 / 0 | Дисциплина уровней, сломавшаяся здесь в FLOW-579, теперь выдержана полностью; guardrail-уроки попали в фактическую цену победы (RH-05) и механизм провала (RH-06) |

## Сравнение с FLOW-579 (что изменилось)

| Метрика | FLOW-579 (V1) | FLOW-586 (V1.1) |
|---|---|---|
| C4 / C1 / C3-высокая у B | 6/6 / 6/6 / 6 | 6/6 / 6/6 / 6 |
| C2 (галлюцинации) | 0 | 0 |
| C6 | 1 — RH-05, **инфляция уровня** T3-05 L3→L2 (карточная, машинно-ловимая) | 1 — RH-04, **прозовая овергенерализация класса** (wording-level, вне охвата детерминированного линтера) |
| Claimed vs computed L-уровни | нарушение в 1 карточке | **20/20 совпадение; линтер 12/12 PASS** |
| C5 | B 6:0 | B 6:0 |
| False blockers | 0:0 | 0:0 |
| Retention-слепота (систематика) | ни одно плечо не предсказало retention-эффектов | Частично закрыта: RH-06-B явно допустил позитивный retention-исход (факт: +7d/14d p=0.000); RH-02-B предсказал retention-цену (факт: значимые −7d/14d iOS); мимо остались RH-04 (iOS var2 ret7d) и знак в RH-05 |
