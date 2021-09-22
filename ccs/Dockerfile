FROM debian:buster-slim

RUN apt-get update && apt-get install -y libc6-i386 libusb-0.1-4 libgconf-2-4 libncurses5 libpython2.7 libtinfo5 libgtk-3-dev udev curl

RUN curl -L https://software-dl.ti.com/ccs/esd/CCSv10/CCS_10_4_0/exports/CCS10.4.0.00006_linux-x64.tar.gz --output /ccs.tar.gz

RUN tar -xvzf ccs.tar.gz && \
    mv /CCS*/ /CCS/ && \
    mv CCS/ccs_setup_* CCS/ccs_setup.run

RUN ./CCS/ccs_setup.run --mode unattended --prefix /opt

ADD run.sh /run.sh

RUN chmod +x /run.sh

ENTRYPOINT /run.sh