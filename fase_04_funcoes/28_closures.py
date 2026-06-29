
# Closures em Python

# Closure = função que "lembra" do escopo onde foi criada
# mesmo depois que esse escopo já terminou

# Entendendo o conceito
def exterior():
    mensagem = "Olá do exterior!"

    def interior():
        print(mensagem)  # acessa variável do escopo externo

    return interior  # retorna a função, não executa!

minha_funcao = exterior()
minha_funcao()  # "Olá do exterior!"
# exterior() já terminou, mas interior() ainda lembra de mensagem!

# Inspecionando o closure
print(minha_funcao.__closure__)
print(minha_funcao.__closure__[0].cell_contents)  # "Olá do exterior!"

# Closure como parâmetro
def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}! {nome}"
    return saudar

ola = criar_saudacao("Olá")
oi = criar_saudacao("Oi")
bom_dia = criar_saudacao("Bom dia ")

print(ola("Miguel"))    # Olá, Miguel!
print(oi("João"))       # Oi, João!
print(bom_dia("Ana"))   # Bom dia, Ana!

# Cada closure tem sua própria cópia de saudacao
# ola, oi e bom_dia são funções independentes

# Closure como contador

def criar_contador(inicio = 0, passo = 1):
    estado = [inicio] # lista para poder modificar via nonlocal

    def incrementar():
        estado[0] += passo
        return estado[0]

    def decrementar():
        estado[0] -= passo
        return estado[0]

    def resetar():
        estado[0] = inicio

    def valor():
        return estado[0]

    return incrementar, decrementar, resetar, valor

inc, dec, reset, val = criar_contador(inicio=0, passo=2)

print(inc())    # 2
print(inc())    # 4
print(inc())    # 6
print(dec())    # 4
print(val())    # 4
print(reset())  # 0

# Dois contadores completamente independentes
inc_a, *_ = criar_contador(0)
inc_b, *_ = criar_contador(100)

print(inc_a())  # 1
print(inc_a())  # 2
print(inc_b())  # 101 → independente!

# Closure com nonlocal

def criar_acumulador():
    total = 0 # variável do escopo enclosing

    def adicionar(valor):
        nonlocal total  # permite modificar a variável acima
        total += valor
        return total

    return adicionar

acumular = criar_acumulador()
print(acumular(10))  # 10
print(acumular(20))  # 30
print(acumular(5))   # 35

# Closure como cache (memoization)

def criar_cache():
    cache = {}

    def buscar(chave, funcao_busca):
        if chave not in cache:
            print(f"  Buscando '{chave}'...")
            cache[chave] = funcao_busca(chave)
        else:
            print(f"  Cache hit: '{chave}'!")
        return cache[chave]

    def limpar():
        cache.clear()
        print("Cache limpo")

    return buscar, limpar

def buscar_usuario(id):
    usuarios = {"1": "Miguel", "2": "João", "3": "Ana"}
    return usuarios.get(id, "Não encontrado")

buscar, limpar_cache = criar_cache()
print(buscar("1", buscar_usuario))  # Buscando... → Miguel
print(buscar("1", buscar_usuario))  # Cache hit!  → Miguel
print(buscar("2", buscar_usuario))  # Buscando... → João
print(buscar("2", buscar_usuario))  # Cache hit!  → João
limpar_cache()
print(buscar("1", buscar_usuario))  # Buscando de novo → Miguel

# Closures vs Classes

# Closure e classe resolvem problemas parecidos
# Closure → mais simples, poucos comportamentos
# Classe  → mais organizada, muitos comportamentos

# Com closure
def criar_conta_closure(saldo_inicial):
    saldo = [saldo_inicial]

    def depositar(valor):
        if valor <= 0:
            return "Valor inválido"
        saldo[0] += valor
        return saldo[0]

    def sacar(valor):
        if valor <= 0:
            return "Valor inválido"
        if valor > saldo[0]:
            return "Saldo insuficiente"
        saldo[0] -= valor
        return saldo[0]

    def ver_saldo():
        return saldo[0]

    return depositar, sacar, ver_saldo

depositar, sacar, saldo = criar_conta_closure(1000)
print(saldo())      # 1000
print(depositar(500))  # 1500
print(sacar(200))      # 1300
print(sacar(2000))     # Saldo insuficiente
print(saldo())         # 1300

# Quando usar Closure?

# Configuração de comportamento (formatadores, validadores)
# Cache / memoization simples
# Contador ou acumulador de estado
# Decorator (próxima fase!)
# Quando classe seria exagero para poucos comportamentos
