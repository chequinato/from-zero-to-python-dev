
# Lambda em Python

# Lambda = função anônima de uma linha
# lambda parâmetros: expressão

# Básico

# Função normal
def dobrar(x):
    return x * 2

# Lambda equivalente
dobrar = lambda x: x * 2
print(dobrar(5))   # 10

# Lambda com múltiplos parâmetros
somar = lambda a, b: a + b
print(somar(3, 7))  # 10

multiplicar = lambda a, b, c: a * b * c
print(multiplicar(2, 3, 4))  # 24

# Lambda com condição ternária
paridade = lambda x: "par" if x % 2 == 0 else "ímpar"
print(paridade(4))  # par
print(paridade(7))  # ímpar

# Lambda com sorted

pessoas = [
    {"nome": "Carlos", "idade": 35, "salario": 5000},
    {"nome": "Ana",    "idade": 25, "salario": 8000},
    {"nome": "Miguel", "idade": 30, "salario": 6000},
]

por_idade = sorted(pessoas, key=lambda p: p["idade"])
por_salario = sorted(pessoas, key=lambda p: p["salario"], reverse=True)
por_nome = sorted(pessoas, key=lambda p: p["nome"])

for p in por_idade:
    print(f"{p['nome']}: {p['idade']} anos")

# Ordenando tuplas
pontos = [(1, 5), (3, 2), (2, 8), (4, 1)]
por_segundo = sorted(pontos, key=lambda p: p[1])
print(por_segundo)  # [(4, 1), (3, 2), (1, 5), (2, 8)]

# Lambda com filter e map

numeros = [1, 2, 3, 4, 5]

dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)  # [2, 4, 6, 8, 10]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4]

# Encadeando map e filter
resultado = list(map(lambda x: x ** 2,
                     filter(lambda x: x % 2 == 0, numeros)))
print(resultado)  # [4, 16] → quadrado dos pares

# Lambda vs função normal

# Lambda → use quando a função é simples e usada uma vez
chave_ordenacao = lambda x: x["idade"]
ordenados = sorted(pessoas, key=chave_ordenacao)

# Função normal → use quando tem lógica, reutilização ou documentação
def criterio_ordenacao(pessoa):
    """Ordena por salário decrescente, depois por nome."""
    return (-pessoa["salario"], pessoa["nome"])

ordenados = sorted(pessoas, key=criterio_ordenacao)

# Lambda em dicionário de informações

operacoes = {
    "somar":      lambda a, b: a + b,
    "subtrair":   lambda a, b: a - b,
    "multiplicar": lambda a, b: a * b,
    "dividir":    lambda a, b: a / b if b != 0 else "erro",
}

print(operacoes["somar"](10, 5))        # 15
print(operacoes["multiplicar"](3, 4))   # 12
print(operacoes["dividir"](10, 0))      # erro

# Executando todas
for nome, op in operacoes.items():
    print(f"{nome}(10, 2) = {op(10, 2)}")