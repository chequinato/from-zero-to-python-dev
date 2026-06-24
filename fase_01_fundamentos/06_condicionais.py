
# Condicionais em Python

# if básico

idade = 20

if idade >= 18:
    print("aprovado")

saldo = 1400

if saldo >= 1500:
    print("aprovado")
else:
    print("reprovado")


# if / elif / else
nota = 7.5

if nota >= 9:
    print("A")
elif nota >= 7:
    print("B")
elif nota >= 5:
    print("C")
else:
    print("Reprovado")

# Condicionais aninhados
tem_conta = True
saldo = 200
valor_saque = 150

if tem_conta:
    if saldo >= valor_saque:
        print("Saque realizado")
    else:
        print("Saldo insuficiente")
else:
    print("Sem conta cadastrada")


tem_conta_2 = False
saldo = 100
valor_saque = 150

if tem_conta_2:
    if saldo >= valor_saque:
        print("Saque realizado")
    else:
        print("Saldo insuficiente")
else:
    print("Sem conta cadastrada")

# Ternário (if em uma linha)
# valor_se_true if condicao else valor_se_false

idade = 20
status = "maior" if idade >= 18 else "menor"
print(status)  # maior

preco = 100
desconto = 0.1 if preco > 50 else 0
print(f"Desconto: {desconto * 100}%")  # Desconto: 10.0%

# Condicionais com Truthy/Falsy
nome = ""

if nome:
    print(f"Olá, {nome}")
else:
    print("Nome não informado")  # cai aqui pois "" é Falsy

lista = [1, 2, 3]
if lista:
    print("Lista tem itens")  # cai aqui pois existe valores na lista

usuario = None
if usuario is None:
    print("Nenhum usuário logado")

# Exemplos reais

# Verificando permissão de acesso
perfil = "admin"
recurso = "deletar"

if perfil == "admin":
    print(f"Acesso liberado para {recurso}")
elif perfil == "editor":
    if recurso != "deletar":
        print("Acesso parcial liberado")
    else:
        print("Sem permissão para deletar")
else:
    print("Acesso negado")

# Classificando faixa etária
idade = 35

if idade < 12:
    faixa = "criança"
elif idade < 18:
    faixa = "adolescente"
elif idade < 60:
    faixa = "adulto"
else:
    faixa = "idoso"

print(f"Faixa etária: {faixa}")