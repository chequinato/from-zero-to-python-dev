
# Operadores lógicos em Python

# and → ambos precisam ser True
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

idade = 25
tem_cnh = True
print(idade >= 18 and tem_cnh)   # True  → maior de idade E tem CNH
print(idade >= 18 and not tem_cnh)  # False

# or → pelo menos um precisa ser True
print(True or False)    # True
print(False or False)   # False
print(False or True)    # True

tem_dinheiro = False
tem_cartao = True
print(tem_dinheiro or tem_cartao)  # True → tem pelo menos um meio de pagamento

# not → inverte o valor
print(not True)    # False
print(not False)   # True

bloqueado = False
print(not bloqueado)  # True → não está bloqueado = pode passar

# in → verifica se está dentro de uma coleção
frutas = ["banana", "maçã", "laranja"]
print(frutas[0])
print(frutas[1])
print(frutas[2])
print("banana" in frutas) # True
print("banana" not in frutas) # False

nome = "Miguel"
print("M" in nome)      # True
print("z" in nome)      # False

# not in → verifica se NÃO está na coleção
print("manga" not in frutas)   # True
print("banana" not in frutas)  # False

# Combinando operadores lógicos
idade = 20
renda = 3000
tem_divida = False

# Aprovado para crédito: maior de 18, renda > 2000 e sem dívida
aprovado = idade >= 18 and renda > 2000 and not tem_divida
print(aprovado)  # True

# Short-circuit (avaliação curto-circuito)
# Python para de avaliar assim que já sabe o resultado

# Com "and": se o primeiro for False, nem avalia o segundo
# Com "or": se o primeiro for True, nem avalia o segundo

x = 0
print(x != 0 and 10 / x > 1)  # False → não divide por zero, pois parou no "x != 0"

# Truthy e Falsy básico (será aprofundado na Fase 5)
# Valores que se comportam como False:
print(bool(0))        # False
print(bool(0.0))      # False
print(bool(""))       # False
print(bool([]))       # False
print(bool(None))     # False

# Valores que se comportam como True:
print(bool(1))        # True
print(bool(-1))       # True
print(bool("texto"))  # True
print(bool([0]))      # True → lista com qualquer elemento é True