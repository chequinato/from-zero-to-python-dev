
'''

HTTP methods (ou "verbos") indicam qual ação você quer fazer numa API.
Cada um tem uma intenção específica, e usar o verbo errado é um erro comum de quem tá começando com APIs.

GET - buscar/ler dados (buscar lista de usuários
POST - criar novo recurso (criar novo usuário
PUT - atualizar um recurso inteiro (substituir todos os dados de um usuário)
PATCH - atualizar parte de um recurso (mudar só o email de um usuário
DELETE - remover um recurso (deletar um usuário)

idempotência - Um método é "idempotente" quando chamar ele várias vezes seguidas dá o mesmo resultado que chamar uma vez.

GET, PUT, DELETE → idempotentes
Chamar DELETE /usuario/5 uma vez ou 10 vezes = mesmo resultado (usuário deletado)

POST → NÃO é idempotente
Chamar POST /usuario 3 vezes = cria 3 usuários diferentes!

'''

import requests

# GET - buscar dados:
resposta = requests.get('https://api.exemplo.com/usuarios')

# POST - criar dado novo
resposta = requests.post('https://api.exemplo.com/usuarios', json={'usuario': 'Miguel'})

# PUT - atualizar tudo
resposta = requests.put('https://api.exemplo.com/usuarios', json={"nome": "Miguel", "idade": 35})

# PATCH - atualizar só um campo
resposta = requests.patch('https://api.exemplo.com/usuarios', json={'idade': 36})

# DELETE - remover
resposta = requests.delete('https://api.exemplo.com/usuarios/1')

# Isso importa pois toda API REST segue essa lógica dos verbos.