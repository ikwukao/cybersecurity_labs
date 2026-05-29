#!/usr/bin/env python3
"""
PowerShell Deobfuscator - Professional Tool for Red Team Analysis
Handles: Concatenation, Base64, XOR hex arrays, variable substitution
Author: [Your Name] | Date: 2026-01-01
"""

import re
import base64
import argparse


def deobfuscate_concatenation(script):
    """Resolve string concatenation"""
    script = re.sub(
        r'\$([a-z0-9]+)\s*=\s*[\'"]([^\'"]+)[\'"]\s*\+\s*[\'"]([^\'"]+)[\'"]',
        r'"\2\3"',
        script,
    )
    return script


def decode_base64_strings(script):
    """Decode embedded Base64"""
    b64_pattern = r"[A-Za-z0-9+/]{20,}=?"
    matches = re.findall(b64_pattern, script)
    for match in matches:
        try:
            decoded = base64.b64decode(match).decode("utf-8", errors="ignore")
            script = script.replace(match, f'"{decoded}"')
        except:
            pass
    return script


def resolve_xor_hex(script, xor_key=0x37):
    """Deobfuscate XOR hex arrays"""
    hex_pattern = r"0x([0-9a-fA-F]{2})(?:\s*,0x([0-9a-fA-F]{2}))*"
    matches = re.finditer(hex_pattern, script)
    for match in matches:
        hex_bytes = [int(h, 16) for h in match.groups() if h]
        deobf = "".join(chr(b ^ xor_key) for b in hex_bytes)
        script = script.replace(match.group(), f'"{deobf}"')
    return script


def main():
    parser = argparse.ArgumentParser(description="PowerShell Deobfuscator")
    parser.add_argument("input_file", help="Obfuscated .ps1 file")
    parser.add_argument("-o", "--output", help="Output deobfuscated file")
    args = parser.parse_args()

    with open(args.input_file, "r") as f:
        script = f.read()

    # Apply deobfuscation layers
    script = deobfuscate_concatenation(script)
    script = decode_base64_strings(script)
    script = resolve_xor_hex(script)

    output_file = args.output or args.input_file.replace(".ps1", "_deobf.ps1")
    with open(output_file, "w") as f:
        f.write(script)

    print(f"[+] Deobfuscated script saved: {output_file}")


if __name__ == "__main__":
    main()
