ARG BASE_IMAGE=alencarfelipe/riscv-gnu-toolchain:latest

FROM ${BASE_IMAGE}

RUN apt-get update && apt-get install -y \
    python3 python3-pip

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN pip install --no-cache-dir \
    Jinja2==3.1.2 \
    pyserial==3.5 \
    tqdm==4.64.0
    