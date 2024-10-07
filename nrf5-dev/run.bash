#!/bin/bash

docker run --rm -it \
    -v "$(pwd):/work" -w /work \
    -u $(id -u):$(id -g) \
    alencarfelipe/nrf5-dev