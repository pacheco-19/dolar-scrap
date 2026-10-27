import requests
from bs4 import BeautifulSoup

URL = "https://www.dolar-scraping.docker.sulbaranjc.com/"

def obtener_valor() -> str:
    #1. Descargar el HTML que sirve la página local.
    respuesta = requests.get(URL, timeout=5)
    respuesta.raise_for_status()

    #2. Buscar el elemento que contiene el cambio destacado.
    sopa = BeautifulSoup(respuesta.text, "html.parser")
    elemento = sopa.find(id="usd-eur-rate")
    if elemento is None:
        raise ValueError("No se encontró el elemento con id 'usd-eur-rate'.")

    #3. Devolver solo el texto del valor, sin etiquetas HTML.
    return elemento.get_text(strip=True)

if __name__ == "__main__":
    try:
        print(f"1 USD = {obtener_valor()} EUR")
    except (requests.RequestException, ValueError) as error:
        print(f"No se pudo obtener el cambio: {error}")
        raise SystemExit(1)