# Pytest Assertions - Asserções e Testes

"""
Pytest fornece uma maneira simples e poderosa de escrever testes
com assertions que são fáceis de ler e entender.
"""

# ==================== ASSERTIONS BÁSICAS ====================

def test_assertions_basicas():
    """Assertions básicas do pytest"""
    # Igualdade
    assert 1 == 1
    assert "hello" == "hello"
    
    # Diferença
    assert 1 != 2
    assert "hello" != "world"
    
    # Maior/Menor
    assert 10 > 5
    assert 5 < 10
    assert 10 >= 10
    assert 5 <= 10
    
    # Booleanos
    assert True
    assert not False
    assert bool(1)
    assert not bool(0)
    
    # None
    assert None is None
    assert "hello" is not None
    
    # Contém
    assert 1 in [1, 2, 3]
    assert "a" in "abc"
    assert "key" in {"key": "value"}

# ==================== ASSERTIONS DE COLEÇÕES ====================

def test_assertions_colecoes():
    """Assertions para coleções"""
    # Listas
    lista = [1, 2, 3]
    assert len(lista) == 3
    assert 1 in lista
    assert 4 not in lista
    
    # Dicionários
    dicionario = {"a": 1, "b": 2}
    assert "a" in dicionario
    assert dicionario["a"] == 1
    assert len(dicionario) == 2
    
    # Sets
    conjunto = {1, 2, 3}
    assert 1 in conjunto
    assert len(conjunto) == 3

# ==================== ASSERTIONS DE EXCEÇÕES ====================

def test_assertions_excecoes():
    """Testando exceções"""
    # Usando pytest.raises
    import pytest
    
    with pytest.raises(ValueError):
        int("não é número")
    
    with pytest.raises(ZeroDivisionError):
        1 / 0
    
    # Verificando mensagem da exceção
    with pytest.raises(ValueError) as exc_info:
        int("abc")
    
    assert "invalid literal" in str(exc_info.value)

# ==================== ASSERTIONS DE TIPOS ====================

def test_assertions_tipos():
    """Testando tipos"""
    assert isinstance(1, int)
    assert isinstance("hello", str)
    assert isinstance([1, 2], list)
    assert isinstance({"a": 1}, dict)
    
    assert type(1) is int
    assert type("hello") is str

# ==================== ASSERTIONS DE APROXIMAÇÃO ====================

def test_assertions_aproximacao():
    """Testando valores aproximados"""
    import math
    
    # Para floats
    assert 0.1 + 0.2 == pytest.approx(0.3)
    assert 3.14159 == pytest.approx(3.14, rel=0.01)
    
    # Para listas
    assert [0.1 + 0.2, 0.3] == pytest.approx([0.3, 0.3])

# ==================== ASSERTIONS CUSTOMIZADAS ====================

def test_assertions_customizadas():
    """Assertions customizadas com mensagens"""
    x = 5
    y = 10
    
    # Com mensagem customizada
    assert x < y, f"{x} deveria ser menor que {y}"
    
    # Verificação complexa
    resultado = [1, 2, 3]
    assert all(isinstance(x, int) for x in resultado), "Todos os elementos devem ser inteiros"
    assert len(resultado) > 0, "A lista não deve estar vazia"

# ==================== ASSERTIONS DE OBJETOS ====================

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __eq__(self, other):
        return self.nome == other.nome and self.idade == other.idade

def test_assertions_objetos():
    """Testando objetos"""
    p1 = Pessoa("João", 30)
    p2 = Pessoa("João", 30)
    p3 = Pessoa("Maria", 25)
    
    assert p1 == p2
    assert p1 != p3
    assert p1.nome == "João"
    assert p1.idade == 30

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS PARA ASSERTIONS:

1. Use uma assert por teste para clareza
2. Use mensagens descritivas em asserts complexos
3. Prefira assert x == y em vez de assert True se x == y
4. Use pytest.approx para comparações de floats
5. Use pytest.raises para testar exceções
6. Evite asserts múltiplos em uma linha
7. Teste comportamento, não implementação
8. Use fixtures para setup de testes
9. Mantenha testes independentes
10. Use nomes descritivos para funções de teste
"""

if __name__ == "__main__":
    # Para rodar os testes: pytest fase_18_testes_pytest/85_assertions.py -v
    print("Execute: pytest fase_18_testes_pytest/85_assertions.py -v")