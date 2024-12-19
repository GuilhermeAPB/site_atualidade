from utils import noticias_db, noticias_enviadas

async def apagar_materia(update, context):
    try:
        indice = int(context.args[0])
        noticia = next((n for n in noticias_db if n["indice"] == indice), None)

        if noticia:
            noticias_db.remove(noticia)
            noticias_enviadas.remove(noticia["link"])
            await update.message.reply_text(f"A matéria com índice {indice} foi apagada com sucesso.")
        else:
            await update.message.reply_text("Índice inválido ou a notícia não foi encontrada.")
    except ValueError:
        await update.message.reply_text("Por favor, forneça um número válido para o índice da notícia.")
