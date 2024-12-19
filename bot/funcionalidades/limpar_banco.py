def limpar_banco(noticias_db, noticias_enviadas):
    noticias_db.clear()
    noticias_enviadas.clear()
    logger.info("Banco de notícias limpo.")
