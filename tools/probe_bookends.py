#!/usr/bin/env python3
"""Bookend probe (Procedure 04, strict standard).

Transcribes only the opening and closing windows of a vocal stem, with the
packet's bookend lines as the bias prompt, and reports what is heard. This
is the most sensitive local test of whether "Packet <X> / <Packet Name>"
is actually sung at both ends: a bookend still unheard under a tight,
biased window is very likely skipped.

Usage: probe_bookends.py STEM --lyrics-file packet-e.md [--open 40 --close 45]
Exit 0 if both bookends are heard (fuzzy match >= 0.7), 1 otherwise.
"""
import argparse
import difflib
import re
import sys
from pathlib import Path


def norm(t):
    return " ".join(re.sub(r"[^a-z0-9' ]+", " ", t.lower()).split())


def heard_ratio(target, heard):
    tw, hw = norm(target).split(), norm(heard).split()
    best = 0.0
    for i in range(len(hw)):
        for w in range(max(1, len(tw) - 1), len(tw) + 2):
            cand = " ".join(hw[i:i + w])
            best = max(best, difflib.SequenceMatcher(None, " ".join(tw), cand).ratio())
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stem")
    ap.add_argument("--lyrics-file", required=True)
    ap.add_argument("--open", type=float, default=40.0)
    ap.add_argument("--close", type=float, default=45.0)
    ap.add_argument("--model", default="medium")
    args = ap.parse_args()

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from lyric_fidelity import load_v2_lyrics
    lines = load_v2_lyrics(args.lyrics_file)
    open_pair, close_pair = lines[:2], lines[-2:]
    prompt = f"{open_pair[0]}. {open_pair[1]}. {lines[2]}. {lines[3]}."

    import librosa
    from faster_whisper import WhisperModel
    dur = librosa.get_duration(path=args.stem)
    model = WhisperModel(args.model, device="cpu", compute_type="int8", cpu_threads=8)

    def hear(t0, t1):
        segs, _ = model.transcribe(args.stem, language="en", initial_prompt=prompt,
                                   clip_timestamps=[t0, t1], beam_size=5,
                                   condition_on_previous_text=False)
        return " ".join(s.text for s in segs).strip()

    head = hear(0.0, min(args.open, dur))
    tail = hear(max(0.0, dur - args.close), dur)
    ok = True
    print(f"opening heard: {head!r}")
    for ln in open_pair:
        r = heard_ratio(ln, head); ok &= r >= 0.7
        print(f"  {ln!r}: {r:.2f} {'HEARD' if r >= 0.7 else 'NOT HEARD'}")
    print(f"closing heard: {tail!r}")
    for ln in close_pair:
        r = heard_ratio(ln, tail); ok &= r >= 0.7
        print(f"  {ln!r}: {r:.2f} {'HEARD' if r >= 0.7 else 'NOT HEARD'}")
    print("BOOKENDS", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
