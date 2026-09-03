# Song Screen: packet-e-take4

- Source file: `/Users/fala/Music/scripture-memorization/navigators/songs/packet-e-take4.mp3`
- Duration: 05:12 (312.2s)
- Expected lyrics source: `/Users/fala/Music/scripture-memorization/navigators/lyrics/packet-e.md`
- Transcription model: faster-whisper `small` (local CPU, int8)

## Verdict: FAIL

- Spoken-word check: PASS (spoken fraction 0.0%, longest suspect range 0.0s)
- Lyric-fidelity check: FAIL (overall WER 10.2%, 0 missing / 4 altered / 19 transcriber-uncertain lines, 0 repeat finding(s))

## Spoken-Word Screen

- **Spoken-fraction estimate (of full track): 0.0%**
- Longest single suspect range: 0.0s
- Melodicity threshold used: **0.40** (calibrated on packet-a-memorized.mp3; see screen-packet-a-memorized.md)

### Suspect time ranges

None. No windows fell below the melodicity threshold.

## Lyric-Fidelity Check

- Overall word-error estimate: **10.2%** (488 reference words)
- Per-line noise threshold (transcriber-uncertainty ceiling): **0.70** (calibrated on packet-a-memorized.mp3)
- Lines: 52 total, 0 missing, 4 altered, 19 transcriber-uncertain (passing), rest exact.

### Missing / altered lines (structural)

| # | Status | Expected | Heard |
|---|---|---|---|
| 1 | ALTERED (wer=1.00) | Packet Ee | can he |
| 27 | ALTERED (wer=1.00) | Honesty | ee |
| 51 | ALTERED (wer=1.00) | Packet Ee | pachytee |
| 52 | ALTERED (wer=1.00) | Grow in Christlikeness | growing chris likeness |

### Transcriber-uncertain lines (passing; ASR noise only)

| # | wer | Expected | Heard |
|---|---|---|---|
| 2 | 0.33 | Grow in Christlikeness | grow in christmas |
| 6 | 0.02 | A new commandment I give unto you, That ye love one another; as I have loved you, that ... | ay new commandment i give unto you that ye love 1 another... |
| 7 | 0.40 | John thirteen thirty-four to thirty-five. | john 13 34 235 |
| 10 | 0.25 | First John three eighteen. | 1 john 3 t |
| 13 | 0.20 | Philippians two three to four. | philippians 2 3 2 4 |
| 14 | 0.03 | Let nothing be done through strife or vainglory; but in lowliness of mind let each este... | let nothing be done through strife or glory but in lowlin... |
| 15 | 0.20 | Philippians two three to four. | philippians 2 3 2 4 |
| 17 | 0.02 | Likewise, ye younger, submit yourselves unto the elder. Yea, all of you be subject one ... | likewise ye younger submit yourselves unto the elder yey ... |
| 18 | 0.17 | First Peter five five to six. | 1 peter 5 5 2 6 |
| 20 | 0.40 | Ee Five and Ee Six | eve 5 and eve 6 |
| 22 | 0.06 | But fornication, and all uncleanness, or covetousness, let it not be once named among y... | but fornication and all uncleanness or covetousness let i... |
| 26 | 0.50 | First Peter two eleven. | 1 peter 211 honesty |
| 29 | 0.67 | Leviticus nineteen eleven. | leviticus 1911 |
| 30 | 0.17 | Ye shall not steal, neither deal falsely, neither lie one to another. | ye shall not steal the deal falls neither lie 1 to another |
| 31 | 0.67 | Leviticus nineteen eleven. | leviticus 1911 |
| 36 | 0.20 | Ee Nine and Ee Ten | ay 9 and ee 10 |
| 44 | 0.20 | Ee Eleven and Ee Twelve | 11 and ee 12 |
| 46 | 0.19 | And let us not be weary in well doing: for in due season we shall reap, if we faint not... | and let us not be weary we shall reap if we faint not as ... |
| 49 | 0.09 | Let your light so shine before men, that they may see your good works, and glorify your... | that your lights so shine before men that they may see yo... |

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

## Verification Addendum (medium-model re-check, 2026-09-02)

This is Packet E round 2 (take3, take4 — same lyrics and style as round 1,
byte-verified before generation). Every structural finding below was
independently re-checked with a full-track faster-whisper `medium`
re-transcription (local CPU, int8; no cloud inference) before being allowed
to stand. Transcript saved at `packet_e_take4_medium_segments.json` in the
scratch directory. Re-running the alignment against the medium transcript
(same 0.70 threshold) drops overall WER from 10.2% (small) to 5.1%
(medium), with 0 missing and 0 repeats; two lines remain flagged.

| Finding (round-2, small model) | Verdict | Evidence |
|---|---|---|
| Line 27 "Honesty" (topic title) ALTERED, heard "ee" | **ASR_MISS** | Medium transcript `[170.4–173.8]`: *"Honesty E, E7 and E8"* — "Honesty" is clearly and correctly transcribed by the medium model, immediately before the designator. |
| Line 51 "Packet Ee" (closing) ALTERED, heard "pachytee" | **ASR_MISS** | Final medium segment `[301.2–309.2]`: *"Packety, grow in Chrislikeness"* — a recognizable phonetic rendering of "Packet Ee, Grow in Christlikeness." Same fade-out difficulty seen on every other take, including the Packet A calibration reference. |
| Line 52 "Grow in Christlikeness" (closing) ALTERED, heard "growing chris likeness" | **ASR_MISS** | Same final segment as above — "grow in Chrislikeness" is phonetically accurate; the WER=1.00 on the small model's version was a token-boundary artifact ("growing" vs "grow"+"in"), not missing or altered content. |
| Line 1 "Packet Ee" (opening) ALTERED, heard "can he" | **UNCLEAR — not resolved to ASR_MISS** | Medium transcript `[0.0–10.0]`: *"How can ye grow in Christ's likeness, love?"* Unlike every other flagged line in rounds 1–2, this is not a garbled-but-recognizable phonetic near-miss of "Packet Ee" — both the small model ("can he") and the medium model ("How can ye...") independently produced a different, fluently-formed phrase in place of the expected "Packet Ee" title line, with "grow in Christ's likeness" (≈"Grow in Christlikeness," the second bookend line) following immediately after. This could still be an ASR artifact (a coherent-sounding hallucination filling in an unclear reverb-heavy passage), but it could also mean the opening title recitation was genuinely reworded/dropped in this take. Two independent model sizes failing to recover anything resembling "Packet Ee" — rather than a recognizable garbled variant, as seen everywhere else — is the one piece of evidence in this whole screening pass that does not cleanly resolve on transcription alone. **Recommend a direct human listen to the first ~10 seconds of packet-e-take4.mp3** to settle this. |

**Updated assessment:** packet-e-take4 has no confirmed missing, altered
(beyond the one unresolved opening line), or repeated content — three of
four round-2 findings resolve cleanly to the same bookend transcription
noise seen throughout this project. The opening line remains genuinely
uncertain rather than confidently dismissed, per the instruction not to
leave ASR_MISS-shaped findings unverified.

## Human Prompts

#### Initial Document Written On 2026-09-02

- Generated automatically by `screen_song.py` per `navigators/procedures/04-spoken-word-screen.md` (spoken-word + lyric-fidelity screening pass).

#### Document Modification On 2026-09-02

- Coordinator follow-up: Packet E round 2 (take3, take4) generated with byte-verified identical lyrics/style. Run both checks on take3 and take4, and — given what was learned about small-model noise on this choral style — verify every structural finding (missing/repeated/reordered) directly with the medium model before letting it stand, rather than assuming ASR miss. Report REAL/ASR_MISS/UNCLEAR per finding with excerpts and timestamps, then recommend a final Packet E official take among take2, take3, and take4 (best lyric fidelity wins, tie-break lower spoken fraction), noting this is the last round.
