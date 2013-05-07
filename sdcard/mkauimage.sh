#!/bin/bash

# Usage: ./mkauimage.sh audio1.ogg [audio2.mp3 ...] audio.raw
# Takes in several audio files, concatenates them, and converts them to
# raw 16-bit signed-integer big-endian PCM data

length=$(($#-1))
inputs=${@:1:$length}
output=$(eval echo \$$#)

for file in $inputs
do
	sox "$file" -b 16 -e signed-integer -B -c 1 -t raw - >tempfile
        cat tempfile | wc -c | dd bs=512
        dd if=tempfile bs=512
done > $output
