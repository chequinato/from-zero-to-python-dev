

'''

Conceito:
sqlite3 já vem embutido no Python — não precisa instalar nada.
Ele cria um banco de dados inteiro dentro de um arquivo só (.db), perfeito pra estudar e pra projetos pequenos/médios sem precisar de servidor de banco separado.
CRUD = Create, Read, Update, Delete — as 4 operações básicas que qualquer sistema faz num banco.

'''

# Conectando e criando tabela

import sqlite3

# conecta (se o arquivo não existir, ele CRIA na hora)
conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor() # cursor é quem executa os comandos SQL

cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL
    )
""")

conexao.commit()
conexao.close()

# create - inserindo dados
# nunca concatenar string direto, pois abre brecha para SQL injection
# Usa "?" como placeholder e passa os valores numa tupla

cursor.execute(
    "INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)",
    ("Teclado", 250.90, 15)
)

conexao.commit()
print(f"Produto inserido com id {cursor.lastrowid}") # pega o id do último
conexao.close()

# read - consultando dados

cursor.execute("SELECT * FROM produtos")
todos = cursor.fetchall() # lista de tuplas: [(1, 'Teclado', 250.9, 15), ...]
print(todos)

cursor.execute("SELECT * FROM produtos WHERE id = ?", (1,))
um_produto = cursor.fetchone() # traz só um resultado (ou None)
print(um_produto)

conexao.close()

# update - atualizando dados

cursor.execute("UPDATE produtos SET estoque = ? WHERE id = ?", (10, 1))

conexao.commit()
print(f"{cursor.rowcount} linha(s) atualizada(s)") # rowcount retorna as linhas afetadas pela consulta

conexao.close()

# delete - removendo dados

cursor.execute("DELETE FROM produtos WHERE id = ?", (1,))
conexao.commit()
print(f"{cursor.rowcount} linha(s) deletada(s)")

conexao.close()

# jeito seguro usando with que fecha a conexão sozinho

with sqlite3.connect('banco.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    print(cursor.fetchall())
# conexão comita e fecha automaticamente ao sair do with

