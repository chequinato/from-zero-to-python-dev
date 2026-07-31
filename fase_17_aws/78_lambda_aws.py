# AWS Lambda - Serverless Computing

"""
AWS Lambda é um serviço serverless que executa código em resposta a eventos
e gerencia automaticamente os recursos de computação.
"""

import boto3
import json
from botocore.exceptions import ClientError

# Inicializar cliente Lambda
lambda_client = boto3.client('lambda')

# ==================== CRIAR FUNÇÃO LAMBDA ====================

def create_lambda_function(function_name, role_arn, handler_code, runtime='python3.9'):
    """Cria uma nova função Lambda"""
    try:
        response = lambda_client.create_function(
            FunctionName=function_name,
            Runtime=runtime,
            Role=role_arn,
            Handler='lambda_function.lambda_handler',
            Code={
                'ZipFile': handler_code
            },
            Description='Função Lambda criada via boto3',
            Timeout=30,
            MemorySize=128,
            Publish=True
        )
        print(f"Função Lambda {function_name} criada com sucesso!")
        return response
    except ClientError as e:
        print(f"Erro ao criar função Lambda: {e}")

# ==================== INVOCAÇÃO ====================

def invoke_lambda(function_name, payload=None, invocation_type='RequestResponse'):
    """Invoca uma função Lambda"""
    try:
        if payload:
            payload = json.dumps(payload)
        
        response = lambda_client.invoke(
            FunctionName=function_name,
            InvocationType=invocation_type,  # 'RequestResponse', 'Event', 'DryRun'
            Payload=payload if payload else b''
        )
        
        if invocation_type == 'RequestResponse':
            response_payload = response['Payload'].read()
            return json.loads(response_payload)
        else:
            print(f"Função {function_name} invocada com sucesso!")
            return response
    except ClientError as e:
        print(f"Erro ao invocar função Lambda: {e}")

# ==================== LISTAR FUNÇÕES ====================

def list_lambda_functions():
    """Lista todas as funções Lambda"""
    try:
        response = lambda_client.list_functions()
        functions = response['Functions']
        print(f"Total de funções Lambda: {len(functions)}")
        for func in functions:
            print(f"- {func['FunctionName']} (Runtime: {func['Runtime']}, Memory: {func['MemorySize']}MB)")
        return functions
    except ClientError as e:
        print(f"Erro ao listar funções Lambda: {e}")

# ==================== ATUALIZAR CÓDIGO ====================

def update_lambda_code(function_name, zip_file_path):
    """Atualiza o código de uma função Lambda"""
    try:
        with open(zip_file_path, 'rb') as f:
            zip_file = f.read()
        
        response = lambda_client.update_function_code(
            FunctionName=function_name,
            ZipFile=zip_file
        )
        print(f"Código da função {function_name} atualizado com sucesso!")
        return response
    except ClientError as e:
        print(f"Erro ao atualizar código: {e}")
    except FileNotFoundError:
        print(f"Arquivo {zip_file_path} não encontrado")

# ==================== CONFIGURAÇÃO ====================

def update_lambda_config(function_name, timeout=None, memory_size=None, environment_vars=None):
    """Atualiza a configuração de uma função Lambda"""
    try:
        params = {'FunctionName': function_name}
        
        if timeout:
            params['Timeout'] = timeout
        if memory_size:
            params['MemorySize'] = memory_size
        if environment_vars:
            params['Environment'] = {'Variables': environment_vars}
        
        response = lambda_client.update_function_configuration(**params)
        print(f"Configuração da função {function_name} atualizada!")
        return response
    except ClientError as e:
        print(f"Erro ao atualizar configuração: {e}")

# ==================== VARIÁVEIS DE AMBIENTE ====================

def get_lambda_environment(function_name):
    """Obtém as variáveis de ambiente de uma função Lambda"""
    try:
        response = lambda_client.get_function_configuration(FunctionName=function_name)
        env_vars = response.get('Environment', {}).get('Variables', {})
        print(f"Variáveis de ambiente de {function_name}:")
        for key, value in env_vars.items():
            print(f"  {key}: {value}")
        return env_vars
    except ClientError as e:
        print(f"Erro ao obter variáveis de ambiente: {e}")

# ==================== LAYERS ====================

def create_layer(layer_name, zip_file_path, compatible_runtimes):
    """Cria um Lambda Layer"""
    try:
        with open(zip_file_path, 'rb') as f:
            zip_file = f.read()
        
        response = lambda_client.publish_layer_version(
            LayerName=layer_name,
            Description='Layer criado via boto3',
            Content={'ZipFile': zip_file},
            CompatibleRuntimes=compatible_runtimes
        )
        print(f"Layer {layer_name} criado com sucesso!")
        return response
    except ClientError as e:
        print(f"Erro ao criar layer: {e}")

def attach_layer_to_function(function_name, layer_arn):
    """Anexa um layer a uma função Lambda"""
    try:
        response = lambda_client.update_function_configuration(
            FunctionName=function_name,
            Layers=[layer_arn]
        )
        print(f"Layer anexado à função {function_name}")
        return response
    except ClientError as e:
        print(f"Erro ao anexar layer: {e}")

# ==================== EVENT SOURCES ====================

def add_s3_trigger(function_name, bucket_name, events=['s3:ObjectCreated:*']):
    """Adiciona um trigger S3 à função Lambda"""
    try:
        # Isso requer permissões S3 e Lambda
        s3_client = boto3.client('s3')
        
        notification_config = {
            'LambdaFunctionConfigurations': [
                {
                    'LambdaFunctionArn': f"arn:aws:lambda:us-east-1:123456789012:function:{function_name}",
                    'Events': events
                }
            ]
        }
        
        s3_client.put_bucket_notification_configuration(
            Bucket=bucket_name,
            NotificationConfiguration=notification_config
        )
        print(f"Trigger S3 adicionado à função {function_name}")
    except ClientError as e:
        print(f"Erro ao adicionar trigger S3: {e}")

# ==================== LOGS ====================

def get_lambda_logs(function_name, start_time=None, end_time=None):
    """Obtém logs do CloudWatch para uma função Lambda"""
    try:
        logs_client = boto3.client('logs')
        log_group_name = f"/aws/lambda/{function_name}"
        
        params = {
            'logGroupName': log_group_name,
            'limit': 50
        }
        
        if start_time:
            params['startTime'] = start_time
        if end_time:
            params['endTime'] = end_time
        
        response = logs_client.filter_log_events(**params)
        
        print(f"Logs da função {function_name}:")
        for event in response['events']:
            timestamp = event['timestamp']
            message = event['message']
            print(f"[{timestamp}] {message}")
        
        return response
    except ClientError as e:
        print(f"Erro ao obter logs: {e}")

# ==================== DELETAR FUNÇÃO ====================

def delete_lambda_function(function_name):
    """Deleta uma função Lambda"""
    try:
        lambda_client.delete_function(FunctionName=function_name)
        print(f"Função Lambda {function_name} deletada com sucesso!")
    except ClientError as e:
        print(f"Erro ao deletar função Lambda: {e}")

# ==================== EXEMPLO DE CÓDIGO LAMBDA ====================

SAMPLE_LAMBDA_CODE = """
import json

def lambda_handler(event, context):
    # Evento contém os dados de entrada
    print("Evento recebido:", json.dumps(event))
    
    # Contexto contém informações sobre a invocação
    print("Request ID:", context.request_id)
    print("Função ARN:", context.function_name)
    
    # Processamento
    result = {
        'statusCode': 200,
        'body': json.dumps({'message': 'Hello from Lambda!'})
    }
    
    return result
"""

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS AWS LAMBDA:

1. Mantenha as funções pequenas e focadas em uma única responsabilidade
2. Use variáveis de ambiente para configuração
3. Gerencie dependências com cuidado (use layers para bibliotecas comuns)
4. Monitore com CloudWatch Logs e X-Ray
5. Use timeouts apropriados (não muito curtos, não muito longos)
6. Otimize o uso de memória (mais memória = mais CPU)
7. Use conexões reutilizáveis (fora do handler)
8. Implemente retry e error handling
9. Use aliases e versões para deployments
10. Considere usar frameworks como Serverless ou SAM para infraestrutura
"""

if __name__ == "__main__":
    print("=== AWS Lambda Examples ===\n")
    
    # Listar funções existentes
    print("Funções Lambda existentes:")
    list_lambda_functions()
    
    # Exemplo de invocação (requer função existente)
    # invoke_lambda("minha-funcao", {"key": "value"})
