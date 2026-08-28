# Source: aruljohn/Bible-kjv (GitHub)

- Files: one JSON per book (e.g. `2Corinthians.json`), plus `Books.json`
- URL: https://github.com/aruljohn/Bible-kjv
- Commit: `a9aa4e55afbb3e095f57e4b14cd1f22c5ee8d7c9` (shallow clone,
  `.git` removed)
- Retrieved: 2026-08-27
- Combined SHA-256:
  `f45722adbce3f7b8b9918de5955bc80e2519c3b83ce6846b2cea98cfe9225a19`
  computed by exactly this command, run from this directory (note the `./`
  path prefix that `find` produces is part of the hashed bytes):
  `find . -type f -name "*.json" | sort | xargs shasum -a 256 | shasum -a 256`
- Format: per book, JSON of the shape
  `{"book": ..., "chapters": [{"chapter": "1", "verses": [{"verse": "1",
  "text": ...}, ...]}, ...]}`
- Copyright: repository is MIT-licensed (see `LICENSE`); the KJV text
  itself is in the public domain in the United States.
