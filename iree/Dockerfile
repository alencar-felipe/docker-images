ARG BASE_IMAGE="debian:12"

FROM $BASE_IMAGE AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
        clang \
        cmake \
        git \
        lld \
        ninja-build \
        python3.11-full \
        python3.11-dev \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/opt/venv/bin:$PATH"

RUN python3 -m venv /opt/venv

RUN git clone https://github.com/iree-org/iree.git

WORKDIR /iree

ARG VERSION="15ea0dc"

RUN git checkout $VERSION

RUN git submodule update --init

RUN pip install -r runtime/bindings/python/iree/runtime/build_requirements.txt

RUN cmake -G Ninja -B ../iree-build/ -S . \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DIREE_ENABLE_ASSERTIONS=ON \
        -DIREE_ENABLE_SPLIT_DWARF=ON \
        -DIREE_ENABLE_THIN_ARCHIVES=ON \
        -DCMAKE_C_COMPILER=clang \
        -DCMAKE_CXX_COMPILER=clang++ \
        -DIREE_ENABLE_LLD=ON \
        -DIREE_BUILD_PYTHON_BINDINGS=ON  \
        -DPython3_EXECUTABLE="$(which python)" \
        -DCMAKE_INSTALL_PREFIX=../iree-build/install \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    && \
    cmake --build ../iree-build/ --target install

# FROM $BASE_IMAGE AS runner
