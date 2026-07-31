# AWS IAM (Identity and Access Management) - Gerenciamento de Identidade e Acesso

"""
IAM é o serviço da AWS que gerencia quem pode fazer o quê na sua conta AWS.
É fundamental para a segurança de qualquer infraestrutura na nuvem.
"""

import boto3
from botocore.exceptions import ClientError

# Inicializar cliente IAM
iam_client = boto3.client('iam')

# ==================== USUÁRIOS ====================

def create_user(username):
    """Cria um novo usuário IAM"""
    try:
        response = iam_client.create_user(UserName=username)
        print(f"Usuário {username} criado com sucesso!")
        return response['User']
    except ClientError as e:
        print(f"Erro ao criar usuário: {e}")

def list_users():
    """Lista todos os usuários IAM"""
    try:
        response = iam_client.list_users()
        users = response['Users']
        print(f"Total de usuários: {len(users)}")
        for user in users:
            print(f"- {user['UserName']} (Criado em: {user['CreateDate']})")
        return users
    except ClientError as e:
        print(f"Erro ao listar usuários: {e}")

def delete_user(username):
    """Deleta um usuário IAM"""
    try:
        # Primeiro remove todas as chaves de acesso
        access_keys = iam_client.list_access_keys(UserName=username)
        for key in access_keys['AccessKeyMetadata']:
            iam_client.delete_access_key(
                UserName=username,
                AccessKeyId=key['AccessKeyId']
            )
        
        # Remove todas as políticas do usuário
        attached_policies = iam_client.list_attached_user_policies(UserName=username)
        for policy in attached_policies['AttachedPolicies']:
            iam_client.detach_user_policy(
                UserName=username,
                PolicyArn=policy['PolicyArn']
            )
        
        # Remove todas as políticas inline
        inline_policies = iam_client.list_user_policies(UserName=username)
        for policy_name in inline_policies['PolicyNames']:
            iam_client.delete_user_policy(
                UserName=username,
                PolicyName=policy_name
            )
        
        # Remove de todos os grupos
        groups = iam_client.list_groups_for_user(UserName=username)
        for group in groups['Groups']:
            iam_client.remove_user_from_group(
                GroupName=group['GroupName'],
                UserName=username
            )
        
        # Finalmente deleta o usuário
        iam_client.delete_user(UserName=username)
        print(f"Usuário {username} deletado com sucesso!")
    except ClientError as e:
        print(f"Erro ao deletar usuário: {e}")

# ==================== GRUPOS ====================

def create_group(group_name):
    """Cria um novo grupo IAM"""
    try:
        response = iam_client.create_group(GroupName=group_name)
        print(f"Grupo {group_name} criado com sucesso!")
        return response['Group']
    except ClientError as e:
        print(f"Erro ao criar grupo: {e}")

def add_user_to_group(group_name, username):
    """Adiciona um usuário a um grupo"""
    try:
        iam_client.add_user_to_group(
            GroupName=group_name,
            UserName=username
        )
        print(f"Usuário {username} adicionado ao grupo {group_name}")
    except ClientError as e:
        print(f"Erro ao adicionar usuário ao grupo: {e}")

def attach_policy_to_group(group_name, policy_arn):
    """Anexa uma política a um grupo"""
    try:
        iam_client.attach_group_policy(
            GroupName=group_name,
            PolicyArn=policy_arn
        )
        print(f"Política anexada ao grupo {group_name}")
    except ClientError as e:
        print(f"Erro ao anexar política: {e}")

# ==================== POLÍTICAS ====================

def create_policy(policy_name, policy_document):
    """Cria uma política IAM gerenciada"""
    try:
        response = iam_client.create_policy(
            PolicyName=policy_name,
            PolicyDocument=policy_document
        )
        print(f"Política {policy_name} criada com sucesso!")
        return response['Policy']
    except ClientError as e:
        print(f"Erro ao criar política: {e}")

def list_policies():
    """Lista todas as políticas gerenciadas"""
    try:
        response = iam_client.list_policies(Scope='Local')
        policies = response['Policies']
        print(f"Total de políticas: {len(policies)}")
        for policy in policies:
            print(f"- {policy['PolicyName']} ({policy['Arn']})")
        return policies
    except ClientError as e:
        print(f"Erro ao listar políticas: {e}")

# ==================== ROLES ====================

def create_role(role_name, trust_policy):
    """Cria uma nova role IAM"""
    try:
        response = iam_client.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=trust_policy
        )
        print(f"Role {role_name} criada com sucesso!")
        return response['Role']
    except ClientError as e:
        print(f"Erro ao criar role: {e}")

def attach_policy_to_role(role_name, policy_arn):
    """Anexa uma política a uma role"""
    try:
        iam_client.attach_role_policy(
            RoleName=role_name,
            PolicyArn=policy_arn
        )
        print(f"Política anexada à role {role_name}")
    except ClientError as e:
        print(f"Erro ao anexar política: {e}")

# ==================== CHAVES DE ACESSO ====================

def create_access_key(username):
    """Cria chaves de acesso para um usuário"""
    try:
        response = iam_client.create_access_key(UserName=username)
        access_key = response['AccessKey']
        print(f"Chaves de acesso criadas para {username}")
        print(f"Access Key ID: {access_key['AccessKeyId']}")
        print(f"Secret Access Key: {access_key['SecretAccessKey']}")
        print("⚠️  Salve estas chaves agora, pois não serão mostradas novamente!")
        return access_key
    except ClientError as e:
        print(f"Erro ao criar chaves de acesso: {e}")

# ==================== EXEMPLOS DE POLÍTICAS ====================

# Política de confiança para EC2 assumir uma role
EC2_TRUST_POLICY = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

# Política para acesso total ao S3
S3_FULL_ACCESS_POLICY = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "*"
        }
    ]
}

# Política para acesso leitura a um bucket específico
S3_READ_ONLY_POLICY = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:Get*",
                "s3:List*"
            ],
            "Resource": [
                "arn:aws:s3:::meu-bucket",
                "arn:aws:s3:::meu-bucket/*"
            ]
        }
    ]
}

# ==================== MELHORES PRÁTICAS ====================

"""
MELHORES PRÁTICAS IAM:

1. Princípio do menor privilégio: Dê apenas as permissões necessárias
2. Use grupos em vez de atribuir políticas diretamente a usuários
3. Use MFA (Multi-Factor Authentication) sempre que possível
4. Roteie chaves de acesso para usuários, não para roles
5. Use roles para aplicações em vez de credenciais hardcoded
6. Gire regularmente as credenciais
7. Revogue acesso quando não for mais necessário
8. Use AWS Organizations para gerenciar múltiplas contas
9. Monitore com AWS CloudTrail e AWS Config
10. Use AWS IAM Access Analyzer para identificar recursos compartilhados
"""

if __name__ == "__main__":
    # Exemplo de uso
    print("=== AWS IAM Examples ===\n")
    
    # Listar usuários existentes
    print("Usuários existentes:")
    list_users()
    
    # Criar um grupo de desenvolvedores
    # create_group("Developers")
    
    # Anexar política de leitura S3 ao grupo
    # S3_READ_ONLY_ARN = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
    # attach_policy_to_group("Developers", S3_READ_ONLY_ARN)
