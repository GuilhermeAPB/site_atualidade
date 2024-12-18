import nest_asyncio
import asyncio
from telegram.ext import Application, CommandHandler
from bot.news_fetcher import buscar_noticias
from bot.rewriter import reescrever_noticia
from bot.telegram_bot import enviar_noticias, reescrever
from config import TELEGRAM_API_KEY, OPENAI_API_KEY
import openai

# Aplica o ajuste para o loop de eventos no Google Colab
nest_asyncio.apply()

openai.api_key = OPENAI_API_KEY

# Função principal para rodar o bot
async def main():
    application = Application.builder().token(TELEGRAM_API_KEY).build()

    # Handlers de comandos
    application.add_handler(CommandHandler("start", buscar_noticias))  # Iniciar ao enviar o comando /start
    application.add_handler(CommandHandler("buscar", buscar_noticias))
    application.add_handler(CommandHandler("reescreva", reescrever))

    # Iniciar o bot
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
