FROM texlive/texlive:latest

RUN tlmgr update --self && \
    tlmgr install \
    collection-basic \
    collection-fontsrecommended \
    collection-langenglish \
    collection-latex \
    collection-latexrecommended \
    collection-latexextra \
    collection-bibtexextra \
    latexmk

WORKDIR /app

ENTRYPOINT ["latexmk"]
