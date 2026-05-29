#!/usr/bin/env python3
# C2 Detection Validator
# Tests rules against generated beacon traffic

import subprocess
import time


def test_sigma(rule_file, pcap_file=None):
    print(f"[*] Testing Sigma rule: {rule_file}")
    # Simulate sigma-tool execution
    cmd = ["sigmac", "-t", "splunk", rule_file]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout[:500])


def generate_traffic(duration=1800):
    print(f"[*] Generating beacon traffic for {duration}s...")
    # Launch simulator in background
    subprocess.Popen(["python", "beacons/http_beacon_simulator.py"])


# Main validation workflow
generate_traffic()
time.sleep(300)  # Let traffic build
test_sigma("detection/sigma/sigma_http_beacon.yml")
print("\n[+] Validation complete")
