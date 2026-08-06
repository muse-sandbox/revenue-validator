# Safe Inventory — Interstitials Experiment Family (FLOW-568)

Собрано: 2026-08-04. Источники: Confluence (alice.mu.se, CQL-поиск `interstitial` / `интерстишл` / `интерстициал` / `межстраничн` по всем спейсам), локальное зеркало базы гипотез (`context/hypotheses/`), реестр экспериментов `mysql_u_guitarcom.ab_experiment` (только metadata-поля: id, name, даты, статус, activation event — поля результата/rollout не читались).

**Outcome-blind:** в этом файле нет величин результатов. Колонка «Outcome есть» — только бинарный факт наличия заполненных секций Results/Decision на странице.

## Определение семейства

По канонической странице [DOCS] «Монетизационные слои UG — Local interstitials» (pageId 777830942): **local interstitial — внутренний экран-предложение UG App, показываемый вместо рекламной паузы в табах** (сценарии AD 14Free / MONETIZATION_VIDEO / AD Winback и их наследники). В корпус входят завершённые A/B-эксперименты UG App, где treatment — содержимое/механика этого монетизационного интерстишл-слоя (в реестре — префикс `[UG Monetization]`).

Не входят (перечислены ниже для полноты, с причинами): рекламные ad-ops эксперименты `[AD]` (частота/тайминг/SDK показа рекламных интерстишлов), web/mobweb-интерстишлы, эксперименты приложений MuseScore/MU, инфраструктурные релизы и research-документы без A/B.

## A. Пригодные кандидаты семейства (in-family, завершённые)

| # | Confluence pageId | Название (и алиасы) | AB experiment IDs | Запуск (стр.) | Завершение | Поверхность | Механика | Сегмент | Итерация/связь | Pre-launch есть | Outcome есть |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [459868984](https://alice.mu.se/pages/viewpage.action?pageId=459868984) | UG iOS: Interstitial – Swap into Landing; алиас: «Swap HL ads into Landing»; реестр: «[UG Монетизация] UG iOS: Interstitial – Swap into Landing» | 4845 | 2024-04-24 | 2024-08-10 | iOS interstitial slot | Замена рекламы на переход в продажный Landing; trigger: Interstitial Banner View | iOS | самостоятельный | да | да |
| 2 | [682704865](https://alice.mu.se/pages/viewpage.action?pageId=682704865) | UG App: paywall – offer instead of ad interstitials; алиас в реестре: «UG App: changing banners and interstitials» (+ «2 iteration», «relaunch») | 6002, 6128, 6191 | 2025-04-11 | 2025-07-10 | iOS+Android interstitial slot | Offer-экран вместо рекламного интерстишла | Free, iOS/Android | итерации 1–2 в одной странице; продолжение → стр. 714432870 | да | да |
| 3 | [707134897](https://alice.mu.se/pages/viewpage.action?pageId=707134897) | UG iOS: paywall – paywall after ad interstitial | 6335 | 2025-07-07 | 2025-08-12 | iOS interstitial slot | Pre-paywall→paywall после рекламного интерстишла; activation: admob_shown | iOS | самостоятельный | да | да |
| 4 | [707139549](https://alice.mu.se/pages/viewpage.action?pageId=707139549) | UG App: paywall – monetization video instead of ad interstitials | 6359, 6416, 6428 | 2025-07-09 | 2025-08-11 (реестр, 6428) | iOS+Android interstitial slot | Монетизационное видео вместо рекламного интерстишла; activation: admob_fail/admob_request | Free, iOS/Android | итерации 1–2 в одной странице | да | да |
| 5 | [714409638](https://alice.mu.se/pages/viewpage.action?pageId=714409638) | UG App: winback – add interstitials for former subscribers; реестр: «winback interstitials for former subscribers» (+ relaunch) | 6461, 6644 | 2025-08-01 | 2025-10-17 | iOS+Android interstitial slot | Winback-интерстишл для бывших подписчиков | Ex-paid, iOS/Android | самостоятельный; продолжение темы → стр. 788612067 | да | да |
| 6 | [714432870](https://alice.mu.se/pages/viewpage.action?pageId=714432870) | UG App: paywall – offer instead of ad interstitials (страница итераций 3+); реестр: + «relaunch», «close button relaunch», «2 iteration» | 6491, 6626, 6716, 6896 | 2025-08-20 | 2026-03-13 | iOS+Android interstitial slot | Offer-экран вместо рекламного интерстишла (доработки) | Free, iOS/Android | продолжение стр. 682704865 (отдельные даты/дизайн/результат) | да | да |
| 7 | [773658792](https://alice.mu.se/pages/viewpage.action?pageId=773658792) | UG App: paywall – pre-paywall with animation for interstitials; реестр: «Pre-paywall with animation for interstitials» (+ relaunch) | 7160, 7187 | 2026-03-09 | 2026-07-01 | iOS+Android interstitial slot | Анимированный pre-paywall в интерстишл-сценарии | Free, iOS/Android | самостоятельный | да | да |
| 8 | [788612067](https://alice.mu.se/pages/viewpage.action?pageId=788612067) | UG App: winback – final interstitial offer | 7487 | 2026-05-04 | 2026-07-30 | iOS+Android interstitial slot | «Последний шанс»-offer в winback-интерстишле | Ex-paid, iOS/Android | развитие темы стр. 714409638 (отдельный эксперимент) | да | да |
| 9 | [788613565](https://alice.mu.se/pages/viewpage.action?pageId=788613565) | UG App: personalized interstitial | 7454 | 2026-05-05 | 2026-06-18 | iOS+Android interstitial slot | Персонализация контента интерстишла | Free, iOS/Android | самостоятельный | да | да |
| 10 | [811868738](https://alice.mu.se/pages/viewpage.action?pageId=811868738) | UG App: interstitial – discounted prices; реестр: «interstitials – discounted prices» | 7712 | 2026-07-03 | 2026-07-21 (реестр; в заголовке страницы «XX» не обновлён) | iOS+Android interstitial slot | Скидочные цены в интерстишл-offer | Free (tour-install), iOS/Android | самостоятельный | да | да |

Единица корпуса — Confluence-страница проекта (все итерации внутри страницы — один кейс; связи между страницами-итерациями помечены явно и учтены в leakage-контроле).

## B. In-family, но непригодные

| pageId | Название | Причина непригодности |
|---|---|---|
| [199903134](https://alice.mu.se/pages/viewpage.action?pageId=199903134) | UG App: доступы вне тура, продажные слои – ad-free на интерстишале (2021-03-04) | Нет задокументированного итогового результата и решения (страница — только план; задачи «Подвести результаты» остались incomplete); нет ID эксперимента |
| [777823482](https://alice.mu.se/pages/viewpage.action?pageId=777823482) | UG App: Interstitials research (2026-03-26) | Research-документ, не A/B-эксперимент |
| [777830942](https://alice.mu.se/pages/viewpage.action?pageId=777830942) | [DOCS] Монетизационные слои UG – Local interstitials | Справочный документ семейства, не эксперимент |
| реестр 7514 | UG App: interstitials – store checks for ex-pro | Не запускался (status 0, дат нет) |
| реестр 6575 | [UG ADV] Interstitials from Applovin MAX | Не запускался (status 0), ad-инфраструктура |

## C. Вне семейства (найдены поиском, исключены из корпуса)

| pageId | Название | Причина исключения |
|---|---|---|
| [494817216](https://alice.mu.se/pages/viewpage.action?pageId=494817216) | UG App iOS: Interstitials for the cold segment (2024-07-04) | Ad-ops: снятие ограничений частоты показа рекламных интерстишлов (реестр 4947, 5022 «[AD] Показ … без ограничений … 60 дней»); treatment — реклама, не offer-слой |
| [459896146](https://alice.mu.se/pages/viewpage.action?pageId=459896146) | UG inAPP: Direct sales in interstitials (2024-06-04) | Прямые рекламные продажи в рекламном слоте (ad-sales), не монетизационный offer-слой |
| [714424280](https://alice.mu.se/pages/viewpage.action?pageId=714424280) | MU App: Interstitials for Direct Sales for free users (2025-08-13) | Другой продукт (MU App); итоговых результатов на странице нет |
| [234401552](https://alice.mu.se/pages/viewpage.action?pageId=234401552) | InApp Добавление Rewarded interstitial (2021-12) | Ad-формат (rewarded), релиз/ad-ops; результатов на странице нет (реестр 2015 — даты расходятся со страницей, помечено как неточное сопоставление) |
| [248477679](https://alice.mu.se/pages/viewpage.action?pageId=248477679) | InApp. Улучшение кодовой базы вызова interstitial (2022-03-07) | Инфраструктурный релиз, не продуктовый эксперимент (возможное соответствие реестру 1591 — неточно) |
| [269950853](https://alice.mu.se/pages/viewpage.action?pageId=269950853) | UG iOS Interstitials' timeout reduction 180s→120s (2022-08-22) | Ad-ops: частота показа рекламы (реестр 2114) |
| [282975913](https://alice.mu.se/pages/viewpage.action?pageId=282975913) | InApp. Сокращение интервала и ограничений на показ Interstitial (2022-12-12) | Ad-ops: частота показа рекламы |
| [289046252](https://alice.mu.se/pages/viewpage.action?pageId=289046252) | InApp. Запуск интерстишл до показа табовой (2023-02-23) | Ad-ops: тайминг показа рекламы (реестр 2570) |
| [296463457](https://alice.mu.se/pages/viewpage.action?pageId=296463457) | UG InApp. HyprMX adapter on Interstitials (2023-03-15) | Ad-SDK/адаптер |
| [721555309](https://alice.mu.se/pages/viewpage.action?pageId=721555309) | UG InApp. Applovin MAX Platform for Interstitials (2026-03-31) | Ad-платформа, эксперимент не завершён |
| [226468110](https://alice.mu.se/pages/viewpage.action?pageId=226468110) | InApp. Крестик на интерстишлы MuseScore (2021-09-21) | Другой продукт (MuseScore), релиз |
| [39424263](https://alice.mu.se/pages/viewpage.action?pageId=39424263) | Interstitials SUCK (2015-10-29) | Web-интерстишлы (другая поверхность/эпоха) |
| [234402316](https://alice.mu.se/pages/viewpage.action?pageId=234402316) | АБ тест web-interstitials от Google (2021-12-03) | Web |
| [257559898](https://alice.mu.se/pages/viewpage.action?pageId=257559898) | Programmatic Web. Web Interstitials (2022-05-24) | Web |
| [282984187](https://alice.mu.se/pages/viewpage.action?pageId=282984187) | Web-Interstitials on Mini Sites (2022-12-27) | Web |
| [276352858](https://alice.mu.se/pages/viewpage.action?pageId=276352858) | UG Mobweb Android: Replace "ListSplash" with Web-Interstitials (2022-10-27) | MobWeb |
| [323822036](https://alice.mu.se/pages/viewpage.action?pageId=323822036) | UG App: Research on displaying special interstitials (2023-09-19) | Research, не эксперимент |
| [340762035](https://alice.mu.se/pages/viewpage.action?pageId=340762035) | Research of iOS Interstitials flow on a device (2023-12-20) | Research/QA, не эксперимент |
| реестр 4144, 4374 | [AD] Показ интерстишелов на TextTabContainer / по диплинку | Ad-ops (отдельные Confluence-страницы поиском не найдены) |

## Дедупликация

- «UG App: changing banners and interstitials» (реестр 6002/6128/6191) = проект «offer instead of ad interstitials» (стр. 682704865) — один кейс, не отдельный эксперимент.
- Relaunch-записи реестра (6416, 6644, 6626→6491, 6716, 7160→7187) — перезапуски тех же итераций, не отдельные эксперименты.
- Копий одного запуска под разными страницами не обнаружено. Пары «страниц-продолжений» (682704865 → 714432870; 714409638 → 788612067) — разные итерации с отдельными датами, дизайном и результатом → считаются разными экспериментами, связь помечена.
