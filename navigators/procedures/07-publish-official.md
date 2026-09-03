# Procedure 07 — Publish Officials to the Public Landing Page (S3)

## Purpose

Make the current official recordings downloadable from a public web page
so the human (and anyone they share the link with) can listen or download
without the repo. The page is a portfolio of the packets: title, style,
topics and references, status, an inline player and a download link per
packet, plus a zip of all five.

## Where things live

| Thing | Location |
|---|---|
| Landing page source | `navigators/official/index.html` (committed) |
| Publish script | `tools/publish-official.sh` |
| Bucket | `scripture-memorization-songs`, region `us-east-1`, account 381492251647 (IAM user `Admin`), public-read bucket policy, static website hosting on |
| Public URL | http://scripture-memorization-songs.s3-website-us-east-1.amazonaws.com/ |
| Object keys | `index.html`, `packet-<letter>.mp3`, `navigators-official-songs.zip` |
| Candidate page (typeset design) | source folder `navigators/official/typeset/` (`index.html`, `icon.svg`, `apple-touch-icon.png`), mirrored to keys `typeset/*`, URL http://scripture-memorization-songs.s3-website-us-east-1.amazonaws.com/typeset/ |
| Candidate page (red-letter design) | source folder `navigators/official/redletter/` (same three files), mirrored to keys `redletter/*`, URL http://scripture-memorization-songs.s3-website-us-east-1.amazonaws.com/redletter/ |
| Candidate page (masthead design) | source folder `navigators/official/masthead/` (same three files), mirrored to keys `masthead/*`, URL http://scripture-memorization-songs.s3-website-us-east-1.amazonaws.com/masthead/ |

The bucket was created once (2026-09-02) with the human's explicit
permission; the script never creates or reconfigures it. Object keys
mirror `official/` filenames, so the canonical per-packet URL is stable
across re-selection, exactly like the local path (Procedure 06).

## Steps

1. Confirm `navigators/official/` holds the intended files (Procedure 06
   already copied them) and `SONGS.md` records the selection.
2. Edit `navigators/official/index.html` so it matches `SONGS.md`:
   the status badge (`Locked` / `Proposed`), duration, file size, and the
   "updated" date in the section head; the total runtime in the hero
   stats. Titles, styles and topic/reference lists come from
   `extracted/packets.md` and `styles.md` and only change if those do.
3. Run `tools/publish-official.sh` (needs the `aws` CLI with the default
   profile; override `BUCKET`/`REGION` via env if ever needed). It syncs
   the mp3s, uploads the page, and rebuilds and uploads the zip. Any
   candidate page listed in the table above is uploaded by hand, file by
   file, to the keys mirroring its folder (`text/html; charset=utf-8`,
   `image/svg+xml`, `image/png`; `max-age=60` for the page, 300 for the
   icons). It references the mp3s and zip by root-relative path, so it
   needs no copies of its own. Each candidate's icon is a hand-drawn
   `icon.svg` (typeset: cream leaf, double rule, rubric shape-note;
   red-letter: black cover, gold rules, gold note; masthead: a woodcut-
  style decorated initial, black vine foliage on paper around a red
  Lombardic S, which the page also shows above its title); the 180px
   `apple-touch-icon.png` is rendered from it in a browser canvas and
   must be regenerated if the SVG changes. Keep candidate pages in step with `SONGS.md` too (same
   badge/duration/size edits as step 2) until the human picks one; then
   the chosen design becomes `index.html` and the other is removed from
   the repo and the bucket.
4. Open the public URL and check every player loads and each download
   link responds (a quick `curl -I` per key is enough).
5. Commit the `index.html` change with the selection it reflects
   (same commit as the Procedure 06 update when practical).

## What updates when

| Event | Update |
|---|---|
| Official copied/overwritten (Procedure 06) | re-run the script; update `index.html` duration/size/date |
| Human locks or overrides a packet | `index.html` badge + re-run the script |
| Style/title/reference text changes upstream | `index.html` copy + re-run the script |
| Bucket, region or URL changes | this document's table and the script defaults |

## Notes

- The original page is plain HTML/CSS with no JavaScript. The typeset
  candidate uses a few lines of inline JavaScript for a styled player
  (falls back to native `<audio controls>` without JS). Both load fonts
  from Google Fonts with system fallbacks and use `preload="none"` so
  page loads stay cheap.
- Several designs are live at once only while the human is choosing
  between them (2026-09-03: original at `/`, typeset candidate at
  `/typeset/`, red-letter candidate at `/redletter/`, masthead candidate
  at `/masthead/`). The red-letter
  design is the readability middle ground: modern printed-KJV idiom
  (black cover band, gilt edge, white paper, red chapter marks, rules
  instead of cards) in a screen-readable text serif. Its script also
  provides listening modes: "Shuffle all" (random order, repeats
  forever, with a fixed now-playing bar and a Next button) and a
  per-packet repeat toggle (loops one recording forever; turning it on
  cancels shuffle and vice versa). Next always works: next in order
  normally, random while shuffling.
- The masthead design is the red-letter page with the skeuomorphic
  cover replaced by a typographic masthead on the same paper (title in
  the body serif, red diamond, epigraph, double rule) so the top and
  the body speak one visual language; the now-playing bar is ink and
  red rather than black and gold. Hosting cost is negligible: each page
  is tens of kilobytes and all candidates share the same mp3 objects.
- For a local preview, `.claude/launch.json` defines `official-preview`,
  a static server on port 8765 rooted at `navigators/official/`, so the
  root-relative mp3 paths resolve.
- The bucket is world-readable by design. Do not put takes, screening
  reports, or anything other than officials and the page in it.

## Human Prompts

#### Initial Document Written On 2026-09-02

- Can you add the official songs to an s3 bucket to be downloaded and have an index file which has the song portfolio please make it look nice and appropriate - a landing page for getting these songs. I give you permission to make a global s3 bucket in my aws account and put the official songs in it

#### Document Modification On 2026-09-03

- I really liked the results however I felt that the style looked a bit familiar in terms of borrowing from anthropic ui. Would it be possible for you to think of an original ui/ux perhaps inspired by the old typeset kjv prints. Please do your best without looking at the prior work to not be biased. Would you publish to s3 the result and provide the link? I'll let you know which I like.
- Can you improve the web icon?
- This one is pretty but less easy to read. Maybe can you take a look at the other version, and make a third one that is in between? Please help me find a UXUI that is not in the lineage of anthropic if possible.
- Can you add a shuffle play option that repeats forever and a loop play option that repeats a single song forever
- I like the redletter version but I feel like the top section is still a bit clashing with the sleek internal portions. I'm thinking it might be better to redesign this rather than continuing with the bible look. What do you think? Please advise with you artistic instinct
- Please try it! Can you make a v4? I think these are cheap to host right? Also the next button doesn't work when the shuffle is turned off
- I love the old single character block that is artistically drawn and used in a printing press block. Wondering if we could incorporate that as an icon at the top for flavor
