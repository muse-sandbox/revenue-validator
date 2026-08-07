# FLOW-635 — Итоговые разделы 18 исходных страниц (дословно)

Источник: self-hosted Confluence `alice.mu.se`, вытянуто `scripts/cnfl pull <pageId>`
2026-08-07. Соответствие «кейс → pageId» взято из инвентаря FLOW-577 V0.1
(`flow-577-04-revenue-flow-2/output/flow577_revenue_inventory/inventory.yaml`),
ab_ids сверены с таблицей задачи FLOW-635 — расхождений нет.

**О дословности.** Цитаты приведены слово в слово из тела страницы. Исходный XHTML
конвертирован в текст (`analysis_scripts/20260807_flow635_xhtml_to_text.py`), поэтому
маркеры списков, курсив и вложенность потеряны — переносы строк внутри цитаты
соответствуют отдельным пунктам списка на странице. Опечатки источника сохранены
(«roll outed», «wiback», «varaitions», «Briantree»). Пропуски таблиц с цифрами
обозначены `[…таблица…]`. Цветной статус-макрос (Green/Red) приведён как
`[status: Red FAIL]`.

**Терминология страниц.** Итоговый раздел называется по-разному: `Decision` (верхний
уровень или внутри итерации), внутри него — подзаголовки `Results` / `Conclusion` /
`Next steps`; на части страниц вердикт лежит прямо в теле `# Results` без отдельного
заголовка `Decision`. Ниже для каждого кейса указано, как раздел называется на
конкретной странице.

---

## T1-01 — ab 4845 — killed

- Страница: **UG iOS: Interstitial – Swap into Landing**, pageId `459868984`
- URL: https://alice.mu.se/pages/viewpage.action?pageId=459868984
- Итоговый раздел: `# Results` (вводный абзац) + внутри-итерационные `Results` / `Conclusion` / `Next steps`. Отдельного заголовка `Decision` нет.

> The obvious thing about its results is simple: nothing changes at all. We didn't get any results with this experiment, there is simply nothing at all. Also we are not planning future iterations with interstitial, so we close experiment as fail. But also we can re-use this landing in future experiments with paywalls.

> \#4845 — [status: Red FAIL]
> Exposure event: Interstitial Banner View
> Results
> no changes since we affect only a very small portion of users
> 6% of users with access after interstitial are from its source
> Conclusion
> average accesses per day are so insignificant, there is no reason in rollout this variation
> Next steps
> we can work with first step of the interstial funnel
> for example show it for same users we show ad, but only once a week as an extra interstitial

---

## T1-02 — ab 6002 / 6128 / 6191 — killed

- Страница: pageId `682704865`
- URL: https://alice.mu.se/pages/viewpage.action?pageId=682704865
- Итоговый раздел: **страничный `# Decision`** (перед `# Results`) + `## Decision` внутри каждой итерации.

Страничный вердикт:

> \# Decision
> [status: Red FAIL]
> Even though ARPU is growing, we won't roll out the current solution yet. First, we'll test other alternatives to replace ads and try less generous offers. We want to avoid the novelty effect trap, where the audience quickly drops off. Instead, we'll implement a general solution first and then fine-tune it with offers if needed. Next project

Итерация 1 (#6128):

> \## Decision
> [status: Red FAIL]
> Results
> increased arpu for 24% iOS and 13% Android
> had problems with ex trials on ios: 21% of users tried to get 14d trials but got instantly charged instead
> iOS interstitials have 13% less conversion rate from trials than average
> Android -45%
> cannibalization
> iOS: 34% of earnings were cannibalized by reduced accesses from other sources
> Android: 63% of earnings were cannibalized by reduced accesses from other sources
> Conclusion
> can be roll outed, but will have an effect of tour update with most revenue on start
> Next steps
> fixed problem with ex subscriptions and relaunched

Итерация 2 — relaunch (#6191):

> \## Decision
> [status: Red FAIL]
> Results
> 7.5% increase in arpu for iOS (vs 24% in previous iteration)
> ~37% of interstitial revenue was from ex trial subscribers that is fixed now
> and 5% non significanlty on Android (vs 13% on previous iteration) considering almost no charges from ex subscribers
> but all matches if take into account all users with rights 4 and 5
> iOS – $0.021 arpu vs $0.018 in previous iteration
> Android – $0.020 arpu vs $0.018 in previous iteration
> Conclusion
> despite fixing only one part with ex subscribers we got 2-3 times worse results than in the previous iteration
> some users with rights = 4 or 5 were able to get valid trial without paying instantly and when we exclude them from the experiment we lost almost all of the revenue improvement
> Next steps
> We're not rolling out the solution yet; first, we're launching the next project

---

## T1-03 — ab 6335 — killed

- Страница: pageId `707134897`
- URL: https://alice.mu.se/pages/viewpage.action?pageId=707134897
- Итоговый раздел: `## Decision` (без цветного статуса и без явной формулы «do not roll out»).

> \## Decision
> Results
> We expected to achieve 10% growth in subscriptions through the new source, but ultimately the difference between variations was around 0.
> In the new scenario, conversion to subscription was only 0.07% of those who saw the new splash
> As a result, the share of subscriptions from the new source accounted for 3% of all subscriptions, but at the same time it cannibalized other sources from the tab page
> In the new scenario, 96% of users leave at the very first pre-paywall, indicating there are problems with paywall reach
> Conclusion
> Longer funnel with pre paywall screen works worse than just banner
> As a next step, we can make all pre-paywalls in the new scenario unskippable. This will solve the problem of high churn and low paywall visibility

---

## T1-04 — ab 6359 / 6416 / 6428 — rolled-out (Android)

- Страница: pageId `707139549`
- URL: https://alice.mu.se/pages/viewpage.action?pageId=707139549
- Итоговый раздел: `## Decision` внутри каждой из трёх итераций. **Итерация #6416 — раздел `Decision` пуст** (заголовки `Results` / `Conclusion` / `Next steps` без текста); это записано как пробел, а не пропуск.

Итерация 1 (#6359):

> \## Decision
> Results
> […перечень метрик по платформам и вариациям…]
> Conclusion
> Do not roll out globally. Variation 2 is a clear win on Android (ARPU +17%, access/charge CR up, engagement up) with neutral retention—recommend a staged Android-only rollout. On iOS, Variation 2 shows a significant ARPU drop in the "Without interstitial accesses" segment; hold iOS. Variation 3 should be rejected: it hurts Android retention and downstream monetization despite higher trial share and mixed engagement signals.
> Next steps
> P0: Ship Variation 2 to Android only behind a ramp (10%→50%→100%) with guardrails: ARPU ≥ +10%, charge CR ≥ +5%, 1/7/14d retention not worse than -0.5%. Monitor cancels/refunds for 14 days.
> P1: Deep-dive iOS (esp. "Without interstitial accesses"): segment by exposure (saw clip vs not), country, cohort (new vs lapsed), trial availability on paywall, and creative. Validate no tracking/eligibility bias due to admob_fail/offline. If issues found, iterate creatives or disable "Try for Free" overlay and re-test on a small iOS slice.
> P2: Pause Variation 3. If revisiting, test reduced frequency/shorter close-delay and alternative creatives (tabs vs chords) in a separate experiment; add latency/exposure diagnostics to ensure the clip trigger isn't degrading session quality.

Итерация 3 (#6428):

> \## Decision
> Results
> […перечень метрик…]
> Conclusion
> roll outed Android test variation
> Next steps
> Extend iOS test duration and compute total revenue impact: verify that ad/video interstitial revenue is fully captured in ARPU, compare eCPM and fill vs the standard interstitial, and re-check ARPU, cancels, and refunds with higher power.
> Cohort follow-up on purchasers: track 14d/1m cancellations and refunds by cohort post-exposure to ensure no delayed monetization or retention degradation before full rollout.

---

## T1-07 — ab 7160 / 7187 — killed

- Страница: pageId `773658792` (space CRO)
- URL: https://alice.mu.se/spaces/CRO/pages/773658792
- Итоговый раздел: блок `Decision` внутри `# Results` (заголовка `## Decision` нет).

> Decision
> [status: Red fail]
> variation #2 is best for roll out
> variation #3 on Android has better monetization (because trials have near 5% conversion rate) metrics but worsen retention
> but i do not recommend full roll out since for some reason variation #2 had 75-77% lower conversion from interstitial to banner which needs further investigation (or relaunch to test)
> Next steps
> It was decided not to roll it out because the revenue was too low.

Из раздела `## Insights` (пояснение к аномалии конверсии):

> variation #2 had a lower conversion to interaction with coupon due to ability to close the banner. as a result 75-77% lower conversion from interstitial to banner on average

---

## T1-08 — ab 7487 — rolled-out

- Страница: pageId `788612067` (space CRO)
- URL: https://alice.mu.se/spaces/CRO/pages/788612067
- Итоговый раздел: блок `Decision` внутри `# Results` + `### Next steps`.

> Decision
> [status: Green success]
> Can roll out variation 2 (the one-time $19.99 final interstitial) on both UGT_ANDROID and UGT_IOS, with active monitoring on iOS.
> no significant increase on arpu but only due to small segments
> Android — clear win, roll out. No cannibalization.
> iOS — roll out, but watch full-price cannibalization.
> Trade-off is by design. The offer converts trials into immediate payment, lowering AOV/ARPPU (iOS AOV −14.4%, p=0.001) — expected, since $19.99 < the ~$40/yr plan. It does not affect the standard winback CR (shown only after the winback window is exhausted).

> \### Next steps
> Roll out variation 2 on Android at 100% — clean incremental win.
> Roll out variation 2 on iOS, with a post-rollout watch on non-winback / full-price conversion (Total − Winbacks) to confirm the diffuse dilution stays bounded and the net stays positive.
> Iterate iOS targeting to cut the dilution — e.g. tighten eligibility so the $19.99 offer reaches only genuinely exhausted users (exclude those who recently viewed a full-price paywall or are mid-trial).
> Recheck churn 14d / refund 14d once the control 14d charge windows close (currently preliminary — pending-charge share > 5% on control branches) to confirm the cheaper product carries no late retention/refund penalty.

Из `## Insights → ### Summary` (то же решение с числами нетто):

> iOS shows dilution; Android is incremental but underpowered. iOS non-winback buyers fell 167 → 140 (−27) and non-winback revenue −$702, largely offsetting the +$998 winback revenue gain (net total → +$296). Android non-winback buyers grew 36 → 44 (+8), non-winback revenue +$221 (net total → +$395), consistent with no cannibalization — but the small sample leaves it short of significance.

> The project hypothesis ("any conversion is net-new, no cannibalization") holds on Android but not on iOS: on iOS some buyers shifted from full-price surfaces to the cheaper $19.99 deal. With matured control, neither platform's total-account ARPU lift reaches significance.

---

## T1-09 — ab 7454 — killed

- Страница: pageId `788613565` (space CRO)
- URL: https://alice.mu.se/spaces/CRO/pages/788613565
- Итоговый раздел: блок `Decision` внутри `# Results` + `## Next steps`.

> Decision
> [status: Red Fail]
> do not roll out iteration #1 as-is. The result is neutral / inconclusive (no significant lift), so iterate before any further investment.
> No metric is statistically significant (all p ≥ 0.32); underpowered on the goal metric despite ~80k members/arm — interstitial-attributed conversions are only ~70–165 per arm.
> Net conversion is flat: combined per family ≈ control (free 0.155% vs 0.153%; winback 1.59% vs 1.66%).
> At impression #1 (~50–60% of all interstitial conversions) the personalized splash converts same-or-worse (free −6%, winback −25%): it wins curiosity but loses intent — paywall→click roughly halves (7.25% → 3.90%).
> The one apparent win (winback paywall +4.6×) was an attribution artifact, not real engagement.
> No guardrail benefit either; ARPU / churn / refund moves are all within noise.

> \## Next steps
> Align the paywall to the personalized hook — change the paywall / offer, not just the interstitial copy. The biggest leak is paywall→click; an unchanged generic paywall likely creates an expectation mismatch after the personalized promise.
> Extend the personalization dose beyond the first impression (it currently reverts to generic after #1, where ~half of conversions live) — test personalized framing on repeat / high-intent impressions.
> The next iteration should test offer-level personalization.
> […]
> The main direction is to personalize the offer, not only the message around the offer.

Из `## Insights`:

> This experiment also suggests that personalization is more likely to work when it changes the offer itself, not only the wrapper around the offer. Previous examples like winback interstitials and discount offers for young users are better examples of meaningful personalization, because the offer matches the user segment.

---

## T1-10 — ab 7712 — inconclusive-stopped

- Страница: pageId `811868738` (space CRO)
- URL: https://alice.mu.se/spaces/CRO/pages/811868738
- Итоговый раздел: `## Decision` + `### Next steps`.

> \## Decision
> Do not roll out this iteration on either platform. Keep the concept alive for iOS. Final call is the DRI's.
> iOS — hold and re-run, do not discard. On the 14Free interstitial the instant offer lifted net revenue by roughly +58% at flat subscription volume, and that comparison is trial-free and fully charged on both sides, so it is a final read rather than a preliminary one. It is still not significant (p=0.22 on surface ARPU) because the run delivered 9 of the 15 designed days.
> Android — no case for the $29.99 step. The higher effective first payment was almost exactly cancelled by a conversion loss, leaving surface revenue slightly negative. This is price elasticity, not execution: same offer, same creative, same triggers as iOS.
> Winback interstitial — undecided, not a negative result. Its control branch is entirely trial-based and most of those trials have not reached their charge date, so control revenue on that surface is still incomplete and the comparison understates it.
> The headline Forecast understates the change and should not drive the call. The projected rollout effect is about −$215/day on iOS and −$110/day on Android, but it is built on Total ARPU, which averages the treated interstitials (12% of iOS and 17% of Android cohort revenue) together with the untouched surfaces that supply the rest and drifted independently.
> Nothing can be concluded about subscriber quality yet. Pending 14d charges sit far above the 5% gate in every branch, so churn and refund movements — including the large nominal Android churn number — are not interpretable at this snapshot.

> \### Next steps
> Re-run on iOS with the interstitial surface as the primary metric. The design's own baseline was the surface ARPU, but the experiment was judged on all-surface Total ARPU — a base roughly 8× wider than the change, which cannot resolve it at any realistic sample.
> Run the re-test to the designed exposure. This iteration stopped at 9 of 15 designed days on iOS and under half the designed Android sample, and shipped 2 of the 3 planned variations.
> Revisit the Winback surface after 2026-08-04, once the control trials' charge window has closed, and re-read charge quality (churn and refund 14d) at the same time.
> On Android, test a smaller price step before repeating $29.99. The conversion loss, not the ticket size, is the binding constraint there.
> Do not reuse Total ARPU as the goal metric for surface-scoped paywall tests. Size and judge them on the segment that the treatment actually reaches.

---

## T2-01 — ab 6293 — killed

- Страница: pageId `699819052`
- URL: https://alice.mu.se/pages/viewpage.action?pageId=699819052
- Итоговый раздел: блок `Decision` внутри `# Results`.

> Decision
> [status: Red FAIL]
> Results
> significant arpu decrease by 12% iOS and 26% Android in variation #3 (without all splashes)
> non significant arpu decrease by 1.2% iOS and 6% Android in variation #2
> didn't increase any product metrics
> Conclusion
> variation #2 arpu changes within expected 3% range. Android is 2 times larger
> We're not rolling out the experiment

---

## T2-02 — ab 6701 — rolled-out

- Страница: pageId `731485619`
- URL: https://alice.mu.se/pages/viewpage.action?pageId=731485619
- Итоговый раздел: блок `Decision` после `# Execution` (до `## Results`) + `## Next steps` в конце страницы.

> Decision
> [status: Red FAIL]
> Based on early results and increasing conversion in the sales funnel, we rolled out the experimental group to everyone (period - )
> However, the final results showed that due to cannibalization of other sources by the sale source, we ended up with less revenue despite having more paying users. Ultimately, we cannot use this mechanic permanently. Potentially, this mechanic could work to boost major one-time sales events with organic traffic growth (Black Friday, New Year, Christmas)
> Also, mechanics with emotional design can be tested and integrated into our regular scenarios to increase conversion

> \## Next steps
> Try the offer with a higher price for variations with emotional design. Adjusting plan pricing can help find the "sweet spot" where higher conversion rate to Access and lower ARPU don't compromise overall revenue. We'll test it for XMAS sale
> Use emotional design to enhance common sales flows: paywalls, tours, etc. Increased conversion on sale sources builds confidence that impact can be achieved without a price factor.

Из `## Results` (обоснование «нет значимых различий»):

> Overall, there are no statistically significant differences between the main monetization and retention metrics.
> […] CR to Access is higher in the test group (+6.8% on iOS and +3.3% on Android),
> However, ARPU in this group is slightly lower — by approximately -2% on both platforms. It can be explained:
> By cannibalization;
> By lower CR from Access to Charge.

---

## T2-05 — ab 6404 / 6614 / 6863 — rolled-out

- Страница: pageId `707149083`
- URL: https://alice.mu.se/pages/viewpage.action?pageId=707149083
- Итоговый раздел: `Decision` внутри каждой из трёх итераций (порядок на странице обратный: #6863, #6614, #6404).

Итерация 1 (#6404) — раскатанная:

> Decision
> [status: Green SUCCESS]
> Results
> […перечень метрик: ARPU +49.3%, Access CR +50.9%, Charge CR +67.3%, AOV −11.4%, ARPPU −10.8%, Trial share −30.1%, 7d/14d retention +2.0%/+1.4% …]
> Conclusion
> Strong, targeted winback impact on iOS canceled subscribers: very large lifts in ARPU/LTV are driven by substantially higher access and charge conversion from the winback splash/banner, with small but significant gains in engagement and R7–R14 retention. The trade-off is expected: discounts reduce AOV/ARPPU and shift users from trials to immediate repurchase (trial share down). The "Without winback accesses" segment shows no significant changes, supporting causality from the treatment. Recommendation: roll out the iOS winback to the eligible canceled-subscriber cohort, while monitoring cancellations/refunds and optimizing discount/copy to recover some per‑payer value without losing the conversion volume.
> Next steps
> roll out test variation #2
> test smaller discounts
> add analytics event then user with canceled subscription enters the app
> fix analytics for splash and benefits funnel

> Summary
> Retention "as a return on payment" has been confirmed: access and conversion to payment have grown significantly, ARPU/Revenue has grown, R7–R14 — a small but significant plus.
> The data shows an increase in instant purchases and a decrease in the share of trials, i.e., the switch to direct purchases has occurred, but with a lower average check.
> The value of the mechanism lies in the volume of returns through discounted repurchases.
> Insights
> The strength of the offer is decisive: a large discount and an exact SKU match result in conversion; a "6-month trial" (previously) was not motivating, but a direct discount is.
> The "immediately after cancellation" timing works: increased access to the offer and the checkout chain confirms the hypothesis of instant contact.
> Winback increases ARPU and total revenue due to the volume of conversions, but reduces AOV/ARPPU — here you need to play with the size of the discount.

Итерация 2 (#6614):

> Decision
> [status: Green SUCCESS]
> Results
> iOS wiback subscriptions were tracked as upgrades
> thus real profit from the current restart splashes is ~10 times lower than expected
> with all this more expensive comeback offers work much better and increase ARPU from that source by 370%
> current Android mode works without level changing. so they just purchase a new subscription
> expensive plans decrease ARPU by 55%
> Conclusion
> should roll out expensive test variation in iOS and keep cheap control on Android
> do not change android config for those cases on level change format
> most probably we wont be able to observe increase in true iOS revenue cause those kind of refund are not displayed in any api data
> they are presented only in total financial report

Итерация 3 (#6863):

> \## Decision
> Results
> [UGT_IOS / Total & Without winback accesses / variation 2] trial share, %: +76.2%–105.3%, higher trial adoption
> Conclusion
> do not roll out
> got 30% less conversion in test variation
> had problem with tracking subscription events in test variation
> Next steps
> fix subscribe / charge events in test varaitions

---

## T2-06 — ab 6515 — rolled-out

- Страница: pageId `714438038`
- URL: https://alice.mu.se/pages/viewpage.action?pageId=714438038
- Итоговый раздел: `## Decision`.

> \## Decision
> Results
> [UGT_IOS / Total / variation 2] ARPU: +3914.1% (growth); access cr, %: +3000+% (growth); charge cr, %: +3000+% (growth)
> [UGT_IOS / Active Trials (for bug test) / variation 2] ARPU: +600% (growth); AOV & ARPPU: +100% (growth)
> [UGT_ANDROID / Total / variation 2] ARPU: +1000% (growth); access cr, %: +800% (growth); charge cr, %: +1300% (growth); subscription -> charge, %: +60% (growth)
> [UGT_ANDROID / Active Trials (for bug test) / variation 2] ARPU: +800% (growth); access cr, %: +200% (growth); charge cr, %: +800% (growth); subscription -> charge, %: +300% (growth)
> Conclusion
> The personalized Anniversary splash (given higher priority over Sale Offer) drove very large monetization lifts across iOS and Android without measurable impact on retention or tab-view engagement.
> This suggests the higher-priority splash successfully converted eligible Pro subscribers.
> However, the Active Trials cohort (which should be excluded per design) shows significant exposure effects
> This points to a targeting/eligibility bug (Anniversary gift funnel launches right after trial)
> but overall it had no affect on monetization
> only 6 subscriptions from iOS and 26 on Android
> Recommendation: roll out with fix: remove users with trials from anniversary funnel
> Next steps
> fix bug with trials: because anniversary calculates through expiration date which is in 7-14 days for trials

Из `## Post-rollout analysis`:

> Anniversary splash revenue + ARPU, $ — current revenue per day iOS: $1100, Android: $300; current ARPU iOS: $1.2, Android: $1.05

---

## T2-07 — ab 6806 — killed

- Страница: pageId `739174418`
- URL: https://alice.mu.se/pages/viewpage.action?pageId=739174418
- Итоговый раздел: блок `Decision` внутри второй итерации (первый блок `Decision` итерации «beginners only» оборван на строке метрик — фиксируется как пробел страницы).

> Decision
> [status: Red FAIL]
> Results
> [UGT_IOS / Total / variation 2] access cr, %: -36.04%, decreased top-of-funnel conversion; charge cr, %: -26.38%, fewer users reach charge; AOV & ARPPU: +14% to +18%, increased spend among payers; tab view per user: -5.84%, decreased usage
> [UGT_ANDROID / Total / variation 2] access cr, %: -28.47%, decreased top-of-funnel conversion; subscriber -> buyer % and subscription -> charge %: +42%–43%, improved downstream conversion among payers; tab view 60s, %: +4.29%, more users pass 60s viewing threshold
> Conclusion
> Do not roll out.
> The 10-second post-action paywall for free users (and strict Official Tab gating) significantly suppresses access conversion on both iOS (-36%) and Android (-28%).
> On iOS this also translates into a lower charge conversion (-26%).
> Engagement signals are mixed (Android +4% in 60s view rate vs. iOS -6% tab views per user), consistent with added friction shortly after feature use and blocked navigation on the Official Tab.
> funnel losses
> conversion to banner: -10% iOS and -18% Android
> conversion from banner click → purchase: -22% iOS and -26% Android
> Next steps
> [пусто]

---

## T3-01 — ab 6026 / 6260 — killed

- Страница: pageId `682712790`
- URL: https://alice.mu.se/pages/viewpage.action?pageId=682712790
- Итоговый раздел: `## Decision` в каждой из двух итераций.

Итерация 1 (#6026):

> \## Decision
> Results
> the only good pattern is 2024 flagship iphones: the higher price → the higher arpu (except for the last one)
> on android segment with 512Gb storage can be evaluated since it has increase in arpu even for most expensive product
> Conclusion
> can rollout variation#5 on iOS in two weeks if churn rate will be fine
> Next steps
> make instant offers also depending on prices
> fix upgrade analytics problem before the next iteration
> calculate full 14d churn to get accurate churn level for new prices
> can run second iteration
> with high prices for iOS flagship 2024
> with high prices for Android with 512Gb of storage

Итерация 2 (#6260) — решающая:

> \## Decision
> Results
> has no significant changes in arpu
> no changes by segment
> Conclusion
> increased arppu in tour by 7%, decreased conversion in charge by 11% which result in no total changes in arpu (bot tour and overall)
> shouldn't rollout test variation
> probably price increase is too high to make the difference
> Next steps
> [пусто]

---

## T3-02 — ab 7268 — rolled-out

- Страница: pageId `777835742`
- URL: https://alice.mu.se/pages/viewpage.action?pageId=777835742
- Итоговый раздел: блок `Decision` внутри `# Results` + `#### Next step`.

> Decision
> [status: Green Success]
> Revenue up 3.2% immediately and up to 6.74% over a 3-year horizon due to the cumulative effect of retention
> The main drivers were Instant plans (+130–160%) and upsells (bundles +38%, courses/books +27%); these offset the negative impact of monthly and trial subscriptions
> Engagement metrics confirm that the product is actually being consumed by a new audience
> Comeback offer -20% and conversion to charge at exchange rates/book rates -20%
> perhaps some additional optimization is needed here.
> We consider the experiment a success

> \#### Next step
> Rolling out lower prices, but we are also implementing a monitoring system to track whether the price reduction is being offset by the anticipated growth and whether the actual trends align with the forecast model

Из `## Post-Rollout Analysis`:

> AOV declined by -44%, closely matching the experiment result (-44.6%) — the price effect reproduced almost exactly.
> Charges grew by +77.5%, notably below the growth observed in the experiment (+88.9%). This gap is the main reason full-rollout revenue came in essentially flat (-0.45%), whereas the experiment showed a revenue increase driven by stronger growth in accesses.

> This comes in below what the experiment led us to expect: the two-year per-cohort uplift is only +1.5%, against +77.5% growth in charges and +83.7% growth in surviving (net-of-cancel) charges. In other words, subscription volume roughly doubled, but the resulting revenue uplift is comparatively modest — a reminder that the per-subscriber value of the cheaper cohort is meaningfully lower, so raw volume growth doesn't translate one-to-one into revenue growth.

> Bottom line
> The drop in cancel rate is a positive leading indicator for retention, and the two-year cohort projection confirms the direction is positive rather than negative — full-rollout revenue is not at risk. However, the magnitude of the upside is modest (+1.5% over two years) and smaller than the experiment implied, given how much cheaper the AOV is relative to the volume gained. At this stage, the retention improvement should be treated as a real but limited offset, not a guarantee that revenue growth will meaningfully outpace the price cut over time.

---

## T3-03 — ab 7502 — killed

- Страница: pageId `785056492`
- URL: https://alice.mu.se/pages/viewpage.action?pageId=785056492
- Итоговый раздел: `## Decision` + `### Next steps`.

> \## Decision
> Do not roll out.
> Var C (6-month plan) shows statistically significant harm: subscribers −11.1% (p=0.028), buyers −11.9% (p=0.038).
> Var B (3-month plan) shows consistent negative trends across ARPU (−7.1%), CR to buyers (−9.0%), and revenue ($26,472 vs $28,987 control) without reaching significance but with no compensating upside.
> The positive trial mechanics signal (+22–26% trial share, +22–26% trial→charge) does not offset the loss of instant annual subscription revenue — the two plans acted as substitutes, not additions.

> \### Next steps
> Re-check churn and refund metrics in ~2 weeks once the 14d charge window matures (currently Pending 14d Charges: Var B 24.0%, Var C 15.7% — preliminary).
> Investigate the anchor effect: test whether keeping the instant annual plan alongside the 3-month trial plan avoids the substitution effect and recovers conversion.
> Review Instant Accesses drop (627 → 470 → 282) as a signal that the annual instant plan is a key conversion driver on web — consider protecting it in future paywall iterations.

---

## T3-05 — ab 6464 / 6482 / 6743 / 6860 / 6875 / 7091 / 7178 — rolled-out (итерация intro, 6875)

- Страница: pageId `714421628`
- URL: https://alice.mu.se/pages/viewpage.action?pageId=714421628
- Итоговый раздел: `## Decision` в каждой из семи итераций.

Итерация 1 (#6464):

> \## Decision
> Results
> [UG_WEB / Total / Variation 2] trial -> charge and trial subscriber -> charge: +25.03% to +29.78%, higher conversion from trial to paid
> [UG_WEB / Print sources only / Variation 2] AOV and ARPPU: -32.19%, lower order and payer value among print-sourced users
> Conclusion
> [status: Red FAIL]
> Do not roll out
> The paywall change (also applied to the print funnel per experiment design) significantly improved trial-to-charge conversion overall, but in the print-sourced segment it materially reduced AOV/ARPPU (~-32%)
> which risks offsetting conversion gains and harming revenue.
> ARPU shows positive trends in Total but are not statistically significant yet.
> Since other funnel steps were unchanged, the mixed outcome likely comes from how the new paywall nudges plan selection on print traffic (e.g., stronger emphasis on cheaper plans or discounts).
> Next steps
> run experiment with new paywall on all platforms

Итерация 2 (#6482):

> \## Decision
> Results
> [UG_WEB / Total / Variation #2] charge cancellations (14d and 1m), %: +25.5% to +37.4%, increase in early and 1-month churn after charge
> Conclusion
> [status: Red FAIL]
> Do not roll out
> While other monetization, retention, and engagement metrics show no statistically significant movement, both 14‑day and 1‑month post‑charge cancellations increased significantly.
> Given the change was limited to the paywall in the print funnel (logic from iteration 1 preserved, other steps unchanged), the likely cause is that the new paywall copy/design attracts more low‑intent purchases or misaligned expectations, leading to quick churn.
> Directionally, checkout purchase success looks higher in the daily funnel, but without significance and with higher early cancellations, the net ARPU impact is at risk.

Итерация 2 relaunch (#6743):

> \## Decision
> Results
> [UG_WEB / Total / variation 2] trial share, %: +6.38%, more users opt into trials; charge -> 14d refund, %: +72.30%, refund rate spiked (worse); Tab View (60s–600s) metrics: −1.45% to −2.26%, engagement depth decreased
> [UG_WEB / Print sources only / variation 2] charge -> 14d refund, %: +208.46%, refunds skyrocketed (worse)
> Conclusion
> [status: Red FAIL]
> Do not roll out
> Even with slightly increase in gross revenue due to higher trials share (with higher price than instants) we lose it because of 70% increase of refunds
> refunds increased in almost all groups / segments
> the highest increase in refund rate (90% of all refunds increas) among pro trials + edu/courses upsell
> but among all reasons i managed to parse from intercom there is no difference between variations
> it is possible that upsell checkout become indistinguishable from the previous pro checkout so more user purchase bundles in misunderstood

Итерация 3 (#6860):

> \## Decision
> Conclusion
> [status: Green SUCCESS]
> No statistically significant effects were detected on UG_WEB across monetization (Total, Print sources), retention, or tab-view metrics for the variant that shows three plans at once.
> Directionally, the Landing funnel suggests more plan browsing but fewer progressions to checkout, yielding a slightly lower overall purchase success rate (variation ≈3.89% vs control ≈4.07%).
> This pattern is consistent with potential choice overload from exposing all three plans upfront. Given the absence of statistically significant lifts and a possible small deterioration in the purchase funnel, do not roll out the current design globally. Iterate the plan presentation and re-test
> Rolling out a test branch
> Next steps
> [P1] Iterate the "three plans at once" UI to reduce choice overload: highlight a single recommended/default plan, simplify comparisons/copy, add a sticky CTA, and consider testing 2 plans vs 3. Rerun an A/B with this refined design.
> [P1] Run a power analysis and extend sample size/duration until primary metrics (access CR, charge CR, ARPU, members→purchase success) have ≥80% power to detect ~3–5% relative changes. Pre-register metrics and decision thresholds (p<0.05).
> [P2] Funnel deep-dive: […]

*(Примечание: цветной статус этой итерации — Green SUCCESS, тогда как текст говорит «do not roll out the current design globally» и «Rolling out a test branch». Противоречие статуса и текста фиксируется как есть.)*

Итерация 4 (#6875) — **раскатанная**:

> \## Decision
> Results
> [UG_WEB / Total / variation 2] arpu: +12.1%; trial -> charge: +32.0%; subscription -> charge: +8.6%; charge -> 14d cancel: -19.2%; Tab View (60s–180s): -1.3% to -1.6%
> [UG_WEB / Total / variation 3] arpu: +19.2%; charge cr: +15.1%; trial -> charge: +28.9%; charge -> 14d cancel: -20.0%; Tab View (60s–300s): -1.1% to -1.4%; retention 1d: -4.8%; retention 7d: -2.5%; retention 14d: -2.1%
> [UG_WEB / Print sources only / variation 2] arpu: +25.6%; trial -> charge: +36.7%
> [UG_WEB / Print sources only / variation 3] arpu: +33.8%; charge cr: +27.8%; charge -> 14d cancel: -35.1%
> Conclusion
> [status: Green Success]
> Both treatments tied to the instant introductory offer (64.99 → 99.99 on the second cycle), new checkout disclaimer, and new paywalls improved monetization.
> Variation 3 (C — three-level paywall) drives the largest gains: ARPU up ~19% overall
> 2% of offers were wrongfully misinterpreted by backend as week offers and charged after a week
> Recommendation: Roll out, but staged. Prefer C (three-level paywall)
> Next steps
> fix problems with into subscriptions
> View the number of debits per user
> relaunch with new prices

Итерация 5 (#7091):

> \## Decision
> Conclusion
> [status: Red FAIL]
> Do not roll out
> There is a 24% drop in ARPU
> 45% increase in trial → charge conversion hadn't helped since there were too few trials in test variation (and overall accesses)
> Next steps
> For the next iteration we made the same plans with different cta and focus on trial

Итерация 5.2 (#7178):

> \## Decision
> Conclusion
> [status: Red FAIL]
> do not roll out
> lost about 6% non significant in ARPU without increasing in subscribers
> Next steps
> can try to sell paid trial for unified bundle for cheaper price (less than $200) in order to increase upsell conversion
> or leave paid trial but keep bundle as a third option on the screen

---

## T3-06 — ab 6326 — rolled-out

- Страница: pageId `699819693`
- URL: https://alice.mu.se/pages/viewpage.action?pageId=699819693
- Итоговый раздел: `## Decision`.

> \## Decision
> Results
> [UGT_IOS / Total] charge cr, %: +16.4%-21.4% (more immediate charges due to trial-to-instant offer); AOV & ARPPU: -9.8%-13.2% (lower order value per payer after switching to the $24.99 discounted annual plan); trial -> charge, % and trial subscriber -> charge, %: -39.4%-39.8% (expected drop in trial-based conversions after removing trials on PRO paywalls); trial share, %: -15.0%-17.0% (fewer users start a trial); subscriber -> buyer, %: +11.9%-15.7% (higher conversion among subscribers); charge -> 14d cancel, % and charge -> 1m cancel, %: -42.2%-46.1% (substantially fewer early cancellations)
> [UGT_IOS / Instant Offer Only] access cr, %: +4.9% (more users enter the monetization funnel for PRO paywalls)
> Conclusion
> [status: Green Success]
> Confirmed the hypothesis + received additional subscriptions
> since the survival rate of such subscriptions is higher, we expect this cohort's revenue to grow in the second and subsequent billing cycles
> Charge conversion increases strongly and early cancellations drop by ~42%-46%, while engagement and retention remain unchanged
> The trade-off is a meaningful reduction in ARPPU (~10%-13%), consistent with the $24.99 discounted, immediate-charge plan. ARPU are not significantly changed in this read
> Roll out to iOS Pro paywalls as tested
> but stage the rollout and closely monitor net revenue and renewal behavior
> the price cut seems to be offset by higher conversion and lower churn, but we should ensure long-term economics remain positive
> Ensure that
> P1 — Quantify net revenue and LTV impact: cohort 7/14/30/60/90-day net revenue (refund- and cancel-adjusted), payer volume vs price drop, and NPV vs control; model 12‑month renewal for the upgraded annual plan.
> P2 — Segment deep-dive: compare effects by PRO paywall type (Official tab, Spotify, Autoscroll, Settings Pro, etc.), new vs returning users, and geo/source; prioritize rollout to strongest segments and hold out weak ones.
> P3 — Price/messaging follow-up test: experiment with less aggressive discounts (e.g., $29.99 or smaller % off) and/or streamlined instant-offer screens to recover AOV/ARPPU while maintaining the conversion and low-cancel benefits.

---

## Пробелы и аномалии, зафиксированные явно

| Кейс | Что не найдено / что не так |
| -- | -- |
| T1-04 | У итерации #6416 раздел `Decision` присутствует, но **пуст**: заголовки `Results` / `Conclusion` / `Next steps` без текста. |
| T2-07 | В первой итерации («beginners only», #6806) блок `Decision` обрывается на одной строке метрик — вердикта нет. Решение сформулировано только во второй итерации на той же странице. |
| T1-03 | В `Conclusion` нет формулы решения («do not roll out» / «roll out»); есть только вывод о механике и следующий шаг. Статус-макроса нет. Вердикт `killed` восстанавливается по смыслу, а не по букве. |
| T3-01 | В обеих итерациях `Next steps` итерации 2 пуст; фактическая раскатка варианта из итерации 1 страницей не подтверждена (Post-rollout пуст). |
| T2-07, T3-01 | `Next steps` пуст. |
| T3-05 #6860 | Цветной статус `Green SUCCESS` противоречит тексту `do not roll out the current design globally`. |
| T2-02 | Страничный статус `Red FAIL` стоит на кейсе, который **был раскатан** (раскатка по ранним данным, финальный вердикт — отрицательный). |
| Все 18 | Ни на одной странице не указан владелец решения (кто принял) и мандат; ни на одной нет упоминания стоимости слота или альтернатив, конкурирующих за тот же слот. |
