FROM debian:bullseye

RUN apt-get update && apt-get install -y \
    gnuradio \
    gr-iio \
    libiio-utils \
    gqrx-sdr \
    libgtk-3-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workdir

ENTRYPOINT ["gnuradio-companion"]