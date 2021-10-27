# ================================== BUILDER ===================================


FROM ubuntu
FROM python:3.9-bullseye AS builder

RUN apt-get update

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["tail", "-f", "/dev/null"]