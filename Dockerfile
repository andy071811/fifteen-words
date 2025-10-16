FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y nodejs npm curl

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/theme/static_src
RUN npm install

WORKDIR /app

ENTRYPOINT [ "./django-start.sh" ]