from flask import Flask, render_template, request
import subprocess
import os
import sys

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    report = None
    chart = None
    heatmap = None
    csv_report = None

    if request.method == "POST":
        minutes = request.form.get("minutes", "1440")

        try:
            subprocess.run(["python3", "main.py", minutes], check=True)
            report = f"SSH analysis for last {minutes} minutes completed successfully."

            # Check and link output files
            if os.path.exists("static/chart.png"):
                chart = "chart.png"
            if os.path.exists("static/attack_heatmap.html"):
                heatmap = "attack_heatmap.html"
            if os.path.exists("static/report.csv"):
                csv_report = "report.csv"

        except subprocess.CalledProcessError as e:
            report = f"Error running analysis: {e}"

    return render_template("index.html", message=report, chart=chart, heatmap=heatmap, csv_report=csv_report)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
