FROM python:3.10-slim

RUN apt-get update && apt-get install -y curl
RUN pip install scikit-learn datetime evidently

RUN df -h

RUN mkdir -p /scikit_learn_data/openml
RUN chmod 775 /scikit_learn_data/openml -R 



