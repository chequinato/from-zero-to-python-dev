
# Desempacotamento em Python

# Desempacotamento = extrair valores de uma coleção
# diretamente em variáveis separadas

# Básico

# Tuplas e listas
coordenada = (10, 20)
x, y = coordenada
print(x)  # 10
print(y)  # 20

pessoa = ["Miguel", 30, "Jundiaí"]

nome, idade, cidade = pessoa
print(nome)   # Miguel
print(idade)  # 30
print(cidade) # Jundiaí

# String
a, b, c = "ABC"
print(a)
print(b)
print(c)

# Swap de variáveis
x = "primeiro"
y = "segundo"

x, y = y, x # troca sem variável temporária
print(x) # segundo
print(y) # primeiro

# Operador * SPLAT
# Captura o "resto" em uma lista
primeiro, *resto = [1, 2, 3, 4, 5]
print(primeiro)  # 1
print(resto)     # [2, 3, 4, 5]

*inicio, ultimo = [1, 2, 3, 4, 5]
print(inicio)   # [1, 2, 3, 4]
print(ultimo)   # 5

primeiro, *meio, ultimo = [1, 2, 3, 4, 5]
print(primeiro)  # 1
print(meio)      # [2, 3, 4]
print(ultimo)    # 5

# Ignorando valores com _
primeiro, _, terceiro = [10, 20, 30]
print(primeiro)  # 10
print(terceiro)  # 30

# Ignorando múltiplos valores
primeiro, *_ = [1, 2, 3, 4, 5]
print(primeiro)  # 1

# Desempacotando em loops
pessoas = [("Miguel", 30), ("João", 25), ("Ana", 28)]

for nome, idade in pessoas:
    print(f"{nome}: {idade} anos")

# Dicionário com items()
produto = {"nome": "Notebook", "preco": 3500, "estoque": 10}

for chave, valor in produto.items():
    print(f"{chave} → {valor}")

# Lista de dicionários (padrão API real)
usuarios = [
    {"nome": "Miguel", "perfil": "admin"},
    {"nome": "João",   "perfil": "editor"},
    {"nome": "Ana",    "perfil": "viewer"},
]

for usuario in usuarios:
    nome, perfil = usuario["nome"], usuario["perfil"]
    print(f"{nome}: {perfil}")

# Desempacotamento aninhado
dados = ("Miguel", (30, "Jundiaí"))
nome, (idade, cidade) = dados
print(nome)   # Miguel
print(idade)  # 30
print(cidade) # Jundiaí

# Usos reais

def minmax(lista):
    return min(lista), max(lista)

menor, maior = minmax([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Min: {menor}, Max: {maior}")

# Processando CSV simulado
linhas = [
    "Miguel,30,Jundiaí",
    "João,25,São Paulo",
    "Ana,28,Campinas"
]

for linha in linhas:
    nome, idade, cidade = linha.split(",")
    print(f"{nome} tem {idade} anos e mora em {cidade}")

# Desempacotamento com enumerate e zip juntos
nomes = ["Miguel", "João", "Ana"]
notas = [9.5, 7.0, 8.5]

for i, (nome, nota) in enumerate(zip(nomes, notas), start=1):
    print(f"{i}. {nome}: {nota}")

nomes = ["Miguel", "João", "Ana"]
notas = [9.5, 7.0, 8.5]
