
# GENERATORS (yield)

# Generator = função que usa yield em vez de return
# Gera valores um a um, sob demanda (lazy evaluation)
# Não carrega tudo na memória de uma vez

# RETURN vs YIELD

# Com return → calcula tudo e retorna de uma vez
def quadrados_lista(n):
    resultado = []
    for i in range(n):
        resultado.append(i ** 2)
    return resultado   # lista inteira na memória

print(quadrados_lista(5))   # [0, 1, 4, 9, 16]

# Com yield → gera um valor por vez, pausa e espera o próximo next()
def quadrados_generator(n):
    for i in range(n):
        yield i ** 2   # pausa aqui, entrega o valor, retoma depois

gen = quadrados_generator(5)
print(gen)             # <generator object ...> → não executou ainda!
print(next(gen))       # 0
print(next(gen))       # 1
print(next(gen))       # 4

# Iterando com for (mais comum)
for valor in quadrados_generator(5):
    print(valor, end=" ")   # 0 1 4 9 16

# COMO YIELD FUNCIONA

def contar():
    print("Início")
    yield 1
    print("Depois do 1")
    yield 2
    print("Depois do 2")
    yield 3
    print("Fim")

gen = contar()

print(next(gen))   # Início → 1
print(next(gen))   # Depois do 1 → 2
print(next(gen))   # Depois do 2 → 3
# next(gen)        # Fim → StopIteration

# A função PAUSA no yield e RETOMA de onde parou!

# GENERATOR INFINITO

def contador_infinito(inicio=0, passo=1):
    atual = inicio
    while True:
        yield atual
        atual += passo

gen = contador_infinito(0, 2)

for i, valor in enumerate(gen):
    if i >= 5:
        break
    print(valor, end=" ")   # 0 2 4 6 8

# VANTAGEM: MEMÓRIA

import sys

# Lista → tudo na memória de uma vez
lista = [x ** 2 for x in range(100000)]
print(f"Lista: {sys.getsizeof(lista):,} bytes")    # ~800.000 bytes

# Generator → um item de cada vez
gen = (x ** 2 for x in range(100000))
print(f"Generator: {sys.getsizeof(gen)} bytes")    # ~200 bytes!

# Para um arquivo de 10GB, list explode a memória
# Com generator, processa linha por linha sem problemas

# YIELD FROM

# Delega para outro generator ou iterável
def generator_a():
    yield 1
    yield 2

def generator_b():
    yield 3
    yield 4

def combinado():
    yield from generator_a()
    yield from generator_b()
    yield from [5, 6, 7]   # funciona com qualquer iterável

for valor in combinado():
    print(valor, end=" ")   # 1 2 3 4 5 6 7

# EXEMPLOS REAIS

# Lendo arquivo enorme linha por linha
def ler_linhas(arquivo):
    with open(arquivo) as f:
        for linha in f:
            yield linha.strip()

# Processando dados em lotes (batch)
def em_lotes(iteravel, tamanho):
    lote = []
    for item in iteravel:
        lote.append(item)
        if len(lote) == tamanho:
            yield lote
            lote = []
    if lote:
        yield lote   # último lote que sobrou

dados = list(range(1, 12))
for lote in em_lotes(dados, 3):
    print(lote)
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# [10, 11]

# Pipeline de processamento (encadeando generators)
def ler_dados():
    yield from [10, -5, 20, -3, 15, 0, 8]

def filtrar_positivos(dados):
    for item in dados:
        if item > 0:
            yield item

def dobrar(dados):
    for item in dados:
        yield item * 2

# Encadeando: cada generator processa um por vez, sem listas intermediárias
pipeline = dobrar(filtrar_positivos(ler_dados()))

for valor in pipeline:
    print(valor, end=" ")   # 20 40 30 16