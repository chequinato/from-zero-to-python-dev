# IMPORT EM PYTHON

# FORMAS DE IMPORTAR

# --- import simples ---
import math

print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.14159...
print(math.ceil(4.2))   # 5
print(math.floor(4.8))  # 4

# --- import com alias (apelido) ---
import math as m

print(m.sqrt(25))   # 5.0

# Muito usado com bibliotecas grandes
import json as j
dados = j.loads('{"nome": "Miguel"}')

# --- from ... import (importa só o que precisa) ---
from math import sqrt, pi, ceil

print(sqrt(9))   # 3.0  → sem precisar de "math."
print(pi)        # 3.14159...

# --- from ... import com alias ---
from math import sqrt as raiz_quadrada

print(raiz_quadrada(64))   # 8.0

# --- from ... import * (evite!) ---
# from math import *   # traz tudo, polui o namespace
# print(sqrt(4))       # funciona mas não fica claro de onde veio

# BIBLIOTECA PADRÃO (stdlib)

# Já vem com Python, não precisa instalar

import os
import sys
import json
import math
import time
import datetime
import random
import re
import pathlib
import itertools
import functools
import collections

# --- os ---
print(os.getcwd())                    # diretório atual
print(os.getenv("PATH"))              # variável de ambiente
print(os.path.exists("arquivo.txt"))  # verifica se existe

# --- sys ---
print(sys.version)     # versão do Python
print(sys.platform)    # linux / win32 / darwin

# --- random ---
import random
print(random.randint(1, 10))          # número inteiro aleatório
print(random.choice(["a", "b", "c"])) # item aleatório da lista
print(random.random())                 # float entre 0 e 1

lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
print(lista)   # lista embaralhada

# --- collections ---
from collections import Counter, defaultdict, deque

# Counter → conta ocorrências
palavras = ["python", "java", "python", "go", "python"]
contagem = Counter(palavras)
print(contagem)              # Counter({'python': 3, 'java': 1, 'go': 1})
print(contagem.most_common(2))  # [('python', 3), ('java', 1)]

# defaultdict → dicionário com valor padrão
grupos = defaultdict(list)
dados = [("A", 1), ("B", 2), ("A", 3), ("B", 4)]
for chave, valor in dados:
    grupos[chave].append(valor)   # não precisa verificar se chave existe
print(dict(grupos))   # {'A': [1, 3], 'B': [2, 4]}

# deque → lista otimizada para inserção/remoção nas extremidades
fila = deque([1, 2, 3])
fila.appendleft(0)   # insere no início → O(1), lista normal seria O(n)
fila.append(4)       # insere no fim
print(fila)          # deque([0, 1, 2, 3, 4])

# --- re (regex) ---
import re

texto = "Meu email é miguel@email.com e meu telefone é 11-99999-9999"

email = re.search(r"[\w.]+@[\w.]+", texto)
if email:
    print(email.group())   # miguel@email.com

todos_numeros = re.findall(r"\d+", texto)
print(todos_numeros)   # ['11', '99999', '9999']

# ORDEM DE BUSCA DO PYTHON

# Quando você faz "import X", Python busca nessa ordem:
# 1. sys.modules (cache — já foi importado antes?)
# 2. Módulos built-in (math, sys, os...)
# 3. sys.path → diretório atual, PYTHONPATH, stdlib, site-packages

print(sys.path)   # lista de caminhos que Python busca

# IMPORTAÇÃO LAZY (dentro de função)

# Importar dentro de função → só carrega quando necessário
def processar_csv(caminho):
    import csv   # só importa quando a função é chamada
    with open(caminho) as f:
        return list(csv.reader(f))

# Útil quando o módulo é pesado e nem sempre necessário