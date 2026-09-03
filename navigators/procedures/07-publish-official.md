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
- The bucket is world-readable by design. Do not put takes, screening
  reports, or anything other than officials and the page in it.

## Human Prompts

#### Initial Document Written On 2026-09-02

- Can you add the official songs to an s3 bucket to be downloaded and have an index file which has the song portfolio please make it look nice and appropriate - a landing page for getting these songs. I give you permission to make a global s3 bucket in my aws account and put the official songs in it
