#!/bin/bash

/opt/ccs/install_scripts/install_drivers.sh

groupadd -g $GID runtimegroup
useradd --create-home runtime -u $UID -g $GID
usermod -aG wheel runtime

echo "wheel ALL=(ALL) ALL" >> /etc/sudoers
echo "runtime ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

su -c 'GTK_THEME=Adwaita:light /opt/ccs/eclipse/ccstudio' runtime
