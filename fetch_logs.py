import subprocess
import sys

def detect_ssh_unit():
    """
    Detects whether the SSH service is named 'ssh' or 'sshd'.
    """
    try:
        output = subprocess.check_output(["systemctl", "list-units", "--type=service"], text=True)
        if "ssh.service" in output:
            return "ssh"
        elif "sshd.service" in output:
            return "sshd"
    except subprocess.SubprocessError:
        pass
    return "ssh"  # Fallback default

def fetch_logs(minutes=15):
    """
    Fetch SSH logs from journalctl within the past `minutes` and write to auth_log.txt.
    """
    try:
        minutes = int(minutes)
        print(f"\n📥 Fetching SSH logs from the last {minutes} minute(s)...")

        unit = detect_ssh_unit()
        print(f"🔍 Detected SSH unit: {unit}")

        with open("auth_log.txt", "w") as f:
            subprocess.run(
                ["sudo", "journalctl", "-u", unit, f"--since={minutes} minutes ago"],
                stdout=f,
                stderr=subprocess.DEVNULL,
                check=True
            )
        return True

    except ValueError:
        print("❌ Invalid input. Use an integer for minutes.")
        return False
    except subprocess.CalledProcessError:
        print("❌ Failed to fetch logs. Are you running with sudo on a systemd-based distro?")
        return False
