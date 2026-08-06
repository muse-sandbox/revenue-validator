# FLOW-584 — Независимый аудит выводов FLOW-571 перед freeze Validator V1

- **Дата:** 2026-08-04
- **Аудитор:** агент Claude Code (`claude-fable-5`), задача FLOW-584, независимая сессия (не сессия FLOW-570/FLOW-571)
- **Вердикт: `PASS`** — факты и выводы FLOW-571 подтверждены; FLOW-581 (freeze Validator V1) можно выполнять с уже запланированными доработками из `recommendations_for_validator_v1.md`. Повторных evals не требуется.

Проверяемые артефакты: `~/Documents/Codex/2026-08-03/users-elzira-obsidian-ug-ai-infrastructure/outputs/` — бандлы `interstitials-kb-v0`, `interstitials-kb-ab-run`, `interstitials-corpus-prep`, `interstitials-kb-evaluation`; первичные Confluence-снапшоты — worktree `flow-568-analytics-inventory-interstitials-holdo/output/confluence/flow568-interstitials/`.

## 1. SHA-256 и целостность бандлов — ПОДТВЕРЖДЕНО (48/48)

Независимый пересчёт `shasum -a 256` каждого файла против манифестов:

| Бандл | Манифест | Результат |
|---|---|---|
| interstitials-kb-v0 | FREEZE_MANIFEST.md | 7/7 OK |
| interstitials-kb-ab-run | BUNDLE_MANIFEST.md | 19/19 OK |
| interstitials-corpus-prep | BUNDLE_MANIFEST.md | 22/22 OK |
| interstitials-kb-evaluation (доп.) | BUNDLE_MANIFEST.md | 9/9 OK |

Дополнительные кросс-проверки: хэши `blind-pairs/IH-0n-{X,Y}` тождественны хэшам `arm-{a,b}/IH-0n` и согласованы с `arm_mapping_sealed.md` по всем 4 кейсам; sha256 `validator_v0_prompt.md` = заявленному в FREEZE_MANIFEST (`61b2ee46…`); KS-хэши в `source_traceability.md` побайтно совпадают с манифестом корпуса (6/6).

## 2. Порядок фаз (blind до unblind) — ПОДТВЕРЖДЕНО

- `blind_pairwise_scorecards.md`: sha256 = `0142d53f…` (совпадает с заявленным freeze-хэшем), mtime 2026-08-04 15:43:11 +0700 = 08:43:11Z (заявленный freeze 08:43:16Z).
- Все unblind-документы записаны позже: 08:47:45Z (`case_scorecards.md`) … 08:51:59Z (`BUNDLE_MANIFEST.md`), монотонная последовательность.
- Freeze-хэш процитирован в `case_scorecards.md`, `analyst_fact_check.md`, `final_verdict.md` — изменение blind-файла после freeze было бы обнаружимо.
- Содержимое blind-файла не ссылается на ground truth; частичность слепоты (плечо распознаваемо по содержимому verbatim-ответов) честно задекларирована в самом файле ДО вскрытия — это уже учтённое ограничение дизайна, не нарушение порядка.
- Ограничение аудита: доказательство порядка опирается на внутренние свидетельства (mtime + взаимные цитаты хэшей) одной машины; внешнего таймстемпинга нет. Рекомендации 6–7 из `recommendations_for_validator_v1.md` (нейтрализация маркеров, независимый судья) это покрывают для будущих циклов.

## 3. Source claims (≥3 на кейс) — ПОДТВЕРЖДЕНО, искажений нет

Сверены с frozen `pattern_cards.md`/`knowledge_base.md` И с первичными карточками `knowledge-sources/KS-01…KS-06` (фактически 6–9 утверждений на кейс):

- **IH-01 (B):** видео-fail 28.05% iOS / 48.23% Android (KS-04 §Execution → IKB-P11) ✓; 96.66% close / 0.07% CR / single-case (KS-03 → IKB-P05) ✓; intro-результат +11.5% p=0.016 / +25% p=0.000 (KS-06 iter2 → IKB-P08/P09) ✓; утечка ex 3.6×/13×, unified_id bug (KS-02 §Post-rollout, KS-05/KS-06 §Execution → IKB-P10/P06) ✓; retention-противоречие KS-04 iter2 ↓ / KS-06 iter1 ↑ / iter2 0 (IKB-P12) ✓; затухание 1.58%→0.41% (KS-06 → IKB-P03) ✓.
- **IH-02 (B):** «works only on free, doesn't affect ex», Total exes −2.2% p=0.77 (KS-06 iter2 → IKB-P09) ✓; cancels −26.6% p=0.016 ✓; охват 99.74% vs push 50–72% (KS-05 → IKB-P11) ✓; +42.8% помечен непереносимым ✓.
- **IH-03 (B):** novelty-ловушка — значимый +7.5% (p=0.029) сознательно не раскатан (KS-02 §Decision «novelty effect trap») ✓; eligibility-сжатие +24%→+7.5% в 2–3× (KS-02 → IKB-P10) ✓; повторный trial 27% iOS vs 100% Android ✓; cancels +118% (KS-05 → IKB-P07) ✓; честная фиксация «аналога message-only в базе нет» ✓.
- **IH-04 (B):** IKB-P09 (−2.2% p=0.77) против модельного +88.3% (+88.30% подтверждён в первичной странице 811868738) ✓; 21% iOS «trial» = instant charge (KS-02) ✓; trial→paid −36…−54% (KS-06 iter1 → IKB-P07) ✓; затухание CR ~4× (IKB-P03) ✓.

Отдельно подтверждён критерий C1 «не выводимо из карточки»: инсайтные факты (unified_id, −2.2%, −26.6%, novelty trap, 28.05/48.23, 3.6×/13×) в blind-карточках `holdout-blind/IH-0x.md` отсутствуют; карточки цитируют только успехи winback (+42.8%, 10–20×) — как и заявлено в оценке.

## 4. Фактические исходы IH-01…IH-04 — ПОДТВЕРЖДЕНО первичными страницами

GT-карточки сверены с raw Confluence-снапшотами (версии совпадают: v27/v29/v41/v17):

| Кейс | Эксперимент | Ключевые проверенные факты |
|---|---|---|
| IH-01 | 7160/7187 (стр. 773658792) | Red fail, «revenue was too low»; iOS var2 ARPU +26.5% p=0.011; Android var3 retention −9.15/−5.26/−4.47 (p≤0.023); «75-77% lower conversion» ✓ |
| IH-02 | 7487 (стр. 788612067) | Green, rollout обеих платформ; winback member→buyers +365.58% iOS / +103.82% Android; iOS диффузное размытие non-winback −$702; «no significant increase on arpu but only due to small segments» ✓ |
| IH-03 | 7454 (стр. 788613565) | Red fail/inconclusive; «No iOS reading is possible» (доставка умерла после 3 дней); paywall→click 7.25%→3.90%; «The main direction is to personalize the offer, not only the message»; ex-paid 1.95% vs free 0.095% (~20×) ✓ |
| IH-04 | 7712 (стр. 811868738) | «Do not roll out this iteration»; iOS surface net revenue +58.14% при flat volume; Android −44.44% объёма — «price elasticity, not execution»; winback «undecided, not a negative result»; «Do not reuse Total ARPU as the goal metric for surface-scoped paywall tests» ✓ |

Расхождений с документами не обнаружено → **ClickHouse-пересчёт не выполнялся** (по условию задачи — только при расхождении).

## 5. Unsupported transfers и граница IKB-P09 — ПОДТВЕРЖДЕНО (0 нарушений)

Прочитаны все четыре B-ответа целиком. Каждое применение single-case паттернов (IKB-P05, IKB-S01…S03, intro-сторона IKB-P08, величины IKB-P10) сопровождено оговоркой; «не переносить»-границы KB не нарушены; противоречие IKB-P12 всегда подано обеими сторонами; в проходах 1–2 KB-ссылки не используются (скрытых переносов нет).

Граница IKB-P09 отдельно: перенос в IH-02 подан явно как «гипотеза переноса» с оговоркой «self-selection по цене может отличаться» и решающим замером; в IH-04 — «как минимум как гипотезу» с downside-критерием. Исход 7487 опроверг перенос по направлению (скидка «оживила мёртвый сегмент»), что корректно классифицировано в `errors_and_limitations.md` как ошибка прогноза, а не grounding-нарушение. Scope-note к IKB-P09 в V1 (паттерн замерен на НЕисчерпанных ex при доступном re-trial и не распространяется на терминальный сегмент) — обязательна и уже запланирована.

## 6. False blockers в IH-02 — ПОДТВЕРЖДЕНО (0 у B, 0 у A)

Оба плеча дали `revise` (A: medium, B: low confidence), не отказ от запуска. По §5 frozen-протокола false blocker требует, чтобы названные причины блокировки НЕ подтвердились исходом. Главные причины обоих плеч подтвердились: (а) нечитаемость денег без power — Total ARPU действительно оказался незначим (p=0.40/0.22, «only due to small segments»); (б) каннибализационный риск — реализовался на iOS (−27 non-winback buyers, −$702, «watch full-price cannibalization»). Ошибочный контр-сигнал B (IKB-P09) был оговоркой при переносе, а не причиной revise. Итог 0 ≤ 0 корректен.

## Найденные расхождения

1. **Минорное (документация):** `interstitials-kb-evaluation/BUNDLE_MANIFEST.md` утверждает, что freeze-хэш `0142d53f…` зафиксирован в тексте `case_scorecards.md`, `metrics.md` и `final_verdict.md`; фактически в `metrics.md` хэша нет (есть в `case_scorecards.md`, `final_verdict.md`, `analyst_fact_check.md`). Свойство tamper-evidence сохраняется; на вердикты не влияет.
2. Существенных расхождений нет.

## Влияние на KB / evidence policy

Изменений сверх уже запланированных в `recommendations_for_validator_v1.md` не требуется. Аудит независимо подтверждает необходимость пунктов 1–3 (scope-note IKB-P09; паттерн «скоупинг goal-метрики к поверхности»; delivery-gate) и корректность пункта 5 (включение 7160/7187, 7487, 7454, 7712 в корпус V1 с новым holdout для следующего цикла). Условный PASS FLOW-571 повышается до подтверждённого: все объективные условия YES-гейта воспроизведены независимо. C7 (человеческое время review) в аудит не входила — измеряется в shadow pilot.

## Ответы на `analyst_fact_check.md` (шаблон)

```
1. Integrity: подтверждаю (7/7, 19/19, 22/22 + 9/9 evaluation)
2. Порядок фаз: подтверждаю (mtime + freeze-хэш; внешнего таймстемпинга нет — ограничение)
3. C2=0: подтверждаю (сверено 6–9 утверждений/кейс по pattern_cards + первичным KS)
4. C6=0: подтверждаю (полное чтение 4 B-ответов; все single-case оговорены)
5. Чтение GT: подтверждаю (сверено с raw снапшотами v27/v29/v41/v17)
6. False blockers 0/0: подтверждаю
7. Пересчёты по ClickHouse: не делал (расхождений с документами нет)
Подпись: Claude Code (claude-fable-5), аудитор FLOW-584. Дата: 2026-08-04
```
