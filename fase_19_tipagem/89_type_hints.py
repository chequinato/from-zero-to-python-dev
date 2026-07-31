# Type Hints - Dicas de Tipo em Python

"""
Type hints permitem adicionar anotações de tipo ao código Python,
melhorando a legibilidade e permitindo verificação estática de tipos.
"""

# ==================== TIPOS BÁSICOS ====================

def soma(a: int, b: int) -> int:
    """Função com type hints básicos"""
    return a + b

def saudacao(nome: str) -> str:
    """String como parâmetro e retorno"""
    return f"Olá, {nome}!"

def processar(valor: bool) -> bool:
    """Booleano como parâmetro e retorno"""
    return not valor

def calcular_area(raio: float) -> float:
    """Float como parâmetro e retorno"""
    import math
    return math.pi * raio ** 2

# ==================== TIPOS COMPOSTOS ====================

from typing import List, Dict, Set, Tuple

def processar_lista(numeros: List[int]) -> List[int]:
    """Lista de inteiros como parâmetro e retorno"""
    return [x * 2 for x in numeros]

def processar_dicionario(dados: Dict[str, int]) -> Dict[str, int]:
    """Dicionário como parâmetro e retorno"""
    return {k: v * 2 for k, v in dados.items()}

def processar_conjunto(valores: Set[str]) -> Set[str]:
    """Set como parâmetro e retorno"""
    return {v.upper() for v in valores}

def processar_tupla(coordenadas: Tuple[float, float]) -> float:
    """Tupla como parâmetro"""
    x, y = coordenadas
    return (x ** 2 + y ** 2) ** 0.5

# ==================== TIPOS OPCIONAIS ====================

from typing import Optional

def encontrar_usuario(usuario_id: int) -> Optional[dict]:
    """Retorna um dict ou None"""
    usuarios = {1: {"nome": "João"}, 2: {"nome": "Maria"}}
    return usuarios.get(usuario_id)

def obter_configuracao(chave: str) -> Optional[str]:
    """Retorna uma string ou None"""
    configuracoes = {"host": "localhost", "port": "5432"}
    return configuracoes.get(chave)

# ==================== TIPOS UNION ====================

from typing import Union

def processar_valor(valor: Union[int, str]) -> str:
    """Aceita int ou str, retorna str"""
    return str(valor)

def calcular_idade(valor: Union[int, str]) -> int:
    """Aceita int ou str, retorna int"""
    if isinstance(valor, str):
        return int(valor)
    return valor

# ==================== TIPOS ANY ====================

from typing import Any

def processar_qualquer_coisa(valor: Any) -> str:
    """Aceita qualquer tipo"""
    return f"Tipo: {type(valor).__name__}, Valor: {valor}"

# ==================== TIPOS CALLABLE ====================

from typing import Callable

def executar_funcao(funcao: Callable[[int, int], int], a: int, b: int) -> int:
    """Recebe uma função como parâmetro"""
    return funcao(a, b)

def aplicar_transformacao(
    dados: List[int],
    transformacao: Callable[[int], int]
) -> List[int]:
    """Aplica uma transformação a cada elemento"""
    return [transformacao(x) for x in dados]

# ==================== TIPOS GENÉRICOS ====================

from typing import TypeVar, Generic

T = TypeVar('T')

class Container(Generic[T]):
    """Classe genérica"""
    def __init__(self, valor: T):
        self.valor = valor
    
    def obter_valor(self) -> T:
        return self.valor

def processar_generico(container: Container[int]) -> int:
    """Processa container genérico"""
    return container.obter_valor() * 2

# ==================== TIPOS LITERAIS ====================

from typing import Literal

def definir_status(status: Literal["ativo", "inativo", "pendente"]) -> str:
    """Aceita apenas valores literais específicos"""
    return f"Status: {status}"

def processar_cor(cor: Literal["vermelho", "verde", "azul"]) -> str:
    """Processa apenas cores específicas"""
    cores = {
        "vermelho": "#FF0000",
        "verde": "#00FF00",
        "azul": "#0000FF"
    }
    return cores[cor]

# ==================== TIPOS PROTOCOL ====================

from typing import Protocol

class Animal(Protocol):
    """Protocolo definindo interface"""
    def fazer_som(self) -> str:
        ...

def processar_animal(animal: Animal) -> str:
    """Processa qualquer objeto que segue o protocolo Animal"""
    return animal.fazer_som()

class Cachorro:
    def fazer_som(self) -> str:
        return "Au au!"

class Gato:
    def fazer_som(self) -> str:
        return "Miau!"

# ==================== TIPOS FINAL ====================

from typing import Final

MAX_TENTATIVAS: Final = 3
NOME_SISTEMA: Final = "MeuSistema"

def configurar_sistema(nome: str = NOME_SISTEMA) -> None:
    """Usa constante final como valor padrão"""
    print(f"Configurando {nome}")

# ==================== TYPE ALIASES ====================

from typing import List, Dict

Usuario = Dict[str, Union[str, int]]
ListaUsuarios = List[Usuario]

def processar_usuarios(usuarios: ListaUsuarios) -> ListaUsuarios:
    """Usa type aliases para melhor legibilidade"""
    return [
        {**usuario, "nome": usuario["nome"].upper()}
        for usuario in usuarios
    ]

Coordenada = Tuple[float, float]
ListaCoordenadas = List[Coordenada]

def calcular_distancia(pontos: ListaCoordenadas) -> List[float]:
    """Calcula distâncias entre pontos"""
    import math
    distancias = []
    for i in range(len(pontos) - 1):
        x1, y1 = pontos[i]
        x2, y2 = pontos[i + 1]
        distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        distancias.append(distancia)
    return distancias

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS PARA TYPE HINTS:

1. Use type hints em funções públicas
2. Seja específico com tipos (evite Any quando possível)
3. Use Optional para valores que podem ser None
4. Use Union para múltiplos tipos possíveis
5. Crie type aliases para tipos complexos
6. Use Protocol para interfaces duck-typing
7. Use Literal para valores fixos
8. Documente tipos complexos com comentários
9. Use ferramentas como mypy para verificação
10. Mantenha type hints consistentes com a implementação
"""

if __name__ == "__main__":
    # Exemplos de uso
    print("=== Type Hints Examples ===\n")
    
    # Funções básicas
    print(soma(2, 3))
    print(saudacao("Mundo"))
    
    # Tipos compostos
    print(processar_lista([1, 2, 3]))
    print(processar_dicionario({"a": 1, "b": 2}))
    
    # Tipos opcionais
    print(encontrar_usuario(1))
    print(encontrar_usuario(99))
    
    # Tipos union
    print(processar_valor(42))
    print(processar_valor("texto"))
    
    # Protocol
    cachorro = Cachorro()
    print(processar_animal(cachorro))