
# Atributos e Métodos

# Atributos de instância vs de classe

class Funcionario:
    # Atributo de CLASSE → compartilhado por todas as instâncias
    empresa = "TechCorp"
    total_funcionarios = 0

    def __init__(self, nome, salario):
        # Atributos de INSTÂNCIA → únicos de cada objeto
        self.nome = nome
        self.salario = salario
        Funcionario.total_funcionarios += 1

f1 = Funcionario("Miguel", 5000)
f2 = Funcionario("Ana", 6000)
print(f1)
print(f2)
print(f1.empresa)   # TechCorp → atributo de classe
print(f2.empresa)   # TechCorp → mesmo valor para todos

print(f1.nome)   # Miguel → atributo de instância
print(f2.nome)   # Ana   → diferente para cada um

print(Funcionario.total_funcionarios)  # 2

# Mudando atributo de classe afeta todos (se acessado pela classe)
Funcionario.empresa = "NovaCorp"
print(f1.empresa)  # NovaCorp
print(f2.empresa)  # NovaCorp

# Mas se atribuir direto na instância, cria atributo NOVO só dela
f1.empresa = "MinhaEmpresa"
print(f1.empresa)  # MinhaEmpresa → só dessa instância
print(f2.empresa)  # NovaCorp     → continua o da classe

# Métodos de instância

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        self.preco = self.preco * (1 - percentual / 100)

    def descricao(self):
        return f"{self.nome}: R${self.preco:.2f}"

produto = Produto("Notebook", 3500)
print(produto.descricao())   # Notebook: R$3500.00

produto.aplicar_desconto(10)
print(produto.descricao())   # Notebook: R$3150.00

# Métodos que retornam valores vs modificam estado

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar(self, item, preco):
        self.itens.append({"item": item, "preco": preco})

    def total(self):
        return sum(i["preco"] for i in self.itens)

    def quantidade_itens(self):
        return len(self.itens)

carrinho = Carrinho()
carrinho.adicionar("Notebook", 3500)
carrinho.adicionar("Mouse", 150)

print(carrinho.quantidade_itens())  # 2
print(carrinho.total())             # 3650

# Modificando atributos diretamente vs métodos

class Termometro:
    def __init__(self, celsius=0):
        self.celsius = celsius

    def para_fahrenheit(self):
        return self.celsius * 9/5 + 32

    def ajustar(self, valor):
        # método permite validação, acesso direto não
        if valor < -273.15:
            print("Temperatura impossível!")
            return
        self.celsius = valor

t = Termometro(25)
print(t.para_fahrenheit())   # 77.0

t.ajustar(-300)   # Temperatura impossível!
print(t.celsius)  # 25 → não mudou

t.celsius = -300  # acesso direto ignora a validação do método!
print(t.celsius)  # -300 → problema! (resolvido com encapsulamento)
