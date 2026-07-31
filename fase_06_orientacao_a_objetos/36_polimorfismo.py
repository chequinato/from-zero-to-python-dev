
# Polimorfismo

# Polimorfismo = "muitas formas"
# Objetos diferentes respondem ao mesmo método de jeitos diferentes

# Polimorfismo com herança

class Forma:
    def area(self):
        raise NotImplementedError("Subclasse deve implementar area()")

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        raise NotImplementedError("Subclasse deve implementar area()")

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.largura = base
        self.altura = altura

    def area(self):
        return 3.14159 * self.raio ** 2

# Mesmo método .area(), comportamento diferente para cada forma
formas = [Retangulo(5, 3), Circulo(4), Triangulo(6, 2)]

for forma in formas:
    print(f"{type(forma).__name__}: área = {forma.area():.2f}")
# Retangulo: área = 15.00
# Circulo: área = 50.27
# Triangulo: área = 6.00

# O código que usa não precisa saber QUAL forma é
def imprimir_area(forma):
    print(f"Área: {forma.area():.2f}")

for forma in formas:
    imprimir_area(forma) # funciona pra qualquer Forma

# Duck typing - polimorfismo sem herança

# "Se anda como pato e faz quack como pato, é um pato"
# Python não exige herança para polimorfismo

class Pato:
    def fazer_som(self):
        print("Quack")

class Pessoa:
    def fazer_som(self):
        print("Estou imitando um pato!")

class Brinquedo:
    def fazer_som(self):
        print("Quack eletrônico!")

# Nenhuma classe herda de ninguém, mas todas têm fazer_som()
objetos = [Pato(), Pessoa(), Brinquedo()]

for obj in objetos:
    obj.fazer_som()   # funciona em todos, sem precisar de herança comum

# Polimorfismo com funções built-in
# len() se comporta diferente dependendo do tipo
print(len("Python"))        # 6 → tamanho da string
print(len([1, 2, 3]))       # 3 → tamanho da lista
print(len({"a": 1, "b": 2})) # 2 → quantidade de chaves

# + se comporta diferente dependendo do tipo
print(1 + 2)            # 3 → soma numérica
print("a" + "b")        # ab → concatenação
print([1, 2] + [3, 4])  # [1, 2, 3, 4] → concatenação de listas

# Polimorfismo em sistemas reais

class Notificacao:
    def enviar(self, mensagem):
        raise NotImplementedError

class NotificacaoEmail(Notificacao):
    def enviar(self, mensagem):
        print(f"Email enviado: {mensagem}")

class NotificacaoSMS(Notificacao):
    def enviar(self, mensagem):
        print(f"SMS enviado: {mensagem}")

class NotificacaoPush(Notificacao):
    def enviar(self, mensagem):
        print(f"Push enviado: {mensagem}")

def notificar_usuario(canal: Notificacao, mensagem):
    canal.enviar(mensagem)   # não importa qual canal é

canais = [NotificacaoEmail(), NotificacaoSMS(), NotificacaoPush()]

for canal in canais:
    notificar_usuario(canal, "Seu pedido foi enviado!")
# Email enviado: Seu pedido foi enviado!
# SMS enviado: Seu pedido foi enviado!
# Push enviado: Seu pedido foi enviado!
