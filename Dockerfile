FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH=$PATH:/root/.local/bin

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --no-cache -r requirements.txt

COPY .env .
COPY start.sh .
COPY project .
