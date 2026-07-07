# DECORATORS EM PYTHON

# Decorator = função que recebe outra função e estende seu comportamento
# sem modificar o código original
# Sintaxe: @decorator acima da função

# ENTENDENDO A BASE

# Para entender decorators, precisa saber que funções são objetos
def saudar():
    print("Olá!")

# Atribuindo a variável
outra = saudar
outra()   # Olá!

# Passando como argumento
def executar(funcao):
    funcao()

executar(saudar)   # Olá!

# DECORATOR BÁSICO

# Decorator manual (sem @)
def meu_decorator(funcao):
    def wrapper():
        print("Antes da função")
        funcao()
        print("Depois da função")
    return wrapper

def saudar():
    print("Olá!")

saudar = meu_decorator(saudar)   # aplicando o decorator manualmente
saudar()
# Antes da função
# Olá!
# Depois da função

# Com @ (syntactic sugar — faz a mesma coisa)
def meu_decorator(funcao):
    def wrapper():
        print("Antes da função")
        funcao()
        print("Depois da função")
    return wrapper

@meu_decorator   # equivale a: saudar = meu_decorator(saudar)
def saudar():
    print("Olá!")

saudar()
# Antes da função
# Olá!
# Depois da função

# DECORATOR COM *ARGS E **KWARGS

# Para funcionar com qualquer função, independente dos parâmetros
def logger(funcao):
    def wrapper(*args, **kwargs):
        print(f"Chamando {funcao.__name__}...")
        resultado = funcao(*args, **kwargs)
        print(f"{funcao.__name__} concluída!")
        return resultado   # sempre retorne o resultado!
    return wrapper

@logger
def somar(a, b):
    return a + b

@logger
def criar_usuario(nome, perfil="viewer"):
    return {"nome": nome, "perfil": perfil}

print(somar(10, 5))
# Chamando somar...
# somar concluída!
# 15

print(criar_usuario("Miguel", perfil="admin"))
# Chamando criar_usuario...
# criar_usuario concluída!
# {'nome': 'Miguel', 'perfil': 'admin'}

# PRESERVANDO A IDENTIDADE DA FUNÇÃO

# Sem functools.wraps, o decorator "esconde" a função original
@logger
def somar(a, b):
    return a + b

print(somar.__name__)   # wrapper → problema! perdemos o nome original

# Com functools.wraps → preserva nome, docstring, etc
from functools import wraps

def logger(funcao):
    @wraps(funcao)   # preserva a identidade da função original
    def wrapper(*args, **kwargs):
        print(f"Chamando {funcao.__name__}...")
        resultado = funcao(*args, **kwargs)
        print(f"{funcao.__name__} concluída!")
        return resultado
    return wrapper

@logger
def somar(a, b):
    """Soma dois números."""
    return a + b

print(somar.__name__)   # somar
print(somar.__doc__)    # Soma dois números.

# DECORATORS ÚTEIS NA PRÁTICA

from functools import wraps
import time

# --- Medir tempo de execução ---
def medir_tempo(funcao):
    @wraps(funcao)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f"{funcao.__name__} levou {fim - inicio:.4f}s")
        return resultado
    return wrapper

@medir_tempo
def processar(dados):
    time.sleep(0.1)   # simulando processamento
    return sum(dados)

print(processar([1, 2, 3, 4, 5]))
# processar levou 0.1001s
# 15

# --- Validar argumentos ---
def validar_positivo(funcao):
    @wraps(funcao)
    def wrapper(valor, *args, **kwargs):
        if valor <= 0:
            raise ValueError(f"Valor deve ser positivo, recebeu: {valor}")
        return funcao(valor, *args, **kwargs)
    return wrapper

@validar_positivo
def calcular_raiz(valor):
    return valor ** 0.5

print(calcular_raiz(16))   # 4.0

try:
    calcular_raiz(-4)
except ValueError as e:
    print(e)   # Valor deve ser positivo, recebeu: -4

# --- Cache simples (memoization) ---
def cache(funcao):
    memo = {}
    @wraps(funcao)
    def wrapper(*args):
        if args not in memo:
            print(f"Calculando para {args}...")
            memo[args] = funcao(*args)
        else:
            print(f"Cache hit para {args}!")
        return memo[args]
    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))
print(fibonacci(5))   # cache hit!

# Python já tem isso pronto no functools:
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# DECORATOR COM PARÂMETRO

# Decorator que recebe argumento precisa de um nível extra
def repetir(vezes):
    def decorator(funcao):
        @wraps(funcao)
        def wrapper(*args, **kwargs):
            for _ in range(vezes):
                resultado = funcao(*args, **kwargs)
            return resultado
        return wrapper
    return decorator

@repetir(vezes=3)
def saudar(nome):
    print(f"Olá, {nome}!")

saudar("Miguel")
# Olá, Miguel!
# Olá, Miguel!
# Olá, Miguel!

# MÚLTIPLOS DECORATORS

# Aplicados de baixo para cima
@medir_tempo
@logger
def calcular(a, b):
    return a + b

calcular(10, 5)
# Execução: medir_tempo(logger(calcular))

# DECORATORS DE CLASSE (já vistos)

# Python tem decorators nativos muito usados em classes:
# @property       → getter/setter elegante
# @staticmethod   → método sem self nem cls
# @classmethod    → método que recebe cls
# @dataclass      → gera __init__, __repr__, __eq__
# @lru_cache      → cache automático de resultados

# QUANDO USAR DECORATORS


# Logging e monitoramento
# Medição de tempo / performance
# Validação de entrada
# Cache / memoization
# Controle de acesso / autenticação
# Retry automático em caso de falha
# Qualquer comportamento que se repete em várias funções