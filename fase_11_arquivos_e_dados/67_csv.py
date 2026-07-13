
'''

CSV - Arquivo de texto onde cada linha é um registro e os valores são
separados por vírgula ou ;. É o formato mais comum para planilhas e exportação
de dados.

- Ler CSV linha por linha - csv.reader()
- Ler CSV como dicionário - csv.DictReader()
- Escrever CSV - csv.writer()
- Escrever CSV com cabeçalho - csv.DictWriter()

'''

# Escrevendo um CSV

import csv

with open("usuarios.txt", "w", newline="") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(["nome", "idade", "cidade"]) # cabeçalho
    writer.writerow(["Miguel", 30, "Jundiaí"])

# O newline evia linhas em branco no windows

# Lendo um CSV

with open("usuarios.txt", "r") as arquivo:
    reader = csv.reader(arquivo)
    for linha in reader:
        print(linha["nome"], linha["idade"], linha["cidade"])

# Cada linha vira um dicionário usando o cabeçalho como chave

# Escrevendo dom DictWritter

campos = ["nome", "idade", "cidade"]

usuarios = [
    {"nome": "Miguel", "idade": 30, "cidade": "Jundiaí"},
    {"nome": "Ana",    "idade": 28, "cidade": "Campinas"},
]

with open("arquivo.txt", "w", newline="") as arquivo:
    writer = csv.DictWriter(arquivo, campos)
    writer.writeheader() # escrever o cabeçalho
    writer.writerow(usuarios) # escrever usuários
    


