#!/usr/bin/env python3
# Simple CloudTrail Log Anomaly Detector

import json
import sys
from collections import Counter


def analyze_events(log_file):
    suspicious = []
    event_counts = Counter()

    with open(log_file) as f:
        for line in f:
            event = json.loads(line)
            name = event.get("eventName", "")
            event_counts[name] += 1

            if name in ["DeleteTrail", "StopLogging", "DeleteBucket"]:
                suspicious.append(event)

    print("Top Events:")
    for event, count in event_counts.most_common(10):
        print(f"  {event}: {count}")

    if suspicious:
        print("\n[!] Suspicious Events Detected:")
        for s in suspicious:
            print(
                f"    {s['eventName']} by {s.get('userIdentity', {}).get('userName')}"
            )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cloudtrail_analyzer.py <cloudtrail_log.json>")
        sys.exit(1)
    analyze_events(sys.argv[1])
