ARG BASE_IMAGE="debian:12"

FROM $BASE_IMAGE AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
        autoconf \
        automake \
        bc \
        bison \
        build-essential \
        curl \
        flex \
        gawk \
        git \
        libexpat-dev \
        libgmp-dev \
        libmpc-dev \
        libmpfr-dev \
        patchutils \
        python3 \
        python3-pip \
        texinfo \
        zlib1g-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/riscv/riscv-gnu-toolchain /riscv-gnu-toolchain && \
    cd /riscv-gnu-toolchain

WORKDIR /riscv-gnu-toolchain

ARG VERSION="e65e7fc"

RUN git checkout $VERSION

ARG RISCV_ARCH="rv32imc_zicsr_zifencei"
ARG RISCV_ABI="ilp32"
ARG RISCV_CMODEL="medlow"

RUN ./configure --prefix=/opt/riscv \
    --enable-debug-info=yes \
    --disable-linux \
    --disable-multilib \
    --with-arch=${RISCV_ARCH} \
    --with-abi=${RISCV_ABI} \
    --with-cmodel=${RISCV_CMODEL} \
    && \
    make -j$(nproc)

FROM $BASE_IMAGE

RUN apt-get update && apt-get install -y --no-install-recommends \
        libgmp10 \
        libmpc3 \
        libmpfr6 \
        zlib1g \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /opt/riscv /opt/riscv

ENV RISCV="/opt/riscv"
ENV PATH="${RISCV}/bin:${PATH}"
