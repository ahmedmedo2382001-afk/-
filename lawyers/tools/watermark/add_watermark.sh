#!/usr/bin/env bash
# يحط العلامة المائية على فيديو أو أكتر، ويطلّع نسخة 720p للعينة
# الاستخدام: ./add_watermark.sh video1.mp4 video2.mp4 ...
# الناتج: sample_<اسم الفيديو>.mp4 في نفس الفولدر
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
WM="$DIR/watermark.png"
OPACITY="${OPACITY:-0.35}"   # الشفافية: 0.35 = 35%

for IN in "$@"; do
  OUT="$(dirname "$IN")/sample_$(basename "${IN%.*}").mp4"
  ffmpeg -y -loglevel error -i "$IN" -i "$WM" -filter_complex \
    "[0:v]scale=-2:720[v];[1:v]format=rgba,colorchannelmixer=aa=${OPACITY}[wm0];[wm0][v]scale2ref=w=iw*0.85:h=ow/mdar[wm][vv];[vv][wm]overlay=(W-w)/2:(H-h)/2" \
    -c:v libx264 -crf 26 -preset veryfast -c:a copy "$OUT"
  echo "✓ $OUT"
done
