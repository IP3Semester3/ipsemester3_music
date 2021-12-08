FROM ubuntu:20.04

MAINTAINER Your Name "me"

RUN apt-get install python3
    apt-get install python3-pip
    apt-get update -y && \
    apt-get install -y python-pip python-dev
WORKDIR /app

RUN python -m pip install flask
RUN python -m pip install requests


COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]
