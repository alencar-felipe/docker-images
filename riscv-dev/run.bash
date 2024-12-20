#!/bin/bash

docker run --rm -it \
    -e PS1='(riscv-dev) $(realpath --relative-to=/work .) \$ ' \
    -v "$(pwd):/work" -w /work \
    -u $(id -u):$(id -g) \
    alencarfelipe/riscv-dev \
    /bin/bash --norc