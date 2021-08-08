FROM ubuntu:20.04

LABEL description = "Imagen "
LABEL mainteiner = "Jesus Manuel HN"
LABEL version = "0.1"

RUN apt-get update
RUN apt-get install -y python3
