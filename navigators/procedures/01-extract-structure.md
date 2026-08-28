# Procedure 01 — Extract Structure from Verses.pdf

## Purpose

Extract the organizational structure of the Navigators Topical Memory System
from the source PDF: packet letters, packet names, topic names, verse
designators, and scripture references. Structure only — no verse body text.

## Why no verse text

The verse text printed in the PDF is likely a copyrighted modern translation.
References, packet names, and topic names are facts and freely extractable.
Verse text is obtained separately, from public-domain KJV sources, in
Procedure 02. Do not copy any verse body text from the PDF into any output.

## Inputs

- `navigators/source-pdf/Verses.pdf`
  - SHA-256:
    `978ab95267f3b9dea8e61e901a22ffc06cba4ba0d60a7a6c7b157bbd4d1bc557`
  - Before extracting, run
    `shasum -a 256 navigators/source-pdf/Verses.pdf` and confirm it matches
    the checksum above. If it does not match, stop and report; do not
    extract from a different file.

## Output

- `navigators/extracted/packets.md`

## Steps

1. Compute and record the PDF's SHA-256 checksum.
2. Read the PDF. Identify every packet: its letter (A, B, C, ...) and its
   packet name (e.g., "Live the New Life").
3. Within each packet, identify each topic name and the verse designators it
   covers (e.g., topic "Christ the Center" covering designators A1 and A2).
4. For each designator, record the scripture reference exactly as printed,
   then parse it into canonical fields:
   - **Book**: full canonical English book name (e.g., `2 Corinthians`,
     `Psalm`, `John`).
   - **Chapter**: integer.
   - **Verses**: integer, or integer range (`6-7`), or list (`9,11`) —
     exactly as the printed reference indicates.
5. Note (as metadata only) which Bible translation the PDF prints, if stated.
6. Write the output file in the schema below.
7. Validate and report (see Validation).

## Output schema

```markdown
# Extracted Packet Structure

- Source: Verses.pdf, SHA-256: <checksum>
- Extracted: <YYYY-MM-DD>
- Translation printed in source (metadata only): <name or "not stated">

## Packet A — Live the New Life

| Designator | Topic | Reference (as printed) | Book | Chapter | Verses |
|---|---|---|---|---|---|
| A1 | Christ the Center | 2 Corinthians 5:17 | 2 Corinthians | 5 | 17 |
| A2 | Christ the Center | Galatians 2:20 | Galatians | 2 | 20 |
| ... | | | | | |

## Packet B — <name>
...

## Validation Report

- Packets found: <n> (<letters>)
- Topics per packet: <counts>
- Verses per packet: <counts>
- Anomalies: <list, or "none">
```

## Rules

- Record what the PDF actually says. Do not correct, complete, or infer
  references from outside knowledge. If text is unreadable, write
  `[UNREADABLE]` in that cell and list it under Anomalies.
- The standard TMS has 5 packets × 6 topics × 2 verses; if the PDF differs,
  report the difference as an anomaly but output what is actually there.
- Do not copy verse body text (see "Why no verse text").
- Do not modify any file other than `navigators/extracted/packets.md`.
- Do not commit; the human reviews the output first.

## Human Prompts

#### Initial Document Written On 2026-08-27

- Please take the Verses.pdf in the downloads folder. We are going to extract it's verse content and structure to a folder called Navigators. I'd like for all of this work to be done in a reproducible way such that a procedure is written and then a subagent is dispatched according to the procedure to produce the outcome. No work should be done in this conversation - or else I'm afraid the context would be driving process rather than documented procedures. Our ultimate goal is to: 1. Convert to kjv via authoritative sources. We need 3 sources (we can prepare this structure outside of the agent. 2. Then to capture the Packet letter and name, topics and scripture reference 3. We then need to create a lyrics folder which has files organized in a format that is easy to view as a human. Markdown is acceptable. We are going to convert these to song via Suno. *(Excerpt of the full prompt; the complete prompt including the Packet A example text is recorded in `03-lyrics-format.md`.)*
- Please weigh on whether to use Navigators or navigators (lower or upper case). *(Excerpt; lowercase chosen.)*
- I'm okay with this. Let's go ahead
