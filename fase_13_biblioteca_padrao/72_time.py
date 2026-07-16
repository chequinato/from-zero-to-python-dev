
'''

Conceito:
O módulo time trabalha com tempo em nível mais "baixo" que o datetime
é focado em timestamps (segundos desde 1970), pausas de execução e medição de performance.
Muito usado pra cronometrar código, criar delays e gerar timestamps simples.

'''

# Timestamp atual

import time

agora = time.time()
print(agora) # 1752678645.123456 → segundos desde 01/01/1970 (epoch)

# Pausando a execução - sleep
print("início")
time.sleep(2) # pausa o código por 2 segundos
print("fim")

# Medindo o tempo de execução
inicio = time.time()

fim = time.time()

soma = sum(range(1_000_000))
print(f"Tempo de execução: {fim - inicio:.4f} segundos ")

# Pra medir performance com mais precisão o ideal é o time.perf_counter()

inicio = time.perf_counter()
soma = sum(range(1_000_000))
fim =  time.perf_counter()

print(f"Tempo (perf_counter): {fim - inicio:.4f} segundos")

# Convertendo timestamp em data legível

timestamp = time.time()
data_local = time.localtime(timestamp)
print(data_local)  # struct_time com ano, mês, dia, hora...

data_formatada = time.strftime("%d/%m/%Y %H:%M:%S", data_local)
print(data_formatada)