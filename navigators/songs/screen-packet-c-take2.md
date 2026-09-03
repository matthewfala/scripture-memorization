# Song Screen: packet-c-take2

- Source file: `/Users/fala/Music/scripture-memorization/navigators/songs/packet-c-take2.mp3`
- Duration: 05:44 (344.2s)
- Expected lyrics source: `/Users/fala/Music/scripture-memorization/navigators/lyrics/packet-c.md`
- Transcription model: faster-whisper `small` (local CPU, int8)

## Verdict: FAIL

- Spoken-word check: PASS (spoken fraction 0.9%, longest suspect range 2.0s)
- Lyric-fidelity check: FAIL (overall WER 9.3%, 0 missing / 2 altered / 15 transcriber-uncertain lines, 0 repeat finding(s))

## Spoken-Word Screen

- **Spoken-fraction estimate (of full track): 0.9%**
- Longest single suspect range: 2.0s
- Melodicity threshold used: **0.40** (calibrated on packet-a-memorized.mp3; see screen-packet-a-memorized.md)

### Suspect time ranges

| Range | Duration | Mean melodicity |
|---|---|---|
| 03:07–03:09 | 2.0s | 0.24 |
| 05:43–05:44 | 1.2s | 0.39 |

## Lyric-Fidelity Check

- Overall word-error estimate: **9.3%** (428 reference words)
- Per-line noise threshold (transcriber-uncertainty ceiling): **0.70** (calibrated on packet-a-memorized.mp3)
- Lines: 52 total, 0 missing, 2 altered, 15 transcriber-uncertain (passing), rest exact.

### Missing / altered lines (structural)

| # | Status | Expected | Heard |
|---|---|---|---|
| 18 | ALTERED (wer=1.00) | Philippians four thirteen. | he |
| 50 | ALTERED (wer=0.83) | Psalm one nineteen nine and eleven. | psalm 199 n11 |

### Transcriber-uncertain lines (passing; ASR noise only)

| # | wer | Expected | Heard |
|---|---|---|---|
| 1 | 0.50 | Packet See | could see |
| 6 | 0.05 | Know ye not that ye are the temple of God, and that the Spirit of God dwelleth in you? | know ye not that ye are the temple of god and let the spi... |
| 14 | 0.05 | Fear thou not; for I am with thee: be not dismayed; for I am thy God: I will strengthen... | fear thou not for i am with thee be not dismayed for i am... |
| 19 | 0.50 | His Faithfulness | is faithfulness |
| 22 | 0.12 | It is of the LORD’s mercies that we are not consumed, because his compassions fail not.... | of the lord s mercies that we are not consumed because hi... |
| 23 | 0.60 | Lamentations three twenty-two to twenty-three. | lamentations 3 222 223 |
| 26 | 0.67 | Numbers twenty-three nineteen. | numbers 2319 |
| 30 | 0.06 | Thou wilt keep him in perfect peace, whose mind is stayed on thee: because he trusteth ... | thou wilt keep him in perfect peace whose mind is stayed ... |
| 32 | 0.25 | First Peter five seven. | 1 the 5 7 |
| 33 | 0.09 | Casting all your care upon him; for he careth for you. | casting all your care upon him for he careeth for you |
| 38 | 0.08 | He that spared not his own Son, but delivered him up for us all, how shall he not with ... | he that spared not his own son but delivered him up for u... |
| 43 | 0.25 | His Help in Temptation | his help and temptation |
| 46 | 0.06 | For in that he himself hath suffered being tempted, he is able to succour them that are... | for in that he himself hath suffered being tempted he is ... |
| 48 | 0.50 | Psalm one nineteen nine and eleven. | psalm 199 and 11 |
| 49 | 0.10 | Wherewithal shall a young man cleanse his way? by taking heed thereto according to thy ... | all shall ay young man cleanse his way by taking heed the... |

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

## Human Prompts

#### Initial Document Written On 2026-09-02

- Generated automatically by `screen_song.py` per `navigators/procedures/04-spoken-word-screen.md` (spoken-word + lyric-fidelity screening pass).
