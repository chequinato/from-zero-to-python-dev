

'''

Conceito
Variáveis de ambiente são valores que vivem no sistema operacional,
não dentro do seu código nem só num arquivo .env.
O .env + python-dotenv é só uma forma prática de carregar essas variáveis pro ambiente durante o desenvolvimento
mas em produção (servidor, AWS, Docker), elas geralmente já são setadas direto no sistema.

O Python acessa isso tudo do mesmo jeito: com os.environ ou os.getenv.
'''

# Setando uma variável de ambiente direto no terminal sem .env:
set MINHA_VARIAVEL=valor123 # isso só vale para aquela sessão do terminal

import os

# Forma 1 -  Retorna o valor da variável ou None (ou um valor padrão, se informado).
valor = os.getenv("MINHA_VARIAVEL")
print(valor)

# Forma 2 - os.environ: Faz praticamente a mesma coisa que o getenv().
valor2 = os.environ.get("MINHA_VARIAVEL2")
print(valor2)

# Forma 3 - acesso direto, dá erro se não existir
valor3 = os.environ["MINHA_VARIAVEL"]
print(valor3)


