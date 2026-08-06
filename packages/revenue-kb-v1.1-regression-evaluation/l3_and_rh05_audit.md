# L3 & RH-05 AUDIT — спеццель regression-прогона FLOW-586

Дата: 2026-08-05. Проверяется исправление единственного провала FLOW-579: в RH-05 плеча B
источник T3-05 был помечен L2 при осях, дающих L3 (инфляция уровня близости, «promote L3
evidence to analog status»). Fix V1.1: детерминированный расчёт L-уровня из осей (§2.2
normative) + машинный линтер (`revenue-kb-v1.1/linter.py`, frozen, selftest 25 GREEN).

## 1. RH-05 плеча B — прямой пересмотр старого дефекта

Ответ `arm-b/RH-05.md`, линтер `linter/arm-b-RH-05.json`:

- Единственная analog-карточка: **T3-05**, оси: `mechanism: different`,
  `flow_stage: exact`, `surface: adjacent`, `segment_monetization_state: different`,
  `money_chain_link: different`, `platform: exact`.
- Пересчёт по §2.2 (вручную, независимо от линтера): L1 требует `mechanism == exact` — нет.
  L2(A) требует `mechanism == exact` — нет. L2(B) требует `surface == exact` И
  `mechanism == different` — surface только adjacent → не срабатывает (ровно та ветка,
  через которую в FLOW-579 произошла инфляция: adjacent был засчитан как достаточный).
  L2(C) требует `mechanism == exact` — нет. → **L3**.
- Claimed в ответе: **L3**. Линтер: `claimed_level: L3`, `computed_level: L3`,
  `card_errors: []`, verdict PASS. **Старый дефект НЕ воспроизведён.**
- Использование T3-05: transferable открывается «[fact] … UI-only iterations were rejected
  on guardrails …» + «[hypothesis] **L3 weak signal only**: a checkout-layout change here
  should carry refund/cancel/AOV guardrails and stop-rules»; not_transferable: «All
  magnitudes; all offer-structure conclusions …; **no product conclusion of any kind
  transfers at L3**». В прозе (§3, риск 5; §6 чеклист) T3-05 фигурирует только как
  «L3 guardrail lesson» для guardrail-пакета. Вердикт «Redesign before launch» опирается
  на внутренние дефекты карточки (power/MDE-противоречие 0.05%/500%/n=1996 при гипотезе
  +3%; mis-scoped goal-метрика; пустая Analytics-секция) — НЕ на T3-05.
- Пустой L1/L2 → ответ содержит явную строку **«no direct analogs»** (раздел 4, строка 14)
  с корректной формулировкой «the nearest source computes to L3 and is used only for
  guardrail/measurement lessons, per rule 4». Требование выполнено.
- Unblind-подтверждение уместности: GT-RH-05 — фактическая цена победы ровно guardrail-ная
  (14d cancel +31.73% p=0.043; retention var3 значимо хуже; решение «Rollout … but monitor
  Charge → Cancel»). L3-сигнал использован в правах и попал в фактический исход.

## 2. Все L3-карточки всех 6 ответов B (полный проход)

Всего в плече B 20 analog-карточек; из них 5 — L3. По каждой: оси → пересчёт §2.2,
маркировка, характер использования, не-основание вердикта.

| Кейс | Источник | Ключевые оси (mech/flow/surface; smc/mcl/platform) | §2.2 → | Claimed | Маркировка в карточке | Использование | Основание вердикта? |
|---|---|---|---|---|---|---|---|
| RH-03 | T1-07 | adjacent/exact/adjacent; exact/exact/exact | ни L1, ни одна ветка L2 (mechanism ≠ exact и ≠ different) → **L3** | L3 | «explicit L3 weak signal, guardrails/sizing only» + «[L3 — guardrail/measurement lesson only, no product conclusion, **not a basis for the verdict**]» | retention-инструментирование + stop-rule D1 для entry-анимации | Нет — вердикт стоит на T2-02/T3-01/T2-01 и дефектах дизайна |
| RH-04 | T1-09 | adjacent/exact/different; different/exact/exact | mechanism adjacent → ни одна ветка → **L3** | L3 | «Inconclusive source: measurement/direction lesson only (rule 6)» + «any product conclusion» в not_transferable | измерять click-КАЧЕСТВО (click→access per card), а не объём | Нет — вердикт «Launch with changes» стоит на дефектах power/exposure/guardrails |
| RH-04 | T2-01 | different/exact/adjacent; exact/exact/exact | L2(B) требует surface exact — adjacent не срабатывает → **L3** | L3 | «L3 guardrail/sizing signal only … **L3 is never a verdict basis**» | guardrail на демотированные фаннелы (Spotify/discount) | Нет |
| RH-05 | T3-05 | different/exact/adjacent; different/different/exact | → **L3** (разбор в §1) | L3 | «L3 weak signal only … no product conclusion of any kind transfers at L3» | guardrail-пакет refunds/cancels/AOV + stop-rules | Нет |
| RH-06 | T3-02 | adjacent/exact/adjacent; exact/exact/exact | mechanism adjacent → **L3** | L3 | «L3 — sizing/guardrail signal only, **not an analog and not a verdict basis**» | sizing ценовой эластичности web + save-offer CR guardrail | Нет — вердикт стоит на L1 (T3-03, T3-05) и дефектах дизайна |

Во всех 5 случаях: (а) уровень вычислен корректно и не завышен; (б) явная L3-метка
присутствует в теле карточки; (в) использование ограничено guardrail/measurement/sizing;
(г) ни один L3-источник не подан как direct analog; (д) ни один вердикт
launch/revise/deprioritize не строится на L3-источнике как самостоятельном основании.

Пограничное (зафиксировано, не нарушение уровня): в RH-04 риск-буллет №1 цитирует L3-источник
T1-09 в связке с mandatory-паттерном P-10 в овергенерализованной фразе — это единственное
C6-нарушение прогона (формальное, wording-level; см. `c6_verification_rh04.md`). Дефект — объём
класса в прозе, не статус/использование L3: T1-09 и в этой точке помечен «direction lesson»,
продуктовый вывод на нём не строится, вердикт ответа позитивный.

## 3. L1/L2-карточки — сверка claimed vs computed (анти-инфляция, все 15 остальных)

Ручной пересчёт §2.2 всех остальных карточек B (независимо от линтера; линтер дал то же):

- **RH-01:** T1-02 (exact/exact/exact; smc different, mcl exact) → L2(C) ✓; T1-08
  (different/exact/exact) → L2(B) ✓; T1-09 (different/exact/exact) → L2(B) ✓. L1 честно
  объявлен отсутствующим («No L1 analog exists»).
- **RH-02:** T1-02 (exact/exact/exact; smc exact, mcl exact, platform exact) → L1 ✓;
  T1-04 (exact/exact/exact; smc different, mcl exact) → L2(C) ✓; T1-07
  (different/exact/exact) → L2(B) ✓.
- **RH-03:** T2-02 (exact/exact/exact; все exact) → L1 ✓; T3-01 (exact/exact/adjacent;
  smc exact, mcl exact, platform adjacent) → L1 ✓ (R1: adjacent platform не демотирует);
  T2-01 (different/exact/exact) → L2(B) ✓.
- **RH-04:** T1-07 (exact/exact/different) → L2(A) ✓.
- **RH-06:** T3-03 (exact/exact/adjacent; smc exact, mcl exact, platform exact) → L1 ✓;
  T3-05 (exact/exact/adjacent; smc exact, mcl exact) → L1 ✓; T3-06 (exact/adjacent/different)
  → L2(A) ✓ (flow_stage adjacent блокирует L1; surface different активирует ветку A).

**Итог: 20/20 карточек — claimed == computed; ни одной инфляции; ни одной дефляции.**
Направление ошибки FLOW-579 (завышение под давлением «найти аналог» в кейсе без близких
источников) в V1.1 не воспроизводится: в том же самом кейсе RH-05 валидатор выдал честный
L3 + «no direct analogs».

## 4. Линтер как контроль

- 12/12 JSON-отчётов: verdict PASS; у плеча A `mode: no-kb-arm`, `cards: []` (карточек нет —
  корректно для no-KB-режима); у плеча B все карточки с `card_errors: []`.
- `run_manifest.md`: повторный прогон линтера на всех 12 ответах дал байт-идентичные отчёты
  (детерминизм на реальных ответах); перезапусков inference по результатам линтера не было.
- `linter_selftest.py`: 25 тестов GREEN (в т.ч. фикстуры `answer_fail_inflation` — ловля
  claimed>computed, `answer_fail_missing_no_direct` — ловля отсутствия «no direct analogs»
  при пустом L1/L2), stdout детерминирован (зафиксировано в FREEZE_MANIFEST V1.1).

## 5. Вывод спеццели

Дефект FLOW-579 (инфляция L-уровня в analog-карточке) **исправлен и не воспроизводится**:
детерминированный расчёт + линтер закрывают карточный канал инфляции полностью (20/20).
Оставшийся канал — **прозовый** (утверждения о корпусе вне карточек), где и произошло новое
формальное C6 в RH-04; он линтером V1.1 не покрывается и адресуется рекомендацией V1.2
(см. `final_verdict.md`).
