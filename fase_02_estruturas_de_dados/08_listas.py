
# Listas em Python
# Lista é uma coleção ordenada, mutável e permite duplicatas

# Criando listas

nomes = ["Miguel", "Ana", "Maria"]
numeros = [1, 2, 3, 4, 5]
mista = [1, "texto", True, 3.14]

print(nomes)
print(type(nomes))
print(len(nomes))
print(numeros)
print(mista)

# Indexação
frutas = ["maçã", "banana", "uva", "manga", "laranja"]

print(frutas[0])  # Saída: maçã
print(frutas[2])  # Saída: uva
print(frutas[-1]) # Saída: laranja
print(frutas[-2]) # Saída: manga

# Fatiamento (slicing)
print(frutas[0:3])   # ['maçã', 'banana', 'uva']
print(frutas[2:])    # ['uva', 'manga', 'laranja']
print(frutas[:3])    # ['maçã', 'banana', 'uva']
print(frutas[::2])   # ['maçã', 'uva', 'laranja'] → de 2 em 2
print(frutas[::-1])  # invertida

# Modificando itens
frutas [1] = "Melancia"
print(frutas)

# append() → adiciona no final
nomes = ["Miguel", "João"]
nomes.append("Ana")
print(nomes)

# insert() → adiciona em posição específica
nomes.insert(1, "Maria")
print(nomes)

# extend() → adiciona vários itens de outra lista
extras = ["Paula", "Lucas"]
nomes.extend(extras)
print(nomes)  # ['Miguel', 'Carlos', 'João', 'Ana', 'Paula', 'Lucas']

# Diferença: append vs extend
lista = [1, 2, 3]
lista.append([4, 5])  # adiciona a lista como UM item
print(lista)  # [1, 2, 3, [4, 5]]

lista = [1, 2, 3]
lista.extend([4, 5])   # adiciona cada item separadamente
print(lista)  # [1, 2, 3, 4, 5]

# remove() → remove por valor
frutas = ["maçã", "banana", "uva", "banana"]
frutas.remove("banana")
print(frutas)

# pop() → remove por índice e retorna o valor
frutas = ["maçã", "banana", "uva"]
removido = frutas.pop()    # remove o último
print(removido)  # uva
print(frutas)    # ['maçã', 'banana']

frutas.pop(1)
print(frutas) # Remove o item no índice 1

removido = frutas.pop(0)
print(removido)
print(frutas)

# clear() → remove tudo
lista = [1, 2, 3]
lista.clear()
print(lista)  # []

# sort() → ordena a lista (modifica no lugar)
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
numeros.sort()
print(numeros)  # [1, 1, 2, 3, 4, 5, 6, 9]

# reverse() → inverte a ordem
numeros = [1, 2, 3, 4, 5]
numeros.reverse()
print(numeros)  # [5, 4, 3, 2, 1]

# index() → retorna o índice de um valor
frutas = ["maçã", "banana", "uva"]
print(frutas.index("banana"))  # 1

# count() → conta ocorrências
numeros = [1, 2, 2, 3, 2, 4]
print(numeros.count(2))  # 3

# copy() → cópia independente da lista
original = [1, 2, 3]
copia = original.copy()
copia.append(4)
print(original)  # [1, 2, 3] → não foi afetada
print(copia) # [1, 2, 3, 4]

# Diferença: cópia vs referência
lista_a = [1, 2, 3]
lista_b = lista_a  # mesma referência!
lista_b.append(4)
print(lista_a)  # [1, 2, 3, 4] → foi afetada!

# Operações úteis
numeros = [3, 1, 4, 1, 5, 9]

print(min(numeros))    # 1
print(max(numeros))    # 9
print(sum(numeros))    # 23
print(len(numeros))    # 6

# in / not in
print("maçã" in frutas)      # True
print("manga" not in frutas)  # True

# Listas aninhadas (matriz)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[0])       # [1, 2, 3]
print(matriz[0][0])    # 1
print(matriz[1][2])    # 6
print(matriz[2][2])    # 9

# Desempacotamento de lista
primeiro, segundo, *resto = [1, 2, 3, 4, 5]
print(primeiro)  # 1
print(segundo)   # 2
print(resto)     # [3, 4, 5]
