
'''

Headers são metadados que viajam junto com a requisição/resposta HTTP — não são o "conteúdo" em si, mas informações sobre como tratar aquele conteúdo:
formato, autenticação, cache, quem tá fazendo a chamada etc.

'''

# Headers mais comuns

# Content-Type: diz o formato do corpo da requisição/resposta (application/json)
# Authorization: carrega o token/credencial de autenticação
# Accept: diz que formato de resposta o cliente aceita receber
# User-Agent: identifica quem/o que está fazendo a requisição
# Cache-Control: Controla como a resposta pode ser cacheada

# Enviando headers com requests

import requests

header = {
    "Authorization": "Bearer meu_token_secreto",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

resposta = requests.get("https://api.exemplo.com/usuarios")
print(resposta.headers) # dict com todos os headers da resposta
print(resposta.headers["Content-Type"]) # application/json; charset=utf-8
print(resposta.headers.get("X-RateLimit"))  # None se não existir (mais seguro que [])

# Authorization - os dois formatos mais comuns

# Bearer token (o mais comum, usado em JWT, OAUth)
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIs..."}

# Basic Auth (usuário:senha em base64)
import base64

credenciais = base64.b64encode(b"usuario:senha").decode()
headers = {"Authorization": f"Basic {credenciais}"}

# Requests também tem um jeito nativo para Basic Auth, sem montar header na mão:
resposta = requests.get("https://api.exemplo.com/usuarios", auth=("usuario", "senha"))