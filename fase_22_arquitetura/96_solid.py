# SOLID Principles - Princípios de Design Orientado a Objetos

"""
SOLID é um acrônimo para cinco princípios de design orientado a objetos
que ajudam a criar software mais manutenível, escalável e robusto.
"""

# ==================== S - SINGLE RESPONSIBILITY PRINCIPLE ====================

"""
Single Responsibility Principle (SRP):
Uma classe deve ter apenas uma razão para mudar.
"""

class Usuario:
    """Classe responsável apenas por dados do usuário"""
    def __init__(self, nome: str, email: str):
        self.nome = nameself.email = email
    
    def __repr__(self):
        return f"Usuario(nome={self.nome}, email={self.email})"

class UsuarioRepository:
    """Classe responsável apenas por persistência de usuários"""
    def __init__(self):
        self.usuarios = []
    
    def salvar(self, usuario: Usuario):
        self.usuarios.append(usuario)
    
    def buscar_por_email(self, email: str) -> Usuario:
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario
        return None

class EmailService:
    """Classe responsável apenas por envio de emails"""
    def enviar_email_boas_vindas(self, usuario: Usuario):
        print(f"Enviando email de boas vindas para {usuario.email}")

# ==================== O - OPEN/CLOSED PRINCIPLE ====================

"""
Open/Closed Principle (OCP):
Entidades de software devem estar abertas para extensão,
mas fechadas para modificação.
"""

from abc import ABC, abstractmethod

class DescontoStrategy(ABC):
    """Interface abstrata para estratégias de desconto"""
    @abstractmethod
    def calcular_desconto(self, valor: float) -> float:
        pass

class DescontoNenhum(DescontoStrategy):
    """Sem desconto"""
    def calcular_desconto(self, valor: float) -> float:
        return 0.0

class DescontoEstudante(DescontoStrategy):
    """Desconto para estudantes"""
    def calcular_desconto(self, valor: float) -> float:
        return valor * 0.10  # 10% de desconto

class DescontoVIP(DescontoStrategy):
    """Desconto para VIP"""
    def calcular_desconto(self, valor: float) -> float:
        return valor * 0.20  # 20% de desconto

class CalculadoraPreco:
    """Calculadora de preço que pode ser estendida sem modificação"""
    def __init__(self, estrategia_desconto: DescontoStrategy):
        self.estrategia = estrategia_desconto
    
    def calcular_preco_final(self, valor: float) -> float:
        desconto = self.estrategia.calcular_desconto(valor)
        return valor - desconto

# ==================== L - LISKOV SUBSTITUTION PRINCIPLE ====================

"""
Liskov Substitution Principle (LSP):
Subclasses devem ser substituíveis por suas classes base.
"""

class Retangulo:
    """Classe base para retângulos"""
    def __init__(self, largura: float, altura: float):
        self.largura = largura
        self.altura = altura
    
    def area(self) -> float:
        return self.largura * self.altura

class Quadrado(Retangulo):
    """Quadrado é um retângulo especial"""
    def __init__(self, lado: float):
        super().__init__(lado, lado)
    
    @property
    def largura(self):
        return self._largura
    
    @largura.setter
    def largura(self, valor):
        self._largura = valor
        self._altura = valor  # Mantém quadrado
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, valor):
        self._altura = valor
        self._largura = valor  # Mantém quadrado

# ==================== I - INTERFACE SEGREGATION PRINCIPLE ====================

"""
Interface Segregation Principle (ISP):
Clientes não devem ser forçados a depender de interfaces
que não utilizam.
"""

from abc import ABC, abstractmethod

class Trabalhador(ABC):
    """Interface básica para trabalhadores"""
    @abstractmethod
    def trabalhar(self):
        pass

class Comedor(ABC):
    """Interface para comer"""
    @abstractmethod
    def comer(self):
        pass

class Dormidor(ABC):
    """Interface para dormir"""
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabalhador, Comedor, Dormidor):
    """Humano implementa todas as interfaces"""
    def trabalhar(self):
        print("Trabalhando...")
    
    def comer(self):
        print("Comendo...")
    
    def dormir(self):
        print("Dormindo...")

class Robo(Trabalhador):
    """Robô implementa apenas o que precisa"""
    def trabalhar(self):
        print("Robô trabalhando...")

# ==================== D - DEPENDENCY INVERSION PRINCIPLE ====================

"""
Dependency Inversion Principle (DIP):
Dependa de abstrações, não de implementações concretas.
"""

class Database(ABC):
    """Interface abstrata para banco de dados"""
    @abstractmethod
    def salvar(self, dados: dict):
        pass
    
    @abstractmethod
    def buscar(self, id: int) -> dict:
        pass

class PostgreSQLDatabase(Database):
    """Implementação concreta para PostgreSQL"""
    def salvar(self, dados: dict):
        print(f"Salvando no PostgreSQL: {dados}")
    
    def buscar(self, id: int) -> dict:
        print(f"Buscando no PostgreSQL: {id}")
        return {"id": id, "nome": "João"}

class MySQLDatabase(Database):
    """Implementação concreta para MySQL"""
    def salvar(self, dados: dict):
        print(f"Salvando no MySQL: {dados}")
    
    def buscar(self, id: int) -> dict:
        print(f"Buscando no MySQL: {id}")
        return {"id": id, "nome": "Maria"}

class UsuarioService:
    """Service que depende da abstração, não da implementação"""
    def __init__(self, database: Database):
        self.database = database
    
    def criar_usuario(self, nome: str):
        dados = {"nome": nome}
        self.database.salvar(dados)
    
    def obter_usuario(self, id: int):
        return self.database.buscar(id)

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS PARA SOLID:

1. SRP: Separe responsabilidades em classes diferentes
2. OCP: Use herança e composição para extensão
3. LSP: Verifique se subclasses podem substituir classes base
4. ISP: Crie interfaces pequenas e específicas
5. DIP: Injete dependências via construtor
6. Use injeção de dependência para desacoplar
7. Prefira composição sobre herança
8. Use interfaces para definir contratos
9. Teste substituibilidade de subclasses
10. Refatore código que viola princípios SOLID
"""

if __name__ == "__main__":
    print("=== SOLID Principles Examples ===\n")
    
    # SRP Example
    print("--- Single Responsibility ---")
    usuario = Usuario("João", "joao@example.com")
    repo = UsuarioRepository()
    repo.salvar(usuario)
    email_service = EmailService()
    email_service.enviar_email_boas_vindas(usuario)
    
    # OCP Example
    print("\n--- Open/Closed ---")
    calc_vip = CalculadoraPreco(DescontoVIP())
    print(f"Preço VIP: {calc_vip.calcular_preco_final(100.0)}")
    
    calc_estudante = CalculadoraPreco(DescontoEstudante())
    print(f"Preço Estudante: {calc_estudante.calcular_preco_final(100.0)}")
    
    # DIP Example
    print("\n--- Dependency Inversion ---")
    service_pg = UsuarioService(PostgreSQLDatabase())
    service_pg.criar_usuario("João")
    
    service_mysql = UsuarioService(MySQLDatabase())
    service_mysql.criar_usuario("Maria")