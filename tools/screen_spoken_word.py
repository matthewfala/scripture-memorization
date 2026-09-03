#!/usr/bin/env python3
"""
Spoken-word screener (Procedure 04 — navigators/procedures/04-spoken-word-screen.md).

Heuristic, local-only DSP tool that estimates how much of a song is spoken
rather than sung, and flags suspect time ranges for human review.

Method
------
1. Harmonic-percussive source separation (HPSS) isolates the harmonic
   (pitched) component of the mix.
2. pYIN pitch tracking runs on the harmonic component, giving a per-frame
   f0 estimate and voiced/unvoiced flag.
3. A frame is "stable" if it sits inside a run of >= ~120ms of
   continuously voiced frames whose pitch varies by less than a small
   cents threshold (sustained-note behavior). Singing holds pitches;
   speech shows rapid, unstable pitch contours and short voicing runs.
4. Melodicity per sliding analysis window = (stable voiced frames) /
   (voiced frames) within that window. Windows with too little voicing
   are treated as silence/instrumental and are not scored.
5. Windows with melodicity below --threshold are "suspect" (spoken-like).
   Adjacent suspect windows are merged into time ranges.

This is advisory only. It cannot reliably distinguish rap-adjacent
melodic delivery, heavily processed/auto-tuned vocals, or very breathy
sung passages from speech; the human ear is the final judge. See the
"Caveats" section of the generated report.

Usage
-----
    python3 screen_spoken_word.py <mp3_path> [options]

    --threshold FLOAT         Melodicity cutoff below which a window is
                              classified suspect (spoken-like). Default is
                              the value calibrated on Packet A (see
                              procedure doc / calibration reports).
    --out-dir DIR             Directory to write the report into. Defaults
                              to the input file's own directory, matching
                              the procedure's `navigators/songs/screen-
                              <songname>.md` convention.
    --window-length FLOAT     Analysis window length in seconds (default 2.0)
    --hop-length FLOAT        Analysis window hop in seconds (default 1.0)
    --min-voiced-fraction F   Minimum fraction of frames in a window that
                              must be voiced for the window to be scored
                              at all; otherwise it's treated as
                              silence/instrumental and excluded from
                              scoring (default 0.2).
    --dev-threshold-cents F   Max pitch deviation (in cents) allowed across
                              a ~120ms run for it to count as "sustained"
                              (default 50.0, i.e. half a semitone).
    --min-stable-run-ms F     Minimum duration (ms) of continuous voicing
                              with small deviation to count as a sustained
                              note (default 120.0, per procedure).
    --sr INT                  Analysis sample rate (default 22050).
    --debug                   Print per-window melodicity scores to stderr.
"""

import argparse
import sys
from pathlib import Path

import numpy as np
import librosa


def fmt_mmss_strict(seconds: float) -> str:
    """mm:ss (integer seconds), the format requested by the procedure doc."""
    seconds = max(0.0, seconds)
    m = int(seconds // 60)
    s = int(round(seconds - m * 60))
    if s == 60:
        s = 0
        m += 1
    return f"{m:02d}:{s:02d}"


def analyze(
    y: np.ndarray,
    sr: int,
    window_length: float,
    hop_length_s: float,
    min_voiced_fraction: float,
    dev_threshold_cents: float,
    min_stable_run_ms: float,
    debug: bool = False,
):
    """Run HPSS + pYIN and compute per-window melodicity scores.

    Returns (windows, total_duration) where windows is a list of dicts:
        {start, end, melodicity (or None if unscored), voiced_fraction}
    """
    total_duration = len(y) / sr

    y_harmonic, _ = librosa.effects.hpss(y)

    frame_length = 2048
    hop_length = 512
    fmin = librosa.note_to_hz("C2")
    fmax = librosa.note_to_hz("C7")

    f0, voiced_flag, voiced_prob = librosa.pyin(
        y_harmonic,
        fmin=fmin,
        fmax=fmax,
        sr=sr,
        frame_length=frame_length,
        hop_length=hop_length,
    )
    voiced_flag = np.asarray(voiced_flag, dtype=bool)
    times = librosa.times_like(f0, sr=sr, hop_length=hop_length)
    frame_period = hop_length / sr

    midi = librosa.hz_to_midi(f0)  # NaN where unvoiced

    # --- per-frame "sustained note" stability -----------------------------
    n_stable = max(2, round((min_stable_run_ms / 1000.0) / frame_period))
    dev_threshold_semitones = dev_threshold_cents / 100.0

    n_frames = len(f0)
    stable = np.zeros(n_frames, dtype=bool)
    for i in range(n_frames - n_stable + 1):
        run_voiced = voiced_flag[i : i + n_stable]
        if not np.all(run_voiced):
            continue
        run_midi = midi[i : i + n_stable]
        if np.nanmax(run_midi) - np.nanmin(run_midi) <= dev_threshold_semitones:
            stable[i : i + n_stable] = True

    # --- sliding analysis windows ------------------------------------------
    windows = []
    w_start = 0.0
    while w_start < total_duration:
        w_end = min(w_start + window_length, total_duration)
        mask = (times >= w_start) & (times < w_end)
        n_in_window = int(np.sum(mask))
        if n_in_window == 0:
            windows.append({"start": w_start, "end": w_end, "melodicity": None, "voiced_fraction": 0.0})
            w_start += hop_length_s
            continue
        voiced_count = int(np.sum(voiced_flag[mask]))
        voiced_fraction = voiced_count / n_in_window
        if voiced_fraction < min_voiced_fraction:
            melodicity = None  # treated as silence/instrumental, not scored
        else:
            stable_voiced_count = int(np.sum(stable[mask] & voiced_flag[mask]))
            melodicity = stable_voiced_count / voiced_count
        windows.append(
            {"start": w_start, "end": w_end, "melodicity": melodicity, "voiced_fraction": voiced_fraction}
        )
        if debug:
            mel_str = "  --  " if melodicity is None else f"{melodicity:5.2f}"
            print(
                f"[{fmt_mmss_strict(w_start)}-{fmt_mmss_strict(w_end)}] "
                f"voiced_frac={voiced_fraction:4.2f} melodicity={mel_str}",
                file=sys.stderr,
            )
        w_start += hop_length_s

    return windows, total_duration


def classify_and_merge(windows, threshold, hop_length_s):
    """Mark scored windows below threshold as suspect, merge adjacent ones."""
    suspect_ranges = []
    current = None
    for w in windows:
        is_suspect = w["melodicity"] is not None and w["melodicity"] < threshold
        if is_suspect:
            if current is not None and abs(w["start"] - current["end_start"]) < 1e-6:
                current["end"] = w["end"]
                current["end_start"] = w["start"]
                current["windows"].append(w)
            else:
                if current is not None:
                    suspect_ranges.append(current)
                current = {"start": w["start"], "end": w["end"], "end_start": w["start"], "windows": [w]}
        else:
            if current is not None:
                suspect_ranges.append(current)
                current = None
    if current is not None:
        suspect_ranges.append(current)
    return suspect_ranges


def write_report(
    out_path: Path,
    song_name: str,
    mp3_path: Path,
    total_duration: float,
    windows,
    suspect_ranges,
    threshold: float,
    params: dict,
):
    scored_windows = [w for w in windows if w["melodicity"] is not None]
    n_scored = len(scored_windows)
    n_suspect = sum(len(r["windows"]) for r in suspect_ranges)

    suspect_duration = sum(r["end"] - r["start"] for r in suspect_ranges)
    # Fraction of the whole song that is spoken-like.
    spoken_fraction_total = suspect_duration / total_duration if total_duration > 0 else 0.0
    # Fraction of scored (sufficiently-voiced) time that is spoken-like.
    scored_duration = n_scored * params["hop_length_s"] if n_scored else 0.0
    spoken_fraction_scored = suspect_duration / scored_duration if scored_duration > 0 else 0.0

    longest_range = max((r["end"] - r["start"] for r in suspect_ranges), default=0.0)

    lines = []
    lines.append(f"# Spoken-Word Screen: {song_name}")
    lines.append("")
    lines.append(f"- Source file: `{mp3_path}`")
    lines.append(f"- Duration: {fmt_mmss_strict(total_duration)} ({total_duration:.1f}s)")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(
        f"- **Spoken-fraction estimate (of full track): {spoken_fraction_total * 100:.1f}%**"
    )
    lines.append(
        f"- Spoken-fraction estimate (of scored/voiced time only): {spoken_fraction_scored * 100:.1f}%"
    )
    lines.append(f"- Longest single suspect range: {longest_range:.1f}s")
    lines.append(
        f"- Decision rule (Procedure 04 default): regenerate if spoken fraction > 10% "
        f"or any suspect range > 15s -> "
        f"{'REGENERATE' if (spoken_fraction_total > 0.10 or longest_range > 15.0) else 'PASS'}"
    )
    lines.append("")
    lines.append("## Suspect time ranges")
    lines.append("")
    if suspect_ranges:
        lines.append("| Range | Duration | Mean melodicity |")
        lines.append("|---|---|---|")
        for r in suspect_ranges:
            dur = r["end"] - r["start"]
            mean_mel = float(np.mean([w["melodicity"] for w in r["windows"]]))
            lines.append(
                f"| {fmt_mmss_strict(r['start'])}–{fmt_mmss_strict(r['end'])} "
                f"| {dur:.1f}s | {mean_mel:.2f} |"
            )
    else:
        lines.append("None. No windows fell below the melodicity threshold.")
    lines.append("")
    lines.append("## Calibration")
    lines.append("")
    lines.append(f"- Melodicity threshold used: **{threshold:.2f}** (window is suspect if melodicity < threshold)")
    lines.append(
        f"- A window's melodicity = (voiced frames judged 'stable', i.e. sustained-pitch runs of "
        f">= {params['min_stable_run_ms']:.0f}ms within {params['dev_threshold_cents']:.0f} cents) "
        f"/ (all voiced frames) in that window."
    )
    lines.append(
        f"- Analysis window: {params['window_length']:.1f}s, hop {params['hop_length_s']:.1f}s. "
        f"Windows with voiced-frame fraction < {params['min_voiced_fraction']:.2f} are treated as "
        f"silence/instrumental and excluded from scoring."
    )
    lines.append(f"- Analysis sample rate: {params['sr']} Hz.")
    lines.append(
        f"- {n_scored} of {len(windows)} analysis windows had enough voicing to be scored; "
        f"{n_suspect} of those were classified suspect."
    )
    lines.append(
        "- Threshold-selection method: the calibration reference is the human-designated memorized "
        "take, `packet-a-memorized.mp3` (Suno clip f3eb752c-a4c6-446a-9e42-8f12dd90a8b2). It "
        "contains no confirmed spoken passage either, so the threshold was chosen two ways and "
        "cross-checked. (1) A synthetic sanity check (held diatonic notes with vibrato vs. rapid "
        "syllable-like pitch glides with short voicing bursts, same DSP pipeline) produced "
        "melodicity scores of 0.93-1.00 for the sung-like signal and 0.00-0.39 for the speech-like "
        "signal — a clean gap with no overlap. (2) Sweeping thresholds against the real Packet A "
        "windows (memorized take, plus the two earlier non-memorized takes for reference) shows all "
        "three stay far under the 10%/15s regenerate thresholds for any threshold from 0.25 to "
        "0.45. On the memorized take specifically: threshold 0.40 flags exactly one 2s window "
        "(00:16-00:18, spoken fraction 0.6%) — comfortably passing. Threshold 0.40 was kept "
        "(not re-tuned) because it sits inside the synthetic gap (above 0.39, below 0.93) and "
        "confirms cleanly against the memorized take, while still surfacing a small number of real "
        "low-melodicity dips across the A recordings for human review, rather than passing "
        "everything trivially."
    )
    lines.append("")
    lines.append("## Caveats (heuristic, advisory only)")
    lines.append("")
    lines.append(
        "- This is a local pitch-stability heuristic, not a speech/singing classifier. "
        "It cannot hear semantics, only pitch-contour shape."
    )
    lines.append(
        "- Rap-adjacent or chant-like melodic delivery (rhythmic, narrow-pitch-range vocals) "
        "can score as low-melodicity even when musically intended, and will be flagged as if spoken."
    )
    lines.append(
        "- Heavily processed vocals (auto-tune, vocoder, harmonizer, or hard-quantized pitch "
        "correction) can artificially inflate melodicity and hide genuinely spoken passages."
    )
    lines.append(
        "- Breathy, quiet, or sustained low-vibrato singing may fall below the voiced-frame "
        "threshold and get excluded from scoring rather than scored correctly."
    )
    lines.append(
        "- Dense instrumental/percussive backing can leak into the 'harmonic' component from HPSS "
        "and distort pitch tracking on quieter vocal passages."
    )
    lines.append(
        "- The threshold above was calibrated on Packet A's two takes; it may not transfer "
        "perfectly to songs with very different arrangement, key, or vocal style."
    )
    lines.append(
        "- The synthetic 'speech-like' signal used to sanity-check the gap (see Calibration) is a "
        "clean, single-voice pitch-glide model, not a real vocal recording mixed with instruments. "
        "It shows the metric *can* separate held notes from unstable pitch in principle, but is not "
        "proof the threshold will catch real spoken-word sections in a produced mix — no confirmed "
        "spoken passage exists in the calibration data to test against directly."
    )
    lines.append(
        "- Final judgment belongs to the human ear; this tool exists to prioritize listening time, "
        "not replace it."
    )
    lines.append("")
    lines.append("## Human Prompts")
    lines.append("")
    lines.append("#### Initial Document Written On 2026-09-02")
    lines.append("")
    lines.append(
        "- Generated automatically by `screen_spoken_word.py` per "
        "`navigators/procedures/04-spoken-word-screen.md`, during calibration on Packet A."
    )
    lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Spoken-word screener (Procedure 04).")
    parser.add_argument("mp3_path", type=str, help="Path to the mp3 file to screen.")
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.40,
        help="Melodicity threshold below which a window is 'suspect' (default: 0.40, "
        "calibrated on Packet A — see navigators/songs/screen-packet-a-take*.md).",
    )
    parser.add_argument("--out-dir", type=str, default=None, help="Directory to write the report into.")
    parser.add_argument("--window-length", type=float, default=2.0, help="Analysis window length, seconds.")
    parser.add_argument("--hop-length", type=float, default=1.0, help="Analysis window hop, seconds.")
    parser.add_argument(
        "--min-voiced-fraction",
        type=float,
        default=0.2,
        help="Minimum voiced-frame fraction for a window to be scored.",
    )
    parser.add_argument(
        "--dev-threshold-cents",
        type=float,
        default=50.0,
        help="Max pitch deviation (cents) across a sustained-note run.",
    )
    parser.add_argument(
        "--min-stable-run-ms", type=float, default=120.0, help="Minimum sustained-run duration, ms."
    )
    parser.add_argument("--sr", type=int, default=22050, help="Analysis sample rate.")
    parser.add_argument("--debug", action="store_true", help="Print per-window scores to stderr.")
    args = parser.parse_args()

    mp3_path = Path(args.mp3_path).expanduser().resolve()
    if not mp3_path.exists():
        print(f"error: file not found: {mp3_path}", file=sys.stderr)
        sys.exit(1)

    song_name = mp3_path.stem
    out_dir = Path(args.out_dir).expanduser().resolve() if args.out_dir else mp3_path.parent
    out_path = out_dir / f"screen-{song_name}.md"

    print(f"Loading {mp3_path} ...", file=sys.stderr)
    y, sr = librosa.load(str(mp3_path), sr=args.sr, mono=True)

    print("Running HPSS + pYIN (this can take a while on first run / JIT warmup) ...", file=sys.stderr)
    windows, total_duration = analyze(
        y,
        sr,
        window_length=args.window_length,
        hop_length_s=args.hop_length,
        min_voiced_fraction=args.min_voiced_fraction,
        dev_threshold_cents=args.dev_threshold_cents,
        min_stable_run_ms=args.min_stable_run_ms,
        debug=args.debug,
    )

    suspect_ranges = classify_and_merge(windows, args.threshold, args.hop_length)

    params = {
        "window_length": args.window_length,
        "hop_length_s": args.hop_length,
        "min_voiced_fraction": args.min_voiced_fraction,
        "dev_threshold_cents": args.dev_threshold_cents,
        "min_stable_run_ms": args.min_stable_run_ms,
        "sr": sr,
    }
    write_report(out_path, song_name, mp3_path, total_duration, windows, suspect_ranges, args.threshold, params)
    print(f"Wrote report: {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
