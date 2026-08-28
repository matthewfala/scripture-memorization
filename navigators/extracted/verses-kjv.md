# Verified KJV Verse Text

- Generated: 2026-08-27
- Sources: gutenberg 0204adaed1f2, sacred-texts 58144ba35f2d, aruljohn f45722adbce3
- Normalization applied:
  1. gutenberg: stripped each `<chapter>:<verse> ` verse-marker token, which can occur either at the start of a wrapped line or mid-line (short verses are not always given their own line); joined wrapped continuation lines with a single space; a run of 2+ blank lines (which precedes the next book's title heading, since the file has no per-chapter heading markup) was treated as the end of that book's verse text and everything after it discarded, so book titles never leak into the last verse of the preceding book.
  2. sacred-texts: stripped the leading `Code|chapter|verse|` pipe-delimited fields, the trailing `~` terminator, and the single leading space before the text.
  3. aruljohn: no source-specific markup was present in the `text` field (plain JSON string); used as-is.
  4. All three: collapsed any run of whitespace (including the newline joins from step 1) to a single space, then trimmed leading/trailing whitespace. Spelling, punctuation, and casing were left untouched so real differences surface.
  5. Multi-verse references (ranges `a-b`, lists `a,b`): each verse looked up and compared independently; when an entire reference agreed, its verses' texts were joined with a single space for the reader-facing quotation.

## Packet A — Live the New Life

### A1 — 2 Corinthians 5:17 — AGREE

Therefore if any man be in Christ, he is a new creature: old things are passed away; behold, all things are become new.

### A2 — Galatians 2:20 — FLAGGED

- v.20: [FLAGGED — see Discrepancies: A2 v.20]

### A3 — Romans 12:1 — AGREE

I beseech you therefore, brethren, by the mercies of God, that ye present your bodies a living sacrifice, holy, acceptable unto God, which is your reasonable service.

### A4 — John 14:21 — AGREE

He that hath my commandments, and keepeth them, he it is that loveth me: and he that loveth me shall be loved of my Father, and I will love him, and will manifest myself to him.

### A5 — 2 Timothy 3:16 — AGREE

All scripture is given by inspiration of God, and is profitable for doctrine, for reproof, for correction, for instruction in righteousness:

### A6 — Joshua 1:8 — AGREE

This book of the law shall not depart out of thy mouth; but thou shalt meditate therein day and night, that thou mayest observe to do according to all that is written therein: for then thou shalt make thy way prosperous, and then thou shalt have good success.

### A7 — John 15:7 — AGREE

If ye abide in me, and my words abide in you, ye shall ask what ye will, and it shall be done unto you.

### A8 — Philippians 4:6-7 — AGREE

Be careful for nothing; but in every thing by prayer and supplication with thanksgiving let your requests be made known unto God. And the peace of God, which passeth all understanding, shall keep your hearts and minds through Christ Jesus.

### A9 — Matthew 18:20 — AGREE

For where two or three are gathered together in my name, there am I in the midst of them.

### A10 — Hebrews 10:24-25 — AGREE

And let us consider one another to provoke unto love and to good works: Not forsaking the assembling of ourselves together, as the manner of some is; but exhorting one another: and so much the more, as ye see the day approaching.

### A11 — Matthew 4:19 — AGREE

And he saith unto them, Follow me, and I will make you fishers of men.

### A12 — Romans 1:16 — AGREE

For I am not ashamed of the gospel of Christ: for it is the power of God unto salvation to every one that believeth; to the Jew first, and also to the Greek.

## Packet B — Proclaim Christ

### B1 — Romans 3:23 — AGREE

For all have sinned, and come short of the glory of God;

### B2 — Isaiah 53:6 — AGREE

All we like sheep have gone astray; we have turned every one to his own way; and the LORD hath laid on him the iniquity of us all.

### B3 — Romans 6:23 — AGREE

For the wages of sin is death; but the gift of God is eternal life through Jesus Christ our Lord.

### B4 — Hebrews 9:27 — AGREE

And as it is appointed unto men once to die, but after this the judgment:

### B5 — Romans 5:8 — AGREE

But God commendeth his love toward us, in that, while we were yet sinners, Christ died for us.

### B6 — 1 Peter 3:18 — AGREE

For Christ also hath once suffered for sins, the just for the unjust, that he might bring us to God, being put to death in the flesh, but quickened by the Spirit:

### B7 — Ephesians 2:8-9 — AGREE

For by grace are ye saved through faith; and that not of yourselves: it is the gift of God: Not of works, lest any man should boast.

### B8 — Titus 3:5 — AGREE

Not by works of righteousness which we have done, but according to his mercy he saved us, by the washing of regeneration, and renewing of the Holy Ghost;

### B9 — John 1:12 — AGREE

But as many as received him, to them gave he power to become the sons of God, even to them that believe on his name:

### B10 — Revelation 3:20 — AGREE

Behold, I stand at the door, and knock: if any man hear my voice, and open the door, I will come in to him, and will sup with him, and he with me.

### B11 — 1 John 5:13 — AGREE

These things have I written unto you that believe on the name of the Son of God; that ye may know that ye have eternal life, and that ye may believe on the name of the Son of God.

### B12 — John 5:24 — AGREE

Verily, verily, I say unto you, He that heareth my word, and believeth on him that sent me, hath everlasting life, and shall not come into condemnation; but is passed from death unto life.

## Packet C — Rely on God's Resources

### C1 — 1 Corinthians 3:16 — AGREE

Know ye not that ye are the temple of God, and that the Spirit of God dwelleth in you?

### C2 — 1 Corinthians 2:12 — AGREE

Now we have received, not the spirit of the world, but the spirit which is of God; that we might know the things that are freely given to us of God.

### C3 — Isaiah 41:10 — AGREE

Fear thou not; for I am with thee: be not dismayed; for I am thy God: I will strengthen thee; yea, I will help thee; yea, I will uphold thee with the right hand of my righteousness.

### C4 — Philippians 4:13 — AGREE

I can do all things through Christ which strengtheneth me.

### C5 — Lamentations 3:22-23 — FLAGGED

- v.22: [FLAGGED — see Discrepancies: C5 v.22]
- v.23: They are new every morning: great is thy faithfulness.

### C6 — Numbers 23:19 — AGREE

God is not a man, that he should lie; neither the son of man, that he should repent: hath he said, and shall he not do it? or hath he spoken, and shall he not make it good?

### C7 — Isaiah 26:3 — AGREE

Thou wilt keep him in perfect peace, whose mind is stayed on thee: because he trusteth in thee.

### C8 — 1 Peter 5:7 — AGREE

Casting all your care upon him; for he careth for you.

### C9 — Romans 8:32 — AGREE

He that spared not his own Son, but delivered him up for us all, how shall he not with him also freely give us all things?

### C10 — Philippians 4:19 — AGREE

But my God shall supply all your need according to his riches in glory by Christ Jesus.

### C11 — Hebrews 2:18 — AGREE

For in that he himself hath suffered being tempted, he is able to succour them that are tempted.

### C12 — Psalm 119:9,11 — AGREE

Wherewithal shall a young man cleanse his way? by taking heed thereto according to thy word. Thy word have I hid in mine heart, that I might not sin against thee.

## Packet D — Be Christ's Disciples

### D1 — Matthew 6:33 — AGREE

But seek ye first the kingdom of God, and his righteousness; and all these things shall be added unto you.

### D2 — Luke 9:23 — AGREE

And he said to them all, If any man will come after me, let him deny himself, and take up his cross daily, and follow me.

### D3 — 1 John 2:15-16 — AGREE

Love not the world, neither the things that are in the world. If any man love the world, the love of the Father is not in him. For all that is in the world, the lust of the flesh, and the lust of the eyes, and the pride of life, is not of the Father, but is of the world.

### D4 — Romans 12:2 — AGREE

And be not conformed to this world: but be ye transformed by the renewing of your mind, that ye may prove what is that good, and acceptable, and perfect, will of God.

### D5 — 1 Corinthians 15:58 — AGREE

Therefore, my beloved brethren, be ye stedfast, unmoveable, always abounding in the work of the Lord, forasmuch as ye know that your labour is not in vain in the Lord.

### D6 — Hebrews 12:3 — AGREE

For consider him that endured such contradiction of sinners against himself, lest ye be wearied and faint in your minds.

### D7 — Mark 10:45 — AGREE

For even the Son of man came not to be ministered unto, but to minister, and to give his life a ransom for many.

### D8 — 2 Corinthians 4:5 — FLAGGED

- v.5: [FLAGGED — see Discrepancies: D8 v.5]

### D9 — Proverbs 3:9-10 — AGREE

Honour the LORD with thy substance, and with the firstfruits of all thine increase: So shall thy barns be filled with plenty, and thy presses shall burst out with new wine.

### D10 — 2 Corinthians 9:6-7 — AGREE

But this I say, He which soweth sparingly shall reap also sparingly; and he which soweth bountifully shall reap also bountifully. Every man according as he purposeth in his heart, so let him give; not grudgingly, or of necessity: for God loveth a cheerful giver.

### D11 — Acts 1:8 — AGREE

But ye shall receive power, after that the Holy Ghost is come upon you: and ye shall be witnesses unto me both in Jerusalem, and in all Judaea, and in Samaria, and unto the uttermost part of the earth.

### D12 — Matthew 28:19-20 — AGREE

Go ye therefore, and teach all nations, baptizing them in the name of the Father, and of the Son, and of the Holy Ghost: Teaching them to observe all things whatsoever I have commanded you: and, lo, I am with you alway, even unto the end of the world. Amen.

## Packet E — Grow in Christlikeness

### E1 — John 13:34-35 — AGREE

A new commandment I give unto you, That ye love one another; as I have loved you, that ye also love one another. By this shall all men know that ye are my disciples, if ye have love one to another.

### E2 — 1 John 3:18 — AGREE

My little children, let us not love in word, neither in tongue; but in deed and in truth.

### E3 — Philippians 2:3-4 — AGREE

Let nothing be done through strife or vainglory; but in lowliness of mind let each esteem other better than themselves. Look not every man on his own things, but every man also on the things of others.

### E4 — 1 Peter 5:5-6 — AGREE

Likewise, ye younger, submit yourselves unto the elder. Yea, all of you be subject one to another, and be clothed with humility: for God resisteth the proud, and giveth grace to the humble. Humble yourselves therefore under the mighty hand of God, that he may exalt you in due time:

### E5 — Ephesians 5:3 — AGREE

But fornication, and all uncleanness, or covetousness, let it not be once named among you, as becometh saints;

### E6 — 1 Peter 2:11 — AGREE

Dearly beloved, I beseech you as strangers and pilgrims, abstain from fleshly lusts, which war against the soul;

### E7 — Leviticus 19:11 — AGREE

Ye shall not steal, neither deal falsely, neither lie one to another.

### E8 — Acts 24:16 — FLAGGED

- v.16: [FLAGGED — see Discrepancies: E8 v.16]

### E9 — Hebrews 11:6 — AGREE

But without faith it is impossible to please him: for he that cometh to God must believe that he is, and that he is a rewarder of them that diligently seek him.

### E10 — Romans 4:20-21 — AGREE

He staggered not at the promise of God through unbelief; but was strong in faith, giving glory to God; And being fully persuaded that, what he had promised, he was able also to perform.

### E11 — Galatians 6:9-10 — AGREE

And let us not be weary in well doing: for in due season we shall reap, if we faint not. As we have therefore opportunity, let us do good unto all men, especially unto them who are of the household of faith.

### E12 — Matthew 5:16 — AGREE

Let your light so shine before men, that they may see your good works, and glorify your Father which is in heaven.

## Series 1 — Getting To Know God

### Jesus Christ (1-1 to 1-12)

#### 1-1 — John 1:1,14 — AGREE

In the beginning was the Word, and the Word was with God, and the Word was God. And the Word was made flesh, and dwelt among us, (and we beheld his glory, the glory as of the only begotten of the Father,) full of grace and truth.

#### 1-2 — Hebrews 1:8 — AGREE

But unto the Son he saith, Thy throne, O God, is for ever and ever: a sceptre of righteousness is the sceptre of thy kingdom.

#### 1-3 — Hebrews 4:15 — AGREE

For we have not an high priest which cannot be touched with the feeling of our infirmities; but was in all points tempted like as we are, yet without sin.

#### 1-4 — Luke 2:52 — AGREE

And Jesus increased in wisdom and stature, and in favour with God and man.

#### 1-5 — 1 Cor. 15:3-4 — AGREE

For I delivered unto you first of all that which I also received, how that Christ died for our sins according to the scriptures; And that he was buried, and that he rose again the third day according to the scriptures:

#### 1-6 — 1 Corinthians 15:20 — AGREE

But now is Christ risen from the dead, and become the firstfruits of them that slept.

#### 1-7 — John 1:18 — FLAGGED

- v.18: [FLAGGED — see Discrepancies: 1-7 v.18]

#### 1-8 — Hebrews 1:3 — FLAGGED

- v.3: [FLAGGED — see Discrepancies: 1-8 v.3]

#### 1-9 — Luke 19:10 — AGREE

For the Son of man is come to seek and to save that which was lost.

#### 1-10 — 1 Peter 1:18-19 — AGREE

Forasmuch as ye know that ye were not redeemed with corruptible things, as silver and gold, from your vain conversation received by tradition from your fathers; But with the precious blood of Christ, as of a lamb without blemish and without spot:

#### 1-11 — I Thessalonians 4:16-17 — AGREE

For the Lord himself shall descend from heaven with a shout, with the voice of the archangel, and with the trump of God: and the dead in Christ shall rise first: Then we which are alive and remain shall be caught up together with them in the clouds, to meet the Lord in the air: and so shall we ever be with the Lord.

#### 1-12 — 1 John 3:2-3 — AGREE

Beloved, now are we the sons of God, and it doth not yet appear what we shall be: but we know that, when he shall appear, we shall be like him; for we shall see him as he is. And every man that hath this hope in him purifieth himself, even as he is pure.

### Holy Spirit (1-13 to 1-24)

#### 1-13 — John 16:13-14 — AGREE

Howbeit when he, the Spirit of truth, is come, he will guide you into all truth: for he shall not speak of himself; but whatsoever he shall hear, that shall he speak: and he will shew you things to come. He shall glorify me: for he shall receive of mine, and shall shew it unto you.

#### 1-14 — 1 Corinthians 12:3 — AGREE

Wherefore I give you to understand, that no man speaking by the Spirit of God calleth Jesus accursed: and that no man can say that Jesus is the Lord, but by the Holy Ghost.

#### 1-15 — Romans 8:9 — AGREE

But ye are not in the flesh, but in the Spirit, if so be that the Spirit of God dwell in you. Now if any man have not the Spirit of Christ, he is none of his.

#### 1-16 — Galatians 4:6 — AGREE

And because ye are sons, God hath sent forth the Spirit of his Son into your hearts, crying, Abba, Father.

#### 1-17 — Ephesians 5:18 — AGREE

And be not drunk with wine, wherein is excess; but be filled with the Spirit;

#### 1-18 — Galatians 5:16 — AGREE

This I say then, Walk in the Spirit, and ye shall not fulfil the lust of the flesh.

#### 1-19 — 1 Corinthians 2:9 — AGREE

But as it is written, Eye hath not seen, nor ear heard, neither have entered into the heart of man, the things which God hath prepared for them that love him.

#### 1-20 — John 14:26 — AGREE

But the Comforter, which is the Holy Ghost, whom the Father will send in my name, he shall teach you all things, and bring all things to your remembrance, whatsoever I have said unto you.

#### 1-21 — I Cor. 2:4-5 — FLAGGED

- v.4: [FLAGGED — see Discrepancies: 1-21 v.4]
- v.5: That your faith should not stand in the wisdom of men, but in the power of God.

#### 1-22 — I Thes. 1:5 — AGREE

For our gospel came not unto you in word only, but also in power, and in the Holy Ghost, and in much assurance; as ye know what manner of men we were among you for your sake.

#### 1-23 — 1 Cor. 12:11 — AGREE

But all these worketh that one and the selfsame Spirit, dividing to every man severally as he will.

#### 1-24 — 1 Cor. 12:4-6 — AGREE

Now there are diversities of gifts, but the same Spirit. And there are differences of administrations, but the same Lord. And there are diversities of operations, but it is the same God which worketh all in all.

### God the Father (1-25 to 1-36)

#### 1-25 — Jeremiah 32:17 — AGREE

Ah Lord GOD! behold, thou hast made the heaven and the earth by thy great power and stretched out arm, and there is nothing too hard for thee:

#### 1-26 — Romans 11:33 — AGREE

O the depth of the riches both of the wisdom and knowledge of God! how unsearchable are his judgments, and his ways past finding out!

#### 1-27 — Jeremiah 23:24 — AGREE

Can any hide himself in secret places that I shall not see him? saith the LORD. Do not I fill heaven and earth? saith the LORD.

#### 1-28 — 2 Corinthians 9:8 — AGREE

And God is able to make all grace abound toward you; that ye, always having all sufficiency in all things, may abound to every good work:

#### 1-29 — 1 Chronicles 29:11-13 — FLAGGED

- v.11: [FLAGGED — see Discrepancies: 1-29 v.11]
- v.12: Both riches and honour come of thee, and thou reignest over all; and in thine hand is power and might; and in thine hand it is to make great, and to give strength unto all.
- v.13: Now therefore, our God, we thank thee, and praise thy glorious name.

#### 1-30 — 2 Thessalonians 3:3 — AGREE

But the Lord is faithful, who shall stablish you, and keep you from evil.

#### 1-31 — John 4:24 — AGREE

God is a Spirit: and they that worship him must worship him in spirit and in truth.

#### 1-32 — 1 Peter 1:15-16 — AGREE

But as he which hath called you is holy, so be ye holy in all manner of conversation; Because it is written, Be ye holy; for I am holy.

#### 1-33 — Psalm 145:3 — AGREE

Great is the LORD, and greatly to be praised; and his greatness is unsearchable.

#### 1-34 — 1 John 4:10 — AGREE

Herein is love, not that we loved God, but that he loved us, and sent his Son to be the propitiation for our sins.

#### 1-35 — Psalm 86:15 — FLAGGED

- v.15: [FLAGGED — see Discrepancies: 1-35 v.15]

#### 1-36 — Romans 8:28 — AGREE

And we know that all things work together for good to them that love God, to them who are the called according to his purpose.

## Series 2 — Growing In Love

### Love in Speech (2-1 to 2-12)

#### 2-1 — Ephesians 4:15 — AGREE

But speaking the truth in love, may grow up into him in all things, which is the head, even Christ:

#### 2-2 — Colossians 3:9 — AGREE

Lie not one to another, seeing that ye have put off the old man with his deeds;

#### 2-3 — Proverbs 17:9 — AGREE

He that covereth a transgression seeketh love; but he that repeateth a matter separateth very friends.

#### 2-4 — Proverbs 11:13 — AGREE

A talebearer revealeth secrets: but he that is of a faithful spirit concealeth the matter.

#### 2-5 — Colossians 4:4-6 — AGREE

That I may make it manifest, as I ought to speak. Walk in wisdom toward them that are without, redeeming the time. Let your speech be alway with grace, seasoned with salt, that ye may know how ye ought to answer every man.

#### 2-6 — Proverbs 15:1 — AGREE

A soft answer turneth away wrath: but grievous words stir up anger.

#### 2-7 — James 5:16 — AGREE

Confess your faults one to another, and pray one for another, that ye may be healed. The effectual fervent prayer of a righteous man availeth much.

#### 2-8 — Matthew 5:23-24 — AGREE

Therefore if thou bring thy gift to the altar, and there rememberest that thy brother hath ought against thee; Leave there thy gift before the altar, and go thy way; first be reconciled to thy brother, and then come and offer thy gift.

#### 2-9 — James 1:19 — AGREE

Wherefore, my beloved brethren, let every man be swift to hear, slow to speak, slow to wrath:

#### 2-10 — Proverbs 18:13 — AGREE

He that answereth a matter before he heareth it, it is folly and shame unto him.

#### 2-11 — Proverbs 9:8-9 — AGREE

Reprove not a scorner, lest he hate thee: rebuke a wise man, and he will love thee. Give instruction to a wise man, and he will be yet wiser: teach a just man, and he will increase in learning.

#### 2-12 — Matthew 18:15 — AGREE

Moreover if thy brother shall trespass against thee, go and tell him his fault between thee and him alone: if he shall hear thee, thou hast gained thy brother.

### Love in Response (2-13 to 2-24)

#### 2-13 — Ephesians 4:32 — FLAGGED

- v.32: [FLAGGED — see Discrepancies: 2-13 v.32]

#### 2-14 — Colossians 3:13 — AGREE

Forbearing one another, and forgiving one another, if any man have a quarrel against any: even as Christ forgave you, so also do ye.

#### 2-15 — Ephesians 4:2 — AGREE

With all lowliness and meekness, with longsuffering, forbearing one another in love;

#### 2-16 — 2 Timothy 2:24-25 — AGREE

And the servant of the Lord must not strive; but be gentle unto all men, apt to teach, patient, In meekness instructing those that oppose themselves; if God peradventure will give them repentance to the acknowledging of the truth;

#### 2-17 — Ephesians 4:26 — AGREE

Be ye angry, and sin not: let not the sun go down upon your wrath:

#### 2-18 — Colossians 3:8 — AGREE

But now ye also put off all these; anger, wrath, malice, blasphemy, filthy communication out of your mouth.

#### 2-19 — Hebrews 12:15 — AGREE

Looking diligently lest any man fail of the grace of God; lest any root of bitterness springing up trouble you, and thereby many be defiled;

#### 2-20 — Ephesians 4:31 — AGREE

Let all bitterness, and wrath, and anger, and clamour, and evil speaking, be put away from you, with all malice:

#### 2-21 — 1 Peter 2:20-21 — AGREE

For what glory is it, if, when ye be buffeted for your faults, ye shall take it patiently? but if, when ye do well, and suffer for it, ye take it patiently, this is acceptable with God. For even hereunto were ye called: because Christ also suffered for us, leaving us an example, that ye should follow his steps:

#### 2-22 — Romans 12:19 — AGREE

Dearly beloved, avenge not yourselves, but rather give place unto wrath: for it is written, Vengeance is mine; I will repay, saith the Lord.

#### 2-23 — Proverbs 27:4 — AGREE

Wrath is cruel, and anger is outrageous; but who is able to stand before envy?

#### 2-24 — James 3:16 — AGREE

For where envying and strife is, there is confusion and every evil work.

### Love in Action (2-25 to 2-36)

#### 2-25 — Romans 15:5-6 — AGREE

Now the God of patience and consolation grant you to be likeminded one toward another according to Christ Jesus: That ye may with one mind and one mouth glorify God, even the Father of our Lord Jesus Christ.

#### 2-26 — 1 Corinthians 1:10 — AGREE

Now I beseech you, brethren, by the name of our Lord Jesus Christ, that ye all speak the same thing, and that there be no divisions among you; but that ye be perfectly joined together in the same mind and in the same judgment.

#### 2-27 — Matthew 20:26-28 — AGREE

But it shall not be so among you: but whosoever will be great among you, let him be your minister; And whosoever will be chief among you, let him be your servant: Even as the Son of man came not to be ministered unto, but to minister, and to give his life a ransom for many.

#### 2-28 — Galatians 5:13 — AGREE

For, brethren, ye have been called unto liberty; only use not liberty for an occasion to the flesh, but by love serve one another.

#### 2-29 — Romans 15:2 — AGREE

Let every one of us please his neighbour for his good to edification.

#### 2-30 — Philippians 2:3-4 — AGREE

Let nothing be done through strife or vainglory; but in lowliness of mind let each esteem other better than themselves. Look not every man on his own things, but every man also on the things of others.

#### 2-31 — 1 Thes. 5:11 — AGREE

Wherefore comfort yourselves together, and edify one another, even as also ye do.

#### 2-32 — Eccl. 4:9-10 — AGREE

Two are better than one; because they have a good reward for their labour. For if they fall, the one will lift up his fellow: but woe to him that is alone when he falleth; for he hath not another to help him up.

#### 2-33 — Matthew 9:36 — AGREE

But when he saw the multitudes, he was moved with compassion on them, because they fainted, and were scattered abroad, as sheep having no shepherd.

#### 2-34 — Romans 12:15 — AGREE

Rejoice with them that do rejoice, and weep with them that weep.

#### 2-35 — James 3:17 — AGREE

But the wisdom that is from above is first pure, then peaceable, gentle, and easy to be intreated, full of mercy and good fruits, without partiality, and without hypocrisy.

#### 2-36 — Galatians 6:1 — AGREE

Brethren, if a man be overtaken in a fault, ye which are spiritual, restore such an one in the spirit of meekness; considering thyself, lest thou also be tempted.

## Series 3 — Growing in Faith

### Promises (3-1 to 3-12)

#### 3-1 — 2 Peter 1:3-4 — AGREE

According as his divine power hath given unto us all things that pertain unto life and godliness, through the knowledge of him that hath called us to glory and virtue: Whereby are given unto us exceeding great and precious promises: that by these ye might be partakers of the divine nature, having escaped the corruption that is in the world through lust.

#### 3-2 — 2 Cor. 1:20 — AGREE

For all the promises of God in him are yea, and in him Amen, unto the glory of God by us.

#### 3-3 — 2 Cor. 1:3-4 — AGREE

Blessed be God, even the Father of our Lord Jesus Christ, the Father of mercies, and the God of all comfort; Who comforteth us in all our tribulation, that we may be able to comfort them which are in any trouble, by the comfort wherewith we ourselves are comforted of God.

#### 3-4 — 1 Cor. 3:7-8 — AGREE

So then neither is he that planteth any thing, neither he that watereth; but God that giveth the increase. Now he that planteth and he that watereth are one: and every man shall receive his own reward according to his own labour.

#### 3-5 — Psalm 1:2-3 — AGREE

But his delight is in the law of the LORD; and in his law doth he meditate day and night. And he shall be like a tree planted by the rivers of water, that bringeth forth his fruit in his season; his leaf also shall not wither; and whatsoever he doeth shall prosper.

#### 3-6 — 2 Peter 1:8 — AGREE

For if these things be in you, and abound, they make you that ye shall neither be barren nor unfruitful in the knowledge of our Lord Jesus Christ.

#### 3-7 — 1 Pet. 5:10 — AGREE

But the God of all grace, who hath called us unto his eternal glory by Christ Jesus, after that ye have suffered a while, make you perfect, stablish, strengthen, settle you.

#### 3-8 — 2 Cor. 12:9 — AGREE

And he said unto me, My grace is sufficient for thee: for my strength is made perfect in weakness. Most gladly therefore will I rather glory in my infirmities, that the power of Christ may rest upon me.

#### 3-9 — Ephesians 1:3 — AGREE

Blessed be the God and Father of our Lord Jesus Christ, who hath blessed us with all spiritual blessings in heavenly places in Christ:

#### 3-10 — Psalm 37:4-5 — AGREE

Delight thyself also in the LORD: and he shall give thee the desires of thine heart. Commit thy way unto the LORD; trust also in him; and he shall bring it to pass.

#### 3-11 — 1 John 2:1-2 — FLAGGED

- v.1: My little children, these things write I unto you, that ye sin not. And if any man sin, we have an advocate with the Father, Jesus Christ the righteous:
- v.2: [FLAGGED — see Discrepancies: 3-11 v.2]

#### 3-12 — Ps. 103:12 — AGREE

As far as the east is from the west, so far hath he removed our transgressions from us.

### Word (3-13 to 3-24)

#### 3-13 — Hebrews 4:12 — AGREE

For the word of God is quick, and powerful, and sharper than any twoedged sword, piercing even to the dividing asunder of soul and spirit, and of the joints and marrow, and is a discerner of the thoughts and intents of the heart.

#### 3-14 — Isaiah 55:10-11 — AGREE

For as the rain cometh down, and the snow from heaven, and returneth not thither, but watereth the earth, and maketh it bring forth and bud, that it may give seed to the sower, and bread to the eater: So shall my word be that goeth forth out of my mouth: it shall not return unto me void, but it shall accomplish that which I please, and it shall prosper in the thing whereto I sent it.

#### 3-15 — 2 Peter 1:20-21 — AGREE

Knowing this first, that no prophecy of the scripture is of any private interpretation. For the prophecy came not in old time by the will of man: but holy men of God spake as they were moved by the Holy Ghost.

#### 3-16 — 1 Thessalonians 2:13 — AGREE

For this cause also thank we God without ceasing, because, when ye received the word of God which ye heard of us, ye received it not as the word of men, but as it is in truth, the word of God, which effectually worketh also in you that believe.

#### 3-17 — Jeremiah 15:16 — AGREE

Thy words were found, and I did eat them; and thy word was unto me the joy and rejoicing of mine heart: for I am called by thy name, O LORD God of hosts.

#### 3-18 — Job 23:12 — AGREE

Neither have I gone back from the commandment of his lips; I have esteemed the words of his mouth more than my necessary food.

#### 3-19 — Acts 17:11 — AGREE

These were more noble than those in Thessalonica, in that they received the word with all readiness of mind, and searched the scriptures daily, whether those things were so.

#### 3-20 — John 5:39-40 — AGREE

Search the scriptures; for in them ye think ye have eternal life: and they are they which testify of me. And ye will not come to me, that ye might have life.

#### 3-21 — John 8:31-32 — AGREE

Then said Jesus to those Jews which believed on him, If ye continue in my word, then are ye my disciples indeed; And ye shall know the truth, and the truth shall make you free.

#### 3-22 — Matthew 4:4 — AGREE

But he answered and said, It is written, Man shall not live by bread alone, but by every word that proceedeth out of the mouth of God.

#### 3-23 — Matthew 24:35 — AGREE

Heaven and earth shall pass away, but my words shall not pass away.

#### 3-24 — John 17:17 — AGREE

Sanctify them through thy truth: thy word is truth.

### Faith (3-25 to 3-36)

#### 3-25 — 1 Peter 1:6-7 — AGREE

Wherein ye greatly rejoice, though now for a season, if need be, ye are in heaviness through manifold temptations: That the trial of your faith, being much more precious than of gold that perisheth, though it be tried with fire, might be found unto praise and honour and glory at the appearing of Jesus Christ:

#### 3-26 — James 1:2-4 — AGREE

My brethren, count it all joy when ye fall into divers temptations; Knowing this, that the trying of your faith worketh patience. But let patience have her perfect work, that ye may be perfect and entire, wanting nothing.

#### 3-27 — Hebrews 4:2 — AGREE

For unto us was the gospel preached, as well as unto them: but the word preached did not profit them, not being mixed with faith in them that heard it.

#### 3-28 — Hebrews 10:38 — AGREE

Now the just shall live by faith: but if any man draw back, my soul shall have no pleasure in him.

#### 3-29 — Ephesians 6:16 — AGREE

Above all, taking the shield of faith, wherewith ye shall be able to quench all the fiery darts of the wicked.

#### 3-30 — 1 Timothy 6:11-12 — AGREE

But thou, O man of God, flee these things; and follow after righteousness, godliness, faith, love, patience, meekness. Fight the good fight of faith, lay hold on eternal life, whereunto thou art also called, and hast professed a good profession before many witnesses.

#### 3-31 — Hebrews 11:1 — AGREE

Now faith is the substance of things hoped for, the evidence of things not seen.

#### 3-32 — Romans 10:17 — AGREE

So then faith cometh by hearing, and hearing by the word of God.

#### 3-33 — Hebrews 6:12 — AGREE

That ye be not slothful, but followers of them who through faith and patience inherit the promises.

#### 3-34 — James 2:17 — AGREE

Even so faith, if it hath not works, is dead, being alone.

#### 3-35 — Galatians 2:16 — AGREE

Knowing that a man is not justified by the works of the law, but by the faith of Jesus Christ, even we have believed in Jesus Christ, that we might be justified by the faith of Christ, and not by the works of the law: for by the works of the law shall no flesh be justified.

#### 3-36 — Romans 5:1 — AGREE

Therefore being justified by faith, we have peace with God through our Lord Jesus Christ:

## Series 4 — Growing in Victory

### Victory (4-1 to 4-12)

#### 4-1 — 1 Cor. 15:57 — AGREE

But thanks be to God, which giveth us the victory through our Lord Jesus Christ.

#### 4-2 — 2 Cor. 2:14 — AGREE

Now thanks be unto God, which always causeth us to triumph in Christ, and maketh manifest the savour of his knowledge by us in every place.

#### 4-3 — 2 Cor. 10:4-5 — AGREE

(For the weapons of our warfare are not carnal, but mighty through God to the pulling down of strong holds;) Casting down imaginations, and every high thing that exalteth itself against the knowledge of God, and bringing into captivity every thought to the obedience of Christ;

#### 4-4 — Eph. 6:10-11 — AGREE

Finally, my brethren, be strong in the Lord, and in the power of his might. Put on the whole armour of God, that ye may be able to stand against the wiles of the devil.

#### 4-5 — Rev. 12:11 — AGREE

And they overcame him by the blood of the Lamb, and by the word of their testimony; and they loved not their lives unto the death.

#### 4-6 — James 4:7-8 — AGREE

Submit yourselves therefore to God. Resist the devil, and he will flee from you. Draw nigh to God, and he will draw nigh to you. Cleanse your hands, ye sinners; and purify your hearts, ye double minded.

#### 4-7 — Romans 8:5-6 — AGREE

For they that are after the flesh do mind the things of the flesh; but they that are after the Spirit the things of the Spirit. For to be carnally minded is death; but to be spiritually minded is life and peace.

#### 4-8 — Romans 13:14 — AGREE

But put ye on the Lord Jesus Christ, and make not provision for the flesh, to fulfil the lusts thereof.

#### 4-9 — 1 John 4:4 — AGREE

Ye are of God, little children, and have overcome them: because greater is he that is in you, than he that is in the world.

#### 4-10 — 1 John 5:4-5 — AGREE

For whatsoever is born of God overcometh the world: and this is the victory that overcometh the world, even our faith. Who is he that overcometh the world, but he that believeth that Jesus is the Son of God?

#### 4-11 — Psalm 37:31 — AGREE

The law of his God is in his heart; none of his steps shall slide.

#### 4-12 — Romans 6:12-13 — AGREE

Let not sin therefore reign in your mortal body, that ye should obey it in the lusts thereof. Neither yield ye your members as instruments of unrighteousness unto sin: but yield yourselves unto God, as those that are alive from the dead, and your members as instruments of righteousness unto God.

### Purity (4-13 to 4-24)

#### 4-13 — Philippians 4:8 — AGREE

Finally, brethren, whatsoever things are true, whatsoever things are honest, whatsoever things are just, whatsoever things are pure, whatsoever things are lovely, whatsoever things are of good report; if there be any virtue, and if there be any praise, think on these things.

#### 4-14 — Titus 1:15 — AGREE

Unto the pure all things are pure: but unto them that are defiled and unbelieving is nothing pure; but even their mind and conscience is defiled.

#### 4-15 — Luke 6:45 — AGREE

A good man out of the good treasure of his heart bringeth forth that which is good; and an evil man out of the evil treasure of his heart bringeth forth that which is evil: for of the abundance of the heart his mouth speaketh.

#### 4-16 — Proverbs 4:23 — AGREE

Keep thy heart with all diligence; for out of it are the issues of life.

#### 4-17 — Matthew 6:22 — AGREE

The light of the body is the eye: if therefore thine eye be single, thy whole body shall be full of light.

#### 4-18 — Matthew 5:28 — AGREE

But I say unto you, That whosoever looketh on a woman to lust after her hath committed adultery with her already in his heart.

#### 4-19 — 1 Thessalonians 4:3 — AGREE

For this is the will of God, even your sanctification, that ye should abstain from fornication:

#### 4-20 — 1 Corinthians 6:13 — AGREE

Meats for the belly, and the belly for meats: but God shall destroy both it and them. Now the body is not for fornication, but for the Lord; and the Lord for the body.

#### 4-21 — Ephesians 4:29 — AGREE

Let no corrupt communication proceed out of your mouth, but that which is good to the use of edifying, that it may minister grace unto the hearers.

#### 4-22 — Matthew 12:36-37 — AGREE

But I say unto you, That every idle word that men shall speak, they shall give account thereof in the day of judgment. For by thy words thou shalt be justified, and by thy words thou shalt be condemned.

#### 4-23 — 1 Thessalonians 5:22 — AGREE

Abstain from all appearance of evil.

#### 4-24 — 1 Timothy 5:1-2 — AGREE

Rebuke not an elder, but intreat him as a father; and the younger men as brethren; The elder women as mothers; the younger as sisters, with all purity.

### Prayer (4-25 to 4-36)

#### 4-25 — Matthew 21:22 — AGREE

And all things, whatsoever ye shall ask in prayer, believing, ye shall receive.

#### 4-26 — Matthew 7:7-8 — AGREE

Ask, and it shall be given you; seek, and ye shall find; knock, and it shall be opened unto you: For every one that asketh receiveth; and he that seeketh findeth; and to him that knocketh it shall be opened.

#### 4-27 — Matthew 6:6 — AGREE

But thou, when thou prayest, enter into thy closet, and when thou hast shut thy door, pray to thy Father which is in secret; and thy Father which seeth in secret shall reward thee openly.

#### 4-28 — Mark 1:35 — AGREE

And in the morning, rising up a great while before day, he went out, and departed into a solitary place, and there prayed.

#### 4-29 — Jeremiah 33:3 — AGREE

Call unto me, and I will answer thee, and shew thee great and mighty things, which thou knowest not.

#### 4-30 — Ephesians 3:20 — AGREE

Now unto him that is able to do exceeding abundantly above all that we ask or think, according to the power that worketh in us,

#### 4-31 — 1 John 5:14-15 — AGREE

And this is the confidence that we have in him, that, if we ask any thing according to his will, he heareth us: And if we know that he hear us, whatsoever we ask, we know that we have the petitions that we desired of him.

#### 4-32 — 1 Thes. 5:17-18 — AGREE

Pray without ceasing. In every thing give thanks: for this is the will of God in Christ Jesus concerning you.

#### 4-33 — 1 Samuel 12:23 — AGREE

Moreover as for me, God forbid that I should sin against the LORD in ceasing to pray for you: but I will teach you the good and the right way:

#### 4-34 — Matthew 9:37-38 — AGREE

Then saith he unto his disciples, The harvest truly is plenteous, but the labourers are few; Pray ye therefore the Lord of the harvest, that he will send forth labourers into his harvest.

#### 4-35 — Hebrews 13:15 — AGREE

By him therefore let us offer the sacrifice of praise to God continually, that is, the fruit of our lips giving thanks to his name.

#### 4-36 — Psalm 146:1-2 — AGREE

Praise ye the LORD. Praise the LORD, O my soul. While I live will I praise the LORD: I will sing praises unto my God while I have any being.

## Series 5 — Sharing Your Faith

### Evangelism (5-1 to 5-12)

#### 5-1 — Colossians 1:27-28 — AGREE

To whom God would make known what is the riches of the glory of this mystery among the Gentiles; which is Christ in you, the hope of glory: Whom we preach, warning every man, and teaching every man in all wisdom; that we may present every man perfect in Christ Jesus:

#### 5-2 — 2 Corinthians 5:19-20 — FLAGGED

- v.19: To wit, that God was in Christ, reconciling the world unto himself, not imputing their trespasses unto them; and hath committed unto us the word of reconciliation.
- v.20: [FLAGGED — see Discrepancies: 5-2 v.20]

#### 5-3 — 1 Thessalonians 2:4 — AGREE

But as we were allowed of God to be put in trust with the gospel, even so we speak; not as pleasing men, but God, which trieth our hearts.

#### 5-4 — 1 Corinthians 9:19 — AGREE

For though I be free from all men, yet have I made myself servant unto all, that I might gain the more.

#### 5-5 — John 4:35 — AGREE

Say not ye, There are yet four months, and then cometh harvest? behold, I say unto you, Lift up your eyes, and look on the fields; for they are white already to harvest.

#### 5-6 — 1 Thessalonians 2:8 — AGREE

So being affectionately desirous of you, we were willing to have imparted unto you, not the gospel of God only, but also our own souls, because ye were dear unto us.

#### 5-7 — Romans 3:10-12 — AGREE

As it is written, There is none righteous, no, not one: There is none that understandeth, there is none that seeketh after God. They are all gone out of the way, they are together become unprofitable; there is none that doeth good, no, not one.

#### 5-8 — 2 Thes. 1:8-9 — AGREE

In flaming fire taking vengeance on them that know not God, and that obey not the gospel of our Lord Jesus Christ: Who shall be punished with everlasting destruction from the presence of the Lord, and from the glory of his power;

#### 5-9 — 1 Peter 2:24 — AGREE

Who his own self bare our sins in his own body on the tree, that we, being dead to sins, should live unto righteousness: by whose stripes ye were healed.

#### 5-10 — 2 Timothy 1:9 — AGREE

Who hath saved us, and called us with an holy calling, not according to our works, but according to his own purpose and grace, which was given us in Christ Jesus before the world began,

#### 5-11 — Romans 10:9-10 — AGREE

That if thou shalt confess with thy mouth the Lord Jesus, and shalt believe in thine heart that God hath raised him from the dead, thou shalt be saved. For with the heart man believeth unto righteousness; and with the mouth confession is made unto salvation.

#### 5-12 — John 10:28-29 — FLAGGED

- v.28: And I give unto them eternal life; and they shall never perish, neither shall any man pluck them out of my hand.
- v.29: [FLAGGED — see Discrepancies: 5-12 v.29]

### Excuses (5-13 to 5-24)

#### 5-13 — Proverbs 21:2 — AGREE

Every way of a man is right in his own eyes: but the LORD pondereth the hearts.

#### 5-14 — Mark 8:36 — AGREE

For what shall it profit a man, if he shall gain the whole world, and lose his own soul?

#### 5-15 — John 7:17 — AGREE

If any man will do his will, he shall know of the doctrine, whether it be of God, or whether I speak of myself.

#### 5-16 — Luke 5:31-32 — AGREE

And Jesus answering said unto them, They that are whole need not a physician; but they that are sick. I came not to call the righteous, but sinners to repentance.

#### 5-17 — John 5:44 — AGREE

How can ye believe, which receive honour one of another, and seek not the honour that cometh from God only?

#### 5-18 — Hebrews 7:25 — AGREE

Wherefore he is able also to save them to the uttermost that come unto God by him, seeing he ever liveth to make intercession for them.

#### 5-19 — Proverbs 27:1 — AGREE

Boast not thyself of to morrow; for thou knowest not what a day may bring forth.

#### 5-20 — Romans 14:12 — AGREE

So then every one of us shall give account of himself to God.

#### 5-21 — John 5:39 — AGREE

Search the scriptures; for in them ye think ye have eternal life: and they are they which testify of me.

#### 5-22 — Prov. 14:12 — AGREE

There is a way which seemeth right unto a man, but the end thereof are the ways of death.

#### 5-23 — Mt. 25:41 — AGREE

Then shall he say also unto them on the left hand, Depart from me, ye cursed, into everlasting fire, prepared for the devil and his angels:

#### 5-24 — Romans 1:20 — AGREE

For the invisible things of him from the creation of the world are clearly seen, being understood by the things that are made, even his eternal power and Godhead; so that they are without excuse:

### Believer's Position in Christ (5-25 to 5-36)

#### 5-25 — 1 Peter 1:18-19 — AGREE

Forasmuch as ye know that ye were not redeemed with corruptible things, as silver and gold, from your vain conversation received by tradition from your fathers; But with the precious blood of Christ, as of a lamb without blemish and without spot:

#### 5-26 — 2 Corinthians 5:18 — AGREE

And all things are of God, who hath reconciled us to himself by Jesus Christ, and hath given to us the ministry of reconciliation;

#### 5-27 — Ephesians 1:7 — AGREE

In whom we have redemption through his blood, the forgiveness of sins, according to the riches of his grace;

#### 5-28 — Romans 6:14-15 — AGREE

For sin shall not have dominion over you: for ye are not under the law, but under grace. What then? shall we sin, because we are not under the law, but under grace? God forbid.

#### 5-29 — Galatians 3:26 — AGREE

For ye are all the children of God by faith in Christ Jesus.

#### 5-30 — 1 Peter 2:9 — FLAGGED

- v.9: [FLAGGED — see Discrepancies: 5-30 v.9]

#### 5-31 — 2 Corinthians 5:21 — AGREE

For he hath made him to be sin for us, who knew no sin; that we might be made the righteousness of God in him.

#### 5-32 — 1 Corinthians 1:30 — AGREE

But of him are ye in Christ Jesus, who of God is made unto us wisdom, and righteousness, and sanctification, and redemption:

#### 5-33 — Hebrews 10:14 — AGREE

For by one offering he hath perfected for ever them that are sanctified.

#### 5-34 — Romans 3:24 — AGREE

Being justified freely by his grace through the redemption that is in Christ Jesus:

#### 5-35 — Phil. 3:20 — AGREE

For our conversation is in heaven; from whence also we look for the Saviour, the Lord Jesus Christ:

#### 5-36 — Colossians 2:9-10 — AGREE

For in him dwelleth all the fulness of the Godhead bodily. And ye are complete in him, which is the head of all principality and power:

## Unassigned — Cover Page Sample (not part of any packet/series; see packets.md Validation Report, Anomaly 4)

### Cover-1 — Psalm 37:31 — AGREE

The law of his God is in his heart; none of his steps shall slide.

### Cover-2 — Proverbs 2:1-5 — AGREE

My son, if thou wilt receive my words, and hide my commandments with thee; So that thou incline thine ear unto wisdom, and apply thine heart to understanding; Yea, if thou criest after knowledge, and liftest up thy voice for understanding; If thou seekest her as silver, and searchest for her as for hid treasures; Then shalt thou understand the fear of the LORD, and find the knowledge of God.

### Cover-3 — Proverbs 6:21-22 — AGREE

Bind them continually upon thine heart, and tie them about thy neck. When thou goest, it shall lead thee; when thou sleepest, it shall keep thee; and when thou awakest, it shall talk with thee.

### Cover-4 — Proverbs 22:17-18 — AGREE

Bow down thine ear, and hear the words of the wise, and apply thine heart unto my knowledge. For it is a pleasant thing if thou keep them within thee; they shall withal be fitted in thy lips.

### Cover-5 — 2 Timothy 2:15 — AGREE

Study to shew thyself approved unto God, a workman that needeth not to be ashamed, rightly dividing the word of truth.

### Cover-6 — Hebrews 2:1 — AGREE

Therefore we ought to give the more earnest heed to the things which we have heard, lest at any time we should let them slip.

## Discrepancies

### A2 — Galatians 2:20 — FLAGGED (spelling)

- gutenberg: I am crucified with Christ: neverthless I live; yet not I, but Christ liveth in me: and the life which I now live in the flesh I live by the faith of the Son of God, who loved me, and gave himself for me.
- sacred-texts: I am crucified with Christ: neverthless I live; yet not I, but Christ liveth in me: and the life which I now live in the flesh I live by the faith of the Son of God, who loved me, and gave himself for me.
- aruljohn: I am crucified with Christ: nevertheless I live; yet not I, but Christ liveth in me: and the life which I now live in the flesh I live by the faith of the Son of God, who loved me, and gave himself for me.
- Majority: I am crucified with Christ: neverthless I live; yet not I, but Christ liveth in me: and the life which I now live in the flesh I live by the faith of the Son of God, who loved me, and gave himself for me.

### C5 — Lamentations 3:22 — FLAGGED (punctuation-only)

- gutenberg: It is of the LORD’s mercies that we are not consumed, because his compassions fail not.
- sacred-texts: It is of the LORD's mercies that we are not consumed, because his compassions fail not.
- aruljohn: It is of the LORD’s mercies that we are not consumed, because his compassions fail not.
- Majority: It is of the LORD’s mercies that we are not consumed, because his compassions fail not.

### D8 — 2 Corinthians 4:5 — FLAGGED (punctuation-only)

- gutenberg: For we preach not ourselves, but Christ Jesus the Lord; and ourselves your servants for Jesus’ sake.
- sacred-texts: For we preach not ourselves, but Christ Jesus the Lord; and ourselves your servants for Jesus' sake.
- aruljohn: For we preach not ourselves, but Christ Jesus the Lord; and ourselves your servants for Jesus’ sake.
- Majority: For we preach not ourselves, but Christ Jesus the Lord; and ourselves your servants for Jesus’ sake.

### E8 — Acts 24:16 — FLAGGED (wording)

- gutenberg: And herein do I exercise myself, to have always a conscience void to offence toward God, and toward men.
- sacred-texts: And herein do I exercise myself, to have always a conscience void to offence toward God, and toward men.
- aruljohn: And herein do I exercise myself, to have always a conscience void of offence toward God, and toward men.
- Majority: And herein do I exercise myself, to have always a conscience void to offence toward God, and toward men.

### 1-7 — John 1:18 — FLAGGED (punctuation-only)

- gutenberg: No man hath seen God at any time, the only begotten Son, which is in the bosom of the Father, he hath declared him.
- sacred-texts: No man hath seen God at any time, the only begotten Son, which is in the bosom of the Father, he hath declared him.
- aruljohn: No man hath seen God at any time; the only begotten Son, which is in the bosom of the Father, he hath declared him.
- Majority: No man hath seen God at any time, the only begotten Son, which is in the bosom of the Father, he hath declared him.

### 1-8 — Hebrews 1:3 — FLAGGED (punctuation-only)

- gutenberg: Who being the brightness of his glory, and the express image of his person, and upholding all things by the word of his power, when he had by himself purged our sins, sat down on the right hand of the Majesty on high:
- sacred-texts: Who being the brightness of his glory, and the express image of his person, and upholding all things by the word of his power, when he had by himself purged our sins, sat down on the right hand of the Majesty on high:
- aruljohn: Who being the brightness of his glory, and the express image of his person, and upholding all things by the word of his power, when he had by himself purged our sins, sat down on the right hand of the Majesty on high;
- Majority: Who being the brightness of his glory, and the express image of his person, and upholding all things by the word of his power, when he had by himself purged our sins, sat down on the right hand of the Majesty on high:

### 1-21 — 1 Corinthians 2:4 — FLAGGED (punctuation-only)

- gutenberg: And my speech and my preaching was not with enticing words of man’s wisdom, but in demonstration of the Spirit and of power:
- sacred-texts: And my speech and my preaching was not with enticing words of man's wisdom, but in demonstration of the Spirit and of power:
- aruljohn: And my speech and my preaching was not with enticing words of man’s wisdom, but in demonstration of the Spirit and of power:
- Majority: And my speech and my preaching was not with enticing words of man’s wisdom, but in demonstration of the Spirit and of power:

### 1-29 — 1 Chronicles 29:11 — FLAGGED (punctuation-only)

- gutenberg: Thine, O LORD is the greatness, and the power, and the glory, and the victory, and the majesty: for all that is in the heaven and in the earth is thine; thine is the kingdom, O LORD, and thou art exalted as head above all.
- sacred-texts: Thine, O LORD is the greatness, and the power, and the glory, and the victory, and the majesty: for all that is in the heaven and in the earth is thine; thine is the kingdom, O LORD, and thou art exalted as head above all.
- aruljohn: Thine, O LORD, is the greatness, and the power, and the glory, and the victory, and the majesty: for all that is in the heaven and in the earth is thine; thine is the kingdom, O LORD, and thou art exalted as head above all.
- Majority: Thine, O LORD is the greatness, and the power, and the glory, and the victory, and the majesty: for all that is in the heaven and in the earth is thine; thine is the kingdom, O LORD, and thou art exalted as head above all.

### 1-35 — Psalms 86:15 — FLAGGED (spelling)

- gutenberg: But thou, O Lord, art a God full of compassion, and gracious, longsuffering, and plenteous in mercy and truth.
- sacred-texts: But thou, O Lord, art a God full of compassion, and gracious, long suffering, and plenteous in mercy and truth.
- aruljohn: But thou, O Lord, art a God full of compassion, and gracious, long suffering, and plenteous in mercy and truth.
- Majority: But thou, O Lord, art a God full of compassion, and gracious, long suffering, and plenteous in mercy and truth.

### 2-13 — Ephesians 4:32 — FLAGGED (punctuation-only)

- gutenberg: And be ye kind one to another, tenderhearted, forgiving one another, even as God for Christ’s sake hath forgiven you.
- sacred-texts: And be ye kind one to another, tenderhearted, forgiving one another, even as God for Christ's sake hath forgiven you.
- aruljohn: And be ye kind one to another, tenderhearted, forgiving one another, even as God for Christ’s sake hath forgiven you.
- Majority: And be ye kind one to another, tenderhearted, forgiving one another, even as God for Christ’s sake hath forgiven you.

### 3-11 — 1 John 2:2 — FLAGGED (punctuation-only)

- gutenberg: And he is the propitiation for our sins: and not for ours only, but also for the sins of the whole world.
- sacred-texts: And he is the propitiation for our sins: and not for our's only, but also for the sins of the whole world.
- aruljohn: And he is the propitiation for our sins: and not for ours only, but also for the sins of the whole world.
- Majority: And he is the propitiation for our sins: and not for ours only, but also for the sins of the whole world.

### 5-2 — 2 Corinthians 5:20 — FLAGGED (punctuation-only)

- gutenberg: Now then we are ambassadors for Christ, as though God did beseech you by us: we pray you in Christ’s stead, be ye reconciled to God.
- sacred-texts: Now then we are ambassadors for Christ, as though God did beseech you by us: we pray you in Christ's stead, be ye reconciled to God.
- aruljohn: Now then we are ambassadors for Christ, as though God did beseech you by us: we pray you in Christ’s stead, be ye reconciled to God.
- Majority: Now then we are ambassadors for Christ, as though God did beseech you by us: we pray you in Christ’s stead, be ye reconciled to God.

### 5-12 — John 10:29 — FLAGGED (punctuation-only)

- gutenberg: My Father, which gave them me, is greater than all; and no man is able to pluck them out of my Father’s hand.
- sacred-texts: My Father, which gave them me, is greater than all; and no man is able to pluck them out of my Father's hand.
- aruljohn: My Father, which gave them me, is greater than all; and no man is able to pluck them out of my Father’s hand.
- Majority: My Father, which gave them me, is greater than all; and no man is able to pluck them out of my Father’s hand.

### 5-30 — 1 Peter 2:9 — FLAGGED (punctuation-only)

- gutenberg: But ye are a chosen generation, a royal priesthood, an holy nation, a peculiar people; that ye should shew forth the praises of him who hath called you out of darkness into his marvellous light;
- sacred-texts: But ye are a chosen generation, a royal priesthood, an holy nation, a peculiar people; that ye should shew forth the praises of him who hath called you out of darkness into his marvellous light;
- aruljohn: But ye are a chosen generation, a royal priesthood, an holy nation, a peculiar people; that ye should shew forth the praises of him who hath called you out of darkness into his marvellous light:
- Majority: But ye are a chosen generation, a royal priesthood, an holy nation, a peculiar people; that ye should shew forth the praises of him who hath called you out of darkness into his marvellous light;
