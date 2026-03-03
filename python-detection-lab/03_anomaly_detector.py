log_file        = "python-detection-lab/sample_logs.txt"
ALERT_THRESHOLD = 5

failure_counts = {}

with open(log_file, 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue    

        parts = line.split("|")
        status = parts[1].strip()  
        user = parts[2].strip().replace("User: ", "") 
        ip = parts[3].strip().replace("IP: ", "")

        if status == "FAILURE":
            if user in failure_counts:
                failure_counts[user] += 1   
            else:
                failure_counts[user] = 1

print("[*] Running anomaly detection...")
print(f"[*] Alert threshold: {ALERT_THRESHOLD}+ failed attempts") 
print("-" * 60)

alerts_triggered = 0

for user, count in failure_counts.items():
    if count >= ALERT_THRESHOLD:
        print(f"🚨 ALERT: {user} has {count} failed login attempt(s)")
        alerts_triggered += 1
    else:
        print(f"  ✅ OK:    {user} has {count} failed login attempt(s)")

print("-" * 60)
print(f"[*] Alerts triggered: {alerts_triggered}")