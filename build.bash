#!/bin/bash

set -e

PWD="$(pwd)"
HUB_USER="alencarfelipe"

build-image () {
    local NAME="$1"
    local TAG="$2"
    local IMAGE="$PWD/$NAME"
    local JSON="$IMAGE/tags.json"

    docker build $IMAGE \
	-t $HUB_USER/$NAME:$TAG \
    $(jq ".[\"$TAG\"] | to_entries | map(\"--build-arg \" + .key + \"=\" + .value) | join(\" \")" -cr $JSON)

	docker push $HUB_USER/$NAME:$TAG 
}

if [ $# -ne 0 ]; then
    build-image $@
    exit
fi

build-image doxygen latest

build-image freecad latest

build-image gnu-arm-embedded-toolchain 10.3-2021.10-bullseye
build-image gnu-arm-embedded-toolchain latest

build-image jupyter-octave latest

build-image my-latex latest

build-image stm32-dev latest

build-image wine latest
