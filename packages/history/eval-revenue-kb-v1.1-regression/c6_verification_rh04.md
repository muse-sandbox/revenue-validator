# C6-верификация RH-04 (адверсариальная проверка флага судьи)

Верификатор: независимый адверсариальный проход, FLOW-586, слепая фаза (ground truth
и arm mapping НЕ вскрывались; `ground-truth-sealed/`, `arm_mapping_sealed.md`,
`split_manifest.*` и бандлы FLOW-579 не читались). Прецедент процедуры: FLOW-579,
верификация до вскрытия GT.

Прочитано: `revenue-corpus-prep-v1/EVALUATION_PROTOCOL.md`,
`revenue-corpus-prep-v1/holdout-blind/RH-04.md`,
`revenue-kb-v1.1-regression-run/blind-pairs/RH-04-Y.md` (+ `RH-04-X.md` для сравнения),
`revenue-kb-v1.1/knowledge_base.md`, `revenue-kb-v1.1/pattern_cards.md`,
`revenue-kb-v1.1/evidence_policy.md`, `revenue-kb-v1.1/evidence_policy_rules.yaml`,
`revenue-kb-v1.1-regression-evaluation/judges/RH-04_scorecard.md`.

---

## 1. Контекст флага

Судья (`judges/RH-04_scorecard.md`, строка C6_Y) зафиксировал у RH-04-Y **одно
пограничное** C6-нарушение:

> «Wrapper changes without offer changes have not lifted purchases in this corpus»
> (risk #1) — овергенерализация: T1-07 (который Y сам цитирует) дал значимый iOS var2
> ARPU +26.5% при wrapper-изменении; смягчено тем, что Y явно декларирует различие
> рычагов T1-07/T1-09 в §4 и что ядро утверждения покрыто P-10.

RH-04 — страта 2 (тот же этап flow S3–S4, другая поверхность): замена статичного
discount-тайла + Spotify-тайла на свайповый showcase из 4 карточек, офферы не меняются
(итерация 1 — одинаковые статичные карточки всем). Гипотеза кейса приписывает эффект
«additional personalization», которой в итерации 1 нет.

## 2. Точные цитаты

**Флагированная фраза в полном контексте (RH-04-Y §3, risk #1, строка 11):**

> - **The stated cause isn't in the test.** The hypothesis credits "additional
>   personalization", but iteration 1 shows the same four static cards to everyone.
>   **Wrapper changes without offer changes have not lifted purchases in this corpus
>   (P-10; T1-09 direction lesson).**

**Все места ответа, где та же мысль повторяется или оговаривается:**

- §2 (строка 7) — та же тема, но с явным противо-примером и корректной квалификацией:
  > "[hypothesis] Showcase view→click on the discount card plausibly rises — the one
  > close precedent for an **interactive-format wrapper** on this exact segment
  > **lifted layer conversion** (T1-07, L2 warning/hypothesis only). But the goal
  > metric (access CR) is likely flat-to-modestly positive… because the model's
  > load-bearing assumption — flat click→access and access→charge — is exactly the
  > assumption that **failed in wrapper-only changes** before (P-03, P-10)."
- §4 (строка 19) — явное разведение рычагов и evidentiary standing:
  > "No conflict to declare: T1-07 (interactive format lifted layer CR) and T1-09
  > (**message-only wrapper**, flat) differ in lever, and T1-09 is inconclusive/L3,
  > so they are not at comparable evidentiary standing."
- Analog-карта T1-07 (строки 29, 40–50): `mechanism: exact # presentation-format
  redesign of an offer surface, offers unchanged`; transferable: "[fact] Gamified
  format lifted interstitial-segment conversion on both platforms… [fact] significant
  relative lift did not yield a sufficient absolute increment"; not_transferable:
  "All magnitudes (+26.5% ARPU, +72-166% layer CR, -9.15% retention)… **Var2
  internals flagged anomalous on the source page.** L2: warning/hypothesis only,
  not a launch basis."
- Analog-карта T1-09 (строки 61, 72–76): `mechanism: adjacent #
  message-personalization wrapper vs structural format redesign; both leave offers
  unchanged`; transferable: "[fact] **Wrapper-only change with unchanged offers moved
  nothing** (all monetization p>=0.32); paywall→click halved. Inconclusive source:
  measurement/direction lesson only (rule 6)."
- §7.3 (строка 133) — операционный вывод из той же линии:
  > "Drop the +65%-ARPU/personalization framing for iteration 1 (nothing personalized
  > is being tested); plan iteration 2 around actual offer/content personalization
  > per P-10."

Идея «wrapper без оффера не поднимал покупки» как **универсальное утверждение о
корпусе** встречается в ответе ровно один раз — во флагированной фразе. Строка 7
утверждает иное (провал flat-downstream-допущения — поддержано T1-09), строка 72 —
[fact] о самом T1-09 (точен).

## 3. Что говорят тексты KB (проверка по источникам)

**T1-07** (`knowledge_base.md`, карта T1-07): механизм "copy/design (gamification) +
frequency/timing"; outcome fact: "**iOS var2 ARPU +26.5% (p=0.011)**; interstitial
segment +72.7% (var2) / +166% (var3); non-skippable: ×8 engagement, **+150–160% layer
revenue**, but And var3 retention D1 −9.15% (p=0.012); absolute increment small
(forecast iOS var2 +$474/day)"; lesson: "**gamification lifts layer conversion on
both platforms**… significant relative lift ≠ sufficient absolute increment";
validity: "pending-trial maturity undocumented; result **mixed**; decision killed";
transfer bounds: "var2 anomaly (−75–77% interstitial→banner) unexplained — **treat
var2 internals with caution**".

Т.е. в корпусе ЕСТЬ формат-изменение обёртки при неизменных офферах, давшее значимый
денежный (ARPU) плюс на одной платформе/арме. Оговорки KB: аномалия касается
внутренностей фаннела var2 (interstitial→banner), сам ARPU-факт KB не отзывает;
maturity не задокументирована; result_class mixed; убит за недостаточный абсолютный
инкремент. Урок KB сформулирован как «lifts layer **conversion**», не «lifts
purchases».

**T1-09**: механизм "copy/design — **message personalization only**, offers
unchanged"; outcome "≈0… paywall→click ×0.5… all monetization p ≥ 0.32";
**inconclusive** ⇒ "measurement/direction lessons only".

**P-10** («Personalize the offer, not only the wrapper», mandatory): claim —
"personalizing only the **message/creative** around an unchanged offer does not lift
purchases; personalization works when the OFFER itself… matches the user's state".
Единственный негативный факт — тот же T1-09. Transfer bans: "…the ban is on
expecting purchase lifts". Applicability: "any personalization idea on S3–S6;
**wrapper-vs-offer design decisions**" — RH-04 в scope.

**P-03** («Attention ≠ intent»): факты T1-09, T1-07 (non-skippable: engagement ×8 при
retention-цене), T2-02; transfer ban: "does not prove creative never matters".

**Вывод по фактике:** буквальное прочтение «Wrapper changes without offer changes
have not lifted purchases in this corpus» противоречит корпусу: T1-07 var2 iOS ARPU
+26.5% (p=0.011) — денежный лифт от wrapper/формат-изменения без изменения оффера, и
сам ответ (а) оценивает механизм T1-07 как exact к RH-04, (б) в §2 называет T1-07
«interactive-format **wrapper**», т.е. в собственной лексике ответа T1-07 входит в
класс «wrapper changes». Противоречие снимается только при узком прочтении
«wrapper = message-only обёртка» (лексика §4 и карты T1-09) и/или при
строго-эвиденциальном прочтении «не поднимал» = «нет валидированного purchase-лифта»
(T1-07: mixed, maturity undocumented, var2-аномалия, killed; урок KB про conversion,
не про purchases). Оба прочтения защитимы, но во фразе не выражены.

**Как ответ квалифицирует аномалию var2:** корректно и дважды — в not_transferable
карты T1-07 ("Var2 internals flagged anomalous on the source page") и удержанием всех
величин (+26.5% и пр.) исключительно в not_transferable; в прозе ответ нигде не
утверждает «T1-07 поднял покупки», только «lifted layer conversion/CR».

## 4. Разбор по определению C6 (§4 протокола) и policy

**Категория 1 — перенос величины как предсказания: НЕТ.** Ни одной величины во фразе
и вокруг; все магнитуды ответа (в т.ч. +26.5%) лежат в `not_transferable`. Линтерная
норма `effect_magnitude present outside [not_transferable, sizing_prior_labeled]` не
нарушена.

**Категория 2 — перенос продуктового вывода из L3/далёкого аналога: ЧАСТИЧНО.**
Ядро реально используемого утверждения («не приписывайте purchase-лифт
message-обёртке; ничего персонализированного не тестируется») покрыто P-10 — frozen
mandatory-паттерном KB, применённым внутри его applicability («wrapper-vs-offer
design decisions»), с корректной инлайн-меткой «T1-09 direction lesson». Это
KB-лицензированное применение, не модельный перенос. Нарушение — в **расширении
класса**: фраза покрывает ВСЕ wrapper-изменения (включая формат-редизайн — механизм
самого RH-04), тогда как P-10 говорит только о message/creative-персонализации, а
T1-09 — единственный inconclusive-кейс этого узкого класса. Утверждение типа «have
not lifted» — вывод класса «does not work», для которого validity gate требует
powered-null («inconclusive is never enough», rule 7 KB §1;
`validity_gate.does_not_work_conclusion_requires: powered-null`); в расширенном
классе оно к тому же противоречит L2-факту (T1-07 var2). По правилу конфликтов
(policy §3) более близкий аналог выигрывает: для формат-класса ближе T1-07 (L2,
mechanism exact), а не T1-09 (L3) — расширенная фраза в точке употребления
подавляет более близкий позитивный факт.

**Категория 3 — single-case generalization без оговорки: ЧАСТИЧНО.** База обобщения —
фактически один кейс (T1-09; негативный факт P-10 — тот же T1-09; T2-02 — тоже
inconclusive). Оговорка ЕСТЬ, но неполная: инлайн-метка «(P-10; T1-09 direction
lesson)» квалифицирует статус ИСТОЧНИКА, однако не квалифицирует ОБЪЁМ класса —
слова «message-only» во фразе нет, а «in this corpus» лишь усиливает универсальность
в границах корпуса. Разведение рычагов сделано в §4, т.е. в другой секции; сам
риск-буллет читается как безоговорочная универсалия.

**Категория 4 — повышение слабого evidence до статуса аналога: НЕТ.** T1-09 подан как
L3/inconclusive, уровень посчитан по осям корректно (mechanism adjacent ⇒ не L1/L2),
никакого промоушена; «no direct analogs» не требовался (L2 непуст).

**Policy `fact_vs_transfer` (§5 / yaml):** нарушение определено как «a source fact
presented as a fact about the new case». Фраза — утверждение о КОРПУСЕ, не факт о
новом кейсе; строгое определение НЕ выполнено.

**Правило pattern_cards (глобальное, №3):** «A pattern must not be applied outside
its applicability scope without flagging the transfer as unsupported». Применение
P-10 к кейсу — в scope; но **claim паттерна расширен** (message/creative → любой
wrapper) без флага. Расширению способствует сама KB: заголовок P-10 («…not only the
wrapper») употребляет «wrapper» шире, чем тело паттерна — смягчающее обстоятельство
для ответа.

**C2 (hallucinated/distorted lesson)?** НЕТ. Ни одной сфабрикованной ссылки, числа
или урока: P-10 и T1-09 существуют и по отдельности процитированы точно (судья
верифицировал C2_Y=0, подтверждаю). Дефект — объём синтезированного обобщения, а не
достоверность источников; это домен C6 (unsupported generalization/transfer), не C2.

## 5. Формальное или содержательное

**Формальное (wording-level).** Проверка по всем точкам опоры ответа:

- **Вердикт** — «Launch with changes» (позитивный); никакой блокировки идеи на фразе
  не строится (blocking-норма policy §4 не задействована; false-blocker риска нет).
- **Прогноз (§2)** — «flat-to-modestly positive» на goal-метрике, рост view→click
  плюс скепсис к модельным 92%/40%/+65% ARPU. Это направление СОГЛАСОВАНО с T1-07
  («significant relative lift ≠ sufficient absolute increment», L2) и не зависит от
  расширенного прочтения фразы; помечено [hypothesis].
- **Рекомендации (§6–7)** — exposure-анкер, re-power, guardrails/stop-rules,
  maturity-гейт, §7.3 «снять рамку персонализации, итерация 2 — офферная
  персонализация per P-10» — всё остаётся валидным при корректной узкой формулировке.
- **Величины/уровни** — не переносятся, не завышаются.

Замена одного словосочетания («Wrapper changes» → «Message-only wrapper changes»
или «Message/creative-personalization wrappers») устраняет нарушение, не меняя ни
одного вывода, риска или рекомендации ответа. Содержательной нагрузки (продуктовый
вывод, вердикт, величина, статус evidence) на овергенерализованном прочтении не
висит.

## 6. Влияние на вердикт ответа

Нулевое по существу: риск #1 остаётся истинным и без фразы (заявленная причина —
персонализация — действительно не тестируется в итерации 1; это подтверждается самой
карточкой кейса), а историческая опора риска в узкой формулировке полностью
покрывается P-10 + T1-09. Внутренняя дисциплина ответа в остальном образцовая:
позитивный противо-пример T1-07 вынесен в §2 первым, конфликт рычагов явно разобран
в §4, магнитуды и var2-аномалия карантинированы в not_transferable.

## 7. Итоговая классификация

- **C6-нарушение: ДА, счёт 1 (подтверждаю флаг судьи), характер — ФОРМАЛЬНОЕ,
  пограничное.** Тип: овергенерализация класса при переносе (расширение claim'а
  P-10 с message/creative-персонализации на все wrapper-изменения, включая
  механизм-класс самого RH-04) без инлайн-оговорки объёма; в расширенном классе
  утверждение буквально противоречит корпусному факту T1-07 var2 iOS ARPU +26.5%
  (p=0.011), который ответ сам цитирует как mechanism-exact L2. Ни одна из четырёх
  категорий C6 не выполнена «чисто» (величина — нет; статус аналога — нет;
  fact-about-new-case — нет; single-case — с частичной оговоркой), поэтому
  существует защитимое миноритарное прочтение C6=0 (узкое «wrapper = message-only»
  по лексике §4 + строго-эвиденциальное «нет валидированного purchase-лифта»:
  T1-07 mixed/maturity-undocumented/var2-anomaly/killed, урок KB — про conversion).
  Решающий довод за 1: в точке употребления (риск-буллет о формат-редизайне)
  естественное прочтение фразы распространяет негатив на рычаг самого RH-04, чего
  цитируемые источники не поддерживают, а протокол считает нарушения по
  утверждениям, а не по нетто-смыслу всего ответа.
- **Не C2:** источники существуют, каждый процитирован точно; дефект — объём
  синтеза, не groundedness.
- **Влияние на гейт «unsupported transfers = 0» (§6.5 протокола):** при зачёте
  счёт C6 у RH-04-Y = 1 > 0 — условие 5 формально НЕ выполняется для этого прогона
  (если Y — плечо B; mapping запечатан, судья идентифицировал Y как KB-несущий по
  содержанию). Frozen-протокол не различает формальные и содержательные нарушения
  (прецедент FLOW-579: формальный NO по одному условию), пороги после начала прогона
  не пересматриваются — рекомендую фиксировать «C6 = 1 (формальное, wording-level,
  без влияния на решения)» и вести гейт по букве. Единственный путь к C6=0 — если
  владелец оценки постановит, что инлайн-оговорка «direction lesson» + разведение
  рычагов в §4 удовлетворяют клаузу «без оговорки» из §4 протокола; это решение
  выходит за мандат данной верификации и должно быть зафиксировано явно, а не
  подразумеваться.
- **Generic-урок для KB V1.2 (не кейс-специфичный):** источник двусмысленности —
  заголовок P-10 («…not only the wrapper») шире тела паттерна; уточнение заголовка
  до «…not only the message/creative wrapper» и линтер-запрет бес-квалификаторных
  универсалий вида «X have not … in this corpus» без перечисления класса закрыли бы
  этот режим отказа системно.
