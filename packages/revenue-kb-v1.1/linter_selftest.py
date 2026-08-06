#!/usr/bin/env python3
"""Deterministic selftest for linter.py (Revenue Validator V1.1, FLOW-586).

All fixtures are synthetic (invented sources T9-01/T9-02/P-90); none derive
from any real or holdout experiment case. Run:

    python3 linter_selftest.py

Exit 0 = all tests green. Output is deterministic; running twice must produce
byte-identical stdout.
"""

import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FIX = os.path.join(HERE, "selftest_fixtures")
LINTER = os.path.join(HERE, "linter.py")
FIXTURE_KB = os.path.join(FIX, "fixture_kb.md")
FIXTURE_PATTERNS = os.path.join(FIX, "fixture_patterns.md")
REAL_KB = os.path.join(HERE, "knowledge_base.md")
REAL_PATTERNS = os.path.join(HERE, "pattern_cards.md")

sys.path.insert(0, HERE)
import linter  # noqa: E402


def run_linter(answer, no_kb_arm=False, kb=FIXTURE_KB, patterns=FIXTURE_PATTERNS):
    cmd = [sys.executable, LINTER, os.path.join(FIX, answer),
           "--kb", kb, "--patterns", patterns]
    if no_kb_arm:
        cmd.append("--no-kb-arm")
    proc = subprocess.run(cmd, capture_output=True, text=True)
    try:
        report = json.loads(proc.stdout)
    except ValueError:
        report = None
    return proc.returncode, report, proc.stdout


def error_codes(report):
    codes = [e["code"] for e in report.get("errors", [])]
    for card in report.get("cards", []):
        codes.extend(e["code"] for e in card.get("card_errors", []))
    return sorted(set(codes))


def make_card(**overrides):
    axes = {a: "exact" for a in linter.AXES}
    axes.update(overrides.pop("axes", {}))
    card = {
        "axes": axes,
        "segment_monetization_state": "exact",
        "money_chain_link": "exact",
        "platform": "exact",
    }
    card.update(overrides)
    return card


def main():
    results = []

    def check(name, ok, detail=""):
        results.append({"test": name, "ok": bool(ok), "detail": detail})

    # --- CLI tests on fixture answers -------------------------------------
    cli_cases = [
        ("cli_pass_l1", "answer_pass_l1.md", False, 0, []),
        ("cli_pass_l2_all_branches", "answer_pass_l2_branches.md", False, 0, []),
        ("cli_pass_l3_no_direct_analogs", "answer_pass_l3_nodirect.md", False, 0, []),
        ("cli_fail_level_inflation", "answer_fail_inflation.md", False, 1,
         [linter.E_LEVEL_MISMATCH]),
        ("cli_fail_missing_no_direct_analogs", "answer_fail_missing_no_direct.md",
         False, 1, [linter.E_MISSING_NO_DIRECT_ANALOGS]),
        ("cli_fail_empty_not_transferable", "answer_fail_empty_nt.md", False, 1,
         [linter.E_EMPTY_NOT_TRANSFERABLE]),
        ("cli_fail_unknown_source_id", "answer_fail_bad_source.md", False, 1,
         [linter.E_UNKNOWN_SOURCE_ID]),
        ("cli_fail_missing_axis", "answer_fail_missing_axis.md", False, 1,
         [linter.E_CARD_PARSE]),
        ("cli_fail_missing_side_effects", "answer_fail_no_sideeffects.md", False, 1,
         [linter.E_MISSING_SIDE_EFFECTS]),
        ("cli_nokb_pass", "answer_nokb_pass.md", True, 0, []),
        ("cli_nokb_fail_card_emitted", "answer_nokb_fail_card.md", True, 1,
         [linter.E_CARD_IN_NO_KB_ARM]),
    ]
    for name, answer, no_kb, want_exit, want_codes in cli_cases:
        code, report, _ = run_linter(answer, no_kb_arm=no_kb)
        if report is None:
            check(name, False, "linter stdout was not JSON")
            continue
        got_codes = error_codes(report)
        ok = code == want_exit and got_codes == sorted(want_codes)
        check(name, ok,
              "exit=%d (want %d), codes=%s (want %s)"
              % (code, want_exit, got_codes, sorted(want_codes)))

    # Per-card computed levels in the L2-branches fixture.
    code, report, _ = run_linter("answer_pass_l2_branches.md")
    levels = [c.get("computed_level") for c in report["cards"]] if report else []
    check("cli_l2_branches_all_compute_L2", levels == ["L2", "L2", "L2", "L2"],
          "computed=%s" % levels)

    # --- Unit tests of the deterministic level formula --------------------
    unit_cases = [
        ("unit_L1_platform_adjacent_is_L1",
         make_card(axes={"surface": "adjacent"}, platform="adjacent"), "L1"),
        ("unit_R1_platform_different_blocks_L1_gives_L2C",
         make_card(platform="different"), "L2"),
        ("unit_R2_segment_axis_different_same_state_stays_L1",
         make_card(axes={"segment": "different"}), "L1"),
        ("unit_L2A_mechanism_exact_surface_different",
         make_card(axes={"surface": "different"}), "L2"),
        ("unit_L2A_mechanism_exact_flow_different",
         make_card(axes={"flow_stage": "different"}), "L2"),
        ("unit_L2B_surface_flow_exact_mechanism_different",
         make_card(axes={"mechanism": "different"}), "L2"),
        ("unit_L2C_monetization_state_different",
         make_card(segment_monetization_state="different"), "L2"),
        ("unit_R4_money_chain_link_different_no_L2C_gives_L3",
         make_card(money_chain_link="different"), "L3"),
        ("unit_R5_flow_adjacent_not_exact_gives_L3",
         make_card(axes={"flow_stage": "adjacent"}), "L3"),
        ("unit_L3_metric_only",
         make_card(axes={a: "different" for a in linter.AXES if a != "metric"},
                   segment_monetization_state="different",
                   money_chain_link="different", platform="different"), "L3"),
    ]
    for name, card, want in unit_cases:
        got = linter.compute_level(card)
        check(name, got == want, "computed=%s want=%s" % (got, want))

    # --- Real KNOWLEDGE CONTEXT source-ID extraction ----------------------
    with open(REAL_KB, encoding="utf-8") as fh:
        kb_text = fh.read()
    with open(REAL_PATTERNS, encoding="utf-8") as fh:
        patterns_text = fh.read()
    ids = linter.collect_known_ids(kb_text, patterns_text)
    expected_present = {"T1-01", "T1-08", "T1-10", "T2-05", "T3-06", "P-01", "P-14"}
    expected_absent = {"T8-99", "T9-01"}
    check("real_kb_ids_present", expected_present.issubset(ids),
          "missing=%s" % sorted(expected_present - ids))
    check("real_kb_ids_absent", not (expected_absent & ids),
          "unexpected=%s" % sorted(expected_absent & ids))

    # --- Determinism: same invocation twice, byte-identical stdout --------
    _, _, out1 = run_linter("answer_pass_l2_branches.md")
    _, _, out2 = run_linter("answer_pass_l2_branches.md")
    check("linter_stdout_deterministic", out1 == out2)

    passed = sum(1 for r in results if r["ok"])
    summary = {
        "tests": results,
        "total": len(results),
        "passed": passed,
        "failed": len(results) - passed,
        "verdict": "GREEN" if passed == len(results) else "RED",
    }
    print(json.dumps(summary, sort_keys=True, indent=2))
    return 0 if summary["verdict"] == "GREEN" else 1


if __name__ == "__main__":
    sys.exit(main())
