from config import *

def detect_anomalies(events, threshold=ALERT_THRESHOLD):
    failure_counts = {}
    ip_map = {}

    for event in events:
        if event["status"] == "FAILURE":
            user = event["user"]
            failure_counts[user] = failure_counts.get(user, 0) + 1
            ip_map[user] = event["ip"]

    print("[*] Running anomaly detection...")
    print(f"[*] Alert threshold: {threshold}+ failed attempts")
    print("-" * 60)

    alerts_triggered = 0
    alerts = {}

    for user, count in failure_counts.items():
        if count >= threshold:
            print(f"🚨 ALERT: {user} has {count} failed login attempt(s)")
            alerts_triggered += 1
            alerts[user] = count
        else:
            print(f"  ✅ OK:    {user} has {count} failed login attempt(s)")

    print("-" * 60)
    print(f"[*] Alerts triggered: {alerts_triggered}")

    return alerts, ip_map