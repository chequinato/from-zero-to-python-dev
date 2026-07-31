
# EXCEPTIONS COMUNS DO PYTHON

# ValueError

# Tipo certo, valor errado
try:
    numero = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")   # invalid literal for int()

try:
    float("texto")
except ValueError as e:
    print(f"ValueError: {e}")

# Validação de domínio
def definir_idade(valor):
    idade = int(valor)   # pode lançar ValueError
    if idade < 0 or idade > 150:
        raise ValueError(f"Idade inválida: {valor}")
    return idade

try:
    definir_idade(-5)
except ValueError as e:
    print(e)

# TypeError

# Operação com tipo errado
try:
    resultado = "texto" + 5
except TypeError as e:
    print(f"TypeError: {e}")   # can only concatenate str (not "int")

try:
    len(42)
except TypeError as e:
    print(f"TypeError: {e}")   # object of type 'int' has no len()

# Parâmetro errado
try:
    def somar(a, b): return a + b
    somar(1, 2, 3)
except TypeError as e:
    print(f"TypeError: {e}")   # takes 2 positional arguments but 3 were given

# KeyError

# Chave não existe no dicionário
usuario = {"nome": "Miguel", "idade": 30}

try:
    print(usuario["email"])
except KeyError as e:
    print(f"KeyError: {e}")   # 'email'

# Evitando com get()
email = usuario.get("email", "não informado")
print(email)   # não informado → sem exceção

# IndexError

# Índice fora do range da lista
lista = [1, 2, 3]

try:
    print(lista[10])
except IndexError as e:
    print(f"IndexError: {e}")   # list index out of range

# Evitando
if len(lista) > 5:
    print(lista[5])
else:
    print("Índice não existe")

# AttributeError

# Atributo ou método não existe no objeto
try:
    texto = "Python"
    texto.inexistente()
except AttributeError as e:
    print(f"AttributeError: {e}")

# Muito comum com None
usuario = None

try:
    print(usuario.nome)
except AttributeError as e:
    print(f"AttributeError: {e}")   # 'NoneType' has no attribute 'nome'

# Verificando antes
if usuario is not None:
    print(usuario.nome)

# FileNotFoundError

try:
    with open("arquivo_inexistente.txt") as f:
        conteudo = f.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

# Verificando antes com pathlib
from pathlib import Path

caminho = Path("arquivo.txt")
if caminho.exists():
    conteudo = caminho.read_text()
else:
    print("Arquivo não existe")

# json.JSONDecodeError

import json

try:
    dados = json.loads("isso não é json {")
except json.JSONDecodeError as e:
    print(f"JSONDecodeError: {e}")

# Muito comum em APIs
def parsear_resposta(texto):
    try:
        return json.loads(texto)
    except json.JSONDecodeError:
        print("Resposta da API não é JSON válido")
        return None

# ZeroDivisionError

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Divisão por zero!")

# Verificando antes
divisor = 0
if divisor != 0:
    resultado = 10 / divisor
else:
    resultado = None

# NameError

# Variável não foi definida
try:
    print(variavel_inexistente)
except NameError as e:
    print(f"NameError: {e}")   # name 'variavel_inexistente' is not defined

# OverflowError e MemoryError

try:
    import math
    resultado = math.exp(1000)   # número enorme demais
except OverflowError as e:
    print(f"OverflowError: {e}")

# HIERARQUIA DAS EXCEPTIONS

# BaseException
# ├── SystemExit            → sys.exit()
# ├── KeyboardInterrupt     → Ctrl+C
# └── Exception             → base de todas as comuns
#     ├── ValueError
#     ├── TypeError
#     ├── KeyError
#     ├── IndexError
#     ├── AttributeError
#     ├── FileNotFoundError (→ OSError → Exception)
#     ├── ZeroDivisionError
#     ├── NameError
#     ├── OverflowError
#     ├── json.JSONDecodeError (→ ValueError)
#     └── StopIteration

# RESUMO: QUANDO CADA UM APARECE

# ValueError          → tipo certo, valor errado (int("abc"), idade=-1)
# TypeError           → tipo errado na operação ("a" + 1, len(42))
# KeyError            → chave ausente no dicionário
# IndexError          → índice fora do range da lista
# AttributeError      → atributo/método não existe, acesso em None
# FileNotFoundError   → arquivo ou diretório não encontrado
# JSONDecodeError     → string não é JSON válido
# ZeroDivisionError   → divisão por zero
# NameError           → variável não definida
# StopIteration       → iterator esgotado