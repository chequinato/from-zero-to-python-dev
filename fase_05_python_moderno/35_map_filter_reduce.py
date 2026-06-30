
# Map, filter e reduce

# Funções funcionais clássicas do Python
# Na prática moderna, list comprehension substitui map/filter
# mas é importante conhecer os três

from functools import reduce

# Map

# map(funcao, iterável) → aplica função em cada item
# Retorna um objeto map (lazy), converta com list()

numeros = [1, 2, 3, 4, 5]

dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)   # [2, 4, 6, 8, 10]

quadrados = list(map(lambda x: x ** 2, numeros))
print(quadrados)  # [1, 4, 9, 16, 25]

# Com função nomeada
def formatar_preco(valor):
    return f"R${valor:.2f}"

precos = [10, 25.5, 100, 3.99]
formatados = list(map(formatar_preco, precos))
print(formatados)  # ['R$10.00', 'R$25.50', 'R$100.00', 'R$3.99']

# Map com múltiplos iteráveis
a = [1, 2, 3]
b = [10, 20, 30]
somados = list(map(lambda x, y: x + y, a, b))
print(somados)  # [11, 22, 33]

# Convertendo tipos
strings = ["1", "2", "3", "4"]
inteiros = list(map(int, strings))
print(inteiros)  # [1, 2, 3, 4]

nomes = ["miguel", "joão", "ana"]
maiusculos = list(map(str.upper, nomes))
print(maiusculos)  # ['MIGUEL', 'JOÃO', 'ANA']

# Filter

# filter(funcao, iterável) → mantém itens onde função retorna True
# Retorna um objeto filter (lazy), converta com list()

numeros = list(range(1, 11))

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)   # [2, 4, 6, 8, 10]

maiores = list(filter(lambda x: x > 5, numeros))
print(maiores)  # [6, 7, 8, 9, 10]

# Filtrando strings vazias e None
dados = ["Miguel", "", None, "João", "", "Ana", None]
validos = list(filter(None, dados))  # None como função = remove Falsy
print(validos)  # ['Miguel', 'João', 'Ana']

# Filtrando dicionários
usuarios = [
    {"nome": "Miguel", "ativo": True,  "idade": 30},
    {"nome": "João",   "ativo": False, "idade": 25},
    {"nome": "Ana",    "ativo": True,  "idade": 28},
]

ativos = list(filter(lambda u: u["ativo"], usuarios))
print([u["nome"] for u in ativos])  # ['Miguel', 'Ana']

adultos = list(filter(lambda u: u["idade"] >= 28, usuarios))
print([u["nome"] for u in adultos])  # ['Miguel', 'Ana']

# Reduce

# reduce(funcao, iterável) → reduz iterável a um único valor
# Aplica a função acumulando resultado

# Somando todos
numeros = [1, 2, 3, 4, 5]
total = reduce(lambda acc, x: acc + x, numeros)
print(total)  # 15

# Como funciona:
# passo 1: acc=1, x=2 → 3
# passo 2: acc=3, x=3 → 6
# passo 3: acc=6, x=4 → 10
# passo 4: acc=10, x=5 → 15

# Com valor inicial
total = reduce(lambda acc, x: acc + x, numeros, 100)
print(total)  # 115 → começa do 100

# Maior valor
maior = reduce(lambda acc, x: acc if acc > x else x, numeros)
print(maior)  # 5

# Concatenando strings
palavras = ["Python", "é", "muito", "poderoso"]
frase = reduce(lambda acc, x: acc + " " + x, palavras)
print(frase)  # Python é muito poderoso

# Produto de todos os números
produto = reduce(lambda acc, x: acc * x, [1, 2, 3, 4, 5])
print(produto)  # 120

# Map, filter e reduce juntos

numeros = list(range(1, 11))

# Soma dos quadrados dos números pares
resultado = reduce(
    lambda acc, x: acc + x,
    map(lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, numeros))
)
print(resultado)  # 220 → 4+16+36+64+100

# Com list comprehension (mais legível)
resultado = sum(x ** 2 for x in numeros if x % 2 == 0)
print(resultado)  # 220

# Quando usar cada um

# map    → transformar cada item
# filter → selecionar itens por condição
# reduce → acumular em um único valor

# Na prática moderna:
# map/filter → substituídos por list comprehension (mais legível)
# reduce     → substituído por sum(), max(), min(), join() quando possível

# Use map/filter quando:
# → trabalhando com funções já existentes (str.upper, int, float)
# → encadeando com outras funções funcionais
# → código de legado ou estilo funcional

# Use reduce quando:
# → não existe função built-in para o que precisa acumular
# → acumulação customizada (ex: merge de dicionários, produto)