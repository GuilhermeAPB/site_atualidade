import nest_asyncio
import asyncio
from telegram.ext import Application, CommandHandler
from bot.news_fetcher import buscar_noticias
from bot.rewriter import reescrever_noticia
from bot.telegram_bot import enviar_noticias, reescrever
from config import TELEGRAM_API_KEY, OPENAI_API_KEY
import openai
from bot.handlers import setup_handlers

from funcionalidades.buscar_noticias import buscar_noticias
from funcionalidades.retry_request import retry_request
from funcionalidades.reescrever_noticia import reescrever_noticia
from funcionalidades.limpar_banco import limpar_banco
from funcionalidades.apagar_materia import apagar_materia
from funcionalidades.enviar_noticias import enviar_noticias

# Aplica o ajuste para o loop de eventos no Google Colab
nest_asyncio.apply()

openai.api_key = OPENAI_API_KEY

# Função principal para rodar o bot
async def main():
    application = Application.builder().token(TELEGRAM_API_KEY).build()

    setup_handlers(application)

    # Iniciar o bot
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
