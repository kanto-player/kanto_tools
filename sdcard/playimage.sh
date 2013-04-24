#!/bin/sh
# Plays raw PCM data

play -b 16 -e signed-integer -B -c 1 -r 44100 -t raw $1
