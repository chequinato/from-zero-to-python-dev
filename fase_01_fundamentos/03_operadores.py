
# Operadores em Python

# Operadores Aritméticos
print(10 + 3)   # 13 → adição
print(10 - 3)   # 7  → subtração
print(10 * 3)   # 30 → multiplicação
print(10 / 3)   # 3.3333... → divisão real (sempre retorna float)
print(10 // 3)  # 3  → divisão inteira (descarta decimal)
print(10 % 3)   # 1  → resto da divisão (módulo)
print(10 ** 3)  # 1000 → potência

# Diferenças importantes entre / e //:
contador = 10

contador += 5   # contador = contador + 5
print(contador) # 15

contador -= 3   # contador = contador - 3
print(contador) # 12

contador *= 2   # contador = contador * 2
print(contador) # 24

contador //= 5  # contador = contador // 5
print(contador) # 4

contador **= 3  # contador = contador ** 3
print(contador) # 64

contador %= 10  # contador = contador % 10
print(contador) # 4

# Precedência de operadores (ordem de execução)
# Segue a mesma regra da matemática: () → ** → * / // % → + -

print(2 + 3 * 4)      # 14  → multiplicação primeiro
print((2 + 3) * 4)    # 20  → parênteses primeiro
print(2 ** 3 + 1)     # 9   → potência primeiro
print(10 % 3 + 1)     # 2   → módulo primeiro

# Operadores com strings (concatenação)
nome = "Miguel"
sobrenome = "Chequinato"

nome_completo = nome + " " + sobrenome
print(nome_completo)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print(lista1 + lista2)  # [1, 2, 3, 4, 5, 6] → concatenação
print(lista1 * 2)       # [1, 2, 3, 1, 2, 3] → repetição

