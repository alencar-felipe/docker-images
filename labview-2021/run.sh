#!/bin/bash

groupadd -g $GID runtimegroup
useradd --create-home runtime -u $UID -g $GID
usermod -aG runtime

echo "wheel ALL=(ALL) ALL" >> /etc/sudoers
echo "runtime ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

su -c 'GTK_THEME=Adwaita:light /usr/local/natinst/LabVIEW-2021-64/labviewprofull' runtime
