# Interstitials Corpus Prep (FLOW-568)

Подготовленный корпус завершённых экспериментов семейства «UG App monetization interstitials» для проверки продуктовой knowledge base (FLOW-567). Split заморожен 2026-08-04 (см. `split_manifest.md`); после freeze состав наборов не меняется.

## Кому что разрешено читать

| Каталог / файл | Knowledge builder (FLOW-567) | Inference / validation agent | Судья (оценка ответов) |
|---|---|---|---|
| `README.md`, `BUNDLE_MANIFEST.md` | ✓ | ✓ | ✓ |
| `knowledge-sources/` | ✓ | по правилам FLOW-567 | ✓ |
| `holdout-blind/` | **✗ запрещено** | ✓ (это его вход) | ✓ |
| `ground-truth-sealed/` | **✗ запрещено** | **✗ запрещено** | ✓ (только после получения предсказаний) |
| `safe_inventory.md`, `corpus_eligibility.md`, `split_manifest.md`, `EXCLUSION_MANIFEST.md`, `LEAKAGE_CHECK.md` | ✗ (содержат mapping holdout) | ✗ | ✓ |

Дополнительно запрещено knowledge builder'у и inference-агенту: чтение исходных Confluence-страниц holdout-экспериментов (список в `EXCLUSION_MANIFEST.md`), поиск в Confluence/Slack/Jira по формулировкам blind-карточек, чтение локального зеркала базы гипотез (`context/hypotheses/` — содержит однострочные аннотации исходов) и реестра `ab_experiment` (поле `success_variation` раскрывает исход).

## Состав

- `safe_inventory.md` — полный дедуплицированный inventory кандидатов (outcome-blind).
- `corpus_eligibility.md` — проверка достаточности: 10 пригодных → READY.
- `split_manifest.md` + `split_manifest.json` — правило, cutoff 2026-01-01, составы, SHA-256.
- `knowledge-sources/` — 6 полных карточек (KS-01…KS-06) с pre-launch данными и результатами.
- `holdout-blind/` — 4 очищенные pre-launch карточки (IH-01…IH-04), исходы удалены.
- `ground-truth-sealed/` — mapping IH→эксперимент, фактические исходы, решения, lessons, ссылки.
- `EXCLUSION_MANIFEST.md` — что запрещено использовать при построении knowledge base.
- `LEAKAGE_CHECK.md` — результаты проверки пересечений и утечек.
- `BUNDLE_MANIFEST.md` — SHA-256 всех файлов пакета.

## Handoff при READY

Агент, строящий knowledge base, получает **только**: `README.md`, `BUNDLE_MANIFEST.md`, `knowledge-sources/`.
