import folium
from folium.plugins import HeatMap
import os

def generate_heatmap(enriched_data, output_file="attack_heatmap.html"):
    heat_data = []
    m = folium.Map(location=[20, 0], zoom_start=2, tiles="CartoDB dark_matter")

    for ip, info in enriched_data.items():
        lat = info.get("lat")
        lon = info.get("lon")
        count = len(info.get("records", []))
        location = info.get("location", "Unknown")

        if lat is not None and lon is not None:
            heat_data.append([lat, lon, count])

            # Create tooltip content
            usernames = list(set(username for _, username, _ in info["records"]))
            tooltip = f"""
            <b>IP:</b> {ip}<br>
            <b>Location:</b> {location}<br>
            <b>Attempts:</b> {count}<br>
            <b>Usernames:</b> {', '.join(usernames)[:100]}...
            """
            folium.Marker(
                location=[lat, lon],
                popup=folium.Popup(tooltip, max_width=300),
                icon=folium.Icon(color="red", icon="info-sign")
            ).add_to(m)

    if not heat_data:
        print("No valid geolocation data to plot.")
        return

    HeatMap(heat_data, radius=15, blur=20, max_zoom=5).add_to(m)
    m.save(output_file)
    print(f"🗺️ Heatmap saved to: {os.path.abspath(output_file)}")
