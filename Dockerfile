# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .  

CMD [ "python", "manage.py", "runserver"]
