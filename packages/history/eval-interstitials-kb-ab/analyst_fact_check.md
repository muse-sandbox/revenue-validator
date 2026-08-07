# ANALYST FACT CHECK — объективные факты на подтверждение аналитику (FLOW-571)

Статус: **не заполнено — подтверждение недоступно в этой сессии.** Зона аналитика: воспроизводимость объективных проверок и outcome alignment. Всё ниже проверяемо механически по frozen-файлам, без вкусовых суждений.

## Факты, требующие подтверждения (каждый — да/нет)

1. **Integrity.** SHA-256 всех файлов трёх бандлов совпадают с манифестами: kb-v0 7/7, ab-run 19/19, corpus-prep 22/22 (перезапустить проверку из `BUNDLE_MANIFEST.md` этой папки, раздел «Preflight re-check»).
2. **Порядок фаз.** `blind_pairwise_scorecards.md` (sha256 `0142d53f442e7a7a78669a996beb8f41e51b40c82a703cd17fd256d6f8c35bbf`) создан и захэширован ДО чтения `arm_mapping_sealed.md` и `ground-truth-sealed/` — проверить по таймстемпам в тексте scorecards (freeze 08:43:16Z) и логике сессии.
3. **C2 = 0 (hallucinations).** Выборочно перепроверить `grounding_audit.md`: минимум по 3 утверждения на кейс сверить с `pattern_cards.md`/`knowledge_base.md` (например: IKB-P09 «Total exes −2.2% p=0.77»; IKB-P10 «21% iOS trial = instant charge», «27% iOS повторный trial»; IKB-P03 «1.58%→0.41%»; IKB-P11 «28–48% видео-fail»; KS-02 §Decision «novelty effect trap»).
4. **C6 = 0 (unsupported transfers).** Подтвердить, что в 4 B-ответах каждый single-case паттерн (IKB-P05, IKB-S01…S03, intro-сторона IKB-P08, величины IKB-P10) сопровождён оговоркой, и «не переносить»-границы KB не нарушены.
5. **Outcome alignment (C5) — корректность моего прочтения GT:**
   - IH-01: причина отказа от rollout — «revenue was too low» при значимом iOS ARPU var2 +26.5% (p=0.011); Android var3 retention значимо вниз (p=0.012/0.018/0.023).
   - IH-02: rollout обеих платформ; winback member→buyers +365.6% iOS (p=0.000); Total ARPU незначим (p=0.40/0.22) «only due to small segments»; iOS диффузное размытие non-winback (−27 buyers, −$702).
   - IH-03: fail/inconclusive; iOS нечитаем (провал доставки); paywall→click 7.25%→3.90%; урок «personalize the offer, not the wrapper»; ex-paid ~20× per member.
   - IH-04: no rollout; iOS surface net revenue +58.14% при flat volume (final read); Android объём −44.4% (эластичность); winback undecided; урок про surface-метрику vs Total ARPU.
6. **False blockers.** Подтвердить трактовку §5 протокола для IH-02: `revise` обоих плеч при частично подтверждённых причинах (нечитаемость ARPU, каннибализационный риск) → не false blocker; итог 0(B) ≤ 0(A).
7. **Активационное событие (для любых собственных пересчётов).** Все четыре эксперимента (7160/7187, 7487, 7454, 7712) активируются `App Experiment Start` с `item_id = <exp_id>` — при желании пересчитать метрики по ClickHouse использовать правила `context/rules/ab-activation-exposure.md`; НЕ фильтровать по одному только `App Experiment Start`.

## Шаблон ответа

```
1. Integrity: подтверждаю / нет (…)
2. Порядок фаз: подтверждаю / нет
3. C2=0: подтверждаю / найдено искажение (…)
4. C6=0: подтверждаю / найден неоговорённый перенос (…)
5. Чтение GT: подтверждаю / поправки (…)
6. False blockers 0/0: подтверждаю / нет
7. (опц.) Пересчёты по ClickHouse: делал / не делал
Подпись, дата:
```
