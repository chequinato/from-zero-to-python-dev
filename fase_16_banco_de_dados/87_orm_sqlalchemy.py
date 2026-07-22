
'''

Conceito:
ORM (Object-Relational Mapping) é uma camada que traduz suas tabelas do banco em classes Python, e suas linhas em objetos.
Em vez de escrever SQL cru (INSERT INTO...), você trabalha com objetos Python normais e o SQLAlchemy gera o SQL por trás dos panos.
Fica mais próximo da lógica orientada a objetos, mais fácil de trocar de banco (sqlite → postgres) sem reescrever tudo.

'''

# Instalação: pip install sqlalchemy

# Definindo uma tabela como classe (MODEL)

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base() # classe base de onde todas as tabelas herdam

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)

    def __repr__(self): # o repr define como o objeto deve ser representado como texto:
        return f"Produto(id={self.id}, nome='{self.nome}', preco={self.preco})"

# a classe Produto é literalmente a tabela produtos do banco, cada column é uma coluna e cada instância vira uma linha

# criando o "engine" e a tabela de verdade
engine = create_engine('sqlite:///banco.db')  # troca só essa string pra mudar de banco
Base.metadata.create_all(engine) # cria a tabela de fato, se não existir

# session - é por ela que você conversa com o banco

Sessao = sessionmaker(bind=engine)
sessao = Sessao()

# create
novo_produto = Produto(nome="Mouse", preco=70, estoque=30)
sessao.add(novo_produto)
sessao.commit()

print(novo_produto.id)  # o id já vem preenchido depois do commit

# read
todos = sessao.query(Produto).all()
print(todos) # [Produto(id=1, nome='Mouse', preco=70)]

um = sessao.query(Produto).filter_by(id=1).first()
print(um)

caros = sessao.query(Produto).filter(Produto.preco > 100).all()

# update
produto = sessao.query(Produto).filter_by(id=1).first()
produto.estoque = 25
sessao.commit()  # o SQLAlchemy detecta a mudança no objeto e gera o UPDATE sozinho

# delete
produto = sessao.query(Produto).filter_by(id=1).first()
sessao.delete(produto)
sessao.commit()

