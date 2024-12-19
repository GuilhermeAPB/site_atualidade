from telegram.ext import CommandHandler
from bot.utils import buscar_noticias, reescrever, limpar_banco, apagar_materia

def setup_handlers(application):
    application.add_handler(CommandHandler("start", buscar_noticias))   # Iniciar ao enviar o comando /start
    application.add_handler(CommandHandler("buscar", buscar_noticias))
    application.add_handler(CommandHandler("reescreva", reescrever))
    application.add_handler(CommandHandler("limpar", limpar_banco))
    application.add_handler(CommandHandler("apagar", apagar_materia))
