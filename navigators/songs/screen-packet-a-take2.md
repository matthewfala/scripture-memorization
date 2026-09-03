# Spoken-Word Screen: packet-a-take2

- Source file: `/Users/fala/Music/scripture-memorization/navigators/songs/packet-a-take2.mp3`
- Duration: 05:25 (324.6s)

## Summary

- **Spoken-fraction estimate (of full track): 1.8%**
- Spoken-fraction estimate (of scored/voiced time only): 1.9%
- Longest single suspect range: 2.0s
- Decision rule (Procedure 04 default): regenerate if spoken fraction > 10% or any suspect range > 15s -> PASS

## Suspect time ranges

| Range | Duration | Mean melodicity |
|---|---|---|
| 03:46–03:48 | 2.0s | 0.00 |
| 03:56–03:58 | 2.0s | 0.39 |
| 05:14–05:16 | 2.0s | 0.38 |

## Calibration

- Melodicity threshold used: **0.40** (window is suspect if melodicity < threshold)
- A window's melodicity = (voiced frames judged 'stable', i.e. sustained-pitch runs of >= 120ms within 50 cents) / (all voiced frames) in that window.
- Analysis window: 2.0s, hop 1.0s. Windows with voiced-frame fraction < 0.20 are treated as silence/instrumental and excluded from scoring.
- Analysis sample rate: 22050 Hz.
- 323 of 325 analysis windows had enough voicing to be scored; 3 of those were classified suspect.
- Threshold-selection method: the calibration reference is the human-designated memorized take, `packet-a-memorized.mp3` (Suno clip f3eb752c-a4c6-446a-9e42-8f12dd90a8b2). It contains no confirmed spoken passage either, so the threshold was chosen two ways and cross-checked. (1) A synthetic sanity check (held diatonic notes with vibrato vs. rapid syllable-like pitch glides with short voicing bursts, same DSP pipeline) produced melodicity scores of 0.93-1.00 for the sung-like signal and 0.00-0.39 for the speech-like signal — a clean gap with no overlap. (2) Sweeping thresholds against the real Packet A windows (memorized take, plus the two earlier non-memorized takes for reference) shows all three stay far under the 10%/15s regenerate thresholds for any threshold from 0.25 to 0.45. On the memorized take specifically: threshold 0.40 flags exactly one 2s window (00:16-00:18, spoken fraction 0.6%) — comfortably passing. Threshold 0.40 was kept (not re-tuned) because it sits inside the synthetic gap (above 0.39, below 0.93) and confirms cleanly against the memorized take, while still surfacing a small number of real low-melodicity dips across the A recordings for human review, rather than passing everything trivially.

## Caveats (heuristic, advisory only)

- This is a local pitch-stability heuristic, not a speech/singing classifier. It cannot hear semantics, only pitch-contour shape.
- Rap-adjacent or chant-like melodic delivery (rhythmic, narrow-pitch-range vocals) can score as low-melodicity even when musically intended, and will be flagged as if spoken.
- Heavily processed vocals (auto-tune, vocoder, harmonizer, or hard-quantized pitch correction) can artificially inflate melodicity and hide genuinely spoken passages.
- Breathy, quiet, or sustained low-vibrato singing may fall below the voiced-frame threshold and get excluded from scoring rather than scored correctly.
- Dense instrumental/percussive backing can leak into the 'harmonic' component from HPSS and distort pitch tracking on quieter vocal passages.
- The threshold above was calibrated on Packet A's two takes; it may not transfer perfectly to songs with very different arrangement, key, or vocal style.
- The synthetic 'speech-like' signal used to sanity-check the gap (see Calibration) is a clean, single-voice pitch-glide model, not a real vocal recording mixed with instruments. It shows the metric *can* separate held notes from unstable pitch in principle, but is not proof the threshold will catch real spoken-word sections in a produced mix — no confirmed spoken passage exists in the calibration data to test against directly.
- Final judgment belongs to the human ear; this tool exists to prioritize listening time, not replace it.

## Human Prompts

#### Initial Document Written On 2026-09-02

- Generated automatically by `screen_spoken_word.py` per `navigators/procedures/04-spoken-word-screen.md`, during calibration on Packet A.
