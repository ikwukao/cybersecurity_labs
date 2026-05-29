#!/usr/bin/env python3
import boto3


def recon_services(endpoint="http://localhost:4566"):
    s3 = boto3.client("s3", endpoint_url=endpoint)
    try:
        buckets = [b["Name"] for b in s3.list_buckets()["Buckets"]]
        print("S3 Buckets:")
        for b in buckets:
            print(f"  - {b}")
    except:
        print("S3 access denied")

    iam = boto3.client("iam", endpoint_url=endpoint)
    try:
        roles = [r["RoleName"] for r in iam.list_roles()["Roles"]]
        print("\nIAM Roles:")
        for r in roles:
            print(f"  - {r}")
    except:
        print("\nIAM access denied")


recon_services()
