import re
from collections import defaultdict
from datetime import datetime

def parse_logs(file_path="auth_log.txt"):
    """
    Parse the auth_log.txt file for failed SSH login attempts.
    Returns a dictionary: {IP: [(timestamp: datetime, username, invalid_flag), ...]}
    """
    attempts = defaultdict(list)
    
    # Matches lines like: Jul 01 04:36:15 ... Failed password for invalid user baituser from 192.168.0.5 ...
    pattern = r"^(\w+ \d+ \d+:\d+:\d+).*Failed password for (invalid user )?([^\s]+) from ([\d.:a-fA-F]+)"

    try:
        with open(file_path, "r") as file:
            logs = file.readlines()

        for line in logs:
            match = re.search(pattern, line)
            if match:
                raw_timestamp = match.group(1)              # e.g., 'Jul 01 04:36:15'
                is_invalid = bool(match.group(2))           # 'invalid user' present
                username = match.group(3)
                ip = match.group(4)

                try:
                    # Add the current year manually to create a full timestamp
                    current_year = datetime.now().year
                    full_timestamp_str = f"{raw_timestamp} {current_year}"
                    timestamp = datetime.strptime(full_timestamp_str, "%b %d %H:%M:%S %Y")
                except ValueError:
                    print(f"⚠️ Failed to parse timestamp: {raw_timestamp}")
                    continue

                attempts[ip].append((timestamp, username, is_invalid))

    except FileNotFoundError:
        print(f"❌ Log file '{file_path}' not found.")

    return attempts
