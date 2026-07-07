# ITERATORS EM PYTHON

# Iterable  = objeto que PODE ser percorrido (lista, string, dict...)
# Iterator  = objeto que SABE qual é o próximo item (__next__)
# Todo iterator é iterable, mas nem todo iterable é iterator

# ENTENDENDO A BASE

# Por baixo dos panos, o for faz isso:
lista = [1, 2, 3]

iterator = iter(lista)         # cria o iterator com iter()
print(next(iterator))          # 1 → pega o próximo
print(next(iterator))          # 2
print(next(iterator))          # 3
# next(iterator)               # StopIteration → acabou!

# O for faz tudo isso automaticamente:
for item in lista:
    print(item)
# é equivalente ao while abaixo:
iterator = iter(lista)
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break

# CRIANDO SEU PRÓPRIO ITERATOR

# Precisa implementar __iter__ e __next__

class Contador:
    def __init__(self, inicio, fim):
        self.atual = inicio
        self.fim = fim

    def __iter__(self):
        return self   # o próprio objeto é o iterator

    def __next__(self):
        if self.atual > self.fim:
            raise StopIteration
        valor = self.atual
        self.atual += 1
        return valor

contador = Contador(1, 5)

for numero in contador:
    print(numero)   # 1 2 3 4 5

# Usando next() diretamente
contador = Contador(1, 3)
print(next(contador))   # 1
print(next(contador))   # 2
print(next(contador))   # 3
# print(next(contador)) # StopIteration

# ITERATOR INFINITO

class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        valor = self.a
        self.a, self.b = self.b, self.a + self.b
        return valor

fib = Fibonacci()

# Precisa de limite pois é infinito!
for i, numero in enumerate(fib):
    if i >= 10:
        break
    print(numero, end=" ")   # 0 1 1 2 3 5 8 13 21 34

# ITERTOOLS (biblioteca padrão)

import itertools

# count → contador infinito
for i in itertools.count(start=10, step=5):
    if i > 30:
        break
    print(i, end=" ")   # 10 15 20 25 30

# cycle → repete infinitamente
status = itertools.cycle(["ativo", "inativo"])
for i, s in zip(range(6), status):
    print(f"item {i}: {s}")
# item 0: ativo, item 1: inativo, item 2: ativo...

# chain → encadeia iteráveis
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
for item in itertools.chain(a, b, c):
    print(item, end=" ")   # 1 2 3 4 5 6 7 8 9

# islice → fatia um iterável (mesmo infinito)
primeiros_5 = list(itertools.islice(itertools.count(0), 5))
print(primeiros_5)   # [0, 1, 2, 3, 4]

# takewhile → pega enquanto condição for True
numeros = itertools.takewhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6])
print(list(numeros))   # [1, 2, 3, 4]

# dropwhile → descarta enquanto condição for True
numeros = itertools.dropwhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6])
print(list(numeros))   # [5, 6]