# HX-01 — ground truth (doc-side)
Источник: 494820283 | [2024-06-09] UG App: tour – split the tour for learners and players [2024-10-16] | https://alice.mu.se/spaces/CRO/pages/494820283
Эксперимент(ы): #4917 (итерация 1), #5058 (итерация 2), #5097 (итерация 3, финальная)
Jira: UMN-6024

## Прогноз IR (повтор из pre-launch, для сверки plan/fact)
Модель: +10% к конверсии Tour→Access при неизменном ARPPU → iOS +$1714/день (Revenue $17136 → $18850), Android +$617/день ($6168 → $6785); суммарно ≈ +$2331/день. ARPU прогнозно +10% (iOS $1.169→$1.286; Android $0.413→$0.454).

## Факт: target metric и денежные метрики (значения A/B, uplift, p-value/CI — как в документе)

### Итерация 1 (#4917) — НЕГАТИВ
Results: «significantly lower conversion to access in tour for both platform». Conclusion: «most downgrade from "Play favorite songs" section».
- iOS (overall): ARPU $1.86 → $1.79 (-3.99%, p=0.29); access cr 9.46% → 9.18% (-2.99%, p=0.17); charge cr 4.20% → 3.97% (-5.28%, p=0.11); revenue $74420 → $72150.
- iOS (Tour only): access cr 6.09% → 5.72% (-5.94%, p=0.03); ARPU $1.43 → $1.38 (-3.45%, p=0.46); AOV +2.29% p=0.03; ARPPU +2.41% p=0.03.
- Android (overall): ARPU $0.71 → $0.64 (-9.26%, p=0.14); access cr 4.18% → 3.80% (-9.05%, p=0.01); charge cr -10.39% (p=0.061); revenue $24299 → $21898.
- Android (Tour only): access cr 2.54% → 2.22% (-12.78%, p=0.005); ARPU -10.27% (p=0.20).
- Forecast (per day): iOS -46 accesses, -33 charges, -$1145; Android -52 accesses, -23 charges, -$878.

### Итерация 2 (#5058) — НЕЙТРАЛ
Results: «no significant changes — neither in overall nor in general goal segments». Conclusion (как в документе, с опечаткой): «bettet than iteration #1 with 13% drop in Android access rate».
- iOS (overall): ARPU $1.64 → $1.67 (+2.16%, p=0.46); access cr 9.45% → 9.31% (-1.47%, p=0.38); revenue $109,614 → $112,434.
- iOS (Tour only): access cr 6.48% → 6.22% (-4.05%, p=0.05); ARPU 0.69% (p=0.85).
- Android (overall): ARPU $0.68 → $0.66 (-3.13%, p=0.57); access cr -0.69% (p=0.83); revenue $32,208 → $31,110.
- Android retention 7d: +2.48% (p=0.04) — единственный значимый плюс.
- Forecast (per day): iOS -17 accesses, +18 charges, +$498; Android -7 accesses, -6 charges, -$356.

### Итерация 3 (#5097, финальная) — НЕЙТРАЛ, признана успешной
Results: «no significant changes»; «cancellations after charge increased by 8% on iOS and decreased by 15% on Android».
- iOS (overall): ARPU $1.52 → $1.55 (+1.65%, p=0.51); access cr 8.82% → 9.05% (+2.58%, p=0.08); trial→charge -0.01% (p=1); charge→14d cancel 23.48% → 25.47% (+8.47%, p=0.047); revenue $142152 → $144392.
- iOS (Tour only): ARPU +0.48% (p=0.88); access cr +2.06% (p=0.27).
- Android (overall): ARPU $0.73 → $0.72 (-2.28%, p=0.56); access cr -3.54% (p=0.12); charge→14d cancel 19.31% → 16.29% (-15.63%, p=0.03); revenue $63202 → $61712.
- Android (Tour only): access cr -5.25% (p=0.069); ARPU -2.33% (p=0.66).
- Retention 1d/7d: без значимых изменений на обеих платформах.
- Forecast (per day): iOS +36 accesses, +11 charges, +$353; Android -22 accesses, +3 charges, -$280. Нетто ≈ +$73/день (vs план +$2331/день).

## Достигнутая выборка и длительность (vs дизайн)
Дизайн: iOS 58652 за 4 дня; Android 149280 за 10 дней (на все вариации).
Факт (по members двух арм): итерация 1 — iOS 80242, Android 68597; итерация 2 — iOS 134247, Android 94829; итерация 3 — iOS 186774, Android 172113. Дизайн-объёмы перекрыты во всех итерациях (iOS с запасом; Android в ит.1 ~46% плана, в ит.3 ~115%). Фактическая длительность в днях в документе не указана — missing.

## Денежные guardrails (факт)
Формальные guardrails не заявлялись. Фактически отслеживались: ARPU, AOV, ARPPU, charge cr, trial→charge, charge→14d cancel, retention 1d/7d. Ит.3: значимые движения только в charge→14d cancel (iOS +8.47% p=0.047 — хуже; Android -15.63% p=0.03 — лучше); остальное незначимо.

## Каннибализация / refunds / reconversion (факт)
Не измерялись / не упомянуты — missing. Ближайший прокси — charge→14d cancel (см. выше).

## Rollout/rollback по документу (решение, формулировка)
Итерация 3 помечена статусом success (green). Формулировка: «We didn't see any significant growth in metrics, but there was no decline either… we made the tour shorter, which slightly increased the passability in test variations… a shorter tour is less tiring for the user… (reducing negative reviews in stores). We consider the experiment successful, we are rolling out a test variation». Next steps: «Continue worsening ab-tests (taking into account the updated branding)». Итерации 1–2 — перезапуски с изменённым дизайном (ит.1 фактически негативная и была переделана).

## Post-rollout данные
missing (на странице нет post-rollout секции).

## Data issues / ограничения измерения
- «Forecast (per day)» — модельная экстраполяция, а не прямое измерение; знаки по платформам противоположны (iOS +, Android -).
- Целевые и денежные диффы финальной итерации незначимы; CI в документе не приведены (только p-value).
- Разнонаправленный значимый эффект на charge→14d cancel (iOS хуже, Android лучше) не объяснён.
- MDE в плане (0.0243 / 0.0144) не согласуется по шкале с базовой конверсией (0.058 / 0.021) — вероятно, относительная/иная единица; в документе не расшифровано.
- Заявленные качественные выгоды (passability, «меньше негативных отзывов») числом в документе не подтверждены (по passability есть только фаннел Tour Start→End: ит.3 iOS ~без изменений, Android +0.2–0.9 п.п. по сегментам).

## Черновая классификация по правилам FLOW-562
**no meaningful uplift** (по финальной итерации #5097 — основанию решения о rollout). Точечные оценки ARPU/revenue близки к нулю и разнонаправлены по платформам (iOS +1.65% p=0.51; Android -2.28% p=0.56), выборка большая (186k/172k members), target-метрика access cr тоже незначима. План +10% конверсии и +$2331/день не подтверждён; rollout сделан по качественным соображениям (короче тур при отсутствии деградации). Отмечу: итерация 1 (#4917) как самостоятельный тест — negative (значимое падение access cr на обеих платформах). p>0.05 здесь трактуется как «нет значимого эффекта» именно из-за большой выборки и малых точечных оценок, а не автоматически.

## Тип результата: CM / EE / OE / NM (по каждому денежному числу)
- Revenue/ARPU/AOV/ARPPU по армам в таблицах Monetization stats/metrics (все итерации) — **CM** (измерено в эксперименте; у финальной итерации эффект незначим).
- Диффы «Forecast (per day)»: -$1145/-$878 (ит.1), +$498/-$356 (ит.2), +$353/-$280 (ит.3) — **EE** (модельная экстраполяция на дневной трафик).
- Прогноз pre-launch модели (+$1714/+$617 в день) — **EE** (план, не факт).
- Выгода «меньше негативных отзывов / лучше UX» — **OE** (мнение автора, не измерено).
- Долгосрочные LTV / refunds / каннибализация / post-rollout revenue — **NM**.
