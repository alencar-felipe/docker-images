ARG BASE_IMAGE="debian:bullseye"
ARG COMMIT="663b3852189acae826d99237cef45e629dfd6471"

FROM $BASE_IMAGE

RUN apt-get update && apt-get install -y \
    make git gcc autoconf automake autotools-dev curl python3 libmpc-dev \
    libmpfr-dev libgmp-dev gawk build-essential bison flex texinfo gperf \
    libtool patchutils bc zlib1g-dev libexpat-dev nodejs \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/riscv/riscv-gnu-toolchain \
    /riscv-gnu-toolchain && \
    cd /riscv-gnu-toolchain && \
    git checkout $COMMIT

WORKDIR /riscv-gnu-toolchain

RUN ./configure --prefix=/opt/riscv \
    --disable-linux \
    --disable-gdb \
    --disable-multilib \
    --with-arch=rv32imc \
    --with-abi=ilp32 \
    --with-cmodel=medlow \
    && \
    make -j8

RUN rm -rf /riscv-gnu-toolchain

ENV PATH="/opt/riscv:${PATH}"

WORKDIR /work