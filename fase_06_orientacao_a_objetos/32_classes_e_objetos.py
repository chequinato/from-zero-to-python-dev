
# Classes e Objetos

# Classe = molde/blueprint
# Objeto = instância criada a partir da classe

# Classe básica

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome # atributo da instância
        self.idade = idade

    def apresentar(self):
        print(f"Olá, sou {self.nome} e tenho {self.idade} anos")

# Criando objetos
pessoa1 = Pessoa("Miguel", 20)
pessoa2 = Pessoa("Ana", 24)
print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa2.nome)
print(pessoa2.idade)

pessoa1.apresentar()
pessoa2.apresentar()

# __init__ e self

# __init__ → construtor, executa ao criar o objeto
# self → representa a própria instância, sempre primeiro parâmetro

class Produto:
    def __init__(self, nome, preco, estoque=0):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque # valor padrão

produto1 = Produto("Notebook", 3500)
produto2 = Produto("Mouse", 150, 50)

print(produto1.nome, produto1.estoque)   # Notebook 0
print(produto2.nome, produto2.estoque)   # Mouse 50

# self é automático — você não passa ele ao chamar
# Produto("Notebook", 3500) por trás vira: Produto(self, "Notebook", 3500)

# Cada objeto é independente

p1 = Pessoa("Miguel", 30)
p2 = Pessoa("João", 25)

p1.nome = "Miguel Silva"
print(p1.nome)  # Miguel Silva
print(p2.nome)  # João → não foi afetado

# Métodos recebendo parâmetros

class ContaBancaria:

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor}. Saldo: R${self.saldo}")

    def sacar(self, valor):
        self.saldo -= valor
        print(f"Saque de R${valor}. Saldo: R${self.saldo}")

conta = ContaBancaria("Miguel", 5000)
conta.depositar(500)
conta.sacar(200)
conta.sacar(5000) # saldo insuficiente

# Verificando o tipo do objeto
print(type(conta))     # <class '__main__.ContaBancaria'>
print(isinstance(conta, ContaBancaria))  # True
print(isinstance(conta, Pessoa))     # False
