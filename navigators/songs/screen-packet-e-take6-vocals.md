# Song Screen: packet-e-take6-vocals

- Source file: `/Users/fala/Music/scripture-memorization/navigators/songs/stems/packet-e-take6-vocals.mp3`
- Duration: 05:28 (327.6s)
- Expected lyrics source: `navigators/lyrics/packet-e.md`
- Transcription model: faster-whisper `medium` (local CPU, int8)

## Verdict: FAIL

- Spoken-word check: PASS (spoken fraction 0.9%, longest suspect range 3.0s)
- Lyric-fidelity check: FAIL (overall WER 20.9%, 7 missing / 2 altered / 17 transcriber-uncertain lines, 0 repeat finding(s))

## Spoken-Word Screen

- **Spoken-fraction estimate (of full track): 0.9%**
- Longest single suspect range: 3.0s
- Melodicity threshold used: **0.65** (calibrated on packet-a-memorized.mp3; see screen-packet-a-memorized.md)

### Suspect time ranges

| Range | Duration | Mean melodicity |
|---|---|---|
| 04:20–04:23 | 3.0s | 0.63 |

## Lyric-Fidelity Check

- Overall word-error estimate: **20.9%** (488 reference words)
- Per-line noise threshold (transcriber-uncertainty ceiling): **0.70** (calibrated on packet-a-memorized.mp3)
- Lines: 52 total, 7 missing, 2 altered, 17 transcriber-uncertain (passing), rest exact.

### Missing / altered lines (structural)

| # | Status | Expected | Heard |
|---|---|---|---|
| 1 | MISSING (wer=1.00) | Packet Ee | (nothing) |
| 2 | MISSING (wer=1.00) | Grow in Christlikeness | (nothing) |
| 3 | MISSING (wer=1.00) | Love | (nothing) |
| 4 | MISSING (wer=1.00) | Ee One and Ee Two | (nothing) |
| 5 | MISSING (wer=1.00) | John thirteen thirty-four to thirty-five. | (nothing) |
| 31 | MISSING (wer=1.00) | Leviticus nineteen eleven. | (nothing) |
| 32 | MISSING (wer=1.00) | Acts twenty-four sixteen. | (nothing) |
| 34 | ALTERED (wer=1.00) | Acts twenty-four sixteen. | back up 2416 |
| 51 | ALTERED (wer=1.00) | Packet Ee | can he |

### Transcriber-uncertain lines (passing; ASR noise only)

| # | wer | Expected | Heard |
|---|---|---|---|
| 6 | 0.49 | A new commandment I give unto you, That ye love one another; as I have loved you, that ... | i have loved you that all so love 1 another i wish that a... |
| 8 | 0.50 | First John three eighteen. | 1 john 3d |
| 9 | 0.28 | My little children, let us not love in word, neither in tongue; but in deed and in truth. | my little children that are such ay good word neither in ... |
| 10 | 0.25 | First John three eighteen. | verse john 3 18 |
| 13 | 0.20 | Philippians two three to four. | philippians 2 3 2 4 |
| 14 | 0.14 | Let nothing be done through strife or vainglory; but in lowliness of mind let each este... | let nothing be done through strife or glory but the lonel... |
| 17 | 0.08 | Likewise, ye younger, submit yourselves unto the elder. Yea, all of you be subject one ... | like whitey younger submit yourselves unto the elder year... |
| 22 | 0.17 | But fornication, and all uncleanness, or covetousness, let it not be once named among y... | but occasion and all uncleanness or covetousness let it n... |
| 25 | 0.17 | Dearly beloved, I beseech you as strangers and pilgrims, abstain from fleshly lusts, wh... | dearly beloved i beseech you as strangers and pilgrims un... |
| 30 | 0.50 | Ye shall not steal, neither deal falsely, neither lie one to another. | ye shall not steal the deal falsely |
| 33 | 0.05 | And herein do I exercise myself, to have always a conscience void of offence toward God... | and herein do i exercise myself to have always ay conscio... |
| 37 | 0.67 | Hebrews eleven six. | hebrews 116 |
| 38 | 0.03 | But without faith it is impossible to please him: for he that cometh to God must believ... | but without faith it is impossible to please him for he t... |
| 39 | 0.67 | Hebrews eleven six. | hebrews 116 |
| 44 | 0.40 | Ee Eleven and Ee Twelve | the 11 and the 12 |
| 46 | 0.05 | And let us not be weary in well doing: for in due season we shall reap, if we faint not... | and let us not be weary in well doing for in due season w... |
| 52 | 0.67 | Grow in Christlikeness | go in likeness |

### Repeated-beyond-format findings

None.

## Calibration

- Calibration reference: `packet-a-memorized.mp3` (Suno clip f3eb752c-a4c6-446a-9e42-8f12dd90a8b2), the human-designated memorized take.
- Melodicity threshold: 0.65 (window suspect if melodicity < threshold); window 2.0s / hop 1.0s.
- Lyric-fidelity noise threshold: 0.70 — a line's (substitutions+deletions)/length must exceed this to count as 'altered' rather than ordinary transcriber uncertainty. Calibrated by transcribing packet-a-memorized.mp3 (known-correct v1 lyrics, 64 lines) and inspecting the per-line word-error distribution: 49/64 lines were exact, most of the rest were small ASR noise (dropped short words, minor substitutions), and the noise topped out at 0.67 for a systematic ASR quirk — adjacent chapter/verse number words collapsing into one 'year-like' 4-digit token (e.g. 'eighteen twenty' -> '1820'). 0.70 sits just above that systematic-noise band. One single-word line ('Witnessing' misheard as 'missing', wer=1.00) still exceeds it on the calibration baseline itself and is reported there as a known residual false positive, for the same reason a one-word line has no middle ground between 0% and 100% word-error — this mirrors how the melodicity check accepts a small number of residual flags on Packet A for human confirmation rather than tuning them away entirely.

## Caveats (heuristic, advisory only)

- Both checks are local heuristics, not ground truth. The human ear is the final judge.
- Spoken-word check: cannot reliably distinguish rap-adjacent/chant-like melodic delivery from speech; heavily processed vocals (auto-tune/vocoder) can hide genuinely spoken passages; breathy or quiet singing may drop out of scoring; dense percussive backing can leak into the harmonic component and distort pitch tracking.
- Lyric-fidelity check: transcription is imperfect, especially for short letter+number designators (e.g. 'Bee One' is often heard by the ASR as 'B1' or similar compact forms) — this is exactly the kind of noise the calibrated threshold is meant to absorb, but an unusually noisy passage can still push a genuinely-correct line over the threshold.
- The word-level alignment is a single global edit-distance alignment against the whole song; when the reference contains repeated text (the reference-sandwich pattern) and a nearby line is genuinely missing or reordered, the alignment can misattribute matched words to the wrong occurrence, which may show as a confusing diff on an adjacent line. Repeat detection is a best-effort substring check restricted to hypothesis text not already claimed by another line's alignment, to avoid false positives from coincidental phrase overlap (e.g. a topic name that is also a literal substring of the following verse) — this can occasionally under-count a real repeat if it sits immediately next to an unrelated missing/altered line, though in that case the take already fails on the other grounds.
- No cloud services were used for either check; faster-whisper model weights are downloaded once from Hugging Face and cached locally, then all inference runs on-device.
- Final judgment belongs to the human ear; this tool exists to prioritize listening time, not replace it.

## Human Prompts

#### Initial Document Written On 2026-09-02

- Generated automatically by `screen_song.py` per `navigators/procedures/04-spoken-word-screen.md` (spoken-word + lyric-fidelity screening pass).
