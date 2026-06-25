
# Range em Python

# range() gera uma sequência de números
# range(stop)
# range(start, stop)
# range(start, stop, step)

# range (stop) - de 0 até stop-1

# --- range(stop) → de 0 até stop-1 ---
for i in range(5):
    print(i)  # 0 1 2 3 4

# range(start, stop)
for i in range(1, 6):
    print(i)  # 1 2 3 4 5

# range(start, stop, step)
for i in range(0, 20, 2):
    print(i)  # 0 2 4 6 8 10 12 14 16 18

for i in range(0, 11, 5):
    print(i)  # 0 5 10

# Range decrescente
for i in range(10, 0, -1):
    print(i)  # 10 9 8 7 6 5 4 3 2 1

for i in range(5, -1, -1):
    print(i)  # 5 4 3 2 1 0

# Range não é só lista mas pode virar uma

sequencia = range(10)
print(sequencia)
print(list(range(10)))
print(type(range(10)))

# len() e in com range
r = range(1, 101)
print(len(r))        # 100
print(50 in r)       # True
print(101 in r)      # False

# Usos práticos
# Repetir N vezes sem usar a variável

for _ in range(3):
    print("Repetindo...")

# Criar lista de numeros
quadrados = []
for i in range(1, 6):
    quadrados.append(i ** 2)
print(quadrados)

# Percorrer lista pelo índice
frutas = ["maçã", "banana", "uva"]
for i in range(len(frutas)):
    print(f"[{i}] {frutas[i]}")

# Tabuada
numero = 7
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Somando com range
total = sum(range(1, 101))  # soma de 1 a 100
print(total)  # 5050