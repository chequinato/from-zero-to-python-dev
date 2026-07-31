# if __name__ == "__main__"

# Todo arquivo .py tem a variável __name__
# Quando executado DIRETAMENTE → __name__ == "__main__"
# Quando importado por outro arquivo → __name__ == nome do módulo

# ENTENDENDO O CONCEITO

# Imagine dois arquivos:

# --- calculadora.py ---
# def somar(a, b):
#     return a + b
#
# def subtrair(a, b):
#     return a - b
#
# # Sem o if __name__:
# print(somar(10, 5))    # ← isso executa quando alguém importa o módulo!
# print(subtrair(10, 5)) # ← indesejado!

# --- main.py ---
# import calculadora   # ← os prints de calculadora.py executam aqui!

# Com if __name__:

# --- calculadora.py ---
# def somar(a, b):
#     return a + b
#
# def subtrair(a, b):
#     return a - b
#
# if __name__ == "__main__":
#     print(somar(10, 5))    # só executa se rodar calculadora.py diretamente
#     print(subtrair(10, 5)) # nunca executa quando importado

# DEMONSTRAÇÃO DIRETA

print(f"__name__ deste arquivo: {__name__}")
# Se rodar diretamente → __main__
# Se importar           → 63_name_main

# PADRÕES DE USO

# --- 1. Proteger código de teste ---
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    return "Obesidade"

if __name__ == "__main__":
    # Só executa ao rodar o arquivo diretamente
    imc = calcular_imc(80, 1.75)
    print(f"IMC: {imc:.2f}")
    print(f"Classificação: {classificar_imc(imc)}")

# --- 2. Ponto de entrada da aplicação ---
# main.py é o arquivo que inicia tudo

# --- main.py de uma aplicação real ---
# from app.services.usuario_service import UsuarioService
# from app.config import Config
#
# def iniciar():
#     config = Config()
#     service = UsuarioService(config)
#     service.executar()
#
# if __name__ == "__main__":
#     iniciar()

# --- 3. Script que também é módulo ---
# O mesmo arquivo serve como script E como módulo importável

def processar_dados(dados):
    return [x * 2 for x in dados if x > 0]

def gerar_relatorio(dados_processados):
    return {
        "total": len(dados_processados),
        "soma": sum(dados_processados),
        "media": sum(dados_processados) / len(dados_processados)
    }

if __name__ == "__main__":
    # Como script: executa o fluxo completo
    dados_brutos = [1, -2, 3, -4, 5, 6]
    processados = processar_dados(dados_brutos)
    relatorio = gerar_relatorio(processados)
    print(relatorio)

# Quando importado, só as funções ficam disponíveis:
# from 63_name_main import processar_dados, gerar_relatorio

# ESTRUTURA PROFISSIONAL

# Projeto real bem organizado:
#
# meu_projeto/
# ├── main.py              ← ponto de entrada, tem o if __name__
# ├── requirements.txt
# ├── .env
# └── app/
#     ├── __init__.py
#     ├── config.py        ← configurações
#     ├── services/
#     │   ├── __init__.py
#     │   └── processador.py
#     ├── models/
#     │   ├── __init__.py
#     │   └── dados.py
#     ├── utils/
#     │   ├── __init__.py
#     │   └── helpers.py
#     └── tests/
#         ├── __init__.py
#         └── test_processador.py

# main.py:
# from app.services.processador import Processador
#
# if __name__ == "__main__":
#     processador = Processador()
#     processador.executar()

# RESUMO

# __name__ == "__main__"  → arquivo foi executado diretamente
# __name__ == "modulo"    → arquivo foi importado

# Sempre use if __name__ == "__main__" para:
# Proteger código de teste/demo de ser executado ao importar
# Definir o ponto de entrada da aplicação
# Criar scripts que também funcionam como módulos importáveis