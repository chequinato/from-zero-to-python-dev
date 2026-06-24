
# Variáveis em Python

nome = "Miguel"
idade = 30
preco = 30.90
ativo = True

# A variável pode mudar de valor a qualquer momento
contador = 10
print(contador)

contador = contador + 1
print(contador)

# Múltiplas atribuições na mesma linha

x, y, z = 1, 2, 3
print(x, y, z)

# Trocar valores entre variáveis (swap)
a = "primeiro"
b = "segundo"
a, b = b, a

print(a)
print(b)

# Atribuição do mesmo valor para múltiplas variáveis
largura = altura = profundidade = 0
print(largura, altura, profundidade)

largura, altura, profundidade = 0, 0, 0
print(largura, altura, profundidade)

# Constantes
# Python não tem constante de verdade, mas a convenção é MAIÚSCULAS

NOME_EMPRESA = ("AWS Corp")
MAX_USUARIOS = 1000
PI = 3.14159

print(NOME_EMPRESA)
print(MAX_USUARIOS)
print(PI)

# Boas práticas de nomenclatura
#snake_case → padrão Python
nome_completo = "Miguel Chequinato"
print(nome_completo)

total_de_itens = 10
print(total_de_itens)

preco_unitario = 5.90
print(preco_unitario)

# evitando:
# NomeCompleto = "Miguel"  → isso é PascalCase, usado para classes
# nomecompleto = "Miguel"  → difícil de ler
# nc = "Miguel"            → sem significado

# variáveis com _ no início (convenção)
_variavel_interna = "uso interno do módulo" # sinal de "não use fora daqui"
__variavel_privada = "privada na classe"  # veremos em OOP

# Deletando uma variável
temporario = "Só preciso por um momento"
print(temporario)
del temporario
print(temporario) # Erro de "is not defined"



