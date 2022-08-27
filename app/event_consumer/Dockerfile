FROM python:3.8-buster

WORKDIR /opt/event_consumer
ADD ./ ./
RUN pip install -r requirement.txt

ENTRYPOINT python main.py