#!/usr/bin/env python3
"""
Combined song screener (Procedure 04 — navigators/procedures/04-spoken-word-screen.md).

Runs BOTH checks on a single song in one process:
  1. Spoken-word / melodicity screening (harmonic-percussive separation +
     pYIN pitch-stability heuristic; see screen_spoken_word.py).
  2. Lyric-fidelity checking (local faster-whisper transcription, aligned
     against the song's expected lyrics; see lyric_fidelity.py).

No cloud services, no LLMs. All computation and model inference is local.

Usage
-----
    python3 screen_song.py <mp3_path> --lyrics-file <path/to/packet-X.md> [options]
    python3 screen_song.py <mp3_path> --lyrics-v1a [options]     # Packet A v1 calibration lyrics

Key options
-----------
    --melodicity-threshold F   Default 0.40 (see screen_spoken_word.py calibration).
    --lyric-noise-threshold F  Max per-line word-error fraction still counted as
                               "transcriber uncertainty" rather than "altered".
                               Default 0.70 (calibrated on packet-a-memorized.mp3;
                               see screen-packet-a-memorized.md).
    --whisper-model NAME       faster-whisper model size (default "small").
    --out-dir DIR              Defaults to the mp3's own directory.
"""

import argparse
import sys
import time
from pathlib import Path

import numpy as np
import librosa

sys.path.insert(0, str(Path(__file__).resolve().parent))
from screen_spoken_word import analyze as melodicity_analyze, classify_and_merge, fmt_mmss_strict
from lyric_fidelity import analyze_lyric_fidelity, load_v1_packet_a_lyrics, load_v2_lyrics

DEFAULT_MELODICITY_THRESHOLD = 0.40
# Calibrated on packet-a-memorized.mp3 (v1 lyrics, 64 lines): after fixing the
# whisper letter+digit tokenization gap, per-line WER on the known-correct
# baseline was 0 for 49/64 lines and topped out at 0.67 for a systematic ASR
# quirk (adjacent chapter/verse number words collapsing into one "year-like"
# 4-digit token, e.g. "eighteen twenty" -> "1820"), with a single one-word
# outlier at 1.00 ("Witnessing" misheard as "missing"). 0.70 sits just above
# the systematic-noise band; the single-word outlier remains a known residual
# false positive on A, reported and left for human confirmation (same
# treatment as residual melodicity flags on A).
DEFAULT_LYRIC_NOISE_THRESHOLD = 0.70


def transcribe(mp3_path: str, model_size: str, cpu_threads: int = 8) -> str:
    from faster_whisper import WhisperModel

    model = WhisperModel(model_size, device="cpu", compute_type="int8", cpu_threads=cpu_threads)
    segments, info = model.transcribe(
        mp3_path,
        language="en",
        vad_filter=False,
        beam_size=5,
        condition_on_previous_text=False,
    )
    texts = [s.text for s in segments]
    return " ".join(texts), info


def write_combined_report(
    out_path: Path,
    song_name: str,
    mp3_path: Path,
    total_duration: float,
    mel_windows,
    suspect_ranges,
    mel_threshold: float,
    mel_params: dict,
    fidelity,
    lyric_noise_threshold: float,
    transcript_text: str,
    whisper_model: str,
    lyrics_source: str,
):
    suspect_duration = sum(r["end"] - r["start"] for r in suspect_ranges)
    spoken_fraction_total = suspect_duration / total_duration if total_duration > 0 else 0.0
    longest_range = max((r["end"] - r["start"] for r in suspect_ranges), default=0.0)
    mel_fail = spoken_fraction_total > 0.10 or longest_range > 15.0
    lyric_fail = fidelity.structural_failure
    overall_verdict = "FAIL" if (mel_fail or lyric_fail) else "PASS"

    lines = []
    lines.append(f"# Song Screen: {song_name}")
    lines.append("")
    lines.append(f"- Source file: `{mp3_path}`")
    lines.append(f"- Duration: {fmt_mmss_strict(total_duration)} ({total_duration:.1f}s)")
    lines.append(f"- Expected lyrics source: `{lyrics_source}`")
    lines.append(f"- Transcription model: faster-whisper `{whisper_model}` (local CPU, int8)")
    lines.append("")
    lines.append(f"## Verdict: {overall_verdict}")
    lines.append("")
    lines.append(
        f"- Spoken-word check: {'FAIL' if mel_fail else 'PASS'} "
        f"(spoken fraction {spoken_fraction_total*100:.1f}%, longest suspect range {longest_range:.1f}s)"
    )
    lines.append(
        f"- Lyric-fidelity check: {'FAIL' if lyric_fail else 'PASS'} "
        f"(overall WER {fidelity.overall_wer*100:.1f}%, "
        f"{fidelity.n_missing} missing / {fidelity.n_altered} altered / "
        f"{fidelity.n_uncertain} transcriber-uncertain lines, {len(fidelity.repeats)} repeat finding(s))"
    )
    lines.append("")

    # --- Spoken-word section ---
    lines.append("## Spoken-Word Screen")
    lines.append("")
    lines.append(f"- **Spoken-fraction estimate (of full track): {spoken_fraction_total*100:.1f}%**")
    lines.append(f"- Longest single suspect range: {longest_range:.1f}s")
    lines.append(f"- Melodicity threshold used: **{mel_threshold:.2f}** (calibrated on packet-a-memorized.mp3; see screen-packet-a-memorized.md)")
    lines.append("")
    lines.append("### Suspect time ranges")
    lines.append("")
    if suspect_ranges:
        lines.append("| Range | Duration | Mean melodicity |")
        lines.append("|---|---|---|")
        for r in suspect_ranges:
            dur = r["end"] - r["start"]
            mean_mel = float(np.mean([w["melodicity"] for w in r["windows"]]))
            lines.append(f"| {fmt_mmss_strict(r['start'])}–{fmt_mmss_strict(r['end'])} | {dur:.1f}s | {mean_mel:.2f} |")
    else:
        lines.append("None. No windows fell below the melodicity threshold.")
    lines.append("")

    # --- Lyric-fidelity section ---
    lines.append("## Lyric-Fidelity Check")
    lines.append("")
    lines.append(f"- Overall word-error estimate: **{fidelity.overall_wer*100:.1f}%** ({fidelity.ref_token_count} reference words)")
    lines.append(f"- Per-line noise threshold (transcriber-uncertainty ceiling): **{lyric_noise_threshold:.2f}** (calibrated on packet-a-memorized.mp3)")
    lines.append(f"- Lines: {len(fidelity.lines)} total, {fidelity.n_missing} missing, {fidelity.n_altered} altered, {fidelity.n_uncertain} transcriber-uncertain (passing), rest exact.")
    lines.append("")
    problem_lines = [l for l in fidelity.lines if l.status in ("missing", "altered")]
    lines.append("### Missing / altered lines (structural)")
    lines.append("")
    if problem_lines:
        lines.append("| # | Status | Expected | Heard |")
        lines.append("|---|---|---|---|")
        for l in problem_lines:
            exp_trunc = l.text if len(l.text) <= 90 else l.text[:87] + "..."
            heard_trunc = l.heard_text if len(l.heard_text) <= 60 else l.heard_text[:57] + "..."
            lines.append(f"| {l.index+1} | {l.status.upper()} (wer={l.line_wer:.2f}) | {exp_trunc} | {heard_trunc or '(nothing)'} |")
    else:
        lines.append("None.")
    lines.append("")
    uncertain_lines = [l for l in fidelity.lines if l.status == "uncertain"]
    lines.append("### Transcriber-uncertain lines (passing; ASR noise only)")
    lines.append("")
    if uncertain_lines:
        lines.append("| # | wer | Expected | Heard |")
        lines.append("|---|---|---|---|")
        for l in uncertain_lines:
            exp_trunc = l.text if len(l.text) <= 90 else l.text[:87] + "..."
            heard_trunc = l.heard_text if len(l.heard_text) <= 60 else l.heard_text[:57] + "..."
            lines.append(f"| {l.index+1} | {l.line_wer:.2f} | {exp_trunc} | {heard_trunc} |")
    else:
        lines.append("None.")
    lines.append("")
    lines.append("### Repeated-beyond-format findings")
    lines.append("")
    if fidelity.repeats:
        lines.append("| Text | Expected count | Observed count |")
        lines.append("|---|---|---|")
        for r in fidelity.repeats:
            txt_trunc = r.text if len(r.text) <= 70 else r.text[:67] + "..."
            lines.append(f"| {txt_trunc} | {r.expected_count} | {r.observed_count} |")
    else:
        lines.append("None.")
    lines.append("")

    # --- Calibration ---
    lines.append("## Calibration")
    lines.append("")
    lines.append(
        "- Calibration reference: `packet-a-memorized.mp3` (Suno clip "
        "f3eb752c-a4c6-446a-9e42-8f12dd90a8b2), the human-designated memorized take."
    )
    lines.append(f"- Melodicity threshold: {mel_threshold:.2f} (window suspect if melodicity < threshold); window {mel_params['window_length']:.1f}s / hop {mel_params['hop_length_s']:.1f}s.")
    lines.append(
        f"- Lyric-fidelity noise threshold: {lyric_noise_threshold:.2f} — a line's (substitutions+deletions)/length "
        "must exceed this to count as 'altered' rather than ordinary transcriber uncertainty. Calibrated by "
        "transcribing packet-a-memorized.mp3 (known-correct v1 lyrics, 64 lines) and inspecting the per-line "
        "word-error distribution: 49/64 lines were exact, most of the rest were small ASR noise (dropped short "
        "words, minor substitutions), and the noise topped out at 0.67 for a systematic ASR quirk — adjacent "
        "chapter/verse number words collapsing into one 'year-like' 4-digit token (e.g. 'eighteen twenty' -> "
        "'1820'). 0.70 sits just above that systematic-noise band. One single-word line ('Witnessing' misheard "
        "as 'missing', wer=1.00) still exceeds it on the calibration baseline itself and is reported there as a "
        "known residual false positive, for the same reason a one-word line has no middle ground between 0% and "
        "100% word-error — this mirrors how the melodicity check accepts a small number of residual flags on "
        "Packet A for human confirmation rather than tuning them away entirely."
    )
    lines.append("")

    # --- Caveats ---
    lines.append("## Caveats (heuristic, advisory only)")
    lines.append("")
    lines.append("- Both checks are local heuristics, not ground truth. The human ear is the final judge.")
    lines.append("- Spoken-word check: cannot reliably distinguish rap-adjacent/chant-like melodic delivery from speech; heavily processed vocals (auto-tune/vocoder) can hide genuinely spoken passages; breathy or quiet singing may drop out of scoring; dense percussive backing can leak into the harmonic component and distort pitch tracking.")
    lines.append("- Lyric-fidelity check: transcription is imperfect, especially for short letter+number designators (e.g. 'Bee One' is often heard by the ASR as 'B1' or similar compact forms) — this is exactly the kind of noise the calibrated threshold is meant to absorb, but an unusually noisy passage can still push a genuinely-correct line over the threshold.")
    lines.append("- The word-level alignment is a single global edit-distance alignment against the whole song; when the reference contains repeated text (the reference-sandwich pattern) and a nearby line is genuinely missing or reordered, the alignment can misattribute matched words to the wrong occurrence, which may show as a confusing diff on an adjacent line. Repeat detection is a best-effort substring check restricted to hypothesis text not already claimed by another line's alignment, to avoid false positives from coincidental phrase overlap (e.g. a topic name that is also a literal substring of the following verse) — this can occasionally under-count a real repeat if it sits immediately next to an unrelated missing/altered line, though in that case the take already fails on the other grounds.")
    lines.append("- No cloud services were used for either check; faster-whisper model weights are downloaded once from Hugging Face and cached locally, then all inference runs on-device.")
    lines.append("- Final judgment belongs to the human ear; this tool exists to prioritize listening time, not replace it.")
    lines.append("")

    lines.append("## Human Prompts")
    lines.append("")
    lines.append("#### Initial Document Written On 2026-09-02")
    lines.append("")
    lines.append(
        "- Generated automatically by `screen_song.py` per `navigators/procedures/04-spoken-word-screen.md` "
        "(spoken-word + lyric-fidelity screening pass)."
    )
    lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    return overall_verdict, spoken_fraction_total, longest_range, fidelity.overall_wer


def main():
    parser = argparse.ArgumentParser(description="Combined spoken-word + lyric-fidelity screener (Procedure 04).")
    parser.add_argument("mp3_path", type=str)
    parser.add_argument("--lyrics-file", type=str, default=None, help="Path to a v2 packet-<letter>.md file.")
    parser.add_argument("--lyrics-v1a", action="store_true", help="Use Packet A's v1 calibration lyrics.")
    parser.add_argument("--procedure-03-path", type=str,
                         default=str(Path(__file__).resolve().parents[1]
                                     / "navigators" / "procedures" / "03-lyrics-format.md"))
    parser.add_argument("--melodicity-threshold", type=float, default=DEFAULT_MELODICITY_THRESHOLD)
    parser.add_argument("--lyric-noise-threshold", type=float, default=DEFAULT_LYRIC_NOISE_THRESHOLD)
    parser.add_argument("--whisper-model", type=str, default="small")
    parser.add_argument("--cpu-threads", type=int, default=8)
    parser.add_argument("--out-dir", type=str, default=None)
    parser.add_argument("--sr", type=int, default=22050)
    args = parser.parse_args()

    mp3_path = Path(args.mp3_path).expanduser().resolve()
    if not mp3_path.exists():
        print(f"error: file not found: {mp3_path}", file=sys.stderr)
        sys.exit(1)

    if args.lyrics_v1a:
        expected_lines = load_v1_packet_a_lyrics(args.procedure_03_path)
        lyrics_source = args.procedure_03_path + " (v1 Packet Ay example, Human Prompts)"
    elif args.lyrics_file:
        expected_lines = load_v2_lyrics(args.lyrics_file)
        lyrics_source = args.lyrics_file
    else:
        print("error: must pass --lyrics-file or --lyrics-v1a", file=sys.stderr)
        sys.exit(1)

    song_name = mp3_path.stem
    out_dir = Path(args.out_dir).expanduser().resolve() if args.out_dir else mp3_path.parent
    out_path = out_dir / f"screen-{song_name}.md"

    print(f"[{song_name}] loading audio...", file=sys.stderr)
    y, sr = librosa.load(str(mp3_path), sr=args.sr, mono=True)
    total_duration = len(y) / sr

    print(f"[{song_name}] melodicity analysis (HPSS + pYIN)...", file=sys.stderr)
    t0 = time.time()
    mel_windows, _ = melodicity_analyze(
        y, sr,
        window_length=2.0, hop_length_s=1.0,
        min_voiced_fraction=0.2, dev_threshold_cents=50.0, min_stable_run_ms=120.0,
        debug=False,
    )
    print(f"[{song_name}] melodicity done in {time.time()-t0:.1f}s", file=sys.stderr)
    suspect_ranges = classify_and_merge(mel_windows, args.melodicity_threshold, 1.0)
    mel_params = {"window_length": 2.0, "hop_length_s": 1.0}

    print(f"[{song_name}] transcribing (faster-whisper {args.whisper_model})...", file=sys.stderr)
    t0 = time.time()
    transcript_text, info = transcribe(str(mp3_path), args.whisper_model, args.cpu_threads)
    print(f"[{song_name}] transcription done in {time.time()-t0:.1f}s "
          f"(lang={info.language} p={info.language_probability:.2f})", file=sys.stderr)

    print(f"[{song_name}] aligning lyrics ({len(expected_lines)} expected lines)...", file=sys.stderr)
    fidelity = analyze_lyric_fidelity(expected_lines, transcript_text, noise_threshold=args.lyric_noise_threshold)

    verdict, spoken_frac, longest, wer = write_combined_report(
        out_path, song_name, mp3_path, total_duration,
        mel_windows, suspect_ranges, args.melodicity_threshold, mel_params,
        fidelity, args.lyric_noise_threshold, transcript_text, args.whisper_model, lyrics_source,
    )
    print(f"[{song_name}] VERDICT={verdict} spoken_frac={spoken_frac*100:.1f}% longest={longest:.1f}s wer={wer*100:.1f}%", file=sys.stderr)
    print(f"Wrote report: {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
