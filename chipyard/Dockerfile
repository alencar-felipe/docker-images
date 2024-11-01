
FROM debian:12

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        wget \
        git \
        sudo \
        ca-certificates \
        keyboard-configuration \
        console-setup \
        bc \
        unzip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install conda ===============================================================

ENV PATH="/opt/conda/bin:$PATH"

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
        -O miniconda.sh \
    && \
    bash miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh

RUN conda install -y \
        python=3.11 \
        conda-libmamba-solver \
        conda-lock==1.4.0

RUN conda config --set solver libmamba

# clone chipyard ==============================================================

RUN git clone https://github.com/ucb-bar/chipyard.git

WORKDIR /chipyard

ARG VERSION="1.13.0"

RUN git checkout ${VERSION}

# setup chipyard ==============================================================

RUN ./build-setup.sh riscv-tools -s 8 -s 9
