#!/bin/bash
# arecord script
arecord -f S16_LE -d 2 -D plughw:1,0 entry.wav