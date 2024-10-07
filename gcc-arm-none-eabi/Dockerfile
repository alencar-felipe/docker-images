FROM debian:12

RUN apt-get update && apt-get install -y wget bzip2

ARG VERSION=10.3-2021.10
ARG URL=https://developer.arm.com/-/media/Files/downloads/gnu-rm/${VERSION}/gcc-arm-none-eabi-${VERSION}-x86_64-linux.tar.bz2

RUN wget ${URL} -O gcc-arm-none-eabi.tar.bz2

RUN tar xjf gcc-arm-none-eabi.tar.bz2 -C /usr/share/ && \
    rm gcc-arm-none-eabi.tar.bz2

RUN echo "PATH=/usr/share/gcc-arm-none-eabi-${VERSION}/bin/:${PATH}" \
    >> /etc/profile