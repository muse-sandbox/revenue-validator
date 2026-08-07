# MAPPING — Held-out validation set (FLOW-568, interstitial experiments)

SEALED ground-truth mapping. Read only by the evaluation judge.

| IH-ID | Original experiment (page title) | pageId | URL | AB experiment ids | Jira | Launch / end dates |
|---|---|---|---|---|---|---|
| IH-01 | [2026-03-09] UG App: paywall – pre-paywall with animation for interstitials [2026-07-01] | 773658792 | https://alice.mu.se/spaces/CRO/pages/773658792 | 7160 (original run, registry 2026-03-16..2026-03-18) + 7187 (relaunch, registry 2026-03-20..2026-03-27; the page's Results section is for #7187) | UMN-10952 | Project page dates 2026-03-09 .. 2026-07-01 |
| IH-02 | [2026-05-04] UG App: winback - final interstitial offer [2026-07-30] | 788612067 | https://alice.mu.se/spaces/CRO/pages/788612067 | 7487 (registry & page: run 2026-05-22 → 2026-06-12, ~21 days) | UMN-11515 | Project page dates 2026-05-04 .. 2026-07-30 |
| IH-03 | [2026-05-05] UG App: personalized interstitial [2026-06-18] | 788613565 | https://alice.mu.se/spaces/CRO/pages/788613565 | 7454 (registry run 2026-05-18..2026-05-27; 10 days per Design-vs-Reality) | UMN-11540 | Project page dates 2026-05-05 .. 2026-06-18 |
| IH-04 | [2026-07-03] UG App: interstitial - discounted prices [2026-XX-XX] | 811868738 | https://alice.mu.se/spaces/CRO/pages/811868738 | 7712 (registry run 2026-07-13..2026-07-21, 9 delivered days) | UMN-12220 | Project page start 2026-07-03; page end date still "2026-XX-XX" (not closed). Registry run dates 2026-07-13 .. 2026-07-21 |

Notes:
- AB registry rows (`_registry.json` in the snapshot folder): 7160 "[UG Monetization] Pre-paywall with animation for interstitials"; 7187 "… (relaunch)"; 7454 "[UG Monetization] UG App: personalized interstitial"; 7487 "[UG Monetization] UG App: winback - final interstitial offer"; 7712 "[UG Monetization] UG App: interstitials - discounted prices". All with activation event `App Experiment Start` and jira keys as above.
- Snapshot versions used: 773658792 v27 (2026-07-23), 788612067 v29 (2026-06-30), 788613565 v41 (2026-06-18), 811868738 v17 (2026-07-31).
