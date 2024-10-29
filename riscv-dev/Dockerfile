ARG BASE_IMAGE="alencarfelipe/riscv-gnu-toolchain:e65e7fc"

FROM ${BASE_IMAGE} AS builder

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

# spike =======================================================================

RUN git clone https://github.com/riscv/riscv-isa-sim.git && \
    cd riscv-isa-sim && \
    git checkout 88fc84ded155a9e01987c4dfb7a77800e69b232b && \
    mkdir build/ && \
    cd build/ && \
    ../configure --prefix=${RISCV} && \
    make -j$(nproc) && \
    make install

# openocd =====================================================================

RUN git clone https://github.com/riscv/riscv-openocd.git && \
    cd riscv-openocd && \
    git checkout 6e9514efcd0b5af1f5ffae5d1afa7e7640962ca6 && \
    ./bootstrap && \
    ./configure --prefix=${RISCV} && \
    make -j$(nproc) && \
    make install

# pk ==========================================================================

RUN git clone https://github.com/riscv-software-src/riscv-pk.git && \
    cd riscv-pk && \
    git checkout fafaedd2825054222ce2874bf4a90164b5b071d4

RUN mkdir riscv-pk/build32 && \
    cd riscv-pk/build32 && \
    ../configure --prefix=${RISCV} \
        --host=riscv64-unknown-elf \
        --with-arch=rv32i_zicsr_zifencei \
    && \
    make -j$(nproc) && \
    make install

RUN mkdir riscv-pk/build64 && \
    cd riscv-pk/build64 && \
    ../configure --prefix=${RISCV} \
        --host=riscv64-unknown-elf \
        --with-arch=rv64imafdc_zicsr_zifencei \
    && \
    make -j$(nproc) && \
    make install

# libgloss-htif ===============================================================

COPY libgloss-htif.patch libgloss-htif.patch

RUN git clone https://github.com/ucb-bar/libgloss-htif.git && \
    cd libgloss-htif && \
    git checkout 39234a16247ab1fa234821b251f1f1870c3de343 && \
    git apply ../libgloss-htif.patch && \
    mkdir build/ && \
    cd build/ && \
    ../configure --prefix=${RISCV}/riscv64-unknown-elf \
        --host=riscv64-unknown-elf \
    && \
    make -j$(nproc) && \
    make install

# =============================================================================

FROM ${BASE_IMAGE} AS runner

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
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

COPY --from=builder ${RISCV} ${RISCV}
