#!/bin/bash

groupadd -g $GID runtimegroup
useradd --create-home runtime -u $UID -g $GID
usermod -aG wheel runtime

echo "wheel ALL=(ALL) ALL" >> /etc/sudoers
echo "runtime ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

cmd="doxygen $@"

su -c "$cmd" runtime