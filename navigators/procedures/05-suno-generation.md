# Procedure 05 — Song Generation (Suno, browser)

## Purpose

Turn a committed lyrics file into candidate recordings ("takes") in the
human's Suno account, downloaded and committed under repo naming
conventions. Runs after Procedure 03 (lyrics exist, style attached) and
before Procedure 04 (screening).

## Preconditions

- `navigators/lyrics/packet-<letter>.md` exists with `## Style` and
  `## Lyrics` sections committed.
- The human is logged into Suno in the browser the agent drives, and has
  confirmed credits may be spent (each generation costs 10 credits and
  yields 2 takes).
- Style status is PROPOSED or LOCKED (Procedure 00). Never generate from
  an unreviewed style.

## Steps

1. Open `https://suno.com/create`. Ensure **Custom/Advanced** mode and the
   current model (v6; as of 2026-09-28 Suno offers only v6, v6-wild and
   v6-mini — v5.5 is gone; the 2026-09-02 takes used v5.5). Record the model version in each SONGS.md
   row. Use the shared workspace named `Packets` when a workspace
   selector is offered.
2. Paste the file's `## Lyrics` section (only the lyric lines, no headers)
   into the Lyrics editor. The editor is a contenteditable div: click it,
   select-all + delete, then type/paste the text. Long text can freeze the
   renderer for ~30 s — wait rather than re-send.
3. **Byte-verify before generating** (mandatory): read the editor text
   back via page JavaScript, normalize (collapse newline runs to one,
   non-breaking spaces to spaces, trim), and compare to the identically
   normalized file text. Fix and re-verify on any mismatch. Verify the
   Styles field matches the file's `## Style` line exactly.
4. Set Song Title to `Packet <letter-uppercase> - <packet title>` (e.g.
   `Packet E - Grow in Christlikeness`).
5. Click Create **once**, then confirm in the workspace/library list that
   exactly two new rows appeared for that title before doing anything
   else. (A double submission burns credits and creates stray clips —
   detected by finding more new rows than expected; note strays in
   `navigators/songs/SONGS.md` and leave deleting them to the human.)
6. Wait for rendering (~2–4 minutes; a row shows a duration when done).
7. Download each take: row menu (More options) → Download → MP3 Audio.
   Move the files into `navigators/songs/` as
   `packet-<letter>-take<N>.mp3`, numbering takes in the order the rows
   list (newest generation's rows, top-to-bottom continue the packet's
   take numbering: round 1 → take1/take2, round 2 → take3/take4, …).
8. Record each take in `navigators/songs/SONGS.md` (duration, date,
   model, style short-name, round) and commit the mp3s together with the
   SONGS.md update.

## Practical notes (2026-09-28)

- **Lyrics entry**: the editor ignores synthetic newlines. Type each line
  as its own `type` action followed by a `Return` key press, then verify
  by reading the editor's `<p>` paragraphs (one per lyric line, no empty
  paragraphs for v3). Faster for regenerations: song menu → Remix →
  **Reuse Prompt**, which refills lyrics + style exactly — still verify.
- **Generating several takes**: clicking Create twice deliberately gives
  four takes; record that it was intentional.
- **Menus**: prefer the playbar's "More options" or collapse the create
  panel first — the song header's "…" is flaky at narrow widths, and
  element refs shift between pages (a stale ref once hit Like instead).
- **Downloads**: each screened take costs one Pro download (the stem
  unlock also unlocks the full song). Full songs of unlocked takes are
  free: download **WAV** and encode locally with
  `afconvert -f m4af -d aac -b 192000 in.wav out.m4a` — Suno's own M4A is
  Opus-in-MP4, which Safari may not play and afconvert cannot read.
- **Signed URLs**: when a browser download doesn't land, the click still
  fires a signed `suno-data-uploads.s3.amazonaws.com` request; capture it
  from the network log and fetch it with curl.

## Rules

- Never edit lyrics or style at generation time; a change means going
  back to Procedure 03/00 and committing there first.
- One generation round per packet per Procedure 04 decision — the round
  cap (2 without human approval) is enforced there.
- Credits are the human's money: report the spend in the session summary.

## Human Prompts

#### Initial Document Written On 2026-09-02

- I'm logged into suno on chrome now. Can you please generate the 5 packets songs? Please store the song mp3 in the folder once generated. Ideally screen for the spoken words rather than sung and regenerate or change the style if so.
- Are the procedures repeatable by another context?
- Yes please add these to a new folder in the root repo. Please also add process to copy the official song to another folder denoting the official songs. Please make the entire pipeline process completely repeatable including the file naming conventions and what files to update after when etc.

#### Document Modification On 2026-09-15

- I have been listening to C so that one is now locked. Can we lock it? Can you regenerate D? Perhaps we can have 3 candidates (which pass) for each. Also I'd like to regenerate E & B. Please try out the new Suno v6 model.

#### Document Modification On 2026-09-28

- Can we switch back to packet a's format? I'd like to focus on packet E. Can you please make sure we have 3 clean samples if possible? Can you also update the website to display all three samples for packet e? I'll listen to those and tell you which I'd like to lock.
