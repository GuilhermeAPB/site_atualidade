from utils import noticias_db, logger

async def enviar_noticias(update):
    noticias = noticias_db[-5:]  # Pegando as últimas 5 notícias

    # Enviar cada notícia separada com um layout mais organizado
    for noticia in noticias:
        news_message = (
            f"<pre>"
            f"+---------------------------------------------------------------+\n"
            f"| <b>Índice</b>   | {noticia['indice']}                                              |\n"
            f"| <b>Site</b>     | {noticia['site']}                                              |\n"
            f"| <b>Título</b>   | {noticia['titulo']}                                           |\n"
            f"| <b>Link</b>     | {noticia['link']}                                           |\n"
            f"| <b>Data/Hora</b>| {noticia['data_hora']}                                      |\n"
            f"+---------------------------------------------------------------+"
            f"</pre>"
        )

        # Envia a mensagem formatada
        try:
            await update.message.reply_text(news_message, parse_mode='HTML', disable_web_page_preview=True)
        except Exception as e:
            logger.error(f"Erro ao enviar notícia: {e}")
            await update.message.reply_text("Ocorreu um erro ao tentar enviar as notícias. Tente novamente mais tarde.")
