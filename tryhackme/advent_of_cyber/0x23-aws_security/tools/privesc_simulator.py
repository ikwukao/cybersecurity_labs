#!/usr/bin/env python3
# Simulate IAM privilege escalation paths



def find_escalation_paths():
    print("[*] Simulating privilege escalation paths...")
    print("1. junior-dev → AssumeRole → vuln-role → AdministratorAccess")
    print("2. EC2 instance role → S3 access → leaked keys")
    print("3. Lambda execution role → over-privileged")
    print("[+] Multiple escalation paths available")


find_escalation_paths()
