
'''

Conceito:
equests é a biblioteca mais usada em Python pra fazer chamadas HTTP — consumir APIs, enviar dados, baixar arquivos.
Ela vem embrulhando toda a complexidade de sockets/conexão numa API simples de usar.

'''
from asyncio import timeout

# Instalação: pip install requests

# Get básico

import requests

resposta = requests.get("https://api.exemplo.com/usuarios")

print(resposta.status_code) # 200
print(resposta.text) # corpo da resposta como string
print(resposta.json())  # corpo da resposta já convertido pra dict/list

# Get com parâmetros na URL (query params)

# em vez de montar a strint na mão, passa um dict em "params"
resposta = requests.get("https://api.exemplo.com/usuarios",
                        params={"idade_min": 18, "cidade": "Jundiaí"})

# vira: https://api.exemplo.com/usuarios?idade_min=18&cidade=Jundiai

print(resposta.url) # mostra a URL final montada

# Post enviando JSON

novo_usuario = {"nome": "Miguel", "idade": 35}

resposta = requests.post("https://api.exemplo.com/usuarios", json=novo_usuario)
# "json=" já serializa o dict e seta o header Content-Type certo

print(resposta.status_code) # 201
print(resposta.json())  # resposta da API, geralmente o recurso criado

# Tratando erro de conexão

try:
    resposta = requests.get("https://api.exemplo.com/usuarios", timeout=5)
    resposta.raise_for_status() # lança erro se status for 4xx/5xx

except requests.exceptions.Timeout:
    print("A API demorou mais pra responder")

except requests.exceptions.ConnectionError:
    print("Não consegui conectar na API")

except requests.exceptions.HTTPError as erro:
    print(f"Erro HTTP: {erro}")

# Sessions - reaproveitando conexão

sessao = requests.Session()
sessao.headers.update({"Authorization": "Bearer meu_token"})

# agora toda requisição feita com "sessao" já manda esse header automaticamente
resposta = sessao.get("https://api.exemplo.com/usuarios")

