#!/bin/bash

if [ "$0" = "$BASH_SOURCE" ]; then
    echo "Error: Script must be sourced"
    exit 1
fi

xhost +

alias ccs-studio="docker run --rm -it -v \$(pwd):/home/runtime -v /tmp/.X11-unix:/tmp/.X11-unix \
--privileged -v /dev/bus/usb:/dev/bus/usb -e DISPLAY=$DISPLAY -e UID=\$(id -u) -e GID=\$(id -g) \
ccs"
