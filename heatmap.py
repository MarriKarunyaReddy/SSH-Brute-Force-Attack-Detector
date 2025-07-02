import folium
from folium.plugins import HeatMap
import os

def generate_heatmap(enriched_data, output_file="attack_heatmap.html"):
    heat_data = []
    for ip, info in enriched_data.items():
        lat = info.get("lat")
        lon = info.get("lon")
        count = len(info.get("records", []))

        if lat is not None and lon is not None:
            # Add weighted point
            heat_data.append([lat, lon, count])

    if not heat_data:
        print("No valid geolocation data to plot.")
        return

    # Initialize the map
    m = folium.Map(location=[20, 0], zoom_start=2, tiles="CartoDB dark_matter")

    # Add heat map layer
    HeatMap(heat_data, radius=12, blur=15, max_zoom=5).add_to(m)

    # Save map to file
    m.save(output_file)
    print(f"🗺️ Heatmap saved to: {os.path.abspath(output_file)}")
