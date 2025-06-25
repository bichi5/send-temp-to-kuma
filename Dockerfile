FROM python:3.11-slim

# Instalar cron y dependencias
RUN apt-get update && apt-get install -y cron

# Crear carpetas necesarias
WORKDIR /app

# Copiar archivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY send_temp_to_kuma.py .
COPY crontab.txt .

# Copiar el crontab
RUN crontab crontab.txt

# Crear log
RUN touch /var/log/cron.log

# Iniciar cron en foreground
CMD cron && tail -f /var/log/cron.log