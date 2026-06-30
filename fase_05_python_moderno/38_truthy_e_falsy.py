
# Truthy e Falsy

# Em Python, qualquer valor pode ser avaliado como True ou False
# Valores Falsy → se comportam como False em condicionais
# Valores Truthy → todo o resto

# Valores Falsy

# Todos os valores abaixo são Falsy:
print(bool(False))    # False
print(bool(None))     # False
print(bool(0))        # False
print(bool(0.0))      # False
print(bool(0j))       # False → número complexo zero
print(bool(""))       # False → string vazia
print(bool([]))       # False → lista vazia
print(bool(()))       # False → tupla vazia
print(bool({}))       # False → dicionário vazio
print(bool(set()))    # False → set vazio

# Valores Truthy

print(bool(True))        # True
print(bool(1))           # True
print(bool(-1))          # True → qualquer número diferente de 0
print(bool(0.1))         # True
print(bool("texto"))     # True → qualquer string não vazia
print(bool(" "))         # True → espaço é truthy!
print(bool([0]))         # True → lista com qualquer item
print(bool([False]))     # True → lista com False é truthy!
print(bool({"a": 1}))   # True

# Uso em condicionais

# Forma verbosa (desnecessária)
lista = [1, 2, 3]
if len(lista) > 0:
    print("tem itens")

# Forma pythônica
if lista:
    print("tem itens")

# Verificando None
usuario = None
if usuario is None:    # correto para None especificamente
    print("sem usuário")

if not usuario:        # também funciona, mas pega outros Falsy
    print("sem usuário")

# Exemplo prático

# Verificando se string tem conteúdo
nome = input("Nome: ") if False else ""   # simulando input vazio
if not nome:
    print("Nome obrigatório")

# Verificando lista
erros = []
if erros:
    print("Tem erros!")
else:
    print("Sem erros!")  # cai aqui

# Verificando dicionário
dados = {}
if not dados:
    print("Dados vazios")  # cai aqui

# Verificando resposta de API
resposta = {"status": 200, "data": []}
if resposta.get("data"):
    print("Tem dados")
else:
    print("Sem dados")  # lista vazia é Falsy

# Armadilhas comuns

# 0 é Falsy mas pode ser valor válido
estoque = 0
if not estoque:
    print("sem estoque")  # cai aqui, mas 0 pode ser intencional!

# Mais explícito quando 0 é valor válido
if estoque is None:
    print("estoque não informado")
elif estoque == 0:
    print("sem estoque")

# False e 0 são iguais
print(False == 0)   # True
print(True == 1)    # True
print(False is 0)   # False → tipos diferentes!

# Lista com False é Truthy
flags = [False, False, False]
if flags:
    print("lista existe!")  # cai aqui, a LISTA é truthy, não os itens

# Para verificar itens:
if any(flags):
    print("algum True")
else:
    print("todos False")  # cai aqui

# Or e And com Truthy e Falsy

# or → retorna o PRIMEIRO valor Truthy, ou o último
print("Miguel" or "padrão")   # Miguel → primeiro é Truthy
print("" or "padrão")         # padrão → primeiro é Falsy
print(None or 0 or "valor")   # valor  → primeiro Truthy
print(None or 0 or False)     # False  → todos Falsy, retorna o último

# and → retorna o PRIMEIRO valor Falsy, ou o último
print("Miguel" and "João")   # João   → todos Truthy, retorna o último
print("" and "João")         # ""     → primeiro é Falsy, para aqui
print(None and "João")       # None   → primeiro é Falsy

# Padrão muito usado: valor padrão com or
nome = "" or "Anônimo"
print(nome)   # Anônimo

config = None or {"debug": False}
print(config)  # {'debug': False}

# Cuidado: 0 or 10 retorna 10 mesmo sendo 0 válido!
quantidade = 0
resultado = quantidade or 10
print(resultado)   # 10 → mas 0 pode ser válido!

# Melhor com None como sentinela
quantidade = None
resultado = quantidade if quantidade is not None else 10
print(resultado)   # 10