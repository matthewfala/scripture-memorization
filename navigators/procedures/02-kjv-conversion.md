# Procedure 02 — KJV Conversion and Verification

## Purpose

Produce the authoritative KJV text for every scripture reference in the
extracted structure, verified by exact agreement across three independently
maintained public-domain sources. Disagreements are flagged for human
review, never auto-resolved.

## Inputs

- `navigators/extracted/packets.md` — the references to look up.
- `navigators/kjv-sources/gutenberg/` — Project Gutenberg eBook #10,
  plain text.
- `navigators/kjv-sources/sacred-texts/` — sacred-texts.com `kjvdat.txt`,
  delimited plain text.
- `navigators/kjv-sources/aruljohn/` — aruljohn/Bible-kjv, one JSON file
  per book.
- Each source directory contains a `SOURCE.md` with URL, retrieval date,
  and checksum. Verify each checksum before use; if any mismatch, stop
  and report.

## Output

- `navigators/extracted/verses-kjv.md`

## Method — scripts, not context

The sources total ~13 MB. Do not read them into context. Write a script
(Python) that does the lookups and comparison; inspect at most small
excerpts (tens of lines) of each source to learn its format. No network
access — the three local sources are the entire universe of truth.

1. By inspection, determine each source's reference scheme (book naming,
   verse line format, any markup such as trailing delimiters or supplied-word
   markers). Build a book-name mapping from the canonical names in
   `packets.md` to each source's naming — only for the books actually
   referenced.
2. For each reference, extract the verse text from each of the three
   sources. For multi-verse references (ranges like `6-7`, lists like
   `9,11`), extract each verse separately and also record the joined text
   (single space between verses).
3. Normalize for comparison only: strip source-specific structural markup
   (delimiters, verse-number prefixes), collapse whitespace runs to single
   spaces, trim. Do not normalize spelling, punctuation, or casing — those
   differences must surface. Document every stripping decision in the
   output header; apply each uniformly to all three sources.
4. Compare per verse:
   - All three identical after normalization → status `AGREE`.
   - Otherwise → status `FLAGGED`; classify the difference
     (punctuation-only / spelling / wording / missing) and record each
     source's text verbatim. If two of three agree, note the majority, but
     the status remains `FLAGGED` for human review.
5. Write the output per the schema below.

## Rules

- The final text of every verse must be byte-identical to the normalized
  text of the agreeing sources. Never emit verse text from model memory,
  and never "correct" a source.
- A `FLAGGED` verse gets no final text — only the per-source candidates.
- Do not modify any file other than the output and your scratch scripts.
- Do not commit; the human reviews first.

## Output schema

```markdown
# Verified KJV Verse Text

- Generated: <YYYY-MM-DD>
- Sources: gutenberg <sha256-prefix>, sacred-texts <sha256-prefix>,
  aruljohn <sha256-prefix or commit>
- Normalization applied: <numbered list of stripping decisions>

## Packet A — Live the New Life

### A1 — 2 Corinthians 5:17 — AGREE

Therefore if any man be in Christ, ...

...

## Discrepancies

### <designator> — <reference> — FLAGGED (<classification>)

- gutenberg: <text>
- sacred-texts: <text>
- aruljohn: <text>
- Majority: <two-source text, or "none">

*(If there are no discrepancies, state "None.")*
```

## Human Prompts

#### Initial Document Written On 2026-08-27

- Our ultimate goal is to: 1. Convert to kjv via authoritative sources. We need 3 sources (we can prepare this structure outside of the agent. *(Excerpt; full prompt recorded in `03-lyrics-format.md`.)*
- For KJV sources, I'm wondering what the most reputable sources would be? If those 3 are somewhat reputable, I'm okay with them Ideally we'd have those copied to the repository with some reference to the source. Ideally these sources need to be free of copyright restrictions. *(Excerpt; full prompt recorded in `03-lyrics-format.md`.)*
- I'm okay with this. Let's go ahead
- Please continue.
