FROM jupyter/scipy-notebook:2023-02-20

USER root

RUN apt-get update && \
    apt-get install -y \
        ghostscript \
        texlive-latex-extra \
        cm-super \
        build-essential \
        python3-dev \
        libcairo2-dev \
        libpango1.0-dev \ 
        ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER jovyan

RUN pip3 install \
    lcapy==1.12 \
    deap==1.3.3 \
    manim==0.17.2 