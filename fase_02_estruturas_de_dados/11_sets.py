
# Sets em Python

# Set é uma coleção SEM ordem, SEM duplicatas e mutável
# Muito eficiente para verificar existência e remover duplicatas

# Criando sets
vazio = set()  # atenção: {} cria dicionário, não set!
numeros = {1, 2, 3, 4, 5}
frutas = {"maçã", "banana", "uva", "maçã"}  # duplicata ignorada

print(numeros)
print(frutas)           # {'uva', 'banana', 'maçã'} → sem duplicata, sem ordem garantida
print(type(frutas))     # <class 'set'>

# Caso mais comum: remover duplicatas de uma lista
lista_com_duplicatas = [1, 2, 2, 3, 3, 3, 4]
sem_duplicatas = list(set(lista_com_duplicatas))
print(sem_duplicatas)  # [1, 2, 3, 4]

lista_com_duplicatas_2 = [1, 2, 2, 3, 3, 3, 4]
sem_duplicadas_2 = list(set(lista_com_duplicatas_2))
print(sem_duplicadas_2)

# Adicionando e removendo
frutas = {"maçã", "banana", "uva"}

frutas.add("manga")
print(frutas)

frutas.remove("banana")    # erro se não existir
print(frutas)

frutas.discard("abacaxi")  # sem erro se não existir
print(frutas)

removido = frutas.pop()    # remove um elemento aleatório
print(removido)

# in → verificação muito rápida
# Sets são muito mais rápidos que listas para isso
permissoes = {"ler", "escrever", "deletar"}
print("ler" in permissoes)      # True
print("executar" in permissoes) # False

# Operações em sets

times_a = {"Miguel", "João", "Ana", "Carlos"}
times_b = {"Ana", "Carlos", "Paula", "Lucas"}

# union() → todos os elementos, sem duplicatas
print(times_a | times_b)
print(times_a.union(times_b))

# intersection() → apenas os comuns
print(times_a & times_b)
print(times_a.intersection(times_b))  # {'Ana', 'Carlos'}

# difference() → no primeiro mas não no segundo
print(times_a - times_b)
print(times_a.difference(times_b))    # {'Miguel', 'João'}

# symmetric_difference() → em um ou outro, mas não nos dois
print(times_a ^ times_b)
print(times_a.symmetric_difference(times_b))  # {'Miguel', 'João', 'Paula', 'Lucas'}

# QUANDO USAR CADA ESTRUTURA?

# Lista  → ordem importa, duplicatas permitidas, acesso por índice
# Tupla  → dados fixos/imutáveis, mais performance
# Dict   → busca por chave, dados estruturados, JSON
# Set    → sem duplicatas, operações entre coleções, busca rápida

# Exemplo real: encontrar usuários em comum entre dois sistemas
sistema_antigo = {"miguel", "joao", "ana", "carlos"}
sistema_novo = {"ana", "carlos", "paula", "lucas"}

em_comum = sistema_antigo & sistema_novo
so_no_antigo = sistema_antigo - sistema_novo
so_no_novo = sistema_novo - sistema_antigo

print(f"Em ambos: {em_comum}")
print(f"Migrar para o novo: {so_no_antigo}")
print(f"Novos usuários: {so_no_novo}")