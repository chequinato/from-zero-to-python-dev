# ===================================
# FASE 12 - AMBIENTE PYTHON: REQUIREMENTS.TXT
# ===================================

# requirements.txt é um arquivo de texto que lista as bibliotecas
# usadas no projeto, junto com suas versões.
# Serve pra outra pessoa (ou você mesmo em outra máquina) recriar
# o mesmo ambiente rapidinho.

# 1. Gerar o requirements.txt com tudo que está instalado no venv atual
# pip freeze > requirements.txt

# 2. Exemplo de como o arquivo fica por dentro:
# requests==2.31.0
# python-dotenv==1.0.1
# flask==3.0.3

# 3. Instalar todas as dependências listadas no arquivo (em outra máquina/venv)
# pip install -r requirements.txt

# Dica: sempre atualiza o requirements.txt quando instalar um pacote novo.
# Isso mantém o projeto reprodutível pra qualquer pessoa que for rodar depois.