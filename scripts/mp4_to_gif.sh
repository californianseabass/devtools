#!/bin/bash

if [[ -z $1 ]]; then
	echo "you must provide a path to an mp4 file"
	exit -1
fi
arg=$(basename $1)
name=${arg%.*}
DIR=/tmp/frames

mkdir $DIR
ffmpeg -i $1  -r 1 '/tmp/frames/frame-%03d.jpg'
cd $DIR
convert -delay 20 -loop 0 *.jpg ${name}.gif
