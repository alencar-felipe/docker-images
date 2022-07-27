#!/bin/bash

sudo docker run --rm -it -v $(pwd):/workdir \
--privileged -e UID=$(id -u) -e GID=$(id -g) \
alencarfelipe/stm32-dev:latest