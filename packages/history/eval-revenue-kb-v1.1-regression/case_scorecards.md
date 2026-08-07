# CASE SCORECARDS — unblind разбор, FLOW-586 regression (Phase C)

Дата: 2026-08-05. Оценщик: изолированный evaluator-агент Фазы C (`claude-fable-5`).
Порядок фаз соблюдён: слепые вердикты заморожены (sha256
`ac80e218d8bcfe4ad10fd15fd1d01a47827c590284f1bd8c85915801cce8d343`, 2026-08-05T08:35:24Z)
→ адверсариальная C6-верификация RH-04 (до вскрытия) → вскрытие `arm_mapping_sealed.md`
и `ground-truth-sealed/` → этот файл. C1–C4, C6 взяты из слепых scorecard'ов без изменений;
C5 и false blockers — unblind, по §4–5 frozen-протокола.

## Mapping (вскрыт) и сверка с судьями

| Кейс | X | Y | KB_BEARING_ANSWER_GUESS судьи | Совпадение |
|---|---|---|---|---|
| RH-01 | arm-B | arm-A | X | ✓ |
| RH-02 | arm-A | arm-B | Y | ✓ |
| RH-03 | arm-A | arm-B | Y | ✓ |
| RH-04 | arm-A | arm-B | Y | ✓ |
| RH-05 | arm-A | arm-B | Y | ✓ |
| RH-06 | arm-A | arm-B | Y | ✓ |

6/6 гадалок судей совпали с mapping (ожидаемо: неполнота слепоты — self-marking ответов —
задекларирована в шапке слепого файла). Кросс-проверка по хешам BUNDLE_MANIFEST:
`blind-pairs/RH-01-X.md` = `arm-b/RH-01.md`, остальные X = arm-a — mapping подтверждён
байтово, аномалий нет. C4-предпочтения судей во всех 6 кейсах указывают на плечо B
(в RH-01 предпочтён X=B, в остальных Y=B).

---

## RH-01 — страта 1. GT: significant-positive, Green SUCCESS, rolled out (#6461, iOS)

Факт (GT-RH-01): ARPU +42.8% (p=0.00), access CR +171%, charge CR +37.8%; эффект целиком
сконцентрирован в видевших interstitial (non-viewers flat, p≥0.40); ad revenue −7.7%;
14d cancels +118% (p=0.00), «offer attracting many low-intent re-trialists who cancel
quickly»; interstitial-sourced charges cancel 33.8% за 14d; retention unchanged; reach 99.74%.

- **C1** (blind): B да (T1-02/T1-08/T1-09, все L2); A нет. **C2**: 0/0. **C3**: B высокая, A низкая.
- **C4** (blind): B (уверенно). **C6** (blind): 0/0. **C7_HUMAN_MIN**: 45 (пара 2 089 слов ≈ 10 мин чтения).
- **C5 outcome alignment: B.** Оба плеча «launch with changes» — совпало с фактическим запуском/раскаткой.
  B: access CR вверх ✓; риск «low-quality re-trials» подтверждён дословно (GT: low-intent
  re-trialists, cancels +118%, 33.8% cancel в источниковом сегменте) — это единственная
  фактическая цена победы, и она входит в решение команды; ad-displacement предсказан и
  оказался умеренным (−7.7%) ✓; правка «re-anchor на matured touched-scope money + cancel
  monitoring» совпала с открытым вопросом GT о long-horizon quality ✓. Промахи B: величина
  money-выигрыша недооценена («confidence in a money win is much lower» при факте +42.8%
  p=0.00); каннибализация не подтвердилась (GT: cleanly incremental) — прецедентный риск,
  корректно поданный как риск, не как прогноз. A: направление access ✓ и «retention drop
  удивил бы» ✓, но ядро прогноза («ARPU likely non-significant in 10 days», «flat or noisy
  revenue read», сигнал утонет в дилюции) опровергнуто фактом p=0.00 без всякой дилюции;
  риск delivery-провала (<80% reach) не реализовался (99.74%). Уникальных подтверждённых
  попаданий у A нет. Перевес B.
- **False blockers:** оба вердикта неблокирующие → A 0, B 0.
- **Страта:** аналоги B — ровно якорная семья (T1-02/T1-08/T1-09, L2), без инфляции; «no L1» явно.

## RH-02 — страта 1. GT: iter1 (#6626, 14d trial) Red FAIL; iter2 (#6896, intro) rolled out

Факт (GT-RH-02, iter1 = дизайн карточки): iOS ARPU +9.71% p=0.06 (n.s.), And +18.5% p=0.19
(n.s.); trial→charge And −43.3% p=0.002 (сегменты −36…−54%); «quality of trials is declining
significantly»; каннибализация (without-interstitial iOS −6.81%; exes −19% p=0.012); net
≈$365/day после ad-потерь; iOS retention 7d/14d значимо вниз (p=0.015/0.019); «on iOS most
of revenue increase came from ex subscribers». Решение: «Do not roll out as-is», re-tune.

- **C1**: B да (T1-02 L1 + T1-04/T1-07 L2); A нет. **C2**: 0/0. **C3**: B высокая, A низкая.
- **C4** (blind): B (уверенно). **C6**: 0/0. **C7_HUMAN_MIN**: 50 (2 215 слов ≈ 11 мин).
- **C5 outcome alignment: B.** B предсказал: «как задизайнено — most likely inconclusive read»
  ✓✓ (iOS p=0.06 — ровно нерешающий); sizing prior 5–8% iOS против факта +9.71% — порядок
  верный; below-average trial quality по прецеденту −13%/−45% [T1-02] против факта −43.3% —
  почти точное попадание величины (перенос корректно держался в sizing/not_transferable);
  каннибализация ✓; ex-subscriber contamination warning ✓ (GT: рост выручки в основном от
  ex subscribers); retention-цена принудительного показа ✓ по знаку (факт — iOS 7d/14d, у
  прецедента And D1 — платформа не совпала); «net-increment predregistration — именно там
  умер предшественник» ✓ (GT: net ≈$365/day и стало главным аргументом Red). A: «flat-to-
  slightly-negative ARPU» — факт положительный n.s. (направление мимо); maturity/displacement
  риски ✓, но без величин и без ex-subs. Перевес B решающий.
- **False blockers:** оба «launch with changes», фактический исход iter1 — fail → блокировок нет; A 0, B 0.
- **Страта:** якорная семья T1; L1 (T1-02) корректен по осям; конфликт T1-02 vs T1-04 разрешён через P-02, не усреднён.

## RH-03 — страта 2. GT: inconclusive Total / Green SUCCESS, var2 rolled out (#6878)

Факт (GT-RH-03): Total-метрики обеих платформ — ничего значимого (ближайшие p=0.05–0.06);
решение принято по scenario-funnel (Christmas splash) +30–40% revenue/ARPU БЕЗ p-values;
var3 (цена $24.99): ARPPU в сценарии +23.76% iOS / +13.37% And, но And splash-click −3.02%
(banner −16.19%) — верх воронки ослаб; refunds var2 iOS −26.4% p=0.05 (позитив); отсутствие
каннибализации; inventory-caveat: var3 смешивает дизайн и цену в одном арме.

- **C1**: B да (T2-02 L1, T2-01 L2, T3-01 L1-scoped, T1-07 L3); A нет. **C2**: 0/0. **C3**: B высокая, A низкая.
- **C4** (blind): B (уверенно). **C6**: 0/0. **C7_HUMAN_MIN**: 45 (2 076 слов ≈ 10 мин).
- **C5 outcome alignment: B.** B: «most likely no detectable effect at this power» на Total ✓✓
  (всё n.s.); идентификация прецедента T2-02 как того самого осеннего null ✓ (GT: #6878 —
  итерация Halloween T2-02); прогноз структуры var3 «conversion down, ARPPU up» ✓✓ (сценарный
  ARPPU вверх, And click-CR вниз); re-scope метрики на exposed/seasonal funnel = ровно то,
  чем команда фактически обосновала решение ✓✓; unbundle price/creative ✓ (inventory-caveat
  подтверждает нечитаемость C). Не подтверждён refund-риск в C (n.s.) — подан как guardrail,
  не прогноз; delivery-провал T2-02 (~9% плана) не повторился (выборка ниже design-числа, но
  duration-чек complete) — риск, не прогноз. A: Total null ✓, структура C ✓, activation-gated
  read ✓ — сильный ответ, но прогнозы ungrounded, прецедент не опознан, и негативный сценарий
  animation-friction не подтверждён (Animation View End ~94%). Перевес B.
- **False blockers:** B «redesign before launch» при фактическом Green SUCCESS — проверка §5:
  причины блокировки (дилюция Total-метрики; underpowered read; confound price+creative в C)
  ПОДТВЕРДИЛИСЬ фактом (Total действительно весь n.s. — решение пришлось выносить по
  непредрегистрированному scenario-funnel без значимости; confound подтверждён inventory-
  caveat). Блокировка с подтвердившимися причинами — НЕ false blocker. A — «launch with
  changes», не блокирует. Итог: A 0, B 0.
- **Страта:** аналоги из type2-кластера той же поверхности; T1-07 удержан на явном L3.

## RH-04 — страта 2. GT: significant-negative, killed (#6902)

Факт (GT-RH-04): аплифта нет нигде; primary CR to Access: And var3 −13% p=0.023 (значимо),
остальное отрицательно n.s.; ARPU все минус (n.s.); CTR var3 +35–47% при view→click Sale-карты
−27/−40% — «attention inflation rather than intent uplift» (вердикт страницы); Spotify-покупки
упали на обеих платформах (paywall reach −43..−51%); iOS var2 ret7d −3.07% p=0.026;
Forecast весь отрицательный. Решение: «Do not roll out either Variant 2 or Variant 3».

- **C1**: B да (T1-07 L2; T1-09, T2-01 L3); A нет. **C2**: 0/0. **C3**: B высокая, A низкая.
- **C4** (blind): B (уверенно). **C6**: B **1** (формальное, wording-level — подтверждено
  адверсариальной верификацией `c6_verification_rh04.md` ДО вскрытия GT; фраза «Wrapper changes
  without offer changes have not lifted purchases in this corpus» — овергенерализация класса
  P-10/T1-09; вердикт/прогноз/рекомендации на ней не строятся); A 0. **C7_HUMAN_MIN**: 45 (1 907 слов ≈ 9 мин).
- **C5 outcome alignment: B (с малым перевесом).** B: «attention ≠ intent» (P-03) — GT-вердикт
  страницы почти дословно воспроизводит паттерн («attention inflation rather than intent
  uplift») ✓✓; риск демоции Spotify-тайла с stop-rule ✓✓ (главный фактический ущерб: покупки
  40→26/32 iOS, 18→6/8 And, reach −50%); within-showcase cannibalization ✓ (Sale And −24/−56%,
  Courses вниз); «not surprised by net-negative Spotify», «surprised by significant Total lift»
  ✓; «drop the personalization framing — ничего персонализированного не тестируется» ✓
  (transfer-bounds GT: оффер-персонализация не опровергнута); «even a significant CR win may
  not clear +$500/day» ✓ (Forecast −$101..−$856/day). Промах B: goal-метрика «flat-to-modestly
  positive» против факта «отрицательно, у And var3 значимо» — знак не угадан; retention-цена
  ожидалась в арме C (auto-advance), а проявилась в iOS var2. A: диапазон −10%..+15% накрыл
  факт ✓ (точечный прогноз ближе, чем у B), Spotify-потеря ✓, cannibalization free-картами ✓,
  «drop arm C» ≈ факт (var3 — единственный значимый минус). Перевес B — по механизменному
  совпадению с уроками GT (attention≠intent, демоция концентрированного оффера, personalization-
  фрейминг) и guardrail-пакету; численно прогноз A был ближе. Оба вердикта «launch with
  changes» при фактическом killed — неблокирующие, к false blockers отношения не имеют.
- **False blockers:** A 0, B 0 (блокировок не было; исход негативный).
- **Страта:** T1-07 честно L2-warning; T1-09/T2-01 строго L3; L1 честно отсутствует.

## RH-05 — страта 3. GT: mixed / Green SUCCESS, var3 rolled out «monitor Charge → Cancel» (#7328)

Факт (GT-RH-05): var3 ARPU +15.26% p=0.024 (значимо), trial→charge +28.42% p=0.008 (главный
драйвер); charge cr +6.95% n.s.; var2 — ничего значимого (все p≥0.152); механизм — сдвиг
payment-mix: CreditCard 68.25%→55.73%, PayPal/GPay/APay вверх; цена победы — 14d cancel
+31.73% p=0.043 (почти во всех методах) и retention var3 значимо хуже (7d −7.23% p=0.021);
post-rollout: ARPU p=0.053, cancel-штраф остался значимым. Решение: «Rollout group 3 but
monitor Charge → Cancel conversion».

- **C1**: B да (T3-05 L3 guardrail-инсайт + P-11/P-13); A нет. **C2**: 0/0. **C3**: B высокая
  (единственный источник корректно L3), A низкая. **C4** (blind): B (с небольшим перевесом).
  **C6**: 0/0. **C7_HUMAN_MIN**: 40 (1 604 слова ≈ 8 мин).
- **C5 outcome alignment: B (с оговоркой по вердикту).** B: «shift in payment-method mix toward
  one-click methods (strongest in arm C)» — ЕДИНСТВЕННОЕ в паре точное предсказание механизма,
  подтверждено дословно GT-инсайтом ✓✓; guardrail-пакет «14d refunds/chargebacks/cancels по
  методу + AOV + stop-rules» попал в фактическую цену победы, и «monitor Charge → Cancel» —
  дословно решение команды ✓✓; ресскоуп метрики на payment-page ✓ (фактический анализ вёлся
  на checkout-популяции); инструментировать method-mix ✓ (стало главным Insights-разделом).
  Промах B: «most probable read is uninterpretable null» — факт: var3 значим (+15.26% ARPU);
  «удивит double-digit conversion lift» — trial→charge +28.42% случился (ARPU-лифт двузначный,
  conversion cr — нет). A: вердикт «launch with changes» ближе к фактическому успешному
  запуску; «small positive or null» для B-арма ✓ (var2 n.s.); но арм C у A «directionally
  ambiguous» (мимо — C победил), method-mix риск без конкретики. Двухфакторный итог (механизм
  + цена победы у B против verdict-близости у A): перевес B.
- **False blockers:** B «redesign before launch» при фактическом успехе — проверка §5: причины
  блокировки — реальные, подтверждённые дефекты карточки (power-таблица 0.05%/500%/n=1996
  внутренне противоречива — GT фиксирует design-ячейки «recorded as 0 — not calculated»;
  goal-метрика «tab view → subscribed» не по затронутой поверхности — фактический анализ
  вёлся на checkout-скоупе; Analytics-секция пуста; method-mix-риск подтверждён значимым
  cancel/retention-штрафом). Прогнозное следствие («null») не сбылось, но §5 требует
  неподтверждённости ПРИЧИН блокировки, а причины подтверждены как дефекты дизайна и как
  реализовавшийся guardrail-риск → НЕ false blocker (симметрично трактовке FLOW-579, где
  блокирующие вердикты с подтвердившимися причинами не считались). A не блокирует. A 0, B 0.
- **Страта 3:** образцовое поведение — единственный источник T3-05 честно L3, «no direct
  analogs» явно, продуктовые выводы явно исключены из переноса.

## RH-06 — страта 3. GT: inconclusive/directionally-negative, killed (#7598)

Факт (GT-RH-06): ARPU −10.36% p=0.11, все money-метрики направленно вниз (n.s.); trials +8%
n.s. при trial→charge −9.23% n.s.; paywall→subscribed −40% (без p-value); Forecast −$1,551/day
против плана +$500/day; retention 7d/14d значимо ЛУЧШЕ в тесте (+1.39/+1.43%, p=0.000);
takeaway: удалённый $19.99 instant работал как якорь/альтернатива — без него часть аудитории
просто не подписывается; next steps: baner-концепт оставить, вернуть 3 плана.

- **C1**: B да (T3-03 L1 — центральное контрсвидетельство миграции спроса; T3-05 L1; T3-06 L2;
  T3-02 L3); A нет. **C2**: 0/0. **C3**: B высокая (конфликт T3-03 vs T3-05 разрешён явно), A низкая.
- **C4** (blind): B (уверенно). **C6**: 0/0. **C7_HUMAN_MIN**: 50 (2 179 слов ≈ 11 мин).
- **C5 outcome alignment: B (решающий перевес).** B: «substitution, not migration — удаление
  cheapest instant теряет его покупателей, а не конвертирует в триалы» [T3-03, P-06] — GT-
  takeaway воспроизводит это почти дословно («The removed instant offer likely worked as an
  anchor/alternative… some users simply do not subscribe rather than moving to trial») ✓✓✓;
  «charges and net revenue flat-to-down» ✓ (факт: направленно вниз всюду, −$1,551/day);
  «modeled trial→charge 24.18→30% has no support» ✓ (факт: −9.23%); «trial-шифт не окупается
  в окне» ✓; hedge-арм с exit-offer по прежним $19.99 — направленно совпадает с фактическим
  next step «вернуть 3 плана» (сохранить якорь) ✓; ~16× несостыковка критерия успеха — реальный
  дефект карточки; предвосхищение ПОЗИТИВНОЙ retention-стороны («cleaner two-option choice
  could improve early satisfaction/retention») — единственное плечо за оба прогона, задевшее
  фактический значимый retention-плюс ✓ (закрывает «retention-слепоту» из систематики FLOW-579,
  частично). Промах B: power/delivery-риск «~30 plan-menu views/день, выборка недостижима» не
  подтверждён — GT: «design (6 days, sample size) was met as planned». A: тоже «redesign before
  launch»; «short-window charged revenue flat-to-negative» ✓; kill-критерий по trial→charge 30%
  ✓; но центрального механизма провала (якорная роль instant) у A нет — A трактует риск как
  mix-shift/отложенные триалы, не как потерю покупателей. Перевес B.
- **False blockers:** оба «redesign before launch», фактический исход — fail/killed → блокировка
  оправдана исходом; A 0, B 0.
- **Страта 3:** близость корректно пересчитана к САМОМУ кейсу — web-источники T3-03/T3-05
  законно L1 (подтверждено детерминированным §2.2), дальние T3-06/T3-02 удержаны на L2/L3.

---

## Агрегаты

- **C4 (blind):** B 6 / A 0 / tie 0 (все «уверенно», RH-05 — «с небольшим перевесом»).
- **C1:** B 6/6 (включая обе страты 2 и обе страты 3); A 0/6.
- **C2:** B 0, A 0 (12 ответов чисты).
- **C6:** B **1** (RH-04, формальное wording-level, подтверждено верификацией до вскрытия), A 0.
- **C5 (unblind): B 6 · A 0 · tie 0** (RH-04 и RH-05 — с оговорками, зафиксированными выше).
- **False blockers: A 0, B 0** (все блокирующие вердикты — RH-03 B, RH-05 B, RH-06 A+B — имели
  подтверждённые причины и/или подтверждённый исходом провал).
- **C7:** human-review pending (оценки судей 40–50 мин относятся к полной сверке цитат с KB;
  чтение пары по объёму 1 604–2 215 слов ≈ 8–11 мин) — меряется в shadow pilot FLOW-566.
