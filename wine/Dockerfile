FROM debian:bullseye

RUN dpkg --add-architecture i386

RUN apt-get update && apt-get install -y curl gnupg software-properties-common \
    cabextract

RUN curl -L https://dl.winehq.org/wine-builds/Release.key | apt-key add - && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys \
    76F1A20FF987672F DFA175A75104960E && \
    echo "deb https://dl.winehq.org/wine-builds/debian/ bullseye main" > \
    /etc/apt/sources.list.d/winehq.list
    
RUN apt-get update && apt-get install -y winehq-stable fonts-wine

WORKDIR /work