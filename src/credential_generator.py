import os
import random
import string

class DecoyCredentialGenerator:
    def __init__(self, listener_url: str):
        self.listener_url = listener_url

    def _rand_str(self, length: int) -> str:
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    def generate_aws_credentials(self, output_path: str) -> dict:
        access_key = f"AKIA{self._rand_str(16)}"
        secret_key = self._rand_str(40)
        
        content = f"""[default]
aws_access_key_id = {access_key}
aws_secret_access_key = {secret_key}
region = us-east-1

[production-db-admin]
aws_access_key_id = AKIA{self._rand_str(16)}
aws_secret_access_key = {self._rand_str(40)}
region = us-west-2
"""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            f.write(content)

        return {"type": "AWS Credentials", "access_key": access_key, "file": output_path}

    def generate_env_file(self, output_path: str) -> dict:
        token_id = self._rand_str(12)
        content = f"""# Production Environment Variables & Database Secrets
DB_HOST=10.240.12.50
DB_USER=canary_admin
DB_PASS=Secur3P@ss_2026_{token_id}
STRIPE_SECRET_KEY=sk_live_{self._rand_str(24)}
CANARY_CALLBACK_URL={self.listener_url}/canary/env_token_{token_id}
"""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            f.write(content)

        return {"type": ".env Configuration", "token_id": token_id, "file": output_path}
