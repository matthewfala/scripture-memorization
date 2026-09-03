# Song Screen: packet-e-take2

- Source file: `/Users/fala/Music/scripture-memorization/navigators/songs/packet-e-take2.mp3`
- Duration: 06:13 (373.0s)
- Expected lyrics source: `/Users/fala/Music/scripture-memorization/navigators/lyrics/packet-e.md`
- Transcription model: faster-whisper `small` (local CPU, int8)

## Verdict: FAIL

- Spoken-word check: PASS (spoken fraction 0.0%, longest suspect range 0.0s)
- Lyric-fidelity check: FAIL (overall WER 15.0%, 0 missing / 6 altered / 24 transcriber-uncertain lines, 1 repeat finding(s))

## Spoken-Word Screen

- **Spoken-fraction estimate (of full track): 0.0%**
- Longest single suspect range: 0.0s
- Melodicity threshold used: **0.40** (calibrated on packet-a-memorized.mp3; see screen-packet-a-memorized.md)

### Suspect time ranges

None. No windows fell below the melodicity threshold.

## Lyric-Fidelity Check

- Overall word-error estimate: **15.0%** (488 reference words)
- Per-line noise threshold (transcriber-uncertainty ceiling): **0.70** (calibrated on packet-a-memorized.mp3)
- Lines: 52 total, 0 missing, 6 altered, 24 transcriber-uncertain (passing), rest exact.

### Missing / altered lines (structural)

| # | Status | Expected | Heard |
|---|---|---|---|
| 1 | ALTERED (wer=1.00) | Packet Ee | christigness packeting |
| 11 | ALTERED (wer=1.00) | Humility | eam |
| 12 | ALTERED (wer=0.80) | Ee Three and Ee Four | humility 3 8 eam |
| 28 | ALTERED (wer=1.00) | Ee Seven and Ee Eight | severland he ate |
| 51 | ALTERED (wer=1.00) | Packet Ee | park it |
| 52 | ALTERED (wer=1.00) | Grow in Christlikeness | here grooming christmas |

### Transcriber-uncertain lines (passing; ASR noise only)

| # | wer | Expected | Heard |
|---|---|---|---|
| 2 | 0.67 | Grow in Christlikeness | robe in christigness |
| 4 | 0.40 | Ee One and Ee Two | in 1 and in 2 |
| 6 | 0.17 | A new commandment I give unto you, That ye love one another; as I have loved you, that ... | ay new commandment i give unto you that he love 1 another... |
| 9 | 0.11 | My little children, let us not love in word, neither in tongue; but in deed and in truth. | my little children let us not love in word neither in ton... |
| 10 | 0.50 | First John three eighteen. | 1 strong 3 8 |
| 13 | 0.40 | Philippians two three to four. | philippians 2 3 8 eam |
| 14 | 0.16 | Let nothing be done through strife or vainglory; but in lowliness of mind let each este... | let nothing be done through strive of englory but in lone... |
| 15 | 0.20 | Philippians two three to four. | philippians 2 3 2 4 |
| 16 | 0.17 | First Peter five five to six. | 1 peter 5 5 6 6 |
| 17 | 0.06 | Likewise, ye younger, submit yourselves unto the elder. Yea, all of you be subject one ... | wise ye younger submit yourselves unto the elder yea all ... |
| 18 | 0.17 | First Peter five five to six. | 1 peter 5 5 2 6 |
| 22 | 0.06 | But fornication, and all uncleanness, or covetousness, let it not be once named among y... | but fornication and all uncleanness or covetousness let i... |
| 24 | 0.25 | First Peter two eleven. | 1 ephesians 2 11 |
| 25 | 0.06 | Dearly beloved, I beseech you as strangers and pilgrims, abstain from fleshly lusts, wh... | dearly beloved i beseech you as strangers and pilgrims up... |
| 26 | 0.25 | First Peter two eleven. | 1 peter to 11 |
| 29 | 0.67 | Leviticus nineteen eleven. | leviticus 1911 |
| 30 | 0.08 | Ye shall not steal, neither deal falsely, neither lie one to another. | he shall not steal neither deal falsely neither lie 1 to ... |
| 33 | 0.05 | And herein do I exercise myself, to have always a conscience void of offence toward God... | and herein do i exercise myself to have always ay conscie... |
| 43 | 0.50 | Good Works | good work |
| 44 | 0.20 | Ee Eleven and Ee Twelve | see 11 and ee 12 |
| 46 | 0.02 | And let us not be weary in well doing: for in due season we shall reap, if we faint not... | and let us not be weary in well doing for in due season w... |
| 47 | 0.20 | Galatians six nine to ten. | galatians 6 9 2 10 |
| 48 | 0.33 | Matthew five sixteen. | matthew 5 10 |
| 49 | 0.05 | Let your light so shine before men, that they may see your good works, and glorify your... | let your life so shine before men that they may see your ... |

### Repeated-beyond-format findings

| Text | Expected count | Observed count |
|---|---|---|
| Purity | 1 | 2 |

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

Round-1 lyric-fidelity used faster-whisper `small`. Choral reverb was
suspected to degrade that model, so the round-1 repeat finding (and, per
the coordinator's request, the Honesty-topic content and the ending) were
re-checked against a full-track re-transcription with faster-whisper
`medium` (still local CPU, int8; no cloud inference). Transcript saved at
`packet_e_take2_medium_segments.json` in the scratch directory.

| Finding | Verdict | Evidence |
|---|---|---|
| "Purity" repeated-beyond-format (expected 1x, observed 2x) | **REAL** | Medium-model transcript, `[157.8–165.8]`: *"Purity, purity, E5 and E6, Ephesians 5, 3."* — the topic title is genuinely sung/spoken twice in immediate succession before its designator. This is a small, single-word repeat, not an extra verse or reference. |
| Honesty-topic content ("Ee Seven and Ee Eight" / Leviticus 19:11 sandwich / Acts 24:16 sandwich) — not flagged in round 1, checked per the coordinator's cross-check request | **PRESENT** | `[202.4–243.8]`: *"Honest E7 and E8, Leviticus 1911." / "He shall not steal, neither deal falsely, neither lie one to another." / "Leviticus 1911, Acts 24-16." / "And herein do I exercise myself, to have always a conscience void of offence toward God and toward men." / "Acts 24, 16."* — full sandwich structure and both verses present, with only the usual minor ASR noise ("Honest" for "Honesty", "He" for "Ye"). |
| Ending / closing bookend, checked for comparison against take1's confirmed outro repeat | **CLEAN — no repeat** | `[330.3–362.7]` shows the final verse (Matthew 5:16) and its reference play through exactly once — *"Galatians 6, 9, 2, 10, Matthew 5, 16." "Let your lives so shine before men" "that they may see your good works" "and glorify your Father, which is in heaven, Matthew 5, 16."* — followed immediately by a single closing bookend, *"Pocketing, growing, criss-crossed."* (garbled "Packet Ee, Grow in Christlikeness"). No duplicated material, unlike take1. |

**Updated assessment:** packet-e-take2's only confirmed real defect is the single word "Purity" said twice in a row — a minor, low-impact repeat. Its Honesty-topic content is fully present, and its ending is clean (no repeat), in contrast to take1's confirmed full-outro repeat (see `screen-packet-e-take1.md` addendum). Between the two E takes, **take2 is the safer official pick without regeneration**, pending the human confirming both takes' findings by ear.

## Human Prompts

#### Initial Document Written On 2026-09-02

- Generated automatically by `screen_song.py` per `navigators/procedures/04-spoken-word-screen.md` (spoken-word + lyric-fidelity screening pass).

#### Document Modification On 2026-09-02

- Coordinator follow-up: re-verify the round-1 "Purity" repeat finding with faster-whisper `medium` (stronger model, since choral reverb was suspected to degrade `small`'s accuracy), report REAL / ASR_MISS / UNCLEAR with transcript excerpts and timestamps, and cross-check whether take2's Honesty-topic content and ending are fully present/clean so it could be the safe official pick without regeneration.
