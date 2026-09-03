# Song Screen: packet-e-take3

- Source file: `/Users/fala/Music/scripture-memorization/navigators/songs/packet-e-take3.mp3`
- Duration: 04:59 (299.1s)
- Expected lyrics source: `/Users/fala/Music/scripture-memorization/navigators/lyrics/packet-e.md`
- Transcription model: faster-whisper `small` (local CPU, int8)

## Verdict: FAIL

- Spoken-word check: PASS (spoken fraction 0.0%, longest suspect range 0.0s)
- Lyric-fidelity check: FAIL (overall WER 7.6%, 2 missing / 1 altered / 17 transcriber-uncertain lines, 0 repeat finding(s))

## Spoken-Word Screen

- **Spoken-fraction estimate (of full track): 0.0%**
- Longest single suspect range: 0.0s
- Melodicity threshold used: **0.40** (calibrated on packet-a-memorized.mp3; see screen-packet-a-memorized.md)

### Suspect time ranges

None. No windows fell below the melodicity threshold.

## Lyric-Fidelity Check

- Overall word-error estimate: **7.6%** (488 reference words)
- Per-line noise threshold (transcriber-uncertainty ceiling): **0.70** (calibrated on packet-a-memorized.mp3)
- Lines: 52 total, 2 missing, 1 altered, 17 transcriber-uncertain (passing), rest exact.

### Missing / altered lines (structural)

| # | Status | Expected | Heard |
|---|---|---|---|
| 1 | ALTERED (wer=1.00) | Packet Ee | packets being |
| 3 | MISSING (wer=1.00) | Love | (nothing) |
| 51 | MISSING (wer=1.00) | Packet Ee | (nothing) |

### Transcriber-uncertain lines (passing; ASR noise only)

| # | wer | Expected | Heard |
|---|---|---|---|
| 2 | 0.33 | Grow in Christlikeness | grown in christlikeness |
| 4 | 0.40 | Ee One and Ee Two | lovey 1 and ay 2 |
| 6 | 0.10 | A new commandment I give unto you, That ye love one another; as I have loved you, that ... | ay new commandment i give unto you that ye love 1 another... |
| 9 | 0.11 | My little children, let us not love in word, neither in tongue; but in deed and in truth. | my little children let us not love in word neither in ton... |
| 10 | 0.25 | First John three eighteen. | 1 john 3 t |
| 13 | 0.20 | Philippians two three to four. | philippians 2 3 2 4 |
| 14 | 0.03 | Let nothing be done through strife or vainglory; but in lowliness of mind let each este... | let nothing be done through strife or glory but in lowlin... |
| 15 | 0.20 | Philippians two three to four. | philippians 2 3 2 4 |
| 17 | 0.06 | Likewise, ye younger, submit yourselves unto the elder. Yea, all of you be subject one ... | wise he younger submit yourselves unto the elder yea all ... |
| 18 | 0.17 | First Peter five five to six. | 1 peter 5 5 2 6 |
| 22 | 0.11 | But fornication, and all uncleanness, or covetousness, let it not be once named among y... | but fornication and all uncleanness or covetousness let i... |
| 28 | 0.40 | Ee Seven and Ee Eight | 7 and 8 |
| 30 | 0.08 | Ye shall not steal, neither deal falsely, neither lie one to another. | he shall not steal neither deal falsely neither lie 1 to ... |
| 33 | 0.05 | And herein do I exercise myself, to have always a conscience void of offence toward God... | and herein do i exercise myself to have always ay conscie... |
| 44 | 0.40 | Ee Eleven and Ee Twelve | see 11 and dee 12 |
| 47 | 0.20 | Galatians six nine to ten. | galatians 6 9 2 10 |
| 52 | 0.67 | Grow in Christlikeness | packety growing christlikeness |

### Repeated-beyond-format findings

None.

## Calibration

- Calibration reference: `packet-a-memorized.mp3` (Suno clip f3eb752c-a4c6-446a-9e42-8f12dd90a8b2), the human-designated memorized take.
- Melodicity threshold: 0.40 (window suspect if melodicity < threshold); window 2.0s / hop 1.0s.
- Lyric-fidelity noise threshold: 0.70 — a line's (substitutions+deletions)/length must exceed this to count as 'altered' rather than ordinary transcriber uncertainty. Calibrated by transcribing packet-a-memorized.mp3 (known-correct v1 lyrics, 64 lines) and inspecting the per-line word-error distribution: 49/64 lines were exact, most of the rest were small ASR noise (dropped short words, minor substitutions), and the noise topped out at 0.67 for a systematic ASR quirk — adjacent chapter/verse number words collapsing into one 'year-like' 4-digit token (e.g. 'eighteen twenty' -> '1820'). 0.70 sits just above that systematic-noise band. One single-word line ('Witnessing' misheard as 'missing', wer=1.00) still exceeds it on the calibration baseline itself and is reported there as a known residual false positive, for the same reason a one-word line has no middle ground between 0% and 100% word-error — this mirrors how the melodicity check accepts a small number of residual flags on Packet A for human confirmation rather than tuning them away entirely.

## Caveats (heuristic, advisory only)

- Both checks are local heuristics, not ground truth. The human ear is the final judge.
- Spoken-word check: cannot reliably distinguish rap-adjacent/chant-like melodic delivery from speech; heavily processed vocals (auto-tune/vocoder) can hide genuinely spoken passages; breathy or quiet singing may drop out of scoring; dense percussive backing can leak into the harmonic component and distort pitch tracking.
- Lyric-fidelity check: transcription is imperfect, especially for short letter+number designators (e.g. 'Bee One' is often heard by the ASR as 'B1' or similar compact forms) — this is exactly the kind of noise the calibrated threshold is meant to absorb, but an unusually noisy passage can still push a genuinely-correct line over the threshold.
- The word-level alignment is a single global edit-distance alignment against the whole song; when the reference contains repeated text (the reference-sandwich pattern) and a nearby line is genuinely missing or reordered, the alignment can misattribute matched words to the wrong occurrence, which may show as a confusing diff on an adjacent line. Repeat detection is a best-effort substring check restricted to hypothesis text not already claimed by another line's alignment, to avoid false positives from coincidental phrase overlap (e.g. a topic name that is also a literal substring of the following verse) — this can occasionally under-count a real repeat if it sits immediately next to an unrelated missing/altered line, though in that case the take already fails on the other grounds.
- No cloud services were used for either check; faster-whisper model weights are downloaded once from Hugging Face and cached locally, then all inference runs on-device.
- Final judgment belongs to the human ear; this tool exists to prioritize listening time, not replace it.

## Verification Addendum (medium-model re-check, 2026-09-02)

This is Packet E round 2 (take3, take4 — same lyrics and style as round 1,
byte-verified before generation). Given round 1's experience with choral
reverb degrading `small`-model accuracy, every structural finding below was
independently re-checked with a full-track faster-whisper `medium`
re-transcription (local CPU, int8; no cloud inference) before being allowed
to stand — none were assumed to be ASR noise. Transcript saved at
`packet_e_take3_medium_segments.json` in the scratch directory. Re-running
the alignment against the medium transcript (same 0.70 threshold) drops
overall WER from 7.6% (small) to 4.3% (medium), with 0 missing, 0 altered
beyond the bookend lines below, and 0 repeats.

| Finding (round-2, small model) | Verdict | Evidence |
|---|---|---|
| Line 1 "Packet Ee" (opening) ALTERED, heard "packets being" | **ASR_MISS** | Medium transcript `[0.0–16.0]`: *"Pack it deep, grow in crisp likeness, Love, E1 and E2, John 13, 34 to 35,"* — "Pack it deep" is a recognizable phonetic rendering of "Packet Ee," immediately followed by "grow in crisp likeness" (="Grow in Christlikeness") and then "Love" and the correct designator/reference. Content confirmed present. |
| Line 3 "Love" (topic title) MISSING, heard nothing | **ASR_MISS** | Same segment above: "Love" is clearly and cleanly transcribed by the medium model, immediately before "E1 and E2." The small model dropped it entirely; the medium model has no trouble with it. |
| Line 51 "Packet Ee" (closing) MISSING, heard nothing | **ASR_MISS** | Final medium segment `[289.0–297.0]`: *"Packety, growing, Chris-like-ness"* — a garbled but recognizable rendering of the closing "Packet Ee, Grow in Christlikeness" bookend. Content present, same fade-out/reverb difficulty seen on every other take (including the Packet A calibration reference itself). |

No repeats were found by the automated check against either transcript, and
manual inspection of the full medium transcript confirms all six topics
(Love, Humility, Purity, Honesty, Faith, Good Works) appear exactly once
each with their reference sandwiches intact — no duplicated verses or
references anywhere, unlike round-1 take1's confirmed outro repeat.

**Updated assessment: packet-e-take3 has no confirmed real lyric-fidelity
defects.** Every flagged line resolves to the same bookend
fade-in/fade-out transcription difficulty observed on the Packet A
calibration reference and on every other Packet E take screened so far —
not a missing, altered, or repeated line. This is the cleanest Packet E
take across both generation rounds (see `screen-packet-e-take2.md` for its
one confirmed minor defect, and `screen-packet-e-take4.md` for round 2's
other take).

## Human Prompts

#### Initial Document Written On 2026-09-02

- Generated automatically by `screen_song.py` per `navigators/procedures/04-spoken-word-screen.md` (spoken-word + lyric-fidelity screening pass).

#### Document Modification On 2026-09-02

- Coordinator follow-up: Packet E round 2 (take3, take4) generated with byte-verified identical lyrics/style. Run both checks on take3 and take4, and — given what was learned about small-model noise on this choral style — verify every structural finding (missing/repeated/reordered) directly with the medium model before letting it stand, rather than assuming ASR miss. Report REAL/ASR_MISS/UNCLEAR per finding with excerpts and timestamps, then recommend a final Packet E official take among take2, take3, and take4 (best lyric fidelity wins, tie-break lower spoken fraction), noting this is the last round.
