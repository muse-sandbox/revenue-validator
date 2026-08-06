# HX-03 — ground truth (doc-side)
Источник: 551496203 | [2024-09-10] UG App: tour update – Tour Update always on Explorer [2024-12-11] | https://alice.mu.se/pages/viewpage.action?pageId=551496203
Эксперимент(ы): #5262 (Iteration #1); Jira: UMN-6557

## Прогноз IR (повтор из pre-launch, для сверки plan/fact)
Модель: +30% завершивших Tour Install видят tour update, 1% из них конвертится в Access. iOS: Access 335→363 (+8.5%), Revenue $3,965→$4,295 (+$330), ARPU $0.43→$0.46 (+7%). Android: Access 193→225 (+16%), Revenue $2,295→$2,682 (+$387), ARPU $0.21→$0.25 (+16%). Горизонт в документе явно не подписан (похоже на сутки).

## Факт: target metric и денежные метрики
- iOS (control / variation 2): members 19,731 / 19,962; revenue $9,825 / $9,455; ARPU $0.50 / $0.47, diff −4.88%, p=0.50; AOV +0.79% p=0.77; ARPPU +0.32% p=0.91; access CR 4.10%→3.92% (−4.33%, p=0.37); charge CR 2.11%→2.00% (−5.19%, p=0.44); trial→charge +0.79% p=0.94; charge→14d cancel −14.20% p=0.26.
- Android (control / variation 2): members 19,923 / 19,638; revenue $4,250 / $4,217; ARPU $0.21 / $0.21, diff +0.66%, p=0.96; AOV −2.84% p=0.64; ARPPU −0.78% p=0.90; access CR 2.14%→2.39% (+11.93%, p=0.088); charge CR +1.45% p=0.90; trial→charge −1.42% p=0.93; charge→14d cancel +26.49% p=0.33.
- Funnel новой точки входа (variation): iOS Preview View 19,961 → Click 789 (3.95%) → Success 740 (3.71%) → Access 10 (0.05%); Android Preview View 18,336 → Click 1,002 (5.46%) → Success 802 (4.37%) → Access 10 (0.05%). Планировалось Tour Update → Access = 1%; факт 0.05% (в 20 раз ниже плана).
- Вывод документа (Decision): «no significant changes in monetization metrics», «low 0.05% conversion rate from tour update banner → access on both platforms».

## Достигнутая выборка и длительность (vs дизайн)
Дизайн: iOS 10 дней / 19,600 на арм; Android 2 дня / 3,661 на арм. Факт: 6 дней; iOS 19,731 + 19,962 (арм ≈ дизайну), Android 19,923 + 19,638 (в ~5.4 раза больше дизайна на арм). Чек «duration of exp >= design» помечен incomplete (6 < 10 дней для iOS); «A/B balance is maintained» — complete; видимых багов и внешних эффектов не отмечено (чеки 915/916 complete).

## Денежные guardrails (факт)
Отдельные guardrails до запуска не заявлялись. Фактические денежные разрезы (AOV, ARPPU, cancel rate) — без значимых изменений (см. выше); Android charge→14d cancel +26.49% (p=0.33, не значимо).

## Каннибализация / refunds / reconversion (факт)
Не измерялись / не обсуждаются в результатах — missing. (Пре-ланч заявлял проверку синергии с sales-баннером; в итогах отдельного разбора нет.)

## Rollout/rollback по документу (решение, формулировка)
Статус страницы: FAIL. «Unfortunately after the test we realised that we didn't get the expected results and moreover we see a worse performance. The only positive moment … slightly better retention rate for the iOS, but it is not enough to make a decisions on relaunching the experiment. So we close it as failed.» Decision: «didn't make any improvement, no need to rollout test variation». Next steps: у баннера очень низкий click rate — можно конвертировать в модал или сделать постоянным в большем числе мест. Ретеншен: iOS ret1d +1.21% (p=0.56), ret7d +2.23% (p=0.20) — не значимо; Android ret1d −4.49% (p=0.049), ret7d −3.77% (p=0.044) — значимое ухудшение.

## Post-rollout данные
missing — раскатки не было; секция Post-rollout analysis пустая (шаблон).

## Data issues / ограничения измерения
- Тест остановлен на 6-й день при дизайне 10 дней для iOS (чек длительности incomplete) — iOS формально недобрал длительность, хотя выборка на арм достигнута.
- Блок «Forecast (per day)» на странице фактически содержит per-day сравнение арм (iOS: control $4,793/день vs variation $4,559/день, −$234/день; Android: +$14/день), а не сверку с пре-ланч прогнозом; прямой plan-vs-fact таблицы по IR нет.
- Заголовки funnel-блоков и подписи выборок в макросах местами неаккуратны (Android preview view 18,336 при 19,638 members), но на выводы не влияют.
- SRM не отмечен («A/B balance is maintained»).

## Черновая классификация по правилам FLOW-562
**no meaningful uplift** (с негативным сигналом по Android-ретеншену). Механизм монетизации фактически не сработал: конверсия из preview в access составила 0.05% против плановых 1% (в 20 раз ниже), поэтому запланированный аплифт ARPU (+7% iOS / +16% Android) не реализовался. iOS достиг дизайн-выборки на арм при MDE +7% и показал ARPU −4.88% (p=0.50) — плановый эффект уверенно не подтверждён; Android при выборке в разы выше дизайна показал +0.66% (p=0.96). Дополнительно: значимое ухудшение ретеншена Android (ret1d p=0.049, ret7d p=0.044). Документ закрывает эксперимент как FAIL без раскатки.

## Тип результата: CM / EE / OE / NM (по каждому денежному числу)
- ARPU/revenue/AOV/ARPPU/charge CR по армам (iOS $0.50 vs $0.47; Android $0.21 vs $0.21; revenue $9,825/$9,455 и $4,250/$4,217) — CM (прямое A/B-измерение со стат-тестом).
- Per-day разница revenue из блока «Forecast (per day)» (iOS −$234/день, Android +$14/день) — EE (пересчёт факта на день, без CI).
- Пре-ланч incremental revenue (+$330 и +$387) — прогнозная модель, фактом не подтверждена; фактического измерения IR как отдельного числа нет — NM в части «сколько денег принесла бы раскатка».
- Каннибализация / refunds / reconversion в деньгах — NM (не измерялись).
