# Interfaces ABC - Abstract Base Classes

"""
ABC (Abstract Base Classes) permite definir interfaces formais em Python,
garantindo que classes derivadas implementem métodos obrigatórios.
"""

from abc import ABC, abstractmethod
from typing import List

# ==================== INTERFACE BÁSICA ====================

class FormaGeometrica(ABC):
    """Interface abstrata para formas geométricas"""
    
    @abstractmethod
    def area(self) -> float:
        """Calcula a área da forma"""
        pass
    
    @abstractmethod
    def perimetro(self) -> float:
        """Calcula o perímetro da forma"""
        pass

class Retangulo(FormaGeometrica):
    """Implementação concreta de retângulo"""
    def __init__(self, largura: float, altura: float):
        self.largura = largura
        self.altura = altura
    
    def area(self) -> float:
        return self.largura * self.altura
    
    def perimetro(self) -> float:
        return 2 * (self.largura + self.altura)

class Circulo(FormaGeometrica):
    """Implementação concreta de círculo"""
    def __init__(self, raio: float):
        self.raio = raio
    
    def area(self) -> float:
        import math
        return math.pi * self.raio ** 2
    
    def perimetro(self) -> float:
        import math
        return 2 * math.pi * self.raio

# ==================== MÉTODOS ABSTRATOS COM PARÂMETROS ====================

class ProcessadorDados(ABC):
    """Interface para processamento de dados"""
    
    @abstractmethod
    def processar(self, dados: List[dict]) -> List[dict]:
        """Processa uma lista de dados"""
        pass
    
    @abstractmethod
    def validar(self, dado: dict) -> bool:
        """Valida um dado individual"""
        pass

class ProcessadorJSON(ProcessadorDados):
    """Implementação para processamento JSON"""
    def processar(self, dados: List[dict]) -> List[dict]:
        return [d for d in dados if self.validar(d)]
    
    def validar(self, dado: dict) -> bool:
        return "id" in dado and "valor" in dado

# ==================== MÉTODOS CONCRETOS EM ABC ====================

class Veiculo(ABC):
    """Classe abstrata com métodos concretos e abstratos"""
    
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self._velocidade = 0
    
    @abstractmethod
    def acelerar(self, incremento: float):
        """Método abstrato para acelerar"""
        pass
    
    @abstractmethod
    def frear(self, decremento: float):
        """Método abstrato para frear"""
        pass
    
    def obter_informacoes(self) -> str:
        """Método concreto compartilhado"""
        return f"{self.marca} {self.modelo} - Velocidade: {self._velocidade} km/h"

class Carro(Veiculo):
    """Implementação concreta de carro"""
    def acelerar(self, incremento: float):
        self._velocidade += incremento
    
    def frear(self, decremento: float):
        self._velocidade = max(0, self._velocidade - decremento)

# ==================== PROPERTIES ABSTRATAS ====================

class Repositorio(ABC):
    """Interface com properties abstratas"""
    
    @property
    @abstractmethod
    def conexao(self):
        """Property abstrata para conexão"""
        pass
    
    @abstractmethod
    def salvar(self, dados: dict):
        pass
    
    @abstractmethod
    def buscar(self, id: int):
        pass

class RepositorioSQL(Repositorio):
    """Implementação SQL do repositório"""
    def __init__(self, string_conexao: str):
        self._conexao = string_conexao
    
    @property
    def conexao(self):
        return self._conexao
    
    def salvar(self, dados: dict):
        print(f"Salvando no SQL: {dados}")
    
    def buscar(self, id: int):
        print(f"Buscando no SQL: {id}")

# ==================== CLASSMETHODS ABSTRATOS ====================

class Factory(ABC):
    """Factory com classmethod abstrato"""
    
    @classmethod
    @abstractmethod
    def criar(cls, tipo: str):
        """Método de fábrica abstrato"""
        pass

class AnimalFactory(Factory):
    """Factory concreta para animais"""
    @classmethod
    def criar(cls, tipo: str):
        if tipo == "cachorro":
            return Cachorro()
        elif tipo == "gato":
            return Gato()
        else:
            raise ValueError("Tipo desconhecido")

class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# ==================== VERIFICAÇÃO DE INSTÂNCIA ====================

def verificar_forma(forma: FormaGeometrica):
    """Função que usa a interface"""
    print(f"Área: {forma.area():.2f}")
    print(f"Perímetro: {forma.perimetro():.2f}")

# ==================== SUBCLASSHOOK ====================

class MinhaInterface(ABC):
    """Interface com __subclasshook__ customizado"""
    
    @classmethod
    def __subclasshook__(cls, subclass):
        """Verifica se uma classe implementa a interface"""
        if cls is MinhaInterface:
            return hasattr(subclass, 'metodo_obrigatorio')
        return NotImplemented

class ClasseComMetodo:
    """Classe que implementa o método obrigatório"""
    def metodo_obrigatorio(self):
        return "Implementado"

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS PARA ABC:

1. Use ABC para definir contratos claros
2. Documente o que cada método abstrato deve fazer
3. Use @abstractmethod para métodos obrigatórios
4. Use @abstractproperty para properties obrigatórias
5. Misture métodos concretos e abstratos quando apropriado
6. Use isinstance() para verificar implementações
7. Implemente __subclasshook__ para verificação customizada
8. Use ABC em vez de duck typing quando precisar de contratos
9. Mantenha interfaces focadas e pequenas
10. Teste implementações de ABC
"""

if __name__ == "__main__":
    print("=== ABC Interfaces Examples ===\n")
    
    # Exemplo básico
    print("--- Formas Geométricas ---")
    retangulo = Retangulo(5, 3)
    print(f"Área do retângulo: {retangulo.area()}")
    print(f"Perímetro do retângulo: {retangulo.perimetro()}")
    
    circulo = Circulo(2)
    print(f"Área do círculo: {circulo.area():.2f}")
    print(f"Perímetro do círculo: {circulo.perimetro():.2f}")
    
    # Exemplo de veículo
    print("\n--- Veículos ---")
    carro = Carro("Toyota", "Corolla")
    carro.acelerar(50)
    print(carro.obter_informacoes())
    
    # Exemplo de factory
    print("\n--- Factory ---")
    cachorro = AnimalFactory.criar("cachorro")
    print(cachorro.fazer_som())
    
    # Verificação de instância
    print("\n--- Verificação de Instância ---")
    print(f"Retângulo é FormaGeometrica: {isinstance(retangulo, FormaGeometrica)}")
    print(f"ClasseComMetodo é MinhaInterface: {issubclass(ClasseComMetodo, MinhaInterface)}")
