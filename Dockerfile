FROM python:3.8

RUN apt-get update && apt-get install -y make nginx tidy
RUN pip install --upgrade pip
RUN pip install pyyaml pytidylib

ENV PROJECT 20200530-quiz

WORKDIR /opt/${PROJECT}

WORKDIR /opt/${PROJECT}
COPY ${PROJECT} /opt/${PROJECT}
COPY docker-config/default /etc/nginx/sites-available/default
COPY docker-config/bashrc /root/.bashrc
