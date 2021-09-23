#!/bin/bash

if [ "$0" != "$BASH_SOURCE" ]; then
    echo "Error: Script must not be sourced"
    exit 1
fi

cd "$(dirname "$(dirname "$0")")"

docker build -t halcogen .