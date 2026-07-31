

# Parâmetros em Python

# Posicionais

# Ordem importa
def apresentar (nome, idade, cidade):
    print(f"{nome}, {idade} anos, mora em {cidade}")

apresentar("Miguel", 30, "Jundiaí")   # correto
apresentar(30, "Miguel", "Jundiaí")   # errado — idade e nome trocados

# Nomeados (KEYWORD ARGUMENTS)

# Permite passar em qualquer ordem
apresentar(cidade="Jundiaí", nome="Miguel", idade=30)

# Misturando posicionais e nomeados
# Posicionais SEMPRE antes dos nomeados

apresentar(cidade="Jundiaí", nome="Miguel", idade=30) # Correto

# apresentar(nome="Miguel", 30, "Jundiaí")    # SyntaxError

# Valores padrão
def criar_usuario (nome, perfil="viewer", ativo=True, nivel=1):
    return{
        "nome": nome,
        "perfil": perfil,
        "ativo": ativo,
        "nivel": nivel
    }

# Usando padrões
print(criar_usuario("Miguel"))
# {'nome': 'Miguel', 'perfil': 'viewer', 'ativo': True, 'nivel': 1}

# Sobrescrevendo um padrão
print(criar_usuario("João", perfil="admin"))
# {'nome': 'João', 'perfil': 'admin', 'ativo': True, 'nivel': 1}

# Sobrescrevendo todos
print(criar_usuario("Ana", "editor", False, 3))

# Armadilha do valor padrão mutável

# Errado: lista compartilhada entre chamadas!
def adicionar_errado(item, lista=[]):
    lista.append(item)
    return lista

print(adicionar_errado("a"))   # ['a']
print(adicionar_errado("b"))   # ['a', 'b'] → acumulou!
print(adicionar_errado("c"))   # ['a', 'b', 'c'] → bug!

# Correto: None como padrão, cria lista nova a cada chamada
def adicionar_certo(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista

print(adicionar_certo("a"))   # ['a']
print(adicionar_certo("b"))   # ['b'] → lista nova!
print(adicionar_certo("c"))   # ['c'] → lista nova!

# A mesma armadilha existe com dicionários e sets
# errado
def registrar_errado(chave, valor, dados={}):
    dados[chave] = valor
    return dados

# Parâmetros somente posicionais (/)
# O / indica que tudo antes dele só pode ser passado por posição

def potencia (base, expoente):
    return base ** expoente

print(potencia(1, 2)) # Correto
# print(potencia(base=2, expoente=10))  # TypeError

# Parâmetros somente nomeados (*)
# O * indica que tudo depois dele só pode ser passado por nome

# O * indica que tudo depois dele só pode ser passado por nome
def criar_relatorio(titulo, *, formato="pdf", paginas=1):
    return f"{titulo} | formato: {formato} | páginas: {paginas}"

print(criar_relatorio("Vendas"))    # Correto
print(criar_relatorio("Vendas", formato="xlsx"))  # Correto
# print(criar_relatorio("Vendas", "xlsx"))    # TypeError

# Exemplos reais

# Conexão com banco — nomeados evitam erros de ordem
def conectar_banco(*, host, porta, banco, usuario, senha):
    print(f"Conectando em {host}:{porta}/{banco}")

conectar_banco(
    host="localhost",
    porta=5432,
    banco="clientes",
    usuario="admin",
    senha="senha123"
)

# Função de envio de email com padrões úteis
def enviar_email(destinatario, assunto, corpo, copia=None,
                 formato="html", prioridade="normal"):
    print(f"Para: {destinatario}")
    print(f"Assunto: {assunto}")
    print(f"Formato: {formato}")
    print(f"Prioridade: {prioridade}")
    if copia:
        print(f"Cópia: {copia}")

