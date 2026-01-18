import psutil
import time

def monitor_cpu(threshold: int = 80, interval: int = 1):
    """
    Continuously monitor CPU usage.
    - threshold: CPU usage percentage to trigger alert (default 80%)
    - interval: time in seconds between checks (default 1s)
    """
    print("Monitoring CPU usage... Press Ctrl+C to stop.")
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=interval)
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
            else:
                print(f"CPU usage: {cpu_usage}%")
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"⚠️ Error occurred while monitoring CPU: {e}")


if __name__ == "__main__":
    # You can adjust threshold and interval here
    monitor_cpu(threshold=80, interval=1)
