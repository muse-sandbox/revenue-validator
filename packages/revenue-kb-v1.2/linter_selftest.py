#!/usr/bin/env python3
"""Deterministic selftest for linter.py (Revenue Validator V1.2, FLOW-593).

All fixtures are synthetic (invented sources T9-01…T9-04, pattern P-90,
invented generalization classes GC-90/GC-91, invented topics "widget nudges"
and "glow buttons"); none derive from any real or holdout experiment case.
The V1.1 fixture answers and fixture_kb.md / fixture_patterns.md are inherited
byte-identically and keep their exact V1.1 expected verdicts (the
`cli_*` block below IS the V1.1 regression proof). Run:

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
FIXTURE_KB_GC = os.path.join(FIX, "fixture_kb_gc.md")
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
    for gen in report.get("generalizations", []):
        codes.extend(e["code"] for e in gen.get("errors", []))
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

    # --- V1.2 CLI tests: corpus-level generalizations (KB §2.5/§2.6) ------
    # These run against the synthetic KB that declares GC-90/GC-91.
    gc_cases = [
        ("gc_fail_unqualified_universal",
         "answer_fail_unqualified_universal.md", 1,
         [linter.E_UNQUALIFIED_UNIVERSAL]),
        ("gc_pass_scoped_universal", "answer_pass_scoped_universal.md", 0, []),
        ("gc_fail_scope_unknown_id", "answer_fail_scope_bad_id.md", 1,
         [linter.E_SCOPE_UNKNOWN_ID]),
        ("gc_fail_scope_malformed", "answer_fail_scope_malformed.md", 1,
         [linter.E_SCOPE_ANNOTATION_MALFORMED]),
        ("gc_fail_contradiction_one_sided", "answer_fail_contradiction.md", 1,
         [linter.E_UNIVERSAL_CONTRADICTS_SOURCE]),
        ("gc_pass_evidence_is_mixed", "answer_pass_mixed_evidence.md", 0, []),
        ("gc_pass_no_generalization", "answer_pass_no_generalization.md", 0, []),
    ]
    for name, answer, want_exit, want_codes in gc_cases:
        code, report, _ = run_linter(answer, kb=FIXTURE_KB_GC)
        if report is None:
            check(name, False, "linter stdout was not JSON")
            continue
        got_codes = error_codes(report)
        ok = code == want_exit and got_codes == sorted(want_codes)
        check(name, ok,
              "exit=%d (want %d), codes=%s (want %s)"
              % (code, want_exit, got_codes, sorted(want_codes)))

    # The V1.1 fixtures must behave identically under the V1.2 linter even
    # when the KB declares generalization classes: no new error may appear.
    for name, answer, no_kb, want_exit, want_codes in cli_cases:
        code, report, _ = run_linter(answer, no_kb_arm=no_kb, kb=FIXTURE_KB_GC)
        if report is None:
            check("v11_under_gc_kb_" + name, False, "linter stdout was not JSON")
            continue
        got_codes = error_codes(report)
        ok = code == want_exit and got_codes == sorted(want_codes)
        check("v11_under_gc_kb_" + name, ok,
              "exit=%d (want %d), codes=%s (want %s)"
              % (code, want_exit, got_codes, sorted(want_codes)))

    # Class metadata is parsed from the KB, never inferred from prose.
    with open(FIXTURE_KB_GC, encoding="utf-8") as fh:
        gc_classes = linter.parse_generalization_classes(fh.read())
    check("gc_classes_parsed",
          [c["class_id"] for c in gc_classes] == ["GC-90", "GC-91"],
          "parsed=%s" % [c["class_id"] for c in gc_classes])
    check("gc_class_directions_parsed",
          gc_classes[0]["outcome_positive"] == ["T9-03"]
          and gc_classes[0]["outcome_negative"] == ["T9-01", "T9-02"],
          "gc90=%s" % gc_classes[0])
    with open(FIXTURE_KB, encoding="utf-8") as fh:
        check("gc_no_classes_in_v11_fixture_kb",
              linter.parse_generalization_classes(fh.read()) == [],
              "V1.1 fixture KB must declare no generalization classes")

    # --- V1.2 unit tests: detector, exemptions, annotation grammar --------
    known = {"T9-01", "T9-02", "T9-03", "T9-04"}

    def gen_errors(text, ids=None, classes=()):
        entries = linter.check_generalizations(text, ids or known, list(classes))
        codes = []
        for entry in entries:
            codes.extend(e["code"] for e in entry["errors"])
        return sorted(set(codes))

    check("unit_universal_needs_corpus_marker",
          gen_errors("Widget nudges never lift purchases.") == [],
          "a universal without a corpus-scope marker must not fire")
    check("unit_corpus_marker_needs_universal",
          gen_errors("Two widget nudge cases exist in this corpus.") == [],
          "a corpus-scope marker without a universal must not fire")
    check("unit_corpus_universal_fires",
          gen_errors("Widget nudges have not lifted purchases in this corpus.")
          == [linter.E_UNQUALIFIED_UNIVERSAL])
    check("unit_no_direct_analogs_exempt",
          gen_errors("There are no direct analogs in this corpus.") == [],
          "the mandatory 'no direct analogs' line must never be flagged")
    check("unit_no_close_analog_exempt",
          gen_errors("I found no close analog in the knowledge base.") == [],
          "an analog-availability statement is a retrieval statement")
    check("unit_card_prose_not_scanned",
          gen_errors("Text.\n\n```yaml\nanalog:\n  transferable: >\n    "
                     "Nothing in this corpus ever did that.\n```\n") == [],
          "fenced blocks are not prose")
    check("unit_scope_annotation_clears",
          gen_errors("Widget nudges have not lifted purchases in this corpus "
                     "[scope: pull-down nudges; ids: T9-01; not covered: "
                     "push-up nudges].") == [])
    check("unit_scope_annotation_unknown_id",
          gen_errors("Widget nudges have not lifted purchases in this corpus "
                     "[scope: pull-down nudges; ids: T9-77; not covered: "
                     "push-up nudges].") == [linter.E_SCOPE_UNKNOWN_ID])
    check("unit_scope_annotation_missing_not_covered",
          gen_errors("Widget nudges have not lifted purchases in this corpus "
                     "[scope: pull-down nudges; ids: T9-01].")
          == [linter.E_SCOPE_ANNOTATION_MALFORMED])
    synthetic_class = [{
        "class_id": "GC-90",
        "label": "synthetic",
        "keywords": ["widget nudge"],
        "outcome_positive": ["T9-03"],
        "outcome_negative": ["T9-01"],
    }]
    check("unit_contradiction_fires_on_cited_counter",
          gen_errors("Widget nudges have not lifted purchases in this corpus "
                     "[scope: all widget nudges; ids: T9-01; not covered: "
                     "glow buttons]. T9-03 is quarantined.",
                     classes=synthetic_class)
          == [linter.E_UNIVERSAL_CONTRADICTS_SOURCE])
    check("unit_contradiction_cleared_by_mixed_phrase",
          gen_errors("Widget nudges have not lifted purchases in this corpus "
                     "[scope: all widget nudges; ids: T9-01; not covered: "
                     "glow buttons]. Here the evidence is mixed: T9-03 did.",
                     classes=synthetic_class) == [])
    check("unit_contradiction_cleared_by_scope_exclusion",
          gen_errors("Widget nudges have not lifted purchases in this corpus "
                     "[scope: pull-down nudges; ids: T9-01; not covered: "
                     "T9-03 and glow buttons]. T9-03 is quarantined.",
                     classes=synthetic_class) == [])
    check("unit_contradiction_needs_a_cited_counter",
          gen_errors("Widget nudges have not lifted purchases in this corpus "
                     "[scope: all widget nudges; ids: T9-01; not covered: "
                     "glow buttons].", classes=synthetic_class) == [])
    check("unit_positive_universal_uses_negative_direction",
          gen_errors("Every widget nudge in this corpus earned money "
                     "[scope: all widget nudges; ids: T9-03; not covered: "
                     "glow buttons]. T9-01 is quarantined.",
                     classes=synthetic_class)
          == [linter.E_UNIVERSAL_CONTRADICTS_SOURCE])

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

    real_classes = linter.parse_generalization_classes(kb_text)
    real_class_ids = [c["class_id"] for c in real_classes]
    check("real_kb_generalization_classes",
          real_class_ids == ["GC-01", "GC-02", "GC-03", "GC-04", "GC-05",
                             "GC-06"],
          "parsed=%s" % real_class_ids)
    check("real_kb_class_ids_exist",
          all(sid in ids
              for c in real_classes
              for sid in c["outcome_positive"] + c["outcome_negative"]),
          "every direction ID of §2.6 must be a real source ID")
    check("real_kb_class_directions_disjoint",
          all(not (set(c["outcome_positive"]) & set(c["outcome_negative"]))
              for c in real_classes),
          "a source may not point both ways inside one class")
    check("real_kb_classes_have_keywords",
          all(c["keywords"] for c in real_classes))

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
