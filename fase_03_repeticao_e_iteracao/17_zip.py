
# Zip em Python

# zip() combina dois ou mais iteráveis em pares
# Para quando precisa percorrer múltiplas listas ao mesmo tempo

# Básico
nomes = ["Miguel", "João", "Ana"]
idades = [30, 25, 28]

for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")

# Zip retorna tuplas
for par in zip(nomes, idades):
    print(par)
# ('Miguel', 30)
# ('João', 25)
# ('Ana', 28)

# Zip com 3 listas
nomes = ["Miguel", "João", "Ana"]
idades = [30, 25, 28]
cidades = ["Jundiaí", "São Paulo", "Campinas"]

for nome, idade, cidade in zip(nomes, idades, cidades):
    print(f"{nome}, {idade} anos, mora em {cidade}")

# Zip para no menor iterável
nomes = ["Miguel", "João", "Ana", "Carlos"]
idades = [30, 25, 28]  # só 3 idades

for nome, idade in zip(nomes, idades):
    print(f"{nome}: {idade}")
# Carlos é ignorado pois não tem idade correspondente

# zip_longest → usa o maior (preenche com None)
from itertools import zip_longest

for nome, idade in zip_longest(nomes, idades, fillvalue="N/A"):
    print(f"{nome}: {idade}")
# Carlos: N/A

#  Criando dicionário com zip
chaves = ["nome", "idade", "cidade"]
valores = ["Miguel", 30, "Jundiaí"]

dicionario = dict(zip(chaves, valores))
print(dicionario)
# {'nome': 'Miguel', 'idade': 30, 'cidade': 'Jundiaí'}

# Descompactando zip com *
pares = [("Miguel", 30), ("João", 25), ("Ana", 28)]
nomes, idades = zip(*pares)
print(nomes)   # ('Miguel', 'João', 'Ana')
print(idades)  # (30, 25, 28)

# Usos práticos

# Comparando duas listas
esperado = [10, 20, 30, 40]
resultado = [10, 21, 30, 39]

for i, (esperado, resultado) in enumerate(zip(esperado, resultado)):
    if esperado != resultado:
        print(f"Divergência no índice {i}: esperado {esperado}, obtido {resultado}")

# Calculando total por produto
produtos = ["Notebook", "Mouse", "Teclado"]
precos = [3500, 150, 250]
quantidades = [2, 5, 3]

for produto, preco, qtd in zip(produtos, precos, quantidades):
    total = preco * qtd
    print(f"{produto}: {qtd}x R${preco} = R${total}")
