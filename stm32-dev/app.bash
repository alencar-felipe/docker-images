#!/bin/bash

set -e

groupadd -g $GID runtimegroup
useradd runtime -u $UID -g $GID -g root

echo "wheel ALL=(ALL) ALL" >> /etc/sudoers
echo "runtime ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

su -s /bin/bash - runtime