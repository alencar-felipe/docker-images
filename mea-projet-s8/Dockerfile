FROM jupyter/scipy-notebook:2023-02-20

USER root

RUN apt-get update && \
    apt-get install -y \
        build-essential \
        git \
        libxml2-dev \
        bison \
        flex \
        libcdk5-dev \
        cmake \
        libusb-1.0-0-dev \
        libavahi-client-dev \
        libavahi-common-dev \
        libaio-dev \
        libgtk-3-dev \
        gnuradio \
        gqrx-sdr \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN git clone --branch v0.23 https://github.com/analogdevicesinc/libiio.git && \
    cd libiio && \
    mkdir build && \
    cd build && \
    cmake -DPYTHON_BINDINGS=ON .. && \
    make -j$(nproc) && \
    make install && \
    ldconfig && \
    cd ../.. && \
    rm -rf libiio

RUN git clone https://github.com/analogdevicesinc/libad9361-iio.git && \
    cd libad9361-iio && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make -j$(nproc) && \
    make install && \
    cd ../.. && \
    rm -rf libad9361-iio

USER jovyan

RUN pip3 install \
    pyadi-iio==0.0.14 \
    ipympl==0.9.3