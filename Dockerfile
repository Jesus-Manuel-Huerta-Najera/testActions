FROM ubuntu:20.04

LABEL description = "Imagen "
LABEL mainteiner = "Jesus Manuel HN"
LABEL version = "0.1"

RUN apt-get update
RUN apt install -y python3
RUN apt install -y python3-pip 
RUN pip3 install pytest
