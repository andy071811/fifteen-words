FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

RUN apt update

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

ENTRYPOINT [ "./django-start.sh" ]