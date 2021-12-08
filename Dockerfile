FROM ubuntu:20.04

MAINTAINER Your Name "me"

WORKDIR /app

RUN python -v
RUN python3 -m pip install flask
RUN python3 -m pip install requests


COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]
