# Procedure 00 — Style Partition

## Purpose

Assign each grouping a Suno style such that the groupings are evenly spaced
over the domain of musical styles — no two groupings overlap — while never
altering the style of any grouping whose music is already memorized or
accepted. The partition is re-runnable: when preferences change, only
non-committed entries are re-derived.

## Groupings

A **grouping** is a unit that owns one style:

- The five lettered packets A–E (Part 1 of `packets.md`).
- The five numbered Series S1–S5 (Part 2 of `packets.md`). Series receive
  style reservations now so the space stays evenly spread before any packet
  locks; their lyrics format is deliberately TBD and will be defined by a
  future procedure.

Songs within a grouping share the grouping's style: a packet split into two
parts, or a Series eventually split into several songs, is still one
grouping with one style.

## Inputs

- `navigators/style-preferences.md` — the human's musical constraints.
  Read this first; it filters the style space below.
- `navigators/styles.md` — the registry (create it if missing, seeding the
  LOCKED Packet A entry given below).
- `navigators/extracted/packets.md` — the groupings to cover (Parts 1
  and 2).

## Output

- `navigators/styles.md` updated: one entry per grouping.

## Entry statuses

| Status | Meaning | May this procedure change it? |
|---|---|---|
| `LOCKED` | Memorization has begun or completed | Never |
| `ACCEPTED` | Human sampled the music and approved | Never |
| `PROPOSED` | Derived by this procedure, awaiting sampling | Yes — see minimal perturbation |

## Fixed point: Packet A

Packet A is `LOCKED` with this style string, exactly:

> Jesus Movement folk - fingerpicked acoustic guitar, close vocal harmony,
> warm 1972 analog tape, gentle 88 BPM, earnest and unhurried.

Its axis coordinates: genre G1, tempo T2 (88 BPM), era E2 (1972), vocal V1.

## The style space

Four axes.

**Genre family** (filter this list through `style-preferences.md` exclusions
before assigning; extend it if exclusions shrink it below the grouping
count):

- G1 Folk / singer-songwriter *(taken by A)*
- G2 Gospel / soul
- G3 Bluegrass / roots country
- G4 Doo-wop / early rock and roll
- G5 Hymn / sacred choral
- G6 Reggae / island
- G7 Jazz / swing
- G8 Bossa nova / Latin
- G9 Pop ballad / soft rock
- G10 Celtic / British Isles folk *(adjacent to G1 — assign it to the
  grouping most distant from A on the other axes)*

**Tempo band**: T1 60–74 · T2 75–89 *(A)* · T3 90–104 · T4 105–119 ·
T5 120–134 BPM. The style string names one specific BPM within the band.

**Era / production**: E1 1960s · E2 1970s analog *(A)* · E3 1980s ·
E4 1990s · E5 contemporary.

**Vocal texture**: V1 close harmony *(A)* · V2 solo lead ·
V3 call-and-response · V4 male-female duet · V5 full choir.

**Spacing rules** (ten groupings over these bands):

1. Every grouping occupies a distinct genre family.
2. On each of tempo, era, and vocal, a band may be used by at most two
   groupings.
3. Any two groupings may share at most ONE band across tempo, era, and
   vocal combined — so every pair of groupings differs on at least three
   of the four axes.

## Steps

1. Read `style-preferences.md`. Remove excluded genre families; note required
   qualities that every style string must express.
2. Read `styles.md`. Record the axis coordinates of every `LOCKED` and
   `ACCEPTED` entry; those assignments are immovable.
3. **Minimal perturbation**: keep every existing `PROPOSED` assignment that
   remains valid under the current constraints and grouping set. Re-derive
   only entries that must move, and record which moved and why in History.
   (A generated-but-not-yet-accepted lyrics file embeds its style string;
   unnecessary churn invalidates it.)
4. For each unassigned grouping (packets in letter order, then Series in
   number order), assign bands satisfying the Spacing rules. Among valid
   assignments, prefer musically natural combinations (a genre's home tempo
   and era) and maximal contrast with already-assigned groupings.
5. Compose each style string in this grammar, matching Packet A's shape:
   `{Genre descriptor} - {instrumentation}, {vocal texture},
   {era/production}, {tempo} BPM, {mood}.`
   Express the required qualities from `style-preferences.md` through the
   genre and descriptor choices, not through negative commands (negative
   commands like "no spoken word" have been observed not to work).
6. Write `styles.md` per the schema below. New entries are `PROPOSED`.
7. Append a History entry: date, what was assigned, kept, or re-derived,
   and which preference lines or constraint changes drove it.
8. Present the resulting registry for human review. Do not commit.

## Registry schema (`navigators/styles.md`)

```markdown
# Style Registry

| Grouping | Status | Style |
|---|---|---|
| A | LOCKED | Jesus Movement folk - ... |
| B | PROPOSED | ... |
| ... | | |
| S1 | PROPOSED | ... |

## Axis coordinates

| Grouping | Genre | Tempo | Era | Vocal |
|---|---|---|---|---|

## Rationale

- B: <why this combination, in one or two sentences>

## History

- <YYYY-MM-DD>: <what changed and why>
```

## Re-running after feedback

When the human rejects a sample or updates `style-preferences.md`: re-run
this procedure. `LOCKED` and `ACCEPTED` entries are immutable fixed points;
`PROPOSED` entries follow minimal perturbation (step 3). Record the
rejection reason in the History section and ensure `style-preferences.md`
was updated to capture it.

## Human Prompts

#### Initial Document Written On 2026-08-27

- I forgot there's also styles that go along with the lyrics. Here's the style for packet A that was memorized: Jesus Movement folk - fingerpicked acoustic guitar, close vocal harmony, warm 1972 analog tape, gentle 88 BPM, earnest and unhurried.
- Ideally one or two files per pack - since that is the granularity of the song. Yes, we need to figure out a procedure to partition the packets such that they do not overlap in style from the start so that when we begin implementing the packets they are evenly spaced over the domain of musical styles.
- Here are some learned experiences with songs: 1. Certain song styles are easier to memorize. - Rythm without melody such as rap is particularly difficult for me to memorize since it blends together. If there are too many repeated melody sections or segments that also blurs together in a song. Suno for some reason has a tendancy with some styles and less for other styles to speak portions of the song and not sing them -- spoken portions are much more difficult to memorize and often do not get memorized as quickly as the rest of the piece. 2. Ideally the framework is flexible enough for me to sample the music and if I reject it or update my preferences we can rebuild the general structure for the styles according to those preferences without altering any of the memorized music.
- fully sung melodic vocals throughout, no spoken word - In my experience this doesn't actually change the outcome of the amount of spoken word so much as the genera of music does. It's hard for me to predict which genres are going to be spoken more. I can share feedback after listening to the music. *(Excerpt; full prompt recorded in `03-lyrics-format.md`.)*
- I'm okay with this. Let's go ahead
- Please continue.

#### Document Modification On 2026-08-28

- Do the style partitions cover the entire pdf?
- I would like to include the other series eventually, however I'm not sure what the best format for converting those sections to song would be just yet.
