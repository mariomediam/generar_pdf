# syntax=docker/dockerfile:1
FROM python:3.11.1


RUN echo "********************* wkhtmltopdF *********************"


# install wkhtmltopdF
RUN apt-get update && \
    apt-get install -y \
    wkhtmltopdf \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code/backend
COPY requirements.txt /code/backend/
RUN pip install -r requirements.txt
COPY . /code/backend