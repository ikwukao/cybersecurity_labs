import requests


# CSP Analyzer & Bypass Suggester
def analyze_csp(url):
    resp = requests.get(url)
    csp = resp.headers.get("Content-Security-Policy")
    if not csp:
        print("[-] No CSP - Easy bypass!")
        return
    print(f"[i] CSP: {csp}")
    # Suggest bypasses
    if "'unsafe-inline'" in csp:
        print("[+] Unsafe-inline: Inject inline <script>alert(1)</script>")
    if "script-src 'self'" in csp:
        print("[+] Self only: Upload malicious JS to same domain")
    # Add more logic for nonce, hash, etc.


if __name__ == "__main__":
    import sys

    analyze_csp(sys.argv[1])
