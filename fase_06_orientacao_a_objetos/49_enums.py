
# ENUMS EM PYTHON

# Enum = conjunto fixo de valores nomeados e constantes
# Evita "strings mágicas" espalhadas pelo código

from enum import Enum, auto

# PROBLEMA SEM ENUM

# Strings soltas são propensas a erro de digitação
status = "aprovado"
if status == "aprovao":   # erro de digitação não detectado!
    print("Aprovado")

# COM ENUM

class StatusPedido(Enum):
    PENDENTE = "pendente"
    APROVADO = "aprovado"
    CANCELADO = "cancelado"
    ENTREGUE = "entregue"

pedido_status = StatusPedido.APROVADO

print(pedido_status)         # StatusPedido.APROVADO
print(pedido_status.name)    # APROVADO
print(pedido_status.value)   # aprovado

if pedido_status == StatusPedido.APROVADO:
    print("Pedido foi aprovado!")

# Erro de digitação agora é detectado (não existe o atributo)
# StatusPedido.APROVAO   # AttributeError

# ENUM COM auto()

# auto() gera valores automaticamente (não precisa definir manualmente)
class Ambiente(Enum):
    DEV = auto()
    HOMOLOGACAO = auto()
    PRODUCAO = auto()

print(Ambiente.DEV.value)            # 1
print(Ambiente.HOMOLOGACAO.value)    # 2
print(Ambiente.PRODUCAO.value)       # 3

# ITERANDO SOBRE ENUM

for status in StatusPedido:
    print(status.name, "→", status.value)
# PENDENTE → pendente
# APROVADO → aprovado
# CANCELADO → cancelado
# ENTREGUE → entregue

# Listando todos os valores
todos_status = [s.value for s in StatusPedido]
print(todos_status)
# ['pendente', 'aprovado', 'cancelado', 'entregue']

# COMPARANDO E VALIDANDO

def processar_pedido(status: StatusPedido):
    if status == StatusPedido.CANCELADO:
        print("Pedido foi cancelado, não processar")
        return
    if status == StatusPedido.APROVADO:
        print("Processando pedido aprovado...")
        return
    print("Aguardando aprovação...")

processar_pedido(StatusPedido.APROVADO)
processar_pedido(StatusPedido.CANCELADO)

# Convertendo string para Enum
valor_recebido = "aprovado"
status_convertido = StatusPedido(valor_recebido)
print(status_convertido)   # StatusPedido.APROVADO

# ENUM EM CLASSE (uso real)

class TipoOperacao(Enum):
    DEPOSITO = "deposito"
    SAQUE = "saque"
    TRANSFERENCIA = "transferencia"

class Transacao:
    def __init__(self, tipo: TipoOperacao, valor):
        self.tipo = tipo
        self.valor = valor

    def descricao(self):
        return f"{self.tipo.value.capitalize()}: R${self.valor}"

transacoes = [
    Transacao(TipoOperacao.DEPOSITO, 500),
    Transacao(TipoOperacao.SAQUE, 200),
    Transacao(TipoOperacao.TRANSFERENCIA, 1000),
]

for t in transacoes:
    print(t.descricao())
# Deposito: R$500
# Saque: R$200
# Transferencia: R$1000

# Filtrando por tipo
depositos = [t for t in transacoes if t.tipo == TipoOperacao.DEPOSITO]
print(len(depositos))   # 1

# QUANDO USAR ENUM

# Status (pendente, aprovado, cancelado)
# Ambientes (dev, homologação, produção)
# Tipos de operação (depósito, saque, transferência)
# Qualquer conjunto fixo e conhecido de opções
# → evita strings "mágicas" e erros de digitação silenciosos