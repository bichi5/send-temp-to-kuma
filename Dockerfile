FROM python:3.11-slim

# Instala herramientas necesarias
RUN apt-get update && apt-get install -y \
    cron \
    snmp \
    curl \
    && apt-get clean

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN crontab crontab.txt
RUN touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log