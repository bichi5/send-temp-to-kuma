import requests
from bs4 import BeautifulSoup
import re
import os

SOURCE_URL = os.getenv("SOURCE_URL")
KUMA_PUSH_URL = os.getenv("KUMA_PUSH_URL")
SENSOR_ID = os.getenv("SENSOR_ID")

def extract_temperature(html, sensor_id):
    soup = BeautifulSoup(html, 'html.parser')
    temp_div = soup.find('div', {'class': 'value', 'id': sensor_id})
    if temp_div:
        match = re.search(r"([\d\.]+)", temp_div.text)
        if match:
            return float(match.group(1))
    return None

def main():
    if not SOURCE_URL or not KUMA_PUSH_URL or not SENSOR_ID:
        print("Error: Variables de entorno no definidas.")
        return

    try:
        res = requests.get(SOURCE_URL, timeout=10)
        res.raise_for_status()
        temp = extract_temperature(res.text, SENSOR_ID)

        if temp is not None:
            payload = {
                'status': 'up',
                'msg': f'Temperatura_CPD_{SENSOR_ID}__{temp}°C'
            }
            kuma_res = requests.get(KUMA_PUSH_URL, params=payload, timeout=5)
            kuma_res.raise_for_status()
            print(f"{SENSOR_ID} enviada: {temp}°C")
        else:
            print(f"No se pudo extraer la temperatura del sensor {SENSOR_ID}.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()