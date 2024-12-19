import openai
import logging

logger = logging.getLogger(__name__)

async def reescrever_noticia(texto, tamanho_original):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Reescreva a seguinte notícia de forma mais clara e interessante, mantendo o tamanho do texto o mais próximo possível de {tamanho_original} caracteres:\n\n{texto}",
            max_tokens=tamanho_original // 4,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        logger.error(f"Erro ao reescrever a notícia: {e}")
        return texto