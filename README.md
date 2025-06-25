# 🧭 Kuma Temperature Pusher (vía SNMP)

Este proyecto lee la temperatura de un dispositivo SNMP y la envía cada minuto a un monitor tipo **Push** de [Uptime Kuma](https://github.com/louislam/uptime-kuma). Esto permite visualizar la temperatura como si fuera latencia en el Dashboard de Kuma.

---

## 🌡️ ¿Cómo funciona?

Consulta periódica vía SNMP:

```bash
snmpget -v 2c -c public 172.16.11.254 1.3.6.1.4.1.21796.4.9.3.1.4.1
```

Devuelve algo como:

```
iso.3.6.1.4.1.21796.4.9.3.1.4.1 = STRING: "19.8"
```

El valor `"19.8"` se envía a Kuma como `msg` y `ping`, para mostrarlo y graficarlo.

---

## 📦 Requisitos

- Docker
- Docker Compose
- Un dispositivo que exponga temperatura por SNMP

---

## 🔧 Configuración

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
# URL del monitor Push de Uptime Kuma
KUMA_PUSH_URL=https://uptime.xxxxxx.com/api/push/<id>

# Configuración SNMP
SNMP_HOST=x.x.x.x
SNMP_COMMUNITY=public
SNMP_OID=1.3.6.1.4.1.21796.4.9.3.1.4.1
```

---

## ▶️ Uso

### 1. Clona el repositorio

```bash
git clone https://github.com/tuusuario/kuma-temp-pusher.git
cd kuma-temp-pusher
```

### 2. Configura `.env` como se muestra arriba

### 3. Ejecuta el contenedor

```bash
docker-compose up --build -d
```

El script se ejecutará automáticamente cada minuto dentro del contenedor gracias a `cron`.

---

## 🔍 Ver logs

```bash
docker logs kuma-temp-pusher
```

También puedes ver directamente el contenido del log del cron:

```bash
docker exec kuma-temp-pusher cat /var/log/cron.log
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

Desarrollado por JMAM con ❤️ para integrar datos de sensores SNMP en Uptime Kuma de forma sencilla y automatizada.