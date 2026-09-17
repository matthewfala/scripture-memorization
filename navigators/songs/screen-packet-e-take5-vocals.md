# Song Screen: packet-e-take5-vocals

- Source file: `/Users/fala/Music/scripture-memorization/navigators/songs/stems/packet-e-take5-vocals.mp3`
- Duration: 05:17 (317.2s)
- Expected lyrics source: `navigators/lyrics/packet-e.md`
- Transcription model: faster-whisper `medium` (local CPU, int8)

## Verdict: FAIL

- Spoken-word check: PASS (spoken fraction 0.9%, longest suspect range 3.0s)
- Lyric-fidelity check: FAIL (overall WER 16.8%, 0 missing / 6 altered / 24 transcriber-uncertain lines, 0 repeat finding(s))

## Spoken-Word Screen

- **Spoken-fraction estimate (of full track): 0.9%**
- Longest single suspect range: 3.0s
- Melodicity threshold used: **0.65** (calibrated on packet-a-memorized.mp3; see screen-packet-a-memorized.md)

### Suspect time ranges

| Range | Duration | Mean melodicity |
|---|---|---|
| 00:03–00:06 | 3.0s | 0.59 |

## Lyric-Fidelity Check

- Overall word-error estimate: **16.8%** (488 reference words)
- Per-line noise threshold (transcriber-uncertainty ceiling): **0.70** (calibrated on packet-a-memorized.mp3)
- Lines: 52 total, 0 missing, 6 altered, 24 transcriber-uncertain (passing), rest exact.

### Missing / altered lines (structural)

| # | Status | Expected | Heard |
|---|---|---|---|
| 1 | ALTERED (wer=1.00) | Packet Ee | it be |
| 2 | ALTERED (wer=1.00) | Grow in Christlikeness | growing risk less |
| 19 | ALTERED (wer=1.00) | Purity | redeem |
| 24 | ALTERED (wer=0.75) | First Peter two eleven. | as peter be led |
| 27 | ALTERED (wer=1.00) | Honesty | august |
| 51 | ALTERED (wer=1.00) | Packet Ee | could he |

### Transcriber-uncertain lines (passing; ASR noise only)

| # | wer | Expected | Heard |
|---|---|---|---|
| 4 | 0.60 | Ee One and Ee Two | you 1 and you too |
| 5 | 0.20 | John thirteen thirty-four to thirty-five. | john 30 34 to 35 |
| 6 | 0.10 | A new commandment I give unto you, That ye love one another; as I have loved you, that ... | ay new commandment i give unto you that ye love 1 another... |
| 9 | 0.17 | My little children, let us not love in word, neither in tongue; but in deed and in truth. | let us not love in word neither in tongue but in deed and... |
| 14 | 0.11 | Let nothing be done through strife or vainglory; but in lowliness of mind let each este... | let nothing be done through strife or glory but in lowlin... |
| 15 | 0.40 | Philippians two three to four. | it to 3 to 4 |
| 16 | 0.17 | First Peter five five to six. | 1 meter 5 5 to 6 |
| 17 | 0.06 | Likewise, ye younger, submit yourselves unto the elder. Yea, all of you be subject one ... | likewise ye younger submit yourselves unto the elder may ... |
| 18 | 0.17 | First Peter five five to six. | 1 peter fire 5 to 6 |
| 20 | 0.40 | Ee Five and Ee Six | me 5 and me 6 |
| 21 | 0.33 | Ephesians five three. | ephesians fire 3 |
| 22 | 0.39 | But fornication, and all uncleanness, or covetousness, let it not be once named among y... | 1 occasion and all planets all cometousness let it not be... |
| 23 | 0.33 | Ephesians five three. | ephesians fire 3 |
| 25 | 0.17 | Dearly beloved, I beseech you as strangers and pilgrims, abstain from fleshly lusts, wh... | dearly beloved i beseech you as strangers and pilgrims st... |
| 26 | 0.25 | First Peter two eleven. | 1 peter to 11 |
| 28 | 0.40 | Ee Seven and Ee Eight | ee vii and ee viii |
| 30 | 0.08 | Ye shall not steal, neither deal falsely, neither lie one to another. | he shall not steal neither deal falsely neither lie 1 to ... |
| 36 | 0.60 | Ee Nine and Ee Ten | be nigh and day 10 |
| 38 | 0.06 | But without faith it is impossible to please him: for he that cometh to God must believ... | with our faith it is impossible to please him for he that... |
| 41 | 0.03 | He staggered not at the promise of God through unbelief; but was strong in faith, givin... | he staggered not at the promise of god through unbelief b... |
| 44 | 0.40 | Ee Eleven and Ee Twelve | 11 and 12 |
| 46 | 0.07 | And let us not be weary in well doing: for in due season we shall reap, if we faint not... | and let us not be weary in well doing for in due season w... |
| 49 | 0.14 | Let your light so shine before men, that they may see your good works, and glorify your... | let your light so shine before men let me see your good w... |
| 52 | 0.67 | Grow in Christlikeness | move in sleepers |

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
