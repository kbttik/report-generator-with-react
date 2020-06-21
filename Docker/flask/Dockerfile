
# FROM phusion/baseimage:0.11
FROM python:3.8.1-slim

# apt
RUN apt update
RUN apt upgrade -y

# java & python3
#RUN apt install -y --no-install-recommends openjdk-8-jdk python3-dev python3-pip
RUN pip install -U pip
RUN pip install -U setuptools
RUN pip install flask

#COPY flask-receiver/src/app.py app.py
COPY flask-receiver/requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN echo $PATH
RUN which python

EXPOSE 5000
# CMD ["flask", "run", "--host", "0.0.0.0", "--port", "80"]
#CMD ["python", "app.py"]
