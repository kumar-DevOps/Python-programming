# CPU Health Monitoring Script 🖥️

A Python program to monitor the CPU usage of the local machine.  
Useful for **DevOps engineers** to track server health and performance.

---

## Features
- ✅ Continuously monitors CPU usage
- ✅ Alerts when usage exceeds a predefined threshold (default: 80%)
- ✅ Runs indefinitely until interrupted
- ✅ Handles errors gracefully

---

## Requirements
- Python 3.x
- `psutil` library

Install `psutil`:
```bash
pip install psutil

Example Output
Monitoring CPU usage... Press Ctrl+C to stop.
CPU usage: 25%
CPU usage: 30%
Alert! CPU usage exceeds threshold: 85%
Alert! CPU usage exceeds threshold: 90%
CPU usage: 45%

