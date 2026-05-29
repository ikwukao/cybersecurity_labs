import email


def analyze_headers(raw_email):
    msg = email.message_from_string(raw_email)
    print("From:", msg["From"])
    print("Return-Path:", msg["Return-Path"])
    print("DKIM:", msg["DKIM-Signature"])
    print("SPF:", msg.get("Received-SPF"))
    # Detect spoofing
    if "tbfc.com" in msg["From"] and "tbfc.com" not in msg["Return-Path"]:
        print("⚠️  POSSIBLE SPOOFING")


# Usage: paste raw email headers
