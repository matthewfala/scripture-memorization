import sys
import time
sys.path.insert(0, "/private/tmp/claude-501/-Users-fala-Music-scripture-memorization/39500d8f-25b4-4253-ac0a-4a80d40e145e/scratchpad")
from lyric_fidelity import analyze_lyric_fidelity, load_v1_packet_a_lyrics
from screen_song import transcribe

mp3 = "/Users/fala/Music/scripture-memorization/navigators/songs/packet-a-memorized.mp3"
proc03 = "/Users/fala/Music/scripture-memorization/navigators/procedures/03-lyrics-format.md"

expected_lines = load_v1_packet_a_lyrics(proc03)
print(f"n expected lines: {len(expected_lines)}")

t0 = time.time()
transcript_text, info = transcribe(mp3, "small", cpu_threads=8)
print(f"transcribe time: {time.time()-t0:.1f}s lang={info.language} p={info.language_probability:.2f}")
print("TRANSCRIPT LENGTH (chars):", len(transcript_text))

# save transcript to disk for reuse (avoid re-running whisper)
with open("packet_a_memorized_transcript.txt", "w") as f:
    f.write(transcript_text)

result = analyze_lyric_fidelity(expected_lines, transcript_text, noise_threshold=1.0)  # permissive: inspect raw distribution
print(f"\noverall_wer={result.overall_wer:.3f}")
print("\nper-line WER (sorted desc):")
sorted_lines = sorted(result.lines, key=lambda l: -l.line_wer)
for l in sorted_lines:
    print(f"  wer={l.line_wer:.2f} idx={l.index:2d} text={l.text!r} heard={l.heard_text!r}")

import statistics
wers = [l.line_wer for l in result.lines]
nonzero = [w for w in wers if w > 0]
print(f"\nn_lines={len(wers)} n_nonzero_wer={len(nonzero)}")
print(f"max={max(wers):.2f} mean={statistics.mean(wers):.3f}")
for p in [50, 75, 80, 85, 90, 95, 98, 100]:
    idx = min(int(len(wers)*p/100), len(wers)-1)
    print(f"  p{p}: {sorted(wers)[idx]:.2f}")

print("\nrepeats found:", len(result.repeats))
for r in result.repeats:
    print(f"  {r.text!r} expected={r.expected_count} observed={r.observed_count}")
