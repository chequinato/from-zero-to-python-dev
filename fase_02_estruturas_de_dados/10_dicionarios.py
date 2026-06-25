
# Dicionários em Python

# Dicionário é uma coleção de pares chave:valor
# Ordenado (Python 3.7+), mutável, chaves únicas

vazio = {}
cliente = {
    "nome": "Miguel",
    "idade": 26,
    "ativo": True,
    "saldo": 3000
}

print(cliente)
print(vazio)
print(type(cliente))
print(len(cliente))

print(cliente["nome"])
print(cliente["idade"])
print(cliente["ativo"])
print(cliente["saldo"])

# get() → mais seguro, não gera erro se a chave não existir

print(cliente.get("idade"))
print(cliente.get("nome"))
print(cliente.get("ativo"))

print(cliente.get("Email", "N/A"))

# Modificando valores
cliente["idade"] = 31
print(cliente["idade"])  # 31

# Adicionando novas chaves
cliente["email"] = "miguel@email.com"
cliente["cidade"] = "São Paulo"
print(cliente)

cliente["endereço"] = "Rua abc"
print(cliente)

# Removendo chaves
del cliente["cidade"]
print(cliente)

removido = cliente.pop("email")   # remove e retorna o valor
print(removido)   # miguel@email.com
print(cliente)

# update() → atualiza com outro dicionário
cliente.update({"cidade": "Jundiaí", "telefone": "11-99999-9999"})
print(cliente)

# Métodos essenciais

produto = {
    "nome": "Notebook",
    "preco": 3500.00,
    "estoque": 10,
    "categoria": "Eletrônicos"
}

# keys() → todas as chaves
print(produto.keys())
# dict_keys(['nome', 'preco', 'estoque', 'categoria'])

# values() → todos os valores
print(produto.values())
# dict_values(['Notebook', 3500.0, 10, 'Eletrônicos'])

# items() → pares chave/valor
print(produto.items())
# dict_items([('nome', 'Notebook'), ('preco', 3500.0), ...])

# Iterando sobre dicionário

for chave in produto.values():
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, valor)

# in → verificando se chave existe
print("nome" in produto)      # True
print("desconto" in produto)  # False

# setdefault() → define valor se chave não existir
produto.setdefault("desconto", 0)
print(produto["desconto"])  # 0

produto.setdefault("nome", "Outro")  # não muda, já existe
print(produto["nome"])  # Notebook

# copy() → cópia independente
original = {"a": 1, "b": 2}
copia = original.copy()
copia["c"] = 3
print(original)  # {"a": 1, "b": 2} → não afetado
print(copia)

# Dicionários aninhados
usuarios = {
    "miguel": {
        "email": "miguel@email.com",
        "perfil": "admin",
        "ativo": True
    },
    "joao": {
        "email": "joao@email.com",
        "perfil": "editor",
        "ativo": False
    }
}

print(usuarios)
print(usuarios["miguel"])
print(usuarios["miguel"]["email"])   # miguel@email.com
print(usuarios["joao"]["perfil"])    # editor

# Iterando dicionário aninhado
for usuario, dados in usuarios.items():
    print(f"Usuário: {usuario}")
    for chave, valor in dados.items():
        print(f"  {chave}: {valor}")

# Padrões reais com dicionários

# Resposta de API (JSON vira dicionário)
resposta_api = {
    "status": 200,
    "data": {
        "id": 1,
        "nome": "Miguel",
        "permissoes": ["ler", "escrever", "deletar"]
    },
    "erro": None
}

print(resposta_api["status"])
print(resposta_api["data"]["nome"])
print(resposta_api["data"]["permissoes"])

# Verificação segura com get() encadeado
nome = resposta_api.get("data", {}).get("nome", "desconhecido")
print(nome)  # Miguel

# Teste 2
resposta_api2 = {
    "status": 400,
    "data": {
        "id": 2,
        "nome": "Guilherme",
        "permissoes": ["ler", "escrever", "deletar"]
    },
    "erro": None
}

nome = resposta_api2.get("data", {}).get("nome", "usuário desconhecido")
print(nome)  # Guilherme
resposta_api3 = {}
