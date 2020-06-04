FROM phusion/baseimage:0.11

# apt
RUN apt update
RUN apt upgrade -y

# nodejs, react
RUN apt install -y nodejs
RUN apt install -y npm
RUN npm install -g n
RUN n stable
RUN npm update -g npm
RUN npm install -g create-react-app
