# Song Screen: packet-b-take3-vocals

- Source file: `/Users/fala/Music/scripture-memorization/navigators/songs/stems/packet-b-take3-vocals.mp3`
- Duration: 04:28 (267.8s)
- Expected lyrics source: `navigators/lyrics/packet-b.md`
- Transcription model: faster-whisper `medium` (local CPU, int8)

## Verdict: FAIL

- Spoken-word check: PASS (spoken fraction 5.2%, longest suspect range 4.0s)
- Lyric-fidelity check: FAIL (overall WER 8.7%, 0 missing / 2 altered / 18 transcriber-uncertain lines, 0 repeat finding(s))

## Spoken-Word Screen

- **Spoken-fraction estimate (of full track): 5.2%**
- Longest single suspect range: 4.0s
- Melodicity threshold used: **0.65** (calibrated on packet-a-memorized.mp3; see screen-packet-a-memorized.md)

### Suspect time ranges

| Range | Duration | Mean melodicity |
|---|---|---|
| 00:20–00:24 | 4.0s | 0.54 |
| 00:36–00:40 | 4.0s | 0.60 |
| 01:32–01:35 | 3.0s | 0.64 |
| 03:30–03:33 | 3.0s | 0.57 |

## Lyric-Fidelity Check

- Overall word-error estimate: **8.7%** (449 reference words)
- Per-line noise threshold (transcriber-uncertainty ceiling): **0.70** (calibrated on packet-a-memorized.mp3)
- Lines: 52 total, 0 missing, 2 altered, 18 transcriber-uncertain (passing), rest exact.

### Missing / altered lines (structural)

| # | Status | Expected | Heard |
|---|---|---|---|
| 1 | ALTERED (wer=1.00) | Packet Bee | t be |
| 51 | ALTERED (wer=1.00) | Packet Bee | could do |

### Transcriber-uncertain lines (passing; ASR noise only)

| # | wer | Expected | Heard |
|---|---|---|---|
| 2 | 0.50 | Proclaim Christ | proclaiming christ |
| 6 | 0.08 | For all have sinned, and come short of the glory of God; | all have sinned and come short of the glory of god |
| 7 | 0.33 | Romans three twenty-three. | romans 3 |
| 8 | 0.67 | Isaiah fifty-three six. | isaiah |
| 9 | 0.11 | All we like sheep have gone astray; we have turned every one to his own way; and the LO... | all we like sheep have gone astray we have turned everyon... |
| 10 | 0.33 | Isaiah fifty-three six. | isaiah 53 |
| 12 | 0.40 | Bee Three and Bee Four | be 3 and be 4 |
| 22 | 0.06 | But God commendeth his love toward us, in that, while we were yet sinners, Christ died ... | but god commended his love toward us in that while we wer... |
| 23 | 0.33 | Romans five eight. | romans 5 |
| 27 | 0.25 | Salvation Not By Works | salvation not by work |
| 30 | 0.07 | For by grace are ye saved through faith; and that not of yourselves: it is the gift of ... | for by grace are ye saved through faith and that not of y... |
| 33 | 0.11 | Not by works of righteousness which we have done, but according to his mercy he saved u... | have by works of righteousness which be of done but accor... |
| 34 | 0.33 | Titus three five. | us 3 5 |
| 36 | 0.40 | Bee Nine and Bee Ten | be 9 and be 10 |
| 40 | 0.67 | Revelation three twenty. | revelation 320 |
| 41 | 0.06 | Behold, I stand at the door, and knock: if any man hear my voice, and open the door, I ... | behold i stand at the door and knock if any man hear my v... |
| 46 | 0.03 | These things have I written unto you that believe on the name of the Son of God; that y... | beast things have i written unto you that believe on the ... |
| 52 | 0.50 | Proclaim Christ | proclaim you |

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
