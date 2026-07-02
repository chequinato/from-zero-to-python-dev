
# Heranca em Python

# LEMBRETE: HERANCA MULTIPLA
# Python permite herdar de MAIS DE UMA classe ao mesmo tempo.
# Isso se chama heranca multipla e aparece em codigo real (ex: Mixins).
#
# Exemplo:
#
# class Logavel:
#     def log(self):
#         print(f"[LOG] {self}")
#
# class Serializable:
#     def to_dict(self):
#         return self.__dict__
#
# class Usuario(Logavel, Serializable):
#     def __init__(self, nome):
#         self.nome = nome
#
# u = Usuario("Miguel")
# u.log()           # herdado de Logavel
# u.to_dict()       # herdado de Serializable
#
# MRO (Method Resolution Order):
# Quando duas classes pai tem o mesmo metodo, Python usa o MRO pra decidir
# qual executar. Voce pode ver a ordem com:
#   print(Usuario.__mro__)
#   # (<class 'Usuario'>, <class 'Logavel'>, <class 'Serializable'>, <class 'object'>)
#
# A ordem e: da esquerda pra direita, na ordem que voce escreveu na heranca.

# HERANÇA

# Herança permite que uma classe (filha) reaproveite
# atributos e métodos de outra classe (pai)

# Herança básica

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print(f"{self.nome} faz um som")

    def dormir(self):
        print(f"{self.nome} está dormindo")

class Cachorro(Animal):
    def latir(self):
        print(f"{self.nome} está latindo: Au au!")

cachorro = Cachorro("Rex")
cachorro.emitir_som()   # herdado de Animal: Rex faz um som
cachorro.dormir()       # herdado de Animal: Rex está dormindo
cachorro.latir()        # próprio de Cachorro: Rex está latindo

print(isinstance(cachorro, Animal))     # True
print(isinstance(cachorro, Cachorro))   # True

# Sobreescrevendo métodos (override)

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print(f"{self.nome} faz um som genérico")

class Gato(Animal):
    def emitir_som(self):  # sobrescreve o método do pai
        print(f"{self.nome} faz: Miau!")

class Pato(Animal):
    def emitir_som(self):
        print(f"{self.nome} faz: Quack!")

animais = [Animal("Genérico"), Gato("Mimi"), Pato("Donald")]
for animal in animais:
    animal.emitir_som()
# Genérico faz um som genérico
# Mimi faz: Miau!
# Donald faz: Quack!

# super() -> chamando o método do pai

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def descricao(self):
        return f"{self.nome} - R${self.salario}"

class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario)   # chama __init__ do pai
        self.equipe = equipe    # adiciona atributo próprio

    def descricao(self):
        base = super().descricao()  # reaproveita método do pai
        return f"{base} - Gerencia {self.equipe} pessoas"

gerente = Gerente("Gerente", 250, 5)
print(gerente.descricao())

# Herança Multinível

class Veiculo:
    def __init__(self, marca):
        self.marca = marca

    def mover(self):
        print(f"{self.marca} está se movendo")

class Carro(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia):
        super().__init__(marca, modelo)
        self.autonomia = autonomia

    def carregar(self):
        print(f"{self.marca} {self.modelo} carregando bateria")

tesla = CarroEletrico("Tesla", 500, "Ford")
tesla.mover()
tesla.carregar()
print(tesla.marca, tesla.modelo, tesla.autonomia)

# Herança Múltipla
class Nadador:
    def nadar(self):
        print("Nadando...")

class Corredor:
    def correr(self):
        print("Correndo...")

class Atleta(Nadador, Corredor):   # herda de duas classes
    pass

atleta = Atleta()
atleta.nadar()    # Nadando...
atleta.correr()   # Correndo...

# Ordem de resolução de métodos (MRO)
print(Atleta.__mro__)
# (Atleta, Nadador, Corredor, object)

# Quando usar herança

# Use herança quando existe relação "é um" (is-a)
# Cachorro É UM Animal
# Gerente É UM Funcionario

# Não force herança quando a relação é "tem um" (has-a)
# → nesse caso, use composição (um atributo que é objeto de outra classe)
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)   # Carro TEM UM Motor

carro = Carro("Civic", 150)
print(carro.motor.potencia)  # 150

