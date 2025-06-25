# 🧭 Kuma Temperature Pusher

Este proyecto lee la temperatura de un sensor expuesto en una página HTML y la envía cada minuto a un monitor tipo **Push** de [Uptime Kuma](https://github.com/louislam/uptime-kuma), permitiendo ver y graficar la temperatura en el dashboard.

La temperatura se extrae desde un `<div>` con un ID específico, como este:

```html
<div class="value" id="s3603">19.7 °C</div>
```

---

## 🚀 Características

- Extrae la temperatura desde una URL local (HTML).
- Envía el valor como `msg` al endpoint de Push de Kuma.
- Se ejecuta automáticamente cada minuto mediante `cron`.
- Corre en un contenedor Docker ligero.
- Totalmente configurable mediante un archivo `.env`.

---

## 📦 Requisitos

- Docker
- Docker Compose

---

## 🔧 Configuración

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
# URL de origen donde está expuesta la temperatura
SOURCE_URL=http://x.x.x.x/

# URL de Push monitor de Uptime Kuma (usa tu token)
KUMA_PUSH_URL=https://uptime.xxx/api/push/<sensor-code>

# ID del div del sensor dentro del HTML
SENSOR_ID=s3603
```

---

## ▶️ Uso

### 1. Clona el repositorio

```bash
git clone https://github.com/tuusuario/kuma-temp-pusher.git
cd kuma-temp-pusher
```

### 2. Edita el archivo `.env`

Coloca la URL de origen, el token de tu monitor Push de Kuma, y el ID del sensor.

### 3. Ejecuta el contenedor

```bash
docker-compose up --build -d
```

El contenedor se encargará de leer la temperatura y enviarla a Kuma cada minuto.

---

## 🔍 Ver logs

Puedes ver los logs de ejecución con:

```bash
docker logs kuma-temp-pusher
```

---

## 🧪 Prueba manual

Si quieres probar el script fuera de cron, puedes ejecutar:

```bash
docker exec kuma-temp-pusher python3 /app/send_temp_to_kuma.py
```

---

## 🛑 Detener

```bash
docker-compose down
```

---

## 📜 Licencia

MIT. Usa este proyecto libremente bajo tu propio riesgo.

---

## 🤝 Créditos

Desarrollado con ❤️ para integrar datos de sensores en Uptime Kuma fácilmente.