def display_results(attempts):
    """
    Display formatted output for the failed login attempts.
    """
    if not attempts:
        print("\n✅ No failed login attempts found.")
    else:
        print("\n🚨 Failed Login Attempts Report:\n")
        for ip, records in attempts.items():
            print(f"[{ip}] — {len(records)} attempt(s)")
            for timestamp, user in records:
                print(f"   └─ {timestamp} → user: {user}")
            print()