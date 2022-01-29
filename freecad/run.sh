#!/bin/bash

groupadd -g $GID runtimegroup
useradd --create-home runtime -u $UID -g $GID
chown runtime /home/runtime 

echo "wheel ALL=(ALL) ALL" >> /etc/sudoers
echo "runtime ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

su -c freecad runtime