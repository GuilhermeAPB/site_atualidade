import requests
from bs4 import BeautifulSoup
import time
from funcionalidades.retry_request import retry_request
from funcionalidades.enviar_noticias import enviar_noticias
from utils import noticias_db, noticias_enviadas, logger

async def buscar_noticias(update, context):
    urls = [
        "https://agenciabrasil.ebc.com.br",
        "https://www12.senado.leg.br/noticias",
        "https://www.camara.leg.br/noticias",
        "https://folhapress.com.br"
    ]
    
    noticias = []

    for url in urls:
        try:
            response = await retry_request(url)  # Função de requisição com retentativa
            soup = BeautifulSoup(response.content, "html.parser")

            for item in soup.find_all("a"):
                title = item.get_text(strip=True)
                link = item.get("href")

                if link and not link.startswith('http'):
                    link = url + link  # Corrige links relativos

                if title and link and link not in noticias_enviadas and not any(ignored in title.lower() for ignored in ["fale conosco", "termos de uso", "política de privacidade", "desenvolvido por", "designed by"]):
                    noticia = {
                        "titulo": title,
                        "link": link,
                        "site": url.split("/")[2],  # Extrai o nome do site da URL
                        "data_hora": time.strftime("%Y-%m-%d %H:%M:%S"),
                        "status": "REGISTRADA",
                        "indice": len(noticias_db) + 1
                    }
                    noticias_db.append(noticia)
                    noticias_enviadas.add(link)  # Marca como já enviada
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao requisitar notícias de {url}: {e}")
            continue  # Tenta obter notícias de outros sites em caso de falha

    if noticias:
        await enviar_noticias(update)
    else:
        await update.message.reply_text("Desculpe, não consegui obter notícias no momento.")
