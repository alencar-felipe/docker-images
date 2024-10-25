FROM alencarfelipe/riscv-dev:rv32imc

RUN git clone https://github.com/ucb-bar/libgemmini.git && \
    cd libgemmini && \
    git checkout 432d9562e0bd9cce896848ccfc472d62024be8ff && \
    make -j$(nproc) && \
    make install
