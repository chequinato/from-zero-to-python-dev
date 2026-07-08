
# MÓDULOS PRÓPRIOS E PACKAGES

# Módulo  = qualquer arquivo .py
# Package = pasta com __init__.py

# MÓDULO PRÓPRIO

# Imagine que você tem essa estrutura:
#
# projeto/
# ├── main.py
# └── utils.py

# --- utils.py ---
# def somar(a, b):
#     return a + b
#
# def formatar_preco(valor):
#     return f"R${valor:.2f}"
#
# PI = 3.14159

# --- main.py ---
# import utils
# print(utils.somar(10, 5))         # 15
# print(utils.formatar_preco(99.9)) # R$99.90
# print(utils.PI)                   # 3.14159

# Ou com from:
# from utils import somar, formatar_preco
# print(somar(10, 5))

# PACKAGE (PACOTE)

# Package = pasta com __init__.py dentro
# Permite organizar módulos em grupos

# Estrutura de um projeto real:
#
# meu_projeto/
# ├── main.py
# └── app/
#     ├── __init__.py          ← transforma a pasta em package
#     ├── services/
#     │   ├── __init__.py
#     │   ├── usuario_service.py
#     │   └── email_service.py
#     ├── models/
#     │   ├── __init__.py
#     │   └── usuario.py
#     └── utils/
#         ├── __init__.py
#         └── formatadores.py

# __init__.py

# __init__.py pode estar vazio (só marca como package)
# ou pode expor o que o package oferece

# --- app/models/__init__.py ---
# from .usuario import Usuario
# from .produto import Produto
#
# Agora de fora você faz:
# from app.models import Usuario   (em vez de app.models.usuario)

# --- app/services/__init__.py ---
# from .usuario_service import UsuarioService
# from .email_service import EmailService


# IMPORTANDO DE PACKAGES


# Importação absoluta (recomendada)
# from app.services.usuario_service import UsuarioService
# from app.models.usuario import Usuario

# Importação relativa (dentro do package)
# Em usuario_service.py:
# from ..models.usuario import Usuario   # sobe um nível, entra em models

# EXEMPLO PRÁTICO COMPLETO


# Estrutura:
# financeiro/
# ├── __init__.py
# ├── calculos.py
# ├── formatadores.py
# └── validadores.py

# --- financeiro/calculos.py ---
# def calcular_juros(principal, taxa, periodo):
#     return principal * (1 + taxa) ** periodo
#
# def calcular_desconto(preco, percentual):
#     return preco * (1 - percentual / 100)

# --- financeiro/formatadores.py ---
# def formatar_moeda(valor):
#     return f"R${valor:,.2f}"
#
# def formatar_percentual(valor):
#     return f"{valor:.1f}%"

# --- financeiro/__init__.py ---
# from .calculos import calcular_juros, calcular_desconto
# from .formatadores import formatar_moeda, formatar_percentual

# --- main.py ---
# import financeiro
# resultado = financeiro.calcular_juros(1000, 0.05, 12)
# print(financeiro.formatar_moeda(resultado))
#
# Ou:
# from financeiro import calcular_juros, formatar_moeda
# print(formatar_moeda(calcular_juros(1000, 0.05, 12)))


# ATRIBUTOS DE MÓDULO

import math

print(math.__name__)   # math → nome do módulo
print(math.__file__)   # caminho do arquivo .py
print(dir(math))       # lista tudo que o módulo oferece

# Descobrindo o que um módulo tem
import json
atributos = [a for a in dir(json) if not a.startswith("_")]
print(atributos)   # ['JSONDecodeError', 'JSONDecoder', 'dumps', 'loads'...]

# RECARREGANDO MÓDULO

# Python cacheia módulos no sys.modules
# Se modificar o arquivo, precisa recarregar
import importlib
import math

importlib.reload(math)   # força recarregar (raro na prática)