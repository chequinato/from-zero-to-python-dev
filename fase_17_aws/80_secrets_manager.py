# AWS Secrets Manager - Gerenciamento de Segredos

"""
Secrets Manager ajuda a proteger segredos como senhas, chaves de API
e tokens de banco de dados, rotacionando-os automaticamente.
"""

import boto3
import json
from botocore.exceptions import ClientError

# Inicializar cliente Secrets Manager
secrets_client = boto3.client('secretsmanager')

# ==================== CRIAR SEGREDO ====================

def create_secret(secret_name, secret_value, description=''):
    """Cria um novo segredo no Secrets Manager"""
    try:
        if isinstance(secret_value, dict):
            secret_string = json.dumps(secret_value)
        else:
            secret_string = str(secret_value)
        
        response = secrets_client.create_secret(
            Name=secret_name,
            Description=description,
            SecretString=secret_string
        )
        
        print(f"Segredo {secret_name} criado com sucesso!")
        print(f"ARN: {response['ARN']}")
        return response
    except ClientError as e:
        print(f"Erro ao criar segredo: {e}")

# ==================== OBTER SEGREDO ====================

def get_secret(secret_name):
    """Obtém um segredo do Secrets Manager"""
    try:
        response = secrets_client.get_secret_value(SecretId=secret_name)
        
        if 'SecretString' in response:
            secret = response['SecretString']
            # Tenta fazer parse como JSON
            try:
                return json.loads(secret)
            except json.JSONDecodeError:
                return secret
        else:
            return response['SecretBinary']
    except ClientError as e:
        print(f"Erro ao obter segredo: {e}")

# ==================== ATUALIZAR SEGREDO ====================

def update_secret(secret_name, new_value):
    """Atualiza um segredo existente"""
    try:
        if isinstance(new_value, dict):
            secret_string = json.dumps(new_value)
        else:
            secret_string = str(new_value)
        
        response = secrets_client.update_secret(
            SecretId=secret_name,
            SecretString=secret_string
        )
        
        print(f"Segredo {secret_name} atualizado com sucesso!")
        print(f"Version: {response['VersionId']}")
        return response
    except ClientError as e:
        print(f"Erro ao atualizar segredo: {e}")

# ==================== LISTAR SEGREDOS ====================

def list_secrets():
    """Lista todos os segredos"""
    try:
        response = secrets_client.list_secrets()
        secrets = response['SecretList']
        print(f"Total de segredos: {len(secrets)}")
        for secret in secrets:
            print(f"- {secret['Name']} (ARN: {secret['ARN']})")
            print(f"  Last rotated: {secret.get('LastRotatedDate', 'Never')}")
        return secrets
    except ClientError as e:
        print(f"Erro ao listar segredos: {e}")

# ==================== DELETAR SEGREDO ====================

def delete_secret(secret_name, force_delete_without_recovery=False):
    """Deleta um segredo"""
    try:
        if force_delete_without_recovery:
            response = secrets_client.delete_secret(
                SecretId=secret_name,
                ForceDeleteWithoutRecovery=True
            )
        else:
            response = secrets_client.delete_secret(
                SecretId=secret_name,
                RecoveryWindowInDays=30  # Período de recuperação
            )
        
        print(f"Segredo {secret_name} deletado!")
        return response
    except ClientError as e:
        print(f"Erro ao deletar segredo: {e}")

# ==================== ROTAÇÃO ====================

def rotate_secret(secret_name, rotation_lambda_arn):
    """Configura rotação automática de segredos"""
    try:
        response = secrets_client.rotate_secret(
            SecretId=secret_name,
            RotationLambdaARN=rotation_lambda_arn,
            RotationRules={
                'AutomaticallyAfterDays': 30  # Rota a cada 30 dias
            }
        )
        
        print(f"Rotação configurada para {secret_name}")
        return response
    except ClientError as e:
        print(f"Erro ao configurar rotação: {e}")

# ==================== RESTAURAR SEGREDO ====================

def restore_secret(secret_name):
    """Restaura um segredo deletado (dentro do período de recuperação)"""
    try:
        response = secrets_client.restore_secret(SecretId=secret_name)
        print(f"Segredo {secret_name} restaurado com sucesso!")
        return response
    except ClientError as e:
        print(f"Erro ao restaurar segredo: {e}")

# ==================== EXEMPLOS DE USO ====================

def example_database_credentials():
    """Exemplo de credenciais de banco de dados"""
    db_credentials = {
        "username": "admin",
        "password": "senha_segura_123",
        "host": "database.example.com",
        "port": 5432,
        "dbname": "production_db"
    }
    return db_credentials

def example_api_keys():
    """Exemplo de chaves de API"""
    api_keys = {
        "api_key": "sk_live_1234567890abcdef",
        "api_secret": "sk_secret_1234567890abcdef",
        "webhook_secret": "whsec_1234567890abcdef"
    }
    return api_keys

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS SECRETS MANAGER:

1. Nunca hardcode segredos no código
2. Use rotação automática para credenciais sensíveis
3. Use IAM policies para controlar acesso aos segredos
4. Use tags para organizar segredos por ambiente/projeto
5. Implemente recuperação de segredos deletados
6. Monitore acesso aos segredos com CloudTrail
7. Use KMS para criptografia de segredos
8. Limite o número de versões de segredos
9. Use descrições claras para identificar o propósito
10. Considere usar Parameter Store para configurações não sensíveis
"""

if __name__ == "__main__":
    print("=== AWS Secrets Manager Examples ===\n")
    
    # Listar segredos existentes
    print("Segredos existentes:")
    list_secrets()
    
    # Exemplo de criação de segredo
    # create_secret("prod/db/credentials", example_database_credentials(), "Credenciais do banco de produção")
    
    # Exemplo de obtenção de segredo
    # secret = get_secret("prod/db/credentials")
    # print("Segredo obtido:", secret)
