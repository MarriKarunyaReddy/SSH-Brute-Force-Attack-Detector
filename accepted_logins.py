import re
from collections import defaultdict

def parse_accepted_logins(file_path="auth_log.txt"):
    """
    Parses log file for successful SSH logins, extracting:
    - timestamp
    - username
    - source IP
    - method used (password/publickey)
    - client port number
    Returns a dictionary: {IP: [(timestamp, username, method, port), ...]}
    """
    accepted = defaultdict(list)
    # Regex: timestamp, method, username, IP, port
    pattern = r"^(\w+\s+\d+\s+\d+:\d+:\d+).*Accepted (\w+) for ([^\s]+) from ([\d.:a-fA-F]+) port (\d+)"

    try:
        with open(file_path, "r") as file:
            for line in file:
                match = re.search(pattern, line)
                if match:
                    timestamp, method, username, ip, port = match.groups()
                    accepted[ip].append((timestamp, username, method, port))
    except FileNotFoundError:
        print(f"❌ Log file '{file_path}' not found.")

    return accepted
