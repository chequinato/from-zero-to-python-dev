

'''

Conceito:
typing é o módulo de type hints — anotações de tipo que você adiciona no código pra deixar explícito o que uma função espera receber e o que ela retorna.
Não muda o comportamento em tempo de execução (Python continua dinâmico),
mas ajuda MUITO o editor a te avisar erro antes de rodar, e deixa o código mais legível pra outras pessoas (e pra você daqui 6 meses).

'''

# Anotações básicas (nem precisam de type hints)

def somar (a: int, b: int) -> int:
    return a + b

nome: str = 'Miguel'
idade: int = 25
altura: float = 1.75
ativo: bool = True

# Tipos compostos - precisam de typing

from typing import List, Dict, Tuple, Optional, Union

nomes: List[str] = ["Ana", "Bruno", "Carlos"]
idades: Dict[str, int] = {"Ana": 30, "Bruno": 25}
coordenada: Tuple[float, float] = (3.0, 4.0)

# A partir do Python 3.9+, dá pra usar direto os tipos nativos, sem importar do typing:
nomes: list[str] = ["Ana", "Bruno"]
idades: dict[str, int] = {"Ana": 30}
coordenada: tuple[float, float] = (10.5, 20.3)

# Optional e Union - quando o valor pode ser de mais de um tipo

def buscar_usuario(id: str) -> Optional[str]:

    if id == 1:
        return "Miguel"
    return None

def processar(valor: Union[int, float]) -> float:
    # Union[int, float] = aceita int OU float
    return valor*1.1

'''
Em projetos com AWS, APIs e bancos de dados, type hints ajudam a pegar erro cedo 
tipo passar str onde a função esperava int. Ferramentas como mypy conseguem checar isso automaticamente antes do código rodar em produção.
'''