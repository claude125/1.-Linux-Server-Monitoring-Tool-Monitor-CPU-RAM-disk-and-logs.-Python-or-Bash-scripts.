<div align="center">

![header](https://capsule-render.vercel.app/api?type=waving&color=0:030712,50:0d1f0d,100:39ff14&height=200&section=header&text=Linux%20Server%20Monitor&fontSize=44&fontColor=ffffff&fontAlignY=38&desc=Lightweight%20Real-Time%20System%20Resource%20Monitoring%20Tool&descSize=15&descAlignY=58&animation=fadeIn)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=14&pause=1500&color=39FF14&center=true&vCenter=true&width=750&height=40&lines=🖥️+Real-Time+CPU+%2F+Memory+%2F+Disk+Monitoring;⚡+Instant+Threshold+Alerts+for+SysAdmins;📋+System+Log+Error+Detection;🐍+Python+%2B+psutil+%2B+Bash+Powered;🛡️+Catch+Issues+Before+They+Become+Outages)](https://git.io/typing-svg)

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![psutil](https://img.shields.io/badge/psutil-Monitoring-39ff14?style=for-the-badge&logoColor=black)
![CLI](https://img.shields.io/badge/CLI-Tool-0d1117?style=for-the-badge&logo=windowsterminal&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</div>

---

## 🖥️ What Is This?

A **lightweight, zero-bloat monitoring tool** for Linux servers. No heavy dashboards, no cloud dependencies — just a clean Python script that tells you exactly what your server is doing, and warns you before things go wrong.

Built for **system administrators** who want fast, reliable visibility into server health directly from the terminal.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔲 **CPU Monitoring** | Real-time CPU utilization per core and overall |
| 🧠 **Memory Monitoring** | RAM usage, available memory, and swap stats |
| 💾 **Disk Monitoring** | Disk usage per partition with free space alerts |
| ⏱️ **Uptime Tracking** | Server uptime displayed in days / hours / minutes |
| 📋 **Log Analysis** | Scans system logs for errors and warnings |
| 🚨 **Threshold Alerts** | Configurable alerts when resources exceed safe limits |
| 💻 **CLI Interface** | Lightweight terminal interface, no GUI required |

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/claude125/linux-server-monitoring-tool.git
cd linux-server-monitoring-tool

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the monitor
python monitor.py
```

---

## 📊 Example Output

```
╔══════════════════════════════════════════════════════╗
║          LINUX SERVER MONITOR  v1.0                  ║
║          2025-03-13  |  14:32:07  UTC+2              ║
╠══════════════════════════════════════════════════════╣
║  🔲 CPU Usage        ████████░░░░░░░░   52.4%        ║
║  🧠 Memory (RAM)     ██████████████░░   87.1%  ⚠️    ║
║  💾 Disk  /          ████████░░░░░░░░   48.3%        ║
║  💾 Disk  /var       ██████████████░░   89.0%  ⚠️    ║
║  ⏱️  Uptime           14 days, 6 hrs, 22 min          ║
╠══════════════════════════════════════════════════════╣
║  📋 Recent Log Errors                                ║
║  [ERROR]  kernel: Out of memory — 14:28:03           ║
║  [WARN ]  sshd: Failed password — 192.168.1.45       ║
╠══════════════════════════════════════════════════════╣
║  🚨 ALERTS                                           ║
║  [!] Memory usage above threshold  (87.1% > 85%)     ║
║  [!] Disk /var usage critical      (89.0% > 85%)     ║
╚══════════════════════════════════════════════════════╝
```

---

## ⚙️ Configuration

Set your own alert thresholds inside `monitor.py`:

```python
# Alert thresholds (percentage)
THRESHOLDS = {
    "cpu"    : 80,   # Alert if CPU  > 80%
    "memory" : 85,   # Alert if RAM  > 85%
    "disk"   : 85,   # Alert if Disk > 85%
}
```

---

## 🧰 Tech Stack

```bash
$ cat requirements.txt
```

```
psutil          # Cross-platform system resource monitoring
subprocess      # Bash command execution from Python
datetime        # Uptime and timestamp formatting
os / sys        # Low-level Linux system interaction
```

---

## 📁 Project Structure

```
linux-server-monitoring-tool/
│
├── 📄 monitor.py          # Main monitoring script
├── 📄 requirements.txt    # Python dependencies
└── 📄 README.md
```

---

## 🌍 Use Cases

`🖥️ VPS Servers` &nbsp; `☁️ Cloud Instances` &nbsp; `🏢 On-Premise Servers` &nbsp; `🔒 Security Monitoring` &nbsp; `🧪 Dev Environments`

---

## 🚀 Roadmap

```python
roadmap = [
    "📧 Email & Slack alert notifications",
    "📈 Historical metrics logging to CSV / SQLite",
    "🌐 Web dashboard for remote browser monitoring",
    "🐳 Docker container resource monitoring",
    "⏰ Cron-based scheduled monitoring reports",
    "🔔 Systemd service for always-on background monitoring",
]
```

---

## 👤 Author

<div align="center">

**Claude Dusengimana**
*Senior Network & Security Engineer | IoT Researcher*
📍 Kigali, Rwanda

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/dusengimana-claude)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-161b22?style=for-the-badge&logo=github&logoColor=white)](https://github.com/claude125)
[![Gmail](https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:dusenge125@gmail.com)

</div>

---

<div align="center">

![footer](https://capsule-render.vercel.app/api?type=waving&color=0:39ff14,50:0d1f0d,100:030712&height=100&section=footer&text=Monitor+everything.+Miss+nothing.&fontSize=14&fontColor=ffffff&fontAlignY=65&animation=fadeIn)

*⭐ Star this repo if it saved your server — or your sleep.*

</div>
