# tools/ — Song Screening Scripts (Procedure 04)

Local-only screening for generated songs: no cloud services, no LLMs;
faster-whisper model weights download once from Hugging Face and cache
locally, then all inference is on-device.

## Setup (one-time)

```bash
python3 -m venv tools/venv
tools/venv/bin/pip install -r tools/requirements.txt
```

Python 3.9+ on macOS; libsndfile (bundled with the `soundfile` wheel)
decodes the mp3s directly — no ffmpeg needed.

## Screening a song (the normal entry point)

```bash
tools/venv/bin/python3 tools/screen_song.py navigators/songs/packet-b-take1.mp3 \
    --lyrics-file navigators/lyrics/packet-b.md
```

Writes `screen-<songname>.md` next to the mp3 (override with `--out-dir`).
Runs both checks: melodicity (spoken-word) and lyric fidelity. One song
per invocation; a ~5-minute song takes roughly 1–3 minutes on CPU
(transcription dominates). Packet A uses `--lyrics-file
navigators/lyrics/packet-a.md` like every other packet (`--lyrics-v1a`
is a legacy fallback that parses the same text out of Procedure 03).

Key options: `--whisper-model small|medium` (small screens; medium
verifies structural findings — see Procedure 04), `--melodicity-threshold`
(default 0.40, calibrated), `--lyric-noise-threshold` (default 0.70,
calibrated against the Packet A baseline).

## Files

- `screen_song.py` — combined runner; writes the per-song report.
- `screen_spoken_word.py` — melodicity module (HPSS → pYIN → stable-pitch
  windows). Can run standalone for spoken-word-only screening.
- `lyric_fidelity.py` — transcription + global edit-distance alignment
  against the expected lyric lines; also holds the lyrics-file loaders.
- `calibrate_lyric_baseline.py` — recompute the transcriber-noise baseline
  on `packet-a-memorized.mp3`.
- `synth_validate.py` / `synth_validate_lyrics.py` — synthetic sanity
  checks (held notes vs. speech-like glides; known-defect lyric cases).
  Run these after any dependency upgrade to confirm the pipeline still
  separates sung from spoken and catches missing/repeated lines.

## Calibration provenance

Thresholds were calibrated 2026-09-02 against the human's memorized
Packet A take (`navigators/songs/packet-a-memorized.mp3`): melodicity
0.40 (synthetic sung/speech gap 0.93–1.00 vs 0.00–0.39), lyric-noise
0.70 (A baseline WER 5.3% with the small model). Recalibrate per
Procedure 04 if dependencies change or a new calibration reference is
designated.

## Human Prompts

#### Initial Document Written On 2026-09-02

- Are the procedures repeatable by another context?
- Yes please add these to a new folder in the root repo. Please also add process to copy the official song to another folder denoting the official songs. Please make the entire pipeline process completely repeatable including the file naming conventions and what files to update after when etc.
