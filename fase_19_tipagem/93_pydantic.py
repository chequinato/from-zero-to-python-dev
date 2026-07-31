# Pydantic - Validação de Dados com Type Hints

"""
Pydantic é uma biblioteca de validação de dados que usa type hints
para validar e converter dados automaticamente.
"""

from pydantic import BaseModel, Field, validator, EmailStr, HttpUrl
from typing import Optional, List
from datetime import datetime

# ==================== MODELO BÁSICO ====================

class Usuario(BaseModel):
    """Modelo básico de usuário"""
    nome: str
    idade: int
    email: Optional[str] = None

# Criar instância
usuario = Usuario(nome="João", idade=30, email="joao@example.com")
print(usuario)
print(usuario.json())
print(usuario.dict())

# ==================== VALIDAÇÃO AUTOMÁTICA ====================

class Produto(BaseModel):
    """Modelo com validação automática"""
    nome: str
    preco: float
    estoque: int = Field(default=0, ge=0)  # ge = greater or equal

try:
    produto_valido = Produto(nome="Notebook", preco=2999.99, estoque=10)
    print(f"Produto válido: {produto_valido}")
    
    # Isso vai falhar validação
    produto_invalido = Produto(nome="Mouse", preco=-50, estoque=-5)
except Exception as e:
    print(f"Erro de validação: {e}")

# ==================== TIPOS ESPECIAIS ====================

class Contato(BaseModel):
    """Modelo com tipos especiais do pydantic"""
    nome: str
    email: EmailStr
    website: Optional[HttpUrl] = None

try:
    contato = Contato(
        nome="Empresa",
        email="contato@empresa.com",
        website="https://empresa.com"
    )
    print(f"Contato válido: {contato}")
except Exception as e:
    print(f"Erro: {e}")

# ==================== VALIDATORS CUSTOMIZADOS ====================

class Pessoa(BaseModel):
    """Modelo com validators customizados"""
    nome: str
    idade: int
    
    @validator('idade')
    def validar_idade(cls, v):
        """Valida que idade é positiva e razoável"""
        if v < 0:
            raise ValueError('Idade não pode ser negativa')
        if v > 150:
            raise ValueError('Idade inválida')
        return v
    
    @validator('nome')
    def validar_nome(cls, v):
        """Valida que nome não está vazio"""
        if not v or len(v.strip()) == 0:
            raise ValueError('Nome não pode estar vazio')
        return v.strip()

try:
    pessoa = Pessoa(nome="  João  ", idade=30)
    print(f"Pessoa válida: {pessoa}")
except Exception as e:
    print(f"Erro: {e}")

# ==================== MODELOS ANINHADOS ====================

class Endereco(BaseModel):
    """Modelo de endereço"""
    rua: str
    numero: int
    cidade: str
    estado: str

class Cliente(BaseModel):
    """Modelo de cliente com endereço aninhado"""
    nome: str
    email: EmailStr
    endereco: Endereco

cliente = Cliente(
    nome="Maria",
    email="maria@example.com",
    endereco={
        "rua": "Rua das Flores",
        "numero": 123,
        "cidade": "São Paulo",
        "estado": "SP"
    }
)
print(f"Cliente: {cliente}")

# ==================== LISTAS E MODELOS ====================

class Pedido(BaseModel):
    """Modelo de pedido"""
    itens: List[str]
    total: float

pedido = Pedido(
    itens=["Notebook", "Mouse", "Teclado"],
    total=3500.00
)
print(f"Pedido: {pedido}")

# ==================== CAMPOS OPCIONAIS ====================

class Configuracao(BaseModel):
    """Modelo com campos opcionais"""
    host: str = "localhost"
    porta: int = 8080
    debug: bool = False
    timeout: Optional[int] = None

config = Configuracao()
print(f"Config padrão: {config}")

config_custom = Configuracao(host="192.168.1.1", porta=3000, debug=True)
print(f"Config custom: {config_custom}")

# ==================== FIELD COM VALIDAÇÃO ====================

class ProdutoAvancado(BaseModel):
    """Modelo com Field para validação avançada"""
    nome: str = Field(..., min_length=1, max_length=100)
    descricao: Optional[str] = Field(None, max_length=500)
    preco: float = Field(..., gt=0, description="Preço deve ser positivo")
    estoque: int = Field(default=0, ge=0, le=1000)

try:
    produto = ProdutoAvancado(
        nome="Smartphone",
        descricao="Smartphone de última geração",
        preco=1999.99,
        estoque=50
    )
    print(f"Produto avançado: {produto}")
except Exception as e:
    print(f"Erro: {e}")

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS PARA PYDANTIC:

1. Use BaseModel para estruturas de dados complexas
2. Use Field para validação de campos individuais
3. Use validators para lógica de validação complexa
4. Use tipos especiais (EmailStr, HttpUrl) quando apropriado
5. Documente modelos com docstrings
6. Use modelos aninhados para estruturas complexas
7. Forneça valores padrão quando apropriado
8. Use Optional para campos que podem ser None
9. Valide dados de entrada com pydantic
10. Use pydantic para APIs (FastAPI, etc)
"""

if __name__ == "__main__":
    print("=== Pydantic Examples ===\n")
    
    # Exemplos básicos
    usuario = Usuario(nome="João", idade=30)
    print(f"Usuário: {usuario}")
    print(f"JSON: {usuario.json()}")
    print(f"Dict: {usuario.dict()}")
    
    # Exemplo de validação
    try:
        produto = Produto(nome="Notebook", preco=2999.99, estoque=10)
        print(f"\nProduto válido: {produto}")
    except Exception as e:
        print(f"\nErro: {e}")
    
    # Exemplo de validator
    try:
        pessoa = Pessoa(nome="João", idade=30)
        print(f"\nPessoa válida: {pessoa}")
    except Exception as e:
        print(f"\nErro: {e}")
