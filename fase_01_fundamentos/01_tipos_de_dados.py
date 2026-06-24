
# Tipo de dado: str
nome = "Miguel"

sobrenome = "Chequinato"

frase = "Estou aprendendo Python"

# Aspas simples ou duplas — tanto faz

print(f"Meu nome é {nome}, sobrenome {sobrenome}, {frase}")
print(type(nome))
print(type(sobrenome))
print(type(frase))

# Tipo de dado: int

idade = 30
ano = 2024
quantidade = -5

print(idade)
print(type(idade))
print(type(ano))
print(type(quantidade))

print(10+3)
print(10-3)
print(10*3)
print(10**3)
print(10//3)
print(10%3)

# Tipo de dado: float

preco = 19.90
altura = 1.75
temperatura = -3.5

print(preco)
print(altura)
print(temperatura)

print(type(preco))
print(type(altura))
print(type(temperatura))

print(0.1 + 0.2)

numero = float(10)
print(numero)
print(type(numero))

# Tipo de dado: Bool

ativo = True
bloqueado = False

print(type(ativo))
print(type(bloqueado))

# Bool por baixo é true = 1 e false = 0
print(True + True)
print(True - False)
print(int(True))
print(int(False))

print(10>5)
print(10<5)
print(10==5)

# Tipo de dado: None

resultado = None
usuario = None

print(resultado)
print(type(resultado))
print(type(usuario))

# Comparação correta com None é com "is", não com "=="
print(resultado is None)
print(usuario is not None)

# Conversões entre tipos (type casting)

# str → int
numero = int("42")
print(numero)       # 42
print(type(numero)) # <class 'int'>

# str → float
preco = float("19.90")
print(preco)  # 19.9

# int → str
codigo = str(100)
print(codigo)        # "100"
print(type(codigo))  # <class 'str'>

# int → bool
print(bool(0))   # False
print(bool(1))   # True
print(bool(-5))  # True → qualquer número diferente de 0 é True

# str → bool
print(bool(""))       # False → string vazia é False
print(bool("texto"))  # True  → qualquer texto é True

# Verificando tipo com type() e isinstance()
nome = "Miguel"
idade = 30
preco = 19.90
ativo = True

# type() → retorna o tipo
print(type(nome))   # <class 'str'>
print(type(idade))  # <class 'int'>
print(type(preco))  # <class 'float'>
print(type(ativo))  # <class 'bool'>

# isinstance() → verifica se é de um tipo (mais usado no código real)
print(isinstance(nome, str))    # True
print(isinstance(idade, int))   # True
print(isinstance(preco, float)) # True
print(isinstance(ativo, bool))  # True

# Verificando múltiplos tipos de uma vez
numero = 42
print(isinstance(numero, (int, float)))  # True