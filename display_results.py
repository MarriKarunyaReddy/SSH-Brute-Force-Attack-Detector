def display_results(enriched_attempts):
    """
    Display formatted output for failed login attempts with geolocation info.
    """
    if not enriched_attempts:
        print("\n✅ No failed login attempts found.")
    else:
        print("\n🚨 Failed Login Attempts Report (with Geolocation):\n")
        for ip, data in enriched_attempts.items():
            location = data.get("location", "Unknown")
            records = data.get("records", [])
            print(f"[{ip}] — {location} — {len(records)} attempt(s)")
            for timestamp, user in records:
                print(f"   └─ {timestamp} → user: {user}")
            print()