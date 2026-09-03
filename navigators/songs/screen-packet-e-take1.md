# Song Screen: packet-e-take1

- Source file: `/Users/fala/Music/scripture-memorization/navigators/songs/packet-e-take1.mp3`
- Duration: 06:07 (366.8s)
- Expected lyrics source: `/Users/fala/Music/scripture-memorization/navigators/lyrics/packet-e.md`
- Transcription model: faster-whisper `small` (local CPU, int8)

## Verdict: FAIL

- Spoken-word check: PASS (spoken fraction 0.0%, longest suspect range 0.0s)
- Lyric-fidelity check: FAIL (overall WER 18.6%, 4 missing / 3 altered / 19 transcriber-uncertain lines, 2 repeat finding(s))

## Spoken-Word Screen

- **Spoken-fraction estimate (of full track): 0.0%**
- Longest single suspect range: 0.0s
- Melodicity threshold used: **0.40** (calibrated on packet-a-memorized.mp3; see screen-packet-a-memorized.md)

### Suspect time ranges

None. No windows fell below the melodicity threshold.

## Lyric-Fidelity Check

- Overall word-error estimate: **18.6%** (488 reference words)
- Per-line noise threshold (transcriber-uncertainty ceiling): **0.70** (calibrated on packet-a-memorized.mp3)
- Lines: 52 total, 4 missing, 3 altered, 19 transcriber-uncertain (passing), rest exact.

### Missing / altered lines (structural)

| # | Status | Expected | Heard |
|---|---|---|---|
| 1 | ALTERED (wer=1.00) | Packet Ee | the 3 |
| 4 | ALTERED (wer=0.80) | Ee One and Ee Two | he won and he too |
| 28 | MISSING (wer=1.00) | Ee Seven and Ee Eight | (nothing) |
| 29 | MISSING (wer=1.00) | Leviticus nineteen eleven. | (nothing) |
| 31 | MISSING (wer=1.00) | Leviticus nineteen eleven. | (nothing) |
| 32 | MISSING (wer=1.00) | Acts twenty-four sixteen. | (nothing) |
| 51 | ALTERED (wer=1.00) | Packet Ee | father which |

### Transcriber-uncertain lines (passing; ASR noise only)

| # | wer | Expected | Heard |
|---|---|---|---|
| 2 | 0.67 | Grow in Christlikeness | hero in christliness |
| 6 | 0.12 | A new commandment I give unto you, That ye love one another; as I have loved you, that ... | ay new commandment i give unto you that he love 1 another... |
| 7 | 0.20 | John thirteen thirty-four to thirty-five. | john 13 4 to 35 |
| 9 | 0.11 | My little children, let us not love in word, neither in tongue; but in deed and in truth. | my little children let us not love in word neither in ton... |
| 12 | 0.40 | Ee Three and Ee Four | he 3 and he 4 |
| 14 | 0.05 | Let nothing be done through strife or vainglory; but in lowliness of mind let each este... | let nothing be done through strife of englory but in lowl... |
| 15 | 0.20 | Philippians two three to four. | philippians 2 3 2 4 |
| 16 | 0.17 | First Peter five five to six. | 1 peter 5 5 2 6 |
| 17 | 0.08 | Likewise, ye younger, submit yourselves unto the elder. Yea, all of you be subject one ... | wise the younger submit yourselves unto the elder yeah al... |
| 18 | 0.17 | First Peter five five to six. | 1 peter 5 5 2 6 |
| 20 | 0.40 | Ee Five and Ee Six | in 5 and in 6 |
| 22 | 0.06 | But fornication, and all uncleanness, or covetousness, let it not be once named among y... | but fornication and all uncleanness or covetousness let i... |
| 30 | 0.08 | Ye shall not steal, neither deal falsely, neither lie one to another. | he shall not steal neither deal falsely neither lie 1 to ... |
| 33 | 0.05 | And herein do I exercise myself, to have always a conscience void of offence toward God... | and herein do i exercise myself to have always ay conscie... |
| 38 | 0.03 | But without faith it is impossible to please him: for he that cometh to God must believ... | but without faith it is impossible to please him for he t... |
| 39 | 0.33 | Hebrews eleven six. | bruised 11 6 |
| 42 | 0.20 | Romans four twenty to twenty-one. | romans 4 20 2 21 |
| 46 | 0.02 | And let us not be weary in well doing: for in due season we shall reap, if we faint not... | and let us not be weary in both doing for in due season w... |
| 52 | 0.67 | Grow in Christlikeness | is in ness |

### Repeated-beyond-format findings

| Text | Expected count | Observed count |
|---|---|---|
| Good Works | 1 | 2 |
| Matthew five sixteen. | 2 | 3 |

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

Round-1 lyric-fidelity used faster-whisper `small`. Choral reverb ("sacred
choral hymn... reverberant 1960s cathedral recording") was suspected to
degrade that model specifically, so the round-1 MISSING and repeat findings
were re-checked against a full-track re-transcription with faster-whisper
`medium` (still local CPU, int8; model weights downloaded once from
Hugging Face and cached — no cloud inference). Transcript saved at
`packet_e_take1_medium_segments.json` in the scratch directory.

| Finding (round 1) | Verdict | Evidence |
|---|---|---|
| Lines 28–32 MISSING: "Ee Seven and Ee Eight" / Leviticus 19:11 sandwich / Acts 24:16 sandwich (the "Honesty" topic) | **ASR_MISS** | Medium-model transcript, `[185.3–223.3]`: *"Honesty." / "E7 and E8, Leviticus 1911. Ye shall not steal, neither deal falsely, neither lie one to another." / "Leviticus 1911, Acts 24, 16. And herein do I exercise myself," / "To have always a conscience void of offence toward God and toward men, Acts 24, 16."* — the full topic (designator, both reference sandwiches, both verses) is present almost verbatim, modulo the usual designator/number-format ASR quirks ("E7"/"E8" for "Ee Seven"/"Ee Eight", "1911" for "nineteen eleven"). The `small` model simply failed to transcribe this passage; the content is there. |
| "Good Works" repeated-beyond-format (expected 1x, observed 2x) | **ASR/algorithm artifact, not a distinct real repeat** | The topic title "Good Works" genuinely appears once, at `[272.2–287.7]`: *"...Good works, E, 11 and E, 12, Galatians 6, 9 to 10..."*. The apparent second occurrence is explained by the confirmed Matthew 5:16 repeat below — that verse's own KJV text contains the phrase "...that they may see your **good works**..." (heard again at `[338.3–347.8]`), a coincidental substring inside a different line's genuine repeat, not a second recitation of the topic-title line itself. |
| "Matthew five sixteen." repeated-beyond-format (expected 2x, observed 3x) | **REAL** — and more extensive than the single flagged line | Medium transcript shows the expected sandwich completing normally: `[304.8–331.4]` *"Galatians 6, 9 to 10, Matthew 5, 16. Let your light so shine before men," ... "That they may see your good works, and glorify your Father, which is in heaven." ... "Matthew 5, 16. Pack it in." "Growing Christ's sixthness."* (this last pair is almost certainly the closing "Packet Ee" / "Grow in Christlikeness" bookend, badly garbled). Then, instead of ending, the **entire final verse, its reference, and the closing bookend play through a second time**: `[334.8–357.8]` *"Let your light so shine before men." "That they may see your good works, and glorify your Father, which is in heaven." "Matthew 5, 16" "Pagody"* (garbled "Packet Ee" again) — before the track finally closes at `[357.8–363.3]` with a clean *"Grow in Christlikeness."* So the take appears to repeat roughly its last ~30 seconds (final verse + reference + closing title bookend) in full, not just the one reference line the automated check happened to catch cleanly. |

**Answer to the specific question asked:** the Honesty block is *not* actually missing in take1 (see above — it's an ASR miss by the small model). Separately, take2's medium-model transcript (see `screen-packet-e-take2.md` addendum) also confirms its own Honesty block is fully present, and additionally confirms take2's ending plays through only once (no repeat) — unlike take1's confirmed final-section repeat.

**Updated assessment:** packet-e-take1's real, confirmed defect is the outro repeating in full (an extra ~30s of duplicated singing), which does constitute genuine "repeated beyond format" content per the procedure's Purpose statement, not a false positive. This is a real, if minor-in-substance, structural issue — the repeated material is exactly correct text, just sung twice — and is much more substantial than take2's confirmed issue (a single word, "Purity," said twice in a row; see the take2 addendum). If choosing between the two E takes without regenerating, **take2 is the safer pick**: its only confirmed defect is far smaller, and its ending is clean. Regeneration remains a reasonable option if the human wants an outro without any duplication at all, but it is not mandatory — both confirmed issues are minor relative to a fully dropped or altered verse.

## Human Prompts

#### Initial Document Written On 2026-09-02

- Generated automatically by `screen_song.py` per `navigators/procedures/04-spoken-word-screen.md` (spoken-word + lyric-fidelity screening pass).

#### Document Modification On 2026-09-02

- Coordinator follow-up: re-verify the round-1 "Honesty" MISSING block and the "Good Works" / "Matthew five sixteen." repeat findings with faster-whisper `medium` (stronger model, since choral reverb was suspected to degrade `small`'s accuracy), report REAL / ASR_MISS / UNCLEAR per finding with transcript excerpts and timestamps, and state whether take2 has all its content confirmed present so it could be the safe official pick without regeneration.
