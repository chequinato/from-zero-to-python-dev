
# Encpsulamento

# Controla o acesso aos atributos de uma classe
# Python não tem encapsulamento "real" (tudo é acessível)
# mas segue convenções fortes

# Público (padrão)

class Pessoa:
    def __init__(self, nome):
        self.nome = nome # púlico -> acessível de qualquer lugar

pessoa = Pessoa("Miguel")
print(pessoa.nome)     #  acesso livre
pessoa.nome = "João"   #  modificação livre

# Protegido

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo   # protegido por convenção

    def ver_saldo(self):
        return self._saldo

conta = ContaBancaria("Miguel", 1000)
print(conta.ver_saldo())   # 1000
print(conta._saldo)        # ainda funciona, mas é "malvisto"

# Privado (name mangling: __atributo)

# Dois underscores = Python renomeia internamente
# Dificulta (mas não impede) o acesso direto

class ContaBancariaSegura:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo # privado

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido")
            return
        self.__saldo += valor

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente")
            return
        self.__saldo -= valor

    def ver_saldo(self):
        return self.__saldo

conta = ContaBancariaSegura("Miguel", 1000)
print(conta.ver_saldo())  # 1000

conta.depositar(500)
print(conta.ver_saldo())  # 1500

conta.sacar(-100)   # Valor inválido — bloqueado pela validação

# print(conta.__saldo) # AttributeError — não existe diretamente
print(conta._ContaBancariaSegura__saldo)   # ainda acessível assim (name mangling)

# Porque encapsular?

# Sem encapsulamento → qualquer um modifica sem validação
class Termometro:
    def __init__(self, celsius=0):
        self.celsius = celsius

t = Termometro(25)
t.celsius = -500   # valor impossível, sem nenhuma validação!

# Com encapsulamento → controla o que entra
class TermometroSeguro:
    def __init__(self, celsius=0):
        self.__celsius = celsius

    def ajustar(self, valor):
        if valor < -273.15:
            print("Temperatura abaixo do zero absoluto!")
            return
        self.__celsius = valor

    def ver_temperatura(self):
        return self.__celsius

t = TermometroSeguro(25)
t.ajustar(-500)   # Temperatura abaixo do zero absoluto!
print(t.ver_temperatura())  # 25 → protegido

# Resumo

# atributo    → público   → acesso livre
# _atributo   → protegido → convenção "não mexa direto"
# __atributo  → privado   → name mangling dificulta acesso externo

# Regra prática:
# Use __privado quando precisar de validação ao alterar o valor
# Combine com @property (próximo arquivo) para controle elegante
