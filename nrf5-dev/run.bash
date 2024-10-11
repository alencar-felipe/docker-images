#!/bin/bash

docker run --rm -it \
    -e PS1='(nrf5-dev) $(realpath --relative-to=/work .) \$ ' \
    -v "$(pwd):/work" -w /work \
    -u $(id -u):$(id -g) \
    --privileged \
    alencarfelipe/nrf5-dev \
    /bin/bash --norc
