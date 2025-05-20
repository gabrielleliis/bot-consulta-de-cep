import requests
from telegram import Update
from telegram.ext import ContextTypes

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
