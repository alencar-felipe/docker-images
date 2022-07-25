ARG BASE_IMAGE

FROM $BASE_IMAGE

RUN apt-get update && apt-get install -y wget bzip2

ARG GNU_RM_VER

RUN wget https://developer.arm.com/-/media/Files/downloads/gnu-rm/\
${GNU_RM_VER}/gcc-arm-none-eabi-${GNU_RM_VER}-x86_64-linux.tar.bz2 \
-O gcc-arm-none-eabi-x86_64-linux.tar.bz2

RUN tar xjf gcc-arm-none-eabi-x86_64-linux.tar.bz2 -C /usr/share/ && \
    rm gcc-arm-none-eabi-x86_64-linux.tar.bz2

RUN echo PATH=/usr/share/gcc-arm-none-eabi-${GNU_RM_VER}/bin/:${PATH} \
    >> /etc/profile