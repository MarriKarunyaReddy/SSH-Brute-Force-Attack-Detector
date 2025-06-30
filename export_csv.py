import csv
from datetime import datetime

def export_to_csv(attempts, filename="report.csv"):
    """
    Export parsed login attempts to a CSV file.
    Columns: Timestamp, Username, IP Address
    """
    if not attempts:
        print("📭 No data to export.")
        return

    try:
        with open(filename, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Timestamp", "Username", "IP Address"])

            for ip, records in attempts.items():
                for timestamp, username in records:
                    writer.writerow([timestamp, username, ip])

        print(f"📄 Exported report to {filename}")
    except Exception as e:
        print(f"❌ Failed to export CSV: {e}")
