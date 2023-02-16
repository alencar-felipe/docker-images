FROM texlive/texlive:latest

RUN apt-get update && apt-get install -y libxaw7

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
