
'''

Status codes são números de 3 dígitos que a API devolve pra dizer o que aconteceu com a requisição.
Eles são agrupados por faixa — a primeira dezena já te diz a categoria geral.

'''

# 1xx - informational (requisição recebida, processando
# 2xx - sucess (deu certo)
# 3xx - redirection (precisa de mais direcionamento)
# 4xx - client error (erro do lado de quem fez a requisição)
# 5xx - server error (erro do lado do servidor)

# Os mais comuns do dia a dia:

# 2xx - Sucesso
# 200 OK              → deu tudo certo (GET, PUT, PATCH, DELETE)
# 201 Created          → recurso criado com sucesso (POST)
# 204 No Content        → deu certo, mas não tem corpo de resposta (DELETE, às vezes)

# 4xx - Erro do cliente
# 400 Bad Request        → requisição mal formada (json errado, campo faltando)
# 401 Unauthorized        → falta autenticação (token ausente/inválido)
# 403 Forbidden           → autenticado, mas sem permissão pra isso
# 404 Not Found           → recurso não existe
# 429 Too Many Requests   → você tá batendo demais na API (rate limit)

# 5xx - Erro do servidor
# 500 Internal Server Error → deu erro genérico no servidor
# 502 Bad Gateway           → servidor intermediário recebeu resposta inválida
# 503 Service Unavailable   → servidor fora do ar/sobrecarregado

# Verificando status code na prática:
import requests

resposta = requests.get("https://api.exemplo.com/usuarios")
print(resposta.status_code) # 200

if resposta.status_code == 200:
    print("Deu certo!")

elif resposta.status_code == 404:
    print("Não encontrado")

elif resposta.status_code == 500:
    print("Erro no servidor")

# Atalho útil - ok e raise_for_status

resposta = requests.get("https://api.exemplo.com/usuarios")
print(resposta.ok) # True se status_code for entre 200-399

# Lança uma exceção automaticamente se o status for erro (4xx ou 5xx)
resposta.raise_for_status()