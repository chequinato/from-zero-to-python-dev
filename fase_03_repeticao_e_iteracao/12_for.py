

# For em Python

# For percorre qualquer coisa iterável
# (lista, tupla, string, dicionário, set, range...)

# Iterando sobre lista

frutas = ["maçã", "banana", "uva", "manga"]

for fruta in frutas:
    print(fruta)

# Iterando sobre string
for letra in "Python":
    print(letra)

# Iterando sobre tupla
coordenadas = (10, 20, 30)

for valor in coordenadas:
    print(valor)

# Iterando sobre dicionário
cliente = {"nome": "Miguel", "idade": 30, "cidade": "Jundiaí"}

for chave in cliente:
    print(chave)

# Iterando sobre valores
for valor in cliente.values():
    print(valor)

# Iterando sobre chave e valor (mais comum)
for chave, valor in cliente.items():
    print(chave, valor)

# Iterando sobre set
permissoes = {"ler", "escrever", "deletar"}
for permissao in permissoes:
    print(permissao)  # sem ordem garantida

# For como acumulador (padrão usado)
numeros = [1, 2, 3, 4, 5]
total = 0

for numero in numeros:
    total += numero
print(f"Total: {total}")

# For com condicional dentro
numeros = [1, 2, 3, 4, 5]

pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(f"Pares: {pares}")

# For aninhado

times = ["Flamengo", "Palmeiras"]
jogadores = ["Miguel", "João", "Ana"]

for time in times:
    for jogador in jogadores:
        print(f"{jogador} jogou no {time}")

# Matriz (Lista de listas)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()

