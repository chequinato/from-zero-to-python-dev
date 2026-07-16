# ===================================
# FASE 12 - AMBIENTE PYTHON: PIP
# ===================================

# pip é o gerenciador de pacotes/bibliotecas do Python.
# Ele instala, atualiza e remove pacotes de dentro do venv ativado.

# 1. Instalar um pacote
# pip install nome_do_pacote

# Exemplo:
# pip install requests

# 2. Instalar uma versão específica
# pip install requests==2.31.0

# 3. Listar os pacotes instalados no ambiente atual
# pip list

# 4. Ver detalhes de um pacote específico
# pip show requests

# 5. Atualizar um pacote
# pip install --upgrade requests

# 6. Remover um pacote
# pip uninstall requests

# 7. "Fotografar" todos os pacotes instalados e suas versões
# pip freeze

# Dica: sempre roda o pip com o venv ativado, senão instala no Python global
# e perde a isolação que o venv oferece.