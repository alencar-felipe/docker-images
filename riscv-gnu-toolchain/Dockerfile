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

RUN git clone https://github.com/riscv/riscv-gnu-toolchain

WORKDIR /riscv-gnu-toolchain

ARG VERSION="e65e7fc"

RUN git checkout $VERSION

ENV RISCV="/opt/riscv"
ENV PATH="${RISCV}/bin:${PATH}"

RUN ./configure --prefix=${RISCV} \
        --enable-debug-info=yes \
        --enable-multilib \
        --disable-linux \
        --with-cmodel=medany \
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

ENV RISCV="/opt/riscv"
ENV PATH="${RISCV}/bin:${PATH}"

COPY --from=builder ${RISCV} ${RISCV}
