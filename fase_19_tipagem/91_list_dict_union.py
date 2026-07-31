# List, Dict e Union - Tipos de Coleção e União

"""
Tipos avançados para coleções e união de tipos em Python.
"""

from typing import List, Dict, Set, Tuple, Union, Optional, Any

# ==================== LIST TIPADA ====================

def processar_numeros(numeros: List[int]) -> List[int]:
    """Processa lista de inteiros"""
    return [x * 2 for x in numeros]

def filtrar_strings(strings: List[str], filtro: str) -> List[str]:
    """Filtra strings que contém um filtro"""
    return [s for s in strings if filtro in s]

def somar_lista(numeros: List[float]) -> float:
    """Soma elementos de uma lista de floats"""
    return sum(numeros)

# ==================== LIST ANINHADA ====================

from typing import List

Matriz = List[List[int]]

def transpor_matriz(matriz: Matriz) -> Matriz:
    """Transpõe uma matriz"""
    return [list(col) for col in zip(*matriz)]

def somar_matriz(matriz: Matriz) -> int:
    """Soma todos os elementos de uma matriz"""
    return sum(sum(linha) for linha in matriz)

# ==================== DICT TIPADO ====================

def contar_frequencia(texto: str) -> Dict[str, int]:
    """Conta frequência de cada caractere"""
    frequencia = {}
    for char in texto:
        frequencia[char] = frequencia.get(char, 0) + 1
    return frequencia

def agrupar_por_paridade(numeros: List[int]) -> Dict[str, List[int]]:
    """Agrupa_numbers por paridade"""
    return {
        "pares": [n for n in numeros if n % 2 == 0],
        "impares": [n for n in numeros if n % 2 != 0]
    }

# ==================== DICT COM VALORES MISTOS ====================

from typing import Dict, Union

ValorMisto = Union[int, str, bool, float]

Configuracao = Dict[str, ValorMisto]

def criar_configuracao() -> Configuracao:
    """Cria uma configuração com valores mistos"""
    return {
        "host": "localhost",
        "porta": 8080,
        "debug": True,
        "timeout": 30.5,
        "max_retries": 3
    }

# ==================== UNION BÁSICO ====================

def processar_valor(valor: Union[int, str]) -> str:
    """Processa int ou str"""
    if isinstance(valor, int):
        return f"Número: {valor}"
    return f"String: {valor}"

def calcular(valor: Union[int, float]) -> float:
    """Calcula com int ou float"""
    return float(valor) * 2

# ==================== UNION COM MÚLTIPLOS TIPOS ====================

from typing import Union

TipoNumerico = Union[int, float, complex]

def processar_numerico(valor: TipoNumerico) -> str:
    """Processa qualquer tipo numérico"""
    if isinstance(valor, complex):
        return f"Complex: {valor.real} + {valor.imag}i"
    return f"Real: {valor}"

# ==================== UNION COM OPTIONAL ====================

from typing import Union, Optional

Resultado = Union[int, str, None]

def processar_resultado(resultado: Resultado) -> str:
    """Processa resultado que pode ser int, str ou None"""
    if resultado is None:
        return "Sem resultado"
    if isinstance(resultado, int):
        return f"Resultado numérico: {resultado}"
    return f"Resultado textual: {resultado}"

# ==================== UNION COM CALLABLE ====================

from typing import Union, Callable

FuncaoProcessamento = Union[
    Callable[[int], int],
    Callable[[str], str]
]

def executar_processamento(
    funcao: FuncaoProcessamento,
    valor: Union[int, str]
) -> Union[int, str]:
    """Executa função de processamento"""
    return funcao(valor)

# ==================== SET TIPADO ====================

def encontrar_unicos(lista: List[int]) -> Set[int]:
    """Encontra elementos únicos"""
    return set(lista)

def intersecao_sets(set1: Set[str], set2: Set[str]) -> Set[str]:
    """Encontra interseção entre dois sets"""
    return set1 & set2

# ==================== TUPLE TIPADA ====================

Coordenada = Tuple[float, float]

def calcular_distancia(p1: Coordenada, p2: Coordenada) -> float:
    """Calcula distância entre dois pontos"""
    import math
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def processar_tupla(dados: Tuple[str, int, float]) -> str:
    """Processa tupla com tipos específicos"""
    nome, idade, salario = dados
    return f"{nome}, {idade} anos, R$ {salario:.2f}"

# ==================== TUPLE COM TAMANHO VARIÁVEL ====================

from typing import Tuple

def processar_varios(*args: Tuple[int, ...]) -> int:
    """Processa múltiplos inteiros"""
    return sum(args)

# ==================== TYPE ALIASES COMPLEXOS ====================

from typing import List, Dict, Optional

Usuario = Dict[str, Union[str, int]]
ListaUsuarios = List[Usuario]

def filtrar_usuarios_ativos(
    usuarios: ListaUsuarios,
    idade_minima: int = 18
) -> ListaUsuarios:
    """Filtra usuários ativos por idade"""
    return [
        usuario for usuario in usuarios
        if usuario.get("idade", 0) >= idade_minima
    ]

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS PARA LIST, DICT E UNION:

1. Use type aliases para tipos complexos e reutilizáveis
2. Seja específico com tipos de coleções
3. Use Union apenas quando realmente necessário
4. Prefira Optional em vez de Union[T, None]
5. Documente tipos complexos com comentários
6. Use List/Tuple em vez de list quando precisar de tipagem
7. Evite Union muito amplos como Union[Any, ...]
8. Considere usar Protocol para interfaces complexas
9. Use mypy para verificar tipos de coleções
10. Mantenha consistência no uso de tipos
"""

if __name__ == "__main__":
    print("=== List, Dict e Union Examples ===\n")
    
    # List examples
    print(processar_numeros([1, 2, 3, 4, 5]))
    print(filtrar_strings(["python", "java", "javascript"], "java"))
    
    # Dict examples
    print(contar_frequencia("hello world"))
    print(agrupar_por_paridade([1, 2, 3, 4, 5, 6]))
    
    # Union examples
    print(processar_valor(42))
    print(processar_valor("texto"))
    
    # Tuple examples
    p1 = (0.0, 0.0)
    p2 = (3.0, 4.0)
    print(calcular_distancia(p1, p2))
    
    # Type alias examples
    usuarios = [
        {"nome": "João", "idade": 25},
        {"nome": "Maria", "idade": 17},
        {"nome": "Pedro", "idade": 30}
    ]
    print(filtrar_usuarios_ativos(usuarios))