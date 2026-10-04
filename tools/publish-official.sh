#!/usr/bin/env bash
# Publish navigators/official/ (index.html + packet-<letter>.mp3) to the
# public S3 website bucket, plus a zip of all officials. See
# navigators/procedures/07-publish-official.md.
set -euo pipefail
BUCKET="${BUCKET:-scripture-memorization-songs}"
REGION="${REGION:-us-east-1}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/navigators/official"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT

# Zip of all official mp3s (flat, human-readable names inside).
mkdir -p "$TMP/Scripture Songs"
for f in "$SRC"/packet-*.mp3; do cp "$f" "$TMP/Scripture Songs/$(basename "$f")"; done
(cd "$TMP" && zip -q -r navigators-official-songs.zip "Scripture Songs")

aws s3 sync "$SRC" "s3://$BUCKET/" --region "$REGION" \
  --exclude '*' --include 'packet-*.mp3' --content-type audio/mpeg --cache-control 'public, max-age=300'
if [ -d "$SRC/candidates" ]; then
  aws s3 sync "$SRC/candidates" "s3://$BUCKET/candidates/" --region "$REGION" --delete \
    --exclude '*' --include '*.m4a' --content-type audio/mp4 --cache-control 'public, max-age=300'
else
  aws s3 rm "s3://$BUCKET/candidates/" --recursive --region "$REGION"
fi
aws s3 cp "$SRC/index.html" "s3://$BUCKET/index.html" --region "$REGION" \
  --content-type 'text/html; charset=utf-8' --cache-control 'public, max-age=60'
aws s3 cp "$TMP/navigators-official-songs.zip" "s3://$BUCKET/navigators-official-songs.zip" --region "$REGION" \
  --content-type application/zip --cache-control 'public, max-age=300'

echo "Published: http://$BUCKET.s3-website-$REGION.amazonaws.com/"
