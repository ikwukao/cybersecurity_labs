#!/usr/bin/env python3
"""
IOC String Extractor for Obfuscated PowerShell
Extracts URLs, IPs, API keys, high-entropy strings
"""

import re
import argparse


def extract_c2_urls(script):
    urls = re.findall(
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        script,
    )
    return urls


def extract_api_keys(script):
    # Common patterns
    patterns = [r"[A-Z0-9\-]{16,}API", r"CANDY-CANE-[A-Z0-9\-]+"]
    keys = []
    for pattern in patterns:
        keys.extend(re.findall(pattern, script))
    return keys


def extract_high_entropy(script):
    # Base64-like high entropy
    entropy_pattern = r"[A-Za-z0-9+/]{40,}"
    return re.findall(entropy_pattern, script)


def main():
    parser = argparse.ArgumentParser(description="Extract IOCs from obfuscated PS")
    parser.add_argument("script_file")
    args = parser.parse_args()

    with open(args.script_file) as f:
        script = f.read()

    print("=== EXTRACTED IOCs ===")
    print("C2 URLs:", extract_c2_urls(script))
    print("API Keys:", extract_api_keys(script))
    print("High Entropy:", extract_high_entropy(script))


if __name__ == "__main__":
    main()
