#!/usr/bin/env python3
# Scan S3 buckets for credentials

import boto3
import re

s3 = boto3.client("s3", endpoint_url="http://localhost:4566")

buckets = s3.list_buckets()["Buckets"]

cred_pattern = re.compile(r"AKIA[0-9A-Z]{16}")

for bucket in buckets:
    name = bucket["Name"]
    try:
        objs = s3.list_objects_v2(Bucket=name)
        for obj in objs.get("Contents", []):
            key = obj["Key"]
            data = s3.get_object(Bucket=name, Key=key)
            content = data["Body"].read().decode()
            if cred_pattern.search(content):
                print(f"[!] CREDENTIALS FOUND in {name}/{key}")
    except:
        pass
