# Pytest - Framework de Testes

"""
Pytest é um framework de testes que torna testes simples e escaláveis.
Suporta testes unitários, funcionais e de integração.
"""

import pytest

# ==================== ESTRUTURA DE TESTE ====================

def test_simples():
    """Teste simples básico"""
    assert 1 + 1 == 2

def test_com_parametro():
    """Teste que usa parâmetros"""
    resultado = soma(2, 3)
    assert resultado == 5

def soma(a, b):
    """Função auxiliar para testes"""
    return a + b

# ==================== PARAMETRIZAÇÃO ====================

@pytest.mark.parametrize("a, b, esperado", [
    (1, 2, 3),
    (2, 3, 5),
    (5, 5, 10),
    (-1, 1, 0),
])
def test_soma_parametrizada(a, b, esperado):
    """Teste parametrizado - roda múltiplas vezes com diferentes valores"""
    assert soma(a, b) == esperado

@pytest.mark.parametrize("entrada, esperado", [
    ("hello", "HELLO"),
    ("world", "WORLD"),
    ("python", "PYTHON"),
])
def test_maiusculas(entrada, esperado):
    """Teste parametrizado para strings"""
    assert entrada.upper() == esperado

# ==================== FIXTURES ====================

@pytest.fixture
def lista_exemplo():
    """Fixture que fornece uma lista para testes"""
    return [1, 2, 3, 4, 5]

def test_usando_fixture(lista_exemplo):
    """Teste que usa uma fixture"""
    assert len(lista_exemplo) == 5
    assert 3 in lista_exemplo

@pytest.fixture
def dicionario_exemplo():
    """Fixture que fornece um dicionário"""
    return {"nome": "João", "idade": 30}

def test_fixture_dicionario(dicionario_exemplo):
    """Teste usando fixture de dicionário"""
    assert dicionario_exemplo["nome"] == "João"
    assert dicionario_exemplo["idade"] == 30

# ==================== FIXTURES COM ESCOPO ====================

@pytest.fixture(scope="module")
def conexao_banco():
    """Fixture com escopo de módulo - executa uma vez por módulo"""
    print("\nConfigurando conexão com banco...")
    yield {"conexao": "mock_conexao"}
    print("Fechando conexão com banco...")

def test_usando_conexao(conexao_banco):
    """Teste usando fixture de conexão"""
    assert conexao_banco["conexao"] == "mock_conexao"

# ==================== FIXTURES COM SETUP/TEARDOWN ====================

@pytest.fixture
def arquivo_temporario(tmp_path):
    """Fixture que usa tmp_path do pytest para arquivos temporários"""
    arquivo = tmp_path / "teste.txt"
    arquivo.write_text("conteúdo de teste")
    return arquivo

def test_arquivo_temporario(arquivo_temporario):
    """Teste usando arquivo temporário"""
    conteudo = arquivo_temporario.read_text()
    assert conteudo == "conteúdo de teste"
    assert arquivo_temporario.exists()

# ==================== MARKERS ====================

@pytest.mark.slow
def test_lento():
    """Teste marcado como lento"""
    import time
    time.sleep(0.1)
    assert True

@pytest.mark.integracao
def test_integracao():
    """Teste marcado como integração"""
    assert True

@pytest.mark.unitario
def test_unitario():
    """Teste marcado como unitário"""
    assert 1 + 1 == 2

# ==================== SKIP E XFAIL ====================

@pytest.mark.skip(reason="Funcionalidade não implementada ainda")
def test_nao_implementado():
    """Teste que será pulado"""
    assert False

@pytest.mark.skipif(
    True,
    reason="Condição para pular teste"
)
def test_skip_condicional():
    """Teste pulado condicionalmente"""
    assert True

@pytest.mark.xfail
def test_falha_esperada():
    """Teste que deve falhar (xfail)"""
    assert False

@pytest.mark.xfail(reason="Bug conhecido")
def test_bug_conhecido():
    """Teste marcado como falha esperada devido a bug"""
    assert 1 == 2

# ==================== CAPTURA DE OUTPUT ====================

def test_captura_output(capsys):
    """Teste que captura stdout/stderr"""
    print("Mensagem de teste")
    captured = capsys.readouterr()
    assert "Mensagem de teste" in captured.out

def test_captura_log(caplog):
    """Teste que captura logs"""
    import logging
    logging.getLogger().warning("Mensagem de warning")
    assert "Mensagem de warning" in caplog.text

# ==================== TESTES DE EXCEÇÃO ====================

def divisao_por_zero():
    """Função que lança exceção"""
    return 1 / 0

def test_excecao():
    """Teste que verifica se exceção é lançada"""
    with pytest.raises(ZeroDivisionError):
        divisao_por_zero()

def test_excecao_com_mensagem():
    """Teste que verifica mensagem da exceção"""
    with pytest.raises(ValueError) as exc_info:
        int("não é número")
    
    assert "invalid literal" in str(exc_info.value)

# ==================== TESTES DE AVISOS ====================

def test_aviso():
    """Teste que verifica warnings"""
    import warnings
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        warnings.warn("Aviso de teste")
        assert len(w) == 1
        assert "Aviso de teste" in str(w[0].message)

# ==================== HOOKS ====================

def pytest_configure(config):
    """Hook executado antes da coleta de testes"""
    print("\nConfigurando pytest...")

def pytest_collection_finish(session):
    """Hook executado após coleta de testes"""
    print(f"\nColetados {len(session.items)} testes")

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS PYTEST:

1. Use nomes descritivos para funções de teste (test_*)
2. Use fixtures para setup e teardown
3. Parametrize testes para reduzir duplicação
4. Use markers para categorizar testes (unit, integration, slow)
5. Mantenha testes independentes
6. Use capsys/caplog para testar output
7. Use pytest.raises para testar exceções
8. Configure pytest.ini para configurações globais
9. Use conftest.py para fixtures compartilhadas
10. Mantenha testes rápidos e focados
"""

if __name__ == "__main__":
    # Para rodar os testes: pytest fase_18_testes_pytest/86_pytest.py -v
    print("Execute: pytest fase_18_testes_pytest/86_pytest.py -v")
    print("Para rodar apenas testes marcados: pytest -m unitario")
    print("Para pular testes lentos: pytest -m 'not slow'")