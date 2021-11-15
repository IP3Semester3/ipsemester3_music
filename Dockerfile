# init a base image (Alpine is small Linux distro)
FROM python:3.6.1-alpine
# define the present working directory
WORKDIR /docker-flask-test
# copy the contents into the working dir
ADD . /docker-flask-test
# run pip to install the dependencies of the flask app
RUN python -m pip install --upgrade pip
RUN python -m pip install flask
RUN python -m pip install requests
# define the command to start the container
CMD ["python","-m","flask","run"]