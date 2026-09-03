import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-fala-Music-scripture-memorization/39500d8f-25b4-4253-ac0a-4a80d40e145e/scratchpad")
from lyric_fidelity import analyze_lyric_fidelity, normalize_tokens, words_to_number_tokens

# --- number normalization sanity ---
tests = [
    ("Romans three twenty-three.", "romans 3 23"),
    ("Second Corinthians five seventeen.", "2 corinthians 5 17"),
    ("Psalm one nineteen nine and eleven.", "psalm 1 19 9 and 11"),
    ("Ephesians two eight to nine.", "ephesians 2 8 to 9"),
    ("First John five thirteen.", "1 john 5 13"),
]
print("=== number normalization ===")
for src, expect in tests:
    got = " ".join(normalize_tokens(src))
    ok = "OK" if got == expect else "MISMATCH"
    print(f"{ok}: {src!r} -> {got!r} (expected {expect!r})")

# --- line classification sanity ---
expected_lines = [
    "Packet Bee",
    "Proclaim Christ",
    "All Have Sinned",
    "Bee One and Bee Two",
    "Romans three twenty-three.",
    "For all have sinned, and come short of the glory of God;",
    "Romans three twenty-three.",
    "Isaiah fifty-three six.",
    "All we like sheep have gone astray; we have turned every one to his own way; and the LORD hath laid on him the iniquity of us all.",
    "Isaiah fifty-three six.",
]

# Simulate a whisper-like transcript that:
# - gets line 0-1 right (small casing/number differences, ASR noise)
# - gets the first Romans 3:23 reference + verse right (with minor noise)
# - REPEATS the "Romans three twenty-three" reference an extra time
# - DROPS the Isaiah 53:6 verse entirely (missing)
# - substitutes wrong words in the closing Isaiah reference (altered)
simulated_transcript = (
    "packet b proclaim christ all have sinned b1 and b2 "
    "romans 3 23 for all have sinned and come short of the glory of god "
    "romans 3 23 romans 3 23 "
    "isaiah 53 6 "
    # verse line MISSING entirely here
    "isaiah fifty four seven"  # altered reference, wrong numbers/words entirely
)

result = analyze_lyric_fidelity(expected_lines, simulated_transcript, noise_threshold=0.5)
print("\n=== line classification ===")
print(f"overall_wer={result.overall_wer:.3f} missing={result.n_missing} altered={result.n_altered} "
      f"uncertain={result.n_uncertain} repeats={len(result.repeats)} structural_failure={result.structural_failure}")
for l in result.lines:
    tag = f"[{l.status.upper()}]"
    print(f"  {tag:12s} wer={l.line_wer:.2f} | {l.text!r} | heard={l.heard_text!r}")
print("\n=== repeat findings ===")
if not result.repeats:
    print("  (none)")
for r in result.repeats:
    print(f"  {r.text!r}: expected {r.expected_count}x, observed {r.observed_count}x")
