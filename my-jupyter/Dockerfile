FROM jupyter/scipy-notebook:2023-02-20

USER root

RUN apt-get update && \
    apt-get install -y \
        ghostscript \
        texlive-latex-extra \
        cm-super \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER jovyan

RUN pip3 install \
    lcapy==1.12 \
    deap==1.3.3 