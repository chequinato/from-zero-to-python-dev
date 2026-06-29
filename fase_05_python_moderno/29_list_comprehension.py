

# List Comprehension

# Forma pythônica de criar listas em uma linha
# [expressão for item in iterável if condição]

# Básico

quadrados = []
for x in range (1, 6):
    quadrados.append(x**2)
print(quadrados) # [1, 4, 9, 16, 25]

# Com list comprehension
quadrados = [x**2 for x in range(1, 6)]
print(quadrados)

# Dobrar valores
numeros = [1, 2, 3, 4, 5]
dobrados = [x * 2 for x in numeros]
print(dobrados)  # [2, 4, 6, 8, 10]

# Converter tipos
strings = ["1", "2", "3", "4"]
inteiros = [int(x) for x in strings]
print(inteiros)  # [1, 2, 3, 4]

# Manipular strings
nomes = ["miguel", "joão", "ana"]
maiusculos = [nome.upper() for nome in nomes]
print(maiusculos)  # ['MIGUEL', 'JOÃO', 'ANA']

# Com condição (filtro)

# [expressão for item in iterável if condição]
pares = [x for x in numeros if x % 2 == 0]
print(pares) # Apenas pares

impares = [x for x in numeros if x % 2 != 0]
print(impares)

maiores_que_5 = [x for x in numeros if x > 5]
print(maiores_que_5)

# Filtrando strings
palavras = ["Python", "", "é", "", "incrível", ""]
sem_vazias = [p for p in palavras if p]  # string vazia é Falsy
print(sem_vazias)  # ['Python', 'é', 'incrível']

# Filtrando None
dados = [1, None, 2, None, 3, None]
validos = [x for x in dados if x is not None]
print(validos)  # [1, 2, 3]

# Com if e else (ternário)

# [valor_se_true if condição else valor_se_false for item in iterável]
numeros = [1, 2, 3, 4, 5, 6]

paridae = ["par" if x % 2 == 0 else "impar" for x in numeros]
print(paridae) # ['ímpar', 'par', 'ímpar', 'par', 'ímpar', 'par']

# Substituindo None por padrão
dados = [10, None, 20, None, 30]
limpos = [x if x is not None else 0 for x in dados]
print(limpos)

# Aninhada

# Lista de listas → lista plana
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
plana = [x for linha in matriz for x in linha]
print(plana)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Combinações
letras = ["a", "b", "c"]
numeros = [1, 2, 3]
combinacoes = [f"{l}{n}" for l in letras for n in numeros]
print(combinacoes)  # ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

# Exemplos reais

# Extraindo campo de lista de dicionários
usuarios = [
    {"nome": "Miguel", "ativo": True,  "idade": 30},
    {"nome": "João",   "ativo": False, "idade": 25},
    {"nome": "Ana",    "ativo": True,  "idade": 28},
]

nomes = [u["nome"] for u in usuarios]
print(nomes)  # ['Miguel', 'João', 'Ana']

nomes_ativos = [u["nome"] for u in usuarios if u["ativo"]]
print(nomes_ativos)  # ['Miguel', 'Ana']

idades = [u["idade"] for u in usuarios if u["idade"] >= 28]
print(idades)  # [30, 28]

# Limpando dados de uma API
dados_sujos = ["  Miguel  ", "  João\n", "\tAna  "]
limpos = [d.strip() for d in dados_sujos]
print(limpos)  # ['Miguel', 'João', 'Ana']

# Arquivos por extensão
arquivos = ["relatorio.pdf", "dados.csv", "foto.jpg", "script.py", "notas.csv"]
csvs = [a for a in arquivos if a.endswith(".csv")]
print(csvs)  # ['dados.csv', 'notas.csv']
