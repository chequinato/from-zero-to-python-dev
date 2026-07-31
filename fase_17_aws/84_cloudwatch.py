# AWS CloudWatch - Monitoramento e Observabilidade

"""
CloudWatch é um serviço de monitoramento e observabilidade que fornece
dados e insights operacionais para aplicações e infraestrutura AWS.
"""

import boto3
import time
from datetime import datetime, timedelta
from botocore.exceptions import ClientError

# Inicializar cliente CloudWatch
cloudwatch_client = boto3.client('cloudwatch')
logs_client = boto3.client('logs')

# ==================== MÉTRICAS ====================

def put_metric(namespace, metric_name, value, dimensions=None, unit='Count'):
    """Envia uma métrica customizada para o CloudWatch"""
    try:
        params = {
            'Namespace': namespace,
            'MetricData': [
                {
                    'MetricName': metric_name,
                    'Value': value,
                    'Unit': unit,
                    'Timestamp': datetime.utcnow()
                }
            ]
        }
        
        if dimensions:
            params['MetricData'][0]['Dimensions'] = dimensions
        
        cloudwatch_client.put_metric_data(**params)
        print(f"Métrica {metric_name} enviada com sucesso!")
    except ClientError as e:
        print(f"Erro ao enviar métrica: {e}")

def get_metric_statistics(namespace, metric_name, dimensions=None, period=300, statistic='Average'):
    """Obtém estatísticas de uma métrica"""
    try:
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(hours=1)
        
        params = {
            'Namespace': namespace,
            'MetricName': metric_name,
            'StartTime': start_time,
            'EndTime': end_time,
            'Period': period,
            'Statistics': [statistic]
        }
        
        if dimensions:
            params['Dimensions'] = dimensions
        
        response = cloudwatch_client.get_metric_statistics(**params)
        datapoints = response['Datapoints']
        
        print(f"Estatísticas de {metric_name}:")
        for dp in sorted(datapoints, key=lambda x: x['Timestamp']):
            print(f"  {dp['Timestamp']}: {dp[statistic]} {dp['Unit']}")
        
        return datapoints
    except ClientError as e:
        print(f"Erro ao obter estatísticas: {e}")

# ==================== ALARMES ====================

def create_alarm(alarm_name, metric_name, namespace, threshold, comparison_operator, 
                 dimensions=None, evaluation_periods=1, period=300):
    """Cria um alarme do CloudWatch"""
    try:
        params = {
            'AlarmName': alarm_name,
            'AlarmDescription': f'Alarme para {metric_name}',
            'ActionsEnabled': True,
            'OKActions': [],  # ARNs para ações quando estado é OK
            'AlarmActions': [],  # ARNs para ações quando alarme dispara
            'InsufficientDataActions': [],
            'MetricName': metric_name,
            'Namespace': namespace,
            'Statistic': 'Average',
            'Period': period,
            'EvaluationPeriods': evaluation_periods,
            'Threshold': threshold,
            'ComparisonOperator': comparison_operator
        }
        
        if dimensions:
            params['Dimensions'] = dimensions
        
        cloudwatch_client.put_metric_alarm(**params)
        print(f"Alarme {alarm_name} criado com sucesso!")
    except ClientError as e:
        print(f"Erro ao criar alarme: {e}")

def list_alarms():
    """Lista todos os alarmes"""
    try:
        response = cloudwatch_client.describe_alarms()
        alarms = response['MetricAlarms']
        print(f"Total de alarmes: {len(alarms)}")
        for alarm in alarms:
            print(f"- {alarm['AlarmName']} ({alarm['StateValue']})")
        return alarms
    except ClientError as e:
        print(f"Erro ao listar alarmes: {e}")

def delete_alarm(alarm_name):
    """Deleta um alarme"""
    try:
        cloudwatch_client.delete_alarms(AlarmNames=[alarm_name])
        print(f"Alarme {alarm_name} deletado!")
    except ClientError as e:
        print(f"Erro ao deletar alarme: {e}")

# ==================== LOGS ====================

def create_log_group(log_group_name):
    """Cria um grupo de logs"""
    try:
        logs_client.create_log_group(logGroupName=log_group_name)
        print(f"Grupo de logs {log_group_name} criado!")
    except ClientError as e:
        print(f"Erro ao criar grupo de logs: {e}")

def put_log_event(log_group_name, log_stream_name, message):
    """Envia um evento de log para o CloudWatch Logs"""
    try:
        # Cria o stream se não existir
        try:
            logs_client.create_log_stream(
                logGroupName=log_group_name,
                logStreamName=log_stream_name
            )
        except logs_client.exceptions.ResourceAlreadyExistsException:
            pass
        
        logs_client.put_log_events(
            logGroupName=log_group_name,
            logStreamName=log_stream_name,
            logEvents=[
                {
                    'timestamp': int(time.time() * 1000),
                    'message': message
                }
            ]
        )
        print(f"Log enviado para {log_stream_name}")
    except ClientError as e:
        print(f"Erro ao enviar log: {e}")

def get_log_events(log_group_name, log_stream_name, limit=50):
    """Obtém eventos de log de um stream"""
    try:
        response = logs_client.get_log_events(
            logGroupName=log_group_name,
            logStreamName=log_stream_name,
            limit=limit
        )
        
        events = response['events']
        print(f"Eventos de log de {log_stream_name}:")
        for event in events:
            timestamp = event['timestamp']
            message = event['message']
            print(f"[{timestamp}] {message}")
        
        return events
    except ClientError as e:
        print(f"Erro ao obter eventos de log: {e}")

def set_retention_policy(log_group_name, days):
    """Define a política de retenção de logs"""
    try:
        logs_client.put_retention_policy(
            logGroupName=log_group_name,
            retentionInDays=days
        )
        print(f"Política de retenção definida para {days} dias")
    except ClientError as e:
        print(f"Erro ao definir política de retenção: {e}")

# ==================== DASHBOARDS ====================

def create_dashboard(dashboard_name, widgets):
    """Cria um dashboard do CloudWatch"""
    try:
        dashboard_body = json.dumps({'widgets': widgets})
        
        cloudwatch_client.put_dashboard(
            DashboardName=dashboard_name,
            DashboardBody=dashboard_body
        )
        
        print(f"Dashboard {dashboard_name} criado!")
    except ClientError as e:
        print(f"Erro ao criar dashboard: {e}")

# ==================== EVENTOS ====================

def put_rule(rule_name, schedule_expression, event_pattern=None):
    """Cria uma regra do CloudWatch Events"""
    try:
        events_client = boto3.client('events')
        
        params = {
            'Name': rule_name,
            'ScheduleExpression': schedule_expression
        }
        
        if event_pattern:
            params['EventPattern'] = json.dumps(event_pattern)
        
        events_client.put_rule(**params)
        print(f"Regra {rule_name} criada!")
    except ClientError as e:
        print(f"Erro ao criar regra: {e}")

# ==================== EXEMPLOS DE MÉTRICAS ====================

# Exemplo de dimensões para métricas EC2
EC2_DIMENSIONS = [
    {'Name': 'InstanceId', 'Value': 'i-1234567890abcdef0'}
]

# Exemplo de dimensões para métricas Lambda
LAMBDA_DIMENSIONS = [
    {'Name': 'FunctionName', 'Value': 'minha-funcao-lambda'}
]

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS CLOUDWATCH:

1. Use namespaces consistentes para métricas customizadas
2. Configure alarmes para métricas críticas
3. Use dimensões para filtrar e agrupar métricas
4. Configure retenção de logs para controlar custos
5. Use Insights para análise de logs complexos
6. Crie dashboards para visualização em tempo real
7. Use metric filters para extrair métricas de logs
8. Configure notificações SNS para alarmes
9. Use X-Ray para rastreamento distribuído
10. Monitore custos com métricas de Billing
"""

if __name__ == "__main__":
    print("=== AWS CloudWatch Examples ===\n")
    
    # Listar alarmes existentes
    print("Alarmes existentes:")
    list_alarms()
    
    # Exemplo de envio de métrica
    # put_metric("MeuNamespace", "MinhaMetrica", 42, unit='Count')
    
    # Exemplo de criação de alarme
    # create_alarm("CPU-Alto", "CPUUtilization", "AWS/EC2", 80, "GreaterThanThreshold")
