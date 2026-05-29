import re
import sys


def extract_iocs(log_file):
    ips = set()
    cmds = []
    with open(log_file) as f:
        for line in f:
            ip = re.search(r"\d+\.\d+\.\d+\.\d+", line)
            if ip:
                ips.add(ip.group())
            cmd = re.search(r"(;|&&|\||\$\()", line)
            if cmd:
                cmds.append(line.strip())
    print("Suspicious IPs:", ips)
    print("Injection Attempts:", cmds)


if __name__ == "__main__":
    extract_iocs(sys.argv[1])
