
# Sorted, any e all

# Sorted

# sorted() → retorna NOVA lista ordenada (não modifica original)
# list.sort() → modifica a lista no lugar, retorna None

numeros = [3, 1, 4, 1, 5, 9, 2, 6]

nova = sorted(numeros)
print(nova)      # [1, 1, 2, 3, 4, 5, 6, 9]
print(numeros)   # [3, 1, 4, 1, 5, 9, 2, 6] → original intacta

decrescente = sorted(numeros, reverse=True)
print(decrescente)  # [9, 6, 5, 4, 3, 2, 1, 1]

# Ordenando strings
nomes = ["Carlos", "ana", "Miguel", "joão"]
print(sorted(nomes))   # ordem ASCII: maiúsculas antes
print(sorted(nomes, key=str.lower))  # ignora case

# Ordenando por tamanho
palavras = ["Python", "é", "muito", "bom"]
print(sorted(palavras, key=len))  # ['é', 'bom', 'muito', 'Python']

# Ordenando dicionários
produtos = [
    {"nome": "Notebook", "preco": 3500, "estoque": 5},
    {"nome": "Mouse",    "preco": 150,  "estoque": 50},
    {"nome": "Teclado",  "preco": 250,  "estoque": 30},
]

por_preco = sorted(produtos, key=lambda p: p["preco"])
por_estoque = sorted(produtos, key=lambda p: p["estoque"], reverse=True)

# Múltiplos critérios com tupla
alunos = [
    {"nome": "Miguel", "nota": 9.0, "turma": "A"},
    {"nome": "Ana",    "nota": 9.0, "turma": "B"},
    {"nome": "João",   "nota": 7.5, "turma": "A"},
]
# Nota decrescente, depois nome alfabético
ordenados = sorted(alunos, key=lambda a: (-a["nota"], a["nome"]))
for a in ordenados:
    print(f"{a['nome']}: {a['nota']}")

# Any

# any() → True se PELO MENOS UM elemento for True
# Para quando o iterável acabar sem achar True

print(any([True, False, False]))   # True
print(any([False, False, False]))  # False
print(any([]))    # False → iterável vazio

numeros = [1, 3, 5, 8, 9]
print(any(x % 2 == 0 for x in numeros))   # True → tem o 8

usuarios = [
    {"nome": "Miguel", "admin": False},
    {"nome": "João",   "admin": True},
    {"nome": "Ana",    "admin": False},
]
tem_admin = any(u["admin"] for u in usuarios)
print(tem_admin)  # True

# Verificando se algum valor existe
permissoes_usuario = ["ler", "escrever"]
pode_acessar = any(p in permissoes_usuario for p in ["deletar", "escrever"])
print(pode_acessar)  # True → tem pelo menos "escrever"

# All

# all() → True se TODOS os elementos forem True
# Para quando achar o primeiro False

print(all([True, True, True]))    # True
print(all([True, False, True]))   # False
print(all([]))     # True → vazio é True (cuidado!)

numeros = [2, 4, 6, 8, 10]
print(all(x % 2 == 0 for x in numeros))   # True → todos pares

# Validando campos obrigatórios
usuario = {"nome": "Miguel", "email": "miguel@email.com", "idade": 30}
campos_obrigatorios = ["nome", "email", "idade"]

todos_preenchidos = all(
    campo in usuario and usuario[campo]
    for campo in campos_obrigatorios
)

print(todos_preenchidos)  # True

# Verificando se todos os pedidos estão aprovados
pedidos = [
    {"id": 1, "status": "aprovado"},
    {"id": 2, "status": "aprovado"},
    {"id": 3, "status": "pendente"},
]
todos_aprovados = all(p["status"] == "aprovado" for p in pedidos)
print(todos_aprovados)  # False

# Any vs All

estoque = [0, 0, 5, 0, 0]

print(any(x > 0 for x in estoque))   # True  → tem algum disponível
print(all(x > 0 for x in estoque))   # False → nem todos disponíveis
print(all(x == 0 for x in estoque))  # False → nem todos zerados
print(any(x == 0 for x in estoque))  # True  → algum zerado