import requests
import time

def lookup_ip_geolocation(attempts):
    """
    Enrich login attempts with detailed geolocation info.
    Returns: {
        ip: {
            'location': 'Country (Region, City)',
            'lat': float,
            'lon': float,
            'org': str,
            'isp': str,
            'as': str,
            'timezone': str,
            'records': [(timestamp, username, is_invalid)]
        }
    }
    """
    enriched = {}

    for ip, records in attempts.items():
        if ip.startswith("192.168.") or ip.startswith("10.") or ip.startswith("172."):
            location = "Private IP (Local Network)"
            enriched[ip] = {
                "location": location,
                "lat": None,
                "lon": None,
                "org": None,
                "isp": None,
                "as": None,
                "timezone": None,
                "records": records
            }
            continue

        if ip == "::1" or ip == "127.0.0.1":
            location = "Loopback (Localhost) / Ngrok Tunnel"
            enriched[ip] = {
                "location": location,
                "lat": None,
                "lon": None,
                "org": None,
                "isp": None,
                "as": None,
                "timezone": None,
                "records": records
            }
            continue

        try:
            print(f"🌐 Looking up geolocation for {ip}...")
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
            if response.status_code == 200:
                data = response.json()
                location = f"{data.get('country', 'Unknown')} ({data.get('regionName', '')}, {data.get('city', '')})"
                enriched[ip] = {
                    "location": location,
                    "lat": data.get("lat"),
                    "lon": data.get("lon"),
                    "org": data.get("org"),
                    "isp": data.get("isp"),
                    "as": data.get("as"),
                    "timezone": data.get("timezone"),
                    "records": records
                }
            else:
                enriched[ip] = {
                    "location": "Unknown",
                    "lat": None,
                    "lon": None,
                    "org": None,
                    "isp": None,
                    "as": None,
                    "timezone": None,
                    "records": records
                }
        except requests.RequestException:
            enriched[ip] = {
                "location": "Lookup failed",
                "lat": None,
                "lon": None,
                "org": None,
                "isp": None,
                "as": None,
                "timezone": None,
                "records": records
            }

        time.sleep(1)

    return enriched
