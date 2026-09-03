"""
Lyric-fidelity check (Procedure 04 update, 2026-09-02).

Transcribes a song locally (faster-whisper) and aligns the transcript
against the song's expected lyrics text, reporting per-line coverage:
missing lines, altered lines (with diff), lines repeated beyond the
format, and an overall word-error estimate. Distinguishes "transcriber
uncertainty" (scattered small errors, expected even on a perfectly-sung
reference) from "structural failure" (a whole line absent, reordered, or
substantively different) using a noise ceiling calibrated on Packet A's
memorized take.

No cloud services: transcription runs locally via faster-whisper
(CTranslate2 / int8 CPU inference). Model weights are downloaded once
from the Hugging Face Hub and cached locally; no audio is uploaded and no
inference happens off-machine.
"""

import re
from dataclasses import dataclass
from typing import List


# ---------------------------------------------------------------------------
# Normalization: lowercase, strip punctuation, spell-out/digit number unify.
# ---------------------------------------------------------------------------

_ONES = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9,
}
_TEENS = {
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
}
_TENS = {
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
}
_ORD_ONES = {
    "first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5,
    "sixth": 6, "seventh": 7, "eighth": 8, "ninth": 9,
}
_ORD_TEENS = {
    "tenth": 10, "eleventh": 11, "twelfth": 12, "thirteenth": 13, "fourteenth": 14,
    "fifteenth": 15, "sixteenth": 16, "seventeenth": 17, "eighteenth": 18, "nineteenth": 19,
}
_ORD_TENS = {
    "twentieth": 20, "thirtieth": 30, "fortieth": 40, "fiftieth": 50,
    "sixtieth": 60, "seventieth": 70, "eightieth": 80, "ninetieth": 90,
}

_ALL_NUMWORDS = set(_ONES) | set(_TEENS) | set(_TENS) | set(_ORD_ONES) | set(_ORD_TEENS) | set(_ORD_TENS)


def words_to_number_tokens(tokens: List[str]) -> List[str]:
    """Replace recognized English number-word tokens/runs with digit strings.

    Combines a tens-word immediately followed by a ones/ordinal-ones word
    ("twenty three" / "twenty third" -> "23"). Standalone number words
    (including the "chapter over 99 read digit-grouped" style, e.g. "one
    nineteen" for 119) are converted independently token-by-token, which is
    exactly the desired behavior since they are not glued by "hundred".
    Also strips ordinal suffixes off digits already present ("21st" -> "21").
    """
    out = []
    i = 0
    n = len(tokens)
    while i < n:
        t = tokens[i]
        # digit with ordinal suffix, e.g. "21st", "3rd"
        m = re.fullmatch(r"(\d+)(st|nd|rd|th)", t)
        if m:
            out.append(m.group(1))
            i += 1
            continue
        if t in _TENS and i + 1 < n and tokens[i + 1] in _ONES:
            out.append(str(_TENS[t] + _ONES[tokens[i + 1]]))
            i += 2
            continue
        if t in _TENS and i + 1 < n and tokens[i + 1] in _ORD_ONES:
            out.append(str(_TENS[t] + _ORD_ONES[tokens[i + 1]]))
            i += 2
            continue
        if t in _ONES:
            out.append(str(_ONES[t]))
            i += 1
            continue
        if t in _TEENS:
            out.append(str(_TEENS[t]))
            i += 1
            continue
        if t in _TENS:
            out.append(str(_TENS[t]))
            i += 1
            continue
        if t in _ORD_ONES:
            out.append(str(_ORD_ONES[t]))
            i += 1
            continue
        if t in _ORD_TEENS:
            out.append(str(_ORD_TEENS[t]))
            i += 1
            continue
        if t in _ORD_TENS:
            out.append(str(_ORD_TENS[t]))
            i += 1
            continue
        out.append(t)
        i += 1
    return out


_PACKET_LETTER_PHONETIC = {"a": "ay", "b": "bee", "c": "see", "d": "dee", "e": "ee"}

# Whisper frequently glues a spoken packet-letter designator into a single
# alphanumeric token ("A3", "b12") while the reference lyrics always spell
# it out as two words ("Ay Three"). Split the glued form apart before
# tokenizing so both sides can align on equal footing.
_GLUED_LETTER_DIGIT_RE = re.compile(r"(?<![a-z0-9])([a-e])(\d{1,3})(?![0-9])")


def normalize_tokens(text: str) -> List[str]:
    text = text.lower()
    text = _GLUED_LETTER_DIGIT_RE.sub(r"\1 \2", text)
    text = text.replace("-", " ")
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    tokens = text.split()
    tokens = words_to_number_tokens(tokens)
    # Map any standalone single-letter packet-designator token (a/b/c/d/e)
    # to its spoken phonetic form, matching how the reference lyrics always
    # spell it. Applied uniformly to both reference and hypothesis text, so
    # this is safe even where the letter is really just the English article
    # "a" — both sides get the same substitution and still align.
    tokens = [_PACKET_LETTER_PHONETIC.get(t, t) for t in tokens]
    return tokens


# ---------------------------------------------------------------------------
# Levenshtein alignment (word-level), with backtrace.
# ---------------------------------------------------------------------------

@dataclass
class AlignResult:
    ops: List[tuple]  # list of (kind, ref_idx_or_None, hyp_idx_or_None)
    edit_distance: int
    n_sub: int
    n_del: int
    n_ins: int
    n_match: int


def align(ref: List[str], hyp: List[str]) -> AlignResult:
    n, m = len(ref), len(hyp)
    # dp[i][j] = edit distance between ref[:i] and hyp[:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        ref_i = ref[i - 1]
        row = dp[i]
        prev_row = dp[i - 1]
        for j in range(1, m + 1):
            if ref_i == hyp[j - 1]:
                row[j] = prev_row[j - 1]
            else:
                row[j] = 1 + min(prev_row[j - 1], prev_row[j], row[j - 1])

    ops = []
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and ref[i - 1] == hyp[j - 1] and dp[i][j] == dp[i - 1][j - 1]:
            ops.append(("match", i - 1, j - 1))
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1:
            ops.append(("sub", i - 1, j - 1))
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            ops.append(("del", i - 1, None))
            i -= 1
        else:
            ops.append(("ins", None, j - 1))
            j -= 1
    ops.reverse()

    n_sub = sum(1 for o in ops if o[0] == "sub")
    n_del = sum(1 for o in ops if o[0] == "del")
    n_ins = sum(1 for o in ops if o[0] == "ins")
    n_match = sum(1 for o in ops if o[0] == "match")
    return AlignResult(ops=ops, edit_distance=dp[n][m], n_sub=n_sub, n_del=n_del, n_ins=n_ins, n_match=n_match)


# ---------------------------------------------------------------------------
# Per-line coverage classification.
# ---------------------------------------------------------------------------

@dataclass
class LineReport:
    index: int
    text: str
    status: str  # "ok" | "uncertain" | "altered" | "missing"
    line_wer: float  # (sub+del)/len(line_tokens)   -- 0 if line has 0 tokens
    heard_text: str  # best-effort reconstruction of what was aligned to this line


@dataclass
class RepeatFinding:
    text: str
    expected_count: int
    observed_count: int


@dataclass
class FidelityResult:
    lines: List[LineReport]
    overall_wer: float
    ref_token_count: int
    hyp_token_count: int
    n_missing: int
    n_altered: int
    n_uncertain: int
    repeats: List[RepeatFinding]
    structural_failure: bool
    noise_threshold: float


def _count_nonoverlapping_token_run(haystack: List[str], needle: List[str]) -> int:
    """Count non-overlapping occurrences of the exact token sequence `needle`
    inside `haystack` (word-boundary safe: compares whole tokens, not
    substrings)."""
    if not needle:
        return 0
    count = 0
    i = 0
    n, m = len(haystack), len(needle)
    while i <= n - m:
        if haystack[i : i + m] == needle:
            count += 1
            i += m
        else:
            i += 1
    return count


def find_repeats(
    expected_lines: List[str], hyp_tokens: List[str], hyp_claimed: List[bool]
) -> List[RepeatFinding]:
    """Best-effort 'repeated beyond format' check.

    Naively counting substring occurrences of a short line's text anywhere
    in the transcript produces false positives: a topic name or short
    phrase can coincidentally appear as a literal substring inside a
    different, longer, unrelated line (e.g. topic "All Have Sinned"
    followed by the verse "For all have sinned, and come short..." — the
    topic text is a genuine substring of the verse text). To avoid that,
    repeat occurrences are only searched for within the *unclaimed*
    remainder of the transcript — hyp tokens that the alignment did not
    already attribute (match/sub) to any expected line. A real extra
    repeat shows up as leftover, unattributed material; a coincidental
    substring inside another line's own matched span does not.

    hyp_claimed[i] is True if hyp_tokens[i] was aligned (match/sub) to
    some expected line's own token range.
    """
    from collections import Counter

    expected_counts = Counter(l.strip() for l in expected_lines)
    unclaimed_tokens = [t for t, claimed in zip(hyp_tokens, hyp_claimed) if not claimed]
    findings = []
    for text, exp_count in expected_counts.items():
        needle = normalize_tokens(text)
        if not needle:
            continue
        extra_count = _count_nonoverlapping_token_run(unclaimed_tokens, needle)
        if extra_count > 0:
            findings.append(
                RepeatFinding(text=text, expected_count=exp_count, observed_count=exp_count + extra_count)
            )
    return findings


def analyze_lyric_fidelity(
    expected_lines: List[str],
    transcript_text: str,
    noise_threshold: float = 0.5,
) -> FidelityResult:
    """Align transcript_text against expected_lines and classify each line.

    noise_threshold: max per-line word-error fraction ((sub+del)/len) that
    still counts as "transcriber uncertainty" rather than "altered". Lines
    with recall == 0 (nothing recognizable aligned) are always "missing"
    regardless of this threshold.
    """
    ref_tokens: List[str] = []
    line_token_ranges = []  # (start, end) exclusive, per line, into ref_tokens
    for line in expected_lines:
        toks = normalize_tokens(line)
        start = len(ref_tokens)
        ref_tokens.extend(toks)
        line_token_ranges.append((start, len(ref_tokens)))

    hyp_tokens = normalize_tokens(transcript_text)

    result = align(ref_tokens, hyp_tokens)

    # ref_idx -> (kind, hyp_idx_or_None)
    ref_status = [None] * len(ref_tokens)
    hyp_claimed = [False] * len(hyp_tokens)
    for kind, ridx, hidx in result.ops:
        if kind in ("match", "sub"):
            ref_status[ridx] = (kind, hidx)
            hyp_claimed[hidx] = True
        elif kind == "del":
            ref_status[ridx] = (kind, None)
        # "ins" ops carry no ref index; repeats are detected separately
        # via find_repeats() rather than alignment-insertion adjacency,
        # since duplicate reference text (the sandwich pattern) makes
        # insertion-point attribution unreliable.

    lines: List[LineReport] = []
    n_missing = n_altered = n_uncertain = 0

    for idx, (line_text, (start, end)) in enumerate(zip(expected_lines, line_token_ranges)):
        n_tok = end - start
        if n_tok == 0:
            lines.append(LineReport(idx, line_text, "ok", 0.0, ""))
            continue
        sub_c = del_c = match_c = 0
        heard_words = []
        for k in range(start, end):
            st = ref_status[k]
            if st is None:
                continue
            kind, hidx = st
            if kind == "match":
                match_c += 1
                heard_words.append(hyp_tokens[hidx])
            elif kind == "sub":
                sub_c += 1
                heard_words.append(hyp_tokens[hidx])
            elif kind == "del":
                del_c += 1
        line_wer = (sub_c + del_c) / n_tok
        heard_text = " ".join(heard_words)

        if match_c == 0 and sub_c == 0:
            status = "missing"
            n_missing += 1
        elif line_wer <= noise_threshold:
            status = "ok" if line_wer == 0 else "uncertain"
            if status == "uncertain":
                n_uncertain += 1
        else:
            status = "altered"
            n_altered += 1

        lines.append(LineReport(idx, line_text, status, line_wer, heard_text))

    overall_wer = result.edit_distance / len(ref_tokens) if ref_tokens else 0.0
    repeats = find_repeats(expected_lines, hyp_tokens, hyp_claimed)
    structural_failure = (n_missing > 0) or (n_altered > 0) or (len(repeats) > 0)

    return FidelityResult(
        lines=lines,
        overall_wer=overall_wer,
        ref_token_count=len(ref_tokens),
        hyp_token_count=len(hyp_tokens),
        n_missing=n_missing,
        n_altered=n_altered,
        n_uncertain=n_uncertain,
        repeats=repeats,
        structural_failure=structural_failure,
        noise_threshold=noise_threshold,
    )


# ---------------------------------------------------------------------------
# Expected-lyrics loaders.
# ---------------------------------------------------------------------------

def load_v2_lyrics(md_path: str) -> List[str]:
    """Extract non-blank lines from the '## Lyrics' section of a v2 packet file."""
    text = open(md_path, encoding="utf-8").read()
    m = re.search(r"^## Lyrics\s*$", text, re.MULTILINE)
    if not m:
        raise ValueError(f"No '## Lyrics' section found in {md_path}")
    start = m.end()
    rest = text[start:]
    m2 = re.search(r"^## ", rest, re.MULTILINE)
    section = rest[: m2.start()] if m2 else rest
    lines = [l.strip() for l in section.splitlines()]
    lines = [l for l in lines if l]
    return lines


def load_v1_packet_a_lyrics(procedure_03_path: str) -> List[str]:
    """Extract Packet A's v1 lyric lines, verbatim, from the Human Prompts
    section of navigators/procedures/03-lyrics-format.md (the "Packet Ay"
    example, with line breaks recorded there as " / ").
    """
    text = open(procedure_03_path, encoding="utf-8").read()
    marker_start = "Packet Ay / Live the New Life"
    idx = text.find(marker_start)
    if idx == -1:
        raise ValueError("Packet Ay v1 example not found in " + procedure_03_path)
    end_marker = '*(Line breaks in the original example are shown here as " / ".)*'
    idx_end = text.find(end_marker, idx)
    if idx_end == -1:
        raise ValueError("End marker for Packet Ay v1 example not found")
    segment = text[idx:idx_end].strip()
    lines = [l.strip() for l in segment.split(" / ")]
    return lines
