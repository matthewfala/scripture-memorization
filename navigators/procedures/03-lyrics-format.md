# Procedure 03 — Lyrics Format and Generation

## Purpose

Generate Suno-ready lyrics files from verified KJV text, in a format tuned
for memorization. This document is both the format specification and the
generation procedure. The format is versioned: memorized packets keep the
format they were memorized under, forever.

## Format versions

- **v1** — Packet A (memorized; immutable; described below for the record).
- **v2** — Packet B onward (current).

### v1 (for the record)

Packet title + packet name at start and end of the song. Each topic
announced with topic name + spoken designators both **before and after** its
verse pair. Each verse sandwiched by its spoken reference. Example (opening
of Packet A):

```
Packet Ay
Live the New Life
Christ the Center
Ay One and Ay Two
Second Corinthians five seventeen.
Therefore if any man be in Christ, he is a new creature: old things are
passed away; behold, all things are become new.
Second Corinthians five seventeen.
...
Christ the Center
Ay One and Ay Two
```

### v2 changes and rationale

1. **Topic announcements are leading-only.** The trailing topic + designator
   repeat is removed. Reason: in memorization practice the trailing
   announcement blurred with the leading one, causing retrieval to jump to
   the next section instead of the verses under the topic. In v2 a topic
   title is only ever followed by its own verses.
2. **Reference sandwich retained.** Spoken reference before and after each
   verse — it enables retrieval in both directions (reference → text and
   text → reference).
3. **Packet title at start and end retained** — status *provisional*; may be
   revisited after Packet B experience.
4. **Format variable `reference-placement`** — default `separate-line` (each
   spoken reference is its own line, hence its own musical phrase, as in
   v1). Fallback variant `joined` (leading reference joined to the verse's
   first phrase on one line, sung in one breath) — to be tried only if
   sampling shows the separate-line references being styled badly or
   spoken. The variant in force is recorded in each generated file.

## Spoken-form rules

- **Packet letters** are written phonetically:
  A → `Ay` · B → `Bee` · C → `See` · D → `Dee` · E → `Ee`
  (extend the table if more packets exist).
- **Designators**: `{Letter} {Number-word}`, e.g. B3 → `Bee Three`. A topic
  pair reads `Bee Three and Bee Four`.
- **Book names** as spoken: leading `1`/`2`/`3` become `First`/`Second`/
  `Third` (e.g., `Second Corinthians`); `Psalms` is spoken `Psalm`.
- **Numbers** are spelled as spoken English words: 17 → `seventeen`,
  21 → `twenty-one` (hyphenated), 119 → `one nineteen` (chapters over 99
  read digit-grouped as commonly spoken).
- **References**: `{Book} {chapter} {verse}.` with a terminal period —
  `Second Corinthians five seventeen.` Ranges use `to`
  (`Philippians four six to seven.`); lists use `and`
  (`Psalm one nineteen nine and eleven.`).

## v2 song structure

One file = one song. If the assembled Lyrics section exceeds 4,000
characters, split the packet into two files at the topic 3/4 boundary
(topics 1–3 and 4–6, never mid-topic), named `packet-<letter>-part-1.md`
and `-part-2.md`; each part carries the full packet title bookends and the
same style block. Otherwise the file is `packet-<letter>.md`.

```
Packet Bee
{Packet Name}

{Topic 1 Name}
Bee One and Bee Two
{spoken reference 1}.
{verse 1 text}
{spoken reference 1}.
{spoken reference 2}.
{verse 2 text}
{spoken reference 2}.

{Topic 2 Name}
Bee Three and Bee Four
...

Packet Bee
{Packet Name}
```

## Lyrics file schema

```markdown
# Packet B — {Packet Name}

- Format: v2 (reference-placement: separate-line)
- Style status at generation: {status from styles.md}
- Generated: {YYYY-MM-DD}

## Style

{style string verbatim from navigators/styles.md}

## Lyrics

{structure above}
```

## Generation steps

1. Preconditions — stop and report if any fail:
   - `navigators/styles.md` has an entry for the target packet.
   - `navigators/extracted/verses-kjv.md` has status `AGREE` (or a
     human-resolved text) for every verse of the packet.
2. Build each spoken reference per the Spoken-form rules.
3. Assemble the structure above, taking verse text **verbatim** from
   `verses-kjv.md`.
4. Apply the split rule if over 4,000 characters.
5. Validate by script: every designator of the packet present exactly once;
   each verse's text byte-identical to `verses-kjv.md`; every reference line
   matches its designator's reference; topic announcements leading-only.
6. Write to `navigators/lyrics/`. Do not commit; the human reviews and
   samples the song in Suno.

## Human Prompts

#### Initial Document Written On 2026-08-27

- Please take the Verses.pdf in the downloads folder. We are going to extract it's verse content and structure to a folder called Navigators. I'd like for all of this work to be done in a reproducible way such that a procedure is written and then a subagent is dispatched according to the procedure to produce the outcome. No work should be done in this conversation - or else I'm afraid the context would be driving process rather than documented procedures. Our ultimate goal is to: 1. Convert to kjv via authoritative sources. We need 3 sources (we can prepare this structure outside of the agent. 2. Then to capture the Packet letter and name, topics and scripture reference 3. We then need to create a lyrics folder which has files organized in a format that is easy to view as a human. Markdown is acceptable. We are going to convert these to song via Suno. Let's work on a format first and the procedure. I have an example text - You can see that A was converted to song format. Pack A is completed, but for B I'd like to update the format according to my memorization experience. Packet Ay / Live the New Life / Christ the Center / Ay One and Ay Two / Second Corinthians five seventeen. / Therefore if any man be in Christ, he is a new creature: old things are passed away; behold, all things are become new. / Second Corinthians five seventeen. / Galatians two twenty. / I am crucified with Christ: nevertheless I live; yet not I, but Christ liveth in me: and the life which I now live in the flesh I live by the faith of the Son of God, who loved me, and gave himself for me. / Galatians two twenty. / Christ the Center / Ay One and Ay Two / Obedience to Christ / Ay Three and Ay Four / Romans twelve one. / I beseech you therefore, brethren, by the mercies of God, that ye present your bodies a living sacrifice, holy, acceptable unto God, which is your reasonable service. / Romans twelve one. / John fourteen twenty-one. / He that hath my commandments, and keepeth them, he it is that loveth me: and he that loveth me shall be loved of my Father, and I will love him, and will manifest myself to him. / John fourteen twenty-one. / Obedience to Christ / Ay Three and Ay Four / The Word / Ay Five and Ay Six / Second Timothy three sixteen. / All scripture is given by inspiration of God, and is profitable for doctrine, for reproof, for correction, for instruction in righteousness: / Second Timothy three sixteen. / Joshua one eight. / This book of the law shall not depart out of thy mouth; but thou shalt meditate therein day and night, that thou mayest observe to do according to all that is written therein: for then thou shalt make thy way prosperous, and then thou shalt have good success. / Joshua one eight. / The Word / Ay Five and Ay Six / Prayer / Ay Seven and Ay Eight / John fifteen seven. / If ye abide in me, and my words abide in you, ye shall ask what ye will, and it shall be done unto you. / John fifteen seven. / Philippians four six to seven. / Be careful for nothing; but in every thing by prayer and supplication with thanksgiving let your requests be made known unto God. And the peace of God, which passeth all understanding, shall keep your hearts and minds through Christ Jesus. / Philippians four six to seven. / Prayer / Ay Seven and Ay Eight / Fellowship / Ay Nine and Ay Ten / Matthew eighteen twenty. / For where two or three are gathered together in my name, there am I in the midst of them. / Matthew eighteen twenty. / Hebrews ten twenty-four to twenty-five. / And let us consider one another to provoke unto love and to good works: Not forsaking the assembling of ourselves together, as the manner of some is; but exhorting one another: and so much the more, as ye see the day approaching. / Hebrews ten twenty-four to twenty-five. / Fellowship / Ay Nine and Ay Ten / Witnessing / Ay Eleven and Ay Twelve / Matthew four nineteen. / And he saith unto them, Follow me, and I will make you fishers of men. / Matthew four nineteen. / Romans one sixteen. / For I am not ashamed of the gospel of Christ: for it is the power of God unto salvation to every one that believeth; to the Jew first, and also to the Greek. / Romans one sixteen. / Witnessing / Ay Eleven and Ay Twelve / Packet Ay / Live the New Life *(Line breaks in the original example are shown here as " / ".)* Can we interact on the plan
- Ideally one or two files per pack - since that is the granularity of the song. Yes, we need to figure out a procedure to partition the packets such that they do not overlap in style from the start so that when we begin implementing the packets they are evenly spaced over the domain of musical styles.
- fully sung melodic vocals throughout, no spoken word - In my experience this doesn't actually change the outcome of the amount of spoken word so much as the genera of music does. It's hard for me to predict which genres are going to be spoken more. I can share feedback after listening to the music. If there was some automatic screening of the spoken word, perhaps that would be ideal - though if it uses cloud LLMs I'm thinking that would be costly and wasteful, and if not, I'm not sure a local model would be effective at detecting the spoken portions. for the format, I like the verse reference before and after the verse content since it does allow me to retrieve the verse ref from the text or the text from the verse ref (end and start), however I do find that having the topical title and the topic reference (a1) to often blur in memory, and I want to retrieve the verses under a topic but rather retrieve the next section because I jump to the end topical title rather than the start. In terms of the title, I think I like it at the start and end, however I'm not sure about this one. I think we should keep it at the start and end for now. I'm wondering if putting the verse reference on a separate line caused it to be it's own sentence of the song, and uniquely styled rather than on the same line (no new line character) and being sung in one breath. For KJV sources, I'm wondering what the most reputable sources would be? If those 3 are somewhat reputable, I'm okay with them Ideally we'd have those copied to the repository with some reference to the source. Ideally these sources need to be free of copyright restrictions. The procedure sounds generally good! Please weigh on whether to use Navigators or navigators (lower or upper case).
- I'm okay with this. Let's go ahead
- Please continue.
