#!/bin/bash

if [ "$0" = "$BASH_SOURCE" ]; then
    echo "Error: Script must be sourced"
    exit 1
fi

xhost +

alias ltspice="docker run --rm -it -v \$(pwd):/home/runtime/workdir -v /tmp/.X11-unix:/tmp/.X11-unix \
-e DISPLAY=$DISPLAY -e UID=\$(id -u) -e GID=\$(id -g) \
ltspice"
