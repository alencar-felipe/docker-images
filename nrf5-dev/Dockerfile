FROM alencarfelipe/gcc-arm-none-eabi:9-2019-q4-major

RUN apt-get update && \
    apt-get install -y \
        cmake \
        build-essential \
        git \
        libncurses5 \
        libncurses-dev \
        libusb-1.0-0-dev \
        openocd \
        unzip \
        usbutils \
        wget

# nrf5 sdk ====================================================================

ARG SDK_URL=https://developer.nordicsemi.com/nRF5_SDK/nRF5_SDK_v12.x.x/nRF5_SDK_12.3.0_d7731ad.zip
ARG VERSION=nRF5_SDK_12.3.0_d7731ad
ENV SDK_ROOT="/opt/nordic/${VERSION}"

RUN mkdir -p /opt/nordic && \
    wget ${SDK_URL} -O sdk.zip && \
    unzip sdk.zip -d /opt/nordic && \
    rm sdk.zip

RUN sed -i 's|^GNU_INSTALL_ROOT :=.*|GNU_INSTALL_ROOT := '"${GCC_ARM_ROOT}"'|' \
    "${SDK_ROOT}/components/toolchain/gcc/Makefile.posix"

# nrf command line tools ======================================================

ARG NRF_COMMAND_LINE_TOOLS_URL=https://nsscprodmedia.blob.core.windows.net/prod/software-and-other-downloads/desktop-software/nrf-command-line-tools/sw/versions-10-x-x/10-24-2/nrf-command-line-tools_10.24.2_amd64.deb

RUN wget -O nrf_command_line_tools.deb ${NRF_COMMAND_LINE_TOOLS_URL} && \
    apt-get update && \
    dpkg -i nrf_command_line_tools.deb || apt-get install -f -y && \
    rm nrf_command_line_tools.deb

# nrfutil =====================================================================

ARG NRFUTIL_URL=https://developer.nordicsemi.com/.pc-tools/nrfutil/x64-linux/nrfutil
ENV NRFUTIL_HOME=/usr/local/share/nrfutil
ENV PATH="${NRFUTIL_HOME}/bin:${PATH}"

RUN mkdir -p ${NRFUTIL_HOME} && \
    wget -q ${NRFUTIL_URL} -O /tmp/nrfutil && \
    chmod +x /tmp/nrfutil && \
    /tmp/nrfutil --version && \
    nrfutil install nrf5sdk-tools && \
    chmod -R 777 ${NRFUTIL_HOME}

# =============================================================================

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]
