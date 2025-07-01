import csv

def export_to_csv(enriched_attempts, filename="report.csv"):
    """
    Export enriched login attempts to a CSV file.
    Columns: Timestamp, Username, IP Address, IsInvalidUser, Location
    """
    if not enriched_attempts:
        print("📭 No data to export.")
        return

    try:
        with open(filename, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Timestamp", "Username", "IP Address", "IsInvalidUser", "Location"])

            for ip, data in enriched_attempts.items():
                location = data.get("location", "Unknown")
                for record in data.get("records", []):
                    if isinstance(record, (list, tuple)):
                        if len(record) == 3:
                            timestamp, username, is_invalid = record
                        elif len(record) == 2:
                            timestamp, username = record
                            is_invalid = "Unknown"
                        else:
                            continue  
                        writer.writerow([timestamp, username, ip, is_invalid, location])
                    else:
                        continue  

        print(f"📄 Exported report to {filename}")
    except Exception as e:
        print(f"❌ Failed to export CSV: {e}")
