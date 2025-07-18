# SSH Sentinel 🔐📊

**SSH Sentinel** is a Python-based real-time SSH brute-force detection system. It analyzes system logs for failed login attempts, enriches the data with IP geolocation info, generates CSV reports, and visualizes attacks using a heatmap and dashboard.

---

# 📊 SSH Brute-Force Attack – Sample Raw CSV Data

This repository contains a **sample CSV data file** generated from logs collected by running a deliberately exposed Linux server (EC2 instance) for **~3 days**. It was part of a cybersecurity project: **SSH Sentinel**, focused on detecting and visualizing SSH brute-force attacks.

## 📁 File Contents

The raw CSV data includes:

- IP Address  
- Geo Location (Country, Region, City)  
- Latitude & Longitude  
- ISP / Organization  
- Timestamp of Attempt  
- Attempted Username  
- Login Method (password/publickey)  
- Valid or Invalid Attempt

---

## 🔗 Download Link

📄 **[Click here to view the raw CSV file (Google Drive)](https://drive.google.com/file/d/1K8DhDmLgFhAPaauZa7_MOeNqfFwBNOGd/view?usp=drive_link)**

---

## 💡 Use Cases

You can use this data for:

- SSH Brute-force pattern analysis  
- IP-based threat enrichment  
- Security dashboards and log monitoring practice  
- Cybersecurity student training  
- Geolocation visualization (heatmaps, clustering)

---

## 🛡️ Disclaimer

This data was collected in a **controlled, intentionally vulnerable environment** for educational and research purposes only. Do **not** replicate this without proper safeguards in place.

---

## 🔗 Related Project

Check out the full project: [SSH Sentinel - Attack Detection & Visualization Dashboard](https://github.com/your-github/SSH-Sentinel)

---

## 🚀 Features

- Parses failed SSH login attempts from system logs
- Groups attempts by source IP
- Enriches IPs with geolocation data using ip-api
- Generates:
  - 📄 CSV report
  - 📊 Bar chart of attacker attempts
  - 🌍 Heatmap of attacker origins
- Web-based dashboard to trigger analysis

---

## 📁 Project Structure

```
SSH-Sentinel/
├── main.py                     # Master script coordinating everything
├── app.py                      # Flask dashboard backend
├── templates/
│   └── index.html              # HTML UI for dashboard
├── static/
│   ├── chart.png               # Bar chart output
│   ├── attack_heatmap.html     # Interactive heatmap
│   └── report.csv              # CSV of attacker data
├── fetch_logs.py               # Fetch SSH logs from journalctl
├── parse_logs.py               # Parse failed SSH login attempts
├── geoip_lookup.py             # Enrich with IP geolocation info
├── display_results.py          # Print structured results
├── export_csv.py               # Export data to CSV
├── plot_chart.py               # Generate matplotlib bar chart
├── accepted_logins.py          # Parse accepted login entries
├── requirements.txt
└── README.md
```

---

## ⚙️ Requirements

- Python 3.8+
- pip
- Access to `journalctl` (Linux systems using `systemd`)

Python libraries:

```
flask
matplotlib
requests
folium
```

Install them using:

```
pip install -r requirements.txt
```

---

## 🔧 Setup

1. Clone this repository:
   ```
   git clone https://github.com/MarriKarunyaReddy/SSH-Sentinel.git
   cd ssh-sentinel
   ```

2. (Optional) Create a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

---

## 🧪 Usage (CLI)

To run detection for the past 1440 minutes (24 hours):

```
python3 main.py 1440
```

This will:

- Fetch and parse SSH logs
- Group and enrich attack attempts by IP
- Print structured report
- Generate:
  - `static/chart.png`
  - `static/attack_heatmap.html`
  - `static/report.csv`

---

## 🌐 Web Dashboard

To launch the Flask dashboard:

```
python3 app.py
```

Then open your browser and go to:  
`http://localhost:5000`

From there you can:

- Enter a custom duration (in minutes)
- Trigger analysis
- View:
  - Heatmap
  - Bar Chart
  - Download CSV

---

## 🔒 Harden Your Server (Optional)

If you're using this on a real server:

1. Disable password SSH logins:  # Reccomended if youre just collecting attack data 
   Edit `/etc/ssh/sshd_config`: 

   ```
   PasswordAuthentication no
   ```

2. Restart SSH:
   ```
   sudo systemctl restart sshd
   ```

3. Make sure your public key is set up in `~/.ssh/authorized_keys` on the server.

Now only public key authentication is allowed, protecting you from password brute-force attacks.

---

## 📌 Notes

- Uses `journalctl -u ssh` to fetch SSH logs.
- Geolocation lookup uses `http://ip-api.com/json`.
- For local testing (e.g., Ngrok), loopback IPs like `127.0.0.1` are labeled as "Ngrok Tunnel".

---

## 🧠 Credits

Built by Marri Karunya Reddy  
License: MIT

---

## 🛠️ To Do

- Add real-time monitoring via watchdog or cron
- Support for multiple Linux distros (non-systemd)
- Email alerts for high-volume attack patterns
