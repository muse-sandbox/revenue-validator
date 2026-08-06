# ARM MAPPING — SEALED (FLOW-570)

**Не открывать до завершения blind pairwise review (C1–C4, C6) всех четырёх кейсов.**
Evaluator сначала выносит вердикты по парам X/Y вслепую и только затем читает этот файл.

Рандомизация: один бит `/dev/urandom` на кейс, зафиксирована 2026-08-04 до сборки пар.

| Кейс | X | Y |
|---|---|---|
| IH-01 | arm A (без KB) | arm B (с KB) |
| IH-02 | arm B (с KB) | arm A (без KB) |
| IH-03 | arm B (с KB) | arm A (без KB) |
| IH-04 | arm A (без KB) | arm B (с KB) |

Проверка целостности: sha256 каждого `blind-pairs/IH-0n-{X,Y}.md` обязан совпадать с sha256
соответствующего `arm-{a,b}/IH-0n.md` из `run_manifest.md` / `BUNDLE_MANIFEST.md`.
