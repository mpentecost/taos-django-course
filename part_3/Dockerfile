FROM python:3.7-stretch

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt