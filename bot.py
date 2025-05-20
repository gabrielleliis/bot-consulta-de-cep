import requests
from telegram import Update
from telegram.ext import ContextTypes, ApplicationBuilder, CommandHandler, MessageHandler, filters

# Parte 1 — Função que busca o endereço
def buscar_endereco(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" in dados:
            return "CEP não encontrado."
        endereco = f"{dados['logradouro']}, {dados['bairro']} - {dados['localidade']}/{dados['uf']}"
        return endereco
    else:
        return "Erro ao consultar o CEP."

# Parte 2 — Função que responde mensagens com o CEP
async def responder_cep(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cep = update.message.text.strip()
    if len(cep) == 8 and cep.isdigit():
        resposta = buscar_endereco(cep)
    else:
        resposta = "Por favor, envie um CEP válido com 8 números."
    await update.message.reply_text(resposta)

# Parte 3 — Comando /start e inicialização do bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Fala! Me manda um CEP que eu te digo o endereço.")

def main():
    # Substitua pelo seu token oficial do BotFather
    app = ApplicationBuilder().token("COLE_SEU_TOKEN_AQUI").build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder_cep))

    print("Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
