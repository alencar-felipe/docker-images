#!/bin/bash

xhost +

sudo docker run --rm -it -v $(pwd):/workdir \
-e DISPLAY=$DISPLAY \
-v /tmp/.X11-unix:/tmp/.X11-unix \
alencarfelipe/gnuradio:latest