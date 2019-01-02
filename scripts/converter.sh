#!/bin/bash

set -eux

# FILE=$(basename $1)

echo "downloading file...."

wget -O $2 $1

echo "spliting into parts"
ffmpeg -i $2 -f segment -segment_time "$(($3))" -c copy files/mp3s/out%03d.mp3

COUNTER=1
for file in files/mp3s/*
do
  yes | ffmpeg -i $file -ac 1 -ar 16000 files/flacs/$COUNTER.flac
  COUNTER=$[$COUNTER +1]
done
