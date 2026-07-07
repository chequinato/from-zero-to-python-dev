
# DUNDER METHODS (MÉTODOS MÁGICOS)

# "Dunder" = Double UNDERscore (__metodo__)
# Permitem que objetos personalizados se comportem como tipos nativos

# __init__ (já conhecido)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

# __str__ vs __repr__

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        # usado em print() e str() → versão "amigável" para o usuário
        return f"{self.nome} - R${self.preco:.2f}"

    def __repr__(self):
        # usado no console/debug → versão técnica, idealmente reconstrói o objeto
        return f"Produto(nome='{self.nome}', preco={self.preco})"

produto = Produto("Notebook", 3500)
print(produto)        # Notebook - R$3500.00 → chama __str__
print(str(produto))   # Notebook - R$3500.00
print(repr(produto))  # Produto(nome='Notebook', preco=3500)

# Se não tiver __str__, Python usa __repr__ como fallback
class Simples:
    def __repr__(self):
        return "Simples()"

print(Simples())   # Simples()

# __len__

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def __len__(self):
        return len(self.itens)

carrinho = Carrinho()
carrinho.adicionar("Notebook")
carrinho.adicionar("Mouse")

print(len(carrinho))   # 2 → funciona com len() nativo!

# __eq__ (comparação de igualdade)

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y

p1 = Ponto(2, 3)
p2 = Ponto(2, 3)
p3 = Ponto(5, 5)

print(p1 == p2)   # True  → usa __eq__
print(p1 == p3)   # False

# Sem __eq__, Python compara identidade (mesmo objeto na memória)

# OUTROS DUNDERS DE COMPARAÇÃO

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __eq__(self, outro):
        return self.preco == outro.preco

    def __lt__(self, outro):   # less than (<)
        return self.preco < outro.preco

    def __gt__(self, outro):   # greater than (>)
        return self.preco > outro.preco

p1 = Produto("Mouse", 150)
p2 = Produto("Notebook", 3500)

print(p1 < p2)    # True  → usa __lt__
print(p1 > p2)    # False → usa __gt__
print(sorted([p2, p1], key=lambda p: p.preco))  # ordenação manual ainda funciona

# __add__ (sobrecarga de operadores)

class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, outro):
        return Vetor(self.x + outro.x, self.y + outro.y)

    def __repr__(self):
        return f"Vetor({self.x}, {self.y})"

v1 = Vetor(2, 3)
v2 = Vetor(4, 1)
resultado = v1 + v2   # usa __add__

print(resultado)   # Vetor(6, 4)

# __getitem__ e __setitem__ (comportamento de lista/dict)

class ListaPersonalizada:
    def __init__(self):
        self.dados = []

    def adicionar(self, item):
        self.dados.append(item)

    def __getitem__(self, indice):
        return self.dados[indice]

    def __setitem__(self, indice, valor):
        self.dados[indice] = valor

minha_lista = ListaPersonalizada()
minha_lista.adicionar("a")
minha_lista.adicionar("b")

print(minha_lista[0])   # a → usa __getitem__
minha_lista[0] = "z"
print(minha_lista[0])   # z → usa __setitem__

# __contains__ (suporte ao "in")

class Time:
    def __init__(self, jogadores):
        self.jogadores = jogadores

    def __contains__(self, jogador):
        return jogador in self.jogadores

time = Time(["Miguel", "João", "Ana"])
print("Miguel" in time)   # True → usa __contains__
print("Carlos" in time)   # False

# RESUMO DOS DUNDERS MAIS USADOS

# __init__   → construtor
# __str__    → print() / str() amigável
# __repr__   → representação técnica/debug
# __len__    → len(objeto)
# __eq__     → objeto == objeto
# __lt__/__gt__ → objeto < / > objeto
# __add__    → objeto + objeto
# __getitem__/__setitem__ → objeto[i] / objeto[i] = valor
# __contains__ → valor in objeto