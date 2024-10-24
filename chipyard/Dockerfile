FROM debian:12

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        git \
        sudo \
        wget \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /opt

ENV PATH="/opt/miniconda3/bin:${PATH}"

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
        -O miniconda3.sh \
    && \
    bash miniconda3.sh -b -u -p ./miniconda3 && \
    rm miniconda3.sh

RUN conda update -y -n base -c conda-forge conda && \
    conda install -y -n base conda-build && \
    conda install -y -n base conda-libmamba-solver && \
    conda install -y -n base conda-lock=1.4 && \
    conda config --system --set channel_priority flexible && \
    conda config --system --set changeps1 false && \
    conda config --system --set auto_activate_base false && \
    conda config --system --add channels ucb-bar && \
    conda init --no-user --system bash

RUN git clone https://github.com/ucb-bar/chipyard.git && \
    cd chipyard && \
    git checkout 1.9.1

WORKDIR /opt/chipyard

RUN export MAKEFLAGS=-"j $(nproc)" && \
    ./build-setup.sh riscv-tools
