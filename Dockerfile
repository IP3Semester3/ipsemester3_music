FROM ubuntu:20.04

MAINTAINER Your Name "me"

RUN apt-get update && \
    apt-get install software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    # Install py39 from deadsnakes repository
    apt-get install python3-9 && \
    # Install pip from standard ubuntu packages
    apt-get install python3-pip
    
WORKDIR /app

RUN python3.9 -v
RUN python3.9 -m pip install flask
RUN python3.9 -m pip install requests


COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]
