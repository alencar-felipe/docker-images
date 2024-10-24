#!/bin/bash

docker run --rm -it \
    -v $(pwd):/work \
    --user $(id -u):$(id -g) \
    alencarfelipe/riscv-gnu-toolchain $@