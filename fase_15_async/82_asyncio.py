
'''

Conceito
asyncio é a biblioteca que gerencia a execução das coroutines —
ela decide quando cada tarefa assíncrona roda, pausa e retoma.
O grande poder dela aparece quando você tem várias tarefas rodando "ao mesmo tempo" em vez de uma de cada vez.

'''

# asyncio.run() - ponto de entrada
import asyncio

async def main():
    print("Iniciando...")

asyncio.run(main()) # cria o "loop de eventos" e roda a coroutine principal

# asyncio.gather() - rodando várias tarefas em paralelo

async def buscar_dado(nome, tempo):
    print(f"Buscando {nome}...")
    await asyncio.sleep(tempo)
    print(f"{nome} encontrado!")
    return f"dado de {nome}"

async def main():
    resultados = await asyncio.gather(
        buscar_dado("usuários", 2),
        buscar_dado("produtos", 1),
        buscar_dado("pedidos", 3)
    )
    print(resultados) # ['dado de usuarios', 'dado de produtos', 'dado de pedidos']

asyncio.run(main())

# asyncio.create_task() - disparando uma tarefa sem esperar na hora
async def tarefa_demorada():
    await asyncio.sleep(2)
    print("Tarefa concluída")

async def main():
    tarefa = asyncio.create_task(tarefa_demorada()) # já começa a rodar em background
    print("Fazendo outra coisa enquanto isso...")
    await tarefa # só aqui a gente espera ela terminar de fato

asyncio.run(main())

# Requests HTTP assíncronos de verdade

# pip install aiohttp
import aiohttp
import asyncio

async def buscar_url(sessao, url):
    async with sessao.get(url) as resposta:
        return await resposta.json()

async def main() :
    async with aiohttp.ClientSession() as sessao:
        resultados = await asyncio.gather(
            buscar_url(sessao, "https://jsonplaceholder.typicode.com/users/1"),
            buscar_url(sessao, "https://jsonplaceholder.typicode.com/users/2"),
        )
    print(resultados)

asyncio.run(main())