import matplotlib.pyplot as plt
from collections import defaultdict


def generate_bar_chart(attempts, output_path="static/chart.png"):
    """
    Generate a bar chart from failed login attempts.
    :param attempts: Dictionary with IP as key, list of (timestamp, username) tuples as value
    :param output_path: Path to save the chart image
    """
    ip_attempts = defaultdict(int)
    for ip, records in attempts.items():
        ip_attempts[ip] += len(records)

    if not ip_attempts:
        print("ℹ️ No data to generate chart.")
        return

    ips = list(ip_attempts.keys())
    counts = list(ip_attempts.values())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(ips, counts, color="salmon")
    plt.xlabel("IP Address")
    plt.ylabel("Number of Failed Attempts")
    plt.title("Failed SSH Login Attempts per IP")
    plt.xticks(rotation=45, ha="right")

    # Annotate bars with values
    for bar, count in zip(bars, counts):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(count),
                 ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"📊 Bar chart saved as {output_path}")