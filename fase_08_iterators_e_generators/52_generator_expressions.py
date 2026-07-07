# GENERATOR EXPRESSIONS

# Sintaxe igual ao list comprehension mas com ()
# Não cria a lista — gera os valores sob demanda

# LIST COMPREHENSION vs GENERATOR EXPRESSION

# List comprehension → cria lista inteira na memória
lista = [x ** 2 for x in range(10)]
print(lista)          # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(type(lista))    # <class 'list'>

# Generator expression → objeto lazy, gera sob demanda
gen = (x ** 2 for x in range(10))
print(gen)            # <generator object ...>
print(type(gen))      # <class 'generator'>

# Iterando sobre generator expression
for valor in gen:
    print(valor, end=" ")   # 0 1 4 9 16 25 36 49 64 81

# Generator só pode ser percorrido UMA vez!
gen = (x ** 2 for x in range(5))
print(list(gen))   # [0, 1, 4, 9, 16]
print(list(gen))   # [] → já foi consumido!

# COM FUNÇÕES QUE ACEITAM ITERÁVEL

numeros = range(1, 11)

# Passando generator direto — sem parênteses extras
total = sum(x ** 2 for x in numeros)
print(total)   # 385

maximo = max(x ** 2 for x in numeros)
print(maximo)  # 100

minimo = min(x for x in numeros if x % 2 != 0)
print(minimo)  # 1

# any() e all() com generator (eficiente — para no primeiro resultado)
tem_par = any(x % 2 == 0 for x in [1, 3, 5, 4, 7])
print(tem_par)   # True → parou no 4, não processou o resto

todos_positivos = all(x > 0 for x in [1, 2, 3, 4, 5])
print(todos_positivos)   # True

# COM CONDIÇÃO

pares = (x for x in range(20) if x % 2 == 0)
print(list(pares))   # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Encadeando condições
resultado = (x ** 2 for x in range(20) if x % 2 == 0 if x > 5)
print(list(resultado))   # [36, 64, 100, 144, 196, 256, 324]

# QUANDO USAR CADA UM

# List comprehension  → quando precisa reutilizar os dados
#                     → quando precisa indexar: lista[0]
#                     → quando precisa len(), count(), etc

# Generator expression → quando processa uma vez só
#                      → quando passa direto pra sum(), any(), all()
#                      → quando o conjunto é muito grande

# Exemplos:

# list comprehension — vai usar a lista várias vezes
nomes = [u["nome"] for u in usuarios]
print(nomes[0])
print(len(nomes))

# generator expression — processa uma vez, só precisa do total
usuarios = [
    {"nome": "Miguel", "ativo": True,  "salario": 5000},
    {"nome": "João",   "ativo": False, "salario": 4000},
    {"nome": "Ana",    "ativo": True,  "salario": 6000},
]

total_salarios = sum(u["salario"] for u in usuarios if u["ativo"])
print(total_salarios)   # 11000

media = total_salarios / sum(1 for u in usuarios if u["ativo"])
print(media)   # 5500.0

# GENERATOR EXPRESSION vs YIELD

# Generator expression → simples, uma linha
quadrados = (x ** 2 for x in range(10))

# Função com yield → quando precisa de lógica mais complexa
def quadrados_pares_ate(limite):
    for x in range(limite):
        if x % 2 == 0:
            quadrado = x ** 2
            if quadrado > 10:   # lógica mais complexa
                yield quadrado

for valor in quadrados_pares_ate(20):
    print(valor, end=" ")   # 16 36 64 100 144 196 256 324