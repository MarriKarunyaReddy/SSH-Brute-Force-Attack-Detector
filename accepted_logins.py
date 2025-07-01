import re
from collections import defaultdict

def parse_accepted_logins(file_path="auth_log.txt"):
    """
    Parses log file for successful SSH logins.
    Returns a dictionary: {IP: [(timestamp, username), ...]}
    """
    accepted = defaultdict(list)
    # Matches both password and publickey accepted logins
    pattern = r"^(\w+ \d+ \d+:\d+:\d+).*Accepted \w+ for (\w+) from ([\d.:a-fA-F]+)"

    try:
        with open(file_path, "r") as file:
            for line in file:
                match = re.search(pattern, line)
                if match:
                    timestamp, username, ip = match.groups()
                    accepted[ip].append((timestamp, username))
    except FileNotFoundError:
        print(f"❌ Log file '{file_path}' not found.")

    return accepted

