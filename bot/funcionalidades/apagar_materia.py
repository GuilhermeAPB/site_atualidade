import logging

logger = logging.getLogger(__name__)

def apagar_materia(noticias_db, noticias_enviadas, indice):
    try:
        noticia = next((n for n in noticias_db if n["indice"] == indice), None)
        if noticia:
            noticias_db.remove(noticia)
            noticias_enviadas.remove(noticia["link"])
            logger.info(f"Matéria com índice {indice} apagada com sucesso.")
        else:
            logger.warning(f"Índice {indice} não encontrado.")
    except Exception as e:
        logger.error(f"Erro ao tentar apagar a matéria: {e}")
