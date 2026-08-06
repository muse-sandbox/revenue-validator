# UG Revenue User Flow — текстовая карта V0 (FLOW-576)

Дата: 2026-08-04. Статус: **V0, черновик до проверки с продуктом и аналитиком** (см. §7).
Назначение: единая текстовая схема monetization flow, по которой размечается место
каждого revenue-эксперимента (FLOW-577): этап × сегмент × платформа × механизм.

Источники: `context/ultimate-guitar-product-context.md` (§6.8, §13, §16),
`context/ab-experiment-split-mechanics.md`, `context/store-commissions.md`,
`context/rules/subscription-identity-and-attribution.md`, `context/rules/date-windows-and-maturity.md`,
`context/mobile-app-screens-analytics.md` (tour/paywall), каталоги событий
`context/data-warehouse/tables_events/` (`ug_subscriptions_events`, payment funnel app,
monetization web, tour), `.claude/skills/ug-experiment-calculator/references/subscriptions.md`.

---

## 0. Как читать карту

Этапы пронумерованы **S0–S9**. Внутри этапа — ветки по платформе `[iOS]` `[And]` `[Web]`
и по сегменту пользователя `{free}` `{ex-paid}` `{paid}`. Каждый этап привязан к
доступным событиям аналитики (клиентские — `ug_rt_events_app` / `ug_rt_events_web`,
бэкенд-подписочные — `default.ug_subscriptions_events`).

Схема одной строкой (scope задачи):

```
действие пользователя (S1) → eligibility (S2) → monetization surface (S3)
→ exposure (S4) → paywall intent / checkout (S5) → trial / purchase (S6)
→ charge (S7) → renewal / cancel / refund (S8) → net revenue (S9)
```

Сегменты (термины из remote-tour конфига, условие `segment` = `free` / `ex-paid` / `paid`,
источник — `formatRightsSegment()` в RN-приложении):

- `{free}` — прав нет и не было: основной конверсионный поток (trial / instant / intro).
- `{ex-paid}` — права были и истекли: целевая аудитория winback-офферов и повторных пейволлов.
- `{paid}` — права активны: пейволлы должны скипаться (tour skip / Welcome Back);
  показ пейволла платному — паттерн бага «paywall fatigue for paid».

---

## S0. Вход в продукт (acquisition)

Не revenue-этап сам по себе, но определяет атрибуцию всей воронки.

- `[App]` Установка. Каждый инсталл классифицируется в **traffic type**
  `paid` (AppsFlyer-атрибуция рекламы) / `referral` (переход с собственного mobweb UG,
  бэкенд-матчинг по `(app, user_ip)`, событие `App Install`) / `organic` (остальное).
  Приоритет: paid > referral > organic. Тип записывается в `default.ug_installs.traffic_source`
  и прокидывается как `Type` в события `Banner Tour View` / `Paywall View` / `Banner Upgrade View`.
  События старта: `Tour Start` (New Install / Reinstall), `Tour Referral Start`.
- `[Web]` SEO-страницы табов / лендинги / прямой заход. Атрибуция входа в воронку —
  `funnel_source` (точка входа) + `funnel_start_action` (действие, запустившее воронку,
  в т.ч. mid-funnel шаги типа Ambulance) на `ug_subscriptions_events`.

## S1. Действие пользователя — триггер монетизации

- `[App]` `{free}` `{ex-paid}` Первый запуск / апдейт → **Tour** (install или update):
  remote tour из бэкенд-конфига (`u_guitarcom.tour`, endpoint `app/tourBuilder`),
  RN `defaultTour` — только фолбэк. Квиз → `Progress` → `PrePaywall` → `Paywall`.
  События шагов: `Tour Start`, `Tour <Step> View/Success`, `Tour Loader View`, `Tour End`.
- `[App]` Попытка использовать премиум-фичу: Official/Pro Tab, autoscroll/SmartScroll,
  transpose, simplify, tuner/metronome, print/export, backing track, Practice Mode,
  Courses/Songbooks (`Tab Official Open`, `paywall_view` курсов и т.п.).
- `[App]` Маркетинговые поверхности вне тура: splash (`Splash View`, source push/direct),
  sale banner (`Sale Banner View`), price increase modal, upgrade-раздел.
- `[App]` `{ex-paid}` Запуск приложения → **WinbackResolver**: проверка истории покупок
  (`Local Subscription Request/Success`, `Pro Subscription Check`) и решение о winback-сплэше
  (`Winback Splash Show Try`, params `d_pro_sku`, `d_was_shown`).
- `[Web]` Премиум-CTA на странице таба / Pro-лендинг (`Landing Upgrade Open`,
  `Landing W Upgrade Open`), email/спецоффер (`Landing Email Offer View`),
  upsell в чекауте, exit-intent **Ambulance** (`Landing Ambulance View`) — mid-funnel
  дисконтный шаг, достижимый из многих `funnel_source`.
- `[Push/CRM]` push/email → paywall/лендинг. ⚠️ События входа из CRM-кампаний
  систематически не каталогизированы (см. §7).

## S2. Eligibility — кто и что может увидеть

Три независимых слоя:

1. **Права/сегмент** (`{free}`/`{ex-paid}`/`{paid}`): активные права Pro/Edu/Book/Sing
   скипают пейволлы (в турах — `available()`/skip-условия: «skips paywall if rights valid»,
   `Tour Pro Rights Success`; для `{paid}` в туре — `Tour Skip` или `Welcome Back Offer`).
2. **Распределение в эксперименты** (влияет на то, какой вариант surface увидит юзер):
   slots (1–100, ≈1%/слот) + `clients` + `clients_options` (только `version` / `country` /
   `platform` / `locale`); вариация — хэш `(exp_id, member_id)`. Start event на сплит
   **не влияет** — он только активация в аналитике. Rollout (`success_variation`)
   игнорирует slots → 100% eligible-аудитории.
3. **Сторовая eligibility офферов**:
   - `[iOS]` Apple intro/trial — один intro на subscription group; проверка
     `Promo Offer Check` (`params.purchaseHistory` = пары `productId:offerId`).
     Отказ Apple в intro → «ex-trial leak»: подписка `trial > 0` с charge в день 0
     на **том же** продукте.
   - `[And]` Google eligibility: `Promo Offer Check` (список product ids).
   - `[Web]` ограничений стора нет; intro-планы — собственная механика (S6).

Платформенные отличия механики на этом этапе:
- `[And]` шаг `PrePaywall` в туре скипается (iOS видит pre-paywall, Android — нет).
- `[iOS]` instant offer часто оформлен как plan switch того же `subscription_id`
  (другой продукт), что меняет атрибуцию (S6).

## S3. Monetization surface — что показываем

- `[App]` Tour paywall (нода `Paywall` remote tour; `params.paywall_type`,
  `params.product_id_1..N` — состав SKU на экране), пост-отказные ноды
  `TrialToInstant` / `SecondPaywall`.
- `[App]` In-app paywall вне тура (`FeatureNativeView` и др.) — upgrade/purchase.
- `[App]` Splash / sale splash / winback splash / anniversary splash / price increase.
- `[Web]` Pro/Edu/Books лендинги; слой перед планами (`Landing Layer Before Plans View`);
  выбор плана (`Landing Plans View`); спецофферы: email offer, **Ambulance**,
  winback/complete-registration модалки; books precheckout.

Разметка экспериментов: surface — основное «место» эксперимента; уточняется
источником (`value`/`funnel_source`) и составом SKU (`product_id_1..N`).

## S4. Exposure — факт показа (счётная точка воронки)

- `[App]` `Paywall View` — всегда; плюс парный `Banner Tour View` (tour) или
  `Banner Upgrade View` (не-tour). Payload: `value`/`lc_value` = источник пейволла,
  `Type` = install traffic type, `params.paywall_type` (purchase/upgrade),
  `params.paywall_rights`, `params.product_id_1..N`. Сплэши: `Splash View`.
- `[Web]` `Landing Upgrade Open` → `Landing Plans View` (+ `Landing Ambulance View`,
  `Landing Email Offer View` для спецшагов).
- **Активация эксперимента** — строго по его `experiment_event_start` из
  `mysql_u_guitarcom.ab_experiment` (часто это paywall-view-событие, `Tour End`,
  `App Start`…). `App Experiment Start` — только в паре с `item_id = <exp_id>`.
  Не считать аудиторию по массивам `experiments.id/variation` — это distribution,
  не exposure. Если start event ниже точки расхождения веток — проверять SRM.

## S5. Интент и checkout

- `[App]` `Banner Plan Select` → `Banner Free Trial Toggle` (переключение trial-режима) →
  `Banner Purchase Click` (`Product` = SKU, `Offer`) → `Purchase Process Start` →
  нативный стор-диалог (Apple/Google). Восстановление: `Banner Restore Click`.
- `[Web]` `Landing Plans Select` / `Landing Plan Click` → `Purchase Process Start` →
  `Landing Checkout View` (Braintree: карта / PayPal / Apple Pay / Google Pay;
  `Landing Instant Pay Available`) → `Landing Purchase Click` →
  ошибки/валидация (`Landing Purchase Validation Error`, `Landing Purchase Error`),
  антибот (`Landing Checkout Captcha *`, `CF Bot Detection *`).
- Гость на web может регистрироваться внутри чекаута (`Landing Sign Up Success`,
  `type: checkout_form`).

## S6. Результат покупки — тип доступа (access)

Клиентское подтверждение:
- `[App]` `Purchased`, `Purchase Process Finish` (успех) / `Canceled` / `Failed`.
- `[Web]` `PURCHASE_SUCCESS_<PRO|EDU|BOOKS|BOOKS_EDU>` + generic `PURCHASE_SUCCESS`,
  `Purchased View`, `Purchase Receipt Send`.

Бэкенд-якорь: **`Subscribed`** в `default.ug_subscriptions_events` — единственная строка
с полным клиентским контекстом (`unified_id`, `funnel_source`, `experiments.*`, страна,
версия…). Идентичность подписки: `(subscription_id, product_code)` — обязательно на iOS
(id переиспользуется между продуктами); web intro — два `subscription_id`, мерджить
по `original_subscription_id`.

Типы доступа (классификация из `subscriptions_by_sub_date.sql` / `monetization_metrics.sql`):

| Тип | Признак | Платформы |
|---|---|---|
| **Trial** | `trial > 0`, нет charge в день 0 | все |
| **Instant offer** | charge в день 0; `funnel_source` = `Tour Instant Offer` / `Instant Offer`. `[iOS]`: часто plan switch того же `subscription_id` на другой продукт — отдельная подписка, НЕ конверсия триала | все |
| **Ex-trial (leak)** | `[iOS]` `trial > 0` + charge день 0 на том же продукте = Apple отказал в intro | iOS |
| **Intro access** | `[Web]` две ноги (`original_subscription_id`), с 2026-07-21 базовая нога пишется с `trial = 366` — это НЕ trial; флаг `is_access_intro` | web |
| **OTP** | one-time purchase (книги/контент): часто `Charged` без `Subscribed`; `is_otp` | все |
| **Restore** | `[iOS]` `Subscribed` переименовывается в `Restored` при `funnel_source` restore/silent restore — не новый доступ | iOS |

Шум, который надо исключать из доступов: web phantom checkout retries
(`Subscribed` → `Canceled` ≤ 60 с, без `Charged`, UG_WEB).

⚠️ «Purchase success ≠ access granted»: общего entitlement-события нет
(`Access Granted` существует только для Guitar Center promo); фактический доступ
проверяется по правам пользователя.

## S7. Charge — деньги

- Реализованные деньги — **только** событие `Charged` (сумма `usd_price` — gross).
  Цена на `Subscribed` — ожидаемая/заголовочная, деньгами не считается.
- Trial → charge: ожидаемая дата = `datetime_next_billing` базовой строки
  (`first_charge_expected_dt` в калькуляторе). Метрики: `trial -> charge, %`;
  `trial -> any charge, %` (добавляет instant того же сервиса в +1 день);
  гейт зрелости `pending trials share, % > 5%` ⇒ когорта незрелая.
- `[Web]` строка `Charged` попадает в таблицу с лагом ~8 дней ⇒ безопасная верхняя
  граница когорты `today() - 9`.
- Фантомы: `[iOS]` `Charged` с `payment_method='iTunes' AND billing_cycle=0` —
  исключать из денег (и только для `event='Charged'`, иначе теряются trial-старты).

## S8. Lifecycle после первой оплаты

| Переход | События | Платформы |
|---|---|---|
| Renewal | `Charged` (повторный; нумеровать по датам, не по `billing_cycle`) | все |
| Cancel autorenew | `Canceled`; `[Web]` предварительно `Cancellation Requested` | все |
| Billing issue → recovery | `[And]` `Entered Grace period` → `Recovered`; `[iOS]` `Recovered` (billing retry/grace через Apple-нотификации) | iOS/And |
| Autorenew re-enable | `Autorenew Enabled` | iOS/web |
| Plan change | `[Web]` `Switched Plan` + `Created After Plan Switch`; `[iOS]` `Upgrade` / `Crossgrade` / `Downgrade` (с `local_refund`/`usd_refund`); `[And]` `Switched Plan` | все |
| Pause (web) | `Paused` / `Created After Pause` / `Pause resumed` / `Created After Pause resumed` | web |
| Refund | `Refunded` (`[iOS]` пропорционально неиспользованному периоду; `[And]` voided purchases; `[Web]` Braintree) | все |
| Dispute / void | `Disputed`, `Voided` | web |
| Price increase | `Price Updated` (+ reminder flow) | — |
| Истечение → `{ex-paid}` | прав нет; юзер возвращается в S1 через winback-ветку | все |

Winback-петля: `{ex-paid}` → S1 (winback splash / повторный пейволл / discounts) →
S3–S7 заново. Отдельного «Winback Purchase»-события нет — атрибуция по
`funnel_source`/`value` источника.

## S9. Net revenue

Гросс → нет по `context/store-commissions.md` (поля `commission_*`/`net_usd_price`
в таблице НЕ заполнены — никогда не использовать):

- `[iOS]` ×0.70 первый год подписки, далее ×0.85 (per-charge шкала в `lifetime_revenue`);
- `[And]` ×0.85 (с 2022; ⚠️ с 2026-06-30 новые региональные тиры EEA/UK/US — следить за дрифтом);
- `[Web]` ×1.0 (комиссии Braintree/PayPal не моделируются).

Refunds вычитаются по refund-логике пакета (`refund_revenue`); канонические поля —
`revenue` / `lifetime_revenue` из `subscriptions_by_sub_date.sql`.

---

## 5. Сводка отличий iOS / Android, меняющих eligibility или механику

1. Tour: `PrePaywall` скипается на Android.
2. Intro/trial eligibility: Apple — один intro на subscription group (отказ ⇒ ex-trial
   leak с charge день 0); Google — своя проверка истории покупок.
3. Instant offer: iOS — plan switch внутри того же `subscription_id` (другой продукт,
   charge день 0) ⇒ отдельная подписка `(subscription_id, product)`; Android — отдельная покупка.
4. Идентичность подписки: iOS требует пары `(subscription_id, product_code)`;
   Android `subscription_id` = order id, `billing_cycle` парсится из суффикса заказа.
5. Grace period: явное событие `Entered Grace period` только Android; iOS — recovery
   через Apple-нотификации (`Recovered`), ground truth — `mysql_mob_api.subscription_ios_notification`.
6. Restore: событие `Restored` — только iOS (silent restore).
7. Refund: iOS — пропорциональный расчёт неиспользованного периода; Android — voided.
8. Комиссия: iOS 30%→15% после года; Android плоские 15%.
9. Фантомные charge: iOS-специфичный баг (`iTunes` + `billing_cycle=0`).

## 6. Правило разметки эксперимента по карте (для FLOW-577)

Каждый эксперимент однозначно описывается кортежем:

```
(этап S0–S9; поверхность из S3; сегмент {free|ex-paid|paid};
 платформа [iOS|And|Web]; механизм: что меняем —
 trigger / eligibility / surface-состав (SKU, цены, копирайт) /
 checkout / тип доступа / lifecycle-условия)
```

Примеры: «7568 Propensity instant vs trial» = S3 tour paywall, {free}, [iOS],
механизм = состав offer'а (instant vs trial default); «7745 Ambulance show reduction» =
S3 Ambulance, {free}, [Web], механизм = частота показа mid-funnel оффера;
«7778 web intro» = S6 intro access, {free}, [Web], механизм = тип доступа.

## 7. Неизвестные и спорные места (⚠️ к проверке с продуктом/аналитиком)

1. **Словарь `funnel_source` / paywall `value`** — полного справочника значений
   (источник пейволла ↔ поверхность) нет; для однозначной разметки нужен каталог.
2. **Актуальная последовательность remote tour** — живёт в бэкенд-конфиге
   (`u_guitarcom.tour`, per-experiment payload); RN `defaultTour` — фолбэк. Перед
   разметкой tour-экспериментов сверять с живым `app/tourBuilder`.
3. **Точные критерии `{ex-paid}`** (`formatRightsSegment()`): какие сервисы/давность
   истечения — в коде не верифицировано.
4. **Winback**: условия показа/частота/набор офферов WinbackResolver прочитаны только
   по событиям, не по полной логике.
5. **Splash scheduling** (sale/anniversary): capping и расписание — только события
   статусов (`Splash Status Received` и др.).
6. **OTP (книги/контент)**: правила отдельно не задокументированы (TODO в доке событий);
   `Charged` без `Subscribed` ломает наивные воронки.
7. **Huawei (`UGT_HUAWEI`)**: источник подписочных событий не найден в коде.
8. **CRM/push/email кампании** как вход в S1: события не каталогизированы.
9. **Web intro double-charge bug** (легаси `7_month_intro`, UMN-12477): дубль-charge
   ~2.7/день — мусор в intro-воронках до фикса.
10. **Entitlement**: общего события «доступ выдан» нет — «оплатил, но не получил доступ»
    в событиях воронки не видно, только через права/саппорт.
11. **Согласование**: короткая проверка flow с продуктом и аналитиком ещё не проведена —
    V0 собран по репозиторной документации (код-верифицированной), без интервью.
