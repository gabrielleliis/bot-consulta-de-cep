import requests

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
