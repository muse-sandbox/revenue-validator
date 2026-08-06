# Interstitials KB V0 — Source Traceability

Версия: **V0 (frozen 2026-08-04)**. Каждое содержательное утверждение KB привязано к source card из `interstitials-corpus-prep/knowledge-sources/` (freeze корпуса 2026-08-04, SHA-256 карточек — из `BUNDLE_MANIFEST.md` корпуса).

## Source cards → эксперименты

| Card | Файл | Эксперименты (AB id) | Годы | Вердикт(ы) |
|---|---|---|---|---|
| KS-01 | `KS-01_swap-into-landing.md` | 4845 | 2024 | FAIL |
| KS-02 | `KS-02_offer-instead-of-ad-interstitials-iter1-2.md` | 6002, 6128, 6191 | 2025 | FAIL, FAIL |
| KS-03 | `KS-03_paywall-after-ad-interstitial.md` | 6335 | 2025 | FAIL |
| KS-04 | `KS-04_monetization-video-instead-of-ad-interstitials.md` | 6359, 6416, 6428 | 2025 | iter1 mixed / iter2 Android rollout |
| KS-05 | `KS-05_winback-interstitials-former-subscribers.md` | 6461, 6644 | 2025 | Green SUCCESS |
| KS-06 | `KS-06_offer-instead-of-ad-interstitials-iter3plus.md` | 6491, 6626, 6716, 6896 | 2025–2026 | iter1 Red FAIL / iter2 rollout |

SHA-256 карточек (из BUNDLE_MANIFEST.md корпуса):

```
f1fa855edba3ec6c53e671fa65a496d2a63f523d3cf518a2c712910dffec13c6  KS-01_swap-into-landing.md
6e2b15b9d019437affc8ba0da1dcb2670adfe52ae0d6eecc44c86b339c2efb69  KS-02_offer-instead-of-ad-interstitials-iter1-2.md
76f0e39eae6ff394863978529f1eb2c32553421a96b42bc832fa60a629e5f179  KS-03_paywall-after-ad-interstitial.md
217737c4a41074a0fbefa5876bef212cdd15b5d4994511392c2b41b5f8fdfc56  KS-04_monetization-video-instead-of-ad-interstitials.md
28f2fbfd53a2cb2b656703b848698d9975d4bcf3292c79b2ff9b4b8ea0826f73  KS-05_winback-interstitials-former-subscribers.md
c8131e75cfebc6e3db395efddac9e650efbbeb74f68ac3bf5bdcd41aac25b710  KS-06_offer-instead-of-ad-interstitials-iter3plus.md
```

## Паттерн → источники → ключевые факты

| Pattern | Source(s) | Ключевые опорные факты (раздел карточки) | Мульти-source? |
|---|---|---|---|
| IKB-P01 | KS-01 §Results, §Lessons; KS-04 §Context, §Execution; KS-05 §Results; KS-06 §Results | 4 access/6% (KS-01); reach 35k/85k users/day (KS-04); 99.74% splash reach (KS-05); 93.8–98.6% Splash View (KS-06) | да (4) |
| IKB-P02 | KS-02 §Results (34%/63%); KS-03 §Results (net-zero + cannibalization); KS-04 §Results (−24.7% p=0.039 iOS Without-interstitials); KS-05 §Results (−$47 vs +$1,014); KS-06 §Results (~30% гросс-выигрыша, ad rev −29% iOS / −$6…−$23 Android) | да (5) |
| IKB-P03 | KS-02 §Post-rollout (60–87% accesses с 1-го контакта); KS-06 §Results (1.58%→0.41% к 4-му показу) | да (2) |
| IKB-P04 | KS-02 §Post-rollout (ad-primed −28%/−14%); KS-03 §Results (96% отвал на 1-м pre-paywall, 0.07% purchase) | да (2) |
| IKB-P05 | KS-03 §Results, §Lessons («longer funnel … worse than just banner») | нет — `single-case` |
| IKB-P06 | KS-02 §Post-rollout (13×/3.6× CR); KS-05 §Results (+42.8% ARPU p=0.00); KS-06 §Results (exes ARPU +18.8% p=0.025) | да (3) |
| IKB-P07 | KS-02 §Results (−13%/−45% trial→charge; ex-trial 8%); KS-05 §Results (cancels +118%, 33.8% у источника); KS-06 §Results (trial→paid −36…−54%) | да (3) |
| IKB-P08 | KS-06 §Results iter1 vs iter2 (внутрилинейное сравнение); KS-02 §Results (trial-сторона) | да (2); intro-сторона `single-case` |
| IKB-P09 | KS-05 §Results (re-trial → ex); KS-06 §Results («works only on free users», exes −2.2% p=0.77) | да (2) |
| IKB-P10 | KS-02 §Execution, §Results, §Post-rollout (21% instant charge, ~37% выручки, 2–3× сжатие, ALL/27% повторных trial); KS-05 §Execution + KS-06 §Execution (unified_id bug) | правило — да; величины `single-case` |
| IKB-P11 | KS-04 §Execution (fail 28–48%), §Mechanics iter2 (preload-фикс); KS-05 §Context/§Results (push 50–72% vs 99.74%); KS-02 §Post-rollout (30% не видели интерстишел) | да (3) |
| IKB-P12 | KS-04 §Results iter1/iter2 (retention нейтрален → значимо вниз); KS-06 §Results iter1 (Android значимо вверх)/iter2 (flat) | да (2), противоречие |
| IKB-S01 | KS-04 §Results (v3 хуже v2), §Decision | нет — `single-case` |
| IKB-S02 | KS-02 §Post-rollout (CPM-сравнение по тирам) | нет — `single-case` |
| IKB-S03 | KS-05 §Context (приоры push-winback), §Results, §Lessons | нет — `single-case` (сопоставление) |

## Проверка правил построения

- Все 12 паттернов IKB-P01…P12, заявленные как мульти-source, имеют ≥2 независимые source cards (KS-02 и KS-06 — разные страницы/эксперименты одной линии; там, где это единственная пара, паттерн опирается на разные итерации/агрегаты, что отмечено в карточке).
- Одиночные выводы (IKB-P05, IKB-S01…S03, intro-сторона IKB-P08, величины IKB-P10) явно помечены `single-case evidence`.
- Утверждений без source-привязки в KB нет; чисел, отсутствующих в карточках KS, в KB нет.
- Причинность заявлена только внутри A/B-контрастов с приведённой значимостью; сравнения между экспериментами помечены как интерпретация/гипотеза переноса.
