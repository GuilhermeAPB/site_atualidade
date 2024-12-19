from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from funcionalidades.buscar_noticias import buscar_noticias
from funcionalidades.reescrever_noticia import reescrever
from funcionalidades.limpar_banco import limpar_banco
from funcionalidades.apagar_materia import apagar_materia
from funcionalidades.enviar_noticias import enviar_noticias_continuamente
from funcionalidades.ajuda import ajuda

async def main():
    application = Application.builder().token("SEU_TOKEN_AQUI").build()

    # Handlers de comandos
    application.add_handler(CommandHandler("start", buscar_noticias))  # Iniciar ao enviar o comando /start
    application.add_handler(CommandHandler("buscar", buscar_noticias))
    application.add_handler(CommandHandler("reescreva", reescrever))
    application.add_handler(CommandHandler("limpar", limpar_banco))
    application.add_handler(CommandHandler("apagar", apagar_materia))
    application.add_handler(CommandHandler("ajuda", ajuda))

    # Iniciar o envio contínuo de notícias
    application.job_queue.run_repeating(enviar_noticias_continuamente, interval=600, first=0)

    # Executar o bot
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
