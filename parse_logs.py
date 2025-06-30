import re
from collections import defaultdict

def parse_logs(file_path="auth_log.txt"):
    """
    Parse the auth_log.txt file for failed SSH login attempts.
    Returns a dictionary: {IP: [(timestamp, username), ...]}
    """
    attempts = defaultdict(list)
    pattern = r"^(\w+ \d+ \d+:\d+:\d+).*Failed password for (\w+) from ([\d.:a-fA-F]+)"

    try:
        with open(file_path, "r") as file:
            logs = file.readlines()

        for line in logs:
            match = re.search(pattern, line)
            if match:
                timestamp, username, ip = match.groups()
                attempts[ip].append((timestamp, username))
    except FileNotFoundError:
        print(f"❌ Log file '{file_path}' not found.")

    return attempts