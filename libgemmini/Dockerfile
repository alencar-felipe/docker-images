ARG BASE_IMAGE="alencarfelipe/riscv-dev"

FROM ${BASE_IMAGE} AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
        autoconf \
        automake \
        build-essential \
        ca-certificates \
        git \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/ucb-bar/libgemmini.git && \
    cd libgemmini && \
    git checkout 432d9562e0bd9cce896848ccfc472d62024be8ff && \
    make -j$(nproc) && \
    make install

FROM ${BASE_IMAGE}

COPY --from=builder ${RISCV} ${RISCV}
