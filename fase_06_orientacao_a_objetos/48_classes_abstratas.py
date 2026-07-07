# CLASSES ABSTRATAS (ABC)

# Classe abstrata = não pode ser instanciada diretamente
# Define um "contrato" que as subclasses DEVEM implementar

from abc import ABC, abstractmethod

# PROBLEMA SEM ABC

class Forma:
    def area(self):
        raise NotImplementedError("Implemente area()")
        # funciona, mas só falha em TEMPO DE EXECUÇÃO, não avisa antes

# COM ABC (mais seguro)

class FormaAbstrata(ABC):
    @abstractmethod
    def area(self):
        pass   # obrigatório implementar nas subclasses

    @abstractmethod
    def perimetro(self):
        pass

    def descricao(self):   # método normal, não precisa ser sobrescrito
        return f"Esta forma tem área {self.area():.2f}"

# Tentando instanciar a classe abstrata diretamente
# forma = FormaAbstrata()   # TypeError: Can't instantiate abstract class

class Retangulo(FormaAbstrata):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

retangulo = Retangulo(5, 3)
print(retangulo.area())        # 15
print(retangulo.perimetro())   # 16
print(retangulo.descricao())   # Esta forma tem área 15.00

# OBRIGANDO IMPLEMENTAÇÃO

class Circulo(FormaAbstrata):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14159 * self.raio ** 2
    # esqueceu de implementar perimetro()!

# circulo = Circulo(5)   # TypeError: Can't instantiate
# Python avisa de cara que falta implementar um método abstrato

# USO REAL: PORTAS/ADAPTADORES (arquitetura hexagonal)

class RepositorioPort(ABC):
    @abstractmethod
    def salvar(self, dado):
        pass

    @abstractmethod
    def buscar(self, id):
        pass

class RepositorioMemoria(RepositorioPort):
    def __init__(self):
        self.dados = {}

    def salvar(self, dado):
        self.dados[dado["id"]] = dado
        print(f"Salvo na memória: {dado}")

    def buscar(self, id):
        return self.dados.get(id)

class RepositorioS3(RepositorioPort):
    def salvar(self, dado):
        print(f"Salvando no S3: {dado}")

    def buscar(self, id):
        print(f"Buscando no S3: {id}")
        return {"id": id, "origem": "s3"}

# O código que usa não precisa saber qual implementação está por trás
def processar(repositorio: RepositorioPort, dado):
    repositorio.salvar(dado)

repo_memoria = RepositorioMemoria()
repo_s3 = RepositorioS3()

processar(repo_memoria, {"id": 1, "nome": "Miguel"})
processar(repo_s3, {"id": 2, "nome": "João"})

# QUANDO USAR ABC

# Quando quer GARANTIR que subclasses implementem certos métodos
# Definir contratos/interfaces (muito usado em arquitetura hexagonal)
# Trocar implementações facilmente (memória, S3, banco) sem mudar o resto do código
# Deixar erros de implementação explícitos cedo, não em produção