# Optional Type - Valores Opcionais em Python

"""
Optional é usado para indicar que um valor pode ser de um tipo específico
ou None. É equivalente a Union[T, None].
"""

from typing import Optional, Union

# ==================== OPTIONAL BÁSICO ====================

def obter_usuario(usuario_id: int) -> Optional[dict]:
    """Retorna um dict de usuário ou None se não encontrado"""
    usuarios = {
        1: {"nome": "João", "email": "joao@example.com"},
        2: {"nome": "Maria", "email": "maria@example.com"}
    }
    return usuarios.get(usuario_id)

def usar_usuario(usuario_id: int) -> str:
    """Usa o resultado opcional de forma segura"""
    usuario = obter_usuario(usuario_id)
    
    if usuario is None:
        return "Usuário não encontrado"
    
    return f"Usuário: {usuario['nome']}"

# ==================== OPTIONAL COM VALOR PADRÃO ====================

def configurar_sistema(
    host: Optional[str] = None,
    porta: Optional[int] = None
) -> dict:
    """Configura sistema com valores opcionais"""
    return {
        "host": host or "localhost",
        "porta": porta or 8080
    }

# ==================== OPTIONAL EM CLASSES ====================

class Usuario:
    def __init__(
        self,
        nome: str,
        email: Optional[str] = None,
        telefone: Optional[str] = None
    ):
        self.nome = nome
        self.email = email
        self.telefone = telefone
    
    def obter_contato(self) -> str:
        """Retorna o contato principal"""
        if self.email:
            return self.email
        if self.telefone:
            return self.telefone
        return "Sem contato"

# ==================== OPTIONAL COM VALIDAÇÃO ====================

def processar_idade(idade: Optional[int]) -> int:
    """Processa idade opcional com validação"""
    if idade is None:
        return 0
    
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    
    if idade > 150:
        raise ValueError("Idade inválida")
    
    return idade

# ==================== OPTIONAL EM LISTAS ====================

from typing import List, Optional

def encontrar_primeiro_par(numeros: List[int]) -> Optional[int]:
    """Encontra o primeiro número par ou None"""
    for numero in numeros:
        if numero % 2 == 0:
            return numero
    return None

def filtrar_opcionais(valores: List[Optional[int]]) -> List[int]:
    """Remove valores None de uma lista"""
    return [v for v in valores if v is not None]

# ==================== OPTIONAL COM UNION ====================

def processar_entrada(
    valor: Optional[Union[str, int]]
) -> str:
    """Processa entrada que pode ser str, int ou None"""
    if valor is None:
        return "Nenhum valor fornecido"
    
    if isinstance(valor, int):
        return f"Número: {valor}"
    
    return f"String: {valor}"

# ==================== OPTIONAL EM DICIONÁRIOS ====================

from typing import Dict, Optional

def obter_configuracao(
    config: Dict[str, Optional[str]],
    chave: str,
    padrao: str = ""
) -> str:
    """Obtém configuração com valor padrão"""
    valor = config.get(chave)
    return valor if valor is not None else padrao

# ==================== OPTIONAL COM TYPE HINTS AVANÇADOS ====================

from typing import Callable, Optional

def executar_se_valido(
    funcao: Callable[[int], int],
    valor: Optional[int]
) -> Optional[int]:
    """Executa função apenas se valor não for None"""
    if valor is None:
        return None
    
    try:
        return funcao(valor)
    except Exception:
        return None

# ==================== OPTIONAL EM RETURN TYPES ====================

def dividir(a: int, b: int) -> Optional[float]:
    """Divide dois números, retorna None se divisão por zero"""
    if b == 0:
        return None
    return a / b

def raiz_quadrada(numero: float) -> Optional[float]:
    """Calcula raiz quadrada, retorna None se número negativo"""
    if numero < 0:
        return None
    return numero ** 0.5

# ==================== OPTIONAL COM PATTERN MATCHING ====================

def processar_resposta(
    resposta: Optional[dict]
) -> str:
    """Processa resposta opcional"""
    match resposta:
        case None:
            return "Sem resposta"
        case {"status": "ok", "dados": dados}:
            return f"Sucesso: {dados}"
        case {"status": "erro", "mensagem": msg}:
            return f"Erro: {msg}"
        case _:
            return "Resposta desconhecida"

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS PARA OPTIONAL:

1. Use Optional em vez de Union[T, None] para melhor legibilidade
2. Sempre verifique se valor é None antes de usar
3. Forneça valores padrão quando apropriado
4. Documente quando None é um valor esperado
5. Use Optional apenas quando None for significativo
6. Evite usar Optional como substituto para valores vazios
7. Considere usar padrões de projeto para valores opcionais
8. Use type guards para refinar tipos
9. Seja consistente no uso de Optional
10. Use mypy para verificar tipos opcionais
"""

if __name__ == "__main__":
    print("=== Optional Type Examples ===\n")
    
    # Exemplos básicos
    print(usar_usuario(1))
    print(usar_usuario(99))
    
    # Configuração com valores opcionais
    config = configurar_sistema("192.168.1.1", 3000)
    print(config)
    
    # Classe com opcionais
    usuario = Usuario("João", email="joao@example.com")
    print(usuario.obter_contato())
    
    # Encontrar primeiro par
    print(encontrar_primeiro_par([1, 3, 5, 7, 9]))
    print(encontrar_primeiro_par([1, 2, 3, 4, 5]))
    
    # Divisão com optional
    print(dividir(10, 2))
    print(dividir(10, 0))