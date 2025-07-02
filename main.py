import sys
from fetch_logs import fetch_logs
from parse_logs import parse_logs
from display_results import display_results
from export_csv import export_to_csv
from plot_chart import generate_bar_chart
from geoip_lookup import lookup_ip_geolocation
from accepted_logins import parse_accepted_logins
from heatmap import generate_heatmap

if __name__ == "__main__":
    # Use command-line argument if provided
    minutes = sys.argv[1] if len(sys.argv) > 1 else 15

    if fetch_logs(minutes):
        attempts = parse_logs()
        enriched = lookup_ip_geolocation(attempts)
        display_results(enriched)
        export_to_csv(enriched)
        generate_bar_chart(attempts)
        generate_heatmap(enriched)
        accepted_logins= parse_accepted_logins()
        if accepted_logins:
            print("\n🟢 Accepted SSH Logins:")
            for ip, records in accepted_logins.items():
                print(f"[{ip}] — {len(records)} login(s)")
                for timestamp, user, method, port in records:
                    print(f"   └─ {timestamp} → user: {user} (method: {method}, port: {port})")
                print()
        else:
            print("🔴 No accepted SSH logins found.")
        print("✅ Detection completed successfully.")
    else:
        print("❌ Could not complete detection.")
