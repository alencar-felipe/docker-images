FROM alencarfelipe/gcc-arm-none-eabi:9-2019-q4-major

RUN apt-get update && \
    apt-get install -y \
        cmake \
        build-essential \
        git \
        libusb-1.0-0-dev \
        unzip \
        wget \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ARG URL=https://developer.nordicsemi.com/nRF5_SDK/nRF5_SDK_v12.x.x/nRF5_SDK_12.3.0_d7731ad.zip
ARG VERSION=nRF5_SDK_12.3.0_d7731ad
ENV SDK_ROOT="/opt/nordic/${VERSION}"

RUN mkdir -p /opt/nordic && \
    wget ${URL} -O sdk.zip && \
    unzip sdk.zip -d /opt/nordic && \
    rm sdk.zip

RUN sed -i 's|^GNU_INSTALL_ROOT :=.*|GNU_INSTALL_ROOT := '"${GCC_ARM_ROOT}"'|' \
    "${SDK_ROOT}/components/toolchain/gcc/Makefile.posix"

CMD ["/bin/bash"]
