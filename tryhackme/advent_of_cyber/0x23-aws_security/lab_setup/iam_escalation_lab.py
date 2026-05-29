# Simulate IAM escalation scenario
import boto3

iam = boto3.client("iam", endpoint_url="http://localhost:4566")

# Create low-priv user that can assume high-priv role
iam.create_user(UserName="junior-dev")
iam.attach_user_policy(
    UserName="junior-dev", PolicyArn="arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
)

# Allow junior-dev to assume vuln-role
policy_doc = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "arn:aws:iam::123456789012:role/vuln-role",
        }
    ],
}
iam.put_user_policy(
    UserName="junior-dev",
    PolicyName="AssumeVulnRole",
    PolicyDocument=json.dumps(policy_doc),
)

print("[+] IAM privilege escalation lab ready")
