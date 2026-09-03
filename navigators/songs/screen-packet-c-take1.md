# Song Screen: packet-c-take1

- Source file: `/Users/fala/Music/scripture-memorization/navigators/songs/packet-c-take1.mp3`
- Duration: 05:30 (329.6s)
- Expected lyrics source: `/Users/fala/Music/scripture-memorization/navigators/lyrics/packet-c.md`
- Transcription model: faster-whisper `small` (local CPU, int8)

## Verdict: FAIL

- Spoken-word check: PASS (spoken fraction 1.2%, longest suspect range 2.0s)
- Lyric-fidelity check: FAIL (overall WER 13.6%, 0 missing / 3 altered / 18 transcriber-uncertain lines, 0 repeat finding(s))

## Spoken-Word Screen

- **Spoken-fraction estimate (of full track): 1.2%**
- Longest single suspect range: 2.0s
- Melodicity threshold used: **0.40** (calibrated on packet-a-memorized.mp3; see screen-packet-a-memorized.md)

### Suspect time ranges

| Range | Duration | Mean melodicity |
|---|---|---|
| 03:58–04:00 | 2.0s | 0.32 |
| 04:17–04:19 | 2.0s | 0.15 |

## Lyric-Fidelity Check

- Overall word-error estimate: **13.6%** (428 reference words)
- Per-line noise threshold (transcriber-uncertainty ceiling): **0.70** (calibrated on packet-a-memorized.mp3)
- Lines: 52 total, 0 missing, 3 altered, 18 transcriber-uncertain (passing), rest exact.

### Missing / altered lines (structural)

| # | Status | Expected | Heard |
|---|---|---|---|
| 1 | ALTERED (wer=1.00) | Packet See | pachycee |
| 15 | ALTERED (wer=1.00) | Isaiah forty-one ten. | i say of |
| 16 | ALTERED (wer=1.00) | Philippians four thirteen. | 4110 philippians 413 |

### Transcriber-uncertain lines (passing; ASR noise only)

| # | wer | Expected | Heard |
|---|---|---|---|
| 13 | 0.33 | Isaiah forty-one ten. | of 41 10 |
| 14 | 0.05 | Fear thou not; for I am with thee: be not dismayed; for I am thy God: I will strengthen... | fear thou not for i am with thee be not dismayed for i am... |
| 17 | 0.20 | I can do all things through Christ which strengtheneth me. | we can do all things through christ which at me |
| 22 | 0.04 | It is of the LORD’s mercies that we are not consumed, because his compassions fail not.... | it is of the lord s mercies that we are not consumed beca... |
| 25 | 0.05 | God is not a man, that he should lie; neither the son of man, that he should repent: ha... | god is not ay man that he should lie neither the son of m... |
| 26 | 0.67 | Numbers twenty-three nineteen. | numbers 2319 |
| 29 | 0.67 | Isaiah twenty-six three. | isaiah 263 |
| 30 | 0.39 | Thou wilt keep him in perfect peace, whose mind is stayed on thee: because he trusteth ... | i will keep him in perfect peace s mine to stay on thee b... |
| 33 | 0.09 | Casting all your care upon him; for he careth for you. | casting all your care upon him for he careeth for you |
| 38 | 0.04 | He that spared not his own Son, but delivered him up for us all, how shall he not with ... | he that spared not his own son but delivered him up for u... |
| 42 | 0.67 | Philippians four nineteen. | philippians 419 |
| 45 | 0.67 | Hebrews two eighteen. | bruised to 18 |
| 46 | 0.11 | For in that he himself hath suffered being tempted, he is able to succour them that are... | for in that he himself has suffered being tempted he is a... |
| 47 | 0.67 | Hebrews two eighteen. | bruised to 18 |
| 48 | 0.33 | Psalm one nineteen nine and eleven. | psalm 119 9 and 11 |
| 49 | 0.10 | Wherewithal shall a young man cleanse his way? by taking heed thereto according to thy ... | all shall ay young man cleanse his way by taking heed the... |
| 50 | 0.50 | Psalm one nineteen nine and eleven. | psalm 199 and 11 |
| 51 | 0.50 | Packet See | can see |

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
