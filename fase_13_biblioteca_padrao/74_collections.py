
'''

Conceito:
O módulo collections traz versões especializadas dos tipos básicos (dict, list, tuple) otimizadas pra situações específicas
contar elementos, ter valores padrão automáticos, criar registros nomeados, ordem garantida.
Muito usado quando o dict/list puro fica "curto" pro que você precisa.

'''

# Contar elementos

from collections import Counter, defaultdict, namedtuple, OrderedDict

palavras = ["python", "sql", "python", "aws", "sql", "python"]
contagem = Counter(palavras)
print(contagem) # Counter({'python': 3, 'sql': 2, 'aws': 1})

print(contagem.most_common(2)) # [('python', 3), ('sql', 2)] → os 2 mais comuns
print(contagem["aws"])  # 3... não, 1 (retorna a contagem daquela chave)

# Dicionário com valor padrão automático

# dict normal: dá KeyError se a chave não existir
# defaultdict: cria a chave automaticamente com um valor padrão

grupos = defaultdict(list)
grupos["python"].append("aula1")
grupos["python"].append("aula2")
grupos["sql"].append("aula1")

print(grupos)  # defaultdict(<class 'list'>, {'python': ['aula1', 'aula2'], 'sql': ['aula1']})

# namedtuple -  tupla com nomes nos campos

Usuario = namedtuple("Usuario", ["nome", "idade", "email"])
u1 = Usuario("Miguel", 30, "miguel@gmail.com")

print(u1)

print(u1.nome)   # Miguel → acessa por nome, não só por índice
print(u1[0])     # Miguel → índice ainda funciona

# OrderedDict - dicionário que garante ordem (menos usado hoje, dict normal já mantém ordem desde Python 3.7+)

od = OrderedDict()
od["a"] = 1
od["b"] = 2
print(od) # OrderedDict([('a', 1), ('b', 2)])


# deque -  fila/pilha eficiente nas duas pontas

fila = deque([1, 2, 3])
fila.append(4) # adiciona no fim
fila.appendleft(0) # adiciona no início
print(fila)  # deque([0, 1, 2, 3, 4])

fila.pop() # remove do fim
fila.popleft() # remove do início