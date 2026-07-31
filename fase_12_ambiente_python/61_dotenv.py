
'''

Conceito:
dotenv (biblioteca python-dotenv) serve pra você guardar informações sensíveis ou que mudam por ambiente como
senha de banco, chave de API, URL de conexão — fora do código, num arquivo separado chamado .env.
Assim você nunca comita senha no GitHub por acidente, e consegue trocar valores sem mexer no código Python.

Passo 1 — instalar a biblioteca
pip install python-dotenv

Passo 2 - criar arquivo .env
Na raiz do projeto, cria um arquivo chamado .env (sem extensão nenhuma, só isso mesmo) com esse conteúdo:

NOME_BANCO=meu_banco_de_dados
SENHA_API=abc123senhasecreta

Passo 3 — carregar e ler as variáveis no Python

Importante: nunca subir o .env para o git. Sempre adicionar no .gitignore.
'''

from dotenv import load_dotenv
import os

load_dotenv() # carrega todo o conteúdo do arquivo .env pro ambiente

valor = os.getenv("SENHA_API")
print(valor)

