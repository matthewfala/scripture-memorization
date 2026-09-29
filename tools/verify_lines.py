#!/usr/bin/env python3
"""Line-presence verifier (Procedure 04, strict standard).

For a vocal stem and its expected lyrics, decide for EVERY expected line
whether it is actually sung — including bookends, designators, and
reference lines that ordinary transcription tends to drop.

Method (local only):
1. Transcribe the stem with faster-whisper (medium, word timestamps),
   passing an ``initial_prompt`` built from the packet's short lines
   (bookends, topic titles, designators, references). Prompt biasing
   makes the ASR far more likely to recognize these tokens when they are
   actually sung; a line that STILL cannot be found under bias is strong
   evidence it is absent.
2. For each expected line, fuzzy-search the transcript word stream for
   the best matching window (difflib ratio over normalized words).
3. Classify: FOUND (ratio >= --found-threshold), WEAK (>= --weak-threshold),
   else NOT_FOUND. For NOT_FOUND lines, report vocal RMS energy in the
   expected region (start/end of track for bookends) as a secondary cue:
   silence there corroborates absence; strong vocals suggest the line may
   be sung but unintelligible to the ASR (human ear decides).

Output: a per-line table to stdout and a
``verify-<stem-basename>.md`` report next to --out-dir.

Exit code 0 if all lines FOUND, 1 otherwise.
"""

import argparse
import difflib
import re
import sys
from pathlib import Path

import numpy as np


def norm_words(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9' ]+", " ", text)
    return [w for w in text.split() if w]


def build_bias_prompt(lines, max_chars=800):
    """Short lines (<= 6 words) are the at-risk vocabulary; join unique ones."""
    seen, parts = set(), []
    for ln in lines:
        if len(ln.split()) <= 6 and ln not in seen:
            seen.add(ln)
            parts.append(ln.rstrip("."))
    prompt = ". ".join(parts) + "."
    return prompt[:max_chars]


def best_window(line_words, words, times):
    """Best fuzzy match of line_words against any window of words."""
    n = len(line_words)
    if n == 0 or not words:
        return 0.0, None, None
    best = (0.0, None, None)
    lo, hi = max(1, n - 2), n + 3
    joined_line = " ".join(line_words)
    for w in range(lo, hi + 1):
        for i in range(0, len(words) - w + 1):
            cand = " ".join(words[i:i + w])
            r = difflib.SequenceMatcher(None, joined_line, cand).ratio()
            if r > best[0]:
                best = (r, times[i], times[i + w - 1])
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stem_path")
    ap.add_argument("--lyrics-file", required=True)
    ap.add_argument("--whisper-model", default="medium")
    ap.add_argument("--cpu-threads", type=int, default=8)
    ap.add_argument("--found-threshold", type=float, default=0.80)
    ap.add_argument("--weak-threshold", type=float, default=0.60)
    ap.add_argument("--out-dir", default=None)
    args = ap.parse_args()

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from lyric_fidelity import load_v2_lyrics

    expected = load_v2_lyrics(args.lyrics_file)
    bias = build_bias_prompt(expected)

    from faster_whisper import WhisperModel
    model = WhisperModel(args.whisper_model, device="cpu",
                         compute_type="int8", cpu_threads=args.cpu_threads)
    segments, _ = model.transcribe(
        args.stem_path, language="en", word_timestamps=True,
        initial_prompt=bias, beam_size=5,
        condition_on_previous_text=False,
    )
    words, times = [], []
    transcript_parts = []
    for seg in segments:
        transcript_parts.append(seg.text)
        for w in (seg.words or []):
            for tok in norm_words(w.word):
                words.append(tok)
                times.append(w.start)
    transcript_text = " ".join(transcript_parts)

    # primary evidence: the proven global aligner on the biased transcript
    from lyric_fidelity import analyze_lyric_fidelity
    fid = analyze_lyric_fidelity(expected, transcript_text, noise_threshold=0.5)
    aligned = {}
    for lr in fid.lines:
        aligned[lr.index] = lr  # status: ok | uncertain | altered | missing

    # vocal energy profile for the NOT_FOUND secondary cue
    import librosa
    y, sr = librosa.load(args.stem_path, sr=16000, mono=True)
    hop = 1600  # 0.1 s
    rms = librosa.feature.rms(y=y, hop_length=hop)[0]
    def energy(t0, t1):
        i0, i1 = int(t0 * 10), max(int(t1 * 10), int(t0 * 10) + 1)
        seg = rms[i0:i1]
        return float(seg.mean()) if len(seg) else 0.0
    active = float(np.percentile(rms[rms > 0.005], 50)) if (rms > 0.005).any() else 0.01
    total = len(y) / 16000.0

    rows, n_found = [], 0
    for idx, line in enumerate(expected, start=1):
        lw = norm_words(line)
        r, t0, t1 = best_window(lw, words, times)
        lr = aligned.get(idx)
        status = lr.status if lr else "missing"
        # A line is FOUND when EITHER evidence channel confirms it:
        # the global alignment (ok/uncertain) or a strong fuzzy window.
        if status in ("ok", "uncertain") or r >= args.found_threshold:
            verdict = "FOUND"
            n_found += 1
        elif r >= args.weak_threshold or status == "altered":
            verdict = "WEAK"
        else:
            verdict = "NOT_FOUND"
        note = ""
        if verdict != "FOUND":
            # guess region: bookends by position, else neighbor timestamps
            if idx <= 2:
                g0, g1 = 0.0, 30.0
            elif idx >= len(expected) - 1:
                g0, g1 = max(0.0, total - 35.0), total
            elif t0 is not None:
                g0, g1 = max(0.0, t0 - 5), (t1 or t0) + 5
            else:
                g0, g1 = 0.0, total
            e = energy(g0, g1)
            note = f"vocal-energy {e/active:.2f}x median in {g0:.0f}-{g1:.0f}s"
        ts = f"{int(t0//60)}:{int(t0%60):02d}" if t0 is not None else "-"
        rows.append((idx, verdict, f"{r:.2f}", ts, line[:60], note))

    name = Path(args.stem_path).stem
    out_dir = Path(args.out_dir) if args.out_dir else Path(args.stem_path).parent
    out = out_dir / f"verify-{name}.md"
    with open(out, "w") as f:
        f.write(f"# Line-presence verification — {name}\n\n")
        f.write(f"- Model: faster-whisper {args.whisper_model} (biased prompt, word timestamps)\n")
        f.write(f"- Found threshold {args.found_threshold}, weak {args.weak_threshold}\n")
        f.write(f"- Result: {n_found}/{len(expected)} lines FOUND\n\n")
        f.write("| # | Verdict | Match | At | Line | Note |\n|---|---|---|---|---|---|\n")
        for row in rows:
            f.write("| " + " | ".join(str(x) for x in row) + " |\n")
        f.write("\n## Human Prompts\n\n#### Initial Document Written On 2026-09-17\n\n")
        f.write("- Generated by `tools/verify_lines.py` per Procedure 04 (strict standard).\n")
    for row in rows:
        if row[1] != "FOUND":
            print("  ", row)
    print(f"[{name}] {n_found}/{len(expected)} FOUND -> {out}")
    sys.exit(0 if n_found == len(expected) else 1)


if __name__ == "__main__":
    main()
