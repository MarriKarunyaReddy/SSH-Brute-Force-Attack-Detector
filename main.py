import sys
from fetch_logs import fetch_logs
from parse_logs import parse_logs
from display_results import display_results
from export_csv import export_to_csv
from plot_chart import generate_bar_chart

if __name__ == "__main__":
    # Use command-line argument if provided
    minutes = sys.argv[1] if len(sys.argv) > 1 else 15

    if fetch_logs(minutes):
        attempts = parse_logs()
        display_results(attempts)
        export_to_csv(attempts)
        generate_bar_chart(attempts)
        print("✅ Detection completed successfully.")
    else:
        print("❌ Could not complete detection.")