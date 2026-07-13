
'''
JSON é o formato mais usado pra trocar dados entre sistemas, APIs,
arquivos de configuração, bancos NoSQL.
Em Python, JSON vira dicionário e dicionário vira JSON.
'''

# String JSON -> Dict Python: json.loads()
# Dict Python -> String JSON: json.dumps()
# arquivo JSON -> Dict Python: json.load()
# Dict Python -> arquivo JSON: json.dump()

import json

# dict -> string JSON

usuario = {"nome": "Miguel", "email": "zzz@gmail.com", "ativo": True}

json_str = json.dumps(usuario)
print(json_str)

json_dict = json.loads(json_str)
print(json_dict)


# Salvando em arquivo

with open("arquivo.txt", "w") as f:
    json.dump(usuario, f) #

# Lendo de arquivo
with open("arquivo.txt", "r") as f:
    dados = json.load(f)

# Dicas
# json.dump(usuario, f, indent=4 -> deixa o JSON legível ao salvar

# json.dumps(usuario, ensure_ascii=False) -> preserva acentos