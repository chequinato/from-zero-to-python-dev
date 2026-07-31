
# Dict Comprehension

# Forma pythônica de criar dicionários em uma linha
# {chave: valor for item in iterável if condição}

# Básico

# Quadrados como dicionário
quadrados = {x: x ** 2 for x in range(1, 6)}
print(quadrados)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Lista → dicionário
nomes = ["Miguel", "João", "Ana"]
tamanhos = {nome: len(nome) for nome in nomes}
print(tamanhos)  # {'Miguel': 6, 'João': 4, 'Ana': 3}

# Duas listas → dicionário (com zip)
chaves = ["nome", "idade", "cidade"]
valores = ["Miguel", 30, "Jundiaí"]
dicionario = {k: v for k, v in zip(chaves, valores)}
print(dicionario)  # {'nome': 'Miguel', 'idade': 30, 'cidade': 'Jundiaí'}

# Com condição
numeros = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
print(numeros)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Filtrando dicionário existente
precos = {"notebook": 3500, "mouse": 150, "teclado": 250, "monitor": 1200}

caros = {k: v for k, v in precos.items() if v > 500}
print(caros)  # {'notebook': 3500, 'monitor': 1200}

baratos = {k: v for k, v in precos.items() if v <= 250}
print(baratos)  # {'mouse': 150, 'teclado': 250}

# Transformando valores

# Aplicando desconto
precos = {"notebook": 3500, "mouse": 150, "teclado": 250}
com_desconto = {k: v * 0.9 for k, v in precos.items()}
print(com_desconto)

# Invertendo chave e valor
original = {"a": 1, "b": 2, "c": 3}
invertido = {v: k for k, v in original.items()}
print(invertido)  # {1: 'a', 2: 'b', 3: 'c'}

# Normalizando chaves
dados_sujos = {"  Nome  ": "Miguel", "  Idade  ": 30}
limpo = {k.strip().lower(): v for k, v in dados_sujos.items()}
print(limpo)  # {'nome': 'Miguel', 'idade': 30}

# Exemplos reais

# Indexando lista por campo (muito usado!)
usuarios = [
    {"id": 1, "nome": "Miguel", "perfil": "admin"},
    {"id": 2, "nome": "João",   "perfil": "editor"},
    {"id": 3, "nome": "Ana",    "perfil": "viewer"},
]

por_id = {u["id"]: u for u in usuarios}
print(por_id[1])  # {'id': 1, 'nome': 'Miguel', 'perfil': 'admin'}
print(por_id[3]["nome"])  # Ana

por_nome = {u["nome"]: u for u in usuarios}
print(por_nome["João"]["perfil"])  # editor

# Contando ocorrências
palavras = ["python", "java", "python", "go", "python", "java"]
contagem = {p: palavras.count(p) for p in set(palavras)}
print(contagem)  # {'go': 1, 'java': 2, 'python': 3}

# Set comprehension (bônus)
numeros = [1, 2, 2, 3, 3, 3, 4]
unicos = {x for x in numeros}
print(unicos)   # {1, 2, 3, 4}
pares_unicos = {x for x in numeros if x % 2 == 0}
print(pares_unicos)  # {2, 4}