# Design Patterns - Padrões de Projeto em Python

"""
Design Patterns são soluções reutilizáveis para problemas comuns
no desenvolvimento de software. Eles são categorizados em:
- Criacionais: Criação de objetos
- Estruturais: Composição de classes e objetos
- Comportamentais: Comunicação entre objetos
"""

# ==================== PADRÕES CRIACIONAIS ====================

# Singleton
class Singleton:
    """Garante que apenas uma instância da classe exista"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.dados = []

# Factory Method
class AnimalFactory:
    """Factory para criar diferentes tipos de animais"""
    @staticmethod
    def criar_animal(tipo: str):
        if tipo == "cachorro":
            return Cachorro()
        elif tipo == "gato":
            return Gato()
        else:
            raise ValueError("Tipo de animal desconhecido")

class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# Builder
class UsuarioBuilder:
    """Builder para construir objetos complexos passo a passo"""
    def __init__(self):
        self.usuario = {}
    
    def nome(self, nome: str):
        self.usuario['nome'] = nome
        return self
    
    def email(self, email: str):
        self.usuario['email'] = email
        return self
    
    def idade(self, idade: int):
        self.usuario['idade'] = idade
        return self
    
    def build(self):
        return self.usuario

# ==================== PADRÕES ESTRUTURAIS ====================

# Adapter
class SistemaLegado:
    """Sistema legado com interface incompatível"""
    def processar_dados_antigos(self, dados: str):
        print(f"Processando dados antigos: {dados}")

class NovoSistema:
    """Novo sistema com interface moderna"""
    def processar_dados(self, dados: dict):
        print(f"Processando dados: {dados}")

class Adapter:
    """Adapter para compatibilizar interfaces"""
    def __init__(self, sistema_legado: SistemaLegado):
        self.sistema_legado = sistema_legado
    
    def processar_dados(self, dados: dict):
        dados_str = str(dados)
        self.sistema_legado.processar_dados_antigos(dados_str)

# Decorator
class Componente:
    def operacao(self):
        pass

class ComponenteConcreto(Componente):
    def operacao(self):
        return "Componente Concreto"

class Decorator(Componente):
    def __init__(self, componente: Componente):
        self.componente = componente
    
    def operacao(self):
        return self.componente.operacao()

class DecoratorA(Decorator):
    def operacao(self):
        return f"DecoratorA({self.componente.operacao()})"

class DecoratorB(Decorator):
    def operacao(self):
        return f"DecoratorB({self.componente.operacao()})"

# Facade
class SubsistemaA:
    def operacao_a(self):
        print("Operação A")

class SubsistemaB:
    def operacao_b(self):
        print("Operação B")

class SubsistemaC:
    def operacao_c(self):
        print("Operação C")

class Facade:
    """Facade simplifica interface de subsistemas complexos"""
    def __init__(self):
        self.a = SubsistemaA()
        self.b = SubsistemaB()
        self.c = SubsistemaC()
    
    def operacao_completa(self):
        print("Iniciando operação completa...")
        self.a.operacao_a()
        self.b.operacao_b()
        self.c.operacao_c()
        print("Operação completa finalizada")

# ==================== PADRÕES COMPORTAMENTAIS ====================

# Observer
class Subject:
    """Subject mantém lista de observers e notifica mudanças"""
    def __init__(self):
        self.observers = []
        self.estado = None
    
    def adicionar_observer(self, observer):
        self.observers.append(observer)
    
    def remover_observer(self, observer):
        self.observers.remove(observer)
    
    def notificar_observers(self):
        for observer in self.observers:
            observer.atualizar(self.estado)
    
    def set_estado(self, estado):
        self.estado = estado
        self.notificar_observers()

class Observer:
    """Observer recebe notificações do subject"""
    def atualizar(self, estado):
        pass

class ObserverConcreto(Observer):
    def __init__(self, nome: str):
        self.nome = nome
    
    def atualizar(self, estado):
        print(f"{self.nome} recebeu atualização: {estado}")

# Strategy
class EstrategiaOrdenacao:
    """Interface para estratégias de ordenação"""
    def ordenar(self, lista: list) -> list:
        pass

class OrdenacaoBubbleSort(EstrategiaOrdenacao):
    def ordenar(self, lista: list) -> list:
        return sorted(lista)

class OrdenacaoQuickSort(EstrategiaOrdenacao):
    def ordenar(self, lista: list) -> list:
        return sorted(lista, reverse=True)

class Contexto:
    """Contexto usa estratégia para ordenar"""
    def __init__(self, estrategia: EstrategiaOrdenacao):
        self.estrategia = estrategia
    
    def ordenar_lista(self, lista: list) -> list:
        return self.estrategia.ordenar(lista)

# Command
class Command:
    """Interface para comandos"""
    def executar(self):
        pass

class CommandConcreto(Command):
    def __init__(self, receiver):
        self.receiver = receiver
    
    def executar(self):
        self.receiver.acao()

class Receiver:
    def acao(self):
        print("Ação executada")

class Invoker:
    """Invoker executa comandos"""
    def __init__(self):
        self.comandos = []
    
    def adicionar_comando(self, command: Command):
        self.comandos.append(command)
    
    def executar_comandos(self):
        for command in self.comandos:
            command.executar()

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS PARA DESIGN PATTERNS:

1. Use padrões para resolver problemas reais, não por moda
2. Entenda o problema antes de aplicar um padrão
3. Não force padrões onde não são necessários
4. Adapte padrões ao contexto do seu projeto
5. Documente quando e por que usar cada padrão
6. Considere a complexidade que o padrão adiciona
7. Use nomes descritivos para classes de padrões
8. Teste implementações de padrões
9. Refatore quando padrões não se encaixam mais
10. Aprenda quando NÃO usar padrões
"""

if __name__ == "__main__":
    print("=== Design Patterns Examples ===\n")
    
    # Singleton
    print("--- Singleton ---")
    s1 = Singleton()
    s2 = Singleton()
    print(f"Mesma instância: {s1 is s2}")
    
    # Factory Method
    print("\n--- Factory Method ---")
    cachorro = AnimalFactory.criar_animal("cachorro")
    print(cachorro.fazer_som())
    
    # Builder
    print("\n--- Builder ---")
    usuario = UsuarioBuilder().nome("João").email("joao@example.com").idade(30).build()
    print(usuario)
    
    # Facade
    print("\n--- Facade ---")
    facade = Facade()
    facade.operacao_completa()
    
    # Observer
    print("\n--- Observer ---")
    subject = Subject()
    obs1 = ObserverConcreto("Observer 1")
    obs2 = ObserverConcreto("Observer 2")
    subject.adicionar_observer(obs1)
    subject.adicionar_observer(obs2)
    subject.set_estado("Novo estado")
    
    # Strategy
    print("\n--- Strategy ---")
    contexto = Contexto(OrdenacaoBubbleSort())
    print(contexto.ordenar_lista([3, 1, 4, 1, 5]))