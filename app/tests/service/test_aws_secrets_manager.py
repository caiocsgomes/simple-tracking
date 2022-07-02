import os

import boto3
from moto import mock_secretsmanager

from src.service.aws_secrets_manager import SecretsManagerService


class TestSecretsManagerService:
    secrets_manager_service: SecretsManagerService

    @classmethod
    def setup_class(cls):
        cls.secrets_manager_service = SecretsManagerService()
        os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
        os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
        os.environ['AWS_SECURITY_TOKEN'] = 'testing'
        os.environ['AWS_SESSION_TOKEN'] = 'testing'
        os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

    @mock_secretsmanager
    def test_get_secret_with_moto(self, app):
        conn = boto3.client("secretsmanager", region_name="us-east-1")
        conn.create_secret(Name="test-secret", SecretString="test-password")
        response = self.secrets_manager_service.get_secret("test-secret")
        assert response == "test-password"
