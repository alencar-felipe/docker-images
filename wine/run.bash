#!/bin/bash

docker run --rm -it \
-v $(pwd):/work \
alencarfelipe/wine:latest
