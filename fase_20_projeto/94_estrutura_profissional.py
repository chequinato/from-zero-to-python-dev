# Estrutura Profissional de Projeto Python

"""
Estrutura recomendada para projetos Python profissionais,
seguindo as melhores práticas da comunidade.
"""

# ==================== ESTRUTURA DE DIRETÓRIOS ====================

"""
meu-projeto/
├── src/                      # Código fonte principal
│   ├── __init__.py
│   ├── main.py              # Ponto de entrada
│   ├── config/              # Configurações
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── models/              # Modelos de dados
│   │   ├── __init__.py
│   │   └── usuario.py
│   ├── services/            # Lógica de negócio
│   │   ├── __init__.py
│   │   └── usuario_service.py
│   ├── repositories/        # Acesso a dados
│   │   ├── __init__.py
│   │   └── usuario_repository.py
│   └── utils/               # Utilitários
│       ├── __init__.py
│       └── helpers.py
├── tests/                   # Testes
│   ├── __init__.py
│   ├── unit/               # Testes unitários
│   ├── integration/        # Testes de integração
│   └── conftest.py         # Configuração pytest
├── docs/                    # Documentação
│   └── api.md
├── scripts/                 # Scripts auxiliares
│   └── setup.py
├── .env                     # Variáveis de ambiente
├── .gitignore
├── requirements.txt         # Dependências
├── requirements-dev.txt     # Dependências de dev
├── pyproject.toml          # Configuração do projeto
├── README.md
└── LICENSE
"""

# ==================== CONFIGURAÇÃO (pyproject.toml) ====================

"""
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "meu-projeto"
version = "1.0.0"
description = "Descrição do projeto"
authors = [{name = "Seu Nome", email = "seu@email.com"}]
requires-python = ">=3.9"
dependencies = [
    "fastapi>=0.68.0",
    "uvicorn>=0.15.0",
    "pydantic>=1.8.0",
    "sqlalchemy>=1.4.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=6.0.0",
    "pytest-cov>=2.0.0",
    "black>=21.0.0",
    "mypy>=0.910",
    "flake8>=3.9.0",
]

[tool.black]
line-length = 100
target-version = ['py39']

[tool.mypy]
python_version = "3.9"
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
"""

# ==================== GITIGNORE ====================

"""
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Environment
.env
.env.local
.env.*.local

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/

# Logs
*.log
logs/
"""

# ==================== REQUIREMENTS.TXT ====================

"""
# requirements.txt - Dependências de produção
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
python-dotenv==1.0.0
boto3==1.29.0
requests==2.31.0
"""

# ==================== REQUIREMENTS-DEV.TXT ====================

"""
# requirements-dev.txt - Dependências de desenvolvimento
-r requirements.txt

pytest==7.4.3
pytest-cov==4.1.0
pytest-mock==3.12.0
black==23.11.0
mypy==1.7.1
flake8==6.1.0
isort==5.12.0
pre-commit==3.5.0
"""

# ==================== README.MD ====================

"""
# Meu Projeto

Descrição breve do projeto.

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\\Scripts\\activate  # Windows
pip install -r requirements.txt
```

## Configuração

```bash
cp .env.example .env
# Edite .env com suas configurações
```

## Execução

```bash
python -m src.main
```

## Testes

```bash
pytest
pytest --cov=src
```

## Desenvolvimento

```bash
# Formatar código
black src tests

# Verificar tipos
mypy src

# Verificar estilo
flake8 src tests
"""

# ==================== CONFTEST.PY ====================

"""
# tests/conftest.py - Configuração compartilhada de testes
import pytest
import os
from dotenv import load_dotenv

@pytest.fixture(scope="session", autouse=True)
def load_env():
    """Carrega variáveis de ambiente para testes"""
    load_dotenv(".env.test")

@pytest.fixture
def client():
    """Fixture para cliente de teste"""
    from src.main import app
    from fastapi.testclient import TestClient
    return TestClient(app)

@pytest.fixture
def db_session():
    """Fixture para sessão de banco de dados"""
    from src.database import get_session
    session = next(get_session())
    yield session
    session.rollback()
    session.close()
"""

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS PARA ESTRUTURA DE PROJETO:

1. Separe código fonte de testes e scripts
2. Use virtual environments isolados
3. Mantenha requirements.txt atualizado
4. Use .env para configurações sensíveis
5. Configure .gitignore adequadamente
6. Documente o projeto com README.md
7. Use type hints em todo o código
8. Configure ferramentas de qualidade (black, mypy, flake8)
9. Use CI/CD para automação
10. Siga convenções de nomenclatura Python
"""

if __name__ == "__main__":
    print("=== Estrutura Profissional de Projeto ===\n")
    print("Consulte os comentários no código para exemplos de:")
    print("- Estrutura de diretórios")
    print("- pyproject.toml")
    print("- .gitignore")
    print("- requirements.txt")
    print("- README.md")
    print("- conftest.py")