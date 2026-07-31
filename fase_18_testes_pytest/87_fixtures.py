# Pytest Fixtures - Setup e Teardown de Testes

"""
Fixtures são funções que fornecem um estado fixo, baseline ou contexto
para os testes. Elas são usadas para setup e teardown de recursos.
"""

import pytest
from datetime import datetime

# ==================== FIXTURE BÁSICA ====================

@pytest.fixture
def dados_exemplo():
    """Fixture básica que retorna dados simples"""
    return {"nome": "João", "idade": 30}

def test_usando_fixture_basica(dados_exemplo):
    """Teste usando fixture básica"""
    assert dados_exemplo["nome"] == "João"
    assert dados_exemplo["idade"] == 30

# ==================== FIXTURE COM YIELD ====================

@pytest.fixture
def conexao_banco():
    """Fixture com setup e teardown usando yield"""
    print("\n[Setup] Conectando ao banco de dados...")
    conexao = {"status": "conectado", "dados": []}
    
    yield conexao  # O teste roda aqui
    
    print("[Teardown] Fechando conexão...")
    conexao["status"] = "desconectado"

def test_usando_fixture_yield(conexao_banco):
    """Teste usando fixture com yield"""
    assert conexao_banco["status"] == "conectado"
    conexao_banco["dados"].append("teste")

# ==================== FIXTURE COM ESCOPOS ====================

@pytest.fixture(scope="function")
def fixture_function():
    """Escopo function (padrão) - roda antes de cada teste"""
    return "function"

@pytest.fixture(scope="class")
def fixture_class():
    """Escopo class - roda uma vez por classe"""
    return "class"

@pytest.fixture(scope="module")
def fixture_module():
    """Escopo module - roda uma vez por módulo"""
    return "module"

@pytest.fixture(scope="session")
def fixture_session():
    """Escopo session - roda uma vez por sessão de testes"""
    return "session"

def test_escopo_function(fixture_function):
    assert fixture_function == "function"

def test_escopo_module(fixture_module):
    assert fixture_module == "module"

# ==================== FIXTURE COM AUTOUSE ====================

@pytest.fixture(autouse=True)
def setup_automatico():
    """Fixture que roda automaticamente para todos os testes"""
    print("\n[Autouse] Setup automático executado")
    yield
    print("[Autouse] Teardown automático executado")

def test_com_autouse():
    """Este teste usa automaticamente a fixture autouse"""
    assert True

# ==================== FIXTURE COM PARÂMETROS ====================

@pytest.fixture(params=[1, 2, 3])
def numero_parametrizado(request):
    """Fixture parametrizada - roda múltiplas vezes"""
    return request.param

def test_fixture_parametrizada(numero_parametrizado):
    """Teste que usa fixture parametrizada"""
    assert numero_parametrizado in [1, 2, 3]

# ==================== FIXTURE COM NOME ====================

@pytest.fixture(name="lista_customizada")
def fixture_com_nome():
    """Fixture com nome customizado"""
    return [1, 2, 3]

def test_usando_nome_customizado(lista_customizada):
    """Teste usando fixture com nome customizado"""
    assert len(lista_customizada) == 3

# ==================== FIXTURES ENCadeADAS ====================

@pytest.fixture
def usuario():
    """Fixture base"""
    return {"nome": "João", "email": "joao@example.com"}

@pytest.fixture
def usuario_com_perfil(usuario):
    """Fixture que depende de outra fixture"""
    usuario["perfil"] = "admin"
    return usuario

def test_fixture_encadeada(usuario_com_perfil):
    """Teste usando fixture encadeada"""
    assert usuario_com_perfil["nome"] == "João"
    assert usuario_com_perfil["perfil"] == "admin"

# ==================== FIXTURE COM CLASSES ====================

class TestComFixtures:
    """Classe de teste usando fixtures"""
    
    @pytest.fixture(autouse=True)
    def setup_classe(self):
        """Fixture específica para a classe"""
        print("\n[Setup] Setup da classe")
        self.dados = {"valor": 42}
        yield
        print("[Teardown] Teardown da classe")
    
    def test_metodo_1(self):
        """Método de teste 1"""
        assert self.dados["valor"] == 42
    
    def test_metodo_2(self):
        """Método de teste 2"""
        assert self.dados["valor"] == 42

# ==================== FIXTURE COM ARQUIVOS TEMPORÁRIOS ====================

@pytest.fixture
def arquivo_temporario(tmp_path):
    """Fixture usando tmp_path do pytest"""
    arquivo = tmp_path / "teste.txt"
    arquivo.write_text("conteúdo de teste")
    return arquivo

def test_arquivo_temporario(arquivo_temporario):
    """Teste usando arquivo temporário"""
    assert arquivo_temporario.exists()
    conteudo = arquivo_temporario.read_text()
    assert conteudo == "conteúdo de teste"

# ==================== FIXTURE COM CAPSYS ====================

@pytest.fixture
def capturar_output(capsys):
    """Fixture que captura stdout/stderr"""
    def capturar():
        return capsys.readouterr()
    return capturar

def test_captura_output(capturar_output):
    """Teste capturando output"""
    print("Mensagem de teste")
    captured = capturar_output()
    assert "Mensagem de teste" in captured.out

# ==================== FIXTURE COM MOCK ====================

@pytest.fixture
def mock_service():
    """Fixture que retorna um mock"""
    class MockService:
        def obter_dados(self):
            return {"status": "ok", "dados": [1, 2, 3]}
    
    return MockService()

def test_usando_mock(mock_service):
    """Teste usando mock"""
    resultado = mock_service.obter_dados()
    assert resultado["status"] == "ok"
    assert len(resultado["dados"]) == 3

# ==================== FIXTURE COM CONFIGURAÇÃO ====================

@pytest.fixture
def config_teste():
    """Fixture que fornece configuração de teste"""
    return {
        "debug": True,
        "timeout": 30,
        "retries": 3
    }

def test_configuracao(config_teste):
    """Teste usando configuração"""
    assert config_teste["debug"] is True
    assert config_teste["timeout"] == 30

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS PARA FIXTURES:

1. Use escopos apropriados (function, class, module, session)
2. Nomeie fixtures de forma descritiva
3. Use yield para teardown em vez de try/finally
4. Evite fixtures muito complexas
5. Use conftest.py para fixtures compartilhadas
6. Use autouse com cautela
7. Documente fixtures complexas
8. Use fixtures para eliminar duplicação
9. Considere usar fixtures parametrizadas
10. Mantenha fixtures independentes quando possível
"""

if __name__ == "__main__":
    # Para rodar os testes: pytest fase_18_testes_pytest/87_fixtures.py -v
    print("Execute: pytest fase_18_testes_pytest/87_fixtures.py -v")
    print("Para ver fixtures disponíveis: pytest --fixtures")