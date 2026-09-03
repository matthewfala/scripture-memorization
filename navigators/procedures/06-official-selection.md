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
