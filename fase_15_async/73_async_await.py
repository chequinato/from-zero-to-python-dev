
'''

Async/await é um jeito de escrever código assíncrono — ou seja, código que consegue "pausar" enquanto espera algo demorado
(uma requisição de rede, leitura de arquivo, consulta a banco) e deixar outras tarefas rodarem nesse meio tempo, em vez de ficar travado esperando.

'''

import asyncio

async def dizer_ola():
    print("inicio")
    await asyncio.sleep(2)   # "pausa" aqui, sem travar o programa inteiro
    print("fim")

# uma função async não roda sozinha só chamando ela — precisa de asyncio.run
asyncio.run(dizer_ola())

# Diferente do time.sleep(2), o asyncio sleep só libera aquela tarefa específica, deixando as outras rodarem enquanto isso.

# await - só funciona dentro de função async

async def buscar_dado():
    await asyncio.sleep(1)
    return "dado encontrado"

async def main():
    resultado = await buscar_dado() # espera a coroutine terminar
    print(resultado)

asyncio.run(main())

# Comparando o código síncrono normal

# SÍNCRONO - cada chamada espera a anterior terminar
import time

# SÍNCRONO - cada chamada espera a anterior terminar
def buscar_sincrono():
    time.sleep(2)
    return "dado"

inicio = time.time()
buscar_sincrono()
buscar_sincrono()
buscar_sincrono()
print(time.time() - inicio)  # ~6 segundos (2+2+2, um de cada vez)

# Com async, rodando 3 tarefas "esperando" ao mesmo tempo, dá pra fazer isso em 2s em vez de 6.