# ===================================
# FASE 12 - AMBIENTE PYTHON: VENV
# ===================================

# venv (virtual environment) cria um ambiente Python isolado pra cada projeto.
# Isso evita conflito entre versões de bibliotecas usadas em projetos diferentes.

# 1. Criar o ambiente virtual (cria uma pasta chamada "venv")
# python -m venv venv

# 2. Ativar o ambiente virtual
# No Windows:
# venv\Scripts\activate

# No Linux/Mac:
# source venv/bin/activate

# Quando ativado, o terminal mostra o nome do ambiente entre parênteses, tipo:
# (venv) usuario@maquina:~/projeto$

# 3. Desativar o ambiente virtual (volta pro Python global)
# deactivate

# Dica: sempre que for trabalhar num projeto, ativa o venv dele primeiro.
# Assim as bibliotecas instaladas ficam isoladas só naquele projeto.