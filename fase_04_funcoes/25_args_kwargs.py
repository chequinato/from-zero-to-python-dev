

# Args e Kwargs

# *args   → número variável de argumentos POSICIONAIS → vira TUPLA
# **kwargs → número variável de argumentos NOMEADOS   → vira DICIONÁRIO

# Args

def somar_tudo(*args):
    print(args)         # tupla com todos os valores
    print(type(args))   # <class 'tuple'>
    return sum(args)

print(somar_tudo(1, 2, 3))           # 6
print(somar_tudo(1, 2, 3, 4, 5))     # 15
print(somar_tudo(10))   # 10
print(somar_tudo())    # 0 → args é tupla vazia

# Iterado sobre args
def apresentar(*nomes):
    for nome in nomes:
        print(f"Olá, {nome}!")

apresentar("Miguel", "João", "Ana")

# Misturando fixo com *args
# Parâmetros fixos ANTES do *args

def registrar(evento, *detalhes):
    print(f"Evento: {evento}")

    for detalhe in detalhes:
        print(f"Detalhe: {detalhe}")

registrar("login")
registrar("Erro", "código: 500", "rota: api/dados", "hora: 10:30")

# Desempacotando lista em *args com *
def somar(a, b , c):
    return a + b + c

numeros = [1, 2, 3]
print(somar(*numeros))# desempacota a lista nos parâmetros

# Kwargs

def mostrar_info(**kwargs):
    print(kwargs)         # dicionário com todos os pares
    print(type(kwargs))   # <class 'dict'>
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

mostrar_info(nome="Miguel", idade=30, cidade="Jundiaí")
# {'nome': 'Miguel', 'idade': 30, 'cidade': 'Jundiaí'}

# Acessando kwargs com get()
def configurar(**kwargs):
    host = kwargs.get("host", "localhost")
    porta = kwargs.get("porta", 5432)
    debug = kwargs.get("debug", False)
    print(f"host={host} porta={porta} debug={debug}")

configurar(host="producao.aws.com", debug=True)
configurar()   # usa todos os padrões

# Desempacotando dicionário em **kwargs com **
def criar_usuario(nome, perfil, ativo):
    return f"{nome} | {perfil} | {ativo}"

dados = {"nome": "Miguel", "perfil": "admin", "ativo": True}
print(criar_usuario(**dados))   # desempacota o dicionário

# Mesclando dicionários com **
config_base = {"host": "localhost", "porta": 5432}
config_extra = {"banco": "clientes", "debug": True}

config_final = {**config_base, **config_extra}
print(config_final)
# {'host': 'localhost', 'porta': 5432, 'banco': 'clientes', 'debug': True}

# Sobrescrevendo valor ao mesclar
config_producao = {**config_base, "host": "producao.aws.com"}
print(config_producao)
# {'host': 'producao.aws.com', 'porta': 5432}

# Ordem correta dos parâmetros
# Regra: fixos → *args → somente nomeados → **kwargs

def funcao_completa(fixo1, fixo2, *args, opcao="padrão", **kwargs):
    print(f"fixo1: {fixo1}")
    print(f"fixo2: {fixo2}")
    print(f"args: {args}")
    print(f"opcao: {opcao}")
    print(f"kwargs: {kwargs}")

funcao_completa(
    "a", "b",          # fixos
    1, 2, 3,            # args
    opcao="custom",     # somente nomeado
    extra1="x",         # kwargs
    extra2="y"
)

# Repassando argumentos

# Padrão muito usado para wrapping de funções
def executar_com_log(funcao, *args, **kwargs):
    print(f"Executando {funcao.__name__}...")
    resultado = funcao(*args, **kwargs)
    print(f"Concluído. Resultado: {resultado}")
    return resultado

def somar(a, b):
    return a + b

def criar_usuario(nome, perfil="viewer"):
    return {"nome": nome, "perfil": perfil}

executar_com_log(somar, 10, 5)
executar_com_log(criar_usuario, "Miguel", perfil="admin")

# Exemplos reais

# Função de log flexível
def log(nivel, mensagem, *args, **kwargs):
    prefixo = f"[{nivel.upper()}]"
    msg_formatada = mensagem.format(*args) if args else mensagem
    extras = " | ".join(f"{k}={v}" for k, v in kwargs.items())
    print(f"{prefixo} {msg_formatada} {extras}".strip())

log("info", "Servidor iniciado")
log("erro", "Falha na rota {}", "/api/dados", codigo=500)
log("debug", "Usuário {} logou", "Miguel", ip="192.168.1.1", hora="10:30")

# Decorator simples com *args e **kwargs (prévia da Fase 7)
def medir_tempo(funcao):
    import time
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f"{funcao.__name__} levou {fim - inicio:.4f}s")
        return resultado
    return wrapper

