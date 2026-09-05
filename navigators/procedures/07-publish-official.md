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
   the mp3s, uploads the page, and rebuilds and uploads the zip.
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

- The page is plain HTML/CSS with no JavaScript; fonts load from Google
  Fonts with system fallbacks. `preload="none"` on the players keeps
  page loads cheap.
- Exactly one design is published: `index.html` at the bucket root.
  Three alternative designs (typeset, red-letter, masthead) were
  trialled beside it as subfolders on 2026-09-03 and retired on
  2026-09-04 when the human chose the original; their sources remain
  in git history (commit 67b3074) should a feature such as the
  red-letter page's shuffle/repeat controls ever be wanted. If designs
  are ever compared again, publish candidates under subfolders by hand
  and remove all but the chosen one from both repo and bucket once the
  choice is made.
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

#### Document Modification On 2026-09-04

- II had claude build several s3 web demos. I like the first one still listed here: http://scripture-memorization-songs.s3-website-us-east-1.amazonaws.com
- Can you delete the others and update the procedure.
