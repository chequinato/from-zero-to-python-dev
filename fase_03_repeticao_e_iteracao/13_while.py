from operator import truediv

# While em Python

# While executa enquanto a condição for True
# Use quando NÃO sabe quantas vezes vai repetir

# While básico

contador = 0

while contador < 5:
    print(contador)
    contador +=1 # SEMPRE lembre de atualizar a condição!
# Saída: 0 1 2 3 4

# While com condição composta

saldo = 1000
gasto = 0

while saldo > 0 and gasto < 800:
    saldo -= 100
    gasto += 100
    print(f"Saldo: {saldo}, Gasto: {gasto} " )

# While com flag (booleano de controle)

rodando = True
tentativas = 0

while rodando:
    tentativas += 1
    print(f"Tentativas: {tentativas}")
    if tentativas >= 3:
        rodando = False

print("Encerrado")

# While para validar entrada do usuário
# (simulando sem input() real)

senhas_testadas = ["errada", "errada", "correta"]
indice = 0
senha_correta = "correta"

while True:
    senha = senhas_testadas[indice]
    indice += 1
    if senha == senha_correta:
        print("Senha correta")
        break
print("Senha incorreta")

# While com else
# else executa quando o while termina NORMALMENTE (sem break)

contador = 0

while contador < 3:
    print(contador)
    contador += 1
else:
    print("While terminou")

# Cuidado: loop infinito
# Nunca faça isso sem um break:
# while True:
#     print("isso nunca para!")

# Correto: while True com break controlado

# Correto: while True com break controlado
tentativas = 0
max_tentativas = 3

while True:
    tentativas += 1
    print(f"Processando... tentativa {tentativas}")
    if tentativas >= max_tentativas:
        print("Máximo de tentativas atingido")
        break

# --- For vs While: quando usar cada um? ---
# For  → quando SABE quantas vezes vai repetir (percorrer lista, range)
# While → quando NÃO SABE (aguardar resposta, tentar até funcionar)