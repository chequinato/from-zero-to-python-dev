
# Heranca em Python

# LEMBRETE: HERANCA MULTIPLA
# Python permite herdar de MAIS DE UMA classe ao mesmo tempo.
# Isso se chama heranca multipla e aparece em codigo real (ex: Mixins).
#
# Exemplo:
#
# class Logavel:
#     def log(self):
#         print(f"[LOG] {self}")
#
# class Serializable:
#     def to_dict(self):
#         return self.__dict__
#
# class Usuario(Logavel, Serializable):
#     def __init__(self, nome):
#         self.nome = nome
#
# u = Usuario("Miguel")
# u.log()           # herdado de Logavel
# u.to_dict()       # herdado de Serializable
#
# MRO (Method Resolution Order):
# Quando duas classes pai tem o mesmo metodo, Python usa o MRO pra decidir
# qual executar. Voce pode ver a ordem com:
#   print(Usuario.__mro__)
#   # (<class 'Usuario'>, <class 'Logavel'>, <class 'Serializable'>, <class 'object'>)
#
# A ordem e: da esquerda pra direita, na ordem que voce escreveu na heranca.
