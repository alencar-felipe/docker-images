ARG GNU_RM_VER=10.3-2021.10

FROM alencarfelipe/gnu-arm-embedded-toolchain:${GNU_RM_VER}-bullseye

# Other Tools =================================================================#

RUN apt-get update && apt-get install -y \
    cmake make stlink-tools usbutils openocd libncurses-dev

RUN ln -s /lib/x86_64-linux-gnu/libncurses.so.6 \
    /lib/x86_64-linux-gnu/libncurses.so.5 && \
    ln -s /lib/x86_64-linux-gnu/libtinfo.so.6 \
    /lib/x86_64-linux-gnu/libtinfo.so.5
    
# Execution Environment =======================================================#

ADD app.bash /app.bash

RUN chmod +x /app.bash && \
    mkdir -p /workdir /home/runtime && \
    echo "PS1=\"(stm32-dev) \$ \"" >> /etc/profile && \
    echo "cd /workdir" >> /etc/profile

WORKDIR /workdir

ENTRYPOINT /app.bash
