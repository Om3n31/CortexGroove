FROM tensorflow/tensorflow:latest AS base
RUN pip install matplotlib panda
RUN apt-get update
RUN apt-get install libcairo2-dev -y
COPY . .
RUN pip install -r requirements.txt
CMD ["sleep", "infinity"]