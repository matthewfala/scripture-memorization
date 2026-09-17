# Song Files

Audio downloaded from the user's Suno account (workspace "Packets" for B–E;
Packet A takes predate this pipeline). Two takes per generation; the human
chooses which take to memorize. Style status at generation: A LOCKED,
B–E PROPOSED (pending sampling).

| File | Packet | Duration | Notes |
|---|---|---|---|
| packet-a-memorized.mp3 | A | 5:21 | **OFFICIAL** — Suno clip f3eb752c-a4c6-446a-9e42-8f12dd90a8b2, human-designated memorized take (2026-09-02); calibration reference |
| packet-a-take1.mp3 | A | 5:33 | Suno clip d872abc8-aa15-40b1-8955-1ccb71d30b5f; non-memorized A take |
| packet-a-take2.mp3 | A | 5:25 | Suno clip d5367c4b-f0c0-4fb0-95f2-12a986465f57; non-memorized A take |
| packet-b-take1.mp3 | B | 3:52 | Generated 2026-09-02, v5.5, gospel soul style |
| packet-b-take2.mp3 | B | 4:08 | Generated 2026-09-02, v5.5, gospel soul style; **PROPOSED OFFICIAL** (screening 2026-09-02, pending human listen) |
| packet-c-take1.mp3 | C | 5:30 | Generated 2026-09-02, v5.5, eighties ballad style |
| packet-c-take2.mp3 | C | 5:44 | Generated 2026-09-02, v5.5, eighties ballad style; **OFFICIAL (LOCKED 2026-09-15)** — human listened and accepted |
| packet-d-take1.mp3 | D | 5:03 | Generated 2026-09-02, v5.5, bluegrass style; **PROPOSED OFFICIAL** — human likes the sound but reported spoken portions (3:54, 4:02, 4:10, 4:17, 4:40), confirmed by stem screening at 13.8% spoken (REGENERATE by rule; human override pending) |
| packet-d-take2.mp3 | D | 5:14 | Generated 2026-09-02, v5.5, bluegrass style; screening suggests possible ordering irregularity near the intro |
| packet-e-take1.mp3 | E | 6:07 | Generated 2026-09-02, v5.5, choral hymn style; REJECTED — entire outro (final verse + reference + bookend) confirmed sung twice |
| packet-e-take2.mp3 | E | 6:13 | Generated 2026-09-02, v5.5, choral hymn style; runner-up — one confirmed doubled word ("Purity"), otherwise clean |
| packet-e-take3.mp3 | E | 4:59 | Round 2, 2026-09-02, same lyrics/style; **PROPOSED OFFICIAL** — zero confirmed defects (all flags resolved to transcriber noise) |
| packet-e-take4.mp3 | E | 5:12 | Round 2, 2026-09-02; close second — one UNCLEAR opening-line finding, needs a ~10s human listen |
| packet-b-take3.m4a | B | 4:28 | v6 round 1, 2026-09-15; clip bb18a496; **POOL CANDIDATE** — stem screen PASS (5.2% spoken, bookend-only flags) |
| packet-b-take4 | B | 4:20 | v6 round 1, 2026-09-15; clip b4394a32; FAIL (3 missing lines); file retrieval pending |
| packet-b-take5..take6 | B | 4:19/4:26 | Sept 10 human-generated v6 takes (clips 397c6b00/e97cbb00), adopted as candidates; both FAIL (structural looseness, WER >30%); stems only |
| packet-b-take7 | B | 4:31 | v6 round 2, 2026-09-17; clip 3d64c597; FAIL (5 missing designator/reference lines, no verse loss); **third pool slot** by least-bad; file retrieval pending |
| packet-b-take8 | B | 4:31 | v6 round 2, 2026-09-17; clip 77aa6fee; FAIL (6 missing incl. a block); stems only |
| packet-d-take3.m4a | D | 4:32 | v6 round 1, 2026-09-15; clip fb9c4bea; **POOL CANDIDATE** — stem screen PASS (7.4% spoken, bookend-only) |
| packet-d-take4.m4a | D | 4:40 | v6 round 1, 2026-09-15; clip cfd39f29; FAIL (12.1% spoken) |
| packet-d-take5.m4a | D | 4:32 | v6 round 2, 2026-09-16; clip 04eca652; **POOL CANDIDATE** — PASS (1.1% spoken, 9.3% WER; opening bookends unheard — spot-listen the intro) |
| packet-d-take6.m4a | D | 4:02 | v6 round 2, 2026-09-16; clip 93c07b14; **POOL CANDIDATE** — PASS (3.7% spoken, 4.9% WER — cleanest take of the project) |
| packet-e-take5.mp3 | E | 5:17 | v6 round 1, 2026-09-15; clip 17090669; **POOL CANDIDATE** — stem screen PASS (0.9% spoken) |
| packet-e-take6.m4a | E | 5:28 | v6 round 1, 2026-09-15; clip d3900654; FAIL (7 missing lines incl. opening) |
| packet-e-take7 | E | 5:14 | Sept 9 human-generated v6 take (clip 80cf869b), adopted as candidate; FAIL (WER 33.6%, missing lines); stems only |

Screening reports (`screen-*.md`) are produced per Procedure 04.

## Official Take Selection (screening round 1, 2026-09-02)

All eight B–E takes pass the spoken-word check (worst: b-take1 at 7.8%,
under the 10% limit). The lyric-fidelity check mechanically flagged every
take, but for B, C, and D the flags sit on short bookend/designator/
reference lines where local transcription is weakest — disclosed in each
report's caveats — not on verse content. Proposed selections: **B take 2,
C take 2, D take 1** (best fidelity profile per packet), pending the
human ear.

**Packet E resolution**: medium-model verification showed round 1's
"missing Honesty block" was a transcriber miss — the real defects were
take 1's duplicated outro (confirmed structural, rejected) and take 2's
doubled word "Purity". Round 2 (takes 3 and 4, same lyrics/style)
produced **take 3 with zero confirmed defects → PROPOSED OFFICIAL for
E**; take 4 is a close second with one unresolved opening-line finding.
Round cap (2 of 2) reached.

Note: the Suno library also contains an accidental extra E generation
pair (1:40 and 2:00 clips, from a double submission during round 2, not
downloaded) — safe for the human to trash.

Note (2026-09-15, corrected 2026-09-17): the six "stray" v6 clips
(four B: 4:19/4:26/4:34/4:23, two E: 5:14/5:05) were NOT phantom
submissions — they are v6 takes the human generated themselves on
Sept 9-10 with the exact committed styles. Three were adopted and
screened as candidates (b-take5, b-take6, e-take7); all three failed
on structural looseness. The remaining two (B 4:34/4:23, E 5:05)
were left unscreened after that pattern. Suno's per-song download
system (Pro quota, 27/month, refreshes 10/6) delivers m4a (~134 kbps
AAC) or mp3 (64 kbps); ~8 downloads remain this month.

## Candidate pools (v6 series result, 2026-09-17)

- **D — pool complete, all stem-verified passers**: take3 (7.4%
  spoken), take5 (1.1% spoken, 9.3% WER), take6 (3.7% spoken, 4.9%
  WER — the cleanest take of the whole project).
- **E — pool complete**: take3 (v5.5 — zero confirmed defects per the
  Sept 2 medium verification; stem spoken 1.0%), take5 (v6 — 0.9%
  spoken, no missing content), take2 (v5.5 runner-up — one confirmed
  doubled word "Purity"; stem not screened).
- **B — pool closed short of 3 clean passers**: take3 (v6 — clean
  pass, bookend-only flags), take2 (v5.5 — borderline: one missing
  designator, phonetic near-misses on others), take7 (v6 round 2 —
  best of the fails: 5 missing designator/reference lines but no
  verse text lost). All four v6 B takes plus both Sept-10 takes
  dropped short designator/reference lines — a consistent
  genre-level failure mode of the gospel call-and-response style,
  recorded in style-preferences.md per Procedure 04; revising B's
  style (Procedure 00) is the alternative to accepting this trait.

Suggested human listens, in priority order: e-take3 (proposed official,
full listen), b-take1's first seconds (opening lines unheard by the
transcriber), d-take2's intro (possible ordering irregularity),
e-take4's first ~10s (the UNCLEAR finding, only if curious).

## Stem-based re-screening (2026-09-15)

The human caught five spoken portions in d-take1 (3:54, 4:02, 4:10,
4:17, 4:40) that the full-mix screen had scored 0.0% spoken — proving
full-mix melodicity blind to speech over pitched accompaniment. Vocal
stems (Suno Get Stems, `stems/` folder) fix this: on the isolated vocal,
d-take1 screens at **13.8% spoken** (12 ranges — all five human spots,
plus 1:52–2:04 and others), a REGENERATE verdict, while the memorized A
stem passes at 3.7% (four short residual ranges: 0:38, 2:09, 4:23, 4:37,
pending human confirmation). Stem screening is now the Procedure 04
default (threshold 0.65, min-run 2); B, C, and E official takes have not
yet been stem-screened. D's official status awaits the human's call:
override (keep take1 for its sound) or regenerate D (round 2 of 2).

## official/ copies (Procedure 06)

`navigators/official/packet-<letter>.mp3` holds the canonical copy of
each packet's current official take. As of 2026-09-15: a ←
packet-a-memorized (LOCKED, human-designated); **c ← c-take2 (LOCKED
2026-09-15, human listened and accepted)**; b ← b-take2, d ← d-take1,
e ← e-take3 (PROPOSED — a v6 regeneration series is in progress for
B, D, and E per the human's request; each will get a pool of 3
stem-screen-passing candidates for the human to choose from). On lock or
override, update the status here and re-copy per Procedure 06.

## Calibration ruling (2026-09-15)

The human reviewed the memorized A stem's four residual flagged ranges
(0:38, 2:09, 4:23, 4:37): "I can hear spoken slightly, but I'd still
classify these as singing." The stem-mode calibration (threshold 0.65,
min-run 2) stands confirmed — A's flags are the acceptable borderline,
and takes flagging materially above A's 3.7% remain suspect.

## Human Prompts

#### Initial Document Written On 2026-09-02

- I'm logged into suno on chrome now. Can you please generate the 5 packets songs? Please store the song mp3 in the folder once generated. Ideally screen for the spoken words rather than sung and regenerate or change the style if so.

#### Document Modification On 2026-09-02

- Here's the song for packet A I memorized. https://suno.com/s/WuvaIW3gO07diy4P Also can we have the checker check the lyrics match exactly as expected too or else regenerate. Ideally we should select the official song for each lyric/style combo
- Maybe you can start a loop

#### Document Modification On 2026-09-02 (repeatability pass)

- Are the procedures repeatable by another context?
- Yes please add these to a new folder in the root repo. Please also add process to copy the official song to another folder denoting the official songs. Please make the entire pipeline process completely repeatable including the file naming conventions and what files to update after when etc.

#### Document Modification On 2026-09-15 (stem-based screening)

- Packet D, I like the sound, however there are portions that are spoken around 3:54 and 4:02 and 04:10 and 04:17 04:40. Is the automated detector able to be calibrated to detect this?
- I'm pretty sure suno has this feature, you can download the spoken section without the music on the website?

#### Document Modification On 2026-09-15 (C locked, v6 regeneration series)

- I have been listening to C so that one is now locked. Can we lock it? Can you regenerate D? Perhaps we can have 3 candidates (which pass) for each. Also I'd like to regenerate E & B. Please try out the new Suno v6 model. Also for the A packet, I can hear spoken slightly, but I'd still classify these as singing.
