# Procedure 04 — Song Screening (experimental)

## Purpose

Screen generated songs on two dimensions before the human invests
listening time:

1. **Spoken-word screening** — estimate how much of the song is spoken
   rather than sung, and flag suspect time ranges. Spoken passages
   memorize far more slowly than sung ones, and style-string guard clauses
   have been observed not to prevent them.
2. **Lyric fidelity** — verify the sung words match the lyrics file
   exactly. A take that drops, alters, or repeats lines must not become
   memorized material.

Both are heuristic, advisory tools: flags guide regeneration and human
listening; the human ear is the final judge.

## Inputs

- An audio file in `navigators/songs/` (mp3).
- `navigators/songs/` also holds the Packet A song, used for calibration.

## Implementation

The scripts live in `tools/` at the repo root (`screen_song.py` is the
entry point); setup, invocation, and calibration provenance are in
`tools/README.md`. Packet A's expected lyrics are
`navigators/lyrics/packet-a.md`.

## Method — local DSP only

No cloud services and no LLMs. A Python script (dependencies: `librosa`,
`numpy`, `soundfile`) that:

1. Loads the audio and applies harmonic–percussive separation; runs pYIN
   pitch tracking on the harmonic component.
2. Scores **melodicity** per sliding window (~1 s hop): the fraction of
   voiced frames whose pitch is locally stable — sustained-note behavior,
   small deviation over 120 ms or longer. Singing holds pitches; speech
   shows rapid, unstable pitch contours and short voicing runs.
3. Classifies low-melodicity windows as suspect; merges adjacent suspect
   windows into time ranges.

## Lyric fidelity — local transcription

Transcribe the vocal with a locally-run speech-recognition model (e.g.
Whisper via `faster-whisper` or `mlx-whisper`; never a cloud service).
Normalize both sides (lowercase; strip punctuation; collapse whitespace;
spell-out mismatches like "20" vs "twenty" normalized) and align the
transcript against the file's Lyrics section. Report per-line coverage:
lines missing, lines altered (with the diff), lines repeated beyond the
format, and an overall word-error estimate. Transcription of sung vocals
is imperfect — the report must distinguish "transcriber uncertainty"
(scattered small errors) from "structural failure" (whole lines missing,
wrong order, invented text), and only structural failure fails the check.

## Calibration — required before trusting any flag

Run both checks on the human's designated memorized Packet A take first
(`packet-a-memorized.mp3`, Suno clip f3eb752c-a4c6-446a-9e42-8f12dd90a8b2
— human-confirmed 2026-09-02; predominantly sung, and its v1-format lyrics
are known). Set the spoken-flag threshold so A's known-sung material
passes, and note the transcription's baseline word-error rate on A —
that baseline is the yardstick for "transcriber uncertainty" on B–E.
Report any A regions still flagged; the human confirms whether they are
genuinely spoken or false positives. Record the thresholds in every
report.

## Verification lessons (learned 2026-09-02, binding)

- Small-model flags on short lines — packet bookends, letter+number
  designators, bare references — are usually transcriber noise, not
  defects. They concentrate at fades and reverb-heavy passages; the
  choral-hymn style is the worst case.
- **No structural finding (missing/repeated/reordered line) may fail a
  take until re-verified with the `medium` Whisper model** (full-track or
  bracketed around the finding). Round 1's scariest finding — a whole
  "missing" topic block — was a small-model miss; the same round hid a
  real duplicated outro that only medium-model verification pinned down.
- When two model sizes return *fluent but different* text for the same
  passage (not a phonetic near-miss), mark it UNCLEAR and refer that
  timestamp to the human ear rather than ruling either way.

## Output

Per screened song: `navigators/songs/screen-<songname>.md` containing the
overall spoken-fraction estimate, suspect time ranges (mm:ss–mm:ss), the
calibration threshold used, and honest caveats.

## Decision rule (default; human may override per song)

- A take FAILS if: spoken fraction > 10%, or any single suspect range
  longer than 15 s, or the lyric-fidelity check shows structural failure
  (missing/altered/reordered lines beyond transcriber uncertainty).
- If every take of a generation round fails → regenerate once with the
  same style string and lyrics.
- If the second round also produces no passing take → stop; record the
  observation (genre, what failed) in the `style-preferences.md` feedback
  log, and refer the style to the human for revision (Procedure 00 re-run).
- Generation attempts per packet are capped at 2 rounds without explicit
  human approval to continue.

## Official take selection

Each lyric/style combo gets one OFFICIAL take — the recording the human
will memorize:

- Packet A's official take is the human-designated memorized clip, always.
- For other packets: among takes that pass both checks, select the one
  with the best lyric fidelity; tie-break on lower spoken fraction. Record
  the selection (and runner-up status of other takes) in
  `navigators/songs/SONGS.md`. The human may override any selection;
  once a packet's status becomes LOCKED its official take never changes.
- The selected take is copied to `navigators/official/` under the
  canonical name — see `06-official-selection.md` for that process.

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

#### Document Modification On 2026-09-02

- Here's the song for packet A I memorized. https://suno.com/s/WuvaIW3gO07diy4P Also can we have the checker check the lyrics match exactly as expected too or else regenerate. Ideally we should select the official song for each lyric/style combo

#### Document Modification On 2026-09-02 (repeatability pass)

- Are the procedures repeatable by another context?
- Yes please add these to a new folder in the root repo. Please also add process to copy the official song to another folder denoting the official songs. Please make the entire pipeline process completely repeatable including the file naming conventions and what files to update after when etc.
