# Procedure 06 — Official Take Selection and the official/ Folder

## Purpose

Designate one OFFICIAL recording per lyric/style combo — the take the
human will memorize — and keep a stable, canonically-named copy of it in
`navigators/official/`, so the memorization player/playlist never needs
to know take numbers.

## Selection rule

- A packet whose official take the human has designated directly (as with
  Packet A's memorized clip) keeps that designation, always.
- Otherwise: among takes that pass both Procedure 04 checks, pick the best
  lyric fidelity; tie-break on lower spoken fraction. If no take passes
  mechanically (common — the checks over-flag short lines), pick the take
  with the fewest *confirmed real* defects and record the evidence.
- When the human has requested a candidate pool (Procedure 04), present
  the three passing candidates and let the human choose the official
  directly; the agent's ranking is advisory.
- Status is **PROPOSED** until the human listens and approves, then
  **LOCKED**. A LOCKED official never changes; a human override replaces a
  PROPOSED selection at any time.

## The official/ folder

- Path: `navigators/official/`. One file per packet, named
  `packet-<letter>.mp3` — no take numbers, so the canonical path is
  stable across re-selection.
- On every selection or override: copy (never move) the selected take
  from `navigators/songs/packet-<letter>-take<N>.mp3` to
  `navigators/official/packet-<letter>.mp3`, overwriting the previous
  copy. The takes in `navigators/songs/` are the archive; official/ is a
  derived view.
- Record in `navigators/songs/SONGS.md`, same commit: which take is
  OFFICIAL (and its status PROPOSED/LOCKED), runner-up notes, and the
  copy's provenance (source take file).

## Candidates on the public site

While a packet is being chosen, its site card shows the candidate pool
instead of a single player: badge **Choosing**, one numbered row per
candidate (take number, duration, model, screening verdict in plain
words, player, download). Candidate files live in
`navigators/official/candidates/packet-<letter>-take<N>.m4a` (AAC, see
Procedure 05) and publish to `candidates/` on S3. On lock, copy the
chosen take to `official/packet-<letter>.mp3` (or .m4a), restore the
single-player card with a **Locked** badge, and delete that packet's
files from `candidates/`.

## What updates when

| Event | Update |
|---|---|
| Screening round completes | SONGS.md take notes + proposed selection |
| Selection made/changed | copy into official/, SONGS.md row + selection section |
| Human approves ("lock") | SONGS.md status → LOCKED (file already in place) |
| Human overrides | re-copy official/, SONGS.md records the override and why |
| Style referred back (Procedure 00) | no official/ entry until a passing take exists |

## Human Prompts

#### Initial Document Written On 2026-09-02

- Here's the song for packet A I memorized. https://suno.com/s/WuvaIW3gO07diy4P Also can we have the checker check the lyrics match exactly as expected too or else regenerate. Ideally we should select the official song for each lyric/style combo
- Yes please add these to a new folder in the root repo. Please also add process to copy the official song to another folder denoting the official songs. Please make the entire pipeline process completely repeatable including the file naming conventions and what files to update after when etc.

#### Document Modification On 2026-09-15

- I have been listening to C so that one is now locked. Can we lock it? Can you regenerate D? Perhaps we can have 3 candidates (which pass) for each. Also I'd like to regenerate E & B. Please try out the new Suno v6 model.

#### Document Modification On 2026-09-28

- Can we switch back to packet a's format? I'd like to focus on packet E. Can you please make sure we have 3 clean samples if possible? Can you also update the website to display all three samples for packet e? I'll listen to those and tell you which I'd like to lock.
