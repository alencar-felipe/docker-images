FROM debian:bullseye

RUN apt-get update && apt-get install -y python3 python3-pip gnuplot octave \
    libffi-dev liboctave-dev

RUN pip3 install jupyter octave_kernel sympy==1.5.1

RUN octave --eval "pkg install -forge symbolic" && \
    octave --eval "pkg install -forge control" && \
    octave --eval "pkg install -forge signal"

RUN mkdir -p /home/runtime/ /notebooks/ && chmod 777 /home/runtime/ /notebooks/ 

ADD jupyter_notebook_config.py /home/runtime/.jupyter/jupyter_notebook_config.py

ADD run.sh /run.sh

RUN chmod +x /run.sh

WORKDIR /notebooks

ENTRYPOINT /run.sh
