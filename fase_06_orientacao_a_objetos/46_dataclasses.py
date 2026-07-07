
# DATACLASSES

# @dataclass gera automaticamente __init__, __repr__, __eq__
# Ideal para classes que só guardam dados

from dataclasses import dataclass, field

# SEM DATACLASS (verboso)

class PontoTradicional:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"PontoTradicional(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# COM DATACLASS (muito mais simples)

@dataclass
class Ponto:
    x: int
    y: int

p1 = Ponto(2, 3)
p2 = Ponto(2, 3)

print(p1)            # Ponto(x=2, y=3) → __repr__ automático
print(p1 == p2)       # True → __eq__ automático
print(p1.x, p1.y)     # 2 3

# VALORES PADRÃO

@dataclass
class Produto:
    nome: str
    preco: float
    estoque: int = 0      # valor padrão
    ativo: bool = True

produto1 = Produto("Notebook", 3500)
produto2 = Produto("Mouse", 150, estoque=50)

print(produto1)   # Produto(nome='Notebook', preco=3500, estoque=0, ativo=True)
print(produto2)   # Produto(nome='Mouse', preco=150, estoque=50, ativo=True)

# CAMPOS MUTÁVEIS (field)

# Não pode usar lista/dict direto como padrão
# @dataclass
# class Carrinho:
#     itens: list = []   # ValueError!

# Use field(default_factory=...)
@dataclass
class Carrinho:
    itens: list = field(default_factory=list)
    descontos: dict = field(default_factory=dict)

carrinho1 = Carrinho()
carrinho2 = Carrinho()

carrinho1.itens.append("Notebook")
print(carrinho1.itens)   # ['Notebook']
print(carrinho2.itens)   # [] → independente!

# MÉTODOS EM DATACLASS

@dataclass
class ContaBancaria:
    titular: str
    saldo: float = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
            return
        self.saldo -= valor

conta = ContaBancaria("Miguel", 1000)
conta.depositar(500)
print(conta.saldo)   # 1500

# DATACLASS IMUTÁVEL (frozen)

@dataclass(frozen=True)
class Coordenada:
    latitude: float
    longitude: float

coord = Coordenada(40.7128, -74.0060)
print(coord)   # Coordenada(latitude=40.7128, longitude=-74.006)

# coord.latitude = 0   # FrozenInstanceError — imutável!

# ORDENAÇÃO AUTOMÁTICA (order=True)

@dataclass(order=True)
class Produto:
    nome: str
    preco: float

p1 = Produto("Mouse", 150)
p2 = Produto("Notebook", 3500)

print(p1 < p2)   # True → compara pela ordem dos campos (nome primeiro)

produtos = [Produto("Teclado", 250), Produto("Mouse", 150), Produto("Monitor", 1200)]
print(sorted(produtos))

# QUANDO USAR DATACLASS

# Classes que armazenam dados (DTOs, modelos simples)
# Substituir namedtuple ou dict com estrutura fixa
# Configurações, registros, respostas de API

# Evite quando a classe tem MUITA lógica de negócio
# → nesse caso, classe normal com __init__ explícito é mais clara