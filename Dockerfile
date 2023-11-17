FROM python:3.11.6-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt


COPY . /code/
