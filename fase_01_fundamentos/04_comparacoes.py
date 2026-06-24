
# Comparações no Python

# Comparações sempre retornam True ou False
print(10 == 10)   # True  → igual
print(10 == 5)    # False

print(10 != 5)    # True  → diferente
print(10 != 10)   # False

print(10 > 5)     # True  → maior que
print(10 > 10)    # False

print(10 >= 10)   # True  → maior ou igual
print(10 >= 11)   # False

print(10 < 20)    # True  → menor que
print(10 <= 10)   # True  → menor ou igual

# Comparando strings
print("abc" == "abc")   # True
print("abc" == "ABC")   # False → case sensitive
print("abc" != "ABC")   # True
print("b" > "a")        # True → ordem alfabética (valor ASCII)
print("z" > "a")        # True

# --- Comparando com None ---
valor = None
print(valor == None)    # True, mas evite
print(valor is None)    # True, forma correta
print(valor is not None)  # False

# Comparando tipos diferentes
print(1 == 1.0)     # True  → Python compara o valor
print(1 == True)    # True  → True vale 1
print(0 == False)   # True  → False vale 0
print(type(1) == type(1.0))  # False → int != float

# Encadeamento de comparações (pythônico!)
nota = 7

print(0 <= nota <= 10)   # True  → nota está entre 0 e 10
print(5 < nota < 10)     # True  → nota está entre 5 e 10

idade = 25
print(18 <= idade <= 65)  # True → adulto em idade de trabalho
print(25 > idade < 18)    # False → idade não é menor que 18

# Comparação de identidade: is vs ==
# == compara VALOR
# is compara se são o MESMO objeto na memória

lista_a = [1, 2, 3]
lista_b = [1, 2, 3]
lista_c = lista_a

print(lista_a == lista_b)   # True  → mesmo valor
print(lista_a is lista_b)   # False → objetos diferentes na memória
print(lista_a is lista_c)   # True  → apontam para o mesmo objeto