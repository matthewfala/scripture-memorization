# Song Screen: packet-a-memorized

- Source file: `/Users/fala/Music/scripture-memorization/navigators/songs/packet-a-memorized.mp3`
- Duration: 05:22 (321.7s)
- Expected lyrics source: `/Users/fala/Music/scripture-memorization/navigators/procedures/03-lyrics-format.md (v1 Packet Ay example, Human Prompts)`
- Transcription model: faster-whisper `small` (local CPU, int8)

## Verdict: FAIL

- Spoken-word check: PASS (spoken fraction 0.6%, longest suspect range 2.0s)
- Lyric-fidelity check: FAIL (overall WER 5.3%, 0 missing / 1 altered / 14 transcriber-uncertain lines, 0 repeat finding(s))

## Spoken-Word Screen

- **Spoken-fraction estimate (of full track): 0.6%**
- Longest single suspect range: 2.0s
- Melodicity threshold used: **0.40** (calibrated on packet-a-memorized.mp3; see screen-packet-a-memorized.md)

### Suspect time ranges

| Range | Duration | Mean melodicity |
|---|---|---|
| 00:16–00:18 | 2.0s | 0.37 |

## Lyric-Fidelity Check

- Overall word-error estimate: **5.3%** (550 reference words)
- Per-line noise threshold (transcriber-uncertainty ceiling): **0.70** (calibrated on packet-a-memorized.mp3)
- Lines: 64 total, 0 missing, 1 altered, 14 transcriber-uncertain (passing), rest exact.

### Missing / altered lines (structural)

| # | Status | Expected | Heard |
|---|---|---|---|
| 61 | ALTERED (wer=1.00) | Witnessing | missing |

### Transcriber-uncertain lines (passing; ASR noise only)

| # | wer | Expected | Heard |
|---|---|---|---|
| 1 | 0.50 | Packet Ay | it ay |
| 9 | 0.05 | I am crucified with Christ: nevertheless I live; yet not I, but Christ liveth in me: an... | i am crucified with christ nevertheless i live yet not i ... |
| 17 | 0.33 | Romans twelve one. | romans 12 |
| 22 | 0.20 | Ay Three and Ay Four | ay 3 ay 4 |
| 36 | 0.12 | If ye abide in me, and my words abide in you, ye shall ask what ye will, and it shall b... | if he abideth me and my words abide in you ye shall ask w... |
| 38 | 0.20 | Philippians four six to seven. | philippians 4 6 7 |
| 39 | 0.05 | Be careful for nothing; but in every thing by prayer and supplication with thanksgiving... | be careful for nothing but in everything by prayer and su... |
| 45 | 0.67 | Matthew eighteen twenty. | matthew 1820 |
| 47 | 0.67 | Matthew eighteen twenty. | matthew 1820 |
| 48 | 0.40 | Hebrews ten twenty-four to twenty-five. | hebrews 1024 to 25 |
| 56 | 0.13 | And he saith unto them, Follow me, and I will make you fishers of men. | and ye say unto them follow me and i will make you fisher... |
| 59 | 0.06 | For I am not ashamed of the gospel of Christ: for it is the power of God unto salvation... | for i am not ashamed of the gospel of christ for it is th... |
| 62 | 0.40 | Ay Eleven and Ay Twelve | ay 11 day 12 |
| 63 | 0.50 | Packet Ay | pack ay |

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
