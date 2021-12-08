FROM python:3.8-slim-buster

MAINTAINER Your Name "me"

WORKDIR /python-docker

RUN python3 -v
RUN python3 -m pip install flask
RUN python3 -m pip install requests

COPY . .

CMD [ "python3", "-m", "flask", "run" ]
