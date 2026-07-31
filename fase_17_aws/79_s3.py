# AWS S3 (Simple Storage Service) - Armazenamento de Objetos

"""
S3 é um serviço de armazenamento de objetos que oferece escalabilidade,
disponibilidade de dados, segurança e performance.
"""

import boto3
from botocore.exceptions import ClientError

# Inicializar cliente S3
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

# ==================== BUCKETS ====================

def create_bucket(bucket_name, region=None):
    """Cria um novo bucket S3"""
    try:
        if region:
            location = {'LocationConstraint': region}
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration=location
            )
        else:
            s3_client.create_bucket(Bucket=bucket_name)
        
        print(f"Bucket {bucket_name} criado com sucesso!")
    except ClientError as e:
        print(f"Erro ao criar bucket: {e}")

def list_buckets():
    """Lista todos os buckets S3"""
    try:
        response = s3_client.list_buckets()
        buckets = response['Buckets']
        print(f"Total de buckets: {len(buckets)}")
        for bucket in buckets:
            print(f"- {bucket['Name']} (Criado em: {bucket['CreationDate']})")
        return buckets
    except ClientError as e:
        print(f"Erro ao listar buckets: {e}")

def delete_bucket(bucket_name):
    """Deleta um bucket S3 (deve estar vazio)"""
    try:
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} deletado com sucesso!")
    except ClientError as e:
        print(f"Erro ao deletar bucket: {e}")

def empty_bucket(bucket_name):
    """Esvazia um bucket deletando todos os objetos"""
    try:
        bucket = s3_resource.Bucket(bucket_name)
        bucket.objects.all().delete()
        print(f"Bucket {bucket_name} esvaziado com sucesso!")
    except ClientError as e:
        print(f"Erro ao esvaziar bucket: {e}")

# ==================== OBJETOS ====================

def upload_file(bucket_name, file_path, object_name=None):
    """Faz upload de um arquivo para o S3"""
    try:
        if object_name is None:
            object_name = file_path.split('/')[-1]
        
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"Arquivo {file_path} enviado para {bucket_name}/{object_name}")
    except ClientError as e:
        print(f"Erro ao fazer upload: {e}")

def download_file(bucket_name, object_name, file_path):
    """Faz download de um arquivo do S3"""
    try:
        s3_client.download_file(bucket_name, object_name, file_path)
        print(f"Arquivo {object_name} baixado para {file_path}")
    except ClientError as e:
        print(f"Erro ao fazer download: {e}")

def list_objects(bucket_name, prefix=''):
    """Lista objetos em um bucket"""
    try:
        response = s3_client.list_objects_v2(
            Bucket=bucket_name,
            Prefix=prefix
        )
        
        if 'Contents' in response:
            objects = response['Contents']
            print(f"Total de objetos: {len(objects)}")
            for obj in objects:
                print(f"- {obj['Key']} ({obj['Size']} bytes)")
            return objects
        else:
            print("Bucket vazio")
            return []
    except ClientError as e:
        print(f"Erro ao listar objetos: {e}")

def delete_object(bucket_name, object_name):
    """Deleta um objeto do S3"""
    try:
        s3_client.delete_object(Bucket=bucket_name, Key=object_name)
        print(f"Objeto {object_name} deletado de {bucket_name}")
    except ClientError as e:
        print(f"Erro ao deletar objeto: {e}")

def copy_object(source_bucket, source_key, dest_bucket, dest_key):
    """Copia um objeto entre buckets"""
    try:
        copy_source = {'Bucket': source_bucket, 'Key': source_key}
        s3_client.copy_object(
            CopySource=copy_source,
            Bucket=dest_bucket,
            Key=dest_key
        )
        print(f"Objeto copiado de {source_bucket}/{source_key} para {dest_bucket}/{dest_key}")
    except ClientError as e:
        print(f"Erro ao copiar objeto: {e}")

# ==================== METADADOS E INFO ====================

def get_object_metadata(bucket_name, object_name):
    """Obtém metadados de um objeto"""
    try:
        response = s3_client.head_object(Bucket=bucket_name, Key=object_name)
        metadata = {
            'ContentType': response.get('ContentType'),
            'ContentLength': response.get('ContentLength'),
            'LastModified': response.get('LastModified'),
            'ETag': response.get('ETag'),
            'Metadata': response.get('Metadata', {})
        }
        print(f"Metadados de {object_name}:")
        for key, value in metadata.items():
            print(f"  {key}: {value}")
        return metadata
    except ClientError as e:
        print(f"Erro ao obter metadados: {e}")

def generate_presigned_url(bucket_name, object_name, expiration=3600):
    """Gera uma URL presigned para acesso temporário"""
    try:
        url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=expiration
        )
        print(f"URL presigned gerada (expira em {expiration}s):")
        print(url)
        return url
    except ClientError as e:
        print(f"Erro ao gerar URL presigned: {e}")

# ==================== VERSIONAMENTO ====================

def enable_versioning(bucket_name):
    """Habilita versionamento em um bucket"""
    try:
        s3_client.put_bucket_versioning(
            Bucket=bucket_name,
            VersioningConfiguration={'Status': 'Enabled'}
        )
        print(f"Versionamento habilitado para {bucket_name}")
    except ClientError as e:
        print(f"Erro ao habilitar versionamento: {e}")

def get_object_versions(bucket_name, object_name):
    """Lista todas as versões de um objeto"""
    try:
        response = s3_client.list_object_versions(Bucket=bucket_name, Prefix=object_name)
        if 'Versions' in response:
            versions = response['Versions']
            print(f"Versões de {object_name}:")
            for version in versions:
                print(f"  VersionId: {version['VersionId']}, LastModified: {version['LastModified']}")
            return versions
    except ClientError as e:
        print(f"Erro ao listar versões: {e}")

# ==================== ENCRYPTATION ====================

def enable_encryption(bucket_name):
    """Habilita criptografia padrão em um bucket"""
    try:
        s3_client.put_bucket_encryption(
            Bucket=bucket_name,
            ServerSideEncryptionConfiguration={
                'Rules': [
                    {
                        'ApplyServerSideEncryptionByDefault': {
                            'SSEAlgorithm': 'AES256'
                        }
                    }
                ]
            }
        )
        print(f"Criptografia habilitada para {bucket_name}")
    except ClientError as e:
        print(f"Erro ao habilitar criptografia: {e}")

# ==================== LIFECYCLE ====================

def set_lifecycle_rule(bucket_name, rule_id, prefix, days):
    """Configura regra de lifecycle para objetos"""
    try:
        s3_client.put_bucket_lifecycle_configuration(
            Bucket=bucket_name,
            LifecycleConfiguration={
                'Rules': [
                    {
                        'ID': rule_id,
                        'Prefix': prefix,
                        'Status': 'Enabled',
                        'Expiration': {'Days': days}
                    }
                ]
            }
        )
        print(f"Regra de lifecycle configurada para {bucket_name}")
    except ClientError as e:
        print(f"Erro ao configurar lifecycle: {e}")

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS S3:

1. Use buckets privados por padrão
2. Habilite versionamento para buckets importantes
3. Use criptografia em repouso (SSE-S3, SSE-KMS, SSE-C)
4. Use políticas de bucket para controle de acesso granular
5. Configure lifecycle rules para gerenciar custos
6. Use CloudFront para distribuição de conteúdo estático
7. Monitore com S3 Event Notifications e CloudWatch
8. Use presigned URLs para acesso temporário
9. Implemente MFA Delete para buckets críticos
10. Use S3 Cross-Region Replication para redundância
"""

if __name__ == "__main__":
    print("=== AWS S3 Examples ===\n")
    
    # Listar buckets existentes
    print("Buckets S3 existentes:")
    list_buckets()
    
    # Exemplo de upload (requer arquivo existente)
    # upload_file("meu-bucket", "arquivo.txt")
    
    # Exemplo de download
    # download_file("meu-bucket", "arquivo.txt", "download.txt")
