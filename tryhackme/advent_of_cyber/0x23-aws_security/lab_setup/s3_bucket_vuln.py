# Simulate vulnerable S3 bucket with sensitive data
import boto3

s3 = boto3.client("s3", endpoint_url="http://localhost:4566")

s3.put_object(
    Bucket="toy-factory-secrets",
    Key="internal/config.json",
    Body='{"db_password": "SuperSecret123!", "api_key": "AKIAFAKEKEY1234567890"}',
)
print("[+] Sensitive config uploaded to public bucket")
