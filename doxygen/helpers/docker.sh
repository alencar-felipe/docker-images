#!/bin/bash

if [ "$0" = "$BASH_SOURCE" ]; then
    echo "Error: Script must be sourced"
    exit 1
fi

alias doxygen="docker run --rm -it -v \$(pwd):/home/runtime/data \
    -e UID=\$(id -u) -e GID=\$(id -g) doxygen"
