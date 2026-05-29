import re


def scan_dockerfile(file_path):
    with open(file_path, "r") as f:
        content = f.read()
    if re.search(r"VOLUME /var/run/docker.sock", content):
        print("⚠️ Vuln: Socket mount detected!")
    # Add more checks (e.g., USER root)


if __name__ == "__main__":
    import sys

    scan_dockerfile(sys.argv[1])
