

# Properties
# @property transforma um método em "atributo calculado"
# Permite validação ao definir valores, mantendo sintaxe simples

# Sem property (problema)

class TermometroSemProperty:
    def __init__(self, celcius=0):
        self.celcius = celcius

t = TermometroSemProperty(25)
t.celcius = -500 # # nenhuma validação, aceita qualquer coisa

# Com property
class Termometro:
    def __init__(self, celsius=0):
        self._celsius = celsius   # atributo "privado" por convenção

    @property
    def celsius(self):  # getter — acessa como atributo
        return self._celsius

    @celsius.setter
    def celsius(self, valor):   # setter — valida antes de atribuir
        if valor < -273.15:
            raise ValueError("Temperatura abaixo do zero absoluto!")
        self._celsius = valor

    @property
    def fahrenheit(self):  # property calculada (somente leitura)
        return self._celsius * 9/5 + 32

t = Termometro(25)
print(t.celsius)  # 25      → chama o getter, sem parênteses!
print(t.fahrenheit) # 77.0    → calculado na hora

t.celsius = 30    # chama o setter
print(t.celsius)  # 30

try:
    t.celsius = -500   # dispara o ValueError do setter
except ValueError as e:
    print(e)   # Temperatura abaixo do zero absoluto!

# t.fahrenheit = 100   # AttributeError — não tem setter, é somente leitura

# Property com validação real
class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco # já passa pelo setter aqui

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("Preço não pode ser negativo")
        self._preco = valor

produto = Produto("Notebook", 3500)
print(produto.preco)   # 3500

produto.preco = 4000
print(produto.preco)   # 4000

try:
    produto.preco = -100
except ValueError as e:
    print(e)   # Preço não pode ser negativo

# Property somente leitur (read-only)

class Circulo:
    def __int__(self, raio):
        self._raio = raio

    @property
    def area(self):
        return 3.14159 * self.raio ** 2

    @property
    def perimetro(self):
        return 2 * 3.14159 * self.raio

circulo = Circulo(5)
print(circulo.area)
print(circulo.perimetro)

# circulo.area = 100   # AttributeError — sem setter, não pode atribuir

# Property com cache (cálculo pesado)
class Relatorio:
    def __init__(self, dados):
        self._dados = dados
        self._total_calculado = None

    @property
    def total(self):
        if self._total_calculado is None:
            print("Calculando total (operação pesada)...")
            self._total_calculado = sum(self._dados)
        return self._total_calculado

relatorio = Relatorio([100, 200, 300, 400])
print(relatorio.total)   # Calculando... 1000
print(relatorio.total)   # 1000 → não recalcula, usa cache

# Quando usar Property

# Quando precisa validar um valor antes de atribuir
# Quando um "atributo" é na verdade calculado a partir de outros
# Quando quer manter a sintaxe simples (objeto.atributo) com lógica por trás
# Quando quer tornar um atributo somente leitura


