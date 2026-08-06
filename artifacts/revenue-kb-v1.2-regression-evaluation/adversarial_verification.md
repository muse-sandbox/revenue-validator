# АДВЕРСАРИАЛЬНАЯ ВЕРИФИКАЦИЯ ФЛАГОВ — FLOW-593 Фаза C

Все пять флагов, поднятых слепыми судьями, проверены независимыми верификаторами
**после** заморозки scorecard'ов (`blind_scorecards_freeze.txt`) и **до** вскрытия
`arm_mapping_sealed.md` и ground truth. Каждый верификатор получил задание
максимально скептически ОПРОВЕРГНУТЬ обвинение, читал только проверяемый ответ из
`blind-pairs/` и frozen KB V1.2, и не имел доступа к mapping, ground truth,
judge-файлам и артефактам FLOW-579/586.

## Сводка

| # | Флаг | Кейс / ответ | Вердикт | Severity |
|---|---|---|---|---|
| 1 | C2 — hallucinated lesson: приписана значимость «significantly negative [T1-04]» | RH-02 / X | **CONFIRMED** | formal-wording |
| 2 | C6 — исход inconclusive-источника T2-02 перенесён в предсказание | RH-03 / Y | **CONFIRMED** | formal-wording |
| 3 | C6 — «полное отключение» (T2-01) расширено на «частичную деградацию» как факт | RH-04 / Y | **CONFIRMED** | formal-wording |
| 4 | CONSIST — односторонний вывод по классу GC-05 при процитированном противоположном evidence | RH-04 / Y | **CONFIRMED** | **substantive** |
| 5 | C6 — направление вывода из T3-02 (ценовая чувствительность save-оффера) шире измеренного | RH-06 / X | **REFUTED** | — |

**Итог: 4 подтверждённых нарушения, 1 опровергнутое.**

## 1. C2 / RH-02 / X — CONFIRMED (formal-wording)

KB по T1-04 ведёт статус значимости пофакторно: для Android — «significant in
both iterations», для iOS iter2 — p=0.43, а для сегмента iOS iter1 приведена
только магнитуда −24.7% без p-value и без метки. То же в P-01/P-02. Ответ дважды
повышает эпистемический статус этого числа до статистически значимого, причём во
второй раз — внутри тега `[fact]` со ссылкой `[T1-04]`, то есть подаёт как
воспроизведение содержимого карточки. Это C2(б) — искажение содержания
существующей карточки KB.

Защита «significantly в обиходном смысле» отклонена: параллельная конструкция
(«iOS was not significant in iter2, and the iter1 iOS segment … was significantly
negative») заведомо статистическая; весь ответ последовательно использует
«significant» в строгом смысле; в `not_transferable` той же карточки автор
воспроизвёл −24.7% корректно, без метки — то есть различал регистры.

Вердикт/прогноз/рекомендации ответа на фразе не держатся: уберите слово
«significantly» — выводы остаются в силе.

## 2. C6 / RH-03 / Y — CONFIRMED (formal-wording)

T2-02 в KB имеет `result_class: inconclusive`; §1.7 прямо гласит: «cases with
`result_class: inconclusive` … ground measurement lessons only — never product
conclusions. For a "does not work" conclusion you need powered-null, not
inconclusive». Спорная фраза в «Predicted outcome» предсказывает продуктовую форму
исхода («null on DAU→Charge … attention metrics possibly up») и обосновывает её
самим источником: «the L1 analog T2-02 read exactly that shape».

Защита «это предсказание нечитаемости, а не продуктовый вывод» отклонена по двум
причинам: (а) вторая половина прогноза — положительный направленный эффект
(splash views вверх), перенесённый из значимого замера inconclusive-кейса, что к
утверждению о нечитаемости не сводится; (б) апелляция к статусу «L1 analog»,
который по §2.2 означает «product conclusion transfers directionally»,
приравнивает inconclusive к powered-null — ровно то, что §1.7 запрещает.

Отягчает то, что собственная analog-карточка ответа воспроизводит правило
дословно («NO product conclusion transfers even at L1 — only measurement
lessons») и тут же в прозе делает запрещённый шаг. Вердикт и рекомендации на
фразе не держатся.

## 3. C6 / RH-04 / Y — CONFIRMED (formal-wording)

T2-01 измерял полное выключение поверхностей (`surface OFF`, both-off arm), и KB
дважды несёт оговорки: «NOT **fully** redistribute» и «when a surface
**disappears**». В прозе ответа сняты обе: «existing tiles carry real incremental
value that does not redistribute when degraded (T2-01, P-02)» — в изъявительном
наклонении, без `[hypothesis]`, со ссылкой как на установленное основание.
Заявленный уровень T2-01 в ответе — L2, а L2 по §2.2 переносится только как
гипотеза/предупреждение.

Analog-карточка нарушение не снимает, а усиливает обвинение: в ней та же мысль
корректно расщеплена на `[fact]` (полное отключение) и `[hypothesis]`
(деградация), а `not_transferable` прямо декларирует «The source measured full
removal, not partial demotion; harm from demotion is a transfer hypothesis». То
есть ответ знал границу и всё равно подал в summary результат за её пределами как
факт. Дополнительно отягчает: единственная в KB частичная версия воздействия —
splash-only-off — оказалась n.s. (iOS −1.2%, p=0.83), то есть доступное
свидетельство о частичном ослаблении скорее противоречит перенесённому
утверждению.

## 4. CONSIST / RH-04 / Y — CONFIRMED (**substantive**)

Это тот самый класс дефекта, ради устранения которого собран V1.2.

Фраза: «Total access CR moves little or not at all … because iteration 1 changes
format only, not offers, and **attention-format lifts have not translated into
purchases on similar App exposure surfaces where measured (T1-09, T2-02, P-03)**».

**Квалификаторы не работают.** «on similar App exposure surfaces»: в опору взят
T1-09, чьи coords — «S3–S4; **interstitial slot**». То есть интерстишл засчитан
как «similar». Но в собственных analog-карточках того же ответа интерстишл
объявлен НЕ похожей поверхностью: T1-07 — `surface: different # interstitial slot
vs persistent discovery tile`; T1-04 — то же. Любое непротиворечивое прочтение
«similar» либо включает все три интерстишла (тогда T1-07 внутри скоупа и
противоречит утверждению), либо исключает их все (тогда рушится собственная опора
T1-09). «where measured» бьёт в обратную сторону: T1-09 и T2-02 — как раз
`inconclusive` («measurement lessons only»), а исключённые T1-07 (iOS var2 ARPU
+26.5%, p=0.011) и T1-04 (Android ARPU +17–19% significant) — единственные со
значимо измеренным денежным эффектом в классе.

**KB прямо объявляет класс двусторонним.** §2.6, GC-05 (creative/design/
gamification на существующей поверхности): `outcome_positive: T1-04, T1-07`;
`outcome_negative: T1-09, T2-02`. Правило чтения там же: «a class listing IDs on
both sides means the corpus itself is mixed for that family. A one-sided universal
over such a family is therefore almost always wrong — say `evidence is mixed` (G3)
or narrow the claim to the sub-class you can actually support (G1)». Ответ взял
ровно две отрицательные ID класса и опустил обе положительные, не дав ни
G1-аннотации, ни G3-литерала.

**Литерала `evidence is mixed` в ответе нет нигде.** Все вхождения слова «mixed» —
это `result_class` источника внутри fenced-блоков. Более того, единственная
прозаическая метка о конфликтности направлений — противоположная по смыслу: «No
conflicts between the retrieved analogs».

**L3-карантин не считается объявлением out-of-scope.** §2.5 описывает именно этот
сценарий как дефект, ради которого написана: «it can contradict a positive case
the same answer cites and **quarantines elsewhere**». Легальны только `not
covered:` в G1-аннотации либо литерал `evidence is mixed` по G3.

**Severity — substantive.** Фраза стоит после «because» и служит прямым
основанием центрального прогноза «Total access CR moves little or not at all — far
below the 92%/40% modeled targets»; повторена как риск №5 и питает рекомендацию
№3. Умолчание о положительном плече GC-05 систематически смещает прогноз вниз.

### Линтер V1.2 этот дефект НЕ ловит — и это главный вывод прогона

Причина строго механическая: правило G2 срабатывает только при конъюнкции
`CORPUS_SCOPE_MARKER AND UNIVERSAL_MARKER`. Универсальный маркер есть («have
not»). Корпусного маркера нет ни одного: в списке `CORPUS_SCOPE_MARKERS` —
`this corpus / the corpus / our corpus / corpus-wide / this|the knowledge base /
this|the evidence base / the knowledge context / the reviewed cases / the cases
reviewed / the cited cases / the source cases / past experiments / prior
experiments / historical cases`. Фраза обобщает через «on similar App exposure
surfaces **where measured**» — семантически это квантор по доказательной базе
(«во всех случаях, где это измеряли»), но лексически ни один литерал из списка не
встречается. Предложение в обычной прозе, под exemption не подпадает, просто не
проходит первую половину конъюнкции. Проверка на противоречие
(`E_UNIVERSAL_CONTRADICTS_SOURCE`) вычисляется только для уже помеченных
предложений, поэтому до неё дело не доходит.

**Следствие:** V1.2 закрывает дыру только для явно корпусно-маркированных
формулировок. Пересказ того же одностороннего обобщения через «на похожих
поверхностях / где измеряли / where measured / in the cases we have» проходит
линтер насквозь. Это ровно ограничение №1, которое builder Фазы A задекларировал
сам; regression-прогон показал, что оно не теоретическое, а реализуется на первом
же прогоне.

## 5. C6 / RH-06 / X — REFUTED

Судья прав фактически: в T3-02 цены снижались (включая сам «ambulance»
$49.99→$19.99), а comeback-CR всё равно упал на 20%, так что наивная эластичность
источником не подтверждена. Но C6 требует переноса продуктового вывода/величины в
неизмеренную сторону, а ответ такого вывода не делает: −20% не перенесён, падение
take при $19.99→$24.99 не предсказано, знак не заявлен. Утверждается
ненаправленная подвижность метрики («take is price-sensitive»), и она буквально
наблюдалась: единственная манипуляция T3-02 была ценовой, guardrail сдвинулся на
20%. При альтернативном объяснении −20% через композицию/селекцию операционный
вывод ответа не меняется — метрику надо инструментировать тем более. §2.2 прямо
разрешает слабое evidence «ONLY for sizing, measurement and guardrails»; T3-02
здесь не далёкий аналог (та же платформа web, тот же этап S5–S6, тот же механизм
price, буквально тот же объект — save/ambulance-оффер).

Остаточный дефект есть, но другой природы: неохеджированное «shows» приписывает
движение guardrail именно цене, хотя KB эту атрибуцию не изолирует. Это вопрос
осторожности формулировки, а не unsupported transfer по C6.
