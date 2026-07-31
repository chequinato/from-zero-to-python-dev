# Pytest Mock - Mocking e Patching

"""
Mocking é usado para substituir partes do sistema por objetos simulados,
permitindo testar código em isolamento sem dependências externas.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock

# ==================== MOCK BÁSICO ====================

def test_mock_basico():
    """Teste usando Mock básico"""
    mock = Mock()
    
    # Configurar retorno
    mock.return_value = 42
    
    # Chamar o mock
    resultado = mock()
    
    assert resultado == 42
    assert mock.called

# ==================== MOCK COM ATRIBUTOS ====================

def test_mock_atributos():
    """Teste configurando atributos do mock"""
    mock = Mock()
    
    # Configurar atributos
    mock.nome = "João"
    mock.idade = 30
    
    assert mock.nome == "João"
    assert mock.idade == 30

# ==================== MOCK COM MÉTODOS ====================

def test_mock_metodos():
    """Teste configurando métodos do mock"""
    mock = Mock()
    
    # Configurar método
    mock.obter_dados.return_value = {"status": "ok"}
    
    resultado = mock.obter_dados()
    
    assert resultado["status"] == "ok"
    assert mock.obter_dados.called

# ==================== MOCK COM VALORES DIFERENTES ====================

def test_mock_side_effect():
    """Teste usando side_effect para retornar valores diferentes"""
    mock = Mock()
    
    # Retorna valores diferentes em cada chamada
    mock.side_effect = [1, 2, 3]
    
    assert mock() == 1
    assert mock() == 2
    assert mock() == 3

# ==================== MOCK LANÇANDO EXCEÇÃO ====================

def test_mock_exception():
    """Teste configurando mock para lançar exceção"""
    mock = Mock()
    
    # Configurar para lançar exceção
    mock.side_effect = ValueError("Erro simulado")
    
    with pytest.raises(ValueError) as exc_info:
        mock()
    
    assert "Erro simulado" in str(exc_info.value)

# ==================== PATCH ====================

class ServicoExterno:
    """Classe que simula um serviço externo"""
    def obter_dados(self):
        return {"dados": "reais"}

def test_patch_classe():
    """Teste usando patch para substituir classe"""
    with patch('__main__.ServicoExterno') as mock_classe:
        # Configurar o mock
        instancia_mock = mock_classe.return_value
        instancia_mock.obter_dados.return_value = {"dados": "mockados"}
        
        servico = ServicoExterno()
        resultado = servico.obter_dados()
        
        assert resultado["dados"] == "mockados"
        mock_classe.assert_called_once()

# ==================== PATCH COM DECORATOR ====================

@patch('__main__.ServicoExterno')
def test_patch_decorator(mock_classe):
    """Teste usando patch como decorator"""
    instancia_mock = mock_classe.return_value
    instancia_mock.obter_dados.return_value = {"dados": "mockados"}
    
    servico = ServicoExterno()
    resultado = servico.obter_dados()
    
    assert resultado["dados"] == "mockados"

# ==================== MAGIC MOCK ====================

def test_magic_mock():
    """Teste usando MagicMock"""
    mock = MagicMock()
    
    # MagicMock cria métodos automaticamente
    mock.qualquer_coisa.return_value = "resultado"
    
    assert mock.qualquer_coisa() == "resultado"
    assert mock.qualquer_metodo_nao_definido() is not None

# ==================== MOCK COM CALL ARGS ====================

def test_mock_call_args():
    """Teste verificando argumentos de chamada"""
    mock = Mock()
    
    mock(1, 2, chave="valor")
    
    # Verificar se foi chamado com argumentos específicos
    mock.assert_called_with(1, 2, chave="valor")
    
    # Verificar argumentos da chamada
    assert mock.call_args == ((1, 2), {"chave": "valor"})

# ==================== MOCK COM CALL COUNT ====================

def test_mock_call_count():
    """Teste verificando número de chamadas"""
    mock = Mock()
    
    mock()
    mock()
    mock()
    
    assert mock.call_count == 3
    mock.assert_called()
    mock.assert_called_once()  # Isso vai falhar

# ==================== MOCK PARA BANCO DE DADOS ====================

class Database:
    """Classe que simula acesso a banco de dados"""
    def query(self, sql):
        return [{"id": 1, "nome": "João"}]

def test_mock_database():
    """Teste mockando acesso a banco de dados"""
    mock_db = Mock(spec=Database)
    mock_db.query.return_value = [{"id": 1, "nome": "Maria"}]
    
    resultado = mock_db.query("SELECT * FROM usuarios")
    
    assert resultado[0]["nome"] == "Maria"
    mock_db.query.assert_called_once_with("SELECT * FROM usuarios")

# ==================== MOCK PARA API EXTERNA ====================

class APIClient:
    """Classe que simula cliente de API"""
    def get(self, url):
        return {"status": 200, "data": "dados reais"}

def test_mock_api():
    """Teste mockando chamada de API"""
    mock_api = Mock(spec=APIClient)
    mock_api.get.return_value = {"status": 200, "data": "dados mockados"}
    
    resultado = mock_api.get("https://api.example.com/users")
    
    assert resultado["data"] == "dados mockados"
    mock_api.get.assert_called_once_with("https://api.example.com/users")

# ==================== PATCH COM FIXTURE ====================

@pytest.fixture
def mock_servico_externo():
    """Fixture que fornece um mock de serviço externo"""
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {"status": "ok"}
        yield mock_get

def test_usando_fixture_mock(mock_servico_externo):
    """Teste usando fixture com mock"""
    import requests
    
    response = requests.get("https://api.example.com")
    dados = response.json()
    
    assert dados["status"] == "ok"
    mock_servico_externo.assert_called_once()

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS PARA MOCKING:

1. Mock apenas interfaces externas, não implementação
2. Use spec para garantir que mock segue a interface
3. Verifique chamadas com assert_called
4. Use side_effect para comportamentos complexos
5. Patch apenas o necessário (não patch tudo)
6. Use fixtures para mocks compartilhados
7. Documente o que está sendo mockado
8. Evite over-mocking (mock demais)
9. Use MagicMock quando precisar de métodos dinâmicos
10. Considere usar bibliotecas como responses para APIs
"""

if __name__ == "__main__":
    # Para rodar os testes: pytest fase_18_testes_pytest/88_mock.py -v
    print("Execute: pytest fase_18_testes_pytest/88_mock.py -v")