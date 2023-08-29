FROM python:3.10-slim

RUN apt-get update && apt-get install -y curl
RUN pip install scikit-learn datetime evidently

RUN mkdir /app
WORKDIR /app




