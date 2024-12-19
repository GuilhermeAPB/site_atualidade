from utils import noticias_db, noticias_enviadas

async def limpar_banco(update, context):
    noticias_db.clear()
    noticias_enviadas.clear()
    await update.message.reply_text("Todas as notícias foram limpas com sucesso.")
