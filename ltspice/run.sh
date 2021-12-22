#!/bin/bash

groupadd -g $GID runtimegroup
useradd --create-home runtime -u $UID -g $GID

echo "wheel ALL=(ALL) ALL" >> /etc/sudoers
echo "runtime ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

su -c 'wine /LTspiceXVII.exe' runtime