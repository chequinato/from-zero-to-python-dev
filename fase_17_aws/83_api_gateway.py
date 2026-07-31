# AWS API Gateway - Gerenciamento de APIs

"""
API Gateway é um serviço totalmente gerenciado que facilita a criação,
publicação, manutenção, monitoramento e proteção de APIs em qualquer escala.
"""

import boto3
import json
from botocore.exceptions import ClientError

# Inicializar cliente API Gateway
apigateway_client = boto3.client('apigateway')

# ==================== CRIAR REST API ====================

def create_rest_api(api_name, description=''):
    """Cria uma nova REST API"""
    try:
        response = apigateway_client.create_rest_api(
            name=api_name,
            description=description,
            version='1.0'
        )
        
        api_id = response['id']
        print(f"REST API {api_name} criada com sucesso!")
        print(f"API ID: {api_id}")
        
        return api_id
    except ClientError as e:
        print(f"Erro ao criar REST API: {e}")

# ==================== LISTAR APIS ====================

def list_apis():
    """Lista todas as REST APIs"""
    try:
        response = apigateway_client.get_rest_apis()
        apis = response['items']
        print(f"Total de APIs: {len(apis)}")
        for api in apis:
            print(f"- {api['name']} (ID: {api['id']})")
        return apis
    except ClientError as e:
        print(f"Erro ao listar APIs: {e}")

# ==================== CRIAR RECURSO ====================

def create_resource(api_id, parent_id, resource_path):
    """Cria um novo recurso na API"""
    try:
        response = apigateway_client.create_resource(
            restApiId=api_id,
            parentId=parent_id,
            pathPart=resource_path
        )
        
        resource_id = response['id']
        print(f"Recurso {resource_path} criado! ID: {resource_id}")
        
        return resource_id
    except ClientError as e:
        print(f"Erro ao criar recurso: {e}")

# ==================== CRIAR MÉTODO ====================

def create_method(api_id, resource_id, http_method, authorization='NONE'):
    """Cria um método HTTP em um recurso"""
    try:
        apigateway_client.put_method(
            restApiId=api_id,
            resourceId=resource_id,
            httpMethod=http_method,
            authorizationType=authorization
        )
        
        print(f"Método {http_method} criado no recurso {resource_id}")
    except ClientError as e:
        print(f"Erro ao criar método: {e}")

# ==================== INTEGRAR COM LAMBDA ====================

def integrate_with_lambda(api_id, resource_id, http_method, lambda_arn, region):
    """Integra um método com uma função Lambda"""
    try:
        # Cria a integração
        apigateway_client.put_integration(
            restApiId=api_id,
            resourceId=resource_id,
            httpMethod=http_method,
            type='AWS_PROXY',
            integrationHttpMethod='POST',
            uri=f"arn:aws:apigateway:{region}:lambda:path/2015-03-31/functions/{lambda_arn}/invocations"
        )
        
        print(f"Integração com Lambda criada!")
        
        # Adiciona permissão para a API Gateway invocar a Lambda
        lambda_client = boto3.client('lambda')
        source_arn = f"arn:aws:execute-api:{region}:*:{api_id}/*/{http_method}{get_resource_path(api_id, resource_id)}"
        
        lambda_client.add_permission(
            FunctionName=lambda_arn,
            StatementId=f"apigateway-{http_method}-{resource_id}",
            Action='lambda:InvokeFunction',
            Principal='apigateway.amazonaws.com',
            SourceArn=source_arn
        )
        
        print("Permissão Lambda adicionada!")
    except ClientError as e:
        print(f"Erro ao integrar com Lambda: {e}")

def get_resource_path(api_id, resource_id):
    """Obtém o caminho completo do recurso"""
    try:
        response = apigateway_client.get_resource(
            restApiId=api_id,
            resourceId=resource_id
        )
        return response['path']
    except ClientError as e:
        print(f"Erro ao obter caminho do recurso: {e}")
        return ''

# ==================== DEPLOY API ====================

def deploy_api(api_id, stage_name, stage_description='', description=''):
    """Faz deploy da API para um stage"""
    try:
        response = apigateway_client.create_deployment(
            restApiId=api_id,
            stageName=stage_name,
            stageDescription=stage_description,
            description=description
        )
        
        deployment_id = response['id']
        print(f"API deployada no stage {stage_name}! Deployment ID: {deployment_id}")
        
        return deployment_id
    except ClientError as e:
        print(f"Erro ao fazer deploy: {e}")

# ==================== CRIAR USAGE PLAN ====================

def create_usage_plan(plan_name, api_stages, throttle=None, quota=None):
    """Cria um usage plan para controle de taxa"""
    try:
        params = {
            'name': plan_name,
            'apiStages': api_stages
        }
        
        if throttle:
            params['throttle'] = throttle
        if quota:
            params['quota'] = quota
        
        response = apigateway_client.create_usage_plan(**params)
        plan_id = response['id']
        
        print(f"Usage plan {plan_name} criado! ID: {plan_id}")
        return plan_id
    except ClientError as e:
        print(f"Erro ao criar usage plan: {e}")

# ==================== CRIAR API KEY ====================

def create_api_key(key_name, stage_keys=None):
    """Cria uma API key"""
    try:
        params = {'name': key_name}
        
        if stage_keys:
            params['stageKeys'] = stage_keys
        
        response = apigateway_client.create_api_key(**params)
        api_key = response['value']
        
        print(f"API key criada: {api_key}")
        print("⚠️  Salve esta key agora, pois não será mostrada novamente!")
        
        return api_key
    except ClientError as e:
        print(f"Erro ao criar API key: {e}")

# ==================== DELETAR API ====================

def delete_rest_api(api_id):
    """Deleta uma REST API"""
    try:
        apigateway_client.delete_rest_api(restApiId=api_id)
        print(f"API {api_id} deletada com sucesso!")
    except ClientError as e:
        print(f"Erro ao deletar API: {e}")

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS API GATEWAY:

1. Use usage plans e API keys para controle de taxa
2. Implemente autorização com Cognito, IAM ou Lambda authorizers
3. Use stages para separar ambientes (dev, staging, prod)
4. Configure CORS para APIs públicas
5. Use request/response validators para validação
6. Implemente caching para reduzir latência
7. Use CloudWatch para monitoramento e alertas
8. Configure WAF para proteção contra ataques
9. Use variáveis de stage para configuração
10. Considere usar HTTP APIs para APIs REST simples (mais barato)
"""

if __name__ == "__main__":
    print("=== AWS API Gateway Examples ===\n")
    
    # Listar APIs existentes
    print("REST APIs existentes:")
    list_apis()
    
    # Exemplo de criação de API
    # api_id = create_rest_api("minha-api", "API de exemplo")
    
    # Exemplo de deploy
    # deploy_api(api_id, "prod", "Produção", "Primeiro deploy")
