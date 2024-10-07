FROM alencarfelipe/gcc-arm-none-eabi:4_9-2015q3

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

ARG SDK_URL=https://developer.nordicsemi.com/nRF5_SDK/nRF5_SDK_v12.x.x/nRF5_SDK_12.3.0_d7731ad.zip
ARG SDK_ROOT=/opt/nordic/nRF5_SDK_12.3.0_d7731ad
ENV SDK_ROOT=${SDK_ROOT}

RUN mkdir -p /opt/nordic && \
    wget ${SDK_URL} -O sdk.zip && \
    unzip sdk.zip -d /opt/nordic && \
    rm sdk.zip

RUN sed -i 's|^GNU_INSTALL_ROOT :=.*|GNU_INSTALL_ROOT := /usr|' \
    ${SDK_ROOT}/components/toolchain/gcc/Makefile.posix

# # Install dependencies

# # Add the toolchain to the PATH
# ENV PATH="/opt/gcc-arm-none-eabi-${GCC_ARM_VERSION}/bin:${PATH}"

# # Download and install nRF5 SDK version 12.3.0
# RUN wget -q https://developer.nordicsemi.com/nRF5_SDK/nRF5_SDK_v12.x.x/nRF5_SDK_${NRF_SDK_VERSION}_d7731ad.zip \
#     && unzip nRF5_SDK_${NRF_SDK_VERSION}_d7731ad.zip -d /opt/ \
#     && rm nRF5_SDK_${NRF_SDK_VERSION}_d7731ad.zip

# # Set the SDK root as an environment variable
# ENV NRF5_SDK_ROOT="/opt/nRF5_SDK_${NRF_SDK_VERSION}_d7731ad"

# # Install J-Link tools (Optional, if you're using Segger J-Link for flashing)
# RUN wget -q https://www.segger.com/downloads/jlink/JLink_Linux_V684a_x86_64.deb \
#     && dpkg -i JLink_Linux_V684a_x86_64.deb \
#     && rm JLink_Linux_V684a_x86_64.deb

# # Install Nordic's nrfutil (for DFU over BLE)
# RUN pip install nrfutil

# # Set workdir to the examples folder in the SDK
# WORKDIR /opt/nRF5_SDK_${NRF_SDK_VERSION}_d7731ad/examples

# Entry point (optional)
CMD ["/bin/bash"]
