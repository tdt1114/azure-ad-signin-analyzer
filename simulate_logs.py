from datetime import datetime, timezone
import json

# Simulated sign-in log data
simulated_logs = {
    "value": [
        # Normal logins
        {
            "userPrincipalName": "jsmith@lab.local",
            "status": {"errorCode": 0},
            "createdDateTime": "2026-02-28T09:15:00Z",
            "ipAddress": "192.168.1.10"
        },
        {
            "userPrincipalName": "mjones@lab.local",
            "status": {"errorCode": 0},
            "createdDateTime": "2026-02-28T08:45:00Z",
            "ipAddress": "192.168.1.11"
        },
        # Failed logins - threshold trigger
        {
            "userPrincipalName": "bwilliams@lab.local",
            "status": {"errorCode": 50126},
            "createdDateTime": "2026-02-28T10:02:00Z",
            "ipAddress": "192.168.1.15"
        },
        {
            "userPrincipalName": "bwilliams@lab.local",
            "status": {"errorCode": 50126},
            "createdDateTime": "2026-02-28T10:03:00Z",
            "ipAddress": "192.168.1.15"
        },
        {
            "userPrincipalName": "bwilliams@lab.local",
            "status": {"errorCode": 50126},
            "createdDateTime": "2026-02-28T10:04:00Z",
            "ipAddress": "192.168.1.15"
        },
        {
            "userPrincipalName": "bwilliams@lab.local",
            "status": {"errorCode": 50126},
            "createdDateTime": "2026-02-28T10:05:00Z",
            "ipAddress": "192.168.1.15"
        },
        # Off hours logins
        {
            "userPrincipalName": "agreen@lab.local",
            "status": {"errorCode": 0},
            "createdDateTime": "2026-02-28T02:34:00Z",
            "ipAddress": "192.168.1.22"
        },
        {
            "userPrincipalName": "agreen@lab.local",
            "status": {"errorCode": 0},
            "createdDateTime": "2026-02-28T03:12:00Z",
            "ipAddress": "192.168.1.22"
        },
        # Both failed AND off hours
        {
            "userPrincipalName": "rthomas@lab.local",
            "status": {"errorCode": 50126},
            "createdDateTime": "2026-02-28T23:45:00Z",
            "ipAddress": "10.0.0.55"
        },
        {
            "userPrincipalName": "rthomas@lab.local",
            "status": {"errorCode": 50126},
            "createdDateTime": "2026-02-28T23:47:00Z",
            "ipAddress": "10.0.0.55"
        },
        {
            "userPrincipalName": "rthomas@lab.local",
            "status": {"errorCode": 50126},
            "createdDateTime": "2026-02-28T23:51:00Z",
            "ipAddress": "10.0.0.55"
        },
    ]
}

def analyze_logs(logs):
    failed_logins = {}
    off_hours = []

    for entry in logs.get("value", []):
        user = entry.get("userPrincipalName", "Unknown")
        status = entry.get("status", {})
        error_code = status.get("errorCode", 0)
        time_str = entry.get("createdDateTime", "")
        ip = entry.get("ipAddress", "Unknown")

        if error_code != 0:
            if user not in failed_logins:
                failed_logins[user] = {"count": 0, "ip": ip}
            failed_logins[user]["count"] += 1

        if time_str:
            time = datetime.fromisoformat(time_str.replace("Z", "+00:00"))
            hour = time.astimezone().hour
            if hour < 6 or hour > 22:
                off_hours.append({
                    "user": user,
                    "time": time_str,
                    "hour": hour,
                    "ip": ip
                })

    return failed_logins, off_hours

def print_report(failed_logins, off_hours):
    print("\n========== SIGN-IN LOG ANALYSIS ==========\n")

    print("--- Failed Login Attempts ---")
    if failed_logins:
        for user, data in sorted(failed_logins.items(), key=lambda x: x[1]["count"], reverse=True):
            flag = " ⚠️  HIGH" if data["count"] >= 3 else ""
            print(f"  {user}: {data['count']} failed attempt(s) from {data['ip']}{flag}")
    else:
        print("  No failed logins detected.")

    print("\n--- Off-Hours Authentication ---")
    if off_hours:
        for entry in off_hours:
            print(f"  {entry['user']} logged in at hour {entry['hour']} from {entry['ip']} ({entry['time']})")
    else:
        print("  No off-hours logins detected.")

    # Cross reference - users that appear in both
    print("\n--- ⚠️  High Priority - Failed AND Off-Hours ---")
    failed_users = set(failed_logins.keys())
    offhours_users = set(e["user"] for e in off_hours)
    overlap = failed_users & offhours_users
    if overlap:
        for user in overlap:
            print(f"  🚨 {user} — multiple failed logins AND off-hours activity detected")
    else:
        print("  None detected.")

    print("\n==========================================\n")

if __name__ == "__main__":
    print("Running analysis on simulated sign-in logs...\n")
    failed, offhours = analyze_logs(simulated_logs)
    print_report(failed, offhours)