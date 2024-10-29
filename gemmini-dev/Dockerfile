ARG BASE_IMAGE="alencarfelipe/riscv-dev"

FROM ${BASE_IMAGE} AS builder

RUN git clone https://github.com/ucb-bar/libgemmini.git && \
    cd libgemmini && \
    git checkout 432d9562e0bd9cce896848ccfc472d62024be8ff && \
    make -j$(nproc) && \
    make install

FROM ${BASE_IMAGE} AS runner

COPY --from=builder ${RISCV} ${RISCV}
