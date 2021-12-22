#!/bin/bash

if [ "$0" = "$BASH_SOURCE" ]; then
    echo "Error: Script must be sourced"
    exit 1
fi

xhost +

alias wine="docker run --rm -it -v \$(pwd):/home/runtime -v /tmp/.X11-unix:/tmp/.X11-unix \
-e DISPLAY=$DISPLAY wine"
