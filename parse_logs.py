import re
from collections import defaultdict

def parse_logs(file_path="auth_log.txt"):
    """
    Parse the auth_log.txt file for failed SSH login attempts.
    Returns a dictionary: {IP: [(timestamp, username, invalid_flag), ...]}
    """
    attempts = defaultdict(list)
    # Handles both valid and invalid users
    pattern = r"^(\w+ \d+ \d+:\d+:\d+).*Failed password for (invalid user )?([^\s]+) from ([\d.:a-fA-F]+)"

    try:
        with open(file_path, "r") as file:
            logs = file.readlines()

        for line in logs:
            match = re.search(pattern, line)
            if match:
                timestamp = match.group(1)
                is_invalid = bool(match.group(2))  # "invalid user " is present
                username = match.group(3)
                ip = match.group(4)
                attempts[ip].append((timestamp, username, is_invalid))
    except FileNotFoundError:
        print(f"❌ Log file '{file_path}' not found.")

    return attempts
