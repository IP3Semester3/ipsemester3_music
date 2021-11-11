FROM ubuntu:16.04

MAINTAINER Your Name "me"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
WORKDIR /app

RUN python3 -m pip install flask
RUN python3 -m pip install requests


COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]