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

## Spoken-word screening on vocal stems (preferred)

Full-mix melodicity cannot detect speech over pitched accompaniment
(Procedure 04, 2026-09-15 lesson). Screen the isolated vocal stem from
Suno's Get Stems instead:

```bash
tools/venv/bin/python3 tools/screen_spoken_word.py \
    navigators/songs/stems/packet-d-take1-vocals.mp3 \
    --threshold 0.65 --min-run 2 --out-dir navigators/songs
```

`--min-run 2` requires at least 2 consecutive suspect windows per
reported range, suppressing single-window blips. Stem-mode calibration
(2026-09-15): 0.65/min-run-2 catches all five human-labeled spoken spots
on `packet-d-take1` (13.8% spoken, REGENERATE) while the memorized
Packet A stem passes at 3.7%.

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

## Strict clean-sample tools (Procedure 04)

- `verify_lines.py STEM --lyrics-file L` — biased-prompt medium
  transcription; per-line FOUND / WEAK / NOT_FOUND with vocal-energy cue;
  writes `verify-<stem>.md` and a `.words.json` timeline.
- `check_topic_order.py WORDS_JSON --lyrics-file L` — v3 lyrics: confirms
  each topic is announced before and after its verses, in order.
- `probe_bookends.py STEM --lyrics-file L` — transcribes the opening and
  closing windows to confirm both "Packet X / Name" bookends are sung.

## Publishing

- `publish-official.sh` — uploads `navigators/official/` (mp3s + `index.html`)
  and a zip of all officials to the public S3 website bucket, plus
  `candidates/*.m4a` for packets still being chosen. Needs the
  `aws` CLI on the default profile. See Procedure 07.

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

#### Document Modification On 2026-09-02 (publishing)

- Can you add the official songs to an s3 bucket to be downloaded and have an index file which has the song portfolio please make it look nice and appropriate - a landing page for getting these songs. I give you permission to make a global s3 bucket in my aws account and put the official songs in it

#### Document Modification On 2026-09-15 (stem-based screening)

- Packet D, I like the sound, however there are portions that are spoken around 3:54 and 4:02 and 04:10 and 04:17 04:40. Is the automated detector able to be calibrated to detect this?
- I'm pretty sure suno has this feature, you can download the spoken section without the music on the website?

#### Document Modification On 2026-09-28

- Can we switch back to packet a's format? I'd like to focus on packet E. Can you please make sure we have 3 clean samples if possible? Can you also update the website to display all three samples for packet e? I'll listen to those and tell you which I'd like to lock.
