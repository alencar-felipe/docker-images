ARG BASE_IMAGE="debian:12"

FROM $BASE_IMAGE

RUN apt-get update && apt-get install -y \
        autoconf \
        automake \
        autotools-dev \
        bc \
        bison \
        build-essential \
        cmake \
        curl \
        flex \
        gawk \
        gperf \
        git \
        libexpat-dev \
        libglib2.0-dev \
        libgmp-dev \
        libmpc-dev \
        libmpfr-dev \
        libslirp-dev \
        libtool \
        ninja-build \
        patchutils \
        python3 \
        python3-pip \
        texinfo \
        zlib1g-dev \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/riscv/riscv-gnu-toolchain \
    /riscv-gnu-toolchain && \
    cd /riscv-gnu-toolchain

WORKDIR /riscv-gnu-toolchain

ARG VERSION="663b385"

RUN git checkout $VERSION

ARG RISCV_ARCH="rv32imc"
ARG RISCV_ABI="ilp32"
ARG RISCV_CMODEL="medlow"

RUN ./configure --prefix=/opt/riscv \
    --disable-linux \
    --disable-gdb \
    --disable-multilib \
    --with-arch=${RISCV_ARCH} \
    --with-abi=${RISCV_ABI} \
    --with-cmodel=${RISCV_CMODEL} \
    && \
    make -j$(nproc)

RUN rm -rf /riscv-gnu-toolchain

ENV PATH="/opt/riscv/bin:${PATH}"

WORKDIR /work