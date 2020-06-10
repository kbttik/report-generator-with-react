
FROM phusion/baseimage:0.11

# apt
RUN apt update
RUN apt upgrade -y --no-install-recommends

# java & python3
RUN apt install -y --no-install-recommends openjdk-8-jdk python3-dev python3-pip
RUN pip3 install -U pip
RUN pip3 install -U setuptools

