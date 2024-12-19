import requests
from bs4 import BeautifulSoup
import time
import logging

logger = logging.getLogger(__name__)

async def buscar_noticias():
    urls = [
        "https://agenciabrasil.ebc.com.br",
        "https://www12.senado.leg.br/noticias",
        "https://www.camara.leg.br/noticias",
        "https://folhapress.com.br"
    ]

    noticias = []

    for url in urls:
        try:
            response = await retry_request(url)
            soup = BeautifulSoup(response.content, "html.parser")

            for item in soup.find_all("a"):
                title = item.get_text(strip=True)
                link = item.get("href")

                if link and not link.startswith('http'):
                    link = url + link

                if title and link:
                    noticia = {
                        "titulo": title,
                        "link": link,
                        "site": url.split("/")[2],
                        "data_hora": time.strftime("%Y-%m-%d %H:%M:%S"),
                        "status": "REGISTRADA",
                        "indice": len(noticias) + 1
                    }
                    noticias.append(noticia)
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao requisitar notícias de {url}: {e}")
            continue

    return noticias
