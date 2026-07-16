
'''

Conceito
O módulo math traz funções matemáticas que não vêm por padrão nos operadores comuns —
raiz quadrada, potência, arredondamento, constantes como π, funções trigonométricas, logaritmo etc.
É tudo baseado em float, então cuidado com precisão quando comparar resultados.

'''

# Constantes e funções básicas

import math

print(math.pi)  # 3.141592653589793
print(math.e)  # 2.718281828459045

print(math.sqrt(16)) # 4.0 → raiz quadrada
print(math.pow(2, 3)) # 8.0 → potência (sempre retorna float)
print(2**3)  # 8 → operador nativo, retorna int (mais usado no dia a dia)

# Arredondamento

print(math.floor(4.7))  # 4 → arredonda pra baixo
print(math.ceil(4.1)) # 5 -> arredonda pra cima
print(math.round(4.5)) # 4 → arredondamento "banker's rounding" do Python (não é do math)

# Outras funções úteis
print(math.factorial(5))     # 120 → 5! = 5*4*3*2*1
print(math.gcd(12, 18))      # 6  → máximo divisor comum
print(math.log(100, 10))     # 2.0 → log base 10 de 100
print(math.hypot(3, 4))      # 5.0 → hipotenusa (raiz de 3²+4²)
print(math.isnan(float('nan')))  # True → verifica se é "não é um número"
print(math.isinf(float('inf')))  # True → verifica se é infinito
