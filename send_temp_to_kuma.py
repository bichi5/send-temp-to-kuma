import os
import subprocess
import re
from dotenv import load_dotenv
import requests

load_dotenv("/app/.env")

KUMA_PUSH_URL = os.getenv("KUMA_PUSH_URL")
SNMP_HOST = os.getenv("SNMP_HOST")
SNMP_COMMUNITY = os.getenv("SNMP_COMMUNITY")
SNMP_OID = os.getenv("SNMP_OID")

def get_temperature():
    try:
        result = subprocess.run(
            ["snmpget", "-v", "2c", "-c", SNMP_COMMUNITY, SNMP_HOST, SNMP_OID],
            capture_output=True, text=True, timeout=10
        )
        match = re.search(r'STRING:\s+"([\d.]+)"', result.stdout)
        if match:
            return float(match.group(1))
    except Exception as e:
        print(f"Error ejecutando SNMP: {e}")
    return None

def main():
    if not (KUMA_PUSH_URL and SNMP_HOST and SNMP_COMMUNITY and SNMP_OID):
        print("Error: Variables de entorno no definidas.")
        return

    temp = get_temperature()
    if temp is not None:
        payload = {
            "status": "up",
            "msg": f"Temperatura CDC: {temp}°C"
        }
        try:
            res = requests.get(KUMA_PUSH_URL, params=payload, timeout=5)
            res.raise_for_status()
            print(f"Temperatura enviada: {temp}°C")
        except Exception as e:
            print(f"Error enviando a Kuma: {e}")
    else:
        print("No se pudo obtener la temperatura por SNMP.")

if __name__ == "__main__":
    main()