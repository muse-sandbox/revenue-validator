# Validator V0 — development-пример

Кейс development set (FLOW-548): **699804101 — [2025-06-16] UG Web: Apple Pay for Chrome checkout**, эксперимент #6287. Вход — только PRE-LAUNCH-часть извлечения `output/flow548/extractions/699804101.md`. Разделы RESULTS при прогоне не использовались.

---

## ПРОХОД 1: pre-launch snapshot

- **S1. Цель и «почему сейчас»:** «Increase conversion to access purchase by enabling Apple Pay for Chrome users»; обоснование — Apple Pay быстрорастущий платёжный метод (Statista, Stripe), «probably, a part of our audience also trusts and finds this method convenient» | цель — assumption (мнение автора), рост метода — fact (внешние отчёты) | Research and Context.
- **S2. Изменение:** добавить Apple Pay в чекаут для Chrome (только macOS), кнопка во все чекауты (courses, songbooks, upsells, offers), адаптация под one-click | fact (описание решения) | Solution. **Флаг цена/оффер: цена НЕ меняется** — добавляется способ оплаты при тех же ценах и продуктах.
- **S3. Аудитория/сценарий:** эксперимент #6287, «all users with access in tour», UG_WEB; exposure — Chrome/macOS открывает чекаут | fact | Experiment design, Analytics. **Соседние денежные потоки поверхности:** те же чекауты сейчас монетизируются картой/PayPal (payment system research: card 61–77%) — новый метод может замещать существующие оплаты, а не добавлять новые.
- **S4. Baseline:** checkout → access = 26.99% (control); Safari Apple Pay checkout→charge = 2.52%, ~10 accesses/день через Apple Pay в Safari | fact | Research results, A/B test model.
- **S5. Reach:** явно users/day — **missing**; производное: ~289 users on checkout/день (= sample 4624 ÷ 16 дней; в модели 289 users on checkout на вариацию) | производное из forecast/design | A/B test model, Design.
- **S6. Денежная модель:** цепочка users on checkout → apple pay accesses (11) → apple pay charges (7) → revenue $359 → total revenue $434/ARPU; прогноз +$434 total revenue на 289 users on checkout на вариацию; **горизонт явно не указан**; модель помечена «optimistic variant without cannibalization»; ARPU +15% ($10.07 → $11.57) | forecast | A/B test model.
- **S7. Центральные коэффициенты и evidence:** (1) конверсия checkout→charge через Apple Pay = 2.52% — взята из замера Safari (Metabase question 4515, таблица payment system research Safari vs Chrome) — fact как замер, assumption как перенос Safari→Chrome; (2) ARPPU $62 constant — fact (текущий уровень) + assumption (неизменность); (3) доля кликнувших Apple Pay — из Safari-долей метода (15%) — fact-замер с переносом | Research results, Payment system research.
- **S8. Gains/losses:** строки потерь нет; риск каннибализации осознан («optimistic variant without cannibalization»), но не смоделирован числом | missing (строка потерь) | A/B test model.
- **S9. Target/guardrails:** target — checkout → access, % (Goal); guardrails явно не объявлены; в гипотезе «without a drop in average order value» (AOV как неявный guardrail) | fact (target), assumption/missing (guardrails) | Experiment design, Hypothesis.
- **S10. Дизайн:** Baseline 26.99%, Lift 14%, MDE 0.084, Power 0.8, Alpha 0.05, Sample 4624/вариацию, Duration 16 дней | fact (зафиксирован) | Experiment design. **MDE посчитан по конверсионной метрике** (checkout→access), не по денежной.
- **S11. Сегменты чтения результата:** заранее в конфиге: Total (free/desktop); **Apple payments only** (payment_method = 'Apple Pay'); Apple Checkout Funnel | fact | «#6287 config».
- **S12. План измерения после rollout:** **missing**.
- **S13. Stop-rule:** **missing**.
- **S14. Противоречия/открытые вопросы:** в тексте гипотезы lift оставлен плейсхолдером «N%» (число только в design-таблице); горизонт денежной модели не указан; sample size противоречив в разных местах документа (4624 в design-шаблоне) | наблюдение по документу.

## ПРОХОД 2: критерии и рекомендация

**1. Рекомендация: `launch`. Уверенность: medium** — модель откалибрована замером и её downside ограничен механикой, но горизонт прогноза не задан, а строка потерь и post-rollout план отсутствуют (средние concern → условия запуска).

**2. Обоснование.** Единственный центральный коэффициент модели (checkout→charge через Apple Pay = 2.52%) — не «из головы», а замер собственного Safari-трафика (S7), что для корпуса паттернов является главным отличием сбывшихся прогнозов. Цена и состав оффера не меняются (S2), поэтому эластичность не задействована. Главный денежный риск — субституция: пользователь заплатил бы картой, а платит Apple Pay; но при неизменных ценах и ARPPU (S7) такая субституция почти не меняет revenue, т.е. реалистичный нижний сценарий ≈ $0, а не минус. Деньги в Total ожидаемо будут нечитаемы (apple-eligible — малая доля трафика), но сегмент чтения денег «Apple payments only» объявлен заранее в конфиге (S11), что закрывает проверяемость денежного результата.

**3. Ожидаемая incremental revenue.** Прогноз автора: +$434 total revenue (из них $359 Apple Pay) на 289 users on checkout на вариацию, горизонт не указан (S6). Реалистичный диапазон валидатора: от ≈ $0 (полная субституция карты при том же чеке; ARPPU в модели constant $62) до +$434 (нулевая каннибализация — собственная «оптимистичная» пометка автора). Точнее внутри диапазона не восстановимо: в документе нет замера доли новых-vs-переключившихся покупателей. Горизонт диапазона — тот же неуказанный горизонт модели; это отдельный пункт missing.

**4. Таблица К1–К6.**

| Критерий | Статус | Severity | Обоснование |
|---|---|---|---|
| К1 эластичность | pass (n/a) | — | Цена/оффер не меняются (S2) — добавляется способ оплаты при тех же ценах. |
| К2 evidence коэффициентов | pass | — | Центральный коэффициент 2.52% checkout→charge — замер Safari (Metabase q4515, S7); перенос Safari→Chrome — допущение, но на собственной аудитории и той же поверхности. |
| К3 gains − losses | concern | средний | Строки потерь нет, модель явно «optimistic without cannibalization» (S8); severity средний: субституция метода оплаты при неизменных ценах/ARPPU ограничивает потерю снизу ≈ 0, знак impact не меняется. |
| К4 достижимость sample | concern | средний | Reach как users/day не замерен SQL-ом (S5 missing, есть лишь производное 289/день из модели); sample 4624/16 дней правдоподобен относительно baseline-данных чекаута, но pre-launch замера reach в документе нет. |
| К5 мощность под деньги | concern | средний | MDE посчитан по конверсии checkout→access (S10), а обещан ARPU +15% (S6); закрыто наполовину: сегмент чтения денег «Apple payments only» объявлен заранее (S11), но MDE/SD по денежной метрике не посчитаны. |
| К6 post-rollout измерение | concern | средний | Плана измерения после rollout нет (S12 missing), stop-rule нет (S13 missing). |

**5. Критичные допущения** (на которых держится положительный impact): перенос Safari-конверсии 2.52% на Chrome/macOS (S7, assumption); отсутствие каннибализации карты/PayPal (S8, assumption «optimistic variant»); ARPPU constant $62 (S7, assumption); lift +14% по checkout→access (S6, forecast).

**6. Риски каннибализации/refunds/guardrails.** Каннибализация: замещение card/PayPal-оплат (сейчас 61–77% метода, S3) — съедает инкремент до ≈ 0, но не в минус при том же чеке; риск для AOV, если чеки Apple Pay систематически ниже. Refunds: не рассмотрены в модели (missing) — one-click-оплата может изменить refund-поведение, поток refunds на этой поверхности существует. Guardrails: формально не объявлены; неявный AOV из гипотезы стоит сделать явным guardrail + добавить refund rate.

**7. Stop-rule.** В документе отсутствует (S13). Предложение валидатора (не данные документа): остановить эксперимент досрочно при значимом падении AOV или значимом росте refund rate в тестовой вариации; при раскатке — откат, если в сегменте Apple payments динамика charges не подтверждает модельный уровень.

**8. Что изменит рекомендацию.** В сторону `revise`: если замер reach покажет, что sample 4624/вариацию недостижим за разумную duration (К4), или если появятся данные, что чек/ARPPU Apple Pay-покупок существенно ниже карточных (тогда субституция даёт минус и К3 становится критичным). Условия запуска (обязательные, но не блокирующие): (а) указать горизонт денежной модели; (б) объявить AOV и refund rate guardrail-ами; (в) до запуска зафиксировать post-rollout протокол — минимум observational: доля/charges Apple Pay-метода и суммарный revenue чекаутов за 30/90d против пред-rollout базы с сезонным контролем (К6); (г) SQL-замер reach за 2–4 недели (К4).

**9. Список `missing`** (значения не достраивались): reach users/day как замер (S5); временной горизонт денежной модели (S6); строка потерь/каннибализации числом (S8); явные guardrails (S9); MDE по денежной метрике (S10); план post-rollout измерения (S12); stop-rule (S13); refunds/reconversion/LTV-риски (S8/S14); заполненный lift в тексте гипотезы (плейсхолдер «N%», S14).

---

*Примечание (вне ответа валидатора, для development-сверки): фактический исход кейса в dev-set — «подтверждённый денежный успех» с оговорками FLOW-551 (positive; значимость денег — именно в заранее объявленном сегменте Apple payments only, Total ARPU ns; post-rollout замер так и не был сделан). Рекомендация `launch` с условиями (б)–(в) согласуется с фактом и заранее называет оба слабых места, проявившихся после запуска.*
