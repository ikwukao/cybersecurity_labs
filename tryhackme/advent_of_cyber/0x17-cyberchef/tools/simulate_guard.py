import argparse
import base64


# Simulate AI Guard Response
def simulate_response(lock, magic):
    passwords = {
        1: "Iamsofluffy",
        2: "Itoldyoutochangeit!",
        3: "BugsBunny",
        4: "passw0rd1",
        5: "51rBr34chBl0ck3r",
    }
    pwd = passwords.get(lock, "Unknown")
    if lock == 1:
        return base64.b64encode(pwd.encode()).decode()
    # Add more simulations for each lock
    return "Simulated obfuscated response"


parser = argparse.ArgumentParser(description="Simulate Guard")
parser.add_argument("--lock", type=int, required=True)
parser.add_argument("--magic", required=True)
args = parser.parse_args()
print(simulate_response(args.lock, args.magic))
