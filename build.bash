#!/bin/bash

docker run --rm -it \
-v /var/run/docker.sock:/var/run/docker.sock \
-v $(pwd):/docker-images \
alencarfelipe/build $@