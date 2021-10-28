FROM debian:buster-slim

RUN apt-get update && apt-get install -y curl p7zip-full alien libxinerama1 libgl1-mesa-glx

RUN curl -L https://download.ni.com/support/softlib/labview/labview_development_system/2021/lv2021community-linux.iso --output /labview-2020.iso

RUN mkdir -p /labview-iso && \
    7z x -o/labview-iso labview-2020.iso && \
    cd /labview-iso && \
    rm ni*i386.rpm && \
    alien -k -c *.rpm && \
    mkdir /usr/local/natinst/ && \
    chmod 755 /usr/local/natinst/ && \
    dpkg -i labview*.deb && \
    dpkg -i *.deb && \
    cd .. && \
    rm -r /labview-iso labview-2020.iso && \
    cd /

ADD run.sh /run.sh

RUN chmod +x /run.sh

WORKDIR /home/runtime

ENTRYPOINT /run.sh