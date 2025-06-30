import subprocess
import sys

def fetch_logs(minutes=15):
    """
    Fetch SSH logs from journalctl within the past `minutes` and write to auth_log.txt.
    """
    try:
        minutes = int(minutes)
        print(f"\n📥 Fetching SSH logs from the last {minutes} minute(s)...")
        with open("auth_log.txt", "w") as f:
            subprocess.run(
                ["sudo", "journalctl", "-u", "ssh", f"--since={minutes} minutes ago"],
                stdout=f,
                stderr=subprocess.DEVNULL,
                check=True
            )
        return True
    except ValueError:
        print("❌ Invalid input. Use an integer for minutes.")
        return False
    except subprocess.CalledProcessError:
        print("❌ Failed to fetch logs. Are you running this on Kali with sudo access?")
        return False