import subprocess
import argparse

parser = argparse.ArgumentParser(description="YARA Rule Validator")
parser.add_argument("rule_file", help="Path to .yar file")
parser.add_argument("sample_dir", help="Directory with test samples")
args = parser.parse_args()

print(f"[*] Compiling {args.rule_file}")
result = subprocess.run(["yarac", args.rule_file, "compiled.yarc"])
if result.returncode != 0:
    print("[-] Syntax error in rule")
    exit(1)

print("[+] Scanning samples...")
matches = subprocess.run(
    ["yara", "compiled.yarc", args.sample_dir], capture_output=True
)
print(matches.stdout.decode())
