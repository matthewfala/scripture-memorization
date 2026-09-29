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

## Stem-based screening (v2, preferred — learned 2026-09-15, binding)

Full-mix melodicity is **blind to speech over pitched accompaniment**: the
pitch tracker latches onto instruments (banjo, fiddle, organ) and scores
spoken passages as sustained notes. Proven by the Packet D take1 incident:
the human heard five spoken portions (3:54, 4:02, 4:10, 4:17, 4:40) that
the full-mix screen scored 0.0% spoken — some at melodicity 1.00.

Therefore, screen the **isolated vocal stem**, not the mix:

1. Get the Lead Vocal stem from Suno: song menu → Get Stems (or the
   Download dialog's "Stems & MIDI") → Auto split → Extract → download
   Lead Vocal as MP3. Unlocking a song's stems costs one monthly Pro
   download; all of that song's stems then become downloadable.
2. Save it as `navigators/songs/stems/<mp3-basename>-vocals.mp3` (other
   stems, e.g. `-backing-vocals`, follow the same pattern) and commit —
   stems are screening evidence and calibration artifacts.
3. Screen the stem with `--threshold 0.65 --min-run 2` (stem-mode
   calibration, 2026-09-15): threshold 0.65 catches all five
   human-labeled spoken spots on D take1; `--min-run 2` (a range must
   span at least 2 consecutive windows) suppresses single-window blips.
   The full-mix defaults (0.40, min-run 1) remain only as a cheap
   pre-filter; a full-mix PASS is NOT evidence of absence of speech.
4. Calibration reference: `stems/packet-a-memorized-vocals.mp3` screens
   at 3.7% spoken with four short ranges (0:38, 2:09, 4:23, 4:37).
   **Human-confirmed 2026-09-15**: "I can hear spoken slightly, but I'd
   still classify these as singing" — A's residuals are the acceptable
   borderline; the calibration stands. The 10%/15s decision rule applies
   unchanged to stem screens.

On this calibration, D take1's stem screens at 13.8% spoken → REGENERATE
by the default rule; the human may override per song (Procedure 06).

## Strict clean-sample standard (2026-09-28, binding)

The human requires every candidate to sing **every** line — bookends,
topic titles and designators included — matching the lyrics. A take is
a **clean sample** only if all of the following hold on its vocal stem:

1. Stem spoken screen passes (threshold 0.65, `--min-run 2`, decision
   rule unchanged).
2. `tools/verify_lines.py` (biased-prompt medium transcription + global
   alignment + fuzzy window) finds every expected line, **or** each
   unconfirmed line shows vocal energy >= 0.8x the stem's median in its
   expected region (sung but unintelligible to the ASR — the memorized
   Packet A reference itself scores 62/64 with its two misses in this
   category).
3. No line is NOT_FOUND with energy < 0.8x at a bookend position (start
   or end of the song) — a low-energy bookend miss means the bookend was
   most likely skipped, which disqualifies the take.
4. No confirmed repeats or extra sung lines beyond the lyrics.
5. **Topic order (v3 lyrics)**: `tools/check_topic_order.py` confirms every
   topic's name is heard in BOTH positions — before its verse pair and
   right after the pair's trailing reference — walking the transcript in
   order. Required because `verify_lines.py`'s fuzzy search is
   position-blind (it can "find" a skipped title inside verse text).
6. **Bookends**: `tools/probe_bookends.py` transcribes only the opening
   and closing windows with the bookend words as bias. Validated
   2026-09-28: it hears Packet A's bookends perfectly and correctly
   reports D takes 5/6 skipping "Packet Dee" (their transcripts start at
   "Put Christ First" despite the bias), so it does not merely echo its
   prompt. A closing bookend transcribed as a same-syllable near-miss in
   its slot ("how did he grow in…") counts as sung-but-blurred.

Run order per take: stem spoken screen → `verify_lines.py` (writes the
word timeline) → `check_topic_order.py` → `probe_bookends.py`. Any hard
failure disqualifies; near-misses are published only as labelled
near-clean candidates.

Biased prompting matters: it feeds the packet's short lines to the
transcriber, and resolved every "missing designator" finding on the B
pool (2026-09-17) as a transcriber artifact.

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

## Candidate pool (human-requested, 2026-09-15)

When the human requests a candidate pool for a packet, generation rounds
continue (human approval already given by the request) until **three
takes pass both checks** (stem-mode spoken screen + lyric fidelity), up
to a sanity cap of 3 rounds per series without a further check-in. The
human then chooses the official from the passing pool (Procedure 06).
Passing takes are candidates; failing takes are recorded as usual.

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

#### Document Modification On 2026-09-15 (stem-based screening)

- Packet D, I like the sound, however there are portions that are spoken around 3:54 and 4:02 and 04:10 and 04:17 04:40. Is the automated detector able to be calibrated to detect this?
- I'm pretty sure suno has this feature, you can download the spoken section without the music on the website?

#### Document Modification On 2026-09-15 (calibration ruling, candidate pool)

- I have been listening to C so that one is now locked. Can we lock it? Can you regenerate D? Perhaps we can have 3 candidates (which pass) for each. Also I'd like to regenerate E & B. Please try out the new Suno v6 model. Also for the A packet, I can hear spoken slightly, but I'd still classify these as singing.

#### Document Modification On 2026-09-28 (strict clean-sample standard)

- Can you make sure all the candidates pass the screeners? We need the bookends too. The text should match the lyrics.
- Can we switch back to packet a's format? I'd like to focus on packet E. Can you please make sure we have 3 clean samples if possible? Can you also update the website to display all three samples for packet e? I'll listen to those and tell you which I'd like to lock.

#### Document Modification On 2026-09-28 (topic-order and bookend probes)

- Can we switch back to packet a's format? I'd like to focus on packet E. Can you please make sure we have 3 clean samples if possible? Can you also update the website to display all three samples for packet e? I'll listen to those and tell you which I'd like to lock.
