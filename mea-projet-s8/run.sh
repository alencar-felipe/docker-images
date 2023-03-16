#!/bin/bash

xhost +

docker run -it --rm \
-p 8888:8888 \
-v $(pwd):/home/jovyan/work \
-e DISPLAY=$DISPLAY \
-v /tmp/.X11-unix:/tmp/.X11-unix \
alencarfelipe/mea-projet-s8 $@