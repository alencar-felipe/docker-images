FROM debian:buster-slim

ENV WINEARCH=win32
ENV WINEPREFIX=/wine
ENV WINEDLLOVERRIDES="mscoree="

RUN dpkg --add-architecture i386

RUN apt-get update && apt-get install -y curl gnupg software-properties-common cabextract

RUN curl -L https://dl.winehq.org/wine-builds/Release.key | apt-key add - && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 76F1A20FF987672F DFA175A75104960E && \
    apt-add-repository 'deb http://dl.winehq.org/wine-builds/debian/ buster main' && \
    apt-add-repository 'deb https://download.opensuse.org/repositories/Emulators:/Wine:/Debian/xUbuntu_18.04/ ./'
    

RUN apt-get update && apt-get install -y winehq-stable \
    xvfb psmisc 

ENV PATH="/opt/wine-stable/bin/:${PATH}"

RUN curl -L https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks --output /usr/local/bin/winetricks && \
    chmod +x /usr/local/bin/winetricks 

#RUN xvfb-run winetricks --unattended dotnet20

ARG WINE_GECKO_VERSION="2.40"

RUN mkdir -p $WINEPREFIX/share/wine/gecko && \
    curl -L https://dl.winehq.org/wine/wine-gecko/2.40/wine-${WINE_GECKO_VERSION}-x86.msi \
    --output $WINEPREFIX/share/wine/gecko/wine-gecko-${WINE_GECKO_VERSION}-x86.msi

#    xvfb-run -a wine msiexec /i $WINEPREFIX/share/wine/gecko/wine-gecko-2.40-x86.msi && \
#    killall Xvfb

#RUN xvfb-run wine wineboot --init 

ARG WINE_MONO_VERSION="5.1.1"

RUN mkdir -p $WINEPREFIX/share/wine/mono && \ 
    curl -L https://dl.winehq.org/wine/wine-mono/${WINE_MONO_VERSION}/wine-mono-${WINE_MONO_VERSION}-x86.msi \
    --output $WINEPREFIX/share/wine/mono/wine-mono-${WINE_MONO_VERSION}-x86.msi
    
#RUN xvfb-run winetricks --unattended dotnet20 dotnet40 && \
#    killall Xvfb

