
# Comando WITH OPEN, leitura e escrita de arquivos em Python

# Escrevendo em um arquivo

with open("arquivo.txt", "w") as arquivo:
    arquivo.write("Miguel\n")
    arquivo.write("João\n")
    arquivo.write("Ana\n")

# Lendo um arquivo

with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Lendo linha por linha de um arquivo

with open("arquivo.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip()) # ['Miguel\n', 'João\n', 'Ana\n']

# Lendo as linhas como lista

with open("nomes.txt", "r") as arquivo:
    linhas = arquivo.readlines() # Lê todo o conteúdo do arquivo aberto e transforma em strings
    print(linhas) # ['Miguel\n', 'João\n', 'Ana\n']

# Adicionando sem apagar (append)

with open("arquivo.txt", "a") as arquivo:
    arquivo.write("Miguel\n")


