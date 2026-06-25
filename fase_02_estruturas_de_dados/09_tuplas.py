
# Typlas em Python

# Tupla é uma coleção ordenada e IMUTÁVEL
# Use quando os dados não devem mudar

# Criando tuplas
vazia = ()
coordenada = (10, 20)
rgb = (255, 128, 0)
pessoa = ("Miguel", 30, "Brasil")

print(vazia)
print(coordenada)
print(rgb)
print(pessoa)

print(type(coordenada))
print(type(vazia))
print(len(pessoa))

# Tupla com um único elemento (precisa da vírgula!)
um_elemento = (42,)
print(type(um_elemento))   # <class 'tuple'>
nao_e_tupla = (42)
print(type(nao_e_tupla))   # <class 'int'>

# Indexação e fatiamento (igual à lista)
pessoa = ("Miguel", 30, "Brasil")
print(pessoa[0])    # Miguel
print(pessoa[-1])   # Brasil
print(pessoa[0:2])  # ('Miguel', 30)

#  Imutabilidade
coordenada = (10, 20)
# coordenada[0] = 99  # TypeError: 'tuple' object does not support item assignment

# Métodos disponíveis (poucos, pois é imutável)
numeros = (1, 2, 2, 3, 2, 4)
print(numeros.count(2))   # 3
print(numeros.index(3))   # 3 → índice do valor 3

# Desempacotamento
pessoa = ("Miguel", 30, "Brasil")
nome, idade, pais = pessoa
print(nome)   # Miguel
print(idade)  # 30
print(pais)   # Brasil

# Ignorando valores com _
x, _, z = (1, 2, 3)
print(x, z)  # 1 3

# Quando usar tupla vs lista?
# Tupla → dados fixos, coordenadas, configurações, retorno de funções
# Lista → dados que vão mudar, coleções dinâmicas

# Exemplos reais de tupla:
ponto = (40.7128, -74.0060)        # coordenadas GPS
cores_rgb = (255, 255, 255)         # branco em RGB
config = ("localhost", 5432, "db")  # host, porta, banco

# Conversão entre lista e tupla
lista = [1, 2, 3]
tupla = tuple(lista)
print(tupla)  # (1, 2, 3)

tupla2 = (4, 5, 6)
lista2 = list(tupla2)
print(lista2)  # [4, 5, 6]

# Tuplas são mais rápidas que listas
# Use tupla quando os dados são fixos → melhor performance e mais seguro
