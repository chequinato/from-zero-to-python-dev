
'''

Timeout é o limite de tempo que você dá pra uma requisição esperar por resposta antes de desistir.
Sem isso, se a API travar ou ficar sem resposder, seu código pode ficar pendurado pra sempre esperando — em produção isso é bem perigoso (trava fila de processos, estoura tempo de execução de Lambda, etc).

'''

# Usando timeout do requests

import requests

# timeout em segundos - se não responder em 5s, lança exceção
resposta = requests.get("http://httpbin.org", timeout=5)

# Timeout separado pra conectar e pra ler a resposta
resposta = requests.get("https://api.exemplo.com/usuarios", timeout=(3, 10))

# Tratando erro de timeout

try:
    resposta = requests.get("http://httpbin.org", timeout=5)
    resposta.raise_for_status()

except requests.exceptions.Timeout:
    print("A API demorou demais e a requisição foi cancelada")

except requests.exceptions.RequestException as e:
    print(f"Outro erro na requisição {e}")

# Retry - tentando de novo quando dá timeout

import time

def buscar_com_retry(url, tentativas=3, timeout=5):
    for tentativas in range(1, tentativas + 1):
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status
            return response.json()
        except requests.exceptions.Timeout:
            print(f"Tentativa {tentativa} deu timeout, tentando de novo...")
            time.sleep(2) # espera um pouco antes de tentar de novo
    return None  # todas as tentativas falharam

