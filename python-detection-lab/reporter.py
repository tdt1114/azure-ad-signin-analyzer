from config import *
import datetime

def generate_report(alerts, ip_map):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(REPORT_FILE, 'w') as r:
        r.write("=" * 60 + "\n")
        r.write(" INCIDENT REPORT - BRUTE FORCE DETECTION\n")
        r.write("=" * 60 + "\n")
        r.write(f"Generated on: {now}\n")
        r.write(f"Log Source  : {LOG_FILE}\n")
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

    print(f"[*] Report saved to: {REPORT_FILE}")
    print("[*] Open incident_report.txt in VS Code to review.")