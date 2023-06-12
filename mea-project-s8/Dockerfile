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
        libsndfile1-dev \
        gdb \
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

RUN git clone --branch maint-3.10 https://github.com/bastibl/gr-foo.git && \
    cd gr-foo && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make && \
    make install && \
    ldconfig && \
    cd ../.. && \
    rm -rf gr-foo

RUN git clone --branch maint-3.10 https://github.com/bastibl/gr-ieee802-15-4.git && \
    cd gr-ieee802-15-4 && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make && \
    make install && \
    ldconfig && \
    cd ../.. && \
    rm -rf gr-ieee802-15-4

USER jovyan

RUN pip3 install \
    pyadi-iio==0.0.14 \
    ipympl==0.9.3
