# Procedure 04 — Spoken-Word Screening (experimental)

## Purpose

Estimate how much of a generated song is spoken rather than sung, and flag
suspect time ranges. Spoken passages memorize far more slowly than sung
ones, and style-string guard clauses have been observed not to prevent
them — so generated audio is screened before the human invests listening
time. This is a heuristic, advisory tool: its flags guide regeneration and
human listening; the human ear is the final judge.

## Inputs

- An audio file in `navigators/songs/` (mp3).
- `navigators/songs/` also holds the Packet A song, used for calibration.

## Method — local DSP only

No cloud services and no LLMs. A Python script (virtualenv in the scratch
directory; dependencies: `librosa`, `numpy`, `soundfile`) that:

1. Loads the audio and applies harmonic–percussive separation; runs pYIN
   pitch tracking on the harmonic component.
2. Scores **melodicity** per sliding window (~1 s hop): the fraction of
   voiced frames whose pitch is locally stable — sustained-note behavior,
   small deviation over 120 ms or longer. Singing holds pitches; speech
   shows rapid, unstable pitch contours and short voicing runs.
3. Classifies low-melodicity windows as suspect; merges adjacent suspect
   windows into time ranges.

## Calibration — required before trusting any flag

Run the screener on the Packet A song first (known memorized, predominantly
sung). Set the flag threshold so A's known-sung material passes. Report any
A regions the screener still flags — these are either A's genuinely spoken
moments or false positives; the human confirms which, and the threshold
choice is recorded in every report.

## Output

Per screened song: `navigators/songs/screen-<songname>.md` containing the
overall spoken-fraction estimate, suspect time ranges (mm:ss–mm:ss), the
calibration threshold used, and honest caveats.

## Decision rule (default; human may override per song)

- Spoken fraction > 10%, or any single suspect range longer than 15 s →
  regenerate once with the same style string.
- If the second take also fails → stop; record the observation (genre,
  what was spoken) in the `style-preferences.md` feedback log, and refer
  the style to the human for revision (Procedure 00 re-run).
- Generation attempts per packet are capped at 2 rounds without explicit
  human approval to continue.

## Rules

- Local computation only; no audio leaves the machine.
- The screener writes only its report files and (per the decision rule,
  with human confirmation) feedback-log entries — never lyrics, styles, or
  verse files.
- Reports must state that the method is a heuristic and what it cannot
  hear (e.g., rap-adjacent melodic delivery, heavily processed vocals).
- Do not commit; the human reviews first.

## Human Prompts

#### Initial Document Written On 2026-08-28

- If there was some automatic screening of the spoken word, perhaps that would be ideal - though if it uses cloud LLMs I'm thinking that would be costly and wasteful, and if not, I'm not sure a local model would be effective at detecting the spoken portions. *(Excerpt; full prompt recorded in `03-lyrics-format.md`.)*
- I'm logged into suno on chrome now. Can you please generate the 5 packets songs? Please store the song mp3 in the folder once generated. Ideally screen for the spoken words rather than sung and regenerate or change the style if so.
