# site_atualidade
Esse projeto está sendo desenvolvido para otimizar o tempo e automatizar o processo de busca e publicação de noticias em um site que fala sobre as atualidades no Brasil. 

---
site_atualidade/
│
├── funcionalidades/
│   ├── __init__.py
│   ├── buscar_noticias.py
│   ├── retry_request.py
│   ├── reescrever_noticia.py
│   ├── limpar_banco.py
│   ├── apagar_materia.py
│   ├── enviar_noticias.py
│
├── utils.py
├── main.py
├── requirements.txt
├── .env
├── README.md

---

# **Site Atualidade - Bot do Telegram**

Este projeto é um bot do Telegram que busca e reescreve notícias de fontes confiáveis. Ele utiliza a API do OpenAI para reescrever as notícias de forma mais clara e interessante.

---

## **Sumário**

- [Como configurar o ambiente](#como-configurar-o-ambiente)
- [Como rodar o bot](#como-rodar-o-bot)
- [Configuração de variáveis de ambiente](#configuração-de-variáveis-de-ambiente)
- [Dependências](#dependências)
- [Estrutura do projeto](#estrutura-do-projeto)

---

## **Como configurar o ambiente**

1. **Clonar o repositório**:
   Primeiro, clone o repositório do GitHub para o seu ambiente local.
   ```bash
   git clone https://github.com/GuilhermeAPB/site_atualidade.git
   cd site_atualidade
   ```

2. **Criar e ativar um ambiente virtual (recomendado)**:
   Criar um ambiente virtual é uma boa prática para garantir que as dependências não entrem em conflito com outros projetos.
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```

3. **Instalar as dependências**:
   Com o ambiente virtual ativado, instale as dependências listadas no `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Como rodar o bot**

1. **Configurar as chaves de API**:
   Antes de rodar o bot, você precisa configurar as chaves de API do Telegram e do OpenAI. Para garantir a segurança, essas chaves não devem ser armazenadas diretamente no código. Você pode definir essas chaves usando variáveis de ambiente.

2. **Definir as variáveis de ambiente**:
   Crie um arquivo `.env` no diretório raiz do projeto ou defina as variáveis de ambiente diretamente no seu terminal.

   Exemplo de arquivo `.env`:
   ```
   TELEGRAM_API_KEY_SECRET=seu_token_do_telegram
   OPENAI_API_KEY_SECRET=sua_chave_de_api_openai
   ```

   **Importante**: Substitua `seu_token_do_telegram` e `sua_chave_de_api_openai` pelos valores corretos.

3. **Rodar o bot**:
   Com as variáveis de ambiente configuradas, execute o arquivo `main.py` para iniciar o bot:
   ```bash
   python main.py
   ```

4. **Interagir com o bot**:
   - **Comando `/start`**: Inicia o bot e busca as últimas notícias.
   - **Comando `/buscar`**: Busca notícias e as envia para o chat.
   - **Comando `/reescreva`**: Reescreve uma notícia que foi enviada.

---

## **Configuração de variáveis de ambiente**

O bot utiliza duas chaves de API:

- **Telegram API Key**: Essa chave é fornecida pelo BotFather no Telegram. Ela é necessária para autenticar o bot e permitir que ele envie mensagens para os usuários.
- **OpenAI API Key**: A chave de API do OpenAI é usada para reescrever as notícias. Você pode obter sua chave em [https://platform.openai.com](https://platform.openai.com).

### **GitHub Secrets (para segurança)**

Caso você queira rodar o bot no GitHub Actions ou em outro ambiente de CI/CD, use **GitHub Secrets** para armazenar as chaves de API de forma segura:

1. No seu repositório GitHub, vá para **Settings** → **Secrets** → **New repository secret**.
2. Adicione duas variáveis:
   - `TELEGRAM_API_KEY_SECRET`: A chave de API do Telegram.
   - `OPENAI_API_KEY_SECRET`: A chave de API do OpenAI.

### **Uso com Docker (opcional)**

Se você preferir rodar o bot dentro de um container Docker, pode usar o arquivo `Dockerfile` incluído no repositório. Para isso, siga estas etapas:

1. **Construir a imagem Docker**:
   ```bash
   docker build -t telegram-bot .
   ```

2. **Rodar o container Docker**:
   ```bash
   docker run --env TELEGRAM_API_KEY_SECRET=seu_token_do_telegram --env OPENAI_API_KEY_SECRET=sua_chave_de_api_openai telegram-bot
   ```

---

## **Dependências**

Este projeto utiliza as seguintes bibliotecas:

- **python-telegram-bot**: Biblioteca para interação com a API do Telegram.
- **openai**: Biblioteca para interação com a API do OpenAI (para reescrever as notícias).
- **beautifulsoup4**: Biblioteca para parsing de HTML e extração de notícias.
- **requests**: Biblioteca para fazer requisições HTTP.

Todas as dependências estão listadas no arquivo `requirements.txt`. Para instalar todas as dependências, basta rodar:

```bash
pip install -r requirements.txt
```

---

## **Estrutura do projeto**

A estrutura do repositório está organizada da seguinte forma:

```
site_atualidade/
├── bot/
│   ├── __init__.py        # Marca o diretório como pacote Python
│   ├── news_fetcher.py    # Lógica para buscar as notícias
│   ├── rewriter.py        # Lógica para reescrever as notícias
│   └── telegram_bot.py    # Lógica de interação com o Telegram
├── requirements.txt       # Dependências do projeto
├── config.py              # Configuração das variáveis de ambiente
├── main.py                # Inicialização do bot
└── README.md              # Este arquivo
```

---

## **Contribuição**

Se você quiser contribuir para este projeto, basta fazer um **fork** do repositório, realizar as alterações e enviar um **pull request**. Se tiver sugestões ou melhorias, fique à vontade para abrir uma **issue**.

---

## **Licença**

Este projeto está licenciado sob a [MIT License](LICENSE).

---

