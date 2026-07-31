# Arquitetura Hexagonal - Ports and Adapters

"""
Arquitetura Hexagonal (também conhecida como Ports and Adapters)
é um padrão de arquitetura que separa a lógica de negócio das
interfaces externas, tornando o sistema mais testável e manutenível.
"""

from abc import ABC, abstractmethod
from typing import List

# ==================== DOMÍNIO (CORE) ====================

class Usuario:
    """Entidade do domínio"""
    def __init__(self, id: int, nome: str, email: str):
        self.id = id
        self.nome = nome
        self.email = email
    
    def __repr__(self):
        return f"Usuario(id={self.id}, nome={self.nome}, email={self.email})"

# ==================== PORTOS (INTERFACES) ====================

# Porto Primário (Driven) - Interface para infraestrutura
class UsuarioRepositoryPort(ABC):
    """Porto para persistência de usuários"""
    @abstractmethod
    def salvar(self, usuario: Usuario) -> Usuario:
        pass
    
    @abstractmethod
    def buscar_por_id(self, id: int) -> Usuario:
        pass
    
    @abstractmethod
    def buscar_por_email(self, email: str) -> Usuario:
        pass
    
    @abstractmethod
    def listar_todos(self) -> List[Usuario]:
        pass

class EmailServicePort(ABC):
    """Porto para envio de emails"""
    @abstractmethod
    def enviar_email(self, para: str, assunto: str, corpo: str) -> bool:
        pass

# Porto Secundário (Driver) - Interface para aplicação
class UsuarioServicePort(ABC):
    """Porto para serviços de usuário"""
    @abstractmethod
    def criar_usuario(self, nome: str, email: str) -> Usuario:
        pass
    
    @abstractmethod
    def obter_usuario(self, id: int) -> Usuario:
        pass
    
    @abstractmethod
    def listar_usuarios(self) -> List[Usuario]:
        pass

# ==================== ADAPTERS (IMPLEMENTAÇÕES) ====================

# Adapter para persistência (Infrastructure)
class InMemoryUsuarioRepository(UsuarioRepositoryPort):
    """Adapter em memória para repositório de usuários"""
    def __init__(self):
        self.usuarios = {}
        self._next_id = 1
    
    def salvar(self, usuario: Usuario) -> Usuario:
        if usuario.id is None:
            usuario.id = self._next_id
            self._next_id += 1
        self.usuarios[usuario.id] = usuario
        return usuario
    
    def buscar_por_id(self, id: int) -> Usuario:
        return self.usuarios.get(id)
    
    def buscar_por_email(self, email: str) -> Usuario:
        for usuario in self.usuarios.values():
            if usuario.email == email:
                return usuario
        return None
    
    def listar_todos(self) -> List[Usuario]:
        return list(self.usuarios.values())

class SMTPEmailService(EmailServicePort):
    """Adapter para envio de emails via SMTP"""
    def enviar_email(self, para: str, assunto: str, corpo: str) -> bool:
        print(f"[SMTP] Enviando email para {para}")
        print(f"[SMTP] Assunto: {assunto}")
        print(f"[SMTP] Corpo: {corpo}")
        return True

# ==================== APLICAÇÃO (USE CASES) ====================

class CriarUsuarioUseCase:
    """Use case para criar usuário"""
    def __init__(
        self,
        repository: UsuarioRepositoryPort,
        email_service: EmailServicePort
    ):
        self.repository = repository
        self.email_service = email_service
    
    def executar(self, nome: str, email: str) -> Usuario:
        """Executa o use case de criar usuário"""
        # Validação
        if not nome or not email:
            raise ValueError("Nome e email são obrigatórios")
        
        # Verifica se email já existe
        existente = self.repository.buscar_por_email(email)
        if existente:
            raise ValueError("Email já cadastrado")
        
        # Cria usuário
        usuario = Usuario(None, nome, email)
        usuario_salvo = self.repository.salvar(usuario)
        
        # Envia email de boas vindas
        self.email_service.enviar_email(
            email,
            "Bem vindo!",
            f"Olá {nome}, bem vindo ao sistema!"
        )
        
        return usuario_salvo

class ListarUsuariosUseCase:
    """Use case para listar usuários"""
    def __init__(self, repository: UsuarioRepositoryPort):
        self.repository = repository
    
    def executar(self) -> List[Usuario]:
        """Executa o use case de listar usuários"""
        return self.repository.listar_todos()

# ==================== CONTROLADORES (INTERFACE) ====================

class UsuarioController:
    """Controller que orquestra os use cases"""
    def __init__(
        self,
        criar_use_case: CriarUsuarioUseCase,
        listar_use_case: ListarUsuariosUseCase
    ):
        self.criar_use_case = criar_use_case
        self.listar_use_case = listar_use_case
    
    def criar_usuario(self, nome: str, email: str) -> Usuario:
        """Cria um novo usuário"""
        return self.criar_use_case.executar(nome, email)
    
    def listar_usuarios(self) -> List[Usuario]:
        """Lista todos os usuários"""
        return self.listar_use_case.executar()

# ==================== INJEÇÃO DE DEPENDÊNCIA ====================

def configurar_sistema():
    """Configura o sistema com todos os componentes"""
    # Adapters (Infrastructure)
    repository = InMemoryUsuarioRepository()
    email_service = SMTPEmailService()
    
    # Use Cases (Application)
    criar_use_case = CriarUsuarioUseCase(repository, email_service)
    listar_use_case = ListarUsuariosUseCase(repository)
    
    # Controller (Interface)
    controller = UsuarioController(criar_use_case, listar_use_case)
    
    return controller

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS PARA ARQUITETURA HEXAGONAL:

1. Mantenha o domínio livre de dependências externas
2. Use portos (interfaces) para definir contratos
3. Implemente adapters para cada tecnologia externa
4. Separe use cases da lógica de negócio
5. Use injeção de dependência para conectar componentes
6. Teste o domínio isoladamente
7. Use mocks para testar adapters
8. Mantenha controllers simples (thin)
9. Documente cada porto e adapter
10. A arquitetura facilita troca de tecnologias
"""

if __name__ == "__main__":
    print("=== Arquitetura Hexagonal Example ===\n")
    
    # Configura o sistema
    controller = configurar_sistema()
    
    # Cria usuários
    print("--- Criando Usuários ---")
    usuario1 = controller.criar_usuario("João", "joao@example.com")
    print(f"Usuário criado: {usuario1}")
    
    usuario2 = controller.criar_usuario("Maria", "maria@example.com")
    print(f"Usuário criado: {usuario2}")
    
    # Lista usuários
    print("\n--- Listando Usuários ---")
    usuarios = controller.listar_usuarios()
    for usuario in usuarios:
        print(usuario)
