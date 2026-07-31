# AWS SNS (Simple Notification Service) - Pub/Sub Messaging

"""
SNS é um serviço de mensageria pub/sub totalmente gerenciado que permite
enviar mensagens para múltiplos assinantes de forma escalável.
"""

import boto3
import json
from botocore.exceptions import ClientError

# Inicializar cliente SNS
sns_client = boto3.client('sns')

# ==================== CRIAR TÓPICO ====================

def create_topic(topic_name, attributes=None):
    """Cria um novo tópico SNS"""
    try:
        params = {'Name': topic_name}
        
        if attributes:
            params['Attributes'] = attributes
        
        response = sns_client.create_topic(**params)
        topic_arn = response['TopicArn']
        
        print(f"Tópico {topic_name} criado com sucesso!")
        print(f"ARN: {topic_arn}")
        
        return topic_arn
    except ClientError as e:
        print(f"Erro ao criar tópico: {e}")

# ==================== LISTAR TÓPICOS ====================

def list_topics():
    """Lista todos os tópicos SNS"""
    try:
        response = sns_client.list_topics()
        topics = response['Topics']
        print(f"Total de tópicos: {len(topics)}")
        for topic in topics:
            print(f"- {topic['TopicArn']}")
        return topics
    except ClientError as e:
        print(f"Erro ao listar tópicos: {e}")

# ==================== ASSINAR TÓPICO ====================

def subscribe_topic(topic_arn, protocol, endpoint, attributes=None):
    """Assina um endpoint a um tópico"""
    try:
        params = {
            'TopicArn': topic_arn,
            'Protocol': protocol,  # 'email', 'sms', 'http', 'https', 'lambda', 'sqs'
            'Endpoint': endpoint
        }
        
        if attributes:
            params['Attributes'] = attributes
        
        response = sns_client.subscribe(**params)
        subscription_arn = response['SubscriptionArn']
        
        print(f"Assinatura criada! ARN: {subscription_arn}")
        return subscription_arn
    except ClientError as e:
        print(f"Erro ao assinar tópico: {e}")

# ==================== LISTAR ASSINATURAS ====================

def list_subscriptions(topic_arn=None):
    """Lista assinaturas de um tópico ou todas"""
    try:
        if topic_arn:
            response = sns_client.list_subscriptions_by_topic(TopicArn=topic_arn)
        else:
            response = sns_client.list_subscriptions()
        
        subscriptions = response['Subscriptions']
        print(f"Total de assinaturas: {len(subscriptions)}")
        
        for sub in subscriptions:
            print(f"- Protocol: {sub['Protocol']}")
            print(f"  Endpoint: {sub['Endpoint']}")
            print(f"  Status: {sub['SubscriptionArn']}")
        
        return subscriptions
    except ClientError as e:
        print(f"Erro ao listar assinaturas: {e}")

# ==================== PUBLICAR MENSAGEM ====================

def publish_message(topic_arn, message, subject=None, message_attributes=None):
    """Publica uma mensagem em um tópico"""
    try:
        if isinstance(message, dict):
            message = json.dumps(message)
        
        params = {
            'TopicArn': topic_arn,
            'Message': message
        }
        
        if subject:
            params['Subject'] = subject
        
        if message_attributes:
            params['MessageAttributes'] = message_attributes
        
        response = sns_client.publish(**params)
        message_id = response['MessageId']
        
        print(f"Mensagem publicada com sucesso! ID: {message_id}")
        return message_id
    except ClientError as e:
        print(f"Erro ao publicar mensagem: {e}")

# ==================== DELETAR ASSINATURA ====================

def unsubscribe(subscription_arn):
    """Cancela uma assinatura"""
    try:
        sns_client.unsubscribe(SubscriptionArn=subscription_arn)
        print(f"Assinatura {subscription_arn} cancelada!")
    except ClientError as e:
        print(f"Erro ao cancelar assinatura: {e}")

# ==================== DELETAR TÓPICO ====================

def delete_topic(topic_arn):
    """Deleta um tópico SNS"""
    try:
        sns_client.delete_topic(TopicArn=topic_arn)
        print(f"Tópico {topic_arn} deletado!")
    except ClientError as e:
        print(f"Erro ao deletar tópico: {e}")

# ==================== SMS ====================

def send_sms(phone_number, message):
    """Envia uma mensagem SMS"""
    try:
        response = sns_client.publish(
            PhoneNumber=phone_number,
            Message=message
        )
        print(f"SMS enviado! ID: {response['MessageId']}")
        return response['MessageId']
    except ClientError as e:
        print(f"Erro ao enviar SMS: {e}")

# ==================== EMAIL ====================

def send_email(email, subject, message):
    """Envia um email"""
    try:
        response = sns_client.publish(
            TopicArn='',
            Protocol='email',
            Endpoint=email,
            Message=message,
            Subject=subject
        )
        print(f"Email enviado! ID: {response['MessageId']}")
        return response['MessageId']
    except ClientError as e:
        print(f"Erro ao enviar email: {e}")

# ==================== PLATFORM APPLICATIONS ====================

def create_platform_application(platform_name, platform, credentials):
    """Cria uma aplicação de plataforma (APNS, GCM, etc)"""
    try:
        response = sns_client.create_platform_application(
            Name=platform_name,
            Platform=platform,  # 'APNS', 'APNS_SANDBOX', 'GCM', 'ADM'
            PlatformPrincipal=credentials.get('principal'),
            PlatformCredential=credentials.get('credential')
        )
        print(f"Aplicação de plataforma {platform_name} criada!")
        return response
    except ClientError as e:
        print(f"Erro ao criar aplicação de plataforma: {e}")

# ==================== ATRIBUTOS DO TÓPICO ====================

def set_topic_attributes(topic_arn, attribute_name, attribute_value):
    """Define atributos do tópico"""
    try:
        sns_client.set_topic_attributes(
            TopicArn=topic_arn,
            AttributeName=attribute_name,
            AttributeValue=attribute_value
        )
        print(f"Atributo {attribute_name} definido!")
    except ClientError as e:
        print(f"Erro ao definir atributo: {e}")

# ==================== EXEMPLOS DE ATRIBUTOS ====================

# Tópico com criptografia
ENCRYPTED_TOPIC_ATTRIBUTES = {
    'KmsMasterKeyId': 'alias/aws/sns'  # KMS key para criptografia
}

# Tópico com delivery de falhas
FAILURE_FEEDBACK_ATTRIBUTES = {
    'ApplicationSuccessFeedbackRoleArn': 'arn:aws:iam::123456789012:role/SNSFailureFeedback',
    'ApplicationFailureFeedbackRoleArn': 'arn:aws:iam::123456789012:role/SNSFailureFeedback'
}

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS SNS:

1. Use tópicos para pub/sub e filas SQS para processamento assíncrono
2. Implemente dead-letter queues para mensagens que falham
3. Use message attributes para filtragem e roteamento
4. Configure IAM policies para controle de acesso granular
5. Use criptografia com KMS para mensagens sensíveis
6. Monitore com CloudWatch métricas (NumberOfNotificationsDelivered, etc)
7. Use server-side encryption para tópicos sensíveis
8. Configure delivery retries e feedback
9. Use tags para organizar tópicos por ambiente/projeto
10. Valide endpoints antes de assinar (especialmente email)
"""

if __name__ == "__main__":
    print("=== AWS SNS Examples ===\n")
    
    # Listar tópicos existentes
    print("Tópicos SNS existentes:")
    list_topics()
    
    # Exemplo de criação de tópico
    # topic_arn = create_topic("meu-topico")
    
    # Exemplo de assinatura
    # subscribe_topic(topic_arn, "email", "usuario@example.com")
    
    # Exemplo de publicação
    # publish_message(topic_arn, {"message": "Olá SNS!"}, "Assunto da mensagem")
