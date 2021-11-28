#!/bin/bash

if [ "$0" = "$BASH_SOURCE" ]; then
    echo "Error: Script must be sourced"
    exit 1
fi

alias jupyter-octave="docker run --rm -it -p 8888:8888 -v \$(pwd):/notebooks \
-v /dev/snd:/dev/snd --privileged \
-e UID=\$(id -u) -e GID=\$(id -g) --network=\"host\" jupyter-octave"
