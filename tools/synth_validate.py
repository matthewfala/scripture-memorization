"""Synthetic sanity check for screen_spoken_word.py's melodicity metric.

We have no known-spoken recording to test against (only two known-sung
Packet A takes), so this builds two synthetic signals with a real
soundfile-based fundamental + harmonics, run through the *same* analyze()
function, to confirm the metric actually separates "sustained held notes"
from "rapidly modulated pitch with short voicing bursts" before we trust a
calibration threshold chosen only from Packet A's own distribution.
"""
import numpy as np
import soundfile as sf
import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-fala-Music-scripture-memorization/39500d8f-25b4-4253-ac0a-4a80d40e145e/scratchpad")
from screen_spoken_word import analyze

sr = 22050


def synth_harmonic(f0_contour, sr, n_harmonics=5, voiced_mask=None):
    n = len(f0_contour)
    t = np.arange(n) / sr
    phase = 2 * np.pi * np.cumsum(f0_contour) / sr
    y = np.zeros(n)
    for h in range(1, n_harmonics + 1):
        y += (1.0 / h) * np.sin(h * phase)
    y /= np.max(np.abs(y))
    if voiced_mask is not None:
        y = y * voiced_mask
    # gentle noise floor
    y = y + 0.01 * np.random.randn(n)
    return y.astype(np.float32)


def make_sung(duration=20.0):
    n = int(duration * sr)
    t = np.arange(n) / sr
    # sequence of held notes (diatonic-ish), 1.2s each, with vibrato
    note_midis = [60, 62, 64, 65, 67, 65, 64, 62, 60, 64, 67, 72, 67, 64, 60, 62]
    note_dur = duration / len(note_midis)
    f0 = np.zeros(n)
    for i, midi in enumerate(note_midis):
        start = int(i * note_dur * sr)
        end = int((i + 1) * note_dur * sr)
        end = min(end, n)
        seg_t = t[start:end]
        base_hz = 440.0 * 2 ** ((midi - 69) / 12.0)
        vibrato = 1.0 * np.sin(2 * np.pi * 5.5 * seg_t)  # +-1 semitone-ish in cents scale below
        # vibrato depth ~ +-40 cents
        cents = 40 * np.sin(2 * np.pi * 5.5 * seg_t)
        hz = base_hz * (2 ** (cents / 1200.0))
        # short attack ramp to avoid a click, but stays voiced throughout (sustained)
        f0[start:end] = hz
    voiced_mask = np.ones(n)
    return synth_harmonic(f0, sr, voiced_mask=voiced_mask)


def make_speech_like(duration=20.0, seed=0):
    rng = np.random.RandomState(seed)
    n = int(duration * sr)
    t = np.arange(n) / sr
    f0 = np.zeros(n)
    voiced_mask = np.zeros(n)
    pos = 0
    base_hz = 150.0  # typical-ish pitch
    while pos < n:
        # "syllable" burst: 80-250ms voiced, then 40-120ms unvoiced gap
        burst_dur = rng.uniform(0.08, 0.25)
        gap_dur = rng.uniform(0.04, 0.12)
        burst_n = int(burst_dur * sr)
        gap_n = int(gap_dur * sr)
        end = min(pos + burst_n, n)
        seg_len = end - pos
        if seg_len > 0:
            seg_t = np.linspace(0, burst_dur, seg_len)
            # rapid pitch glide within the burst: random start/end pitch,
            # swinging several semitones within ~100-200ms (speech-like
            # intonation contour), not a sustained held pitch.
            start_semi = rng.uniform(-4, 4)
            end_semi = rng.uniform(-4, 4)
            semitone_contour = np.linspace(start_semi, end_semi, seg_len)
            # add a fast wobble on top so it's not even a clean linear glide
            semitone_contour += 1.5 * np.sin(2 * np.pi * 8 * seg_t + rng.uniform(0, 6.28))
            hz = base_hz * (2 ** (semitone_contour / 12.0))
            f0[pos:end] = hz
            voiced_mask[pos:end] = 1.0
        pos = end + gap_n
    return synth_harmonic(f0, sr, voiced_mask=voiced_mask)


np.random.seed(0)
sung = make_sung(20.0)
speech = make_speech_like(20.0, seed=1)

sf.write("synth_sung.wav", sung, sr)
sf.write("synth_speech.wav", speech, sr)

for name, y in [("SUNG (synthetic)", sung), ("SPEECH-LIKE (synthetic)", speech)]:
    windows, total = analyze(
        y, sr,
        window_length=2.0, hop_length_s=1.0,
        min_voiced_fraction=0.2,
        dev_threshold_cents=100.0,
        min_stable_run_ms=120.0,
        debug=False,
    )
    scored = [w["melodicity"] for w in windows if w["melodicity"] is not None]
    print(f"{name}: n_windows={len(windows)} scored={len(scored)} "
          f"mean_mel={np.mean(scored):.3f} min={np.min(scored):.3f} max={np.max(scored):.3f}")
    print("  per-window:", [round(m, 2) for m in scored])
