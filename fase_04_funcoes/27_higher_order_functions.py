
# Higher Order Functions

# Funções de ordem superior:
# 1. Recebem funções como parâmetro
# 2. Retornam funções como resultado

# Em Python, funções são "cidadãos de primeira classe":
# podem ser atribuídas a variáveis, passadas e retornadas

# Funções como variável

def saudar(nome):
    return f"Olá {nome}"

# Atribuindo função a variavel (sem parênteses = sem chamar)

cumprimentar = saudar
print(cumprimentar("Miguel")) # Olá, Miguel!
print(type(cumprimentar)) # <class 'function'>

# Lista de funções
def dobrar(x): return x * 2
def triplicar(x): return x * 3
def ao_quadrado(x): return x ** 2

operacoes = [dobrar, triplicar, ao_quadrado]

for operacao in operacoes:
    print(f"operacao.__name__ (5) = {operacao(5)}")

# Funções que recebem funções

def aplicar(funcao, valor):
    return funcao(valor)

print(aplicar(dobrar, 5)) # 10
print(aplicar(ao_quadrado, 5)) # 25
print(aplicar(str.upper, "python")) # PYTHON

# Aplicando em lista
def aplicar_em_lista(funcao, lista):
    resultado = []

    for item in lista:
        resultado.append(funcao(item))
    return resultado

numeros = [1, 2, 3, 4, 5]
print(aplicar_em_lista(dobrar, numeros))        # [2, 4, 6, 8, 10]
print(aplicar_em_lista(ao_quadrado, numeros))   # [1, 4, 9, 16, 25]

# Funções que retornam funções
def criar_multiplicador(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar  # retorna a função, não o resultado!

dobrar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
por_dez = criar_multiplicador(10)

print(dobrar(5))     # 10
print(triplicar(5))  # 15
print(por_dez(5))    # 50

# Criando validadores configuráveis
def criar_validador (minimo, maximo):
    def validar(valor):
        return minimo <= valor <= maximo
    return validar

validar_nota = criar_validador(0, 10)
validar_nota = criar_validador(0, 150)
validar_nota = criar_validador(0, 100)

print(validar_nota(7.5))   # True
print(validar_nota(11))   # False
#print(validar_percentual(110)) # False

# Sorted Key
# sorted() aceita função como key para definir critério de ordenação

pessoas = [
    {"nome": "Carlos", "idade": 35, "salario": 5000},
    {"nome": "Ana",    "idade": 25, "salario": 8000},
    {"nome": "Miguel", "idade": 30, "salario": 6000},
]

# Ordenando por idade
por_idade = sorted(pessoas, key=lambda p: p["idade"])

for p in por_idade:
    print(f"idade = {p['idade']} anos")

# Ordenando por nome
por_nome = sorted(pessoas, key=lambda p: p["nome"])

# Ordenando por salário decrescente
por_salario = sorted(pessoas, key=lambda p: p["salario"], reverse=True)

# Ordenando string por tamanho
palavras = ["Python", "é", "incrível", "e", "poderoso"]
por_tamanho = sorted(palavras, key=len)
print(por_tamanho) #['é', 'e', 'Python', 'incrível', 'poderoso']

# Ordenando po múltiplos critérios
alunos = [
    ("Miguel", 9.0),
    ("João",   7.5),
    ("Ana",    9.0),
    ("Paula",  7.5),
]
# Ordena por nota decrescente, depois por nome

ordenados = sorted(alunos, key=lambda x: (-x[1], x[0]))
print(ordenados)
# [('Ana', 9.0), ('Miguel', 9.0), ('João', 7.5), ('Paula', 7.5)]

# Map
# map(funcao, iteravel) → aplica função em cada item

# Com função nomeada
def formatar_preco(valor):
    return f"R${valor:.2f}"

precos = [10, 25.5, 100, 3.99]
formatados = list(map(formatar_preco, precos))
print(formatados) # ['R$10.00', 'R$25.50', 'R$100.00', 'R$3.99']

# Map com múliplas listas
a = [1, 2, 3]
b = [10, 20, 30]

somados = list(map(lambda x, y: x + y, a, b))
print(somados)   # [11, 22, 33]

# Filter

# filter(funcao, iteravel) → mantém itens onde função retorna True
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)   # [2, 4, 6, 8, 10]

# Filtrando dicionários
usuarios = [
    {"nome": "Miguel", "ativo": True},
    {"nome": "João",   "ativo": False},
    {"nome": "Ana",    "ativo": True},
]

ativos = list(filter(lambda u: u["ativo"], usuarios))
print(ativos)

# Map e filter vs list comprehension

numeros = [1, 2, 3, 4, 5]

# Com map/filter
dobrados_pares = list(map(lambda x: x * 2,
                          filter(lambda x: x % 2 == 0, numeros)))

# Com list comprehension (mais pythônico e legível)
dobrados_pares = [x * 2 for x in numeros if x % 2 == 0]

print(dobrados_pares)  # [4, 8]
# Use list comprehension no dia a dia
# map/filter aparecem em código legado e em contextos funcionais

# Any e All

# any() → True se PELO MENOS UM for True
# all() → True se TODOS forem True

numeros = [2, 4, 6, 8, 10]
print(all(x % 2 == 0 for x in numeros))   # True → todos pares
print(any(x > 5 for x in numeros))        # True → pelo menos um > 5

usuarios = [
    {"nome": "Miguel", "ativo": True},
    {"nome": "João",   "ativo": False},
]
print(any(u["ativo"] for u in usuarios))   # True → algum ativo
print(all(u["ativo"] for u in usuarios))   # False → nem todos ativos

# Verificações reais
permissoes = ["ler", "escrever"]
necessarias = ["ler", "deletar"]

tem_todas = all(p in permissoes for p in necessarias)
print(tem_todas)  # False → não tem "deletar"