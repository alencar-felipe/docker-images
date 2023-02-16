#!/bin/bash

sudo docker run --rm -it \
-v $(pwd):/app \
--user $(id -u):$(id -g) \
alencarfelipe/my-latex $@
