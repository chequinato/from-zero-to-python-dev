# @staticmethod E @classmethod

# Método normal → recebe self (a instância)
# @classmethod   → recebe cls (a classe)
# @staticmethod  → não recebe nem self nem cls

# MÉTODO DE INSTÂNCIA (padrão)

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):   # precisa de self → acessa dados da instância
        return f"Olá, sou {self.nome}"

pessoa = Pessoa("Miguel")
print(pessoa.apresentar())   # Olá, sou Miguel

# @staticmethod

# Não acessa self nem cls
# Função "utilitária" que faz sentido dentro da classe, mas não usa seus dados

class Calculadora:
    @staticmethod
    def somar(a, b):
        return a + b

    @staticmethod
    def eh_par(numero):
        return numero % 2 == 0

# Chama direto pela classe, sem precisar instanciar
print(Calculadora.somar(5, 3))    # 8
print(Calculadora.eh_par(10))     # True

# Também funciona pela instância (mas não é necessário)
calc = Calculadora()
print(calc.somar(2, 2))   # 4

# Exemplo real: validações
class Validador:
    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email

    @staticmethod
    def validar_cpf(cpf):
        return len(cpf.replace(".", "").replace("-", "")) == 11

print(Validador.validar_email("miguel@email.com"))   # True
print(Validador.validar_cpf("123.456.789-00"))         # True

# @classmethod

# Recebe cls (a própria classe), não a instância
# Muito usado para criar "construtores alternativos"

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def a_partir_de_string(cls, dados_str):
        # dados_str = "Miguel,30"
        nome, idade = dados_str.split(",")
        return cls(nome, int(idade))   # cria e retorna nova instância

    @classmethod
    def a_partir_de_dict(cls, dados_dict):
        return cls(dados_dict["nome"], dados_dict["idade"])

# Construtor normal
pessoa1 = Pessoa("Miguel", 30)

# Construtores alternativos via classmethod
pessoa2 = Pessoa.a_partir_de_string("João,25")
pessoa3 = Pessoa.a_partir_de_dict({"nome": "Ana", "idade": 28})

print(pessoa2.nome, pessoa2.idade)   # João 25
print(pessoa3.nome, pessoa3.idade)   # Ana 28

# CLASSMETHOD PARA CONTAR INSTÂNCIAS

class Funcionario:
    total = 0   # atributo de classe

    def __init__(self, nome):
        self.nome = nome
        Funcionario.total += 1

    @classmethod
    def quantidade_funcionarios(cls):
        return cls.total

Funcionario("Miguel")
Funcionario("João")
Funcionario("Ana")

print(Funcionario.quantidade_funcionarios())   # 3

# COMPARANDO OS TRÊS TIPOS

class Exemplo:
    valor_classe = "compartilhado"

    def __init__(self, valor):
        self.valor_instancia = valor

    def metodo_instancia(self):
        # acessa tanto instância quanto classe
        return f"instância: {self.valor_instancia}, classe: {self.valor_classe}"

    @classmethod
    def metodo_classe(cls):
        # acessa só a classe, não a instância específica
        return f"classe: {cls.valor_classe}"

    @staticmethod
    def metodo_estatico():
        # não acessa nem instância nem classe
        return "não preciso de nada da classe"

obj = Exemplo("teste")
print(obj.metodo_instancia())   # instância: teste, classe: compartilhado
print(obj.metodo_classe())      # classe: compartilhado
print(obj.metodo_estatico())    # não preciso de nada da classe

# Todos podem ser chamados pela classe também (exceto instância sem objeto)
print(Exemplo.metodo_classe())    # funciona
print(Exemplo.metodo_estatico())  # funciona
# Exemplo.metodo_instancia()      #  erro, falta self