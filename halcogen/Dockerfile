FROM scottyhardy/docker-wine

RUN apt-get update && apt-get install -y curl unzip

RUN curl -L https://www.ti.com/lit/sw/spnc030g/spnc030g.zip --output spnc030g.zip && \
    unzip spnc030g.zip && \
    rm spnc030g.zip

ENV WINEARCH=win32

RUN xvfb-run -a wine "/HALCoGen-04.07.01-installer.exe" \
    --mode unattended --prefix "/opt/halcogen" \
    --disable-components SafetyLibrary \
    --install_desktop_shortcuts 0 && \
    wineserver -k

ADD run.sh /run.sh

RUN chmod +x /run.sh

ENTRYPOINT /run.sh