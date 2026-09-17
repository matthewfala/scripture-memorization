# Song Screen: packet-b-take2-vocals

- Source file: `/Users/fala/Music/scripture-memorization/navigators/songs/stems/packet-b-take2-vocals.mp3`
- Duration: 04:08 (247.6s)
- Expected lyrics source: `navigators/lyrics/packet-b.md`
- Transcription model: faster-whisper `medium` (local CPU, int8)

## Verdict: FAIL

- Spoken-word check: PASS (spoken fraction 7.3%, longest suspect range 3.0s)
- Lyric-fidelity check: FAIL (overall WER 18.0%, 1 missing / 7 altered / 18 transcriber-uncertain lines, 0 repeat finding(s))

## Spoken-Word Screen

- **Spoken-fraction estimate (of full track): 7.3%**
- Longest single suspect range: 3.0s
- Melodicity threshold used: **0.65** (calibrated on packet-a-memorized.mp3; see screen-packet-a-memorized.md)

### Suspect time ranges

| Range | Duration | Mean melodicity |
|---|---|---|
| 00:15–00:18 | 3.0s | 0.51 |
| 01:09–01:12 | 3.0s | 0.64 |
| 01:29–01:32 | 3.0s | 0.55 |
| 03:07–03:10 | 3.0s | 0.50 |
| 03:26–03:29 | 3.0s | 0.48 |
| 03:52–03:55 | 3.0s | 0.55 |

## Lyric-Fidelity Check

- Overall word-error estimate: **18.0%** (449 reference words)
- Per-line noise threshold (transcriber-uncertainty ceiling): **0.70** (calibrated on packet-a-memorized.mp3)
- Lines: 52 total, 1 missing, 7 altered, 18 transcriber-uncertain (passing), rest exact.

### Missing / altered lines (structural)

| # | Status | Expected | Heard |
|---|---|---|---|
| 1 | ALTERED (wer=1.00) | Packet Bee | could be |
| 12 | ALTERED (wer=0.80) | Bee Three and Bee Four | be free and |
| 13 | ALTERED (wer=1.00) | Romans six twenty-three. | be for romance |
| 27 | ALTERED (wer=0.75) | Salvation Not By Works | salvation |
| 28 | MISSING (wer=1.00) | Bee Seven and Bee Eight | (nothing) |
| 29 | ALTERED (wer=0.80) | Ephesians two eight to nine. | ephesians |
| 36 | ALTERED (wer=0.80) | Bee Nine and Bee Ten | benign and beaten |
| 51 | ALTERED (wer=1.00) | Packet Bee | it beat |

### Transcriber-uncertain lines (passing; ASR noise only)

| # | wer | Expected | Heard |
|---|---|---|---|
| 9 | 0.11 | All we like sheep have gone astray; we have turned every one to his own way; and the LO... | all we like sheep have gone astray we have turned everyon... |
| 14 | 0.10 | For the wages of sin is death; but the gift of God is eternal life through Jesus Christ... | for the wages of sin is death but the gift of god is eter... |
| 15 | 0.33 | Romans six twenty-three. | roman 6 23 |
| 17 | 0.07 | And as it is appointed unto men once to die, but after this the judgment: | and as it is appointed unto men wants to die but after th... |
| 20 | 0.40 | Bee Five and Bee Six | and bee 6 |
| 22 | 0.06 | But God commendeth his love toward us, in that, while we were yet sinners, Christ died ... | but god commended his love toward us in that while we wer... |
| 26 | 0.50 | First Peter three eighteen. | 1 peter 318 |
| 30 | 0.44 | For by grace are ye saved through faith; and that not of yourselves: it is the gift of ... | 2a tonight and that night of yourselves it is the gift of... |
| 31 | 0.40 | Ephesians two eight to nine. | ephesians 2 8 tonight |
| 38 | 0.04 | But as many as received him, to them gave he power to become the sons of God, even to t... | but as many as received to them gave he power to become t... |
| 39 | 0.67 | John one twelve. | john 112 |
| 40 | 0.67 | Revelation three twenty. | revelation 320 |
| 42 | 0.67 | Revelation three twenty. | revelation 320 |
| 44 | 0.40 | Bee Eleven and Bee Twelve | be 11 and be 12 |
| 46 | 0.10 | These things have I written unto you that believe on the name of the Son of God; that y... | these things have i written unto you that believe on the ... |
| 47 | 0.25 | First John five thirteen. | 1 john 5 |
| 48 | 0.33 | John five twenty-four. | john 5 5 |
| 49 | 0.15 | Verily, verily, I say unto you, He that heareth my word, and believeth on him that sent... | verily verily i say unto you and believeth on him that se... |

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
