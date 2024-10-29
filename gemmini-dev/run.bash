#!/bin/bash

docker run --rm -it \
    -e PS1='(gemmini-dev) $(realpath --relative-to=/work .) \$ ' \
    -v "$(pwd):/work" -w /work \
    -u $(id -u):$(id -g) \
    alencarfelipe/gemmini-dev \
    /bin/bash --norc