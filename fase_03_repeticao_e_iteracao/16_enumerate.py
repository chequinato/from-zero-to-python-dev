
# Enumerate em Python

# enumerate() retorna o índice E o valor ao mesmo tempo
# Evita o padrão de usar range(len(lista))

# Problema sem enumerate
frutas = ["maçã", "banana", "uva", "manga"]

# Jeito ruim
for i in range(len(frutas)):
    print(f"{i}: {frutas[i]}")

# Com enumerate
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")

# Começando o índice em 1
for i, fruta in enumerate(frutas, start=1):
    print(f"{i}: {fruta}")
# 1: maçã
# 2: banana
# 3: uva
# 4: manga

# Enumerate retorna tuplas
for item in enumerate(frutas):
    print(item)

# Usos práticos
# Numerar itens de um menu
opcoes = ["Criar conta", "Fazer login", "Recuperar senha", "Sair"]

print("=== MENU ===")
for i, opcao in enumerate(opcoes, start=1):
    print(f"{i}: {opcao}")

# Encontrar índice de um item específico
nomes = ["Ana", "Carlos", "Miguel", "João"]
print(nomes)

for i, nome in enumerate(nomes):
    if nome == "Miguel":
        print(f"Miguel está no índice {i}")
        break

# Modificar lista com base no índice
precos = [100, 200, 300, 400]

for i, preco in enumerate(precos):
    if preco > 150:
        precos[i] = preco * 0.9  # aplica 10% de desconto

print(precos)  # [100, 180.0, 270.0, 360.0]

# Enumerate com string
for i, letra in enumerate("Python"):
    print(f"posição {i}: {letra}")

# Enumerate com dicionário
dados = {"nome": "Miguel", "idade": 30, "cidade": "Jundiaí"}

for i, (chave, valor) in enumerate(dados.items(), start=1):
    print(f"{i}. {chave}: {valor}")