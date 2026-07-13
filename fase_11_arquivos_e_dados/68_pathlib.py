
'''

Pathlib é a forma moderna de trabalhar com caminhos de arquivos e pastas em Python.
ANtes usava os.path com strings, hoje Path é o padrão.

Criamos um objeto Path e a partir dele faz tudo: verificar se existe, criar pasta, listar...

'''


# Criando um Path

from pathlib import Path

# Caminho relativo (a partir de onde o script roda)

pastas = Path('exemplo')
arquivo = Path("exemplo/usuarios.json")

# Navegando entre pastas

from pathlib import Path

base = Path("projeto")

arquivo_completo = base / "dados" / "usuarios.json"
print(arquivo_completo())

# O operador / é a grande sacada do pathlib, muito mais limpo que os.path.join()

# Informações sorbe o caminho

arquivo = Path("dados/usuarios.json")

print(arquivo.name)   # usuarios.json
print(arquivo.stem)   # usuarios
print(arquivo.suffix) # .json
print(arquivo.parent) # dados
print(arquivo.exists()) # True ou False
print(arquivo.is_file()) # True se for arquivo
print(arquivo.is_dir()) # True se for pasta

# Criando pastas e arquivos

pasta = Path("meus_dados")

pasta.mkdir(exist_ok=True) # cria a pasta, não dá erro se já existir

# Criando subpastas de uma vez

Path("a/b/c").mkdir(exist_ok=True, parents=True)

# Lendo e escrevendo direto pelo Path

arquivo = Path("notas.txt")

arquivo.write_text("Olá Miguel\n", encoding="utf-8")

# Ler

conteudo = arquivo.read_text(encoding="utf-8")
print(conteudo)

# Listando arquivos de uma pasta
pasta = Path(".")

# Todos os arquivos e pastas
for item in pasta.iterdir():
    print(item)
    
# Só arquivos .py

for item in pasta.glob("*.py"):
    print(item)

# Buscando em subpastas também
for arquivo in pasta.rglob("*.json"):
    print(arquivo)