import os

# Acessando as chaves de API que foram passadas pelo GitHub Actions
TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

print("Usando a chave do TELEGRAM:", TELEGRAM_API_KEY)
print("Usando a chave da OPENAI API:", OPENAI_API_KEY)
