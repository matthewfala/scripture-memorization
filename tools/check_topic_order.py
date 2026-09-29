#!/usr/bin/env python3
"""Position-aware topic-announcement check (v3 lyrics, Procedure 04).

v3 announces each topic (name + designators) before AND after its verse
pair. A position-blind fuzzy search can "find" a topic title inside verse
text ("faith", "good works"), so this check walks the transcript in order:
for each topic it locates the closing words of the topic's second verse,
then requires the topic name to be heard within the next few words (after
the trailing reference). It also checks the leading announcement before
the first verse.

Input: the ``verify-<stem>.words.json`` word timeline written by
verify_lines.py. Usage:
    check_topic_order.py WORDS_JSON --lyrics-file packet-e.md
Exit 0 if every topic is announced in both positions.
"""
import argparse
import difflib
import json
import re
import sys
from pathlib import Path


def norm(t):
    return re.sub(r"[^a-z0-9' ]+", " ", t.lower()).split()


def find_seq(words, target, start, window=None, min_ratio=0.75):
    """Index just past the best fuzzy occurrence of target in words[start:]."""
    tw = " ".join(target)
    end = len(words) if window is None else min(len(words), start + window)
    best, best_end = 0.0, None
    n = len(target)
    for i in range(start, end):
        for w in (n - 1, n, n + 1):
            if w <= 0 or i + w > len(words):
                continue
            r = difflib.SequenceMatcher(None, tw, " ".join(words[i:i + w])).ratio()
            if r > best:
                best, best_end = r, i + w
    return (best_end, best) if best >= min_ratio else (None, best)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("words_json")
    ap.add_argument("--lyrics-file", required=True)
    ap.add_argument("--lookahead", type=int, default=14)
    args = ap.parse_args()
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from lyric_fidelity import load_v2_lyrics
    L = load_v2_lyrics(args.lyrics_file)
    W = json.load(open(args.words_json))
    words = [w for _, w in W]
    times = [t for t, _ in W]

    # v3 layout: 2 bookend lines, then 6 blocks of 10 lines, then 2 bookend lines
    ok_all, pos = True, 0
    for k in range(6):
        b = L[2 + 10 * k: 2 + 10 * (k + 1)]
        topic, verse2 = b[0], b[6]
        tail = norm(verse2)[-5:]
        # leading announcement: topic name near where verse block begins
        lead_end, lead_r = find_seq(words, norm(topic), pos, window=60, min_ratio=0.6)
        v2_end, _ = find_seq(words, tail, pos, min_ratio=0.7)
        if v2_end is None:
            print(f"{topic:12s} could not locate end of second verse — UNVERIFIED")
            ok_all = False
            continue
        trail_end, trail_r = find_seq(words, norm(topic), v2_end, window=args.lookahead, min_ratio=0.6)
        heard = " ".join(words[v2_end:v2_end + args.lookahead])
        lead_ok, trail_ok = lead_end is not None, trail_end is not None
        ok_all &= lead_ok and trail_ok
        t = times[v2_end] if v2_end < len(times) else times[-1]
        print(f"{topic:12s} lead {'OK ' if lead_ok else 'MISS'} trail {'OK ' if trail_ok else 'MISS'} "
              f"@{int(t//60)}:{int(t%60):02d} after verse: {heard!r}")
        pos = trail_end if trail_end is not None else v2_end
    print("TOPIC ORDER", "PASS" if ok_all else "FAIL")
    sys.exit(0 if ok_all else 1)


if __name__ == "__main__":
    main()
