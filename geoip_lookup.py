import requests
import time

def lookup_ip_geolocation(attempts):
    """
    Enrich the attempts dictionary with geolocation info per IP.
    Returns: { ip: { 'location': 'Country (Region)', 'records': [(timestamp, username), ...] } }
    """
    enriched = {}

    for ip, records in attempts.items():
        if ip.startswith("192.168.") or ip.startswith("10.") or ip.startswith("172."):
            location = "Private IP (Local Network)"
        elif ip == "::1" or ip == "127.0.0.1":
            location = "Loopback (Localhost) / Ngrok Tunnel"
        else:
            try:
                print(f"🌐 Looking up geolocation for {ip}...")
                response = requests.get(f"https://ipapi.co/{ip}/json/", timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    country = data.get("country_name", "Unknown")
                    region = data.get("region", "")
                    location = f"{country} ({region})" if region else country
                else:
                    location = "Unknown"
            except requests.RequestException:
                location = "Unknown"

        enriched[ip] = {
            "location": location,
            "records": records
        }

        time.sleep(1)  # Avoid hitting API too fast

    return enriched