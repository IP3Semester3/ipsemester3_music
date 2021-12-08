FROM ubuntu:16.04

MAINTAINER Your Name "me"

RUN apt-get update && apt-get -y install python3 python3-pip
RUN apt-get -y upgrade 
WORKDIR /app

RUN pip3 install flask
RUN pip3 install requests


COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "python3", "-m" , "flask", "run" ]
