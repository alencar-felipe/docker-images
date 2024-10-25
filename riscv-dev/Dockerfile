ARG BASE_IMAGE="alencarfelipe/riscv-gnu-toolchain:rv32imc-e65e7fc"

FROM ${BASE_IMAGE} AS builder

ARG RISCV_ARCH="rv32imc_zicsr_zifencei"

RUN apt-get update && apt-get install -y --no-install-recommends \
    autoconf \
    automake \
    build-essential \
    ca-certificates \
    device-tree-compiler \
    git \
    libftdi1-dev \
    libgpiod-dev \
    libtool \
    libusb-1.0.0-dev \
    libftdi1-dev \
    pkg-config \
    texinfo \
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

RUN apt-get update && apt-get install -y --no-install-recommends \
        libusb-1.0-0 \
        libftdi1 \
        libgpiod2 \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder ${RISCV} ${RISCV}
