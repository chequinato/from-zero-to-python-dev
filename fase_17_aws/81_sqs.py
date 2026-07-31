# AWS SQS (Simple Queue Service) - Filas de Mensagens

"""
SQS é um serviço de filas totalmente gerenciado que permite desacoplar
e escalar microserviços, sistemas distribuídos e aplicações serverless.
"""

import boto3
import json
import time
from botocore.exceptions import ClientError

# Inicializar cliente SQS
sqs_client = boto3.client('sqs')
sqs_resource = boto3.resource('sqs')

# ==================== CRIAR FILA ====================

def create_queue(queue_name, attributes=None):
    """Cria uma nova fila SQS"""
    try:
        params = {'QueueName': queue_name}
        
        if attributes:
            params['Attributes'] = attributes
        
        response = sqs_client.create_queue(**params)
        queue_url = response['QueueUrl']
        queue_arn = response['QueueArn']
        
        print(f"Fila {queue_name} criada com sucesso!")
        print(f"URL: {queue_url}")
        print(f"ARN: {queue_arn}")
        
        return queue_url, queue_arn
    except ClientError as e:
        print(f"Erro ao criar fila: {e}")

# ==================== LISTAR FILAS ====================

def list_queues():
    """Lista todas as filas SQS"""
    try:
        response = sqs_client.list_queues()
        queue_urls = response.get('QueueUrls', [])
        print(f"Total de filas: {len(queue_urls)}")
        for url in queue_urls:
            print(f"- {url}")
        return queue_urls
    except ClientError as e:
        print(f"Erro ao listar filas: {e}")

# ==================== ENVIAR MENSAGEM ====================

def send_message(queue_url, message_body, message_attributes=None):
    """Envia uma mensagem para a fila"""
    try:
        if isinstance(message_body, dict):
            message_body = json.dumps(message_body)
        
        params = {
            'QueueUrl': queue_url,
            'MessageBody': message_body
        }
        
        if message_attributes:
            params['MessageAttributes'] = message_attributes
        
        response = sqs_client.send_message(**params)
        message_id = response['MessageId']
        
        print(f"Mensagem enviada com sucesso! ID: {message_id}")
        return message_id
    except ClientError as e:
        print(f"Erro ao enviar mensagem: {e}")

# ==================== RECEBER MENSAGEM ====================

def receive_message(queue_url, max_messages=1, wait_time=0):
    """Recebe mensagens da fila"""
    try:
        response = sqs_client.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=max_messages,
            WaitTimeSeconds=wait_time,  # Long polling
            AttributeNames=['All'],
            MessageAttributeNames=['All']
        )
        
        messages = response.get('Messages', [])
        print(f"Mensagens recebidas: {len(messages)}")
        
        for message in messages:
            print(f"ID: {message['MessageId']}")
            print(f"Body: {message['Body']}")
            print(f"ReceiptHandle: {message['ReceiptHandle']}")
        
        return messages
    except ClientError as e:
        print(f"Erro ao receber mensagens: {e}")

# ==================== DELETAR MENSAGEM ====================

def delete_message(queue_url, receipt_handle):
    """Deleta uma mensagem da fila após processamento"""
    try:
        sqs_client.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )
        print("Mensagem deletada com sucesso!")
    except ClientError as e:
        print(f"Erro ao deletar mensagem: {e}")

# ==================== PROCESSAR MENSAGENS ====================

def process_messages(queue_url, callback, max_messages=10, visibility_timeout=30):
    """Processa mensagens da fila com uma função de callback"""
    processed = 0
    
    while processed < max_messages:
        messages = receive_message(queue_url, max_messages=1, wait_time=20)
        
        if not messages:
            print("Nenhuma mensagem disponível")
            break
        
        for message in messages:
            try:
                # Processa a mensagem
                callback(message)
                
                # Deleta a mensagem após processamento bem-sucedido
                delete_message(queue_url, message['ReceiptHandle'])
                processed += 1
                
            except Exception as e:
                print(f"Erro ao processar mensagem: {e}")
                # A mensagem ficará visível novamente após o visibility timeout

# ==================== ATRIBUTOS DA FILA ====================

def get_queue_attributes(queue_url, attribute_names=['All']):
    """Obtém atributos da fila"""
    try:
        response = sqs_client.get_queue_attributes(
            QueueUrl=queue_url,
            AttributeNames=attribute_names
        )
        
        attributes = response['Attributes']
        print(f"Atributos da fila:")
        for key, value in attributes.items():
            print(f"  {key}: {value}")
        
        return attributes
    except ClientError as e:
        print(f"Erro ao obter atributos: {e}")

def set_queue_attributes(queue_url, attributes):
    """Define atributos da fila"""
    try:
        sqs_client.set_queue_attributes(
            QueueUrl=queue_url,
            Attributes=attributes
        )
        print("Atributos da fila atualizados!")
    except ClientError as e:
        print(f"Erro ao definir atributos: {e}")

# ==================== DEAD LETTER QUEUE ====================

def create_dead_letter_queue(main_queue_name, dlq_name):
    """Cria uma fila principal e sua Dead Letter Queue"""
    try:
        # Cria a DLQ
        dlq_url, dlq_arn = create_queue(dlq_name)
        
        # Cria a fila principal com redirecionamento para DLQ
        main_queue_url, main_queue_arn = create_queue(
            main_queue_name,
            attributes={
                'RedrivePolicy': json.dumps({
                    'deadLetterTargetArn': dlq_arn,
                    'maxReceiveCount': 3  # Após 3 tentativas, vai para DLQ
                })
            }
        )
        
        print("Fila principal e DLQ criadas!")
        return main_queue_url, dlq_url
    except ClientError as e:
        print(f"Erro ao criar filas: {e}")

# ==================== DELETAR FILA ====================

def delete_queue(queue_url):
    """Deleta uma fila SQS"""
    try:
        sqs_client.delete_queue(QueueUrl=queue_url)
        print(f"Fila deletada com sucesso!")
    except ClientError as e:
        print(f"Erro ao deletar fila: {e}")

# ==================== PURGAR FILA ====================

def purge_queue(queue_url):
    """Remove todas as mensagens de uma fila"""
    try:
        sqs_client.purge_queue(QueueUrl=queue_url)
        print("Fila purgada com sucesso!")
    except ClientError as e:
        print(f"Erro ao purgar fila: {e}")

# ==================== EXEMPLOS DE ATRIBUTOS ====================

# Fila com retenção de mensagens longa
LONG_RETENTION_ATTRIBUTES = {
    'MessageRetentionPeriod': '1209600'  # 14 dias em segundos
}

# Fila com entrega atrasada
DELAY_ATTRIBUTES = {
    'DelaySeconds': '30'  # 30 segundos de delay
}

# Fila FIFO (requer nome terminando em .fifo)
FIFO_ATTRIBUTES = {
    'FifoQueue': 'true',
    'ContentBasedDeduplication': 'true'
}

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS SQS:

1. Use Dead Letter Queues para mensagens que falham
2. Configure visibility timeout apropriado para o tempo de processamento
3. Use long polling para reduzir custos e latência
4. Use message attributes para metadados
5. Implemente idempotência no processamento de mensagens
6. Monitore com CloudWatch métricas (NumberOfEmptyReceives, etc)
7. Use filas FIFO para ordenamento estrito
8. Limite o tamanho das mensagens (máximo 256KB)
9. Use batching para enviar/receber múltiplas mensagens
10. Considere SNS para pub/sub e SQS para filas
"""

if __name__ == "__main__":
    print("=== AWS SQS Examples ===\n")
    
    # Listar filas existentes
    print("Filas SQS existentes:")
    list_queues()
    
    # Exemplo de criação de fila
    # queue_url, queue_arn = create_queue("minha-fila")
    
    # Exemplo de envio de mensagem
    # send_message(queue_url, {"message": "Olá SQS!"})
    
    # Exemplo de processamento
    # def process_callback(message):
    #     print("Processando:", message['Body'])
    # process_messages(queue_url, process_callback)
