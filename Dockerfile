FROM ubuntu:18.10

MAINTAINER Your Name "me"

RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip nginx
RUN pip3 install uwsgi

COPY ./ ./app
WORKDIR ./app

RUN pip3 install flask
RUN pip3 install requests


COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]