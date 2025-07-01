import csv

def export_to_csv(enriched_attempts, filename="report.csv"):
    """
    Export enriched login attempts with geolocation details to a CSV file.
    Columns: Timestamp, Username, IP Address, IsInvalidUser, Location, Latitude, Longitude, Organization, ISP, AS, Timezone
    """
    if not enriched_attempts:
        print("📭 No data to export.")
        return

    try:
        with open(filename, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                "Timestamp", "Username", "IP Address", "IsInvalidUser",
                "Location", "Latitude", "Longitude", "Organization",
                "ISP", "AS", "Timezone"
            ])

            for ip, data in enriched_attempts.items():
                location = data.get("location", "Unknown")
                lat = data.get("lat")
                lon = data.get("lon")
                org = data.get("org")
                isp = data.get("isp")
                asn = data.get("as")
                timezone = data.get("timezone")

                for record in data.get("records", []):
                    if len(record) == 3:
                        timestamp, username, is_invalid = record
                    else:
                        timestamp, username = record
                        is_invalid = "Unknown"

                    writer.writerow([
                        timestamp, username, ip, is_invalid,
                        location, lat, lon, org, isp, asn, timezone
                    ])

        print(f"📄 Exported detailed report to {filename}")
    except Exception as e:
        print(f"❌ Failed to export CSV: {e}")
