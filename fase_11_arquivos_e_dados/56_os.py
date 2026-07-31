

'''

O módulo os é a interface do Python com o sistema operacional - navegar em pastas,
criar diretórios, renomear arquivos, ler variáveis de ambiente...

'''

import os

# Lendo uma variável de ambiente
valor = os.getenv("HOME")
print(valor)

# Com valor padrão se não existir
ambiente =  os.getenv("AMBIENTE", "desenvolvimento")
print(ambiente)

# Todas as variáveis de ambiente
print(os.environ) # dicionário com tudo
print(os.environ.get("HOME")) # acesso direto (erro se não existir)

# Usando AWS, por exemplo:

AWS_BUCKET = os.getenv("AWS_BUCKET_NAME")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Navegação de pastas

print(os.getcwd()) # pasta atual
os.chdir("outra pasta") # muda de pasta
print(os.listdir(".")) # lista arquivos e pastas do diretório atual

# Criando e removendo

os.mkdir("nova_pasta") # cria uma pasta
os.makedirs("a/b/c", exist_ok=True) # cria subpastas de uma vez
os.rename("antigo.txt", "novo.txt") # renomeia arquivo
os.remove("arquivo.txt") # deleta arquivo
os.rmdir("pasta_vazia") # deleta pasta vazia

# os.path (legado)

caminho = os.path("pasta", "arquivo.txt") # monta caminho
print(os.path.exists("arquivo.txt")) # True ou False
print(os.path.basename("/pasta/arquivo.txt"))    # arquivo.txt
print(os.path.dirname("/pasta/arquivo.txt")) # /pasta
print(os.path.splitext("arquivo.txt"))  # ('arquivo', '.txt')

# Informações do sistema

print(os.name)  # 'nt' no Windows, 'posix' no Linux/Mac
print(os.sep) # '/' no Linux, '\' no Windows
print(os.linesep)  # separador de linha do sistema