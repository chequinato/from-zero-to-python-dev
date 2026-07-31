
# RAISE E EXCEPTIONS CUSTOMIZADAS

# RAISE

# raise → lança uma exceção manualmente

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisor não pode ser zero")
    return a / b

try:
    dividir(10, 0)
except ZeroDivisionError as e:
    print(e)   # Divisor não pode ser zero

# Relançando exceção (re-raise)
def processar(valor):
    try:
        return int(valor)
    except ValueError as e:
        print(f"Log: falha ao converter '{valor}'")
        raise   # relança a mesma exceção para cima

try:
    processar("abc")
except ValueError as e:
    print(f"Tratado fora: {e}")

# Raise com causa (exception chaining)
def buscar_configuracao(chave):
    config = {"host": "localhost"}
    try:
        return config[chave]
    except KeyError as e:
        raise ValueError(f"Configuração '{chave}' não encontrada") from e

try:
    buscar_configuracao("porta")
except ValueError as e:
    print(e)
    print(f"Causa: {e.__cause__}")

# EXCEPTIONS CUSTOMIZADAS

# Crie suas próprias herdando de Exception

class ErroBase(Exception):
    """Exceção base da aplicação"""
    pass

class ErroValidacao(ErroBase):
    """Erro de validação de dados"""
    def __init__(self, campo, mensagem):
        self.campo = campo
        super().__init__(f"Validação falhou em '{campo}': {mensagem}")

class ErroNegocio(ErroBase):
    """Erro de regra de negócio"""
    pass

class ErroRecursoNaoEncontrado(ErroBase):
    """Recurso não encontrado"""
    def __init__(self, recurso, id):
        super().__init__(f"{recurso} com id={id} não encontrado")
        self.recurso = recurso
        self.id = id

# Usando as exceções customizadas
def criar_usuario(dados):
    if not dados.get("nome"):
        raise ErroValidacao("nome", "campo obrigatório")
    if len(dados.get("nome", "")) < 2:
        raise ErroValidacao("nome", "mínimo 2 caracteres")
    if not dados.get("email") or "@" not in dados["email"]:
        raise ErroValidacao("email", "email inválido")
    return {"id": 1, **dados}

try:
    criar_usuario({"nome": "", "email": "teste@email.com"})
except ErroValidacao as e:
    print(e)           # Validação falhou em 'nome': campo obrigatório
    print(e.campo)     # nome

def buscar_usuario(id):
    usuarios = {1: "Miguel", 2: "João"}
    if id not in usuarios:
        raise ErroRecursoNaoEncontrado("Usuário", id)
    return usuarios[id]

try:
    buscar_usuario(99)
except ErroRecursoNaoEncontrado as e:
    print(e)            # Usuário com id=99 não encontrado
    print(e.recurso)    # Usuário
    print(e.id)         # 99

# HIERARQUIA DE EXCEPTIONS

# Organizar exceções em hierarquia permite capturar no nível certo
class ErroAWS(ErroBase):
    pass

class ErroS3(ErroAWS):
    pass

class ErroLambda(ErroAWS):
    pass

class ErroS3ArquivoNaoEncontrado(ErroS3):
    def __init__(self, bucket, chave):
        super().__init__(f"s3://{bucket}/{chave} não encontrado")

try:
    raise ErroS3ArquivoNaoEncontrado("meu-bucket", "dados/2024.csv")
except ErroS3 as e:
    print(f"Erro S3: {e}")     # captura qualquer ErroS3
except ErroAWS as e:
    print(f"Erro AWS: {e}")    # captura qualquer ErroAWS
except ErroBase as e:
    print(f"Erro geral: {e}")  # captura qualquer erro da app

# BOAS PRÁTICAS


# Crie uma exceção base para sua aplicação
# Nomeie com sufixo Error ou Erro
# Adicione atributos úteis (campo, recurso, código)
# Docstring explicando quando usar
# Prefira específico ao genérico ao capturar
# Nunca silencie exceções sem motivo

# Errado — silencia o erro sem avisar ninguém
try:
    resultado = int("abc")
except Exception:
    pass   # o erro sumiu e você não sabe o que aconteceu

# Correto — pelo menos loga
import logging

try:
    resultado = int("abc")
except Exception as e:
    logging.error(f"Erro inesperado: {e}")
    raise   # relança para não esconder o problema