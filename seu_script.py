import os

# Acessando as chaves de API que foram passadas pelo GitHub Actions
telegram_api_key = os.getenv('TELEGRAM_API_KEY')
news_api_key = os.getenv('OPENAI_API_KEY')

print("Usando a chave do TELEGRAM:", telegram_api_key)
print("Usando a chave da OPENAI API:", news_api_key)
