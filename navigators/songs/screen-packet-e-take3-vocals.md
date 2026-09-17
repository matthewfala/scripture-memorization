# Song Screen: packet-e-take3-vocals

- Source file: `/Users/fala/Music/scripture-memorization/navigators/songs/stems/packet-e-take3-vocals.mp3`
- Duration: 04:59 (299.1s)
- Expected lyrics source: `navigators/lyrics/packet-e.md`
- Transcription model: faster-whisper `medium` (local CPU, int8)

## Verdict: FAIL

- Spoken-word check: PASS (spoken fraction 1.0%, longest suspect range 3.0s)
- Lyric-fidelity check: FAIL (overall WER 13.7%, 6 missing / 3 altered / 9 transcriber-uncertain lines, 0 repeat finding(s))

## Spoken-Word Screen

- **Spoken-fraction estimate (of full track): 1.0%**
- Longest single suspect range: 3.0s
- Melodicity threshold used: **0.65** (calibrated on packet-a-memorized.mp3; see screen-packet-a-memorized.md)

### Suspect time ranges

| Range | Duration | Mean melodicity |
|---|---|---|
| 01:47–01:50 | 3.0s | 0.63 |

## Lyric-Fidelity Check

- Overall word-error estimate: **13.7%** (488 reference words)
- Per-line noise threshold (transcriber-uncertainty ceiling): **0.70** (calibrated on packet-a-memorized.mp3)
- Lines: 52 total, 6 missing, 3 altered, 9 transcriber-uncertain (passing), rest exact.

### Missing / altered lines (structural)

| # | Status | Expected | Heard |
|---|---|---|---|
| 1 | MISSING (wer=1.00) | Packet Ee | (nothing) |
| 2 | MISSING (wer=1.00) | Grow in Christlikeness | (nothing) |
| 26 | MISSING (wer=1.00) | First Peter two eleven. | (nothing) |
| 27 | MISSING (wer=1.00) | Honesty | (nothing) |
| 28 | ALTERED (wer=1.00) | Ee Seven and Ee Eight | honest deeds |
| 31 | MISSING (wer=1.00) | Leviticus nineteen eleven. | (nothing) |
| 44 | MISSING (wer=1.00) | Ee Eleven and Ee Twelve | (nothing) |
| 51 | ALTERED (wer=1.00) | Packet Ee | packagey |
| 52 | ALTERED (wer=1.00) | Grow in Christlikeness | growing chris likeness |

### Transcriber-uncertain lines (passing; ASR noise only)

| # | wer | Expected | Heard |
|---|---|---|---|
| 6 | 0.02 | A new commandment I give unto you, That ye love one another; as I have loved you, that ... | ay new commandment i give unto you that ye love 1 another... |
| 14 | 0.05 | Let nothing be done through strife or vainglory; but in lowliness of mind let each este... | let nothing be done through strife or glory but in lowlin... |
| 17 | 0.16 | Likewise, ye younger, submit yourselves unto the elder. Yea, all of you be subject one ... | wise beyond the submit yourselves unto the elder yea all ... |
| 20 | 0.60 | Ee Five and Ee Six | 5 and |
| 22 | 0.44 | But fornication, and all uncleanness, or covetousness, let it not be once named among y... | and all unclannished let it not be once named among you |
| 25 | 0.11 | Dearly beloved, I beseech you as strangers and pilgrims, abstain from fleshly lusts, wh... | i beseech you as strangers and pilgrims abstain from fles... |
| 30 | 0.33 | Ye shall not steal, neither deal falsely, neither lie one to another. | neither deal falsely neither lie 1 to another |
| 33 | 0.11 | And herein do I exercise myself, to have always a conscience void of offence toward God... | and in do i exercise myself to have always ay conscience ... |
| 42 | 0.60 | Romans four twenty to twenty-one. | romans 4 |

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
