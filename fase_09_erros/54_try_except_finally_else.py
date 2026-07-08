
# TRY / EXCEPT / FINALLY / ELSE

# try     → código que pode falhar
# except  → o que fazer se falhar
# else    → executa se NÃO houve erro
# finally → executa SEMPRE, com ou sem erro

# TRY / EXCEPT BÁSICO

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero!")

# Capturando o erro
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Erro capturado: {e}")   # division by zero

# MÚLTIPLOS EXCEPT

def processar(valor):
    try:
        numero = int(valor)
        resultado = 100 / numero
        return resultado
    except ValueError:
        print("Erro: valor não é um número")
    except ZeroDivisionError:
        print("Erro: não pode dividir por zero")

processar("abc")   # ValueError
processar("0")     # ZeroDivisionError
processar("5")     # funciona: 20.0

# Capturando múltiplos em um except só
try:
    numero = int("abc")
except (ValueError, TypeError) as e:
    print(f"Erro de tipo ou valor: {e}")

# EXCEPT GENÉRICO (use com moderação)

try:
    resultado = 10 / 0
except Exception as e:
    print(f"Algum erro: {type(e).__name__} - {e}")

# ⚠Evite except "pelado" — captura ATÉ KeyboardInterrupt e SystemExit
# try:
#     ...
# except:       # nunca faça isso
#     pass

# ELSE

# else → executa APENAS se nenhum erro ocorreu no try
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Não pode dividir por zero")
    else:
        print(f"Resultado: {resultado}")   # só chega aqui se não houve erro
        return resultado

dividir(10, 2)   # Resultado: 5.0
dividir(10, 0)   # Não pode dividir por zero

# FINALLY

# finally → executa SEMPRE, com ou sem erro
# Muito usado para liberar recursos (fechar arquivo, conexão, etc)

def ler_arquivo(caminho):
    arquivo = None
    try:
        arquivo = open(caminho, "r")
        conteudo = arquivo.read()
        return conteudo
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")
    finally:
        if arquivo:
            arquivo.close()   # fecha SEMPRE, mesmo se der erro
            print("Arquivo fechado")

ler_arquivo("inexistente.txt")
# Arquivo não encontrado: inexistente.txt
# Arquivo fechado → finally executou!

# BLOCO COMPLETO

def buscar_usuario(id):
    print(f"Iniciando busca do usuário {id}")
    try:
        usuarios = {1: "Miguel", 2: "João"}
        usuario = usuarios[id]            # pode lançar KeyError
        nome = usuario.upper()            # pode lançar AttributeError
    except KeyError:
        print(f"Usuário {id} não encontrado")
        return None
    except AttributeError:
        print("Erro ao processar nome do usuário")
        return None
    else:
        print(f"Usuário encontrado: {nome}")   # só se deu tudo certo
        return nome
    finally:
        print("Busca finalizada\n")   # sempre

buscar_usuario(1)
buscar_usuario(99)

# WITH STATEMENT (gerenciador de contexto)

# Forma moderna e pythônica de garantir finally automático
# Substitui o padrão try/finally para recursos

# Jeito antigo
try:
    arquivo = open("dados.txt", "w")
    arquivo.write("conteúdo")
finally:
    arquivo.close()

# Jeito moderno com with
with open("dados.txt", "w") as arquivo:
    arquivo.write("conteúdo")
# arquivo.close() chamado automaticamente ao sair do with

# ENCADEANDO TRATAMENTOS
import json

def processar_payload(payload_str):
    try:
        dados = json.loads(payload_str)
    except json.JSONDecodeError as e:
        print(f"JSON inválido: {e}")
        return None

    try:
        nome = dados["nome"]
        idade = int(dados["idade"])
    except KeyError as e:
        print(f"Campo obrigatório ausente: {e}")
        return None
    except ValueError:
        print("Idade deve ser um número")
        return None

    return {"nome": nome, "idade": idade}

print(processar_payload('{"nome": "Miguel", "idade": "30"}'))
print(processar_payload('{"nome": "João"}'))
print(processar_payload("json inválido {"))