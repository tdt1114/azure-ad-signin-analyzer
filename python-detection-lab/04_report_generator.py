import datetime

log_file        = "python-detection-lab/sample_logs.txt"
ALERT_THRESHOLD = 5
report_file     = "python-detection-lab/incident_report.txt" 

failure_counts  = {}
ip_map          = {} 

with open(log_file, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue   

        parts = line.split(" | ")
        status = parts[1].strip()  
        user = parts[2].strip().replace("User: ", "") 
        ip = parts[3].strip().replace("IP: ", "")

        if status == "FAILURE":
            failure_counts[user] = failure_counts.get(user, 0) + 1
            ip_map[user] = ip

alerts = {user: count for user, count in failure_counts.items() if count >= ALERT_THRESHOLD}

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(report_file, 'w') as r:
    r.write("=" * 60 + "\n")
    r.write(" INCIDENT REPORT - BRUTE FORCE DETECTION\n")
    r.write("=" * 60 + "\n")
    r.write(f"Generated on: {now}\n")
    r.write(f"Log Source  : {log_file}\n")
    r.write(f"Threshold   : {ALERT_THRESHOLD}+ failures\n")
    r.write(f"Alerts Found: {len(alerts)}\n")
    r.write("-" * 60 + "\n")

    if alerts:
        r.write("SUSPICIOUS ACCOUNTS:\n\n")
        for user, count in alerts.items():
         r.write(f"  Account  : {user}\n")
         r.write(f"  Source IP: {ip_map.get(user, 'Unknown')}\n")
         r.write(f"  Failures : {count}\n")
         r.write(f"  Action   : Investigate account. Consider blocking {ip_map.get(user)}.\n")
         r.write("\n")

    else:
        r.write("No suspicious activity detected above threshold.\n")

    r.write("=" * 60 + "\n")
    r.write("END OF REPORT\n")

print(f"[*] Report saved to: {report_file}")
print("[*] Open incident_report.txt in VS Code to review.")