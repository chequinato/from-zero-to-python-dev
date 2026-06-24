
# String em Python

# Criando strings
simples = 'aspas simples'
duplas = "aspas duplas"
multiline = """
Linha 1
Linha 2
Linha 3
"""
print(multiline)

# f-strings (forma moderna e mais usada)
nome = "Miguel"
idade = 30
preco = 19.90

print(f"Olá, {nome}!")
print(f"Idade: {idade}")
print(f"Preço: R${preco:.2f}")     # 2 casas decimais
print(f"Resultado: {10 * 2}")      # expressão dentro do f-string
print(f"Nome em maiúsculo: {nome.upper()}")

#Indexação e fatiamento (slicing)
texto = "Python"

print(texto[0])    # P → primeiro caractere
print(texto[-1])   # n → último caractere
print(texto[0:3])  # Pyt → do índice 0 até 2
print(texto[2:])   # thon → do índice 2 até o fim
print(texto[:3])   # Pyt → do início até o índice 2
print(texto[::-1]) # nohtyP → string invertida

# Métodos essenciais
frase = "  Olá, Mundo!  "

print(frase.strip())        # "Olá, Mundo!"  → remove espaços das bordas
print(frase.lstrip())       # "Olá, Mundo!  " → remove só à esquerda
print(frase.rstrip())       # "  Olá, Mundo!" → remove só à direita

texto = "Python é incrível"
print(texto.upper())        # PYTHON É INCRÍVEL
print(texto.lower())        # python é incrível
print(texto.capitalize())   # Python é incrível → só primeira letra maiúscula
print(texto.title())        # Python É Incrível → primeira de cada palavra

# replace()
frase = "Eu gosto de Java"
nova_frase = frase.replace("Java", "Python")
print(nova_frase)  # Eu gosto de Python

# Substituindo múltiplas ocorrências
frase = "banana banana banana"
print(frase.replace("banana", "maçã"))        # maçã maçã maçã
print(frase.replace("banana", "maçã", 2))     # maçã maçã banana → limita a 2

# split() → string para lista
frase = "Miguel,João,Ana,Paula"
nomes = frase.split(",")
print(nomes)   # ['Miguel', 'João', 'Ana', 'Paula']
print(type(nomes))  # <class 'list'>

frase2 = "Estou aprendendo Python"
palavras = frase2.split()  # sem argumento divide por espaço
print(palavras)  # ['Estou', 'aprendendo', 'Python']

#  join() → lista para string
nomes = ["Miguel", "João", "Ana"]
resultado = ", ".join(nomes)
print(resultado)  # Miguel, João, Ana

caminhos = ["home", "usuario", "documentos"]
print("/".join(caminhos))  # home/usuario/documentos

# startswith() / endswith()
arquivo = "relatorio_2024.pdf"
print(arquivo.endswith(".pdf"))     # True
print(arquivo.endswith(".xlsx"))    # False
print(arquivo.startswith("rel"))    # True
print(arquivo.startswith("doc"))    # False

# Verificando múltiplas opções
print(arquivo.endswith((".pdf", ".xlsx", ".csv")))  # True

# find() / count() / in
texto = "Python é poderoso e Python é popular"
print(texto.find("Python"))     # 0  → índice da primeira ocorrência
print(texto.find("Java"))       # -1 → não encontrado
print(texto.count("Python"))    # 2  → quantas vezes aparece
print("Python" in texto)        # True

# Verificações
print("123".isdigit())      # True  → só números
print("abc".isalpha())      # True  → só letras
print("abc123".isalnum())   # True  → letras e números
print("  ".isspace())       # True  → só espaços
print("PYTHON".isupper())   # True
print("python".islower())   # True

# Formatação com zfill e center
codigo = "42"
print(codigo.zfill(5))          # 00042 → preenche com zeros à esquerda
print("Python".center(20, "-")) # -------Python------- → centraliza

#  strip em dados reais (muito usado em APIs e CSVs)
dado_sujo = "  miguel@email.com  \n"
dado_limpo = dado_sujo.strip()
print(dado_limpo)  # miguel@email.com