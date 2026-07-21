
'''

Payload é o "corpo" (body) de uma requisição — os dados de verdade que você tá enviando ou recebendo, separado dos headers.
Em APIs modernas, o formato padrão desse payload é JSON. Python converte entre JSON (texto) e dict/list (estrutura nativa) usando o módulo json ou os métodos prontos do requests

'''

# JSON é texto (string), dict é uma estutura Python na memória

# JSON (texto/string)
'{"nome": "Miguel", "idade": 25, "ativo": true}'

# Dict Python (objeto)
{"nome": "Miguel", "idade": 25, "ativo": True}

# true JSON vira True (Python), null vira None

# Convertendo com módulo json

import json

dados = {"nome": "Miguel", "idade": 25, "idade": 25}

# dict -> JSON
texto_json = json.dumps(dados)
print(texto_json) # '{"nome": "Miguel", "idade": 25}'
print(type(texto_json)) # <class 'str'>

# JSON (string) -> dict
dados_de_volta = json.loads(texto_json)
print(dados_de_volta) # {'nome': 'Miguel', 'idade': 25}
print(type(dados_de_volta))  # <class 'dict'>

# json.dumps com formatação legível

dados = {"nome": "Miguel", "cursos": ["Python", "AWS", "SQL"]}

print(json.dumps(dados, indent=4, ensure_ascii=False))
# {
#     "nome": "Miguel",
#     "cursos": [
#         "Python",
#         "AWS",
#         "SQL"
#     ]
# }

# Payload na prática com requests
import requests

payload = {"nome": "Miguel", "email": "miguel@email.com"}

# "json=" já serializa o dit automaticamente
resposta = requests.post("https://api.exemplo.com/usuarios", json=payload)

# resposta.json() já desserializa automaticamente de volta pra dict
dados_resposta = resposta.json()
print(dados_resposta["id"]) # acessa como dict normal

# Lendo/salvando JSON de arquivo

# Salvar dict num arquivo .json
with open("dados.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

# Ler arquivo .json pra um dict

with open("dados.json", "r", encoding="utf-8") as arquivo:
    dado_lidos = json.load(arquivo)