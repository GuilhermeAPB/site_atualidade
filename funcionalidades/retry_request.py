import requests
import asyncio
from utils import logger

async def retry_request(url, retries=3, delay=5):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, verify=False)  # Desabilita verificação SSL
            response.raise_for_status()  # Verifica se a resposta foi bem sucedida
            return response
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                logger.warning(f"Falha ao tentar acessar {url}. Tentando novamente... (Tentativa {attempt + 1}/{retries})")
                await asyncio.sleep(delay)  # Espera antes de tentar novamente
            else:
                logger.error(f"Falha ao acessar {url}. Erro: {e}")
                raise  # Relevanta o erro após o número máximo de tentativas
