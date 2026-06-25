
# Break e continue

# break   → PARA o loop completamente
# continue → PULA para a próxima iteração

# Break

# Parando ao encontrar um valor
numeros = [1, 3, 5, 8, 9, 11]

for numero in numeros:
    if numero % 2 == 0:
        print(f"Primeiro par encontrado: {numero}")
        break  # para tudo ao achar o primeiro par

# Break em while (padrão usado)

tentativa = 0

while True:
    tentativa += 1
    print(f"Tentativa {tentativa}")
    if tentativa == 3:
        print("Sucesso!")
        break

# Break em loop aninhado (só para o loop mais interno)

for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(f"i={i}, j={j}")

# Buscando listas com break

usuarios = ["ana", "carlos", "miguel", "joao"]
busca = "miguel"
encontrado = False

for usuario in usuarios:
    if usuario == busca:
        encontrado = True
        break

if encontrado:
    print("Sucesso!")
else:
    print("Fracasso!")

# Continue

# Pulando números pares
for numero in range(1, 11):
    if numero % 2 == 0:
        continue # pula pares, continua o loop
    print(numero)

# Pulando valores inválidos

dados = [10, None, 20, None, 30, 0, 40]

total = 0

for dado in dados:
    if dado is None or dado == 0:
        continue
    total += dado

# Continue em while

contador = 0

while contador <10:
    contador += 1
    if contador % 3 == 0:
        continue # pula múltiplos de 3
    print(contador)

# Padrão real: validar e processar
pedidos = [
    {"id": 1, "valor": 150, "status": "aprovado"},
    {"id": 2, "valor": 80,  "status": "cancelado"},
    {"id": 3, "valor": 200, "status": "aprovado"},
    {"id": 4, "valor": 50,  "status": "pendente"},
]

total_aprovado = 0

for pedido in pedidos:
    if pedido["status"] != "aprovado":
        continue # Pula não aprovados
    total_aprovado += pedido["valor"]

print(f"Total aprovado: {total_aprovado}")

# For / wile com else

# else executa APENAS se o loop terminou sem break

# Exemplo: buscar item — else indica "não encontrado"

produtos = ["notebook", "mouse", "teclado"]
busca = "monitor"

for produto in produtos:
    if produto == busca:
        print(f"Produto: {produto}")
        break
else:
    print(f"{busca} não está na lista")