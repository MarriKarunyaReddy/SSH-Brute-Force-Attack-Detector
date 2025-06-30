import sys
from fetch_logs import fetch_logs
from parse_logs import parse_logs
from display_results import display_results

if __name__ == "__main__":
    # Use command-line argument if provided
    minutes = sys.argv[1] if len(sys.argv) > 1 else 15

    if fetch_logs(minutes):
        attempts = parse_logs()
        display_results(attempts)
    else:
        print("❌ Could not complete detection.")