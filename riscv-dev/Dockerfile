ARG BASE_IMAGE="alencarfelipe/riscv-gnu-toolchain:rv32imc-663b385"

FROM ${BASE_IMAGE} AS builder

ARG RISCV_ARCH="rv32imc_zicsr_zifencei"

RUN apt-get update && apt-get install -y --no-install-recommends \
        autoconf \
        automake \
        build-essential \
        ca-certificates \
        device-tree-compiler \
        git \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/riscv/riscv-isa-sim.git && \
    cd riscv-isa-sim && \
    git checkout 530af85d83781a3dae31a4ace84a573ec255fefa && \
    mkdir build/ && cd build/ && \
    ../configure --prefix=/opt/riscv \
        --enable-histogram \
        --with-isa=${RISCV_ARCH} \
    && \
    make -j$(nproc) && \
    make install

RUN git clone https://github.com/riscv-software-src/riscv-pk.git && \
    cd riscv-pk && \
    git checkout fafaedd2825054222ce2874bf4a90164b5b071d4 && \
    mkdir build/ && cd build/ && \
    ../configure --prefix=/opt/riscv \
        --host=riscv32-unknown-elf \
        --with-arch=${RISCV_ARCH} \
    && \
    make -j$(nproc) && \
    make install

RUN git clone https://github.com/riscv/riscv-openocd.git && \
    cd riscv-openocd && \
    git checkout 6e9514efcd0b5af1f5ffae5d1afa7e7640962ca6 && \
    ./bootstrap && \
    ./configure --prefix=/opt/riscv \
    && \
    make -j$(nproc) && \
    make install

FROM ${BASE_IMAGE}

COPY --from=builder /opt/riscv /opt/riscv

ENV PATH="/opt/riscv/bin:${PATH}"
