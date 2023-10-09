FROM tensorflow/tensorflow:latest AS base
RUN pip install matplotlib panda
RUN apt-get update
RUN apt-get install libcairo2-dev -y
RUN pip install -r /backend/requirements.txt
EXPOSE 8000
