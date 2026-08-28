# Procedure 00 — Style Partition

## Purpose

Assign each packet a Suno style such that the packets are evenly spaced over
the domain of musical styles — no two packets overlap — while never altering
the style of any packet whose music is already memorized or accepted. The
partition is re-runnable: when preferences change, only non-committed entries
are re-derived.

## Inputs

- `navigators/style-preferences.md` — the human's musical constraints.
  Read this first; it filters the style space below.
- `navigators/styles.md` — the registry (create it if missing, seeding the
  LOCKED Packet A entry given below).
- `navigators/extracted/packets.md` — the list of packets to cover.

## Output

- `navigators/styles.md` updated: one entry per packet.

## Entry statuses

| Status | Meaning | May this procedure change it? |
|---|---|---|
| `LOCKED` | Memorization has begun or completed | Never |
| `ACCEPTED` | Human sampled the music and approved | Never |
| `PROPOSED` | Derived by this procedure, awaiting sampling | Yes — freely re-derived |

## Fixed point: Packet A

Packet A is `LOCKED` with this style string, exactly:

> Jesus Movement folk - fingerpicked acoustic guitar, close vocal harmony,
> warm 1972 analog tape, gentle 88 BPM, earnest and unhurried.

Its axis coordinates: genre G1, tempo T2 (88 BPM), era E2 (1972), vocal V1.

## The style space

Four axes. Every packet must occupy a unique band on every axis.

**Genre family** (filter this list through `style-preferences.md` exclusions
before assigning; extend it if more bands are needed than remain):

- G1 Folk / singer-songwriter *(taken by A)*
- G2 Gospel / soul
- G3 Bluegrass / roots country
- G4 Doo-wop / early rock and roll
- G5 Hymn / sacred choral
- G6 Reggae / island
- G7 Jazz / swing
- G8 Bossa nova / Latin
- G9 Pop ballad / soft rock
- G10 Celtic / British Isles folk *(adjacent to G1 — use only if bands run out)*

**Tempo band**: T1 60–74 · T2 75–89 *(taken by A)* · T3 90–104 ·
T4 105–119 · T5 120–134 BPM. The style string names one specific BPM within
the band.

**Era / production**: E1 1960s · E2 1970s analog *(taken by A)* · E3 1980s ·
E4 1990s · E5 contemporary.

**Vocal texture**: V1 close harmony *(taken by A)* · V2 solo lead ·
V3 call-and-response · V4 male-female duet · V5 full choir.

## Steps

1. Read `style-preferences.md`. Remove excluded genre families; note required
   qualities that every style string must express.
2. Read `styles.md`. Record the axis coordinates of every `LOCKED` and
   `ACCEPTED` entry; those bands are taken.
3. For each remaining packet in letter order, assign one free band per axis.
   Among valid assignments, prefer musically natural combinations (a genre's
   home tempo and era) and maximal contrast with already-assigned packets.
4. Compose each style string in this grammar, matching Packet A's shape:
   `{Genre descriptor} - {instrumentation}, {vocal texture},
   {era/production}, {tempo} BPM, {mood}.`
   Express the required qualities from `style-preferences.md` through the
   genre and descriptor choices, not through negative commands (negative
   commands like "no spoken word" have been observed not to work).
5. Write `styles.md` per the schema below. New entries are `PROPOSED`.
6. Append a History entry: date, what was assigned or re-derived, and which
   preference lines drove any change.
7. Present the resulting registry for human review. Do not commit.

## Registry schema (`navigators/styles.md`)

```markdown
# Style Registry

| Packet | Status | Style |
|---|---|---|
| A | LOCKED | Jesus Movement folk - ... |
| B | PROPOSED | ... |

## Axis coordinates

| Packet | Genre | Tempo | Era | Vocal |
|---|---|---|---|---|

## Rationale

- B: <why this combination, in one or two sentences>

## History

- <YYYY-MM-DD>: <what changed and why>
```

## Re-running after feedback

When the human rejects a sample or updates `style-preferences.md`: re-run
this procedure. `LOCKED` and `ACCEPTED` entries are immutable fixed points;
only `PROPOSED` entries are re-derived, spread over whatever bands remain.
Record the rejection reason in the History section and ensure
`style-preferences.md` was updated to capture it.

## Human Prompts

#### Initial Document Written On 2026-08-27

- I forgot there's also styles that go along with the lyrics. Here's the style for packet A that was memorized: Jesus Movement folk - fingerpicked acoustic guitar, close vocal harmony, warm 1972 analog tape, gentle 88 BPM, earnest and unhurried.
- Ideally one or two files per pack - since that is the granularity of the song. Yes, we need to figure out a procedure to partition the packets such that they do not overlap in style from the start so that when we begin implementing the packets they are evenly spaced over the domain of musical styles.
- Here are some learned experiences with songs: 1. Certain song styles are easier to memorize. - Rythm without melody such as rap is particularly difficult for me to memorize since it blends together. If there are too many repeated melody sections or segments that also blurs together in a song. Suno for some reason has a tendancy with some styles and less for other styles to speak portions of the song and not sing them -- spoken portions are much more difficult to memorize and often do not get memorized as quickly as the rest of the piece. 2. Ideally the framework is flexible enough for me to sample the music and if I reject it or update my preferences we can rebuild the general structure for the styles according to those preferences without altering any of the memorized music.
- fully sung melodic vocals throughout, no spoken word - In my experience this doesn't actually change the outcome of the amount of spoken word so much as the genera of music does. It's hard for me to predict which genres are going to be spoken more. I can share feedback after listening to the music. *(Excerpt; full prompt recorded in `03-lyrics-format.md`.)*
- I'm okay with this. Let's go ahead
- Please continue.
