# Song Screen: packet-b-take7-vocals

- Source file: `/Users/fala/Music/scripture-memorization/navigators/songs/stems/packet-b-take7-vocals.mp3`
- Duration: 04:31 (271.2s)
- Expected lyrics source: `navigators/lyrics/packet-b.md`
- Transcription model: faster-whisper `medium` (local CPU, int8)

## Verdict: FAIL

- Spoken-word check: PASS (spoken fraction 3.7%, longest suspect range 4.0s)
- Lyric-fidelity check: FAIL (overall WER 16.9%, 5 missing / 2 altered / 18 transcriber-uncertain lines, 0 repeat finding(s))

## Spoken-Word Screen

- **Spoken-fraction estimate (of full track): 3.7%**
- Longest single suspect range: 4.0s
- Melodicity threshold used: **0.65** (calibrated on packet-a-memorized.mp3; see screen-packet-a-memorized.md)

### Suspect time ranges

| Range | Duration | Mean melodicity |
|---|---|---|
| 00:21–00:25 | 4.0s | 0.48 |
| 01:08–01:11 | 3.0s | 0.64 |
| 03:31–03:34 | 3.0s | 0.45 |

## Lyric-Fidelity Check

- Overall word-error estimate: **16.9%** (449 reference words)
- Per-line noise threshold (transcriber-uncertainty ceiling): **0.70** (calibrated on packet-a-memorized.mp3)
- Lines: 52 total, 5 missing, 2 altered, 18 transcriber-uncertain (passing), rest exact.

### Missing / altered lines (structural)

| # | Status | Expected | Heard |
|---|---|---|---|
| 1 | ALTERED (wer=1.00) | Packet Bee | gonna be |
| 8 | MISSING (wer=1.00) | Isaiah fifty-three six. | (nothing) |
| 12 | MISSING (wer=1.00) | Bee Three and Bee Four | (nothing) |
| 20 | MISSING (wer=1.00) | Bee Five and Bee Six | (nothing) |
| 36 | MISSING (wer=1.00) | Bee Nine and Bee Ten | (nothing) |
| 39 | MISSING (wer=1.00) | John one twelve. | (nothing) |
| 51 | ALTERED (wer=1.00) | Packet Bee | it big |

### Transcriber-uncertain lines (passing; ASR noise only)

| # | wer | Expected | Heard |
|---|---|---|---|
| 3 | 0.67 | All Have Sinned | oh have seen |
| 4 | 0.40 | Bee One and Bee Two | be 1 and be 2 |
| 9 | 0.21 | All we like sheep have gone astray; we have turned every one to his own way; and the LO... | always like sheep have gone astray we have turned everyon... |
| 14 | 0.05 | For the wages of sin is death; but the gift of God is eternal life through Jesus Christ... | for the wage of sin is death but the gift of god is etern... |
| 17 | 0.07 | And as it is appointed unto men once to die, but after this the judgment: | and as it is appointed unto men wants to die but after th... |
| 22 | 0.17 | But God commendeth his love toward us, in that, while we were yet sinners, Christ died ... | but god commended his love toward us while we were yet si... |
| 24 | 0.25 | First Peter three eighteen. | 1 peter free 18 |
| 25 | 0.03 | For Christ also hath once suffered for sins, the just for the unjust, that he might bri... | for christ also had once suffered for sins the just for t... |
| 26 | 0.25 | First Peter three eighteen. | 1 up 3 18 |
| 28 | 0.20 | Bee Seven and Bee Eight | 3 7 and bee 8 |
| 30 | 0.11 | For by grace are ye saved through faith; and that not of yourselves: it is the gift of ... | for by grace are ye saved through faith and that not of y... |
| 31 | 0.20 | Ephesians two eight to nine. | ephesians 2 8 and 9 |
| 34 | 0.33 | Titus three five. | titus 3 |
| 40 | 0.67 | Revelation three twenty. | revelation 320 we |
| 41 | 0.21 | Behold, I stand at the door, and knock: if any man hear my voice, and open the door, I ... | hope i stand at the door and knock your finny man hear my... |
| 42 | 0.67 | Revelation three twenty. | revelation 320 |
| 47 | 0.25 | First John five thirteen. | s john 5 13 |
| 49 | 0.09 | Verily, verily, I say unto you, He that heareth my word, and believeth on him that sent... | verily i say unto you he that heareth my word and believe... |

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
