FROM debian:buster-slim

RUN apt-get update && apt-get install -y doxygen graphviz

ADD run.sh /run.sh

RUN chmod +x /run.sh

RUN mkdir -p /home/runtime/data

WORKDIR /home/runtime/data

ENTRYPOINT ["/run.sh"]