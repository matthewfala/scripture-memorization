# Song Screen: packet-e-take7-vocals

- Source file: `/Users/fala/Music/scripture-memorization/navigators/songs/stems/packet-e-take7-vocals.mp3`
- Duration: 05:14 (314.4s)
- Expected lyrics source: `navigators/lyrics/packet-e.md`
- Transcription model: faster-whisper `medium` (local CPU, int8)

## Verdict: FAIL

- Spoken-word check: PASS (spoken fraction 0.0%, longest suspect range 0.0s)
- Lyric-fidelity check: FAIL (overall WER 33.6%, 11 missing / 4 altered / 19 transcriber-uncertain lines, 1 repeat finding(s))

## Spoken-Word Screen

- **Spoken-fraction estimate (of full track): 0.0%**
- Longest single suspect range: 0.0s
- Melodicity threshold used: **0.65** (calibrated on packet-a-memorized.mp3; see screen-packet-a-memorized.md)

### Suspect time ranges

None. No windows fell below the melodicity threshold.

## Lyric-Fidelity Check

- Overall word-error estimate: **33.6%** (488 reference words)
- Per-line noise threshold (transcriber-uncertainty ceiling): **0.70** (calibrated on packet-a-memorized.mp3)
- Lines: 52 total, 11 missing, 4 altered, 19 transcriber-uncertain (passing), rest exact.

### Missing / altered lines (structural)

| # | Status | Expected | Heard |
|---|---|---|---|
| 1 | MISSING (wer=1.00) | Packet Ee | (nothing) |
| 2 | ALTERED (wer=1.00) | Grow in Christlikeness | and the song |
| 11 | MISSING (wer=1.00) | Humility | (nothing) |
| 19 | ALTERED (wer=1.00) | Purity | purism |
| 24 | MISSING (wer=1.00) | First Peter two eleven. | (nothing) |
| 27 | MISSING (wer=1.00) | Honesty | (nothing) |
| 28 | MISSING (wer=1.00) | Ee Seven and Ee Eight | (nothing) |
| 29 | MISSING (wer=1.00) | Leviticus nineteen eleven. | (nothing) |
| 30 | MISSING (wer=1.00) | Ye shall not steal, neither deal falsely, neither lie one to another. | (nothing) |
| 32 | MISSING (wer=1.00) | Acts twenty-four sixteen. | (nothing) |
| 40 | MISSING (wer=1.00) | Romans four twenty to twenty-one. | (nothing) |
| 43 | MISSING (wer=1.00) | Good Works | (nothing) |
| 44 | MISSING (wer=1.00) | Ee Eleven and Ee Twelve | (nothing) |
| 51 | ALTERED (wer=1.00) | Packet Ee | broke in |
| 52 | ALTERED (wer=1.00) | Grow in Christlikeness | christ my quest |

### Transcriber-uncertain lines (passing; ASR noise only)

| # | wer | Expected | Heard |
|---|---|---|---|
| 4 | 0.40 | Ee One and Ee Two | me 1 and me 2 |
| 6 | 0.05 | A new commandment I give unto you, That ye love one another; as I have loved you, that ... | ay new commandment i give unto you that ye love 1 another... |
| 9 | 0.33 | My little children, let us not love in word, neither in tongue; but in deed and in truth. | my little children let us not love in word neither in tongue |
| 12 | 0.20 | Ee Three and Ee Four | humanity 3 and ee 4 |
| 13 | 0.20 | Philippians two three to four. | philippians 2 3 2 4 |
| 14 | 0.05 | Let nothing be done through strife or vainglory; but in lowliness of mind let each este... | let nothing be done through strife or glory but in lowlin... |
| 15 | 0.40 | Philippians two three to four. | ants 2 3 2 4 |
| 16 | 0.17 | First Peter five five to six. | 1 peter 5 5 2 6 |
| 17 | 0.08 | Likewise, ye younger, submit yourselves unto the elder. Yea, all of you be subject one ... | wise ye youngers submit yourselves unto the elder yet all... |
| 20 | 0.40 | Ee Five and Ee Six | in 5 and in 6 |
| 22 | 0.28 | But fornication, and all uncleanness, or covetousness, let it not be once named among y... | but fornication and all uncleanness let it not be once na... |
| 25 | 0.67 | Dearly beloved, I beseech you as strangers and pilgrims, abstain from fleshly lusts, wh... | dearly beloved abstain from fleshly lusts |
| 26 | 0.25 | First Peter two eleven. | 1 peter 2 |
| 31 | 0.67 | Leviticus nineteen eleven. | 11 |
| 41 | 0.44 | He staggered not at the promise of God through unbelief; but was strong in faith, givin... | he staggered not at the promise of god through unbelief a... |
| 42 | 0.60 | Romans four twenty to twenty-one. | romans 4 |
| 46 | 0.21 | And let us not be weary in well doing: for in due season we shall reap, if we faint not... | for in due season we shall reap if we faint not as we hav... |
| 47 | 0.20 | Galatians six nine to ten. | galatians 6 9 10 |
| 49 | 0.09 | Let your light so shine before men, that they may see your good works, and glorify your... | let your light so shine before men that they may see all ... |

### Repeated-beyond-format findings

| Text | Expected count | Observed count |
|---|---|---|
| Love | 1 | 7 |

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
