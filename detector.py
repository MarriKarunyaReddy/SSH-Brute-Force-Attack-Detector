import os
import re
import sys
import subprocess
from collections import defaultdict

# Step 1: Get minutes from command line or default to 15
try:
    minutes = int(sys.argv[1]) if len(sys.argv) > 1 else 15
except ValueError:
    print("❌ Invalid input. Use an integer for minutes.")
    exit(1)

print(f"📥 Fetching SSH logs from the last {minutes} minute(s)...")

# Step 2: Auto-fetch latest SSH logs
try:
    subprocess.run(
        ["sudo", "journalctl", "-u", "ssh", f"--since={minutes} minutes ago"],
        stdout=open("auth_log.txt", "w"),
        stderr=subprocess.DEVNULL,
        check=True
    )
except subprocess.CalledProcessError:
    print("❌ Failed to fetch logs. Are you running this on Kali with sudo access?")
    exit(1)

# Step 3: Analyze logs
attempts = defaultdict(list)
pattern = r"^(\w+ \d+ \d+:\d+:\d+).*Failed password for (\w+) from ([\d.:a-fA-F]+)"

with open("auth_log.txt", "r") as file:
    logs = file.readlines()

for line in logs:
    match = re.search(pattern, line)
    if match:
        timestamp, username, ip = match.groups()
        attempts[ip].append((timestamp, username))

# Step 4: Display
if not attempts:
    print("✅ No failed login attempts found.")
else:
    print("🚨 Failed Login Attempts Report:\n")
    for ip, records in attempts.items():
        print(f"[{ip}] — {len(records)} attempt(s)")
        for timestamp, user in records:
            print(f"   └─ {timestamp} → user: {user}")
        print()
