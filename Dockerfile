FROM ubuntu:18.04

MAINTAINER Your Name "me"

RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y python3.6 python3-distutils python3-pip python3-apt
RUN apt-get update -y

WORKDIR /app

RUN python3 -v
RUN python3 -m pip install flask
RUN python3 -m pip install requests


COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]
