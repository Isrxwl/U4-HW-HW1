import requests
import logging

logging.basicConfig(filename='errores.log', level=logging.ERROR)

def build_url(latitude, longitude, days=3):
    # Construye la URL completa con parámetros por defecto
    return f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min&timezone=America/Merida&forecast_days={days}"


def fetch_forecast(latitude, longitude, days=3):
    url = build_url(latitude, longitude, days)
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    return response.json()

def safe_fetch(latitude, longitude, days=3):
    try:
        return fetch_forecast(latitude, longitude, days)
    except requests.exceptions.HTTPError as e:
        logging.error(f"Error de estado HTTP: {e}")
        return None
    except requests.exceptions.Timeout as e:
        logging.error(f"Tiempo de espera agotado: {e}")
        return None
    except requests.exceptions.ConnectionError as e:
        logging.error(f"Falla de conexion: {e}")
        return None
    except Exception as e:
        # La excepción general va al final
        logging.error(f"Error inesperado: {e}")
        return None
    