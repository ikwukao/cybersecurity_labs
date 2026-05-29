import csv

# Simple CSV timeline builder from multiple logs
# Demo with parsed data
timeline = [
    {"time": "2025-12-15 10:00", "event": "Command Injection Attempt"},
    {"time": "2025-12-15 10:01", "event": "whoami.exe executed"},
    {"time": "2025-12-15 10:02", "event": "PowerShell download attempt"},
]

with open("timeline.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["time", "event"])
    writer.writeheader()
    writer.writerows(timeline)
print("[+] Timeline generated: timeline.csv")
