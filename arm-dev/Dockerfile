ARG LLVM_VER=12
ARG GNU_RM_VER=10.3-2021.10

FROM alencarfelipe/gnu-arm-embedded-toolchain:${GNU_RM_VER}-bullseye-slim

# LLVM Toolchain ==============================================================#

ARG LLVM_VER

RUN apt-get update && apt-get install -y \
    lsb-release wget software-properties-common gnupg2 perl

RUN wget https://apt.llvm.org/llvm.sh && \
    chmod +x llvm.sh && \
    ./llvm.sh ${LLVM_VER} all && \
    rm llvm.sh

# Other Tools =================================================================#

RUN apt-get update && apt-get install -y \
    cmake make stlink-tools usbutils openocd 

# Execution Environment =======================================================#

ADD app.bash /app.bash

RUN chmod +x /app.bash && \
    mkdir -p /workdir /home/runtime && \
    echo "PS1=\"(arm-dev) \$ \"" >> /etc/profile && \
    echo "cd /workdir" >> /etc/profile

WORKDIR /workdir

ENTRYPOINT /app.bash
