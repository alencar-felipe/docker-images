#!/bin/bash

sudo docker run --rm -it \
--privileged \
-v $(pwd):/work \
--user $(id -u):$(id -g) \
alencarfelipe/riscv-dev $@