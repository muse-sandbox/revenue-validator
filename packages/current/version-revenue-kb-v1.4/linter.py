#!/usr/bin/env python3
"""Deterministic answer linter for Revenue Validator V1.4 (FLOW-632).

Machine check of a validator answer against

  * the deterministic closeness model of knowledge_base.md §2.2 and the
    strict card format of §2.4 (Evidence Policy V1, level_computation +
    linter.hard_errors) — unchanged from V1.1;
  * the scope rules for corpus-level generalizations of §2.5, using the
    machine-readable generalization classes of §2.6 (V1.2);
  * the grounding rules for product proposals of §2.7 (V1.3); and
  * the provenance rules for `[computed]` claims of §2.8 (new in V1.4): every
    number inside a `[computed]` statement must occur in the experiment card
    under review or be the result of an operation shown in the same
    statement. A number that is in neither place is `FABRICATED`, unless it
    occurs in the KNOWLEDGE CONTEXT, in which case it is a magnitude transfer
    dressed as a calculation (`FROM_KB`). Checking this requires `--card`.

Usage:
    python3 linter.py <answer.md> --kb <knowledge_base.md> \
        --patterns <pattern_cards.md> [--card <experiment_card.md>] \
        [--no-kb-arm]

Exit code 0 = PASS (no hard errors), 1 = FAIL (answer invalid),
2 = usage/IO error. Warnings (`W_*`) are reported but never change the
verdict. A JSON report is printed to stdout. The linter is fully
deterministic: stdlib only, no network, no clock, no randomness, and it reads
ONLY the files passed as arguments. It never prints the full answer text —
only extracted cards, flagged-sentence excerpts (<= 160 chars) and errors.
"""

import argparse
import json
import re
import sys

AXES = [
    "flow_stage",
    "segment",
    "trigger_eligibility",
    "surface",
    "mechanism",
    "offer",
    "behavior",
    "metric",
    "money_chain",
    "guardrails",
]
MATCH3 = ("exact", "adjacent", "different")
MATCH2 = ("exact", "different")
LEVELS = ("L1", "L2", "L3")

# Enum-valued card fields outside `axes`.
ENUM_FIELDS = {
    "segment_monetization_state": MATCH2,
    "money_chain_link": MATCH2,
    "platform": MATCH3,
    "level": LEVELS,
}
REQUIRED_FIELDS = [
    "source",
    "axes",
    "segment_monetization_state",
    "money_chain_link",
    "platform",
    "level",
    "transferable",
    "not_transferable",
]

SOURCE_ID_RE = re.compile(r"\bT\d-\d{2}\b|\bP-\d{2}\b")
FENCE_RE = re.compile(r"^```")
SIDE_EFFECTS_RE = re.compile(r"non-monetization effects to instrument", re.IGNORECASE)
NO_DIRECT_ANALOGS_RE = re.compile(r"no direct analogs", re.IGNORECASE)

# Hard-error codes (generic; Evidence Policy V1 linter.hard_errors).
E_LEVEL_MISMATCH = "E_LEVEL_MISMATCH"          # claimed level != computed level
E_EMPTY_NOT_TRANSFERABLE = "E_EMPTY_NOT_TRANSFERABLE"
E_UNKNOWN_SOURCE_ID = "E_UNKNOWN_SOURCE_ID"    # source ID absent from KNOWLEDGE CONTEXT
E_CARD_PARSE = "E_CARD_PARSE"                  # card unparsable / missing fields or axes
E_MISSING_NO_DIRECT_ANALOGS = "E_MISSING_NO_DIRECT_ANALOGS"
E_MISSING_SIDE_EFFECTS = "E_MISSING_SIDE_EFFECTS"
E_CARD_IN_NO_KB_ARM = "E_CARD_IN_NO_KB_ARM"    # analog card emitted without a KB

# --- V1.2 hard-error codes (KB §2.5, generic; no case-specific tuning) -----
E_UNQUALIFIED_UNIVERSAL = "E_UNQUALIFIED_UNIVERSAL"        # G1/G2
E_SCOPE_ANNOTATION_MALFORMED = "E_SCOPE_ANNOTATION_MALFORMED"
E_SCOPE_UNKNOWN_ID = "E_SCOPE_UNKNOWN_ID"
E_UNIVERSAL_CONTRADICTS_SOURCE = "E_UNIVERSAL_CONTRADICTS_SOURCE"  # G3

# --- V1.3 hard-error codes (KB §2.7, generic; no case-specific tuning) -----
E_MISSING_PRODUCT_PROPOSALS = "E_MISSING_PRODUCT_PROPOSALS"      # PP1
E_PROPOSAL_UNTYPED = "E_PROPOSAL_UNTYPED"                        # PP2
E_PROPOSAL_UNGROUNDED = "E_PROPOSAL_UNGROUNDED"                  # PP3
E_PROPOSAL_UNKNOWN_ID = "E_PROPOSAL_UNKNOWN_ID"                  # PP3
E_PROPOSAL_WEAK_GROUNDING = "E_PROPOSAL_WEAK_GROUNDING"          # PP3 (L3-only)
E_PROPOSAL_ID_IN_UNGROUNDED = "E_PROPOSAL_ID_IN_UNGROUNDED"      # PP4
E_MISSING_NO_GROUNDED_PROPOSAL = "E_MISSING_NO_GROUNDED_PROPOSAL"  # PP4
E_PROPOSAL_IN_NO_KB_ARM = "E_PROPOSAL_IN_NO_KB_ARM"              # PP1/PP3

# --- V1.3 warning codes (reported, never change the verdict) ---------------
W_PROPOSAL_CAP_EXCEEDED = "W_PROPOSAL_CAP_EXCEEDED"              # PP2 (max 3)
W_RISK_SOURCE_WITHOUT_PROPOSAL = "W_RISK_SOURCE_WITHOUT_PROPOSAL"  # PP5

# --- V1.4 hard-error codes (KB §2.8, generic; no case-specific tuning) -----
E_MISSING_COMPUTED_SLOT = "E_MISSING_COMPUTED_SLOT"              # CC5
E_MISSING_NO_COMPUTABLE_LIMIT = "E_MISSING_NO_COMPUTABLE_LIMIT"  # CC5/CC6
E_COMPUTED_NUMBER_FABRICATED = "E_COMPUTED_NUMBER_FABRICATED"    # CC1
E_COMPUTED_NUMBER_FROM_KB = "E_COMPUTED_NUMBER_FROM_KB"          # CC1
E_COMPUTED_NO_OPERATION = "E_COMPUTED_NO_OPERATION"              # CC2
E_COMPUTED_SOURCE_ID = "E_COMPUTED_SOURCE_ID"                    # CC3

# --- V1.4 warning codes ----------------------------------------------------
W_CARD_NOT_SUPPLIED = "W_CARD_NOT_SUPPLIED"                      # CC1 unchecked
W_COMPUTED_ARITHMETIC_MISMATCH = "W_COMPUTED_ARITHMETIC_MISMATCH"  # CC2

# --- V1.2 lexicons (normative copy of knowledge_base.md §2.5) --------------
CORPUS_SCOPE_MARKERS = (
    "this corpus",
    "the corpus",
    "our corpus",
    "corpus-wide",
    "this knowledge base",
    "the knowledge base",
    "this evidence base",
    "the evidence base",
    "the knowledge context",
    "the reviewed cases",
    "the cases reviewed",
    "the cited cases",
    "the source cases",
    "past experiments",
    "prior experiments",
    "historical cases",
)
UNIVERSAL_MARKERS_NEGATIVE = (
    "never", "none", "nothing", "nowhere", "not a single", "at no point",
    "no case", "no experiment", "no source", "no iteration", "no evidence",
    "has not", "have not", "had not", "hasn't", "haven't", "does not",
    "do not", "did not", "doesn't", "don't", "is not", "are not", "was not",
    "were not", "cannot", "can't", "failed to", "fails to",
)
UNIVERSAL_MARKERS_POSITIVE = (
    "always", "every", "all", "any", "universally", "invariably",
    "without exception", "in all cases", "only ever",
)

# Retrieval statements about analog availability are not product
# generalizations (KB §2.5 exemption b).
NO_ANALOG_EXEMPT_RE = re.compile(r"\bno\s+(?:\w+\s+)?analogs?\b", re.IGNORECASE)
# The §2.7 abstention literal is a retrieval statement too, not a product
# generalization: it is removed before the §2.5 marker scan (KB §2.5 (b)).
NO_GROUNDED_PROPOSAL_RE = re.compile(
    r"no\s+grounded\s+product\s+proposal", re.IGNORECASE
)
SCOPE_ANNOTATION_RE = re.compile(r"\[scope:[^\]]*\]", re.IGNORECASE | re.DOTALL)
SCOPE_INNER_RE = re.compile(
    r"^\s*(?P<sub>[^;]+?)\s*;\s*ids\s*:\s*(?P<ids>[^;]+?)\s*;"
    r"\s*not\s+covered\s*:\s*(?P<nc>.+?)\s*$",
    re.IGNORECASE | re.DOTALL,
)
STRICT_SOURCE_ID_RE = re.compile(r"^(?:T\d-\d{2}|P-\d{2})$")
EVIDENCE_MIXED_RE = re.compile(r"evidence is mixed", re.IGNORECASE)
GEN_CLASS_HEAD_RE = re.compile(r"^generalization_class:\s*(\S+)\s*$")
GEN_CLASS_FIELD_RE = re.compile(r"^\s+([a-z_]+):\s*(.*)$")
BULLET_SPLIT_RE = re.compile(r"\n(?=\s*(?:[-*+]\s|\d+[.)]\s|#{1,6}\s))")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
EXCERPT_LEN = 160


def _marker_re(marker):
    return re.compile(r"(?<!\w)" + re.escape(marker) + r"(?!\w)", re.IGNORECASE)


CORPUS_MARKER_RES = tuple((m, _marker_re(m)) for m in CORPUS_SCOPE_MARKERS)
NEG_MARKER_RES = tuple((m, _marker_re(m)) for m in UNIVERSAL_MARKERS_NEGATIVE)
POS_MARKER_RES = tuple((m, _marker_re(m)) for m in UNIVERSAL_MARKERS_POSITIVE)


def read_text(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def extract_fenced_blocks(text):
    """Return the contents of all ``` fenced blocks, in document order."""
    blocks = []
    lines = text.splitlines()
    inside = False
    current = []
    for line in lines:
        if FENCE_RE.match(line.strip()):
            if inside:
                blocks.append("\n".join(current))
                current = []
                inside = False
            else:
                inside = True
            continue
        if inside:
            current.append(line)
    # An unterminated fence is treated as a block too (still deterministic).
    if inside and current:
        blocks.append("\n".join(current))
    return blocks


def is_analog_block(block):
    for line in block.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        return stripped == "analog:" or stripped.startswith("analog:")
    return False


def indent_of(line):
    return len(line) - len(line.lstrip(" "))


def parse_analog_card(block):
    """Parse one strict analog card (KB §2.4 subset of YAML).

    Returns (card_dict, errors). card_dict maps field -> scalar string or,
    for `axes`, a dict axis -> value-line. Prose fields (`transferable`,
    `not_transferable`, `sizing_prior`, `conflict`) collect their folded
    continuation lines.
    """
    errors = []
    card = {}
    lines = [ln for ln in block.splitlines()]
    # Locate the `analog:` root line.
    root_idx = None
    for i, ln in enumerate(lines):
        if ln.strip() == "analog:" or ln.strip().startswith("analog:"):
            root_idx = i
            break
    if root_idx is None:
        return None, ["no `analog:` root key"]

    i = root_idx + 1
    current_field = None       # field currently collecting prose continuation
    in_axes = False
    axes_indent = None
    field_indent = None
    while i < len(lines):
        raw = lines[i]
        i += 1
        if not raw.strip():
            continue
        ind = indent_of(raw)
        stripped = raw.strip()
        if field_indent is None and stripped:
            field_indent = ind  # indentation level of top card fields
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):(.*)$", stripped)
        if in_axes:
            if ind > (axes_indent if axes_indent is not None else 0) and m:
                axis = m.group(1)
                card["axes"][axis] = m.group(2).strip()
                continue
            in_axes = False  # fell out of the axes mapping
        if m and ind == field_indent:
            key = m.group(1)
            rest = m.group(2).strip()
            current_field = None
            if key == "axes":
                card["axes"] = {}
                in_axes = True
                axes_indent = ind
            else:
                card[key] = rest
                if rest in (">", "|", ">-", "|-", ""):
                    card[key] = ""
                    current_field = key
        elif current_field is not None and ind > field_indent:
            card[current_field] = (card[current_field] + " " + stripped).strip()
        elif m and field_indent is not None and ind > field_indent:
            # Nested mapping outside `axes` — tolerate but ignore.
            continue
        else:
            errors.append("unrecognized line in card: %r" % stripped[:80])
    return card, errors


def enum_value(raw):
    """First token of an enum-valued line; ` # rationale` comments allowed."""
    if raw is None:
        return None
    value = raw.split("#", 1)[0].strip()
    if not value:
        return None
    return value.split()[0]


def validate_card_structure(card, parse_errors):
    """Return list of E_CARD_PARSE reasons for missing/invalid fields."""
    reasons = list(parse_errors)
    for field in REQUIRED_FIELDS:
        if field not in card:
            reasons.append("missing required field: %s" % field)
    axes = card.get("axes")
    if isinstance(axes, dict):
        for axis in AXES:
            if axis not in axes:
                reasons.append("missing axis: %s" % axis)
            else:
                val = enum_value(axes[axis])
                if val not in MATCH3:
                    reasons.append(
                        "axis %s has invalid value %r (expected one of %s)"
                        % (axis, val, "/".join(MATCH3))
                    )
        for axis in sorted(axes):
            if axis not in AXES:
                reasons.append("unknown axis: %s" % axis)
    elif "axes" in card:
        reasons.append("`axes` is not a mapping")
    for field, allowed in ENUM_FIELDS.items():
        if field in card:
            val = enum_value(card[field])
            if val not in allowed:
                reasons.append(
                    "field %s has invalid value %r (expected one of %s)"
                    % (field, val, "/".join(allowed))
                )
    return reasons


def compute_level(card):
    """Deterministic level per KB §2.2 (L1 first, then L2 branches, else L3)."""
    axes = {a: enum_value(v) for a, v in card["axes"].items()}
    sms = enum_value(card["segment_monetization_state"])
    mcl = enum_value(card["money_chain_link"])
    platform = enum_value(card["platform"])

    l1 = (
        axes["mechanism"] == "exact"
        and axes["flow_stage"] == "exact"
        and axes["surface"] in ("exact", "adjacent")
        and sms == "exact"
        and mcl == "exact"
        and platform in ("exact", "adjacent")   # R1
    )
    if l1:
        return "L1"

    branch_a = axes["mechanism"] == "exact" and (
        axes["surface"] == "different" or axes["flow_stage"] == "different"
    )
    branch_b = (
        axes["surface"] == "exact"
        and axes["flow_stage"] == "exact"
        and axes["mechanism"] == "different"
    )
    branch_c = (
        axes["mechanism"] == "exact"
        and axes["flow_stage"] == "exact"
        and axes["surface"] in ("exact", "adjacent")
        and mcl == "exact"                      # R4
        and (
            sms == "different"                  # R2
            or axes["segment"] == "different"
            or platform == "different"
        )
    )
    if branch_a or branch_b or branch_c:
        return "L2"
    return "L3"


def collect_known_ids(kb_text, patterns_text):
    ids = set(SOURCE_ID_RE.findall(kb_text))
    ids.update(SOURCE_ID_RE.findall(patterns_text))
    return ids


# ---------------------------------------------------------------------------
# V1.2: corpus-level generalizations (KB §2.5) over the classes of KB §2.6
# ---------------------------------------------------------------------------

def parse_generalization_classes(kb_text):
    """Parse the §2.6 blocks. Returns a list of dicts, in document order.

    Grammar (inside a fenced block, exactly as written in the KB):

        generalization_class: GC-01
          label: <free text>
          keywords: <comma-separated substrings>
          outcome_positive: <comma-separated source IDs>
          outcome_negative: <comma-separated source IDs>

    A KB without such blocks simply yields no classes and the contradiction
    check never fires (this is what keeps V1.1 fixtures behaving as in V1.1).
    """
    classes = []
    current = None
    for block in extract_fenced_blocks(kb_text):
        for line in block.splitlines():
            head = GEN_CLASS_HEAD_RE.match(line.strip()) if line.strip() else None
            if head and line[:1] not in (" ", "\t"):
                current = {
                    "class_id": head.group(1),
                    "label": "",
                    "keywords": [],
                    "outcome_positive": [],
                    "outcome_negative": [],
                }
                classes.append(current)
                continue
            if current is None:
                continue
            field = GEN_CLASS_FIELD_RE.match(line)
            if not field:
                if line.strip():
                    current = None      # block ended / unrelated content
                continue
            key, value = field.group(1), field.group(2).strip()
            if key == "label":
                current["label"] = value
            elif key == "keywords":
                current["keywords"] = [
                    k.strip().lower() for k in value.split(",") if k.strip()
                ]
            elif key in ("outcome_positive", "outcome_negative"):
                current[key] = [k.strip() for k in value.split(",") if k.strip()]
        current = None
    return classes


def strip_fenced_blocks(text):
    """Answer prose: every fenced block replaced by a paragraph break."""
    out = []
    inside = False
    for line in text.splitlines():
        if FENCE_RE.match(line.strip()):
            inside = not inside
            out.append("")
            continue
        out.append("" if inside else line)
    return "\n".join(out)


def normalize_scan_text(text):
    """Whitespace-collapsed, ASCII-apostrophe copy used for marker matching."""
    return " ".join(text.replace("’", "'").split())


def split_paragraphs(prose):
    return [p for p in re.split(r"\n\s*\n", prose) if p.strip()]


def split_sentences(paragraph):
    """Deterministic sentence split; `[scope: …]` annotations are protected."""
    annotations = SCOPE_ANNOTATION_RE.findall(paragraph)
    protected = paragraph
    for i, ann in enumerate(annotations):
        protected = protected.replace(ann, "\x00A%d\x00" % i, 1)
    sentences = []
    for chunk in BULLET_SPLIT_RE.split(protected):
        for sentence in SENTENCE_SPLIT_RE.split(chunk):
            if sentence.strip():
                sentences.append(sentence)
    restored = []
    for sentence in sentences:
        for i, ann in enumerate(annotations):
            sentence = sentence.replace("\x00A%d\x00" % i, ann)
        restored.append(sentence)
    return restored


def matched_markers(scan_text, marker_res):
    return [m for m, rx in marker_res if rx.search(scan_text)]


def validate_scope_annotation(raw, known_ids):
    """Return (parsed_or_None, errors) for one `[scope: …]` annotation."""
    inner = raw[raw.index(":") + 1:-1]
    match = SCOPE_INNER_RE.match(inner)
    if not match:
        return None, [{
            "code": E_SCOPE_ANNOTATION_MALFORMED,
            "detail": "expected `[scope: <sub-class>; ids: <ID>[, <ID>…]; "
                      "not covered: <text>]`, got %r"
                      % normalize_scan_text(raw)[:EXCERPT_LEN],
        }]
    errors = []
    sub = normalize_scan_text(match.group("sub"))
    not_covered = normalize_scan_text(match.group("nc"))
    ids = [i.strip() for i in match.group("ids").split(",") if i.strip()]
    if not sub:
        errors.append({"code": E_SCOPE_ANNOTATION_MALFORMED,
                       "detail": "empty <sub-class>"})
    if not not_covered:
        errors.append({"code": E_SCOPE_ANNOTATION_MALFORMED,
                       "detail": "empty `not covered:` part"})
    if not ids:
        errors.append({"code": E_SCOPE_ANNOTATION_MALFORMED,
                       "detail": "empty `ids:` list"})
    for source_id in ids:
        if not STRICT_SOURCE_ID_RE.match(source_id):
            errors.append({
                "code": E_SCOPE_ANNOTATION_MALFORMED,
                "detail": "%r is not a source ID (T*-** / P-**)" % source_id,
            })
        elif source_id not in known_ids:
            errors.append({
                "code": E_SCOPE_UNKNOWN_ID,
                "detail": "scope ID %s does not exist in KNOWLEDGE CONTEXT"
                          % source_id,
            })
    parsed = {
        "sub_class": sub,
        "ids": ids,
        "not_covered": not_covered,
        "excluded_ids": sorted(set(SOURCE_ID_RE.findall(match.group("nc")))),
    }
    return parsed, errors


def check_generalizations(answer_text, known_ids, gen_classes):
    """KB §2.5 G1–G3. Returns a list of report entries (each with `errors`)."""
    entries = []
    cited_ids = set(SOURCE_ID_RE.findall(answer_text))
    prose = strip_fenced_blocks(answer_text)
    index = 0
    for p_index, paragraph in enumerate(split_paragraphs(prose)):
        paragraph_has_mixed = bool(
            EVIDENCE_MIXED_RE.search(normalize_scan_text(paragraph))
        )
        for sentence in split_sentences(paragraph):
            annotations_raw = SCOPE_ANNOTATION_RE.findall(sentence)
            errors = []
            parsed_annotations = []
            for raw in annotations_raw:
                parsed, ann_errors = validate_scope_annotation(raw, known_ids)
                errors.extend(ann_errors)
                if parsed is not None:
                    parsed_annotations.append(parsed)
            # Detection runs on the sentence WITHOUT annotations and without
            # the analog-availability exemption (KB §2.5 exemptions b, c).
            scan_source = SCOPE_ANNOTATION_RE.sub(" ", sentence)
            scan_source = NO_ANALOG_EXEMPT_RE.sub(" ", scan_source)
            scan_source = NO_GROUNDED_PROPOSAL_RE.sub(" ", scan_source)
            scan_text = normalize_scan_text(scan_source)
            corpus_hits = matched_markers(scan_text, CORPUS_MARKER_RES)
            neg_hits = matched_markers(scan_text, NEG_MARKER_RES)
            pos_hits = matched_markers(scan_text, POS_MARKER_RES)
            flagged = bool(corpus_hits) and bool(neg_hits or pos_hits)
            if not flagged:
                if errors:      # a voluntary annotation must still be valid
                    index += 1
                    entries.append({
                        "index": index,
                        "paragraph": p_index + 1,
                        "flagged": False,
                        "polarity": None,
                        "classes": [],
                        "annotations": len(annotations_raw),
                        "excerpt": scan_text[:EXCERPT_LEN],
                        "errors": errors,
                    })
                continue
            index += 1
            polarity = "negative" if neg_hits else "positive"
            if not annotations_raw:
                errors.append({
                    "code": E_UNQUALIFIED_UNIVERSAL,
                    "detail": "corpus-scoped universal without a [scope: …] "
                              "annotation (corpus markers %s; universal "
                              "markers %s)"
                              % (sorted(corpus_hits),
                                 sorted(neg_hits + pos_hits)),
                })
            excluded = set()
            for parsed in parsed_annotations:
                excluded.update(parsed["excluded_ids"])
            hit_classes = []
            for gen_class in gen_classes:
                if not any(k in scan_text.lower() for k in gen_class["keywords"]):
                    continue
                counter_field = ("outcome_positive" if polarity == "negative"
                                 else "outcome_negative")
                counters = sorted(
                    set(gen_class[counter_field]) & cited_ids - excluded
                )
                hit_classes.append({
                    "class_id": gen_class["class_id"],
                    "counter_ids": counters,
                })
                if counters and not paragraph_has_mixed:
                    errors.append({
                        "code": E_UNIVERSAL_CONTRADICTS_SOURCE,
                        "detail": "%s universal over class %s, but the answer "
                                  "cites opposite-direction source(s) %s that "
                                  "the declared scope does not exclude; the "
                                  "paragraph must contain the literal "
                                  "'evidence is mixed'"
                                  % (polarity, gen_class["class_id"],
                                     ", ".join(counters)),
                    })
            entries.append({
                "index": index,
                "paragraph": p_index + 1,
                "flagged": True,
                "polarity": polarity,
                "classes": hit_classes,
                "annotations": len(annotations_raw),
                "excerpt": scan_text[:EXCERPT_LEN],
                "errors": errors,
            })
    return entries


# ---------------------------------------------------------------------------
# V1.3: product proposals (KB §2.7)
# ---------------------------------------------------------------------------

HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s")
PRODUCT_PROPOSALS_HEAD_RE = re.compile(
    r"^\s{0,3}#{1,6}\s*(?:\d+[.)]\s*)?product\s+proposals\s*:?\s*$",
    re.IGNORECASE,
)
RISKS_HEAD_RE = re.compile(
    r"^\s{0,3}#{1,6}\s*(?:\d+[.)]\s*)?top\s+risks\b.*$", re.IGNORECASE
)
BULLET_RE = re.compile(r"^\s{0,3}(?:[-*+]|\d+[.)])\s+")
PROPOSAL_TYPES = ("mechanic", "segment", "offer", "ungrounded")
PROPOSAL_TYPE_RE = re.compile(
    r"\[\s*(%s)\s*\]" % "|".join(PROPOSAL_TYPES), re.IGNORECASE
)
GROUNDED_TYPES = ("mechanic", "segment", "offer")
MAX_PROPOSALS = 3


def extract_section(answer_text, head_re):
    """Text of EVERY section whose heading matches `head_re`, concatenated.

    Each section runs from the line after its heading to the next markdown
    heading of any level (or end of file). All matches are merged, so an
    answer that emits the heading twice (e.g. an ordinal `## 3. Product
    proposals` immediately followed by `## Product proposals`) is parsed as
    one section instead of yielding an empty first match. Returns None when
    the heading is absent. Fenced blocks inside the section are stripped, so
    a stray code block can neither hide nor fabricate a source ID.
    """
    lines = answer_text.splitlines()
    parts = []
    for i, line in enumerate(lines):
        if not head_re.match(line):
            continue
        end = len(lines)
        for j in range(i + 1, len(lines)):
            if HEADING_RE.match(lines[j]):
                end = j
                break
        parts.append("\n".join(lines[i + 1:end]))
    if not parts:
        return None
    return strip_fenced_blocks("\n\n".join(parts))


def split_bullets(section_text):
    """Top-level bullets of a section, each with its continuation lines."""
    bullets = []
    current = None
    for line in section_text.splitlines():
        if BULLET_RE.match(line):
            if current is not None:
                bullets.append(current)
            current = [line]
        elif current is not None:
            if line.strip():
                current.append(line)
            else:
                bullets.append(current)
                current = None
    if current is not None:
        bullets.append(current)
    return ["\n".join(b) for b in bullets]


def check_product_proposals(answer_text, known_ids, no_kb_arm, cards):
    """KB §2.7 PP1–PP5. Returns (report_dict, errors, warnings)."""
    errors = []
    warnings = []
    report = {
        "section_present": False,
        "bullets": [],
        "grounded_count": 0,
        "abstention_literal": False,
    }

    section = extract_section(answer_text, PRODUCT_PROPOSALS_HEAD_RE)
    if section is None:
        errors.append({
            "code": E_MISSING_PRODUCT_PROPOSALS,
            "detail": "mandatory section 'Product proposals' is absent "
                      "(KB §2.7 PP1)",
        })
        return report, errors, warnings

    report["section_present"] = True
    report["abstention_literal"] = bool(NO_GROUNDED_PROPOSAL_RE.search(section))

    # A case ID grounds a product proposal only through an L1/L2 card of THIS
    # answer (KB §2.7 PP3); pattern IDs ground on their own.
    l1l2_sources = {
        card["source_id"]
        for card in cards
        if card.get("source_id") and card.get("computed_level") in ("L1", "L2")
    }

    bullets = split_bullets(section)
    if len(bullets) > MAX_PROPOSALS:
        warnings.append({
            "code": W_PROPOSAL_CAP_EXCEEDED,
            "detail": "%d proposal bullets, at most %d allowed (KB §2.7 PP2)"
                      % (len(bullets), MAX_PROPOSALS),
        })

    proposal_ids = set()
    for index, bullet in enumerate(bullets, start=1):
        first_line = bullet.splitlines()[0]
        types = [t.lower() for t in PROPOSAL_TYPE_RE.findall(first_line)]
        ids = sorted(set(SOURCE_ID_RE.findall(bullet)))
        entry = {
            "index": index,
            "type": types[0] if len(types) == 1 else None,
            "ids": ids,
            "grounded": False,
            "errors": [],
            "excerpt": normalize_scan_text(first_line)[:EXCERPT_LEN],
        }
        if len(types) != 1:
            entry["errors"].append({
                "code": E_PROPOSAL_UNTYPED,
                "detail": "bullet carries %d type literals, exactly one of "
                          "%s is required on its first line (KB §2.7 PP2)"
                          % (len(types),
                             "/".join("[%s]" % t for t in PROPOSAL_TYPES)),
            })
            report["bullets"].append(entry)
            errors.extend(entry["errors"])
            continue

        kind = types[0]
        if kind == "ungrounded":
            if ids:
                entry["errors"].append({
                    "code": E_PROPOSAL_ID_IN_UNGROUNDED,
                    "detail": "[ungrounded] bullet cites source ID(s) %s; an "
                              "abstention carries none (KB §2.7 PP4)"
                              % ", ".join(ids),
                })
            report["bullets"].append(entry)
            errors.extend(entry["errors"])
            continue

        if no_kb_arm:
            entry["errors"].append({
                "code": E_PROPOSAL_IN_NO_KB_ARM,
                "detail": "[%s] proposal in an arm without a KNOWLEDGE "
                          "CONTEXT: nothing can ground it (KB §2.7 PP1)" % kind,
            })
            report["bullets"].append(entry)
            errors.extend(entry["errors"])
            continue

        if not ids:
            entry["errors"].append({
                "code": E_PROPOSAL_UNGROUNDED,
                "detail": "[%s] proposal cites no source ID (KB §2.7 PP3)"
                          % kind,
            })
        qualifying = []
        for source_id in ids:
            if source_id not in known_ids:
                entry["errors"].append({
                    "code": E_PROPOSAL_UNKNOWN_ID,
                    "detail": "proposal cites %s, which does not exist in the "
                              "KNOWLEDGE CONTEXT" % source_id,
                })
            elif source_id.startswith("P-") or source_id in l1l2_sources:
                qualifying.append(source_id)
            else:
                entry["errors"].append({
                    "code": E_PROPOSAL_WEAK_GROUNDING,
                    "detail": "proposal cites case %s, which is not the source "
                              "of an L1/L2 analog card in this answer; an L3 or "
                              "uncarded case grounds no product proposal "
                              "(KB §2.7 PP3)" % source_id,
                })
        if qualifying and not entry["errors"]:
            entry["grounded"] = True
            report["grounded_count"] += 1
            proposal_ids.update(qualifying)
        report["bullets"].append(entry)
        errors.extend(entry["errors"])

    if report["grounded_count"] == 0 and not report["abstention_literal"]:
        errors.append({
            "code": E_MISSING_NO_GROUNDED_PROPOSAL,
            "detail": "no grounded product proposal was made, but the "
                      "mandatory literal 'no grounded product proposal' is "
                      "absent from the section (KB §2.7 PP4)",
        })

    # PP5 — an L1/L2 case used only as a warning is usually a missed proposal.
    # Reported, never a failure. Pattern IDs are deliberately excluded: the
    # measurement/design patterns legitimately appear in risks alone.
    risks = extract_section(answer_text, RISKS_HEAD_RE)
    if risks and not no_kb_arm:
        risk_ids = set(SOURCE_ID_RE.findall(risks))
        missed = sorted((risk_ids & l1l2_sources) - proposal_ids)
        if missed:
            warnings.append({
                "code": W_RISK_SOURCE_WITHOUT_PROPOSAL,
                "detail": "source(s) %s ground a risk but no product proposal "
                          "(KB §2.7 PP5)" % ", ".join(missed),
            })
    return report, errors, warnings


# ---------------------------------------------------------------------------
# V1.4: computed claims (KB §2.8)
# ---------------------------------------------------------------------------

COMPUTED_SLOT_HEAD_RE = re.compile(
    r"^\s{0,3}#{1,6}\s*(?:\d+[.)]\s*)?what\s+this\s+experiment\s+cannot\s+show"
    r"\s*:?\s*$",
    re.IGNORECASE,
)
COMPUTED_LABEL_RE = re.compile(r"\[\s*computed\s*\]", re.IGNORECASE)
NO_COMPUTABLE_LIMIT_RE = re.compile(r"no\s+computable\s+limit", re.IGNORECASE)

# Structural constants used to build complements and percentages. They are
# arithmetic scaffolding, not data, so they need no provenance (KB §2.8 CC1).
FREE_CONSTANTS = (0.0, 1.0, 100.0)

# Unicode operators and relations normalised before any numeric scan. En and
# em dashes are deliberately NOT mapped to minus: in prose they are
# punctuation far more often than subtraction, and mapping them invents
# operations nobody wrote.
_OPERATOR_MAP = {
    "−": "-",                       # U+2212 minus
    "×": "*", "·": "*", "⋅": "*",   # ×, ·, ⋅
    "÷": "/",
    "≈": "=", "≡": "=", "→": "=",   # ≈, ≡, →
    " ": " ", " ": " ", " ": " ",   # nbsp, thin spaces
}
_ARROW_RE = re.compile(r"->")
# Units that sit BETWEEN the operands of an expression (`1.60 pp ≈ 1.25 pp`).
# They carry no value, so they are removed before the arithmetic scan; any
# other word still terminates the run.
_UNIT_RE = re.compile(r"\b(?:pp|p\.p\.|ppt|bps?)\b", re.IGNORECASE)
_SUPERSCRIPTS = {"²": "^2", "³": "^3"}
# Up to three words naming what a number counts (`24,500 per variation ÷ 22
# days ≈ 1,114/day`) sit between operands without carrying value. A longer run
# of words is prose, and prose terminates the expression.
_INLINE_UNIT_WORDS_RE = re.compile(
    r"(?<=[\d%)])\s+(?:[A-Za-z][A-Za-z.]{0,11}\s+){1,3}(?=[-+*/^=(]|\d)"
)
NUMBER_TOKEN_RE = re.compile(r"[-+]?\d+(?:\.\d+)?")
# A number in prose: not glued to a word character on either side, so `14d`,
# `Q3` and version strings do not become data points.
PROSE_NUMBER_RE = re.compile(r"(?<![\w.])[-+]?\d+(?:\.\d+)?(?![\w])")
# Maximal run of characters that can belong to an arithmetic expression.
ARITH_RUN_RE = re.compile(r"[0-9%()+\-*/^=. ]{3,}")
COMPUTED_TOLERANCE_REL = 0.02


def normalize_math(text):
    """ASCII-normalised copy: unicode operators, arrows and decimal commas."""
    for src, dst in _OPERATOR_MAP.items():
        text = text.replace(src, dst)
    text = _ARROW_RE.sub("=", text)
    for src, dst in _SUPERSCRIPTS.items():
        text = text.replace(src, dst)
    text = _UNIT_RE.sub(" ", text)
    text = _INLINE_UNIT_WORDS_RE.sub(" ", text)
    # `78% x (1 - 27%)`: a spaced `x` between two operands is multiplication.
    text = re.sub(r"(?<=[\d%)])\s+x\s+(?=[\d(])", " * ", text)
    # `1,5` is a decimal comma; `1,500` is a thousands separator.
    text = re.sub(r"(?<=\d),(?=\d\d?(?!\d))", ".", text)
    text = re.sub(r"(?<=\d),(?=\d{3}(?!\d))", "", text)
    return text


def scan_numbers(text):
    """Numeric values appearing in prose, source IDs removed first."""
    cleaned = SOURCE_ID_RE.sub(" ", normalize_math(text))
    values = []
    for raw in PROSE_NUMBER_RE.findall(cleaned):
        try:
            values.append(float(raw))
        except ValueError:
            continue
    return values


def decimals_of(raw):
    return len(raw.split(".")[1]) if "." in raw else 0


def value_matches(value, pool, decimals):
    """Is `value` one of `pool`, at the precision the answer actually wrote?

    Three tolerances, none of which is about the size of the number:

    * precision — the card's `26.8%` may be written `~27%`, not `27.4%`;
    * sign — prose routinely drops the minus of a margin (`a 0.5 pp
      guardrail` for a card's `-0.5 pp`);
    * scale by 100 — a share and a percentage are the same number written two
      ways, and an answer that computes with `0.78` where the card says `78%`
      is doing arithmetic, not inventing a figure.

    All three are deliberate: provenance is about where the digits came from,
    not about the notation the answer chose for them.
    """
    for candidate in pool:
        for scaled in (candidate, candidate * 100.0, candidate / 100.0):
            for a, b in ((value, scaled), (abs(value), abs(scaled))):
                if a == b:
                    return True
                if round(b, decimals) == a:
                    return True
    return False


class _ExprParser:
    """Recursive-descent parser for `+ - * / ( )` over decimal numbers.

    Two readings are produced for every expression: one where `%` means
    "divide by 100" and one where `%` is only a unit marker. The caller
    accepts a stated result that matches either reading, so an answer is not
    failed for writing `78% x (1 - 27%) ~ 57%` instead of `0.5694`.
    """

    def __init__(self, text, percent_divides):
        self.tokens = self._tokenize(text)
        self.pos = 0
        self.percent_divides = percent_divides
        self.operators = 0

    @staticmethod
    def _tokenize(text):
        tokens = []
        i = 0
        while i < len(text):
            ch = text[i]
            if ch.isspace():
                i += 1
                continue
            if ch.isdigit() or (ch == "." and i + 1 < len(text)
                                and text[i + 1].isdigit()):
                match = NUMBER_TOKEN_RE.match(text, i)
                if match is None:
                    return None
                tokens.append(("num", match.group(0)))
                i = match.end()
                continue
            if ch in "+-*/^()%":
                tokens.append((ch, ch))
                i += 1
                continue
            return None
        return tokens

    def parse(self):
        if not self.tokens:
            return None
        try:
            value = self._expression()
        except (ValueError, ZeroDivisionError):
            return None
        if self.pos != len(self.tokens):
            return None
        return value

    def _peek(self):
        return self.tokens[self.pos][0] if self.pos < len(self.tokens) else None

    def _expression(self):
        value = self._term()
        while self._peek() in ("+", "-"):
            op = self.tokens[self.pos][0]
            self.pos += 1
            self.operators += 1
            right = self._term()
            value = value + right if op == "+" else value - right
        return value

    def _term(self):
        value = self._power()
        while self._peek() in ("*", "/"):
            op = self.tokens[self.pos][0]
            self.pos += 1
            self.operators += 1
            right = self._power()
            if op == "*":
                value = value * right
            else:
                if right == 0:
                    raise ZeroDivisionError
                value = value / right
        return value

    def _power(self):
        """`(1.0 / 0.5)² = 4`: squaring a ratio is ordinary sizing arithmetic."""
        value = self._factor()
        if self._peek() == "^":
            self.pos += 1
            self.operators += 1
            exponent = self._power()
            if abs(exponent) > 8 or abs(value) > 1e6:
                raise ValueError("exponent out of range")
            value = value ** exponent
        return value

    def _factor(self):
        kind = self._peek()
        if kind in ("+", "-"):
            self.pos += 1
            operand = self._factor()
            return operand if kind == "+" else -operand
        if kind == "(":
            self.pos += 1
            value = self._expression()
            if self._peek() != ")":
                raise ValueError("unbalanced parentheses")
            self.pos += 1
            return self._apply_percent(value)
        if kind == "num":
            raw = self.tokens[self.pos][1]
            self.pos += 1
            return self._apply_percent(float(raw))
        raise ValueError("unexpected token")

    def _apply_percent(self, value):
        if self._peek() == "%":
            self.pos += 1
            if self.percent_divides:
                return value / 100.0
        return value


def balance_parentheses(text):
    """Drop parentheses the run captured only one half of.

    A scan over prose regularly starts inside a bracket (`(24,500 / 22 ...`)
    or ends past one. The arithmetic is still fully visible; only the
    punctuation is lopsided.
    """
    while text.count("(") > text.count(")"):
        text = text.replace("(", "", 1)
    while text.count(")") > text.count("("):
        head, _, tail = text.rpartition(")")
        text = head + tail
    return text


def evaluate_expression(text):
    """(values, operator_count) for both percent readings of `text`."""
    text = balance_parentheses(text)
    values = []
    operators = 0
    for percent_divides in (True, False):
        parser = _ExprParser(text, percent_divides)
        value = parser.parse()
        if value is None:
            return [], 0
        values.append(value)
        operators = max(operators, parser.operators)
    return values, operators


def shown_operations(block_text):
    """Every `<expression> = <result>` written out inside a block.

    An operation counts as shown only when both halves are visible: the
    arithmetic AND the number it produces. `8-18%` is a range, not a shown
    operation, and does not satisfy CC2. Returns one entry per operation with
    the stated result and whether the arithmetic actually yields it.
    """
    text = normalize_math(SOURCE_ID_RE.sub(" ", block_text))
    operations = []
    for run in ARITH_RUN_RE.findall(text):
        # A run may chain relations (`2 x 38,147 = 76,294 at 7,700/day`); each
        # adjacent pair is examined, so a later half never swallows an earlier
        # operation.
        parts = run.split("=")
        for index in range(len(parts) - 1):
            lhs, rhs = parts[index], parts[index + 1]
            if not any(op in lhs for op in "+-*/"):
                continue
            lhs_values, operators = evaluate_expression(lhs)
            if not lhs_values or operators == 0:
                continue
            rhs_tokens = PROSE_NUMBER_RE.findall(rhs)
            if len(rhs_tokens) != 1:
                continue
            stated_raw = rhs_tokens[0]
            stated = float(stated_raw)
            decimals = decimals_of(stated_raw)
            tolerance = max(0.5 * (10 ** -decimals),
                            abs(stated) * COMPUTED_TOLERANCE_REL)
            candidates = []
            for value in lhs_values:
                candidates.extend((value, value * 100.0, value / 100.0))
            operations.append({
                "expression": normalize_scan_text(lhs)[:EXCERPT_LEN],
                "result": stated,
                "agrees": any(
                    abs(candidate - stated) <= tolerance
                    or abs(abs(candidate) - abs(stated)) <= tolerance
                    for candidate in candidates
                ),
            })
    return operations


def computed_blocks(answer_text):
    """The `[computed]` statements of an answer, one entry per bullet/paragraph."""
    prose = strip_fenced_blocks(answer_text)
    blocks = []
    for paragraph in split_paragraphs(prose):
        units = split_bullets(paragraph)
        if not units:
            units = [paragraph]
        elif not BULLET_RE.match(paragraph.splitlines()[0]):
            # Lead-in text before the first bullet is a unit of its own.
            lead = paragraph.split(units[0])[0]
            if lead.strip():
                units = [lead] + units
        for unit in units:
            if COMPUTED_LABEL_RE.search(unit):
                blocks.append(unit)
    return blocks


def check_computed_claims(answer_text, card_text, kb_numbers, no_kb_arm):
    """KB §2.8 CC1–CC6. Returns (report_dict, errors, warnings)."""
    errors = []
    warnings = []
    report = {
        "slot_present": False,
        "slot_has_computed": False,
        "abstention_literal": False,
        "card_supplied": card_text is not None,
        "statements": [],
    }

    card_numbers = scan_numbers(card_text) if card_text is not None else []
    report["card_number_count"] = len(card_numbers)

    slot = extract_section(answer_text, COMPUTED_SLOT_HEAD_RE)
    if slot is None:
        errors.append({
            "code": E_MISSING_COMPUTED_SLOT,
            "detail": "mandatory section 'What this experiment cannot show' is "
                      "absent (KB §2.8 CC5)",
        })
    else:
        report["slot_present"] = True
        report["slot_has_computed"] = bool(COMPUTED_LABEL_RE.search(slot))
        report["abstention_literal"] = bool(NO_COMPUTABLE_LIMIT_RE.search(slot))
        if not report["slot_has_computed"] and not report["abstention_literal"]:
            errors.append({
                "code": E_MISSING_NO_COMPUTABLE_LIMIT,
                "detail": "the section carries no [computed] statement, but the "
                          "mandatory literal 'no computable limit' is absent "
                          "(KB §2.8 CC5/CC6)",
            })

    blocks = computed_blocks(answer_text)
    if blocks and card_text is None:
        warnings.append({
            "code": W_CARD_NOT_SUPPLIED,
            "detail": "%d [computed] statement(s) found, but no --card was "
                      "given: provenance of their numbers was NOT checked "
                      "(KB §2.8 CC1)" % len(blocks),
        })

    for index, block in enumerate(blocks, start=1):
        entry = {
            "index": index,
            "excerpt": normalize_scan_text(block)[:EXCERPT_LEN],
            "operations": [],
            "numbers": [],
            "errors": [],
        }

        ids = sorted(set(SOURCE_ID_RE.findall(block)))
        if ids:
            entry["errors"].append({
                "code": E_COMPUTED_SOURCE_ID,
                "detail": "[computed] statement cites source ID(s) %s; a "
                          "calculation over the card's own numbers carries "
                          "none, and a knowledge-base number makes it a "
                          "magnitude transfer under rule 4 (KB §2.8 CC3)"
                          % ", ".join(ids),
            })

        operations = shown_operations(block)
        entry["operations"] = operations
        if not operations:
            entry["errors"].append({
                "code": E_COMPUTED_NO_OPERATION,
                "detail": "[computed] statement shows no arithmetic: the "
                          "operation must be written out in the sentence "
                          "(KB §2.8 CC2)",
            })
        for operation in operations:
            if operation["agrees"] is False:
                warnings.append({
                    "code": W_COMPUTED_ARITHMETIC_MISMATCH,
                    "detail": "statement %d: `%s` does not evaluate to the "
                              "stated %s" % (index, operation["expression"],
                                             _format_number(operation["result"])),
                })

        # Results of shown operations are admissible inputs to later steps of
        # the same statement, so the pool is grown to a fixed point.
        derived = [op["result"] for op in operations
                   if op["agrees"] and op["result"] is not None]
        pool = list(card_numbers) + list(FREE_CONSTANTS) + derived

        if card_text is None:
            report["statements"].append(entry)
            errors.extend(entry["errors"])
            continue

        cleaned = SOURCE_ID_RE.sub(" ", normalize_math(block))
        for raw in PROSE_NUMBER_RE.findall(cleaned):
            value = float(raw)
            decimals = decimals_of(raw)
            if value_matches(value, pool, decimals):
                if value_matches(value, card_numbers, decimals):
                    origin = "card"
                elif value in FREE_CONSTANTS:
                    origin = "constant"
                else:
                    origin = "derived"
                entry["numbers"].append({"value": value, "origin": origin})
                continue
            if not no_kb_arm and value_matches(value, kb_numbers, decimals):
                entry["numbers"].append({"value": value,
                                         "origin": "knowledge_base"})
                entry["errors"].append({
                    "code": E_COMPUTED_NUMBER_FROM_KB,
                    "detail": "%s is absent from the experiment card and is not "
                              "derived by any operation shown here, but it "
                              "occurs in the KNOWLEDGE CONTEXT: this is a "
                              "magnitude transfer presented as a calculation "
                              "(KB §2.8 CC1)" % _format_number(value),
                })
                continue
            entry["numbers"].append({"value": value, "origin": "unknown"})
            entry["errors"].append({
                "code": E_COMPUTED_NUMBER_FABRICATED,
                "detail": "%s is absent from the experiment card and is not "
                          "derived by any operation shown here (KB §2.8 CC1)"
                          % _format_number(value),
            })

        report["statements"].append(entry)
        errors.extend(entry["errors"])

    return report, errors, warnings


def _format_number(value):
    if value is None:
        return "none"
    if float(value).is_integer():
        return str(int(value))
    return ("%.6f" % value).rstrip("0")


def lint(answer_text, known_ids, no_kb_arm, gen_classes=(), card_text=None,
         kb_numbers=()):
    report = {
        "mode": "no-kb-arm" if no_kb_arm else "kb-arm",
        "cards": [],
        "generalizations": [],
        "product_proposals": {},
        "computed_claims": {},
        "errors": [],
        "warnings": [],
        "verdict": "PASS",
    }
    blocks = [b for b in extract_fenced_blocks(answer_text) if is_analog_block(b)]

    if no_kb_arm:
        if blocks:
            report["errors"].append({
                "code": E_CARD_IN_NO_KB_ARM,
                "detail": "%d analog card(s) emitted, but this arm has no "
                          "KNOWLEDGE CONTEXT — no cards may be emitted" % len(blocks),
            })
            report["cards"] = [
                {"index": i + 1, "checked": False} for i in range(len(blocks))
            ]
    else:
        computed_levels = []
        for i, block in enumerate(blocks):
            entry = {
                "index": i + 1,
                "source_id": None,
                "claimed_level": None,
                "computed_level": None,
                "card_errors": [],
            }
            card, parse_errors = parse_analog_card(block)
            if card is None:
                entry["card_errors"].append(
                    {"code": E_CARD_PARSE, "detail": "; ".join(parse_errors)}
                )
                report["cards"].append(entry)
                continue
            structure_reasons = validate_card_structure(card, parse_errors)
            source_raw = card.get("source", "")
            m = SOURCE_ID_RE.search(source_raw or "")
            if m:
                entry["source_id"] = m.group(0)
            if structure_reasons:
                entry["card_errors"].append(
                    {"code": E_CARD_PARSE, "detail": "; ".join(structure_reasons)}
                )
            else:
                entry["claimed_level"] = enum_value(card["level"])
                entry["computed_level"] = compute_level(card)
                computed_levels.append(entry["computed_level"])
                if entry["claimed_level"] != entry["computed_level"]:
                    entry["card_errors"].append({
                        "code": E_LEVEL_MISMATCH,
                        "detail": "claimed %s but axes compute %s"
                                  % (entry["claimed_level"], entry["computed_level"]),
                    })
                nt = card.get("not_transferable", "")
                if not nt or not nt.strip():
                    entry["card_errors"].append({
                        "code": E_EMPTY_NOT_TRANSFERABLE,
                        "detail": "not_transferable is empty",
                    })
            if "source" in card:
                if entry["source_id"] is None:
                    entry["card_errors"].append({
                        "code": E_UNKNOWN_SOURCE_ID,
                        "detail": "no source ID (T*-** / P-**) found in `source`",
                    })
                elif entry["source_id"] not in known_ids:
                    entry["card_errors"].append({
                        "code": E_UNKNOWN_SOURCE_ID,
                        "detail": "source ID %s does not exist in KNOWLEDGE "
                                  "CONTEXT" % entry["source_id"],
                    })
            report["cards"].append(entry)

        has_l1_l2 = any(lv in ("L1", "L2") for lv in computed_levels)
        any_parse_error = any(
            e["code"] == E_CARD_PARSE
            for c in report["cards"]
            for e in c.get("card_errors", [])
        )
        # With an unparsable card the L1/L2-emptiness is undetermined and the
        # parse error already invalidates the answer, so the no-direct-analogs
        # rule is checked only over successfully computed levels.
        if not has_l1_l2 and not any_parse_error:
            # All cards L3 (or no cards): the literal line is mandatory.
            if not NO_DIRECT_ANALOGS_RE.search(answer_text):
                report["errors"].append({
                    "code": E_MISSING_NO_DIRECT_ANALOGS,
                    "detail": "no card computes to L1/L2, but the mandatory "
                              "line 'no direct analogs' is absent",
                })

    if not SIDE_EFFECTS_RE.search(answer_text):
        report["errors"].append({
            "code": E_MISSING_SIDE_EFFECTS,
            "detail": "mandatory section 'Non-monetization effects to "
                      "instrument' is absent",
        })

    # V1.2 (KB §2.5): scope/qualifier rules for corpus-level generalizations.
    # Applied in both arms — they constrain the answer's prose, not the cards.
    report["generalizations"] = check_generalizations(
        answer_text, known_ids, list(gen_classes)
    )

    # V1.3 (KB §2.7): the product-proposal channel. Applied in both arms; the
    # card-derived grounding set comes from the cards checked above.
    proposals, proposal_errors, proposal_warnings = check_product_proposals(
        answer_text, known_ids, no_kb_arm, report["cards"]
    )
    report["product_proposals"] = proposals
    report["errors"].extend(proposal_errors)
    report["warnings"].extend(proposal_warnings)

    # V1.4 (KB §2.8): provenance of the numbers inside [computed] statements
    # and the mandatory MAIN slot. Applied in both arms — the numbers come
    # from the card under review, which both arms receive.
    computed, computed_errors, computed_warnings = check_computed_claims(
        answer_text, card_text, list(kb_numbers), no_kb_arm
    )
    report["computed_claims"] = computed
    report["errors"].extend(computed_errors)
    report["warnings"].extend(computed_warnings)

    any_card_error = any(e for c in report["cards"] for e in c.get("card_errors", []))
    any_gen_error = any(
        e for g in report["generalizations"] for e in g.get("errors", [])
    )
    if report["errors"] or any_card_error or any_gen_error:
        report["verdict"] = "FAIL"
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("answer", help="path to the validator answer (.md)")
    parser.add_argument("--kb", required=True, help="path to knowledge_base.md")
    parser.add_argument("--patterns", required=True, help="path to pattern_cards.md")
    parser.add_argument(
        "--card",
        help="path to the experiment card under review; required to check the "
             "provenance of numbers inside [computed] statements (KB §2.8). "
             "Without it those checks are skipped and a warning is emitted",
    )
    parser.add_argument(
        "--no-kb-arm",
        action="store_true",
        help="arm without KNOWLEDGE CONTEXT: cards must not be emitted; "
             "card-level checks are skipped",
    )
    args = parser.parse_args(argv)

    try:
        answer_text = read_text(args.answer)
        kb_text = read_text(args.kb)
        patterns_text = read_text(args.patterns)
        card_text = read_text(args.card) if args.card else None
    except OSError as exc:
        print(json.dumps({"error": str(exc)}, sort_keys=True))
        return 2

    known_ids = collect_known_ids(kb_text, patterns_text)
    gen_classes = parse_generalization_classes(kb_text)
    kb_numbers = scan_numbers(kb_text) + scan_numbers(patterns_text)
    report = lint(answer_text, known_ids, args.no_kb_arm, gen_classes,
                  card_text=card_text, kb_numbers=kb_numbers)
    report["files"] = {
        "answer": args.answer,
        "kb": args.kb,
        "patterns": args.patterns,
        "card": args.card,
    }
    report["known_source_ids_count"] = len(known_ids)
    report["generalization_classes"] = [c["class_id"] for c in gen_classes]
    print(json.dumps(report, sort_keys=True, indent=2, ensure_ascii=False))
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
