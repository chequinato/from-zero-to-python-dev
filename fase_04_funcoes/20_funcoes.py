
# LEMBRETE: DOCSTRINGS
# Docstring e uma string de documentacao que fica logo abaixo da definicao da funcao.
# Serve pra explicar o que a funcao faz. Todo projeto profissional usa.
#
# Exemplo:
#
# def calcular_desconto(preco, percentual):
#     """Calcula o valor do desconto sobre um preco.
#
#     Args:
#         preco: valor original do produto
#         percentual: percentual de desconto (ex: 10 para 10%)
#
#     Returns:
#         O valor do desconto calculado
#     """
#     return preco * (percentual / 100)
#
# Acessando a docstring:
#   print(calcular_desconto.__doc__)
#   help(calcular_desconto)

# Funcoes em Python

# Função é um bloco de código reutilizável
# Evita repetição, organiza o código e facilita manutenção

# Definindo e chamando

# Função simples

def somar(a, b):
    return a + b

resultado = somar(4, 5)
print(resultado)

# Usando o retorno diretamente
def verificar_idade(idade):
    if idade < 0 or idade > 100:
        return "Idade inválida"
    if idade < 18:
        return ("Menor de idade""")
    return "Maior de idade"

print(verificar_idade(18))
print(verificar_idade(7))
print(verificar_idade(-12))

# Função sem return -> retorna None
def sem_retorno():
    print("Executo mas não retorno nada")

resultado = sem_retorno()
print(type(resultado)) # <class 'NoneType'>
print(resultado)

def calcular(a, b):
    return a + b, a - b, a * b

resultado = calcular(1, 2)
print(resultado)
print(type(resultado)) # Retorna uma tupla

# Desempacotando o retorno
soma, sub, multi = calcular(10, 3)
print(soma)   # 13
print(sub)    # 7
print(multi)  # 30

# Ignorando valores do retorno com _
soma, _, multi = calcular(10, 3)
print(soma)
print(multi)

# Return antecipado (early return)
# Padrão muito usado: validar primeiro, processar depois

def processar_pedido(pedido):
    if pedido is None:
        return "Pedido inválido"
    if pedido.get("valor", 0) <= 0:
        return "Valor inválido"
    if pedido.get("status") == "cancelado":
        return "Pedido cancelado"

    # só chega aqui se passou em todas as validações
    return f"Processando pedido R${pedido['valor']}"

print(processar_pedido(None))
print(processar_pedido({"valor": 0}))
print(processar_pedido({"valor": 150, "status": "aprovado"}))

# Funções como documentação
# Docstring → documenta o que a função faz
def calcular_imc(peso, altura):
    """
    Calcula o IMC de uma pessoa.

    Args:
        peso: peso em kg
        altura: altura em metros

    Returns:
        float: valor do IMC
    """
    return peso / (altura ** 2)

print(calcular_imc(80, 1.75))   # 26.12...
print(calcular_imc.__doc__)     # mostra a docstring

# Funções dentro de funções
def processar_dados(dados):
    def validar(item):
        return item is not None and item > 0

    def formatar(item):
        return round(item, 2)

    resultado = []

    for item in dados:
        if validar(item):
            resultado.append(formatar(item))
    return resultado

dados = [1.234, None, -5, 2.567, 0, 3.891]
print(processar_dados(dados))  # [1.23, 2.57, 3.89]

# Boas práticas
# Função faz UMA coisa só
def calcular_desconto(preco, percentual):
    return preco * (1 - percentual / 100)

def aplicar_imposto(preco, percentual):
    return preco * (1 + percentual / 100)

# Nome de função é verbo + substantivo
def buscar_usuario(id): pass
def calcular_total(itens): pass
def enviar_email(destinatario): pass
def validar_cpf(cpf): pass

# Evitar funções que fazem muitas coisas
def fazer_tudo(dados):
    # busca, valida, calcula, salva, envia email...
    # difícil de testar e manter
    pass
