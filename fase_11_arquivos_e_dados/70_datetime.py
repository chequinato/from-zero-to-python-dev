
'''

Datetime é o módulo para trabalhar com datas e horas: pegar a data atual, calcular a
diferença entre datas, formatar, converter strings em data...

Classe
- date: só data (ano, mês, dia)
- time: só hora (hora, minuto, segundo)
- datetime: data + hora juntos
- timedelta: diferença entre datas

'''

# Data e hora atual

from datetime import datetime, timedelta, date
from time import strptime

agora = datetime.now()
print(agora)
print(type(agora))

hoje = datetime.today()
print(hoje)

# Acessando partes
print(agora.year())
print(agora.month())
print(agora.day())
print(agora.hour())
print(agora.minute())

# Criando datas manualmente

aniversario = date(1994, 3, 15)
reuniao = datetime(1994, 3, 15, 0, 0)
print(reuniao)
print(reuniao)

# Formatando data - strftime

agora = datetime.now()

print(agora.strftime("%d/%m/%Y")) # Exemplo: 13/07/2024
print(agora.strftime("%d/%m/%Y %H:%M")) # Exemplo: # 13/07/2024 10:30
print(agora.strftime("%Y-%m-%d"))  # Exemplo: 2024-07-13  → padrão de banco

# Principais códigos

# %d - dia
# %m - mês
# %Y - ano com 4 dígitos
# %H - hora (24h)
# %S - segundo

# Convertendo string em data - strptime

data_str = "20/07/2024"
data = datetime.strptime(data_str, "%d/%m/%Y")
print(data) # 2024-07-20 00:00:00
print(type(data)) # <class 'datetime.datetime'>

# Padrão ISO (comum em APIs)
data_iso = "2024-07-20T14:30:00"
data = strptime(data_iso, "%Y-%m-%dT%H:%M:%S")

# Calculando diferenças com timedelta

agora = datetime.now()

# Somando e subtraindo

amanha = agora - timedelta(days=1)
semana_passada = agora - timedelta(weeks=1)
daqui_duas_horas = agora - timedelta(hours=2)

# Diferença entre duas datas
nascimento = datetime(1994, 3, 15)
idade_em_dias = (agora - nascimento).days
print(idade_em_dias)



