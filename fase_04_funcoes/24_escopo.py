

# Escopo em Python

# Escopo define onde uma variável pode ser acessada
# Python usa a regra LEGB:
# L → Local
# E → Enclosing (função exterior)
# G → Global
# B → Built-in (print, len, type...)

# Local
def minha_funcao():
    variavel_local = "só existo aqui dentro"
    print(variavel_local) # funciona

minha_funcao()
# print(variavel_local)  # NameError — não existe fora

def contador():
    total = 0
    total += 1
    return total

print(contador())  # 1
print(contador())  # 1 → sempre começa do zero

# Global
nome_global = "Miguel"
versao = "1.0.0"

def mostrar():
    print(nome_global)  # pode LER variável global
    print(versao)       # pode LER variável global

mostrar()

# Tentando modificar global sem declarar
contador_global = 0

def incrementar_errado():
    # contador_global += 1  # UnboundLocalError!
    # Python acha que é local pois está sendo atribuída
    pass

# Modificando global com global keyword
def incrementar():
    global contador_global
    contador_global += 1

incrementar()
incrementar()
print(contador_global) # 2

#  Use global com moderação, dificulta testes e manutenção


# Melhor alternativa: passar e retornar
def incrementar_melhor(contador):
    return contador + 1

contador = 0
contador = incrementar_melhor(contador)
contador = incrementar_melhor(contador)
print(contador)  # 2

# Enclosing (LEGB - E)
# Variável da função exterior visível na interior
def exterior():
    mensagem = "Olá do exterior"

    def interior():
        print(mensagem)  # acessa variável do escopo enclosing

    interior()

exterior()

# Modificando variável enclosing com nonlocal

def criar_contador():
    total = 0

    def incrementar():
        nonlocal total  # acessa e modifica a variável do escopo a
        total += 1
        return total

    return incrementar

contar = criar_contador()
print(contar())  # 1
print(contar())  # 2
print(contar())  # 3

# Built-in (LEGB - E)

# Python tem funções built-in disponíveis em qualquer escopo
print(len([1, 2, 3]))   # len é built-in
print(type("texto"))    # type é built-in
print(range(5))         # range é built-in

# Cuidado: não sobrescreva built-ins!
# list = [1, 2, 3]   # Errado - agora 'list' não é mais a função built-in
# print = "texto"    # Errado - agora 'print' não funciona mais

# Regra LEGB na prática

x = "global"

def exterior():
    x = "enclosing"

    def interior():
        x = "local"
        print(x)   # local → encontrou no escopo L primeiro

    interior()
    print(x)       # enclosing → escopo L de exterior()

exterior()
print(x)           # global → escopo G

# Se não existir local:
y = "global"

def mostrar_y():
    print(y)   # global → não achou local, subiu para G

mostrar_y()

# Escopos em loops e condicionais

# Em Python, if/for/while NÃO criam escopo próprio!
for i in range(5):
    ultimo = i

print(ultimo)  # 4 → variável existe fora do for!
print(i)       # 4 → i também existe fora!

if True:
    criada_no_if = "existo fora do if"

print(criada_no_if)  # funciona, diferente de outras linguagens!
