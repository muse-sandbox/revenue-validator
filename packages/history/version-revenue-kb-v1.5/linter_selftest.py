#!/usr/bin/env python3
"""Deterministic selftest for linter.py (Revenue Validator V1.5, FLOW-629).

All fixtures are synthetic (invented sources T9-01…T9-04, pattern P-90,
invented generalization classes GC-90/GC-91, an invented experiment card, and
invented topics "widget nudges", "glow buttons" and "invented widget"); none
derive from any real or holdout experiment case. The V1.1/V1.2/V1.3/V1.4 fixture
answers and fixture_kb.md / fixture_kb_gc.md / fixture_patterns.md are
inherited byte-identically. Because V1.5 makes `## Findings` and
`## What you decide` mandatory and retires the section
`## What this experiment cannot show`, those inherited answers no longer pass
as written: the `v15_delta_*` blocks below assert that the ONLY codes they
acquire are `E_MISSING_FINDINGS` and `E_MISSING_DECISIONS` (on top of the
V1.3 delta for the older ones), that the two codes tied to the retired
section disappear and nothing else does, and that their warnings are
unchanged — that is the regression proof for this version. The `cc_*` block
still tests §2.8 itself, including the pair of runs that proves the linter
tells invention and transfer apart on the SAME answer, using only the
presence of the number in the knowledge base. The `fd_*` block tests §2.9.
Run:

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
FIXTURE_KB_NUM = os.path.join(FIX, "fixture_kb_num.md")
FIXTURE_PATTERNS = os.path.join(FIX, "fixture_patterns.md")
FIXTURE_CARD = "fixture_card.md"
FIXTURE_CARD_NO_NUMBERS = "fixture_card_no_numbers.md"
REAL_KB = os.path.join(HERE, "knowledge_base.md")
REAL_PATTERNS = os.path.join(HERE, "pattern_cards.md")

sys.path.insert(0, HERE)
import linter  # noqa: E402


def run_linter(answer, no_kb_arm=False, kb=FIXTURE_KB, patterns=FIXTURE_PATTERNS,
               card=None):
    cmd = [sys.executable, LINTER, os.path.join(FIX, answer),
           "--kb", kb, "--patterns", patterns]
    if card is not None:
        cmd.extend(["--card", os.path.join(FIX, card)])
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


def warning_codes(report):
    return sorted({w["code"] for w in report.get("warnings", [])})


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

    # --- Inherited V1.1/V1.2 fixture answers ------------------------------
    # These are the V1.1/V1.2 expectations, kept verbatim. Under V1.3 every
    # one of them additionally lacks the now-mandatory `## Product proposals`
    # section, so the assertion is a DELTA assertion: exit 1, and the code set
    # is exactly the old one plus E_MISSING_PRODUCT_PROPOSALS. Nothing else
    # may change — that is what proves V1.3 did not disturb V1.1/V1.2.
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
    # V1.5 replaces one mandatory section with two, so the delta an inherited
    # answer acquires is three codes: the V1.3 one and the two V1.5 ones.
    # Nothing else may change — that is the V1.1/V1.2/V1.3 regression proof.
    V13_DELTA = [linter.E_MISSING_PRODUCT_PROPOSALS]
    # What an inherited answer GAINS under V1.5: the two mandatory sections of
    # KB §2.9.
    V15_DELTA = [linter.E_MISSING_FINDINGS, linter.E_MISSING_DECISIONS,
                 linter.E_MISSING_MAIN_BANNER]
    # What a V1.4-era answer LOSES: the mandatory `[computed]` slot moved out
    # of `## What this experiment cannot show` and into the findings, so an
    # answer that still carries the old section is simply an answer without
    # findings, and the two codes tied to that section can no longer fire.
    V15_RETIRED = {linter.E_MISSING_COMPUTED_SLOT,
                   linter.E_MISSING_NO_COMPUTABLE_LIMIT}

    def delta_check(prefix, cases, kb=FIXTURE_KB, delta=None):
        delta = V13_DELTA + V15_DELTA if delta is None else delta
        for entry in cases:
            if len(entry) == 5:
                name, answer, no_kb, _v12_exit, v12_codes = entry
            else:
                name, answer, _v12_exit, v12_codes = entry
                no_kb = False
            code, report, _ = run_linter(answer, no_kb_arm=no_kb, kb=kb)
            if report is None:
                check(prefix + name, False, "linter stdout was not JSON")
                continue
            got_codes = error_codes(report)
            want = sorted(set(v12_codes) | set(delta))
            ok = code == 1 and got_codes == want
            check(prefix + name, ok,
                  "exit=%d (want 1), codes=%s (want %s)"
                  % (code, got_codes, want))

    delta_check("v15_delta_", cli_cases)

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
    delta_check("v15_delta_", gc_cases, kb=FIXTURE_KB_GC)

    # The inherited fixtures must acquire the same delta whether or not the KB
    # declares generalization classes.
    delta_check("v15_delta_under_gc_kb_", cli_cases, kb=FIXTURE_KB_GC)

    # --- V1.3 CLI tests: product proposals (KB §2.7) ----------------------
    # Under V1.5 these acquire exactly the two §2.9 codes, because none of
    # them carries either new mandatory section. Their warnings must be
    # unchanged: a V1.3 fixture emits no [computed] statement and no finding,
    # so the §2.8/§2.9 machinery has nothing else to say about it.
    pp_cases = [
        ("pp_pass_grounded", "answer_pp_pass_grounded.md", False, 0, [], []),
        ("pp_pass_abstention", "answer_pp_pass_abstention.md", False, 0, [], []),
        ("pp_fail_missing_section", "answer_pp_fail_missing_section.md",
         False, 1, [linter.E_MISSING_PRODUCT_PROPOSALS], []),
        ("pp_fail_untyped", "answer_pp_fail_untyped.md", False, 1,
         [linter.E_PROPOSAL_UNTYPED,
          linter.E_MISSING_NO_GROUNDED_PROPOSAL], []),
        ("pp_fail_ungrounded_claim", "answer_pp_fail_ungrounded_claim.md",
         False, 1, [linter.E_PROPOSAL_UNGROUNDED,
                    linter.E_MISSING_NO_GROUNDED_PROPOSAL], []),
        ("pp_fail_weak_grounding_l3", "answer_pp_fail_weak_grounding.md",
         False, 1, [linter.E_PROPOSAL_WEAK_GROUNDING,
                    linter.E_MISSING_NO_GROUNDED_PROPOSAL], []),
        ("pp_fail_unknown_id", "answer_pp_fail_unknown_id.md", False, 1,
         [linter.E_PROPOSAL_UNKNOWN_ID,
          linter.E_MISSING_NO_GROUNDED_PROPOSAL], []),
        ("pp_fail_id_in_ungrounded", "answer_pp_fail_id_in_ungrounded.md",
         False, 1, [linter.E_PROPOSAL_ID_IN_UNGROUNDED], []),
        ("pp_fail_missing_literal", "answer_pp_fail_missing_literal.md",
         False, 1, [linter.E_MISSING_NO_GROUNDED_PROPOSAL], []),
        ("pp_nokb_pass", "answer_pp_nokb_pass.md", True, 0, [], []),
        ("pp_nokb_fail_proposal", "answer_pp_nokb_fail_proposal.md", True, 1,
         [linter.E_PROPOSAL_IN_NO_KB_ARM], []),
        ("pp_pass_cap_warning", "answer_pp_pass_cap_warning.md", False, 0, [],
         [linter.W_PROPOSAL_CAP_EXCEEDED]),
        ("pp_pass_risk_without_proposal",
         "answer_pp_pass_risk_without_proposal.md", False, 0, [],
         [linter.W_RISK_SOURCE_WITHOUT_PROPOSAL]),
        ("pp_pass_duplicate_heading",
         "answer_pp_pass_duplicate_heading.md", False, 0, [], []),
    ]
    for name, answer, no_kb, _v13_exit, v13_codes, want_warnings in pp_cases:
        code, report, _ = run_linter(answer, no_kb_arm=no_kb)
        if report is None:
            check("v15_delta_" + name, False, "linter stdout was not JSON")
            continue
        got_codes = error_codes(report)
        got_warnings = warning_codes(report)
        want_codes = sorted(set(v13_codes) | set(V15_DELTA))
        ok = (code == 1 and got_codes == want_codes
              and got_warnings == sorted(want_warnings))
        check("v15_delta_" + name, ok,
              "exit=%d (want 1), codes=%s (want %s), warnings=%s (want %s)"
              % (code, got_codes, want_codes,
                 got_warnings, sorted(want_warnings)))

    # --- V1.4 CLI tests: computed claims (KB §2.8) ------------------------
    # The listed codes are the V1.4 expectations, kept verbatim. Under V1.5
    # each of these answers additionally lacks both §2.9 sections and can no
    # longer produce the two codes tied to the retired slot, so the assertion
    # is again a DELTA assertion: exit 1, codes = the V1.4 set minus
    # V15_RETIRED plus V15_DELTA, warnings unchanged. `--card` is the
    # synthetic experiment card.
    cc_cases = [
        ("cc_pass_computed", "answer_cc_pass_computed.md", False,
         FIXTURE_CARD, 0, [], []),
        ("cc_pass_ordinal_heading", "answer_cc_pass_ordinal_heading.md", False,
         FIXTURE_CARD, 0, [], []),
        ("cc_pass_abstention", "answer_cc_pass_abstention.md", False,
         FIXTURE_CARD_NO_NUMBERS, 0, [], []),
        ("cc_fail_fabricated_number", "answer_cc_fail_fabricated.md", False,
         FIXTURE_CARD, 1, [linter.E_COMPUTED_NUMBER_FABRICATED], []),
        ("cc_fail_no_operation", "answer_cc_fail_no_operation.md", False,
         FIXTURE_CARD, 1, [linter.E_COMPUTED_NO_OPERATION,
                           linter.E_COMPUTED_NUMBER_FABRICATED], []),
        ("cc_fail_source_id", "answer_cc_fail_source_id.md", False,
         FIXTURE_CARD, 1, [linter.E_COMPUTED_SOURCE_ID], []),
        ("cc_fail_arithmetic_mismatch",
         "answer_cc_fail_arithmetic_mismatch.md", False, FIXTURE_CARD, 1,
         [linter.E_COMPUTED_NUMBER_FABRICATED],
         [linter.W_COMPUTED_ARITHMETIC_MISMATCH]),
        ("cc_fail_missing_slot", "answer_cc_fail_missing_slot.md", False,
         FIXTURE_CARD, 1, [linter.E_MISSING_COMPUTED_SLOT], []),
        ("cc_fail_missing_literal", "answer_cc_fail_missing_literal.md", False,
         FIXTURE_CARD, 1, [linter.E_MISSING_NO_COMPUTABLE_LIMIT], []),
        ("cc_nokb_pass", "answer_cc_nokb_pass.md", True,
         FIXTURE_CARD, 0, [], []),
        ("cc_nokb_fail_invented_magnitudes",
         "answer_cc_nokb_fail_invented.md", True, FIXTURE_CARD, 1,
         [linter.E_COMPUTED_NUMBER_FABRICATED], []),
    ]
    for name, answer, no_kb, card, _v14_exit, v14_codes, want_warnings in cc_cases:
        code, report, _ = run_linter(answer, no_kb_arm=no_kb, card=card)
        if report is None:
            check("v15_delta_" + name, False, "linter stdout was not JSON")
            continue
        got_codes = error_codes(report)
        got_warnings = warning_codes(report)
        want = sorted((set(v14_codes) - V15_RETIRED) | set(V15_DELTA))
        ok = (code == 1 and got_codes == want
              and got_warnings == sorted(set(want_warnings)))
        check("v15_delta_" + name, ok,
              "exit=%d (want 1), codes=%s (want %s), warnings=%s (want %s)"
              % (code, got_codes, want,
                 got_warnings, sorted(set(want_warnings))))

    # The two failures §2.8 exists to separate must carry DIFFERENT codes on
    # the same answer shape: a number that is nowhere, and a number that is
    # in the knowledge base. Only the KB differs between these two runs.
    code_fab, report_fab, _ = run_linter("answer_cc_fail_kb_transfer.md",
                                         card=FIXTURE_CARD, kb=FIXTURE_KB)
    code_kb, report_kb, _ = run_linter("answer_cc_fail_kb_transfer.md",
                                       card=FIXTURE_CARD, kb=FIXTURE_KB_NUM)
    check("cc_fail_kb_transfer_is_diagnosed_as_transfer",
          code_kb == 1 and report_kb is not None
          and error_codes(report_kb) == sorted(
              {linter.E_COMPUTED_NUMBER_FROM_KB} | set(V15_DELTA)),
          "codes=%s" % (error_codes(report_kb) if report_kb else None))
    check("cc_same_number_absent_from_kb_is_fabricated",
          code_fab == 1 and report_fab is not None
          and error_codes(report_fab) == sorted(
              {linter.E_COMPUTED_NUMBER_FABRICATED} | set(V15_DELTA)),
          "the identical answer must be diagnosed as invention when the "
          "number is in no knowledge base; codes=%s"
          % (error_codes(report_fab) if report_fab else None))

    # Without a KNOWLEDGE CONTEXT there is nothing to transfer from, so the
    # same borrowed number can only be an invention.
    _, report_nokb, _ = run_linter("answer_cc_fail_kb_transfer.md",
                                   card=FIXTURE_CARD, kb=FIXTURE_KB_NUM,
                                   no_kb_arm=True)
    check("cc_nokb_arm_never_reports_a_transfer",
          report_nokb is not None
          and linter.E_COMPUTED_NUMBER_FROM_KB not in error_codes(report_nokb)
          and linter.E_COMPUTED_NUMBER_FABRICATED in error_codes(report_nokb),
          "codes=%s" % (error_codes(report_nokb) if report_nokb else None))

    # Without --card the provenance check cannot run; it must say so instead
    # of silently passing the answer.
    code_nocard, report_nocard, _ = run_linter("answer_cc_fail_fabricated.md")
    check("cc_missing_card_warns_instead_of_passing_silently",
          code_nocard == 1 and report_nocard is not None
          and warning_codes(report_nocard) == [linter.W_CARD_NOT_SUPPLIED]
          and linter.E_COMPUTED_NUMBER_FABRICATED
          not in error_codes(report_nocard),
          "codes=%s warnings=%s"
          % (error_codes(report_nocard) if report_nocard else None,
             warning_codes(report_nocard) if report_nocard else None))

    # A warning must never flip the verdict.
    _, warn_report, _ = run_linter("answer_pp_pass_cap_warning.md")
    check("pp_warning_does_not_fail_the_answer",
          warn_report is not None
          and linter.E_MISSING_FINDINGS in error_codes(warn_report)
          and warn_report["warnings"],
          "a reported warning must not be the reason an answer fails")
    _, mismatch_report, _ = run_linter("answer_cc_fail_arithmetic_mismatch.md",
                                       card=FIXTURE_CARD)
    check("cc_arithmetic_mismatch_is_a_warning_not_a_verdict",
          mismatch_report is not None
          and linter.W_COMPUTED_ARITHMETIC_MISMATCH
          in warning_codes(mismatch_report),
          "arithmetic that does not add up is reported, and the answer fails "
          "on the provenance of the stated number, not on the warning")

    # --- V1.5 CLI tests: findings (KB §2.9) -------------------------------
    # Every fixture below is a complete V1.5 answer, so the only codes it can
    # produce are §2.9 ones. All are synthetic: the invented card, the
    # invented widget topic, the synthetic source T9-01.
    fd_cases = [
        ("fd_pass", "answer_fd_pass.md", False, FIXTURE_CARD, 0, [], []),
        ("fd_pass_ordinal_heading", "answer_fd_pass_ordinal_heading.md",
         False, FIXTURE_CARD, 0, [], []),
        ("fd_pass_abstention", "answer_fd_pass_abstention.md", False,
         FIXTURE_CARD_NO_NUMBERS, 0, [], []),
        ("fd_nokb_pass", "answer_fd_nokb_pass.md", True, FIXTURE_CARD,
         0, [], []),
        ("fd_fail_paper_headline", "answer_fd_fail_paper_headline.md", False,
         FIXTURE_CARD, 1, [linter.E_FINDING_HEADLINE_PAPER], []),
        ("fd_fail_no_result_verb", "answer_fd_fail_no_result_verb.md", False,
         FIXTURE_CARD, 1, [linter.E_FINDING_HEADLINE_NO_RESULT_VERB], []),
        ("fd_fail_no_price", "answer_fd_fail_no_price.md", False,
         FIXTURE_CARD, 1, [linter.E_FINDING_NO_PRICE], []),
        ("fd_fail_price_unit_outside_list", "answer_fd_fail_price_unit.md",
         False, FIXTURE_CARD, 1, [linter.E_FINDING_PRICE_UNIT_UNKNOWN], []),
        ("fd_fail_no_mechanism", "answer_fd_fail_no_mechanism.md", False,
         FIXTURE_CARD, 1, [linter.E_FINDING_NO_MECHANISM,
                           linter.E_MISSING_NO_COMPUTABLE_LIMIT], []),
        ("fd_fail_mechanism_ungrounded",
         "answer_fd_fail_mechanism_ungrounded.md", False, FIXTURE_CARD, 1,
         [linter.E_FINDING_MECHANISM_UNGROUNDED,
          linter.E_MISSING_NO_COMPUTABLE_LIMIT], []),
        ("fd_fail_no_consequence", "answer_fd_fail_no_consequence.md", False,
         FIXTURE_CARD, 1, [linter.E_FINDING_NO_CONSEQUENCE], []),
        ("fd_fail_untyped", "answer_fd_fail_untyped.md", False,
         FIXTURE_CARD, 1, [linter.E_FINDING_UNTYPED], []),
        ("fd_fail_not_ranked_by_price", "answer_fd_fail_not_ranked.md", False,
         FIXTURE_CARD, 1, [linter.E_FINDINGS_NOT_RANKED], []),
        ("fd_fail_too_many_stops", "answer_fd_fail_too_many_stops.md", False,
         FIXTURE_CARD, 1, [linter.E_TOO_MANY_STOP_FINDINGS], []),
        ("fd_fail_missing_findings", "answer_fd_fail_missing_findings.md",
         False, FIXTURE_CARD, 1, [linter.E_MISSING_FINDINGS], []),
        ("fd_fail_missing_decisions", "answer_fd_fail_missing_decisions.md",
         False, FIXTURE_CARD, 1, [linter.E_MISSING_DECISIONS], []),
        ("fd_fail_decision_role_missing",
         "answer_fd_fail_decision_role_missing.md", False, FIXTURE_CARD, 1,
         [linter.E_DECISION_ROLE_MISSING], []),
        ("fd_fail_machine_field_in_main",
         "answer_fd_fail_machine_field_main.md", False, FIXTURE_CARD, 1,
         [linter.E_MACHINE_FIELD_IN_MAIN], []),
        ("fd_fail_analog_card_in_main",
         "answer_fd_fail_analog_card_in_main.md", False, FIXTURE_CARD, 1,
         [linter.E_MACHINE_FIELD_IN_MAIN], []),
        ("fd_warn_duplicate_across_sections", "answer_fd_warn_duplicate.md",
         False, FIXTURE_CARD, 0, [],
         [linter.W_DUPLICATE_ACROSS_SECTIONS]),
    ]
    for name, answer, no_kb, card, want_exit, want_codes, want_warnings in fd_cases:
        code, report, _ = run_linter(answer, no_kb_arm=no_kb, card=card)
        if report is None:
            check(name, False, "linter stdout was not JSON")
            continue
        got_codes = error_codes(report)
        got_warnings = warning_codes(report)
        ok = (code == want_exit and got_codes == sorted(set(want_codes))
              and got_warnings == sorted(set(want_warnings)))
        check(name, ok,
              "exit=%d (want %d), codes=%s (want %s), warnings=%s (want %s)"
              % (code, want_exit, got_codes, sorted(set(want_codes)),
                 got_warnings, sorted(set(want_warnings))))

    # The price of a finding is read from a closed list, and the rank is what
    # FD7 sorts by. A unit outside the list has no rank at all.
    for unit, rank in linter.PRICE_UNITS:
        check("fd_price_unit_" + unit.replace(" ", "_"),
              linter.price_rank(unit + " — because of X") == (unit, rank),
              "parsed=%s" % (linter.price_rank(unit),))
    check("fd_price_unit_outside_list_has_no_rank",
          linter.price_rank("reputational damage") == (None, None),
          "parsed=%s" % (linter.price_rank("reputational damage"),))
    check("fd_price_unit_survives_emphasis",
          linter.price_rank("**experiment slot** — spent again")[1] == 4,
          "markdown emphasis must not hide the unit")
    check("fd_price_ranks_are_strictly_ordered",
          [r for _, r in linter.PRICE_UNITS] == [5, 4, 3, 2, 1],
          "the closed list is ordered strongest first")

    # FD3 constrains the FIRST word only: a headline may say what will not
    # happen, it may not open by naming a hole in the paper.
    check("fd_forbidden_opener_lexicon_is_closed",
          "no" in linter.FORBIDDEN_HEADLINE_OPENERS
          and "there" in linter.FORBIDDEN_HEADLINE_OPENERS
          and "we" not in linter.FORBIDDEN_HEADLINE_OPENERS,
          "opener lexicon=%s" % (linter.FORBIDDEN_HEADLINE_OPENERS,))
    check("fd_result_verb_needs_a_word_boundary",
          any(r.search("the read gets worse") for r in linter.RESULT_VERB_RES)
          and not any(r.search("we target the beginners")
                      for r in linter.RESULT_VERB_RES),
          "'get' must not match inside 'target'")
    check("fd_result_verb_lexicon_excludes_descriptions",
          not any(r.search("the guardrail is underpowered")
                  for r in linter.RESULT_VERB_RES),
          "'is' carries a description and is deliberately absent")

    # The headline runs to the first terminator or slot marker, whichever
    # comes first, and markdown emphasis around it is ignored.
    bullet = ("- **[stop]** We lose the read. *Mechanism:* [computed] 1 + 1 = "
              "2. *Consequence:* x. *Price:* money — y.")
    m = linter.SEVERITY_RE.search(bullet)
    check("fd_headline_stops_at_the_first_terminator",
          linter.headline_of(bullet, m) == "We lose the read.",
          "parsed=%r" % linter.headline_of(bullet, m))
    unterminated = "- **[improve]** We pay more *Price:* money — y."
    m2 = linter.SEVERITY_RE.search(unterminated)
    check("fd_headline_stops_at_the_first_slot_marker",
          linter.headline_of(unterminated, m2) == "We pay more",
          "parsed=%r" % linter.headline_of(unterminated, m2))

    # The §2.9 sections are read from MAIN only, so appendix D never counts as
    # a findings section and an appendix card never trips FD8.
    doc = ("# MAIN\n\n## Findings\n\n- a\n\n# APPENDIX\n\n"
           "## D. Findings without a price\n\n- b\n")
    main = linter.extract_main(doc)
    check("fd_main_stops_at_the_appendix",
          "## D. Findings without a price" not in main and "- a" in main,
          "extracted=%r" % main)
    check("fd_appendix_d_is_not_a_findings_section",
          linter.extract_section(main, linter.FINDINGS_HEAD_RE) is not None
          and linter.extract_section(
              "## D. Findings without a price\n\n- b\n",
              linter.FINDINGS_HEAD_RE) is None,
          "the appendix heading must not match FINDINGS_HEAD_RE")

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

    # --- V1.3 unit tests: section extraction, bullets, grounding ----------
    check("unit_pp_abstention_literal_exempt_from_scope_scan",
          gen_errors("There is no grounded product proposal in this corpus.")
          == [],
          "the §2.7 abstention literal must not be read as a corpus universal")

    section_doc = ("## Product proposals\n\n- **[mechanic]** A — T9-01\n"
                   "  continues here\n- **[offer]** B — P-90\n\n"
                   "## Non-monetization effects to instrument\n\n- not a "
                   "proposal T9-02\n")
    section = linter.extract_section(section_doc,
                                     linter.PRODUCT_PROPOSALS_HEAD_RE)
    check("unit_pp_section_stops_at_next_heading",
          section is not None and "T9-02" not in section
          and "continues here" in section,
          "section=%r" % (section or "")[:120])
    check("unit_pp_numbered_heading_matches",
          linter.extract_section("## 3. Product proposals\n\n- x\n",
                                 linter.PRODUCT_PROPOSALS_HEAD_RE) is not None)
    check("unit_pp_absent_section_is_none",
          linter.extract_section("## Analogs\n\n- x\n",
                                 linter.PRODUCT_PROPOSALS_HEAD_RE) is None)
    merged = linter.extract_section(
        "## 3. Product proposals\n\n## Product proposals\n\n- **[offer]** x — "
        "P-90\n\n## Analogs\n\n- other T9-02\n",
        linter.PRODUCT_PROPOSALS_HEAD_RE)
    check("unit_pp_duplicate_headings_merge",
          merged is not None and "P-90" in merged and "T9-02" not in merged,
          "an empty first match must not hide the real section; merged=%r"
          % (merged or "")[:120])
    check("unit_pp_bullets_keep_continuations",
          linter.split_bullets(section) is not None
          and len(linter.split_bullets(section)) == 2
          and "continues here" in linter.split_bullets(section)[0],
          "bullets=%s" % linter.split_bullets(section))
    check("unit_pp_fenced_block_inside_section_is_stripped",
          "T9-04" not in (linter.extract_section(
              "## Product proposals\n\n```yaml\nanalog:\n  source: T9-04\n"
              "```\n\n- **[ungrounded]** x\n",
              linter.PRODUCT_PROPOSALS_HEAD_RE) or ""),
          "a fenced block may not smuggle a source ID into the section")

    pp_known = known | {"P-90"}

    def pp_codes(answer, no_kb=False, cards=()):
        _, errs, _ = linter.check_product_proposals(answer, pp_known, no_kb,
                                                    list(cards))
        return sorted({e["code"] for e in errs})

    l1_card = {"source_id": "T9-01", "computed_level": "L1"}
    l3_card = {"source_id": "T9-01", "computed_level": "L3"}
    pattern_only = "## Product proposals\n\n- **[offer]** x — P-90\n"
    check("unit_pp_pattern_id_grounds_without_a_card",
          pp_codes(pattern_only) == [],
          "a pattern ID grounds a proposal on its own")
    case_bullet = "## Product proposals\n\n- **[mechanic]** x — T9-01\n"
    check("unit_pp_case_id_needs_an_l1_l2_card",
          pp_codes(case_bullet, cards=[l1_card]) == []
          and pp_codes(case_bullet, cards=[l3_card])
          == sorted([linter.E_PROPOSAL_WEAK_GROUNDING,
                     linter.E_MISSING_NO_GROUNDED_PROPOSAL]),
          "L1/L2 grounds a case proposal, L3 does not")
    check("unit_pp_two_type_literals_is_untyped",
          linter.E_PROPOSAL_UNTYPED in pp_codes(
              "## Product proposals\n\n- **[mechanic] [offer]** x — P-90\n"),
          "exactly one type literal per bullet")
    check("unit_pp_type_must_be_on_the_first_line",
          linter.E_PROPOSAL_UNTYPED in pp_codes(
              "## Product proposals\n\n- x — P-90\n  **[offer]** buried\n"),
          "a type literal buried in a continuation line does not count")
    check("unit_pp_prose_only_section_needs_the_literal",
          pp_codes("## Product proposals\n\nno grounded product proposal.\n")
          == [] and
          pp_codes("## Product proposals\n\nNothing here.\n")
          == [linter.E_MISSING_NO_GROUNDED_PROPOSAL])

    # --- V1.4 unit tests: number scanning, arithmetic, provenance ---------
    check("unit_cc_source_id_is_not_a_number",
          linter.scan_numbers("Following T9-01 and P-90, nothing follows.")
          == [],
          "source IDs must not be read as data points")
    check("unit_cc_word_glued_digits_are_not_numbers",
          linter.scan_numbers("Instrument D1/D7 and refund 14d over Q3.") == [],
          "identifiers such as D1, 14d and Q3 are not magnitudes")
    check("unit_cc_decimal_comma_and_thousands",
          linter.scan_numbers("A 1,5 pp margin over 12,500 users.")
          == [1.5, 12500.0],
          "got=%s" % linter.scan_numbers("A 1,5 pp margin over 12,500 users."))

    ops = linter.shown_operations("64% × (1 − 25%) ≈ 48% of the arm")
    check("unit_cc_operation_is_parsed_and_verified",
          len(ops) == 1 and ops[0]["result"] == 48.0 and ops[0]["agrees"],
          "ops=%s" % ops)
    units = linter.shown_operations("pooled as 78% × 1.60 pp ≈ 1.25 pp here")
    check("unit_cc_units_between_operands_do_not_break_the_scan",
          len(units) == 1 and units[0]["result"] == 1.25 and units[0]["agrees"],
          "`pp` carries no value and must not terminate the run; ops=%s"
          % units)
    power = linter.shown_operations("needs (1.0 ÷ 0.5)² = 4 times the sample")
    check("unit_cc_squared_ratio_is_arithmetic",
          len(power) == 1 and power[0]["result"] == 4.0
          and power[0]["agrees"],
          "squaring a ratio is ordinary sizing arithmetic; ops=%s" % power)
    chained = linter.shown_operations(
        "2 × 38,147 = 76,294 exposures at ≈7,700/day is ≈10 days")
    check("unit_cc_chained_relations_keep_the_first_operation",
          any(op["result"] == 76294.0 and op["agrees"] for op in chained),
          "a second relation in the same run must not swallow the first; "
          "ops=%s" % chained)
    parenthesised = linter.shown_operations(
        "at (24,500 per variation ÷ 22 days ≈ 1,114/day) it holds")
    check("unit_cc_half_captured_bracket_still_parses",
          len(parenthesised) == 1 and parenthesised[0]["result"] == 1114.0
          and parenthesised[0]["agrees"],
          "a run that starts inside a bracket is still visible arithmetic; "
          "ops=%s" % parenthesised)
    check("unit_cc_em_dash_is_punctuation_not_minus",
          linter.shown_operations(
              "a loss of −1.60 pp — a null here is uninformative") == [],
          "an em dash between clauses must not be read as subtraction")
    check("unit_cc_range_is_not_an_operation",
          linter.shown_operations("the metric rises 8-18% here") == [],
          "a dash between two numbers is a range, not shown arithmetic")
    check("unit_cc_operation_without_a_result_is_not_shown",
          linter.shown_operations("64% × (1 − 25%) of the arm") == [],
          "CC2 needs both halves: the arithmetic and what it produces")
    bad = linter.shown_operations("64% × (1 − 25%) ≈ 61% of the arm")
    check("unit_cc_wrong_arithmetic_is_detected",
          len(bad) == 1 and bad[0]["agrees"] is False, "ops=%s" % bad)

    check("unit_cc_rounding_precision_is_respected",
          linter.value_matches(27.0, [26.8], 0)
          and not linter.value_matches(27.4, [26.8], 1),
          "a card's 26.8% may be written ~27%, but not 27.4%")
    check("unit_cc_sign_is_not_provenance",
          linter.value_matches(0.5, [-0.5], 1),
          "prose drops the sign of a margin; provenance is about the digits")
    check("unit_cc_share_and_percentage_are_one_number",
          linter.value_matches(0.78, [78.0], 2)
          and linter.value_matches(78.0, [0.78], 0),
          "dividing by a card's 78% as 0.78 is arithmetic, not invention")

    def cc_codes(block, card, no_kb=False, kb_numbers=(37.0,)):
        answer = ("## What this experiment cannot show\n\n" + block + "\n")
        _, errs, _ = linter.check_computed_claims(answer, card,
                                                 list(kb_numbers), no_kb)
        return sorted({e["code"] for e in errs})

    synthetic_card = "The arm reaches 64% of users and 25% see no content."
    check("unit_cc_derived_number_is_admissible",
          cc_codes("- [computed] 64% × (1 − 25%) ≈ 48% of the arm sees it.",
                   synthetic_card) == [],
          "the result of a shown operation is an admissible input")
    check("unit_cc_label_outside_the_slot_is_still_checked",
          linter.E_COMPUTED_NUMBER_FABRICATED in sorted({
              e["code"] for e in linter.check_computed_claims(
                  "## What this experiment cannot show\n\nno computable limit\n"
                  "\n## Top risks & failure modes\n\n- [computed] the metric "
                  "moves 91% because 64% × (1 − 25%) ≈ 48%.\n",
                  synthetic_card, [37.0], False)[1]}),
          "CC7: a [computed] statement anywhere in the answer is checked")

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
