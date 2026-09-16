# The Pipeline — End-to-End, Repeatable

This document is the map: run these procedures in this order and any
fresh context reproduces the whole flow, from source PDF to an official
recording per packet. Each stage's own file is authoritative for its
details; this page fixes the order, the naming, and what gets updated
when.

## Stage order

| # | Procedure | In → Out |
|---|---|---|
| 1 | `01-extract-structure.md` | `source-pdf/Verses.pdf` → `extracted/packets.md` (structure only, no verse text) |
| 2 | `02-kjv-conversion.md` | `extracted/packets.md` + `kjv-sources/` → verified KJV text per reference (3-source agreement) |
| 3 | `00-style-partition.md` | `style-preferences.md` → `styles.md` (one style per grouping; statuses PROPOSED/LOCKED) |
| 4 | `03-lyrics-format.md` | KJV text + `styles.md` → `lyrics/packet-<letter>.md` (v2 format; v1 is Packet A's immutable historical format) |
| 5 | `05-suno-generation.md` | lyrics file → `songs/packet-<letter>-take<N>.mp3` + `songs/SONGS.md` rows |
| 6 | `04-spoken-word-screen.md` | takes → `songs/screen-<songname>.md` reports + PASS/FAIL verdicts (tools in `tools/`, see `tools/README.md`) |
| 7 | `06-official-selection.md` | verdicts → `official/packet-<letter>.mp3` + selection recorded in `SONGS.md` |
| 8 | `07-publish-official.md` | `official/` → public S3 landing page (`official/index.html` + mp3s + zip) via `tools/publish-official.sh` |

Stages 5–7 loop per Procedure 04's decision rule (max 2 generation
rounds per packet without human approval; then style referral to
Procedure 00).

## Naming conventions

- Lyrics: `navigators/lyrics/packet-<letter>.md` (lowercase letter).
  Sections: `## Style`, `## Lyrics`. Screening reads only `## Lyrics`.
- Takes: `navigators/songs/packet-<letter>-take<N>.<ext>`, N counts
  across rounds and series (round 1 → 1,2; round 2 → 3,4; …). `<ext>`
  is `.mp3` for the 2026-09-02 v5.5 takes; v6 takes are `.m4a` (Suno's
  Pro download system delivers ~134 kbps AAC m4a or 64 kbps mp3 — take
  the m4a). Packet A's human-designated recording is
  `packet-a-memorized.mp3`.
- Screening reports: `navigators/songs/screen-<mp3-basename>.md`.
- Vocal stems (screening evidence, Procedure 04 stem mode):
  `navigators/songs/stems/<mp3-basename>-vocals.mp3` (and
  `-backing-vocals.mp3` etc.), extracted via Suno Get Stems.
- Officials: `navigators/official/packet-<letter>.mp3` — canonical,
  take-number-free, overwritten on re-selection (Procedure 06).
- Landing page: `navigators/official/index.html`; S3 keys mirror `official/`
  filenames (Procedure 07).
- Suno-side titles: `Packet <LETTER> - <Packet Title>`; workspace
  `Packets`.

## What to update, when

| After… | Update (same commit) |
|---|---|
| downloading takes | mp3s + `SONGS.md` rows (duration, date, round) |
| a screening run | `screen-*.md` reports + `SONGS.md` verdict notes |
| a failed round | `style-preferences.md` feedback log entry (with human confirmation) |
| a selection | `official/packet-<letter>.mp3` copy + `SONGS.md` selection section |
| a human lock/override | `SONGS.md` status change (and re-copy on override) |
| any change to `official/` | `official/index.html` (badge/duration/size/date) + run `tools/publish-official.sh` |

Commits follow `CLAUDE.md` (Human Prompts in messages; no agent
attribution). Documents carry `## Human Prompts` sections; generated
reports include one naming the generating script.

## Environment for a fresh context

- Screening: `tools/` — one-time venv setup per `tools/README.md`;
  thresholds and calibration provenance are recorded there and in
  Procedure 04. Local compute only.
- Generation: a browser logged into the human's Suno account (ask the
  human), credits available; byte-verification of pasted lyrics is
  mandatory (Procedure 05).
- Calibration reference: `songs/packet-a-memorized.mp3` + `lyrics/packet-a.md`.
- Publishing: `aws` CLI, default profile on account 381492251647 (Procedure 07).

## Human Prompts

#### Initial Document Written On 2026-09-02

- Are the procedures repeatable by another context?
- Yes please add these to a new folder in the root repo. Please also add process to copy the official song to another folder denoting the official songs. Please make the entire pipeline process completely repeatable including the file naming conventions and what files to update after when etc.

#### Document Modification On 2026-09-02 (publishing)

- Can you add the official songs to an s3 bucket to be downloaded and have an index file which has the song portfolio please make it look nice and appropriate - a landing page for getting these songs. I give you permission to make a global s3 bucket in my aws account and put the official songs in it

#### Document Modification On 2026-09-15 (stem-based screening)

- Packet D, I like the sound, however there are portions that are spoken around 3:54 and 4:02 and 04:10 and 04:17 04:40. Is the automated detector able to be calibrated to detect this?
- I'm pretty sure suno has this feature, you can download the spoken section without the music on the website?
