# Logging - Sistema de Logs em Python

"""
O módulo logging fornece um sistema flexível de eventos de logging
para aplicações Python, permitindo diferentes níveis de severidade.
"""

import logging
import sys
from datetime import datetime

# ==================== CONFIGURAÇÃO BÁSICA ====================

def configurar_logging_basico():
    """Configura logging básico"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

def exemplo_logging_basico():
    """Exemplo de logging básico"""
    logger = logging.getLogger(__name__)
    
    logger.debug("Mensagem de debug")
    logger.info("Mensagem informativa")
    logger.warning("Mensagem de aviso")
    logger.error("Mensagem de erro")
    logger.critical("Mensagem crítica")

# ==================== NÍVEIS DE LOGGING ====================

def exemplo_niveis():
    """Demonstra os diferentes níveis de logging"""
    logger = logging.getLogger(__name__)
    
    # DEBUG: Informação detalhada para diagnóstico
    logger.debug("Variável x = 10, y = 20")
    
    # INFO: Confirmação de funcionamento normal
    logger.info("Aplicação iniciada com sucesso")
    
    # WARNING: Algo inesperado, mas ainda funciona
    logger.warning("Conexão com banco lenta")
    
    # ERROR: Erro mais sério, software não conseguiu fazer algo
    logger.error("Falha ao processar pagamento")
    
    # CRITICAL: Erro muito sério, programa pode não continuar
    logger.critical("Sistema sem memória disponível")

# ==================== CONFIGURAÇÃO AVANÇADA ====================

def configurar_logging_avancado():
    """Configura logging avançado com handlers"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    # Formatter personalizado
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Handler para console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    
    # Handler para arquivo
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

# ==================== LOGGING EM MÓDULOS ====================

def criar_logger_modulo(nome_modulo):
    """Cria logger para um módulo específico"""
    logger = logging.getLogger(nome_modulo)
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(
            logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        )
        logger.addHandler(handler)
    
    return logger

def exemplo_modulos():
    """Exemplo de logging em diferentes módulos"""
    logger_db = criar_logger_modulo('database')
    logger_api = criar_logger_modulo('api')
    
    logger_db.info("Conectando ao banco de dados...")
    logger_api.info("Recebendo requisição HTTP...")

# ==================== LOGGING COM EXCEPTIONS ====================

def exemplo_exception():
    """Exemplo de logging com informações de exceção"""
    logger = logging.getLogger(__name__)
    
    try:
        resultado = 1 / 0
    except ZeroDivisionError as e:
        logger.error("Erro ao dividir por zero", exc_info=True)
        # Ou usando logger.exception
        logger.exception("Erro ao dividir por zero")

# ==================== LOGGING ESTRUTURADO ====================

def exemplo_logging_estruturado():
    """Exemplo de logging estruturado"""
    logger = logging.getLogger(__name__)
    
    usuario = {"nome": "João", "idade": 30}
    logger.info("Usuário criado", extra={"usuario": usuario})
    
    # Em produção, considere usar bibliotecas como structlog
    # para logging estruturado mais avançado

# ==================== LOGGING COM FILTROS ====================

class FiltroDebug(logging.Filter):
    """Filtro personalizado para mensagens de debug"""
    def filter(self, record):
        # Permite apenas mensagens de debug
        return record.levelno == logging.DEBUG

def exemplo_filtro():
    """Exemplo de uso de filtros"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    # Adiciona filtro
    filtro = FiltroDebug()
    logger.addFilter(filtro)
    
    logger.debug("Esta mensagem vai passar")
    logger.info("Esta mensagem não vai passar")

# ==================== LOGGING COM ROTATION ====================

def configurar_rotation():
    """Configura logging com rotação de arquivos"""
    from logging.handlers import RotatingFileHandler
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    # RotatingFileHandler: rota quando arquivo atinge tamanho máximo
    handler = RotatingFileHandler(
        'app.log',
        maxBytes=1024*1024,  # 1MB
        backupCount=5
    )
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)

def configurar_time_rotation():
    """Configura logging com rotação por tempo"""
    from logging.handlers import TimedRotatingFileHandler
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    # TimedRotatingFileHandler: rota em intervalos de tempo
    handler = TimedRotatingFileHandler(
        'app.log',
        when='midnight',  # rota à meia-noite
        interval=1,
        backupCount=7
    )
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)

# ==================== LOGGING EM CLASSES ====================

class Servico:
    """Classe com logging integrado"""
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
        
        if not self.logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            handler.setFormatter(
                logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            )
            self.logger.addHandler(handler)
    
    def processar(self, dados):
        """Processa dados com logging"""
        self.logger.info(f"Iniciando processamento de {len(dados)} itens")
        
        try:
            # Processamento
            resultado = [d * 2 for d in dados]
            self.logger.info("Processamento concluído com sucesso")
            return resultado
        except Exception as e:
            self.logger.error(f"Erro no processamento: {e}")
            raise

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS PARA LOGGING:

1. Use níveis apropriados (DEBUG, INFO, WARNING, ERROR, CRITICAL)
2. Configure logging no início da aplicação
3. Use logger específico para cada módulo (__name__)
4. Inclua contexto relevante nas mensagens
5. Use exc_info=True ou exception() para erros
6. Evite logging em loops críticos de performance
7. Use logging estruturado para melhor análise
8. Configure rotação de arquivos para produção
9. Não use print() para logging em produção
10. Considere usar bibliotecas como structlog ou loguru
"""

if __name__ == "__main__":
    print("=== Logging Examples ===\n")
    
    # Configuração básica
    configurar_logging_basico()
    exemplo_logging_basico()
    
    # Exemplo de níveis
    print("\n--- Exemplo de Níveis ---")
    exemplo_niveis()
    
    # Configuração avançada
    print("\n--- Configuração Avançada ---")
    logger = configurar_logging_avancado()
    logger.info("Logging configurado com sucesso")
    
    # Exemplo de exceção
    print("\n--- Exemplo de Exceção ---")
    exemplo_exception()
    
    # Exemplo de classe
    print("\n--- Exemplo de Classe ---")
    servico = Servico()
    servico.processar([1, 2, 3, 4, 5])