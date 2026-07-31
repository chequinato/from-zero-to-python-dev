# Mypy - Verificação Estática de Tipos

"""
Mypy é um verificador estático de tipos para Python que ajuda
a encontrar erros de tipo antes de executar o código.
"""

# ==================== CONFIGURAÇÃO BÁSICA ====================

# mypy.ini
"""
[mypy]
python_version = 3.9
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
"""

# ==================== VERIFICAÇÃO DE TIPOS BÁSICA ====================

def soma_correta(a: int, b: int) -> int:
    """Função com tipos corretos"""
    return a + b

def soma_incorreta(a: int, b: int) -> int:
    """Função com erro de tipo (mypy vai reclamar)"""
    return str(a) + str(b)  # type: ignore

# ==================== VERIFICAÇÃO DE RETORNO ====================

def obter_valor() -> int:
    """Retorna int corretamente"""
    return 42

def obter_valor_errado() -> int:
    """Retorna str quando deveria retornar int (erro mypy)"""
    return "42"  # type: ignore

# ==================== VERIFICAÇÃO DE PARÂMETROS ====================

def processar_string(texto: str) -> str:
    """Processa string corretamente"""
    return texto.upper()

def chamada_correta():
    """Chama função corretamente"""
    return processar_string("hello")

def chamada_incorreta():
    """Chama função com tipo errado (erro mypy)"""
    return processar_string(123)  # type: ignore

# ==================== VERIFICAÇÃO DE OPTIONAL ====================

from typing import Optional

def obter_usuario(usuario_id: int) -> Optional[str]:
    """Retorna string ou None"""
    if usuario_id == 1:
        return "João"
    return None

def usar_usuario_correto(usuario_id: int) -> str:
    """Usa resultado opcional corretamente"""
    usuario = obter_usuario(usuario_id)
    if usuario is None:
        return "Usuário não encontrado"
    return f"Usuário: {usuario}"

def usar_usuario_incorreto(usuario_id: int) -> str:
    """Não verifica None (erro mypy)"""
    usuario = obter_usuario(usuario_id)
    return f"Usuário: {usuario}"  # type: ignore

# ==================== VERIFICAÇÃO DE LISTAS ====================

from typing import List

def processar_lista(numeros: List[int]) -> List[int]:
    """Processa lista de inteiros"""
    return [x * 2 for x in numeros]

def chamada_lista_correta():
    """Chama com lista correta"""
    return processar_lista([1, 2, 3])

def chamada_lista_incorreta():
    """Chama com lista incorreta (erro mypy)"""
    return processar_lista(["1", "2", "3"])  # type: ignore

# ==================== VERIFICAÇÃO DE DICIONÁRIOS ====================

from typing import Dict

def processar_dict(dados: Dict[str, int]) -> Dict[str, int]:
    """Processa dicionário"""
    return {k: v * 2 for k, v in dados.items()}

def chamada_dict_correta():
    """Chama com dict correto"""
    return processar_dict({"a": 1, "b": 2})

def chamada_dict_incorreta():
    """Chama com dict incorreto (erro mypy)"""
    return processar_dict({"a": "1", "b": "2"})  # type: ignore

# ==================== TYPE IGNORE ====================

def funcao_com_type_ignore(valor: int) -> str:
    """Função que usa type: ignore para suprimir erro"""
    # Às vezes necessário quando mypy não consegue inferir
    return str(valor)  # type: ignore

# ==================== CAST ====================

from typing import cast

def processar_union(valor: int | str) -> int:
    """Processa valor union com cast"""
    if isinstance(valor, str):
        # Cast para int após verificação
        valor_int = cast(int, int(valor))
        return valor_int * 2
    return valor * 2

# ==================== TYPE GUARDS ====================

from typing import Any

def is_string(valor: Any) -> TypeGuard[str]:
    """Type guard para verificar se é string"""
    return isinstance(valor, str)

def processar_com_type_guard(valor: Any) -> str:
    """Usa type guard para refinar tipo"""
    if is_string(valor):
        # mypy sabe que valor é str aqui
        return valor.upper()
    return str(valor)

# ==================== VERIFICAÇÃO DE CLASSES ====================

class Usuario:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self) -> str:
        return f"Sou {self.nome}, {self.idade} anos"

def processar_usuario(usuario: Usuario) -> str:
    """Processa objeto Usuario"""
    return usuario.apresentar()

def chamada_classe_correta():
    """Chama com objeto correto"""
    usuario = Usuario("João", 30)
    return processar_usuario(usuario)

def chamada_classe_incorreta():
    """Chama com objeto incorreto (erro mypy)"""
    return processar_usuario("João")  # type: ignore

# ==================== CONFIGURAÇÃO STRICT ====================

# Para habilitar modo strict no mypy.ini:
"""
[mypy]
strict = True
"""

# Isso habilita:
# - disallow_any_generics
# - disallow_subclassing_any
# - disallow_untyped_calls
# - disallow_untyped_defs
# - disallow_incomplete_defs
# - check_untyped_defs
# - no_implicit_optional
# - warn_redundant_casts
# - warn_unused_ignores
# - warn_return_any
# - no_implicit_reexport

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS PARA MYPY:

1. Configure mypy no início do projeto
2. Use modo strict quando possível
3. Adicione type hints em todas as funções públicas
4. Use type: ignore apenas quando realmente necessário
5. Corrija erros do mypy em vez de ignorar
6. Use type guards para refinar tipos complexos
7. Configure CI para rodar mypy automaticamente
8. Use stubs para bibliotecas sem type hints
9. Mantenha mypy atualizado
10. Documente decisões de usar type: ignore
"""

if __name__ == "__main__":
    print("=== Mypy Examples ===\n")
    
    # Exemplos de funções
    print(soma_correta(2, 3))
    print(obter_valor())
    
    # Exemplos de optional
    print(usar_usuario_correto(1))
    print(usar_usuario_correto(99))
    
    # Exemplos de listas
    print(chamada_lista_correta())
    
    # Exemplos de classes
    print(chamada_classe_correta())
    
    print("\nPara verificar tipos com mypy:")
    print("mypy fase_19_tipagem/92_mypy.py")
    print("mypy --strict fase_19_tipagem/92_mypy.py")