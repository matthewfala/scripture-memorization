# Song Screen: packet-d-take5-vocals

- Source file: `/Users/fala/Music/scripture-memorization/navigators/songs/stems/packet-d-take5-vocals.mp3`
- Duration: 04:32 (272.0s)
- Expected lyrics source: `navigators/lyrics/packet-d.md`
- Transcription model: faster-whisper `medium` (local CPU, int8)

## Verdict: FAIL

- Spoken-word check: PASS (spoken fraction 1.1%, longest suspect range 3.0s)
- Lyric-fidelity check: FAIL (overall WER 9.3%, 3 missing / 1 altered / 13 transcriber-uncertain lines, 0 repeat finding(s))

## Spoken-Word Screen

- **Spoken-fraction estimate (of full track): 1.1%**
- Longest single suspect range: 3.0s
- Melodicity threshold used: **0.65** (calibrated on packet-a-memorized.mp3; see screen-packet-a-memorized.md)

### Suspect time ranges

| Range | Duration | Mean melodicity |
|---|---|---|
| 02:16–02:19 | 3.0s | 0.52 |

## Lyric-Fidelity Check

- Overall word-error estimate: **9.3%** (548 reference words)
- Per-line noise threshold (transcriber-uncertainty ceiling): **0.70** (calibrated on packet-a-memorized.mp3)
- Lines: 52 total, 3 missing, 1 altered, 13 transcriber-uncertain (passing), rest exact.

### Missing / altered lines (structural)

| # | Status | Expected | Heard |
|---|---|---|---|
| 1 | MISSING (wer=1.00) | Packet Dee | (nothing) |
| 2 | MISSING (wer=1.00) | Be Christ's Disciples | (nothing) |
| 44 | MISSING (wer=1.00) | Dee Eleven and Dee Twelve | (nothing) |
| 51 | ALTERED (wer=1.00) | Packet Dee | t be |

### Transcriber-uncertain lines (passing; ASR noise only)

| # | wer | Expected | Heard |
|---|---|---|---|
| 14 | 0.02 | Love not the world, neither the things that are in the world. If any man love the world... | love not the world neither the things that are in the wor... |
| 17 | 0.03 | And be not conformed to this world: but be ye transformed by the renewing of your mind,... | and be not conformed unto this world but be ye transforme... |
| 22 | 0.23 | Therefore, my beloved brethren, be ye stedfast, unmoveable, always abounding in the wor... | therefore my beloved brethren be steadfast unmovable alwa... |
| 25 | 0.20 | For consider him that endured such contradiction of sinners against himself, lest ye be... | for consider him that endured such contradiction of sinne... |
| 33 | 0.06 | For we preach not ourselves, but Christ Jesus the Lord; and ourselves your servants for... | for we preach not ourselves but christ jesus the lord and... |
| 38 | 0.13 | Honour the LORD with thy substance, and with the firstfruits of all thine increase: So ... | honor the lord with thy substance and with the fruits of ... |
| 41 | 0.09 | But this I say, He which soweth sparingly shall reap also sparingly; and he which sowet... | but this i say he which soweth sparingly shall reap also ... |
| 45 | 0.67 | Acts one eight. | acts 1a |
| 46 | 0.05 | But ye shall receive power, after that the Holy Ghost is come upon you: and ye shall be... | but ye shall receive power after that the holy ghost has ... |
| 47 | 0.67 | Acts one eight. | acts 1a |
| 49 | 0.04 | Go ye therefore, and teach all nations, baptizing them in the name of the Father, and o... | go ye therefore and teach all nations baptizing them in t... |
| 50 | 0.40 | Matthew twenty-eight nineteen to twenty. | matthew 28 19 i can |
| 52 | 0.25 | Be Christ's Disciples | be christ s disciple |

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
