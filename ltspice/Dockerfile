FROM scottyhardy/docker-wine

RUN apt-get update && apt-get install -y curl

RUN curl -L https://ltspice.analog.com/software/LTspiceXVII.exe --output LTspiceXVII.exe && \
    chmod +x LTspiceXVII.exe

RUN mkdir -p /root/workdir

WORKDIR /root/workdir

ENTRYPOINT ["bash"]